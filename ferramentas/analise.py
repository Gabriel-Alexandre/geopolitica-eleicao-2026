"""F2, F3 e F6: concordância entre as passadas, taxas-base, teste do passado e os números de interesses.

Uso: python ferramentas/analise.py
Entradas: dados/casos/passada_{a,b}_{1,2}.json, dados/derivados/*.csv, dados/f1 (resultados/f1_resumo.json)
Saídas:   resultados/RESUMO.json e as tabelas de resultados/*.csv
Regras: pré-registro §5 e emendas 2 e 3.
"""
import csv
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CASOS = RAIZ / "dados" / "casos"
DERIVADOS = RAIZ / "dados" / "derivados"
RESULTADOS = RAIZ / "resultados"
POTENCIAS = ["eua", "china", "russia", "ue"]
CAMPOS = [
    "fraude_demonstrada", "observadores", "autoridade_certificou_o_resultado_anunciado", "perdedor_foi_a_justica",
    "eleicao_anulada_ou_refeita", "governo_ou_candidato_paralelo_reconhecido_por_alguma_potencia",
    "eua_sancao_ou_corte_ligado_a_eleicao_em_12_meses", "vencedor_anunciado_tomou_posse",
    "violencia_relevante_depois_da_eleicao",
    "relacao_do_vencedor.eua", "relacao_do_vencedor.china", "relacao_do_vencedor.russia",
    "reacao.eua.tipo", "reacao.china.tipo", "reacao.russia.tipo", "reacao.ue.tipo",
]
CASOS_DO_TESTE = ["brasil-2022", "honduras-2025", "hungria-2026"]


# ---------- leitura e consenso ----------

def ler_passada(letra: str) -> dict:
    casos = {}
    for arquivo in sorted(CASOS.glob(f"passada_{letra}_*.json")):
        for caso in json.loads(arquivo.read_text(encoding="utf-8")):
            casos[caso["caso"]] = caso
    return casos


def pegar(caso: dict, campo: str):
    valor = caso
    for parte in campo.split("."):
        valor = valor.get(parte) if isinstance(valor, dict) else None
    if isinstance(valor, str):
        valor = valor.strip().lower()
        valor = {"aliado": "proximo"}.get(valor, valor)
    return valor


def kappa(pares: list[tuple]) -> float | None:
    """Kappa de Cohen para um campo categórico."""
    if not pares:
        return None
    n = len(pares)
    observado = sum(a == b for a, b in pares) / n
    conta_a = Counter(a for a, _ in pares)
    conta_b = Counter(b for _, b in pares)
    esperado = sum(conta_a[k] * conta_b.get(k, 0) for k in conta_a) / (n * n)
    if esperado == 1:
        return 1.0
    return round((observado - esperado) / (1 - esperado), 3)


def consenso(a: dict, b: dict) -> tuple[dict, list[dict]]:
    """Emenda 2: o que as duas passadas confirmam entra; o que diverge sai daquele campo."""
    linhas_concordancia = []
    juntos = {}
    for campo in CAMPOS:
        pares = []
        for nome in sorted(set(a) & set(b)):
            va, vb = pegar(a[nome], campo), pegar(b[nome], campo)
            if va is not None and vb is not None:
                pares.append((va, vb))
        iguais = sum(x == y for x, y in pares)
        linhas_concordancia.append({"campo": campo, "casos_com_as_duas": len(pares), "iguais": iguais,
                                    "concordancia": round(iguais / len(pares), 3) if pares else None,
                                    "kappa": kappa(pares)})
    for nome in sorted(set(a) & set(b)):
        ca, cb = a[nome], b[nome]
        if not (ca.get("fecha_com_duas_fontes") and cb.get("fecha_com_duas_fontes")):
            juntos[nome] = {"excluido": "não fecha com duas fontes em uma das passadas"}
            continue
        registro = {}
        for campo in CAMPOS:
            va, vb = pegar(ca, campo), pegar(cb, campo)
            registro[campo] = va if (va == vb and va is not None) else ("divergente" if None not in (va, vb) else None)
        for potencia in POTENCIAS:
            da, db = pegar(ca, f"reacao.{potencia}.dias_ate_parabens"), pegar(cb, f"reacao.{potencia}.dias_ate_parabens")
            if isinstance(da, (int, float)) and isinstance(db, (int, float)):
                registro[f"dias.{potencia}"] = (da + db) / 2 if abs(da - db) <= 2 else "divergente"
            else:
                registro[f"dias.{potencia}"] = da if da == db else None
        registro["margem_pontos"] = ca.get("margem_pontos")
        juntos[nome] = registro
    return juntos, linhas_concordancia


