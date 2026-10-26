"""F3: coleta os dados de interesses com sha256.

Uso: python ferramentas/coletar_f3.py
- Comércio do Brasil com o mundo, a China, os EUA e a Rússia, 2015 a 2025 (UN Comtrade, prévia pública,
  um ano por pedido; a API do Comex Stat respondeu 429 a todos os pedidos de 26/out e os arquivos em lote não abriram)
- Concordância nos votos da Assembleia Geral da ONU (Erik Voeten, Harvard Dataverse, AgreementScores.csv)
- Pontos ideais na ONU (mesma base, IdealpointestimatesFP_2026FP.csv)
- Reservas de terras raras (USGS, Mineral Commodity Summaries 2026)
- Importação de adubos (capítulo 31 do SH, UN Comtrade)
Brutos em dados/brutos/ (fora do git); sha256 de cada arquivo em dados/MANIFESTO_F3.json;
derivados leves em dados/derivados/ (no git).
"""
import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados" / "brutos"
DERIVADOS = RAIZ / "dados" / "derivados"
MANIFESTO = RAIZ / "dados" / "MANIFESTO_F3.json"
PARCEIROS = {"0": "Mundo", "156": "China", "842": "EUA", "643": "Rússia"}
CODIGOS_COW = {2: "EUA", 710: "China", 365: "Rússia"}  # Correlates of War; Brasil = 140
ANOS = range(2015, 2026)
DATAVERSE = "https://dataverse.harvard.edu/api/access/datafile/{}"
ARQUIVOS_ONU = {"AgreementScores.csv": 11837234, "IdealpointestimatesFP_2026FP.csv": 14098429}


def sha256_arquivo(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1 << 20), b""):
            resumo.update(bloco)
    return resumo.hexdigest()


def registrar(manifesto: dict, chave: str, url: str, caminho: Path) -> None:
    manifesto[chave] = {
        "url": url,
        "capturado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bytes": caminho.stat().st_size,
        "sha256": sha256_arquivo(caminho),
    }


def comercio(manifesto: dict) -> None:
    pasta = BRUTOS / "comtrade"
    pasta.mkdir(parents=True, exist_ok=True)
    linhas = []
    for ano in ANOS:
        destino = pasta / f"brasil_{ano}.json"
        url = ("https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=76"
               f"&period={ano}&partnerCode={','.join(PARCEIROS)}&flowCode=X,M&cmdCode=TOTAL")
        if not destino.exists():
            for tentativa in range(4):
                resposta = requests.get(url, timeout=60)
                if resposta.status_code == 200:
                    destino.write_bytes(resposta.content)
                    break
                time.sleep(10 * (tentativa + 1))
            time.sleep(3)
        if not destino.exists():
            print(f"comtrade {ano}: falhou")
            continue
        registrar(manifesto, f"comtrade_{ano}", url, destino)
        for registro in json.loads(destino.read_text(encoding="utf-8")).get("data", []):
            parceiro = str(registro["partnerCode"])
            if parceiro in PARCEIROS:
                linhas.append({"ano": ano, "fluxo": "exportacao" if registro["flowCode"] == "X" else "importacao",
                               "parceiro": PARCEIROS[parceiro], "valor_usd": round(registro["primaryValue"])})
    with (DERIVADOS / "comercio_brasil.csv").open("w", encoding="utf-8", newline="") as saida:
        escritor = csv.DictWriter(saida, fieldnames=["ano", "fluxo", "parceiro", "valor_usd"])
        escritor.writeheader()
        escritor.writerows(sorted(linhas, key=lambda l: (l["ano"], l["fluxo"], l["parceiro"])))
    print(f"comtrade: {len(linhas)} linhas")


def onu(manifesto: dict) -> None:
    pasta = BRUTOS / "onu"
    pasta.mkdir(parents=True, exist_ok=True)
    for nome, ident in ARQUIVOS_ONU.items():
        destino = pasta / nome
        url = DATAVERSE.format(ident)
        if not destino.exists():
            with requests.get(url, stream=True, timeout=300) as resposta:
                resposta.raise_for_status()
                with destino.open("wb") as saida:
                    for bloco in resposta.iter_content(1 << 20):
                        saida.write(bloco)
        registrar(manifesto, f"onu_{nome}", url, destino)

    with (pasta / "AgreementScores.csv").open(encoding="utf-8", errors="replace") as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = leitor.fieldnames
        linhas = []
        for linha in leitor:
            if linha.get("ccode1") == "140" and int(float(linha.get("ccode2") or 0)) in CODIGOS_COW:
                linhas.append({"ano": int(float(linha["year"])), "par": CODIGOS_COW[int(float(linha["ccode2"]))],
                               "concordancia": linha.get("agree"), "distancia_ponto_ideal": linha.get("IdealPointDistance")})
    with (DERIVADOS / "onu_concordancia_brasil.csv").open("w", encoding="utf-8", newline="") as saida:
        escritor = csv.DictWriter(saida, fieldnames=["ano", "par", "concordancia", "distancia_ponto_ideal"])
        escritor.writeheader()
        escritor.writerows(sorted(linhas, key=lambda l: (l["ano"], l["par"])))
    print(f"onu: campos {campos[:12]}; {len(linhas)} linhas do Brasil")


