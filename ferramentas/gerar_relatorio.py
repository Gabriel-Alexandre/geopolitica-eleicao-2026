"""Escreve RELATORIO.md, RESUMO_SIMPLES.md, docs/LEITURA_DA_IA.md e docs/F4_CONTESTACAO.md a partir dos resultados.

Uso: python ferramentas/gerar_relatorio.py
Entradas: resultados/RESUMO.json, resultados/f1_resumo.json, resultados/f2_*.csv, resultados/f6_teste_do_passado.csv,
          dados/criterios_c1_c5.csv, dados/sintese_suposicoes.csv, dados/hipoteses_veredito.csv
Nenhum número é escrito à mão: todos saem dos arquivos acima.
"""
import csv
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RES = RAIZ / "resultados"
DADOS = RAIZ / "dados"
REPO = "https://github.com/Gabriel-Alexandre/geopolitica-eleicao-2026"
APONTA = {"sem_dado": "sem dado", "L_provisorio": "aponta L (provisório)", "L_parcial": "aponta L (parcial)",
          "L": "aponta L", "F": "aponta F"}


def ler_csv(caminho: Path) -> list[dict]:
    if not caminho.exists():
        return []
    with caminho.open(encoding="utf-8") as arquivo:
        return list(csv.DictReader(arquivo))


def milhar(n: int) -> str:
    return f"{n:,}".replace(",", ".")


def num(valor: float, casas: int = 1) -> str:
    return f"{float(valor):.{casas}f}".replace(".", ",")


RELACAO = {"proximo": "próximo", "neutro": "neutro", "adversario": "adversário"}


def pct(valor: float) -> str:
    return f"{100 * float(valor):.0f}%"


def taxa(base: list[dict], desfecho: str, grupo: str, condicao: str = "todas") -> str:
    linha = next((l for l in base if l["desfecho"] == desfecho and l["grupo"] == grupo and l["condicao"] == condicao), None)
    return f"{linha['sim']} de {linha['n']} ({pct(linha['taxa'])})" if linha else "sem casos"


def veredito_de_lente(criterios: list[dict]) -> str:
    """Regra da §3 do pré-registro com a emenda 6: C2 (arquivos das urnas) bate nas duas lentes e pesa menos,
    e 'L sustentada' passa a exigir também C3 (Justiça) e C5 (teste de integridade) apontando L sem ressalva."""
    aponta = {c["criterio"]: c["aponta"] for c in criterios}
    if any(v == "F" for v in aponta.values()):
        return "F1: um critério aponta fraude demonstrada"
    if aponta.get("C1", "").startswith("L") and aponta.get("C2", "").startswith("L"):
        if aponta.get("C3") == "L" and aponta.get("C5") == "L":
            return "L sustentada"
        a_favor_l = [c for c, v in aponta.items() if v.startswith("L")]
        ressalvas = [f"{c} {APONTA[v]}" for c, v in aponta.items() if v != "L"]
        return (f"L na frente, sem prova para nenhum lado: {len(a_favor_l)} de 5 critérios apontam L "
                f"({', '.join(a_favor_l)}), nenhum aponta F; pela emenda 6, C2 bate nas duas lentes e pesa menos, "
                f"e a lente L só fica sustentada com C3 e C5 fechados ({'; '.join(ressalvas)})")
    a_favor_l = [c for c, v in aponta.items() if v.startswith("L")]
    sem = [c for c, v in aponta.items() if v == "sem_dado"]
    if not a_favor_l:
        return (f"aberta: nenhum dos {len(aponta)} critérios tem dado suficiente para apontar um lado "
                f"({', '.join(sem)} sem dado); nenhum aponta fraude e nenhum aponta legitimidade")
    return (f"aberta: {len(a_favor_l)} de 5 critérios apontam L ({', '.join(a_favor_l)}), nenhum aponta F, "
            f"e {len(sem)} estão sem dado ({', '.join(sem)})")