# ---------- desfechos binários ----------

def parabens_ate(registro: dict, potencia: str, dias: int):
    tipo, d = registro.get(f"reacao.{potencia}.tipo"), registro.get(f"dias.{potencia}")
    if tipo in (None, "divergente", "nao_se_aplica"):
        return None
    if tipo != "parabens":
        return 0
    if not isinstance(d, (int, float)):
        return None
    return int(d <= dias)


def sim_nao(valor):
    if valor in (True, "true", "sim"):
        return 1
    if valor in (False, "false", "nao", "não"):
        return 0
    return None


DESFECHOS = {
    "eua_parabens_30d": lambda r: parabens_ate(r, "eua", 30),
    "china_parabens_7d": lambda r: parabens_ate(r, "china", 7),
    "russia_parabens_7d": lambda r: parabens_ate(r, "russia", 7),
    "ue_parabens_30d": lambda r: parabens_ate(r, "ue", 30),
    "eua_nao_reconheceu": lambda r: None if r.get("reacao.eua.tipo") in (None, "divergente", "nao_se_aplica")
    else int(r["reacao.eua.tipo"] == "nao_reconheceu"),
    "anulada_ou_refeita": lambda r: sim_nao(r.get("eleicao_anulada_ou_refeita")),
    "vencedor_tomou_posse": lambda r: sim_nao(r.get("vencedor_anunciado_tomou_posse")),
    "eua_sancao_12m": lambda r: sim_nao(r.get("eua_sancao_ou_corte_ligado_a_eleicao_em_12_meses")),
    "violencia": lambda r: sim_nao(r.get("violencia_relevante_depois_da_eleicao")),
}
# o que se sabe na noite do resultado e condiciona cada desfecho (emenda 2)
CONDICAO = {
    "eua_parabens_30d": "relacao_do_vencedor.eua", "eua_nao_reconheceu": "relacao_do_vencedor.eua",
    "eua_sancao_12m": "relacao_do_vencedor.eua", "china_parabens_7d": "relacao_do_vencedor.china",
    "russia_parabens_7d": "relacao_do_vencedor.russia",
}


def taxas_base(casos: dict) -> list[dict]:
    validos = {n: r for n, r in casos.items() if "excluido" not in r}
    linhas = []
    grupos_lente = {"todos": lambda r: True,
                    "fraude não demonstrada (lente L)": lambda r: r.get("fraude_demonstrada") == "nao",
                    "fraude demonstrada ou disputada (lente F)": lambda r: r.get("fraude_demonstrada") in ("sim", "disputado")}
    for desfecho, funcao in DESFECHOS.items():
        for nome_grupo, filtro in grupos_lente.items():
            valores = [(n, funcao(r), r.get(CONDICAO.get(desfecho, ""), None)) for n, r in validos.items() if filtro(r)]
            valores = [(n, v, c) for n, v, c in valores if v is not None]
            if not valores:
                continue
            linhas.append({"desfecho": desfecho, "grupo": nome_grupo, "condicao": "todas",
                           "sim": sum(v for _, v, _ in valores), "n": len(valores),
                           "taxa": round(sum(v for _, v, _ in valores) / len(valores), 3),
                           "casos": ";".join(n for n, _, _ in valores)})
            if desfecho in CONDICAO:
                por_condicao = defaultdict(list)
                for n, v, c in valores:
                    por_condicao[c].append((n, v))
                for c, itens in sorted(por_condicao.items(), key=lambda x: str(x[0])):
                    if c in (None, "divergente"):
                        continue
                    linhas.append({"desfecho": desfecho, "grupo": nome_grupo, "condicao": f"vencedor {c} da potência",
                                   "sim": sum(v for _, v in itens), "n": len(itens),
                                   "taxa": round(sum(v for _, v in itens) / len(itens), 3),
                                   "casos": ";".join(n for n, _ in itens)})
    return linhas