# Reservas de terras raras (USGS, Mineral Commodity Summaries 2026). A tabela do PDF cola o número da nota de rodapé
# no número (ex.: "136,300,000" é a nota 13 + 6.300.000), então o valor é escrito aqui e conferido contra a linha do PDF.
USGS_URL = "https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf"
USGS_RESERVAS = {"China": ("China ", "44,000,000"), "Brasil": ("Brazil ", "11,000,000"),
                 "Austrália": ("Australia ", "6,300,000"), "Rússia": ("Russia ", "3,800,000"),
                 "Vietnã": ("Vietnam ", "3,500,000"), "EUA": ("United States ", "1,900,000")}


def terras_raras(manifesto: dict) -> None:
    from pypdf import PdfReader
    pasta = BRUTOS / "usgs"
    pasta.mkdir(parents=True, exist_ok=True)
    destino = pasta / "mcs2026-rare-earths.pdf"
    if not destino.exists():
        destino.write_bytes(requests.get(USGS_URL, timeout=120, headers={"User-Agent": "Mozilla/5.0"}).content)
    registrar(manifesto, "usgs_terras_raras_2026", USGS_URL, destino)
    texto = "\n".join(pagina.extract_text() for pagina in PdfReader(destino).pages)
    (RAIZ / "dados" / "capturas" / "usgs_terras_raras_2026.txt").write_bytes(texto.encode("utf-8"))
    linhas_pdf = texto.splitlines()
    saida = []
    for pais, (inicio, numero) in USGS_RESERVAS.items():
        linha = next(l for l in linhas_pdf if l.startswith(inicio) and l.rstrip().endswith(numero))
        saida.append({"pais": pais, "reservas_t_oxido": int(numero.replace(",", "")), "linha_do_pdf": linha.strip()})
    with (DERIVADOS / "terras_raras_reservas.csv").open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["pais", "reservas_t_oxido", "linha_do_pdf"])
        escritor.writeheader()
        escritor.writerows(saida)
    print(f"usgs: {len(saida)} países conferidos contra a linha do PDF")


def fertilizantes(manifesto: dict) -> None:
    """Importação brasileira de adubos (capítulo 31 do SH) do mundo, da Rússia, da China e dos EUA."""
    pasta = BRUTOS / "comtrade"
    linhas = []
    for ano in range(2021, 2026):
        destino = pasta / f"brasil_adubos_{ano}.json"
        url = ("https://comtradeapi.un.org/public/v1/preview/C/A/HS?reporterCode=76"
               f"&period={ano}&partnerCode={','.join(PARCEIROS)}&flowCode=M&cmdCode=31")
        if not destino.exists():
            for tentativa in range(4):
                resposta = requests.get(url, timeout=60)
                if resposta.status_code == 200:
                    destino.write_bytes(resposta.content)
                    break
                time.sleep(10 * (tentativa + 1))
            time.sleep(3)
        registrar(manifesto, f"comtrade_adubos_{ano}", url, destino)
        for registro in json.loads(destino.read_text(encoding="utf-8")).get("data", []):
            parceiro = str(registro["partnerCode"])
            if parceiro in PARCEIROS:
                linhas.append({"ano": ano, "parceiro": PARCEIROS[parceiro], "valor_usd": round(registro["primaryValue"])})
    with (DERIVADOS / "adubos_importacao_brasil.csv").open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=["ano", "parceiro", "valor_usd"])
        escritor.writeheader()
        escritor.writerows(sorted(linhas, key=lambda l: (l["ano"], l["parceiro"])))
    print(f"adubos: {len(linhas)} linhas")


def main() -> None:
    DERIVADOS.mkdir(parents=True, exist_ok=True)
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8")) if MANIFESTO.exists() else {}
    comercio(manifesto)
    onu(manifesto)
    terras_raras(manifesto)
    fertilizantes(manifesto)
    MANIFESTO.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
