# F2 · A ficha de cada caso (instrução de codificação)

Regra do pré-registro (§5): cada caso é codificado em **duas passadas independentes**, e a concordância é medida. Quem codifica uma passada **não lê** a outra. Toda afirmação da ficha precisa de **duas fontes** (de preferência uma primária: governo, chancelaria, órgão eleitoral, missão de observação, tribunal; e uma de imprensa de referência ou estudo acadêmico). Caso que não fechar com duas fontes fica com `"fecha_com_duas_fontes": false` e sai da conta.

## Os 25 casos

| id | Caso |
|---|---|
| brasil-2014 | Brasil, presidente, 2º turno de 2014 (Dilma × Aécio) |
| brasil-2018 | Brasil, presidente, 2º turno de 2018 (Bolsonaro × Haddad) |
| brasil-2022 | Brasil, presidente, 2º turno de 2022 (Lula × Bolsonaro) |
| eua-2000 | EUA, presidente, 2000 (Bush × Gore) |
| eua-2020 | EUA, presidente, 2020 (Biden × Trump) |
| mexico-2006 | México, presidente, 2006 (Calderón × López Obrador) |
| peru-2021 | Peru, presidente, 2º turno de 2021 (Castillo × Keiko Fujimori) |
| quenia-2007 | Quênia, presidente, 2007 (Kibaki × Odinga) |
| quenia-2017 | Quênia, presidente, agosto de 2017 (anulada pela Suprema Corte) |
| malaui-2019 | Malaui, presidente, 2019 (anulada e refeita em 2020) |
| romenia-2024 | Romênia, presidente, 1º turno de novembro de 2024 (anulado) |
| venezuela-2013 | Venezuela, presidente, 2013 (Maduro × Capriles) |
| venezuela-2018 | Venezuela, presidente, 2018 |
| venezuela-2024 | Venezuela, presidente, 2024 (Maduro × Edmundo González) |
| nicaragua-2021 | Nicarágua, presidente, 2021 |
| bielorrussia-2020 | Bielorrússia, presidente, 2020 |
| bolivia-2019 | Bolívia, presidente, 2019 |
| ucrania-2004 | Ucrânia, presidente, 2º turno de 2004 (refeito) |
| servia-2000 | Sérvia (Iugoslávia), presidente, 2000 |
| georgia-2003 | Geórgia, parlamento, 2003 (Revolução das Rosas) |
| costa-do-marfim-2010 | Costa do Marfim, presidente, 2º turno de 2010 |
| honduras-2017 | Honduras, presidente, 2017 |
| honduras-2025 | Honduras, presidente, 2025 |
| hungria-2026 | Hungria, parlamento, abril de 2026 |
| argentina-2025 | Argentina, legislativa, outubro de 2025 |

## O formato (um objeto JSON por caso, numa lista)

```json
{
  "caso": "brasil-2022",
  "margem_pontos": 1.8,
  "fraude_demonstrada": "nao",
  "quem_demonstrou_ou_rejeitou": "TSE rejeitou o pedido do PL em 23/11/2022",
  "autoridade_certificou_o_resultado_anunciado": true,
  "observadores": "validaram",
  "perdedor_foi_a_justica": true,
  "eleicao_anulada_ou_refeita": false,
  "governo_ou_candidato_paralelo_reconhecido_por_alguma_potencia": false,
  "relacao_do_vencedor": {"eua": "neutro", "china": "proximo", "russia": "proximo"},
  "reacao": {
    "eua":    {"tipo": "parabens", "dias_ate_parabens": 0, "quem": "Biden", "data": "2022-10-30"},
    "china":  {"tipo": "parabens", "dias_ate_parabens": 1, "quem": "porta-voz; Xi depois", "data": "2022-10-31"},
    "russia": {"tipo": "parabens", "dias_ate_parabens": 1, "quem": "Putin", "data": "2022-10-31"},
    "ue":     {"tipo": "parabens", "dias_ate_parabens": 0, "quem": "Borrell / von der Leyen", "data": "2022-10-30"}
  },
  "eua_sancao_ou_corte_ligado_a_eleicao_em_12_meses": false,
  "vencedor_anunciado_tomou_posse": true,
  "violencia_relevante_depois_da_eleicao": true,
  "fontes": ["https://...", "https://..."],
  "fecha_com_duas_fontes": true,
  "notas": "uma ou duas frases"
}
```

### Valores permitidos

| Campo | Valores |
|---|---|
| `fraude_demonstrada` | `sim` (demonstrada por tribunal, órgão eleitoral ou missão de observação com prova pública) · `nao` (alegada e rejeitada, ou não alegada) · `disputado` (há relatório que aponta e relatório sério que contesta) |
| `observadores` | `validaram` · `apontaram_problemas_graves` · `parcial` · `sem_missao_relevante` |
| `relacao_do_vencedor.*` | `aliado`/`proximo` · `neutro` · `adversario` |
| `reacao.*.tipo` | `parabens` (mensagem de cumprimento ao vencedor) · `nota_sem_parabens` (reconhece ou fala do processo sem cumprimentar) · `silencio` (nada em 30 dias) · `questionou` (põe o resultado em dúvida sem ato formal) · `nao_reconheceu` (declara o resultado ilegítimo ou reconhece outro) · `nao_se_aplica` (a própria eleição da potência) |
| `reacao.*.dias_ate_parabens` | dias entre o anúncio do resultado e os parabéns; `null` se não houve |

## Como trabalhar

- Os **dois lados**: em cada caso, procure tanto o que sustenta a acusação de fraude quanto o que a rejeita, e registre a conclusão das instituições e dos observadores, não a sua.
- Datas exatas sempre que achar; se a data for aproximada, diga nas notas.
- Não invente: campo sem fonte fica `null` e a nota diz por quê.