def ano(nome: str) -> int:
    return int(nome.rsplit("-", 1)[1])


def teste_do_passado(casos: dict, so_anteriores: bool = False) -> tuple[list[dict], dict]:
    """Emenda 2: cada caso previsto pela taxa dos outros (deixa-um-de-fora), com a condição conhecida na noite."""
    validos = {n: r for n, r in casos.items() if "excluido" not in r}
    linhas = []
    for nome, registro in validos.items():
        for desfecho, funcao in DESFECHOS.items():
            real = funcao(registro)
            if real is None:
                continue
            chave = CONDICAO.get(desfecho)
            condicao = registro.get(chave) if chave else None
            outros = [funcao(r) for n, r in validos.items() if n != nome
                      and (not so_anteriores or ano(n) < ano(nome))
                      and (chave is None or condicao in (None, "divergente") or r.get(chave) == condicao)]
            outros = [v for v in outros if v is not None]
            previsto = (sum(outros) + 1) / (len(outros) + 2)  # Laplace: sem dado, 50%
            linhas.append({"caso": nome, "desfecho": desfecho, "condicao": condicao or "todas",
                           "previsto": round(previsto, 3), "real": real, "n_outros": len(outros),
                           "brier": round((previsto - real) ** 2, 4), "brier_50": 0.25})
    resumo = {}
    if linhas:
        resumo["brier_metodo"] = round(sum(l["brier"] for l in linhas) / len(linhas), 4)
        resumo["brier_chute_50"] = 0.25
        resumo["previsoes"] = len(linhas)
        for caso in CASOS_DO_TESTE:
            do_caso = [l for l in linhas if l["caso"] == caso]
            if do_caso:
                resumo[caso] = round(sum(l["brier"] for l in do_caso) / len(do_caso), 4)
    return linhas, resumo


def brier_sem_condicionar(casos: dict) -> float:
    """Referência mais dura (pedido do auditor): a taxa geral dos outros casos, sem a relação do vencedor."""
    validos = {n: r for n, r in casos.items() if "excluido" not in r}
    notas = []
    for nome, registro in validos.items():
        for funcao in DESFECHOS.values():
            real = funcao(registro)
            if real is None:
                continue
            outros = [v for v in (funcao(r) for n, r in validos.items() if n != nome) if v is not None]
            previsto = (sum(outros) + 1) / (len(outros) + 2)
            notas.append((previsto - real) ** 2)
    return round(sum(notas) / len(notas), 4)


# ---------- F3 ----------

