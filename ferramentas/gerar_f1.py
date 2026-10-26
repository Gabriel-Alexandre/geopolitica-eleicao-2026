"""Confere cada citação da F1 no texto capturado e gera o relatório da fase.

Uso: python ferramentas/gerar_f1.py
Entradas: dados/fontes_f1.csv, dados/citacoes_f1.csv, dados/MANIFESTO.json, dados/capturas/*.txt
Saídas:   resultados/f1_citacoes.csv, resultados/f1_resumo.json, docs/F1_REACOES.md
Citação que não aparece, palavra por palavra, no texto capturado sai marcada como não conferida.
"""
import csv
import json
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "dados"
RESULTADOS = RAIZ / "resultados"
COMMIT_PRE_REGISTRO = "0f72f8e"
GRUPOS = [
    ("trump", "O presidente dos EUA"),
    ("oficial_eua", "O governo dos EUA"),
    ("circulo_trump", "Quem fala pelo círculo do Trump ou perto dele (inclui aliados brasileiros do Flávio que moram nos EUA)"),
    ("circulo_lula", "Quem fala pelo círculo do Lula"),
    ("brasil", "Os candidatos e as campanhas"),
    ("russia", "Rússia"),
    ("china", "China"),
    ("ue", "União Europeia"),
    ("america_latina", "América Latina"),
]


def normalizar(texto: str) -> str:
    texto = texto.replace(" ", " ")
    for de, para in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("«", '"'), ("»", '"')):
        texto = texto.replace(de, para)
    return re.sub(r"\s+", " ", texto).strip().lower()


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def posts_do_arquivo_truth(texto: str) -> list[tuple[str, str]]:
    """Separa os posts da página de busca do arquivo Trump's Truth: (data e hora, texto)."""
    plano = re.sub(r"\s+", " ", texto.replace(" ", " "))
    partes = re.split(r"Donald J\. Trump @realDonaldTrump · ", plano)[1:]
    posts = []
    for parte in partes:
        achado = re.match(r"([A-Z][a-z]+ \d+, \d{4}, [\d:]+ [AP]M)(.*)", parte)
        if achado:
            posts.append((achado.group(1), achado.group(2)))
    return posts


def hora_do_commit(commit: str) -> str:
    saida = subprocess.run(["git", "log", "-1", "--format=%cI", commit], cwd=RAIZ,
                           capture_output=True, text=True)
    return saida.stdout.strip() or "não encontrado"