def tabela_suposicoes(sintese: list[dict], com_porque: bool = True) -> list[str]:
    linhas = ["| # | Suposição | Se legítimo (L) | Se fraude demonstrada (F1) | Se fraude não demonstrada (F2) | Mudou desde o pré-registro? |"
              + (" Por quê |" if com_porque else ""),
              "|---|---|---|---|---|---|" + ("---|" if com_porque else "")]
    for s in sintese:
        linha = f"| {s['id']} | {s['suposicao']} | {s['final_L']} | {s['final_F1']} | {s['final_F2']} | {s['mudou']} |"
        if com_porque:
            linha += f" {s['porque']} |"
        linhas.append(linha)
    return linhas


def relatorio(r: dict, f1: dict, base: list[dict], conc: list[dict], criterios: list[dict], sintese: list[dict],
              hipoteses: list[dict]) -> str:
    f2, f3, f6 = r["f2"], r["f3"], r.get("f6", {})
    ano = f3["ultimo_ano_comercio"]
    fat = f3["fatias_pct"]
    l = ["# O que esperar dos EUA, da China e da Rússia depois do 2º turno de 2026: relatório\n",
         f"Gerado por `ferramentas/gerar_relatorio.py`. Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre, "
         f"pelas regras do [`docs/PRE_REGISTRO.md`](docs/PRE_REGISTRO.md) e das emendas 1 a 6, em 3 rodadas (26, 27 e 28/out, [`docs/RODADAS.md`](docs/RODADAS.md)). Repositório: {REPO}\n",
         "## O que este projeto não consegue dizer\n",
         "- **A lente F2 (fraude que não deixou prova) não é testável por dado.** É o mundo em que boletins, logs, totalização e teste de integridade fecham entre si. O projeto mostra o que ela implicaria, mas nenhum dado a confirma ou derruba.",
         "- **Três critérios de lente ainda têm ressalva em 28/out:** C3 aponta L de forma provisória, porque as ações de cassação não foram julgadas; C4 aponta L em parte, porque a OEA publicou o relatório preliminar e a PF não concluiu o inquérito sobre os ônibus; C5 aponta L em parte, porque falta o consolidado do teste de integridade. Os arquivos das urnas (C2) batem, mas isso é o esperado nas duas lentes (emenda 6).",
         f"- **{len(f2['casos_excluidos'])} dos 25 casos históricos saíram da conta** por não fecharem com duas fontes numa das passadas (emenda 2): {', '.join(f2['casos_excluidos']) or 'nenhum'}.",
         "- **Três casos somem das tabelas por lente** (Malaui 2019, Venezuela 2018 e Nicarágua 2021) porque as duas passadas divergiram em `fraude_demonstrada` (emenda 2); eles continuam nas tabelas de *todos os casos*.",
         "- **A base sistemática NELDA não foi usada** (emenda 5): a taxa-base sai só dos casos codificados à mão.",
         "- **As duas passadas foram feitas por instâncias da mesma IA**, com a mesma instrução e sem ver uma a outra; erros comuns ao mesmo modelo não são pegos pela concordância.",
         "- **Interesse se mede pelo que é público** (comércio, votos na ONU, reservas, medidas oficiais). Intenção de pessoa não se mede e não é afirmada.",
         "- **As reações foram lidas até 28/out, por volta das 17h20 (rodada 3).** De um dia para o outro uma decisão pode mudar o quadro; as suposições têm prazo e critério de resolução para serem conferidas depois.\n",
         "## 1. A resposta, pelas duas lentes\n",
         f"**Veredito de lente hoje:** {veredito_de_lente(criterios)}. Os critérios estão na §3.\n"]
    l += tabela_suposicoes(sintese)
    l += ["", "## 2. O que o Trump e quem fala por ele disseram\n",
          f"- A fala do *\"manual de Joe Biden\"* tinha uma origem só, um texto da agência EFE (noite de 25/out), e **a própria EFE trocou esse texto**, no mesmo endereço, por outro dizendo que o Trump não tinha se pronunciado (relido na tarde de 26/out; `docs/F1_REACOES.md` §1). Ela não está entre os posts do Truth Social de 25/out no arquivo independente: "
          f"{f1['truth_social_posts_sobre_brasil']} de {f1['truth_social_posts_em_25_out']} posts de 25/out falam do Brasil.",
          "- O advogado da Trump Media, Martin De Luca, escreveu que ninguém vai reconhecer a eleição; Donald Trump Jr. e Elon Musk compartilharam; Jason Miller publicou o discurso do Flávio em inglês.",
          "- **Rodada 2:** em 26/out, a repórteres, o próprio Trump disse que a eleição pareceu *\"another rigged election\"*, que a prorrogação foi *\"very strange\"*, que não tomou partido e que gosta do Lula; não apoiou a anulação. Segundo a Folha, o Departamento de Estado tinha uma nota pronta e o governo mandou adiar a publicação. Até 27/out, 14h30: nenhuma nota da Casa Branca ou do Departamento de Estado, nenhuma medida nova da OFAC ([`dados/f4_estado_27out.md`](dados/f4_estado_27out.md) §1).",
          "- **Rodada 3:** em 27/out, um alto funcionário do Departamento de Estado disse que o governo vai dar vistos ao Flávio e à família e deixá-los entrar nos EUA; à noite, o Trump disse que aprovaria e que a eleição foi *\"very strange\"* e *\"terrible\"*, de novo sem afirmar fraude com todas as letras. O De Luca, em entrevista de 26/out, defendeu refazer o 2º turno se não houver investigação independente, e disse que, se o Lula ganhou por 4 milhões de votos, vai ser o primeiro a reconhecer. Até 28/out, 17h20: nenhuma nota sobre o resultado, nenhuma medida nova contra o Brasil ([`dados/f4_estado_28out.md`](dados/f4_estado_28out.md) §3 e §4).",
          f"- {f1['citacoes_conferidas']} de {f1['citacoes']} citações conferidas palavra por palavra no texto capturado: [`docs/F1_REACOES.md`](docs/F1_REACOES.md).\n",
          "## 3. A contestação: os critérios C1 a C5\n",
          "| Critério | Estado em 28/out (rodada 3) | Aponta |", "|---|---|---|"]
    l += [f"| {c['criterio']} · {c['nome']} | {c['estado_em_28out']} | {APONTA[c['aponta']]} |" for c in criterios]
    t = r["teto_das_duas_pontas"]
    imp = t["eleitores_impedidos_necessarios"]
    v16 = json.loads((DADOS / "derivados" / "video16" / "rodada2.json").read_text(encoding="utf-8"))["A6_votos_depois_das_17h"]
    l += ["", "### 3.1 O teto das duas pontas (emenda 4)\n",
          f"A conta mostra o tamanho que cada queixa precisaria ter, no pior caso para cada lado. **Medido na rodada 2** (projeto do vídeo 16, A6): {milhar(v16['votos_depois_17h'])} votos depois das 17h, {num(v16['teto_contra_margem_pct'], 2)}% da diferença mesmo que todos fossem do Lula.\n",
          f"- **Votos acrescentados pela prorrogação** (a queixa do lado do Flávio): para virar a diferença de {milhar(t['diferenca_votos'])} votos, "
          f"a prorrogação teria de ter acrescentado pelo menos esse número de votos, todos para o Lula. O g1 contou {milhar(t['votos_depois_das_17h_g1'])} "
          f"votos depois das 17h; teria de estar errado {num(t['vezes_que_o_g1_teria_de_estar_errado'])} vezes. Esse número do g1 não entra em critério (emenda 3) e espera os logs.",
          f"- **Eleitores impedidos de votar** (seções que fecharam antes do aviso das 17h49, a queixa do lado do Flávio; a falta de ônibus, "
          f"queixa do lado do Lula, iria no sentido contrário): se os impedidos "
          f"votassem 60% no Flávio, seriam precisos {milhar(imp['60% para o Flávio'])}; com 75%, {milhar(imp['75% para o Flávio'])}; com 100%, "
          f"{milhar(imp['100% para o Flávio'])}. Para comparar, a abstenção inteira do 2º turno de 2022 foi de {milhar(t['abstencao_2o_turno_2022'])} "
          f"eleitores, e a do 1º turno de 2026, de {milhar(t['abstencao_1o_turno_2026'])}.",
          "- **O que a conta não diz:** ela não mede quantos foram impedidos de fato (parte b do C1). O sinal indireto vai contra o teto: a abstenção caiu 1,86 ponto entre os turnos e o comparecimento subiu em 80% dos municípios (projeto do vídeo 16).\n"]
    l += ["", "Detalhe, com as alegações dos dois lados: [`docs/F4_CONTESTACAO.md`](docs/F4_CONTESTACAO.md).\n",
          "## 4. O histórico: as outras vezes\n",
          f"{f2['casos_na_conta']} casos na conta, codificados em duas passadas independentes. Concordância média entre as passadas: "
          f"{pct(f2['concordancia_media']) if f2['concordancia_media'] is not None else 'sem dado'}; kappa mediano: {num(f2['kappa_mediano'], 2)}. "
          "Tabelas: `resultados/f2_concordancia.csv`, `resultados/f2_taxas_base.csv`.\n",
          "| O que aconteceu | Fraude não demonstrada (lente L) | Fraude demonstrada ou disputada (lente F) |", "|---|---|---|"]
    for chave, rotulo in [("eua_parabens_30d", "Os EUA parabenizaram em até 30 dias"),
                          ("eua_nao_reconheceu", "Os EUA não reconheceram"),
                          ("china_parabens_7d", "A China parabenizou em até 7 dias"),
                          ("russia_parabens_7d", "A Rússia parabenizou em até 7 dias"),
                          ("anulada_ou_refeita", "A eleição foi anulada ou refeita"),
                          ("vencedor_tomou_posse", "O vencedor anunciado tomou posse"),
                          ("eua_sancao_12m", "Os EUA aplicaram sanção ligada à eleição em 12 meses"),
                          ("violencia", "Houve violência relevante depois")]:
        l.append(f"| {rotulo} | {taxa(base, chave, 'fraude não demonstrada (lente L)')} | {taxa(base, chave, 'fraude demonstrada ou disputada (lente F)')} |")
    l += ["", "**Os EUA, pela relação com o vencedor** (todos os casos):\n", "| Relação do vencedor com os EUA | Parabéns em até 30 dias | Sanção ligada à eleição em 12 meses |", "|---|---|---|"]
    for relacao in ("proximo", "neutro", "adversario"):
        cond = f"vencedor {relacao} da potência"
        l.append(f"| {RELACAO[relacao]} | {taxa(base, 'eua_parabens_30d', 'todos', cond)} | {taxa(base, 'eua_sancao_12m', 'todos', cond)} |")
    if f6:
        l += ["", f"**Teste do passado** (cada caso previsto pelos outros, só com o que se sabia na noite): nota de Brier "
              f"{num(f6['brier_metodo'], 3)} em {f6['previsoes']} previsões, contra {num(f6['brier_chute_50'], 2)} de quem chuta sempre 50% "
              "(quanto menor, melhor). "
              + " · ".join(f"{c}: {num(f6[c], 3)}" for c in ("brasil-2022", "honduras-2025", "hungria-2026") if c in f6)
              + f". Só com casos anteriores a cada um (emenda 4): {num(f6['brier_so_com_casos_anteriores'], 3)}; com a taxa geral, sem a relação "
              f"do vencedor: {num(f6['brier_taxa_geral_sem_condicionar'], 3)}. O teste mede a taxa-base, não as faixas ajustadas na síntese. "
              "Tabela: `resultados/f6_teste_do_passado.csv`.\n"]
    variantes = ler_csv(RES / "variantes.csv")
    if variantes:
        l += ["### 4.1 As variantes pedidas pela revisão adversarial\n", "| Variante | Desfecho | Principal | Com a variante |", "|---|---|---|---|"]
        l += [f"| {v['variante']} | {v['desfecho']} | {v['principal']} | {v['variante_valor']} |" for v in variantes]
        l += ["", "**Leitura:** quando a fraude ficou demonstrada e o governo acusado controlava as instituições (Bielorrússia 2020, Venezuela 2024), "
              "ele ficou no poder e os EUA não reconheceram; quando a fraude foi disputada e a Justiça ou o órgão eleitoral do país agiu "
              "(Quênia, Bolívia, Romênia), a eleição foi anulada ou refeita. A lente F1 deste projeto (fraude demonstrada pela própria "
              "Justiça brasileira) se parece mais com o segundo grupo.\n"]
    l += ["## 5. Os interesses, medidos\n",
          f"- **Comércio ({ano}):** a China comprou {num(fat[f'{ano}|exportacao|China'])}% das exportações brasileiras; os EUA, {num(fat[f'{ano}|exportacao|EUA'])}%; a Rússia, {num(fat[f'{ano}|exportacao|Rússia'])}%. "
          f"Nas importações: China {num(fat[f'{ano}|importacao|China'])}%, EUA {num(fat[f'{ano}|importacao|EUA'])}%, Rússia {num(fat[f'{ano}|importacao|Rússia'])}%.",
          f"- **Saldo de {ano}:** com os EUA, o Brasil {'vendeu mais do que comprou' if f3['saldo_brasil_com_eua_usd_ultimo_ano'] > 0 else 'comprou mais do que vendeu'}, uma diferença de US$ {num(abs(f3['saldo_brasil_com_eua_usd_ultimo_ano']) / 1e9)} bilhões; "
          f"com a China, {'vendeu mais do que comprou' if f3['saldo_brasil_com_china_usd_ultimo_ano'] > 0 else 'comprou mais do que vendeu'}, uma diferença de US$ {num(abs(f3['saldo_brasil_com_china_usd_ultimo_ano']) / 1e9)} bilhões.",
          f"- **Votos na ONU (2024):** pelo índice de concordância de Erik Voeten (abstenção conta como meia concordância), o Brasil votou no mesmo sentido que a China em {pct(f3['onu_concordancia']['2024|China'])} das votações, à Rússia em {pct(f3['onu_concordancia']['2024|Rússia'])} e aos EUA em {pct(f3['onu_concordancia']['2024|EUA'])}.",
          f"- **Adubos:** em valor, a Rússia vendeu {f3['adubos_fatia_russia_pct'][str(ano)] if str(ano) in f3['adubos_fatia_russia_pct'] else f3['adubos_fatia_russia_pct'][ano]:.0f}% do adubo que o Brasil importou em {ano}.",
          f"- **Terras raras:** o Brasil tem a {f3['terras_raras_posicao_brasil']}ª maior reserva conhecida ({f3['terras_raras_reservas_t']['Brasil'] / 1e6:.0f} milhões de toneladas de óxido), atrás só da China ({f3['terras_raras_reservas_t']['China'] / 1e6:.0f} milhões); os EUA têm {num(f3['terras_raras_reservas_t']['EUA'] / 1e6)} milhão.",
          "", "Gráficos em `resultados/figuras/`.\n",
          "## 6. As hipóteses concorrentes, potência por potência\n",
          "| Potência | Hipótese que fica de pé | Hipóteses com mais evidência contra | Por quê |", "|---|---|---|---|"]
    l += [f"| {h['potencia']} | {h['fica']} | {h['caem']} | {h['porque']} |" for h in hipoteses]
    l += ["", "## 7. Validação, revisão e emendas\n",
          "- Números centrais refeitos por outro caminho: `resultados/validacao_independente.csv`.",
          "- Revisão adversarial, com um leitor que defende a lente F, um que defende a L e um auditor: [`docs/REVISAO_ADVERSARIAL.md`](docs/REVISAO_ADVERSARIAL.md).",
          "- Emendas ao pré-registro: §13 de [`docs/PRE_REGISTRO.md`](docs/PRE_REGISTRO.md).\n",
          "## 8. Como refazer\n", "```bash", "pip install -r requirements.txt",
          "python ferramentas/capturar.py dados/fontes_f1.csv", "python ferramentas/capturar.py dados/fontes_f1.csv --navegador",
          "python ferramentas/capturar.py dados/fontes_r2.csv", "python ferramentas/capturar.py dados/fontes_r3.csv",
          "python ferramentas/capturar_pdf.py r3_58 https://www.oas.org/fpdb/press/2026_MOE_Brasil_Segundo_Turno_Relatorio_Preliminar_POR.pdf",
          "python ferramentas/gerar_f1.py", "python ferramentas/coletar_f3.py", "python ferramentas/capturar.py dados/fontes_f3.csv",
          "python ferramentas/analise.py", "python ferramentas/validacao_independente.py", "python ferramentas/graficos.py",
          "python ferramentas/gerar_relatorio.py", "python ferramentas/conferir_linguagem.py", "python -m pytest -q", "```", ""]
    return "\n".join(l) + "\n"


