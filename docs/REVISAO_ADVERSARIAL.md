# Revisão adversarial (26/out/2026)

Três leitores independentes, cada um uma instância da IA em contexto separado, leram o projeto inteiro depois da primeira síntese. Os textos completos estão em [`docs/revisao/`](revisao/):

| Leitor | Papel | Arquivo |
|---|---|---|
| Defensor da lente F | a versão mais forte da hipótese de que o resultado foi fraudado ou não reflete a vontade do eleitor | [`defensor_lente_F.md`](revisao/defensor_lente_F.md) |
| Defensor da lente L | a versão mais forte da hipótese de que o resultado é legítimo e as dúvidas são de procedimento | [`defensor_lente_L.md`](revisao/defensor_lente_L.md) |
| Auditor | método, números refeitos a partir dos dados, linguagem e o que falta para um terceiro refazer | [`auditor.md`](revisao/auditor.md) |

## O que mudou por causa da revisão

| Objeção | De quem | O que foi feito |
|---|---|---|
| C3 e C5 contados como "apontam L" contra a régua do próprio projeto (prazo de 14 horas; fontes de uma origem ou de resumo de busca) | lente F e auditor | aceita: os dois viram *sem dado* (emenda 4). O veredito de lente passou de "2 de 5 apontam L" para "nenhum critério tem dado suficiente" |
| O C1 mede votos acrescentados e não eleitores impedidos de votar | lente F | aceita: C1 ganhou a parte b (emenda 4) e o relatório publica o teto das duas pontas |
| O rótulo "aberta" põe as duas lentes no mesmo pé sem mostrar o tamanho que cada queixa precisaria ter | lente L | aceita: o teto das duas pontas (relatório §3.1) mostra quantos votos acrescentados ou quantos eleitores impedidos seriam precisos |
| "Nenhuma eleição sem fraude demonstrada foi anulada" depende de como o Quênia 2017 e o Malaui 2019 foram codificados | lente F | aceita: variante V1; a S1 na lente L subiu de quase nenhuma chance para muito improvável |
| A lente F do histórico juntava fraude demonstrada e disputada sem dizer | auditor | aceita: emenda 4 e variante V3, que mostra que os dois grupos se comportam de forma oposta |
| A relação do Lula com os EUA em 2026 não estava declarada | lente L | aceita: declarada neutra, como em 2014 e 2022 (emenda 4), com a variante adversário publicada (V2) |
| A coluna F1 não usava as taxas do grupo F (S4, S8) | lente F | aceita em parte: S8 em F1 desceu para provável. A S4 em F1 chegou a subir para provável e voltou para improvável na releitura do roteiro (26/out): a suposição vai até 2027, e na Bolívia de 2019, com a eleição anulada, os EUA reconheceram a presidente interina |
| Sinais de distensão nas próprias capturas (sanção a Moraes retirada, tarifa sobre alimentos derrubada) não entravam na S8 | lente L | aceita: entraram no porquê da S8 |
| A Hungria 2026 entrava para baixar a S5 e não era citada na S7 | lente L | aceita: a S7 agora cita a Hungria como evidência contra |
| A H1 caía por "nenhuma nota em 24 h" quando só tinham passado umas 13 horas | lente L | aceita: texto corrigido |
| A H9 era narrativa, não contagem | lente L e auditor | aceita: a contagem pelos casos pré-registrados está na tabela de hipóteses |
| A regra da §6 não estava aplicada por escrito (H2 e H3) | auditor | aceita: escrita na tabela de hipóteses |
| Kappa mediano 0,93 com a mediana real de 0,92; F1 contando 49 páginas | auditor | aceita: corrigidos no script |
| Teste do passado usava casos posteriores ao caso testado | auditor | aceita: publicado também só com casos anteriores (0,214) e contra a taxa geral (0,224); o método continua melhor que as duas referências |
| O conferidor de linguagem deixava passar uma negação de fraude | auditor | aceita: conferidor reescrito, agora acusa a frase de teste |
| Frases mais fortes que o dado ("virou restrição de visto", "votou igual", "não foi post", a premissa da lente F2 dita como fato) | auditor | aceita: reescritas |
| Fonte do comércio, NELDA, Laplace, prazo da S12, fontes da F4 sem hash, ordem da emenda 2 | auditor | aceita: emenda 5; fontes da F4 capturadas (41 de 46) |
| Independência das passadas não documentada | auditor | aceita: registrada em `docs/F2_FICHA.md`, com o limite de serem o mesmo modelo |

## O que não mudou, e por quê

| Objeção | De quem | Por que não mudou |
|---|---|---|
| A S6 deveria ser provável, pelo histórico da lente L | lente L | a fala do presidente relatada pela EFE e o silêncio do governo pesam contra; a faixa ficou em chance parecida e a objeção está publicada |
| Áustria 2016 deveria entrar na classe de referência | lente F | conferida só numa fonte; pela emenda 2, caso sem duas fontes não entra. Citada aqui como o caso que mais reforçaria a variante V1 |
| O C1 deveria usar o número do g1 | lente L | a emenda 3 manda esperar os logs; o número entra só no teto das duas pontas, com a ressalva |
| Eduardo Bolsonaro e Paulo Figueiredo não falam pelo Trump | lente L | ficam na tabela da F1 com o vínculo descrito como "aliados brasileiros do Flávio que moram nos EUA", sem pesar como fala do governo |
| A validação independente cobre pouco do teste do passado | auditor | limite registrado: os números do teste do passado foram refeitos pelo auditor, não por um script independente |
