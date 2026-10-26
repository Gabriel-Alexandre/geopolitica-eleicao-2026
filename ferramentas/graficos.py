"""Gráficos 1920x1080 a partir de resultados/RESUMO.json e das tabelas de resultados/.

Uso: python ferramentas/graficos.py  (grava em resultados/figuras/)
"""
import csv
import json
import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
RESULTADOS = RAIZ / "resultados"
FIGURAS = RESULTADOS / "figuras"
COR = {"EUA": "#2F5D8C", "China": "#C9902B", "Rússia": "#6B6B6B", "UE": "#6A4C93", "Brasil": "#2E8B57"}
RODAPE = "github.com/Gabriel-Alexandre/geopolitica-eleicao-2026 · análise feita pelo Claude"

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 22, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.titleweight": "bold", "axes.titlesize": 34,
                     "axes.titlepad": 30})


def nova(titulo: str, subtitulo: str):
    figura, eixo = plt.subplots(figsize=(16, 9), dpi=120)
    figura.subplots_adjust(left=0.08, right=0.82, top=0.78, bottom=0.16)
    figura.suptitle(titulo, x=0.08, y=0.965, ha="left", fontsize=34, fontweight="bold")
    figura.text(0.08, 0.855, subtitulo, ha="left", fontsize=21, color="#444444")
    return figura, eixo


def salvar(figura, nome: str, fonte: str) -> None:
    figura.text(0.08, 0.05, f"Fonte: {fonte}", fontsize=15, color="#555555", ha="left")
    figura.text(0.08, 0.018, RODAPE, fontsize=15, color="#555555", ha="left")
    FIGURAS.mkdir(parents=True, exist_ok=True)
    figura.savefig(FIGURAS / f"{nome}.png")
    plt.close(figura)


def linha_com_rotulo(eixo, xs, ys, nome, cor, formato="{:.0f}%"):
    eixo.plot(xs, ys, color=cor, linewidth=5)
    eixo.text(xs[-1] + 0.3, ys[-1], f"{nome}  {formato.format(ys[-1])}", color=cor, fontsize=24,
              va="center", fontweight="bold")


def g01_exportacoes(f3: dict) -> None:
    figura, eixo = nova("Para quem o Brasil vende", "Fatia das exportações brasileiras, 2015 a 2025")
    anos = sorted({int(k.split("|")[0]) for k in f3["fatias_pct"]})
    for parceiro in ("China", "EUA", "Rússia"):
        linha_com_rotulo(eixo, anos, [f3["fatias_pct"][f"{a}|exportacao|{parceiro}"] for a in anos], parceiro, COR[parceiro])
    eixo.set_ylim(0, 36)
    eixo.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
    salvar(figura, "g01_exportacoes", "UN Comtrade (dados declarados pelo Brasil)")


def g02_importacoes(f3: dict) -> None:
    figura, eixo = nova("De quem o Brasil compra", "Fatia das importações brasileiras, 2015 a 2025")
    anos = sorted({int(k.split("|")[0]) for k in f3["fatias_pct"]})
    for parceiro in ("China", "EUA", "Rússia"):
        linha_com_rotulo(eixo, anos, [f3["fatias_pct"][f"{a}|importacao|{parceiro}"] for a in anos], parceiro, COR[parceiro])
    eixo.set_ylim(0, 30)
    eixo.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
    salvar(figura, "g02_importacoes", "UN Comtrade (dados declarados pelo Brasil)")


def g03_onu(f3: dict) -> None:
    figura, eixo = nova("Com quem o Brasil vota na ONU",
                        "Concordância do Brasil com cada país nas votações da Assembleia Geral, 2000 a 2024")
    for par in ("China", "Rússia", "EUA"):
        anos = sorted(int(k.split("|")[0]) for k in f3["onu_concordancia"] if k.endswith(f"|{par}") and int(k.split("|")[0]) >= 2000)
        valores = [100 * f3["onu_concordancia"][f"{a}|{par}"] for a in anos]
        linha_com_rotulo(eixo, anos, valores, par, COR[par])
    eixo.set_ylim(0, 100)
    eixo.yaxis.set_major_formatter(lambda v, _: f"{v:.0f}%")
    salvar(figura, "g03_votos_na_onu", "Erik Voeten, United Nations General Assembly Voting Data (Harvard Dataverse)")


def g04_terras_raras(f3: dict) -> None:
    figura, eixo = nova("O Brasil tem a 2ª maior reserva de terras raras",
                        "Reservas em toneladas de óxido de terras raras, 2025")
    figura.subplots_adjust(left=0.15)
    reservas = sorted(f3["terras_raras_reservas_t"].items(), key=lambda x: x[1])
    nomes = [n for n, _ in reservas]
    valores = [v / 1e6 for _, v in reservas]
    barras = eixo.barh(nomes, valores, color=[COR["Brasil"] if n == "Brasil" else COR.get(n, "#9AA5B1") for n in nomes])
    for barra, valor in zip(barras, valores):
        eixo.text(barra.get_width() + 0.5, barra.get_y() + barra.get_height() / 2, f"{valor:.1f} milhões".replace(".", ","),
                  va="center", fontsize=22)
    eixo.set_xlim(0, 52)
    eixo.set_xticks([])
    eixo.spines["bottom"].set_visible(False)
    salvar(figura, "g04_terras_raras", "USGS, Mineral Commodity Summaries 2026")