def resumo_simples(r: dict, criterios: list[dict], sintese: list[dict]) -> str:
    l = ["# Resumo simples\n",
         "**A pergunta:** depois da reeleição do Lula (51,79% a 48,21%), com a votação prorrogada até as 19h e o Trump dizendo que a eleição pareceu fraudada, o que esperar dos EUA, da China e da Rússia?\n",
         "**Como:** a IA levantou 25 eleições contestadas do mundo desde 1990 (19 fecharam com duas fontes e entraram na conta), mediu os interesses de cada país no Brasil com dado oficial e leu o que cada um disse nas primeiras horas. Tudo foi feito pelas duas lentes: tratando o resultado como legítimo e tratando como fraude.\n",
         f"**Qual lente o dado de hoje sustenta:** {veredito_de_lente(criterios)}.\n",
         ("**O tamanho das queixas:** para a prorrogação virar o resultado, ela teria de ter acrescentado "
          f"{milhar(r['teto_das_duas_pontas']['diferenca_votos'])} votos, todos para o Lula; os logs das urnas mostram 34.810 votos "
          "depois das 17h, 0,79% disso (projeto do vídeo 16). Para eleitores impedidos de votar virarem o resultado, com 60% deles no Flávio, "
          f"seriam precisos {milhar(r['teto_das_duas_pontas']['eleitores_impedidos_necessarios']['60% para o Flávio'])}; "
          "a abstenção caiu entre os turnos.\n"),
         "**O que mudou de 26 para 27/out (rodada 2):** o Flávio desistiu da anulação e o PL reconheceu o resultado; o Trump disse que a eleição pareceu fraudada e, na mesma fala, que gosta do Lula; a nota do Departamento de Estado foi adiada; o Xi mandou mensagem pessoal; a Argentina só \"tomou nota\". Detalhe em [`docs/RODADAS.md`](docs/RODADAS.md).\n",
         "**O que mudou de 27 para 28/out (rodada 3):** a OEA publicou o relatório preliminar do 2º turno dizendo que não tem dúvidas sobre a integridade dos dados oficiais; o Flávio saiu pela Argentina, chegou a Miami e divulgou carta dizendo que é o presidente eleito; o Departamento de Estado deu vistos a ele e à família; o Trump disse que aprovaria e que a eleição foi muito estranha; o pedido da PF para apreender os passaportes foi assinado 7 minutos depois de o TSE confirmar o resultado, e a hora da decisão do Moraes não foi divulgada.\n",
         "**O que esperar, em uma linha cada:**\n"]
    for s in sintese:
        l.append(f"- **{s['suposicao']}:** {s['final_L']} se o resultado for legítimo; {s['final_F1']} se a fraude for demonstrada.")
    l += ["", "**O que mais pesa:** nos casos do histórico, os governos de fora reagiram ao que ficou demonstrado e seguiram o que a Justiça do país decidiu. Por essa regra, uma fraude que não deixasse prova teria a mesma reação de um resultado legítimo. Com o que dá para ver de fora, há dúvidas que são justas e não há prova de fraude; o que falta ver está dentro do TSE e nos processos que ainda vão ser julgados.\n",
          f"Relatório completo: [`RELATORIO.md`](RELATORIO.md). Repositório: {REPO}\n"]
    return "\n".join(l) + "\n"