def main() -> None:
    fontes = {f["id"]: f for f in ler_csv(DADOS / "fontes_f1.csv")}
    manifesto = json.loads((DADOS / "MANIFESTO.json").read_text(encoding="utf-8"))
    citacoes = ler_csv(DADOS / "citacoes_f1.csv")

    for citacao in citacoes:
        arquivo = DADOS / "capturas" / f"{citacao['fonte']}.txt"
        texto = arquivo.read_text(encoding="utf-8") if arquivo.exists() else ""
        citacao["conferida"] = "sim" if normalizar(citacao["citacao"]) in normalizar(texto) else "não"
        citacao["url"] = fontes[citacao["fonte"]]["url"]
        citacao["sha256_texto"] = manifesto.get(citacao["fonte"], {}).get("sha256_texto", "")

    posts = posts_do_arquivo_truth((DADOS / "capturas" / "t10.txt").read_text(encoding="utf-8"))
    termos = re.compile(r"brazil|brasil|lula|bolsonaro|playbook|biden", re.I)
    posts_25 = [p for p in posts if p[0].startswith("October 25, 2026")]
    sobre_brasil = [p for p in posts if termos.search(p[1])]

    # só as fontes da F1 (o MANIFESTO também guarda as capturas da F3)
    capturadas = [i for i, r in manifesto.items() if r.get("ok") and i in fontes]
    falhas = {i: r for i, r in manifesto.items() if not r.get("ok") and i in fontes}
    conferidas = [c for c in citacoes if c["conferida"] == "sim"]
    resumo = {
        "fontes_na_lista": len(fontes),
        "fontes_capturadas": len(capturadas),
        "fontes_que_falharam": {i: r.get("status_http", r.get("erro")) for i, r in falhas.items()},
        "citacoes": len(citacoes),
        "citacoes_conferidas": len(conferidas),
        "truth_social_posts_lidos": len(posts),
        "truth_social_posts_em_25_out": len(posts_25),
        "truth_social_posts_sobre_brasil": len(sobre_brasil),
        "truth_social_primeiro_e_ultimo": [posts[-1][0], posts[0][0]] if posts else [],
        "commit_pre_registro": COMMIT_PRE_REGISTRO,
        "hora_commit_pre_registro": hora_do_commit(COMMIT_PRE_REGISTRO),
    }

    RESULTADOS.mkdir(exist_ok=True)
    campos = ["id", "fonte", "grupo", "quem", "quando", "canal", "citacao", "observacao", "conferida", "url", "sha256_texto"]
    with (RESULTADOS / "f1_citacoes.csv").open("w", encoding="utf-8", newline="") as saida:
        escritor = csv.DictWriter(saida, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(citacoes)
    (RESULTADOS / "f1_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2), encoding="utf-8")
    (RAIZ / "docs" / "F1_REACOES.md").write_text(relatorio(citacoes, resumo, sobre_brasil), encoding="utf-8")
    print(json.dumps(resumo, ensure_ascii=False, indent=2))


def linha_citacao(c: dict) -> str:
    marca = "✅" if c["conferida"] == "sim" else "❌ não conferida"
    obs = f" · {c['observacao']}" if c["observacao"] else ""
    return (f"| {c['quem']} | {c['quando']} | {c['canal']} | *\"{c['citacao']}\"*{obs} "
            f"| [{c['fonte']}]({c['url']}) | {marca} |")


def relatorio(citacoes: list[dict], r: dict, sobre_brasil: list) -> str:
    por_id = {c["id"]: c for c in citacoes}
    l = []
    l.append("# F1 · As reações das primeiras horas (25 e 26/out/2026)\n")
    l.append("Gerado por `ferramentas/gerar_f1.py`. Cada citação foi procurada, palavra por palavra, no texto "
             "capturado da página (`dados/capturas/<fonte>.txt`, com sha256 em `dados/MANIFESTO.json`). "
             "As duas lentes do pré-registro valem aqui: as falas dos dois lados entram pela mesma régua.\n")
    l.append(f"**Captura:** {r['fontes_capturadas']} de {r['fontes_na_lista']} páginas. "
             f"**Citações conferidas no texto capturado:** {r['citacoes_conferidas']} de {r['citacoes']}.\n")

    l.append("## 1. O que o Trump disse, e o que não disse\n")
    l.append(f"- **A fala existe, e a origem é uma só: a agência EFE**, de Washington, na noite de 25/out: "
             f"*\"{por_id['q01']['citacao']}\"* ({por_id['q01']['conferida'] == 'sim' and 'conferida no texto capturado' or 'NÃO conferida'}). "
             "Vários veículos republicaram o mesmo despacho (Infobae, Times Brasil, Primera Hora, Diario Libre); isso é uma fonte repetida, não várias.")
    l.append(f"- **Não está entre os posts do Truth Social de 25/out.** O arquivo independente dos posts dele (Trump's Truth) tem "
             f"{r['truth_social_posts_em_25_out']} posts em 25/out, do primeiro ({r['truth_social_primeiro_e_ultimo'][0] if r['truth_social_primeiro_e_ultimo'] else '?'}) "
             f"ao último lido ({r['truth_social_primeiro_e_ultimo'][1] if r['truth_social_primeiro_e_ultimo'] else '?'}, horário da costa leste dos EUA), e "
             f"{r['truth_social_posts_sobre_brasil']} falam de Brasil, Lula, Bolsonaro ou Biden. A EFE não diz o canal, e não foi achado vídeo nem transcrição da fala.")
    l.append(f"- **A Time não registrou a fala** até o começo da manhã de 26/out (*\"{por_id['q03']['citacao']}\"*).")
    # releitura da tarde (t11, t12, t13): a própria EFE trocou o texto
    manifesto = json.loads((DADOS / "MANIFESTO.json").read_text(encoding="utf-8"))
    tarde = (DADOS / "capturas" / "t12.txt")
    trocado = tarde.exists() and "no se ha pronunciado" in tarde.read_text(encoding="utf-8")
    if "t11" in manifesto and trocado:
        l.append(f"- 🔧 **Relido à tarde, a própria EFE trocou o texto.** Às {manifesto['t12']['capturado_em_utc']} (UTC), o endereço do Infobae dava "
                 f"{manifesto['t11'].get('status_http')}, e o Diario Libre trazia, no mesmo endereço e com a mesma hora do despacho, outro texto da EFE: "
                 "*\"Trump aún no se pronuncia sobre la derrota de su aliado Flávio Bolsonaro\"*, dizendo que ele *\"no se ha pronunciado aún públicamente\"*. "
                 "A Times Brasil ainda trazia a frase, citando a EFE (t13). **Leitura do projeto:** a frase não tem fonte de pé; ela entra como algo que uma agência "
                 "publicou e trocou, nunca como fala do Trump. As duas versões do pré-registro se resolvem assim: não foi achado post dele, nem nota da Casa Branca, "
                 "nem fala que a agência mantivesse.")
    l.append(f"- Antes do resultado, ele tinha dito: *\"{por_id['q02']['citacao']}\"*.")
    l.append("- **Como isso entra nas suposições:** a fala é anterior ao commit do pré-registro e já estava no §0 dele (*\"duas versões\"*), e depois foi trocada pela própria EFE. "
             "Ela não usa as palavras do critério da S7 (*fraudada, roubada, manipulada*, ou apoio à anulação), então **a S7 continua aberta** até 05/jan/2027. "
             "Para a S5 (parabéns em até 30 dias), é um sinal na direção prevista em L, não uma resolução.\n")

    l.append("## 2. As falas, por grupo\n")
    for chave, titulo in GRUPOS:
        do_grupo = [c for c in citacoes if c["grupo"] == chave]
        if not do_grupo:
            continue
        l.append(f"### {titulo}\n")
        l.append("| Quem | Quando | Canal | O que disse | Fonte | Conferida |")
        l.append("|---|---|---|---|---|---|")
        l.extend(linha_citacao(c) for c in do_grupo)
        l.append("")

    l.append("## 3. As suposições do pré-registro que já se mexeram\n")
    l.append("| # | Suposição | Situação em 26/out | Base |")
    l.append("|---|---|---|---|")
    l.append(f"| S10 | Putin parabeniza Lula | ✅ **aconteceu**, às 12h40 de Moscou (6h40 de Brasília), **antes** do commit do pré-registro ({r['commit_pre_registro']}, {r['hora_commit_pre_registro']}). Pela emenda 1, sai da nota de Brier e é publicada à parte | q24, q25, q26 |")
    l.append("| S9 | Xi Jinping manda mensagem pessoal | ⬜ aberta: até agora só o porta-voz Guo Jiakun, que já estava no §0 | q27, q28 |")
    l.append("| S5 | Trump parabeniza Lula em até 30 dias | ⬜ aberta; o sinal da noite de 25/out (EFE) aponta para o lado previsto em L | q01, q03 |")
    l.append("| S6 | O Departamento de Estado trata o resultado como válido | ⬜ aberta: nenhuma nota até a captura | q04, q05 |")
    l.append("| S7 | Trump ou o governo dos EUA falam em fraude ou apoiam a anulação | ⬜ aberta: a fala da EFE não usa as palavras do critério | q01 |")
    l.append("| S11 | China ou Rússia citam interferência dos EUA | ⬜ aberta: nenhuma das falas capturadas fala nisso | q26, q27 |\n")

    l.append("## 4. Correções ao que o plano dizia\n")
    l.append("- **Eduardo Bolsonaro não chamou a prorrogação de golpe.** Ele disse *\"Estranho, hein\"*; a palavra *golpe* é do Paulo Figueiredo, e está no título do DCM (q13, q14).")
    l.append("- **A fala do Eduardo sobre a volta das sanções a Moraes (10/out) era condicionada à vitória do Flávio** (q16). Com o Lula reeleito, ela pesa menos do que o plano dava a ela no porquê da S8. A faixa da S8 fica como está (o pré-registro manda); a correção entra na síntese.")
    l.append("- **O TSE é presidido pelo ministro Kassio Nunes Marques**: agora com duas fontes (Latin Times e DCM, q23).\n")

    l.append("## 5. O que não foi capturado\n")
    for ident, motivo in r["fontes_que_falharam"].items():
        l.append(f"- `{ident}`: {motivo}")
    l.append("\nA fala do Flávio, que estava no Conjur (403), está conferida pela Al Jazeera (q21) e pela CN1 (b03). "
             "A apuração da Reuters sobre o Departamento de Estado (US News, tempo esgotado) segue registrada no pré-registro como reportagem com fonte anônima.\n")
    return "\n".join(l) + "\n"


if __name__ == "__main__":
    main()