def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def interesses() -> dict:
    comercio = ler_csv(DERIVADOS / "comercio_brasil.csv")
    valor = {(int(l["ano"]), l["fluxo"], l["parceiro"]): int(l["valor_usd"]) for l in comercio}
    anos = sorted({k[0] for k in valor})
    fatias = {}
    for ano in anos:
        for fluxo in ("exportacao", "importacao"):
            mundo = valor[(ano, fluxo, "Mundo")]
            for parceiro in ("China", "EUA", "Rússia"):
                fatias[f"{ano}|{fluxo}|{parceiro}"] = round(100 * valor[(ano, fluxo, parceiro)] / mundo, 2)
    ultimo = anos[-1]
    saldo_eua = valor[(ultimo, "exportacao", "EUA")] - valor[(ultimo, "importacao", "EUA")]
    saldo_china = valor[(ultimo, "exportacao", "China")] - valor[(ultimo, "importacao", "China")]
    onu = ler_csv(DERIVADOS / "onu_concordancia_brasil.csv")
    concordancia = {f"{l['ano']}|{l['par']}": round(float(l["concordancia"]), 3) for l in onu if l["concordancia"]}
    adubos = ler_csv(DERIVADOS / "adubos_importacao_brasil.csv")
    av = {(int(l["ano"]), l["parceiro"]): int(l["valor_usd"]) for l in adubos}
    adubos_russia = {a: round(100 * av[(a, "Rússia")] / av[(a, "Mundo")], 1) for a in sorted({k[0] for k in av})}
    terras = {l["pais"]: int(l["reservas_t_oxido"]) for l in ler_csv(DERIVADOS / "terras_raras_reservas.csv")}
    return {
        "ultimo_ano_comercio": ultimo,
        "fatias_pct": fatias,
        "saldo_brasil_com_eua_usd_ultimo_ano": saldo_eua,
        "saldo_brasil_com_china_usd_ultimo_ano": saldo_china,
        "onu_concordancia": concordancia,
        "adubos_fatia_russia_pct": adubos_russia,
        "terras_raras_reservas_t": terras,
        "terras_raras_posicao_brasil": sorted(terras, key=terras.get, reverse=True).index("Brasil") + 1,
    }


# ---------- revisão adversarial: o teto das duas pontas e as variantes ----------

DIFERENCA_2026 = 64_256_232 - 59_826_041  # votos do Lula menos votos do Flávio (TSE, 100% apurado)
VOTOS_DEPOIS_17H_G1 = 35_521  # contagem do g1 nos logs (dados/f4_estado_26out.md §4); uma origem só


def teto_das_duas_pontas() -> dict:
    """As duas queixas de procedimento, levadas ao pior caso para cada lado (pedido dos dois revisores)."""
    detalhe = ler_csv(DERIVADOS / "copias" / "uf_detalhe_previsao_segundo_turno.csv")
    abst = lambda ano, turno: sum(int(l["abstencoes"]) for l in detalhe if l["ano"] == str(ano) and l["turno"] == str(turno))  # noqa: E731
    impedidos = {}
    for fatia in (55, 60, 65, 75, 100):
        saldo_por_eleitor = (2 * fatia - 100) / 100  # cada impedido tiraria esse saldo do Flávio
        impedidos[f"{fatia}% para o Flávio"] = round(DIFERENCA_2026 / saldo_por_eleitor)
    return {
        "diferenca_votos": DIFERENCA_2026,
        "votos_acrescentados_necessarios_todos_para_o_lula": DIFERENCA_2026,
        "votos_depois_das_17h_g1": VOTOS_DEPOIS_17H_G1,
        "vezes_que_o_g1_teria_de_estar_errado": round(DIFERENCA_2026 / VOTOS_DEPOIS_17H_G1, 1),
        "eleitores_impedidos_necessarios": impedidos,
        "abstencao_2o_turno_2022": abst(2022, 2),
        "abstencao_1o_turno_2026": abst(2026, 1),
    }


