"""Captura um PDF (relatório oficial), extrai o texto e registra tudo com sha256, no mesmo padrão de capturar.py.

Uso: python ferramentas/capturar_pdf.py <id> <url>
- PDF bruto em dados/brutos/<id>.pdf (fora do git)
- texto extraído (pypdf) em dados/capturas/<id>.txt (no git)
- endereço, hora, status, tamanho e sha256 em dados/MANIFESTO.json
"""
import hashlib
import io
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests
from pypdf import PdfReader

sys.path.insert(0, str(Path(__file__).resolve().parent))
from capturar import CABECALHO, tarjar  # noqa: E402

RAIZ = Path(__file__).resolve().parent.parent
MANIFESTO = RAIZ / "dados" / "MANIFESTO.json"


def main() -> None:
    ident, url = sys.argv[1], sys.argv[2]
    registro = {"url": url, "capturado_em_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "metodo": "pedido direto (requests), PDF lido com pypdf"}
    resposta = requests.get(url, headers=CABECALHO, timeout=60)
    bruto = resposta.content
    registro.update(status_http=resposta.status_code, bytes_pdf=len(bruto), sha256_pdf=hashlib.sha256(bruto).hexdigest())
    (RAIZ / "dados" / "brutos" / f"{ident}.pdf").write_bytes(bruto)
    paginas = [p.extract_text() or "" for p in PdfReader(io.BytesIO(bruto)).pages]
    texto = tarjar(f"TITULO: PDF {url}\n\n" + "\n".join(paginas) + "\n")
    dados = texto.encode("utf-8")
    (RAIZ / "dados" / "capturas" / f"{ident}.txt").write_bytes(dados)
    registro.update(sha256_texto=hashlib.sha256(dados).hexdigest(), caracteres_texto=len(texto), paginas=len(paginas),
                    ok=resposta.status_code == 200 and len(texto) > 500)
    manifesto = json.loads(MANIFESTO.read_text(encoding="utf-8"))
    manifesto[ident] = registro
    MANIFESTO.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2), encoding="utf-8")
    print(ident, "ok" if registro["ok"] else "FALHOU", registro["status_http"], registro.get("paginas"))


if __name__ == "__main__":
    main()
