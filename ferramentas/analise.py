"""F2, F3 e F6: concordância entre as passadas, taxas-base, teste do passado e os números de interesses.

Uso: python ferramentas/analise.py
Entradas: dados/casos/passada_{a,b}_{1,2}.json, dados/derivados/*.csv, dados/f1 (resultados/f1_resumo.json)
Saídas:   resultados/RESUMO.json e as tabelas de resultados/*.csv
Regras: pré-registro §5 e emendas 2 e 3.
"""
import csv
import json
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


def teste_do_passado(casos: dict) -> tuple[list[dict], dict]:
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
    gravar_csv("f2_concordancia.csv", concordancia)
    gravar_csv("f2_taxas_base.csv", base)
    gravar_csv("f6_teste_do_passado.csv", teste)
    (RESULTADOS / "f2_casos_consenso.json").write_text(json.dumps(casos, ensure_ascii=False, indent=2), encoding="utf-8")
    pares = [l for l in concordancia if l["casos_com_as_duas"]]
    resumo = {
        "f2": {"casos_passada_a": len(a), "casos_passada_b": len(b),
               "casos_na_conta": sum("excluido" not in r for r in casos.values()),
               "casos_excluidos": {n: r["excluido"] for n, r in casos.items() if "excluido" in r},
               "concordancia_media": round(sum(l["concordancia"] for l in pares) / len(pares), 3) if pares else None,
               "kappa_mediano": sorted(l["kappa"] for l in pares if l["kappa"] is not None)[len(pares) // 2] if pares else None},
        "f6": resumo_teste,
        "f3": interesses(),
    }
    (RESULTADOS / "RESUMO.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in resumo.items() if k != "f3"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