def g05_adubos(f3: dict) -> None:
    figura, eixo = nova("Um quarto do adubo importado vem da Rússia",
                        "Fatia da Rússia nas importações brasileiras de adubos (capítulo 31), 2021 a 2025")
    anos = sorted(int(a) for a in f3["adubos_fatia_russia_pct"])
    valores = [f3["adubos_fatia_russia_pct"][str(a)] if str(a) in f3["adubos_fatia_russia_pct"]
               else f3["adubos_fatia_russia_pct"][a] for a in anos]
    barras = eixo.bar([str(a) for a in anos], valores, color=COR["Rússia"])
    for barra, valor in zip(barras, valores):
        eixo.text(barra.get_x() + barra.get_width() / 2, valor + 0.6, f"{valor:.0f}%", ha="center", fontsize=24)
    eixo.set_ylim(0, 35)
    eixo.set_yticks([])
    eixo.spines["left"].set_visible(False)
    salvar(figura, "g05_adubos_da_russia", "UN Comtrade (dados declarados pelo Brasil)")


def g06_taxas_base() -> None:
    caminho = RESULTADOS / "f2_taxas_base.csv"
    if not caminho.exists():
        return
    with caminho.open(encoding="utf-8") as arquivo:
        linhas = [l for l in csv.DictReader(arquivo) if l["condicao"] == "todas"]
    itens = [("eua_parabens_30d", "EUA parabenizam em até 30 dias"), ("china_parabens_7d", "China parabeniza em até 7 dias"),
             ("russia_parabens_7d", "Rússia parabeniza em até 7 dias"), ("anulada_ou_refeita", "A eleição é anulada ou refeita")]
    figura, eixo = nova("O que aconteceu nas eleições contestadas",
                        "Em quantos casos, pelas duas lentes (fraude não demonstrada e fraude demonstrada ou disputada)")
    figura.subplots_adjust(left=0.30)
    grupos = [("fraude não demonstrada (lente L)", "#2E8B57", -0.2), ("fraude demonstrada ou disputada (lente F)", "#B03A2E", 0.2)]
    for grupo, cor, deslocamento in grupos:
        for posicao, (chave, _) in enumerate(itens):
            linha = next((l for l in linhas if l["desfecho"] == chave and l["grupo"] == grupo), None)
            if not linha:
                continue
            taxa = 100 * float(linha["taxa"])
            eixo.barh(posicao + deslocamento, taxa, height=0.38, color=cor)
            eixo.text(taxa + 1, posicao + deslocamento, f"{linha['sim']} de {linha['n']}", va="center", fontsize=20)
    eixo.set_yticks(range(len(itens)))
    eixo.set_yticklabels([rotulo for _, rotulo in itens])
    eixo.invert_yaxis()
    eixo.set_xlim(0, 115)
    eixo.xaxis.set_major_formatter(lambda v, _: f"{v:.0f}%" if v <= 100 else "")
    eixo.text(0.0, -0.13, "verde: fraude não demonstrada  ·  vermelho: fraude demonstrada ou disputada",
              transform=eixo.transAxes, fontsize=18, color="#444444")
    salvar(figura, "g06_o_que_aconteceu", "fichas dos casos, duas passadas independentes (dados/casos/)")


def g07_quem_reconheceu() -> None:
    with (RAIZ / "dados" / "quadro_reacoes.csv").open(encoding="utf-8") as arquivo:
        linhas = list(csv.DictReader(arquivo))
    figura, eixo = nova("Quem já deu parabéns ao Lula", "Reações oficiais até a manhã de 26/out/2026")
    eixo.axis("off")
    for i, linha in enumerate(linhas):
        y = 1 - (i + 0.5) / len(linhas)
        cor = "#2E8B57" if linha["situacao"] == "parabenizou" else "#B03A2E"
        eixo.text(0.0, y, linha["quem"], fontsize=30, fontweight="bold", va="center", transform=eixo.transAxes)
        eixo.text(0.38, y, linha["situacao"], fontsize=28, color=cor, fontweight="bold", va="center", transform=eixo.transAxes)
        eixo.text(0.38, y - 0.075, textwrap.fill(linha["detalhe"], 70), fontsize=17, color="#444444", va="center", transform=eixo.transAxes)
    salvar(figura, "g07_quem_deu_parabens", "capturas com sha256 em dados/capturas/ (docs/F1_REACOES.md)")


def main() -> None:
    resumo = json.loads((RESULTADOS / "RESUMO.json").read_text(encoding="utf-8"))
    f3 = resumo["f3"]
    g01_exportacoes(f3)
    g02_importacoes(f3)
    g03_onu(f3)
    g04_terras_raras(f3)
    g05_adubos(f3)
    g06_taxas_base()
    g07_quem_reconheceu()
    print(sorted(p.name for p in FIGURAS.glob("*.png")))


if __name__ == "__main__":
    main()
