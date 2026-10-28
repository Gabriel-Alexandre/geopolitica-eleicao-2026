import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def test_toda_citacao_conferida_no_texto_capturado():
    with (RAIZ / "resultados" / "f1_citacoes.csv").open(encoding="utf-8") as arquivo:
        linhas = list(csv.DictReader(arquivo))
    assert linhas and all(linha["conferida"] == "sim" for linha in linhas)


def test_toda_citacao_aponta_para_captura_com_hash():
    manifesto = json.loads((RAIZ / "dados" / "MANIFESTO.json").read_text(encoding="utf-8"))
    with (RAIZ / "dados" / "citacoes_f1.csv").open(encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            assert manifesto[linha["fonte"]].get("ok"), linha["id"]
            assert len(manifesto[linha["fonte"]]["sha256_texto"]) == 64, linha["id"]


def test_o_arquivo_capturado_bate_com_o_hash_do_manifesto():
    import hashlib
    manifesto = json.loads((RAIZ / "dados" / "MANIFESTO.json").read_text(encoding="utf-8"))
    for ident, registro in manifesto.items():
        if registro.get("ok"):
            dados = (RAIZ / "dados" / "capturas" / f"{ident}.txt").read_bytes()
            assert hashlib.sha256(dados).hexdigest() == registro["sha256_texto"], ident


def test_todos_os_scripts_compilam():
    import py_compile
    for script in (RAIZ / "ferramentas").glob("*.py"):
        py_compile.compile(str(script), doraise=True)


def _normal(texto: str) -> str:
    import re
    texto = texto.replace("\u200b", "").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    return re.sub(r"\s+", " ", texto).lower()


def test_rodada_2_toda_citacao_esta_no_texto_capturado_com_hash():
    """Rodada 2 (27/out): cada citação de dados/citacoes_r2.csv aparece, palavra por palavra, na captura com sha256."""
    manifesto = json.loads((RAIZ / "dados" / "MANIFESTO.json").read_text(encoding="utf-8"))
    with (RAIZ / "dados" / "citacoes_r2.csv").open(encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            assert manifesto[linha["fonte"]].get("ok"), linha["id"]
            texto = (RAIZ / "dados" / "capturas" / f"{linha['fonte']}.txt").read_text(encoding="utf-8")
            assert _normal(linha["citacao"]) in _normal(texto), linha["id"]


def test_rodada_3_toda_citacao_esta_no_texto_capturado_com_hash():
    """Rodada 3 (28/out): cada citação de dados/citacoes_r3.csv aparece, palavra por palavra, na captura com sha256."""
    manifesto = json.loads((RAIZ / "dados" / "MANIFESTO.json").read_text(encoding="utf-8"))
    with (RAIZ / "dados" / "citacoes_r3.csv").open(encoding="utf-8") as arquivo:
        for linha in csv.DictReader(arquivo):
            assert manifesto[linha["fonte"]].get("ok"), linha["id"]
            texto = (RAIZ / "dados" / "capturas" / f"{linha['fonte']}.txt").read_text(encoding="utf-8")
            assert _normal(linha["citacao"]) in _normal(texto), linha["id"]


def test_rodada_3_curva_da_noite_copiada_com_hash():
    """A curva oficial da noite, copiada do projeto do vídeo 16, bate com o sha256 registrado em dados/f4_estado_28out.md."""
    import hashlib
    dados = (RAIZ / "dados" / "derivados" / "video16" / "d5_curva_noite.csv").read_bytes()
    assert hashlib.sha256(dados).hexdigest() == "983557aa491f7c3752f30d3395b5c38f56c864f9f89df844abec6ec43af95e5f"
