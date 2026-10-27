# Estado

**27/out/2026 (rodada 2):** os critérios C1, C2, C3 e C5 ganharam dado (do projeto do vídeo 16 e das fontes de 27/out); veredito de lente: **L na frente, sem prova para nenhum lado** (emenda 6). O que mudou: [`docs/RODADAS.md`](docs/RODADAS.md).

**26/out/2026 (rodada 1):** todas as fases do pré-registro rodaram com o que existia até a manhã de 26/out. Comece pelo [`RESUMO_SIMPLES.md`](RESUMO_SIMPLES.md) e pelo [`RELATORIO.md`](RELATORIO.md).

| Fase | O que saiu | Estado |
|---|---|---|
| F0 · Pré-registro | `docs/PRE_REGISTRO.md` (`0f72f8e`) e as emendas 1 a 5 (§13) | ✅ |
| F1 · As primeiras horas | 39 de 42 páginas com sha256, 33 de 33 citações conferidas: [`docs/F1_REACOES.md`](docs/F1_REACOES.md) | ✅ 1ª captura; ⬜ nova captura em 02/nov e na posse (§9 do pré-registro) |
| F2 · O histórico | 25 casos em duas passadas independentes, 19 na conta, concordância e kappa em `resultados/f2_concordancia.csv` | ✅ |
| F3 · Os interesses | comércio, adubos, votos na ONU, terras raras e as medidas dos EUA, com sha256 em `dados/MANIFESTO_F3.json` | ✅ |
| F4 · A contestação | critérios C1 a C5 em [`docs/F4_CONTESTACAO.md`](docs/F4_CONTESTACAO.md) e o levantamento dos dois lados em `dados/f4_estado_26out.md` (41 de 46 fontes com sha256) | ✅ rodada 2 (27/out): C1, C2 e C5 (parcial) apontam L, C3 aponta L provisório, C4 sem dado; levantamento em `dados/f4_estado_27out.md` |
| F5 · Síntese | as 12 suposições pelas lentes L, F1 e F2 em `dados/sintese_suposicoes.csv` e no relatório | ✅ |
| F6 · Teste do passado | deixa-um-de-fora em `resultados/f6_teste_do_passado.csv` | ✅ |
| F7 · Fechamento | validação independente, revisão adversarial, relatório, resumo, leitura da IA, 8 gráficos | ✅ |

## O que falta, e quando

- **C3, C4 e C5:** o julgamento das ações de cassação, a conclusão da PF e o relatório da OEA, e o consolidado do teste de integridade (até 30 dias). Quando sair, nova rodada: atualizar `dados/criterios_c1_c5.csv` e rodar `graficos.py` e `gerar_relatorio.py`.
- **O caso do Flávio:** a S13 (asilo ou recusa de entregar) resolve até 05/jan/2027.
- **Conferir as suposições:** cada uma tem prazo e critério de resolução na §8 do pré-registro (02/nov, 25/nov, 05/jan/2027 e fim de 2027).

## Como refazer tudo

Ver a §8 do `RELATORIO.md`.