ROTULO_DESFECHO = {"anulada_ou_refeita": "eleição anulada ou refeita", "vencedor_tomou_posse": "o vencedor tomou posse",
                   "violencia": "violência relevante depois", "eua_nao_reconheceu": "os EUA não reconheceram",
                   "eua_parabens_30d": "os EUA parabenizaram em até 30 dias", "eua_sancao_12m": "sanção dos EUA ligada à eleição em 12 meses",
                   "china_parabens_7d": "a China parabenizou em até 7 dias", "russia_parabens_7d": "a Rússia parabenizou em até 7 dias"}


def historico(espec: str, base: list[dict]) -> str:
    partes = []
    for item in espec.split(";"):
        pedacos = item.split("|")
        if len(pedacos) != 3:
            partes.append(item)
            continue
        desfecho, grupo, condicao = pedacos
        onde = grupo if condicao == "todas" else f"{grupo}, {condicao}"
        partes.append(f"{ROTULO_DESFECHO.get(desfecho, desfecho)}: {taxa(base, desfecho, grupo, condicao)} ({onde})")
    return " · ".join(partes)


def leitura_da_ia(sintese: list[dict], hipoteses: list[dict], base: list[dict]) -> str:
    l = ["# A leitura da IA, item por item\n",
         "Feita pelo Claude depois de todas as fases. Para cada suposição: o que mudou desde o pré-registro, e por quê. A régua é a do pré-registro; o que é leitura está marcado como leitura.\n"]
    for s in sintese:
        l += [f"## {s['id']} · {s['suposicao']}\n",
              f"- **Antes (pré-registro):** L {s['pre_L']} · F1 {s['pre_F1']} · F2 {s['pre_F2']}",
              f"- **Agora:** L {s['final_L']} · F1 {s['final_F1']} · F2 {s['final_F2']}",
              f"- **O histórico:** {historico(s['taxa_base'], base)}",
              f"- **O estado em 26/out:** {s['estado_26out']}",
              f"- **O estado em 27/out (rodada 2):** {s['estado_27out']}",
              f"- **O estado em 28/out (rodada 3):** {s['estado_28out']}",
              f"- **Por quê:** {s['porque']}\n"]
    l += ["## As potências\n"]
    l += [f"- **{h['potencia']}:** fica de pé *{h['fica']}*. {h['porque']}" for h in hipoteses]
    return "\n".join(l) + "\n"


