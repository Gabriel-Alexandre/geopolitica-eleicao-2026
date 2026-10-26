"""Refaz os números centrais por outro caminho (pandas e os arquivos brutos), sem importar ferramentas/analise.py.

Uso: python ferramentas/validacao_independente.py
Saída: resultados/validacao_independente.csv (item, principal, independente, passou)
"""
import json
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados" / "brutos"
RESUMO = json.loads((RAIZ / "resultados" / "RESUMO.json").read_text(encoding="utf-8"))
PARCEIROS = {0: "Mundo", 156: "China", 842: "EUA", 643: "Rússia"}


def comercio(linhas: list) -> None:
    registros = []
    for arquivo in sorted((BRUTOS / "comtrade").glob("brasil_20*.json")):
        for r in json.loads(arquivo.read_text(encoding="utf-8"))["data"]:
            registros.append({"ano": r["period"], "fluxo": r["flowCode"], "parceiro": PARCEIROS.get(r["partnerCode"]),
                              "valor": r["primaryValue"]})
    tabela = pd.DataFrame(registros).dropna().pivot_table(index=["ano", "fluxo"], columns="parceiro", values="valor")
    for (ano, fluxo), linha in tabela.iterrows():
        for parceiro in ("China", "EUA", "Rússia"):
            independente = round(100 * linha[parceiro] / linha["Mundo"], 2)
            nome_fluxo = "exportacao" if fluxo == "X" else "importacao"
            principal = RESUMO["f3"]["fatias_pct"][f"{ano}|{nome_fluxo}|{parceiro}"]
            linhas.append({"item": f"fatia {nome_fluxo} {parceiro} {ano}", "principal": principal,
                           "independente": independente, "passou": abs(principal - independente) < 0.01})


def onu(linhas: list) -> None:
    tabela = pd.read_csv(BRUTOS / "onu" / "AgreementScores.csv", usecols=["ccode1", "ccode2", "agree", "year"])
    brasil = tabela[(tabela.ccode1 == 140) & (tabela.ccode2.isin([2, 710, 365])) & (tabela.year >= 2015)]
    nomes = {2: "EUA", 710: "China", 365: "Rússia"}
    for _, linha in brasil.iterrows():
        chave = f"{int(linha.year)}|{nomes[int(linha.ccode2)]}"
        principal = RESUMO["f3"]["onu_concordancia"].get(chave)
        linhas.append({"item": f"concordância ONU {chave}", "principal": principal,
                       "independente": round(float(linha.agree), 3),
                       "passou": principal is not None and abs(principal - float(linha.agree)) < 0.001})


def taxas(linhas: list) -> None:
    """Refaz três taxas-base a partir das passadas brutas, com regra própria, e compara com f2_taxas_base.csv."""
    caminho = RAIZ / "resultados" / "f2_taxas_base.csv"
    if not caminho.exists():
        return
    principal = pd.read_csv(caminho)

    def ler(letra):
        casos = []
        for arquivo in sorted((RAIZ / "dados" / "casos").glob(f"passada_{letra}_*.json")):
            casos += json.loads(arquivo.read_text(encoding="utf-8"))
        return {c["caso"]: c for c in casos}

    a, b = ler("a"), ler("b")
    comuns = [n for n in a if n in b and a[n].get("fecha_com_duas_fontes") and b[n].get("fecha_com_duas_fontes")]

    def parabens(caso, potencia, limite):
        reacao = (caso.get("reacao") or {}).get(potencia) or {}
        tipo, dias = reacao.get("tipo"), reacao.get("dias_ate_parabens")
        if tipo in (None, "nao_se_aplica"):
            return None
        if tipo != "parabens":
            return 0
        return None if dias is None else int(dias <= limite)

    def taxa(potencia, limite, filtro):
        valores = []
        for nome in comuns:
            if not filtro(a[nome], b[nome]):
                continue
            va, vb = parabens(a[nome], potencia, limite), parabens(b[nome], potencia, limite)
            da = ((a[nome].get("reacao") or {}).get(potencia) or {}).get("dias_ate_parabens")
            db = ((b[nome].get("reacao") or {}).get(potencia) or {}).get("dias_ate_parabens")
            ta = ((a[nome].get("reacao") or {}).get(potencia) or {}).get("tipo")
            tb = ((b[nome].get("reacao") or {}).get(potencia) or {}).get("tipo")
            # emenda 2: o campo que diverge (o tipo de reação) sai, mesmo quando o desfecho binário coincide
            if va is None or vb is None or va != vb or ta != tb:
                continue
            if isinstance(da, (int, float)) and isinstance(db, (int, float)) and abs(da - db) > 2:
                continue
            if va == 1 and limite < 30 and (da + db) / 2 > limite:
                continue
            valores.append(va)
        return (sum(valores), len(valores))

    todos = lambda x, y: True  # noqa: E731
    lente_l = lambda x, y: x.get("fraude_demonstrada") == y.get("fraude_demonstrada") == "nao"  # noqa: E731
    for desfecho, potencia, limite, grupo, filtro in [
        ("china_parabens_7d", "china", 7, "todos", todos),
        ("russia_parabens_7d", "russia", 7, "todos", todos),
        ("eua_parabens_30d", "eua", 30, "fraude não demonstrada (lente L)", lente_l),
    ]:
        sim, n = taxa(potencia, limite, filtro)
        linha = principal[(principal.desfecho == desfecho) & (principal.grupo == grupo) & (principal.condicao == "todas")]
        valor_principal = f"{int(linha.sim.iloc[0])} de {int(linha.n.iloc[0])}" if len(linha) else None
        linhas.append({"item": f"taxa-base {desfecho} ({grupo})", "principal": valor_principal,
                       "independente": f"{sim} de {n}", "passou": valor_principal == f"{sim} de {n}"})


def main() -> None:
    linhas = []
    comercio(linhas)
    onu(linhas)
    taxas(linhas)
    tabela = pd.DataFrame(linhas)
    tabela.to_csv(RAIZ / "resultados" / "validacao_independente.csv", index=False)
    print(f"{int(tabela.passou.sum())} de {len(tabela)} passaram")
    if not tabela.passou.all():
        print(tabela[~tabela.passou].to_string())


if __name__ == "__main__":
    main()
