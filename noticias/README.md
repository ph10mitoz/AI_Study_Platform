# Notícias

Status: ideação. Nada implementado ainda — este arquivo existe pra registrar as decisões já tomadas, não perder isso em histórico de chat.

## Objetivo
Curadoria (não feed bruto) de atualizações relevantes em IA/ML, com dupla função: manter o usuário atualizado e reforçar os fundamentos/programação do estágio de estudo atual.

## Como decidimos que funciona
- Filtro por **fontes/autores/labs específicos** que o usuário segue (ex: Anthropic, DeepMind, Karpathy) — não é varredura bruta do arXiv (volume inviável, ~200 papers/dia só em cs.LG).
- Cada item entregue como **resumo + link da fonte original**, revisado, não um despejo de texto.
- Filtrado também pelo estágio atual do roadmap (`../estudo/ROADMAP.md`) — prioriza o que reforça o que está sendo estudado agora.
- É feed de leitura — sem SM-2, sem virar flashcard automaticamente (diferente do conteúdo de estudo, que sempre vira flashcard).

## Cross-link com `estudo/`
Uma notícia lida pode gerar vínculo com um estágio do roadmap (reforça o que o usuário está estudando). O vínculo passa pelo contexto compartilhado (perfil + estágio atual), não por um link direto entre notícia e capítulo.

## Pendente antes de implementar
- Lista de fontes/autores específicos a seguir (ainda não levantada com o usuário).
- Mecanismo de "o que conta como atualização relevante" na prática — ainda não testado.
- Fontes gerais de curadoria (The Batch, Import AI, TLDR AI etc.) já estão em `../estudo/SOURCES.md`, mas sem verificação de acesso real (ex: se têm RSS, se são scrapeable).