def variantes(casos: dict) -> list[dict]:
    """Objeções que viram conta (docs/REVISAO_ADVERSARIAL.md)."""
    linhas = []
    validos = {n: r for n, r in casos.items() if "excluido" not in r}
    # V1 (defensor da lente F): anulação por irregularidade de procedimento conta na lente L
    base = [n for n, r in validos.items() if r.get("fraude_demonstrada") == "nao" and sim_nao(r.get("eleicao_anulada_ou_refeita")) is not None]
    anuladas_base = [n for n in base if sim_nao(validos[n].get("eleicao_anulada_ou_refeita")) == 1]
    for nome, extra in [("V1a: Quênia 2017 contado como fraude não demonstrada (a Suprema Corte anulou por irregularidade, sem atribuir fraude)", ["quenia-2017"]),
                        ("V1b: Quênia 2017 e Malaui 2019 contados como fraude não demonstrada", ["quenia-2017", "malaui-2019"])]:
        extras = [n for n in extra if n not in base]
        anuladas = anuladas_base + [n for n in extras]  # os dois foram anulados
        linhas.append({"variante": nome, "desfecho": "anulada_ou_refeita (lente L)",
                       "principal": f"{len(anuladas_base)} de {len(base)}", "variante_valor": f"{len(anuladas)} de {len(base) + len(extras)}"})
    # V3 (auditor): a lente F do histórico junta fraude demonstrada e fraude disputada; aqui separadas
    for desfecho in ("anulada_ou_refeita", "eua_nao_reconheceu", "eua_sancao_12m", "vencedor_tomou_posse"):
        for categoria in ("sim", "disputado"):
            valores = [(n, DESFECHOS[desfecho](r)) for n, r in validos.items() if r.get("fraude_demonstrada") == categoria]
            valores = [(n, v) for n, v in valores if v is not None]
            linhas.append({"variante": f"V3: só fraude {'demonstrada' if categoria == 'sim' else 'disputada'}", "desfecho": desfecho,
                           "principal": "demonstrada e disputada juntas",
                           "variante_valor": f"{sum(v for _, v in valores)} de {len(valores)} ({', '.join(n for n, _ in valores)})"})
    # V2 (defensor da lente L): a relação do Lula com os EUA em 2026 declarada como neutra, como em 2014 e 2022
    for desfecho in ("eua_parabens_30d", "eua_sancao_12m"):
        for relacao in ("neutro", "adversario"):
            valores = [DESFECHOS[desfecho](r) for r in validos.values() if r.get("relacao_do_vencedor.eua") == relacao]
            valores = [v for v in valores if v is not None]
            linhas.append({"variante": f"V2: relação do Lula com os EUA em 2026 = {relacao}", "desfecho": desfecho,
                           "principal": "relação não declarada", "variante_valor": f"{sum(valores)} de {len(valores)}"})
    return linhas


def gravar_csv(nome: str, linhas: list[dict]) -> None:
    if not linhas:
        return
    with (RESULTADOS / nome).open("w", encoding="utf-8", newline="") as saida:
        escritor = csv.DictWriter(saida, fieldnames=list(linhas[0].keys()))
        escritor.writeheader()
        escritor.writerows(linhas)


def main() -> None:
    RESULTADOS.mkdir(exist_ok=True)
    a, b = ler_passada("a"), ler_passada("b")
    casos, concordancia = consenso(a, b)
    base = taxas_base(casos)
    teste, resumo_teste = teste_do_passado(casos)
    _, resumo_anteriores = teste_do_passado(casos, so_anteriores=True)
    resumo_teste["brier_so_com_casos_anteriores"] = resumo_anteriores.get("brier_metodo")
    resumo_teste["brier_taxa_geral_sem_condicionar"] = brier_sem_condicionar(casos)
    gravar_csv("f2_concordancia.csv", concordancia)
    gravar_csv("f2_taxas_base.csv", base)
    gravar_csv("f6_teste_do_passado.csv", teste)
    gravar_csv("variantes.csv", variantes(casos))
    (RESULTADOS / "f2_casos_consenso.json").write_text(json.dumps(casos, ensure_ascii=False, indent=2), encoding="utf-8")
    pares = [l for l in concordancia if l["casos_com_as_duas"]]
    resumo = {
        "f2": {"casos_passada_a": len(a), "casos_passada_b": len(b),
               "casos_na_conta": sum("excluido" not in r for r in casos.values()),
               "casos_excluidos": {n: r["excluido"] for n, r in casos.items() if "excluido" in r},
               "concordancia_media": round(sum(l["concordancia"] for l in pares) / len(pares), 3) if pares else None,
               "kappa_mediano": round(statistics.median(l["kappa"] for l in pares if l["kappa"] is not None), 3) if pares else None},
        "f6": resumo_teste,
        "f3": interesses(),
        "teto_das_duas_pontas": teto_das_duas_pontas(),
    }
    (RESULTADOS / "RESUMO.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumo.items() if k != "f3"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
