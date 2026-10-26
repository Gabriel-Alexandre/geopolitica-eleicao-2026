# Estado

**26/out/2026, 8h:** repositório criado e pré-registro publicado (`docs/PRE_REGISTRO.md`).

**26/out/2026, manhã: F1 feita.** 39 de 42 páginas capturadas com sha256, 33 de 33 citações conferidas palavra por palavra no texto capturado, relatório em [`docs/F1_REACOES.md`](docs/F1_REACOES.md). O que o Trump disse: a fala do *"manual de Joe Biden"* existe e vem de uma origem só, a EFE; não foi post no Truth Social (0 de 19 posts de 25/out falam do Brasil). Putin parabenizou às 6h40 de Brasília, antes do pré-registro: emenda 1 (sai da nota de Brier). Para refazer: `python ferramentas/capturar.py dados/fontes_f1.csv` (e `--navegador` para as que recusam o pedido direto) e `python ferramentas/gerar_f1.py`.

## Próximas fases (do pré-registro)

| Fase | O que sai | Estado |
|---|---|---|
| F0 · Pré-registro | `docs/PRE_REGISTRO.md` | ✅ |
| F1 · As primeiras 72 h | reações oficiais e falas dos dois círculos, capturadas com hash | ✅ 1ª captura (26/out, manhã); novas capturas em 7 dias e na posse |
| F2 · A classe de referência | NELDA e as fichas dos casos, em duas passadas | ⬜ |
| F3 · Os interesses | comércio, investimento, minerais, sanções, votos na ONU | ⬜ |
| F4 · A contestação | critérios C1 a C5, com o projeto `apuracao-segundo-turno-2026` | ⬜ |
| F5 · Síntese | suposições pelas lentes L, F1 e F2, peso das lentes | ⬜ |
| F6 · Teste do passado | Brasil 2022, Honduras 2025, Hungria 2026, com a nota de Brier | ⬜ |
| F7 · Fechamento | validação, revisão adversarial, relatório e gráficos por script | ⬜ |

Mudança de regra depois de hoje: só por emenda, na §13 do pré-registro.
