"""Confere a linguagem dos textos públicos do projeto (pré-registro §11).

Uso: python ferramentas/conferir_linguagem.py
Acusa: travessão; afirmação de fraude ou de ausência de fraude fora de aspas; julgamento de intenção; recomendação de voto.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVOS = ["README.md", "RELATORIO.md", "RESUMO_SIMPLES.md", "ESTADO.md", "docs/LEITURA_DA_IA.md",
            "docs/REVISAO_ADVERSARIAL.md", "docs/F1_REACOES.md", "docs/F4_CONTESTACAO.md", "docs/PRE_REGISTRO.md"]
PROIBIDOS = [
    (r"—", "travessão"),
    (r"\bhouve fraude\b", "afirma fraude"),
    (r"\bfoi fraudad[ao]\b", "afirma fraude"),
    (r"\b(eleição|resultado) (foi )?roubad[ao]\b", "afirma roubo"),
    (r"\bnão houve fraude\b", "nega fraude fora do veredito"),
    (r"\bprovou que\b", "conclusão mais forte que o dado"),
    (r"\bmentiu\b", "julgamento de pessoa"),
    (r"\b(Trump|Lula|Flávio|Putin|Xi) quer\b", "julga intenção"),
    (r"\bvote (em|no|na)\b", "recomendação de voto"),
]


def hipotetico(antes: str) -> bool:
    """A palavra aparece como hipótese de lente ou como fala relatada ("se houve", "dizem que houve", "lente F")."""
    janela = antes[-45:].lower()
    return any(marca in janela for marca in ("se ", "que ", "lente", "hipótese", "como ", "o resultado é legítimo"))


def fora_de_aspas(linha: str) -> str:
    return re.sub(r"[\"“][^\"”]*[\"”]|\*\"[^\"]*\"\*|`[^`]*`", "", linha)


def main() -> int:
    achados = []
    for nome in ARQUIVOS:
        caminho = RAIZ / nome
        if not caminho.exists():
            continue
        for numero, linha in enumerate(caminho.read_text(encoding="utf-8").splitlines(), 1):
            limpa = fora_de_aspas(linha)
            for padrao, motivo in PROIBIDOS:
                achado = re.search(padrao, limpa if motivo != "travessão" else linha, re.IGNORECASE)
                if achado and motivo != "travessão" and hipotetico(limpa[:achado.start()]):
                    continue
                if achado:
                    achados.append(f"{nome}:{numero}: {motivo}: {linha.strip()[:120]}")
    for achado in achados:
        print(achado)
    print(f"{len(achados)} achados")
    return 1 if achados else 0


if __name__ == "__main__":
    sys.exit(main())
