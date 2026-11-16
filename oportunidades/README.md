# Oportunidades

Status: ideação. Nada implementado ainda — este arquivo existe pra registrar as decisões já tomadas, não perder isso em histórico de chat.

## Objetivo
Coletânea curada de oportunidades (bolsas, intercâmbios, programas de pesquisa, cursos) em ML/DL/AI/data science, cruzando:
- O perfil do usuário (quem é, o que já sabe) — hoje vive em `../CLAUDE.md` e no estado de `../estudo/ROADMAP.md`/`../estudo/progress/`.
- O que ele está aprendendo agora (estágio atual da trilha de estudo).

## Como decidimos que funciona
- Não é filtro estático (área + elegibilidade + deadline fixo). É adaptativo: parte de um contexto inicial e vai mudando conforme decisões de curto/médio/longo prazo do usuário.
- "Curto/médio/longo prazo" é um **atributo descritivo de cada oportunidade** (ex: curto = curso/programa dentro do semestre; longo = programa de anos), não um mecanismo de filtro separado.
- É feed de leitura — sem SM-2, sem virar flashcard. O usuário lê e decide agir (aplicar, ignorar, salvar).
- Não existe documento de metas separado — o perfil já está nos arquivos do projeto (`CLAUDE.md`, roadmap, progresso). Não duplicar isso aqui.

## Cross-link com `estudo/`
Uma oportunidade com deadline próximo pode sinalizar prioridade de estudo (ex: bolsa exige PyTorch em 2 meses → antecipa Track 2). O vínculo passa pelo contexto compartilhado, não por link direto entre um item de oportunidade e um capítulo específico.

## Pendente antes de implementar
Fontes de busca (SiROP, DAAD RISE, MITACS, labs de universidades) já estão listadas em `../estudo/SOURCES.md`, mas não verificadas — isso precisa de uma passada de pesquisa como foi feita pra `estudo/CONTENT_LIBRARY.md`, só que ainda não foi priorizada.
