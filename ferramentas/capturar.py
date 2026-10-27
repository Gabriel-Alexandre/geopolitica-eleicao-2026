"""Captura as páginas da lista de fontes, extrai o texto e registra tudo com sha256.

Uso: python ferramentas/capturar.py dados/fontes_f1.csv [--refazer] [--navegador]
- HTML bruto em dados/brutos/<id>.html (fora do git)
- texto extraído em dados/capturas/<id>.txt (no git)
- endereço, hora, status, tamanho e sha256 em dados/MANIFESTO.json
Página com texto já capturado não é baixada de novo, a menos que se passe --refazer.
Com --navegador, as que faltam são abertas no Edge (para páginas que recusam o pedido direto); com --chrome, no Chrome.
"""
import csv
import re
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados" / "brutos"
CAPTURAS = RAIZ / "dados" / "capturas"
MANIFESTO = RAIZ / "dados" / "MANIFESTO.json"
CABECALHO = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/129.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,es;q=0.7",
}


def sha256(dados: bytes) -> str:
    return hashlib.sha256(dados).hexdigest()


def extrair_texto(html: bytes) -> str:
    sopa = BeautifulSoup(html, "html.parser")
    for marca in sopa(["script", "style", "noscript", "svg", "iframe", "form"]):
        marca.decompose()
    titulo = sopa.title.get_text(" ", strip=True) if sopa.title else ""
    # o maior bloco de matéria; a primeira <article> costuma ser um card de "leia também"
    candidatos = sopa.find_all("article") + sopa.find_all("main")
    corpo = max(candidatos, key=lambda c: len(c.get_text(" ", strip=True)), default=None)
    if corpo is None or len(corpo.get_text(" ", strip=True)) < 1000:
        corpo = sopa.body or sopa
    linhas = [linha.strip() for linha in corpo.get_text("\n").splitlines()]
    texto = "\n".join(linha for linha in linhas if linha)
    return tarjar(f"TITULO: {titulo}\n\n{texto}\n")


def tarjar(texto: str) -> str:
    """Documento pessoal (passaporte, identidade, CPF) não entra no repositório público, nem quando a página oficial o traz."""
    texto = re.sub(r"(Passport)\s+[A-Z]{0,3}\d[\w-]*", r"\1 [tarjado]", texto)
    texto = re.sub(r"(National ID No\.)\s*[\d./-]+", r"\1 [tarjado]", texto)
    return re.sub(r"(CPF:?)\s*\d{3}\.?\d{3}\.?\d{3}-?\d{2}", r"\1 [tarjado]", texto)


def baixar_com_navegador(url: str, canal: str = "msedge") -> tuple[int, bytes]:
    """Para páginas que recusam o pedido direto (403, 406, tempo esgotado): abre no Edge (ou no Chrome, com --chrome)
    e salva o HTML renderizado."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        navegador = p.chromium.launch(channel=canal)
        pagina = navegador.new_page(locale="pt-BR")
        resposta = pagina.goto(url, timeout=60000, wait_until="domcontentloaded")
        pagina.wait_for_timeout(4000)
        html = pagina.content().encode("utf-8")
        status = resposta.status if resposta else 0
        navegador.close()
    return status, html


def main() -> None:
    lista = Path(sys.argv[1])
    refazer = "--refazer" in sys.argv
    chrome = "--chrome" in sys.argv
    navegador = "--navegador" in sys.argv or chrome
    BRUTOS.mkdir(parents=True, exist_ok=True)
    CAPTURAS.mkdir(parents=True, exist_ok=True)
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8")) if MANIFESTO.exists() else {}
    for linha in csv.DictReader(lista.open(encoding="utf-8")):
        ident, url = linha["id"], linha["url"]
        destino = CAPTURAS / f"{ident}.txt"
        if destino.exists() and not refazer and manifesto.get(ident, {}).get("ok"):
            continue
        registro = {"url": url, "capturado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        try:
            if navegador:
                registro["metodo"] = f"navegador ({'Chrome' if chrome else 'Edge'} via Playwright, HTML renderizado)"
                status, bruto = baixar_com_navegador(url, "chrome" if chrome else "msedge")
            else:
                registro["metodo"] = "pedido direto (requests)"
                resposta = requests.get(url, headers=CABECALHO, timeout=40)
                status, bruto = resposta.status_code, resposta.content
            registro["status_http"] = status
            registro["bytes_html"] = len(bruto)
            registro["sha256_html"] = sha256(bruto)
            (BRUTOS / f"{ident}.html").write_bytes(bruto)
            if status == 200:
                texto = extrair_texto(bruto)
                # gravado em bytes: no Windows, write_text trocaria o fim de linha e o arquivo deixaria de bater com o hash
                bytes_texto = texto.encode("utf-8")
                destino.write_bytes(bytes_texto)
                registro["sha256_texto"] = sha256(bytes_texto)
                registro["caracteres_texto"] = len(texto)
                registro["ok"] = len(texto) > 500
            else:
                registro["ok"] = False
        except Exception as erro:  # rede, tempo esgotado ou navegador
            registro["ok"] = False
            registro["erro"] = type(erro).__name__
        manifesto[ident] = registro
        print(f"{ident}: {'ok' if registro['ok'] else 'FALHOU'} {registro.get('status_http', registro.get('erro'))}")
        time.sleep(1)
    MANIFESTO.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
