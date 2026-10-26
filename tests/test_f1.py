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