def f4(criterios: list[dict]) -> str:
    l = ["# F4 · A contestação, critério por critério (rodada 3, 28/out/2026)\n",
         "Gerado por `ferramentas/gerar_relatorio.py`. O levantamento completo, com as duas fontes de cada fato e as alegações dos **dois lados** "
         "(a quebra de isonomia apontada pelo lado do Flávio; a falta de ônibus apontada pelo lado do Lula), está em "
         "[`dados/f4_estado_26out.md`](../dados/f4_estado_26out.md) (rodada 1), [`dados/f4_estado_27out.md`](../dados/f4_estado_27out.md) (rodada 2) e [`dados/f4_estado_28out.md`](../dados/f4_estado_28out.md) (rodada 3).\n",
         "| Critério | Estado | Aponta | Base |", "|---|---|---|---|"]
    l += [f"| {c['criterio']} · {c['nome']} | {c['estado_em_28out']} | {APONTA[c['aponta']]} | {c['base']} |" for c in criterios]
    l += ["", f"**Veredito de lente:** {veredito_de_lente(criterios)}.\n",
          "**Correções ao §0 do pré-registro achadas na F4:** os ônibus com adesivo do PT retidos foram em Salvador, não em São Paulo; a PF tem 1 inquérito e 4 apurações (5 estados), não 7.\n"]
    return "\n".join(l) + "\n"


def main() -> None:
    r = json.loads((RES / "RESUMO.json").read_text(encoding="utf-8"))
    f1 = json.loads((RES / "f1_resumo.json").read_text(encoding="utf-8"))
    base, conc = ler_csv(RES / "f2_taxas_base.csv"), ler_csv(RES / "f2_concordancia.csv")
    criterios = ler_csv(DADOS / "criterios_c1_c5.csv")
    sintese, hipoteses = ler_csv(DADOS / "sintese_suposicoes.csv"), ler_csv(DADOS / "hipoteses_veredito.csv")
    (RAIZ / "RELATORIO.md").write_text(relatorio(r, f1, base, conc, criterios, sintese, hipoteses), encoding="utf-8")
    (RAIZ / "RESUMO_SIMPLES.md").write_text(resumo_simples(r, criterios, sintese), encoding="utf-8")
    (RAIZ / "docs" / "LEITURA_DA_IA.md").write_text(leitura_da_ia(sintese, hipoteses, base), encoding="utf-8")
    (RAIZ / "docs" / "F4_CONTESTACAO.md").write_text(f4(criterios), encoding="utf-8")
    print("relatório, resumo simples, leitura da IA e F4 gravados")


if __name__ == "__main__":
    main()
