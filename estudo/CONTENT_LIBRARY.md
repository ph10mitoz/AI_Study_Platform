# Biblioteca de Conteúdo — Fontes para a Trilha

Catálogo de fontes gratuitas mapeadas aos estágios do `ROADMAP.md` (Track 1: 1-6 matemática/NumPy; Track 2: ferramentas).

Legenda de verificação:
- **[VERIFICADO]** — conteúdo real foi acessado (fetch/leitura direta) nesta pesquisa.
- **[NÃO VERIFICADO]** — conhecido só por nome/reputação ou snippet de busca, conteúdo não foi lido diretamente.

Status: em andamento.

---

## IMPA — Curso de Machine Learning (mestrado, Paulo Orenstein) **[VERIFICADO]**

Base: `https://w3.impa.br/~pauloo/teaching/ml/`. Estrutura: Sobre o curso (`/`), Aulas (`/aulas/`), Código/Labs (`/labs/`), Listas de exercícios (`/listas/`), Provas (`/provas/`).
Livro-texto: *Introduction to Statistical Learning* (statlearning.com), código adaptado em `github.com/qx0731/Sharing_ISL_python`.

Labs (notebooks `.ipynb`, caminho `w3.impa.br/~pauloo/ipynb/<arquivo>`):
| Lab | Tópico | Arquivo |
|---|---|---|
| 1 | Introdução ao ambiente computacional (HTML, não notebook) | `labs/html/lab_1/lab_1` |
| 2 | Introdução a Python | `cap_2.ipynb` |
| 3 | Regressão linear | `cap_3.ipynb` |
| 4 | Classificação linear | `cap_4.ipynb` |
| 5 | Métodos de reamostragem | `cap_5.ipynb` |
| 6 | Seleção de modelos e regularização | `cap_6.ipynb` |
| 7 | Além de linearidades | `cap_7.ipynb` |
| 8 | Árvores de decisão | `cap_8.ipynb` |
| 9 | Support Vector Machines | `cap_9.ipynb` |
| 10 | Deep learning | `cap_10.ipynb` |
| 12 | Aprendizado não-supervisionado | `cap_12.ipynb` (não existe lab 11) |

Série GPT (profundidade alta — construção de um GPT do zero, bate direto com Track 1 Stage 4-6):
| GPT | Tópico | Arquivo |
|---|---|---|
| 0 | Diferenciação automática | `gpt_0.ipynb` |
| 1 | Bigramas e trigramas | `gpt_1.ipynb` |
| 2 | Rede neural de uma camada | `gpt_2.ipynb` |
| 3 | Resolvendo problemas na rede neural | `gpt_3.ipynb` |
| 4 | Rede neural de muitas camadas | `gpt_4.ipynb` |
| 5 | Finalmente, GPT | `gpt_5.ipynb` |

Não vi "Aulas", "Listas" e "Provas" com conteúdo (só o link da página de Código foi buscado) — pendente de fetch numa próxima passada.

## MIT Missing Semester **[VERIFICADO]**

URL base: `https://missing.csail.mit.edu/`. Edição 2026, 9 aulas (foco Track 2 — ferramentas de dev, não matemática de ML):
| Data | Aula | URL |
|---|---|---|
| 1/12 | Course Overview + Introduction to the Shell | `/2026/course-shell/` |
| 1/13 | Command-line Environment | `/2026/command-line-environment/` |
| 1/14 | Development Environment and Tools | `/2026/development-environment/` |
| 1/15 | Debugging and Profiling | `/2026/debugging-profiling/` |
| 1/16 | Version Control and Git | `/2026/version-control/` |
| 1/20 | Packaging and Shipping Code | `/2026/shipping-code/` |
| 1/21 | Agentic Coding | `/2026/agentic-coding/` |
| 1/22 | Beyond the Code | `/2026/beyond-code/` |
| 1/23 | Code Quality | `/2026/code-quality/` |

Edições antigas (não cobertas em 2026, mas arquivadas): Data Wrangling, Security and Cryptography, Backups, Automation, OS Customization, Web and Browsers (2019-2020) — não verifiquei se ainda estão acessíveis.

Mapeamento: cobre Git/GitHub e ambiente de dev do Track 2 bem; não cobre nada de matemática/Track 1. "Agentic Coding" é relevante pro item "agentes/MCP" do Track 2.

## freeCodeCamp

Não achei uma "trilha freeCodeCamp construída sobre cursos de Stanford/MIT" como produto único e atual — a busca não confirma essa estrutura específica existir hoje. O que existe e é real:

- **[VERIFICADO]** Artigo de David Venturi na freeCodeCamp, ["Every Single Machine Learning Course on the Internet, Ranked by Your Reviews"](https://www.freecodecamp.org/news/every-single-machine-learning-course-on-the-internet-ranked-by-your-reviews-3c4a7b8026c0/) — é uma curadoria/ranking, não um curso próprio. Top 3: *Machine Learning* (Stanford/Coursera, Andrew Ng), *Machine Learning* (Columbia/edX, John Paisley — mais avançado, exige cálculo/álgebra/estatística prévios), *Machine Learning A-Z* (Udemy, prático, fraco em matemática). Outros citados: The Analytics Edge (MIT/edX), bootcamps de Python/R (Udemy), Georgia Tech via Udacity.
- **[NÃO VERIFICADO]** Artigo "Building a data science curriculum with advanced math and machine learning" menciona uma série de vídeos/notebooks planejada por Kylie Ying (freeCodeCamp) — não confirmei se está publicada/atual.

Conclusão: freeCodeCamp aqui funciona melhor como **curador de terceiros** do que como fonte primária de conteúdo técnico profundo — não é prioridade pra Track 1 (matemática do zero).

## Syllabi de universidades

### Stanford CS229 (Machine Learning) — **[NÃO VERIFICADO / bloqueado]**
Conteúdo atual (Winter 2026) exige login institucional Stanford (Canvas) — página pública não expõe o cronograma de aulas. Não consegui extrair estrutura real.

### Stanford CS231n (Deep Learning for Computer Vision) — **[VERIFICADO]** via `https://cs231n.stanford.edu/schedule.html`
18 aulas, cronograma completo com leituras ligadas. As mais relevantes pro Track 1:
| # | Tópico | Relevância |
|---|---|---|
| 2 | Image Classification, k-NN, linear classifiers, softmax loss | Stage 2/3 |
| 3 | Regularization and Optimization (SGD, momentum, AdaGrad, Adam) | Stage 5 |
| 4 | Neural Networks and Backpropagation (com handout de backprop linear, paper "Efficient BackProp" de LeCun) | Stage 4 |
| 7 | Recurrent Neural Networks, LSTM, GRU | Stage 6 (pré-transformer) |
| 8 | Attention and Transformers (com "Attention Is All You Need", "The Illustrated Transformer", paper ViT) | Stage 6 |
Demais aulas (detecção de objetos, vídeo, modelos generativos, 3D vision) são avançadas/fora do escopo do Track 1 atual.

### Stanford CS224n (NLP com Deep Learning) — **[VERIFICADO]** via `https://web.stanford.edu/class/cs224n/`
19 aulas, Winter 2026, cronograma completo com slides/leituras/assignments. Relevantes:
| # | Tópico | Relevância |
|---|---|---|
| 2 | Word Vectors (word2vec, GloVe) | Além do Track 1 atual, útil pro Track 2 (NLP/embeddings) |
| 3 | Backpropagation and Neural Network Basics | Stage 4 |
| 4 | Language Models and RNNs | Stage 6 |
| 5 | Transformers | Stage 6 |
| 7-8 | Pretraining / Post-training (RLHF, SFT, DPO) | Track 2 (LLMs/agentes) |
| 10 | Agents, Tool Use, and RAG (ReAct, Toolformer) | Track 2 (agentes/MCP) — bate direto com o item "LLMs e agentes" do seu roadmap |
Tem sessões extras: Python Review, PyTorch Tutorial, Hugging Face Transformers Tutorial — relevantes pro Track 2.

### MIT 6.S191 (Introduction to Deep Learning) — **[VERIFICADO]** via `https://introtodeeplearning.com/`
Edição 2026 (Mar 30 – Mai 25), 9 aulas + 3 software labs:
| Aula/Lab | Tópico | Relevância |
|---|---|---|
| Lecture 1 | Intro to Deep Learning | Stage 2 |
| Lecture 2 + Lab 1 | Deep Sequence Modeling + geração de música | Stage 6 |
| Lecture 3 | Deep Computer Vision | fora do Track 1 atual |
| Lecture 4 + Lab 2 | Deep Generative Modeling + detecção facial | avançado |
| Lab 3 | Fine-tuning de LLM | Track 2 |
| Lecture 9 | Treino massivamente paralelo (multi-GPU) | avançado/infra |

### Berkeley CS189 (Introduction to Machine Learning) — **[NÃO VERIFICADO]**
Busca não trouxe cronograma atual acessível publicamente (página oficial eecs189.org não respondeu nos resultados; página pessoal de Jonathan Shewchuk tem plano aula-a-aula mas de oferta passada — Spring 2025). Pendente de fetch direto numa próxima passada.

### fast.ai — Practical Deep Learning for Coders — **[VERIFICADO]** via `https://course.fast.ai/`
Parte 1, 8 lições + bônus:
| Lição | Tópico |
|---|---|
| 1 | Getting started |
| 2 | Deployment (treinar e colocar um modelo no ar) |
| 3 | Neural net foundations |
| 4 | NLP |
| 5 | From-scratch model |
| 6 | Random forests |
| 7 | Collaborative filtering |
| 8 | Convolutions (CNNs) |
| Bônus | Data ethics |
Parte 2 (avançada, lições 9-25) existe mas não foi detalhada. Curso é hands-on/top-down (começa com modelo funcionando, depois explica teoria) — filosofia oposta ao seu Track 1 (bottom-up, matemática primeiro). Bom como Track 2 (ferramentas práticas), não como fonte de rigor matemático.

## roadmap.sh — AI and Data Scientist **[VERIFICADO]** (PDF lido via download+Read, igual ao roadmap "AI Engineer" já catalogado na conversa)

Estrutura (8 blocos principais, em ordem):
1. **Mathematics** — Linear Algebra, Calculus, Mathematical Analysis, Differential Calculus. Fontes: "Mathematics for Machine Learning" (Coursera), "Algebra and Differential Calculus" (Coursera).
2. **Statistics** — CLT, Hypothesis Testing, Probability/Sampling, AB Testing (CUPED, ratio metrics, casos reais Booking.com/DoorDash/Netflix/Microsoft). Fontes: cursos Coursera + artigos/papers de indústria.
3. **Econometrics** — pré-requisitos, regressão/séries temporais/ajuste de distribuições. Fontes: livros "Fundamentals of Econometrics", "Intro to Econometrics", curso Coursera, Kaggle Time Series, ARIMA.
4. **Coding** — Python (Kaggle, Google's Python Class), estrutura de dados/algoritmos (Leetcode, Algorithms Specialization), SQL.
5. **Exploratory Data Analysis** — pandas, seaborn, cursos dedicados.
6. **Machine Learning** — clássico (sup./não-sup.) e avançado (ensembles, NNs). Fontes: Open Machine Learning Course (OpenDS), Machine Learning Specialization, livro Bishop *Pattern Recognition & ML* + repo GitHub de notas.
7. **Deep Learning** — Fully Connected, CNN, RNN, LSTM, Transformers, Transfer Learning. Fontes: Deep Learning Specialization, Deep Learning Book (Goodfellow — já está no SOURCES.md), paper "Attention is all you need", "The Illustrated Transformer" (Jay Alammar — já está no SOURCES.md).
8. **MLOps** — deployment, CI/CD. Fonte: MLOps Specialization.

Observação: a maioria das fontes citadas no PDF são **nomes de curso sem URL explícita no texto extraído** (ex: "Coursera: Introduction to Statistics Course") — contam como **[NÃO VERIFICADO]** quanto ao link exato, mesmo a estrutura do roadmap em si sendo verificada.

## IMPA — Aulas, Listas e Provas (extensão) **[VERIFICADO]**

24 aulas (Aula 0-23), cronograma completo com slides em PDF:
| Aula | Tópico | Relevância pro ROADMAP.md |
|---|---|---|
| 0 | Pré-requisitos: álgebra linear, estatística, otimização | **Stage 1** — é literalmente o pré-requisito que o seu Track 1 pede antes de tudo |
| 1 | Noções básicas de aprendizado | Stage 1-2 |
| 2-3 | Regressão linear (+ revisão/código) | Stage 2 |
| 4 | Classificação linear | Stage 2-3 |
| 5-6 | Métodos de reamostragem (+ revisão/código) | fora do Track 1 atual (validação cruzada, bootstrap) |
| 7 | Seleção de modelos e regularização | Stage 5 |
| 8-9 | Além de linearidades, revisão de meio de curso | Stage 2 avançado |
| 10, 23 | Prova 1 (Caps 1-7), Prova 2 (Caps 1-10,12) | avaliação, não conteúdo |
| 11-12 | Support Vector Machines | fora do Track 1 (ML clássico) |
| 13-14 | Métodos baseados em árvores | fora do Track 1 (ML clássico) |
| 15-17 | Deep learning (teoria + código, GPT 0) | **Stage 4** (GPT 0 = diferenciação automática) |
| 18-19 | Código (GPT 1-5) | **Stage 6** — construção de um GPT do zero, ponta a ponta |
| 20-21 | Aprendizado não-supervisionado | fora do Track 1 atual |
| 22 | Revisão final | — |

Listas de exercícios: só 2 listas (Lista 1: cobre caps. até aula 9 antes da Prova 1; Lista 2: cobre até aula 20 antes da Prova 2), sem tópico detalhado nem arquivo anexado nesta página — teria que abrir cada lista individualmente (links não vieram no fetch). Provas: 2 provas dissertativas, sem gabarito público.

**Conclusão**: a Aula 0 (pré-requisitos) é a melhor pista encontrada até agora pra fechar o Stage 1 — vale abrir o PDF `aula_0.pdf` diretamente numa próxima passada pra ver se ela de fato ensina álgebra linear/estatística do zero ou só lista o que é esperado que você já saiba.

## Kaggle Learn — **[DESCARTADO]**

Existência confirmada (7 cursos: python, pandas, intro/intermediate ML, feature-engineering, time-series, computer-vision), mas conteúdo bloqueado por SPA em JS — WebFetch só pega o `<title>`. Decisão: não insistir. O conteúdo desses micro-cursos já está coberto por fontes verificadas e de maior profundidade (d2l.ai, Google ML Crash Course, Made With ML Foundations, IMPA). Não vale o custo de infra (browser real) pra algo redundante. Se no futuro faltar prática leve de Pandas/feature engineering especificamente, reabrir isso.

## FastAPI — Tutorial oficial **[VERIFICADO]** via `https://fastapi.tiangolo.com/tutorial/`

41 capítulos, estrutura real extraída direto do sumário:
| Bloco | Capítulos | Tópico |
|---|---|---|
| Básico | 1-12 | First Steps, path/query params, request body, validação, tipos extras |
| Headers/cookies/respostas | 13-19 | Cookie/Header Parameters, Response Model, Status Code |
| Forms e arquivos | 20-23 | Form Data, Request Files |
| Erros e config | 24-27 | Handling Errors, JSON Encoder, Body Updates |
| Dependencies | 28 | injeção de dependência, sub-dependências, `yield` |
| Security | 29 | OAuth2, JWT, hashing de senha |
| App-level | 30-33 | Middleware, CORS, **SQL Databases**, Bigger Applications |
| Streaming/background | 34-36 | SSE, Background Tasks |
| Docs/testes | 37-41 | Static Files, **Testing**, Debugging |

Fecha a lacuna "FastAPI" do Track 2 com fonte primária oficial. Depois do tutorial vêm Advanced Guide, CLI, Deployment — relevantes pra colocar o modelo em produção de fato.

## Docker — docker-curriculum.com + docs.docker.com **[VERIFICADO]**

`docker-curriculum.com` (tutorial prático, 4 seções): Foundations (imagens vs. containers vs. VM) → Dockerfiles (servir site estático, empacotar app Flask) → Compose (app multi-serviço com Flask + Elasticsearch) → Modern Docker (multi-stage builds, ARM/x86, Compose Watch, hardening).
`docs.docker.com/get-started/docker-overview/` (docs oficiais, estático): conceitos (imagem, container, daemon, client, registry), arquitetura cliente-servidor, casos de uso (CI/CD, deploy, consolidação de workloads).

Combinação fecha a lacuna "Docker" do Track 2: conceito (docs oficiais) + prática real empacotando uma app Flask (equivalente direto a empacotar uma API FastAPI do seu projeto).

## Hugging Face — Cursos **[VERIFICADO]**

12 cursos oficiais em `huggingface.co/learn`, nenhum com módulos detalhados nesta passada (página index não expõe currículo interno):
| Curso | URL | Cobre | Relevância |
|---|---|---|---|
| LLM Course | `/learn/llm-course` | LLMs com o ecossistema HF (renomeado — antigo "NLP Course") | Track 2 |
| Agents Course | `/learn/agents-course` | construir e publicar agentes de IA | Track 2 (agentes) |
| Context Course | `/learn/context-course` | engenharia de contexto pra agentes de código | Track 2 (agentes) |
| a smol course | `/learn/smol-course` | pós-treinamento de modelos (curto) | Track 2 |
| Deep RL Course | `/learn/deep-rl-course` | reinforcement learning profundo | fora do Track 1/2 atual |
| Computer Vision Course | `/learn/computer-vision-course` | visão computacional com o ecossistema | fora do escopo atual |
| Audio Course | `/learn/audio-course` | transformers aplicados a áudio | fora do escopo atual |
| Diffusion Course | `/learn/diffusion-course` | modelos de difusão | avançado/fora do escopo |
| ML for Games / Robotics / 3D Courses | `/learn/ml-games-course`, `/learn/robotics-course`, `/learn/ml-for-3d-course` | nichos específicos | não mapeado (pode interessar no "futuro, outros tópicos" que você mencionou) |
| Open-Source AI Cookbook | `/learn/cookbook` | coleção de notebooks, não é curso estruturado | referência solta |

Pendente: abrir o currículo interno de cada curso (módulos/unidades) numa próxima passada — a página-índice não expôs isso.

## d2l.ai — Dive into Deep Learning **[VERIFICADO]** (já citado no SOURCES.md, agora com estrutura real confirmada)

Livro completo, 23 capítulos + apêndices, com fetch direto do sumário. É de longe a fonte mais completa encontrada pra fechar as lacunas de Stage 1 e Stage 3:
| Capítulo/Seção | Tópico | Fecha lacuna |
|---|---|---|
| 2.3 Linear Algebra, 2.6 Probability and Statistics | álgebra linear e estatística, com código | **Stage 1** — match direto |
| 2.5 Automatic Differentiation | diferenciação automática | Stage 4 |
| 22. Appendix: Mathematics for Deep Learning (2.1 Geometria/Álgebra Linear, 22.3-22.5 Cálculo, 22.6 Random Variables, **22.7 Maximum Likelihood**, 22.8 Distributions, 22.10 Statistics, 22.11 Information Theory) | apêndice matemático completo, rigor de pós-graduação | **Stage 1 e Stage 3 — fecha as duas lacunas de uma vez**, 22.7 é literalmente MLE |
| 12. Optimization Algorithms (Gradient Descent, SGD, Momentum, Adagrad, RMSProp, Adam) | otimização | Stage 5, cobertura mais completa que CS231n |
| 11. Attention Mechanisms and Transformers | atenção e transformers, do zero | Stage 6 |
| 23. Appendix: Tools for Deep Learning | Jupyter, Colab, SageMaker, EC2, GPUs | Track 2 (infra básica) |

Único "porém": é um livro denso (23 capítulos), não um curso com cronograma — você decide o ritmo. Tem código executável em cada seção (PyTorch/outros frameworks), o que ajuda também o Track 2 (migração NumPy→PyTorch).

## Google ML Crash Course **[VERIFICADO]**

12 módulos em 5 blocos: ML Models (Regressão Linear, Logística, Classificação) → Data (dados numéricos, categóricos, generalização/overfitting) → Advanced ML Models (Redes Neurais, Embeddings, **Intro to LLMs** — módulo novo) → Real-world ML (Production ML Systems, AutoML, ML Fairness).
Relevância: Stage 2-3 (nível intro, mais raso que CS231n/d2l.ai), e o módulo "Intro to Large Language Models" + "Production ML Systems" tocam o Track 2. Bom como primeira passada rápida, não como fonte de profundidade.

## Full Stack Deep Learning (FSDL) **[VERIFICADO]**

Edição 2022, 9 aulas + labs — curso focado em produção, não em matemática:
| Aula/Lab | Tópico | Relevância |
|---|---|---|
| Lecture 2 + Lab: Development Infrastructure & Tooling | setup de ambiente de ML | Track 2 |
| **Lab 4: Experiment Management** | tracking de experimentos | **fecha parte da lacuna "experiment tracking" do Track 2** |
| Lecture 4: Data Management | versionamento de dados | Track 2 |
| **Lecture 5: Deployment + Lab 7: Web Deployment** | colocar modelo em produção via web | **fecha parte da lacuna de deployment/serving** (não confirma FastAPI especificamente, mas é o mesmo problema) |
| Lecture 6 + Lab 8: Continual Learning / Model Monitoring | manutenção em produção | Track 2 |
| Lecture 7: Foundation Models | modelos pré-treinados grandes | Track 2 (LLMs) |

Existe edição 2021 mais longa (~27 itens, cobre fundamentos de DL + MLOps) — não detalhada nesta passada.

## Made With ML **[VERIFICADO]**

Curso de MLOps ponta a ponta, estrutura por fases: Design → Data → Model (Training, **Tracking**, Tuning, Evaluation, Serving) → Develop (Scripting, CLI) → Utilities → Test → Reproducibility (Versioning) → Production (Jobs & Services, **CI/CD**, Monitoring).
Tem também curso "Foundations" separado: Toolkit (Notebooks, Python, NumPy, Pandas, **PyTorch**), Machine Learning (regressão, redes neurais), Deep Learning (CNNs, embeddings, RNNs, attention, transformers).
**Importante**: o texto extraído da página não menciona FastAPI nem Docker nominalmente, mesmo cobrindo "Serving" e "CI/CD" — não posso confirmar que usa essas ferramentas especificamente sem abrir a lição. Fecha a lacuna conceitual de MLOps/tracking, mas não confirma a lacuna específica "FastAPI + Docker" do seu ROADMAP.md.

## DeepLearning.AI — Short Courses **[VERIFICADO, lista parcial — página relatou 109 cursos, só uma parte veio no fetch]**

Fecha bem a lacuna "Track 2 - LLMs, agentes, RAG, MCP":
- **"Build AI Apps with MCP Server: Working with Box Files"** (Box) — curso dedicado a **MCP**, o único encontrado em toda a pesquisa até agora.
- Multi AI Agent Systems with crewAI, Long-Term Agentic Memory With LangGraph, Building AI Browser Agents — agentes.
- Post-training of LLMs (SFT, DPO, RL), Reinforcement Fine-Tuning with GRPO, Build and Train an LLM with JAX — treino/fine-tuning, fora do escopo raso do Track 2 mas relevante se quiser ir fundo.
- Pydantic for LLM Workflows — validação estruturada de output de LLM.
- **Não encontrado**: nenhum curso específico de experiment tracking apareceu na parte visível da página (109 cursos no total, lista truncada — pode existir fora do que veio no fetch).

## Cruzamento com estágios do ROADMAP.md

| Estágio / Área | Fontes que cobrem (verificadas) | Lacuna |
|---|---|---|
| **Track 1 - Stage 1** (vetores, matrizes, normalização, estatística; carregar dataset, calcular stats à mão) | **d2l.ai 2.3 (Linear Algebra) + 2.6 (Probability and Statistics) + Apêndice 22** — match direto, com código. IMPA Aula 0 (pré-requisitos) candidata forte, PDF ainda não lido. Tutorial `numpy/numpy-tutorials` (achado na conversa principal). | **Resolvida** nesta 2ª passada — d2l.ai fecha com profundidade. |
| **Track 1 - Stage 2** (forward pass: um neurônio, depois rede pequena) | IMPA GPT 2 (rede de uma camada) e GPT 4 (muitas camadas) — direto. CS231n aulas 2-4. MIT 6.S191 Lecture 1. | Bem coberto. |
| **Track 1 - Stage 3** (loss: MSE, cross-entropy, MLE) | **d2l.ai 22.7 Maximum Likelihood** (match direto) + CS231n aula 2 (softmax loss) + Google ML Crash Course módulo 1 (raso). | **Resolvida** nesta 2ª passada — d2l.ai cobre MLE isoladamente. |
| **Track 1 - Stage 4** (backprop, regra da cadeia, gradientes) | CS231n aula 4 (com handout de backprop manual + paper "Efficient BackProp"). CS224n aula 3. IMPA GPT 0 (diferenciação automática) — ótimo encaixe, é literal "backprop by hand". | Bem coberto, inclusive com fonte de alto rigor (IMPA). |
| **Track 1 - Stage 5** (otimização: GD, SGD, Adam, overfitting, regularização) | CS231n aula 3, IMPA Lab 6, **d2l.ai cap. 12 inteiro** (GD, SGD, Momentum, Adagrad, RMSProp, Adam — mais completo). | Bem coberto, agora com fonte ainda mais completa. |
| **Track 1 - Stage 6** (softmax, sampling, atenção, transformers, LM pequeno) | IMPA série GPT, CS231n aula 8, CS224n aulas 4-5, MIT 6.S191, **d2l.ai cap. 11 (Attention Mechanisms and Transformers, do zero)**. | Bem coberto — estágio com mais excesso de fontes de toda a trilha. |
| **Track 2 - Git/GitHub, ambiente de dev** | MIT Missing Semester (quase inteiro: shell, ambiente, debugging, git, empacotamento). | Coberto. |
| **Track 2 - PyTorch** | fast.ai, CS224n tutorial, **Made With ML (Toolkit: NumPy, Pandas, PyTorch)**, d2l.ai (código em PyTorch em quase todo capítulo). | Melhorou — ainda sem "tradutor" dedicado NumPy→PyTorch, mas 4 fontes já usam PyTorch lado a lado com os conceitos do Track 1. |
| **Track 2 - LLMs, agentes, RAG, MCP** | CS224n aulas 9-10, MIT Missing Semester "Agentic Coding", HF Agents/Context/LLM Courses, **DeepLearning.AI "Build AI Apps with MCP Server"** (único curso de MCP encontrado) + cursos de agentes (crewAI, LangGraph). | **MCP deixou de ser lacuna total** — achei 1 curso dedicado. Resto já estava bem coberto. |
| **Track 2 - Hugging Face** | CS224n tutorial, MIT 6.S191 Lab 3, **12 cursos oficiais HF catalogados** (LLM, Agents, Context, smol, Deep RL, CV, Audio, Diffusion, Games/Robotics/3D). | Melhorou bastante — módulos internos de cada curso ainda não verificados. |
| **Track 2 - FastAPI, Docker, experiment tracking** | **FastAPI tutorial oficial** (41 capítulos, inclui SQL DB e testing) + **docker-curriculum.com + docs.docker.com** (conceito + prática empacotando app Flask) + **FSDL Lab 4** (experiment tracking). | **Resolvida** — as três ferramentas específicas agora têm fonte primária verificada. |
| **roadmap.sh "AI and Data Scientist" (blocos 1-8)** | Sem mudança nesta passada. | — |
| **Kaggle Learn (micro-courses)** | **Descartado por decisão** — redundante com d2l.ai/Google Crash Course/Made With ML, custo de infra (browser real) não compensa. | Não é mais lacuna a perseguir. |

**Lacunas que seguem abertas de verdade, mesmo após essa 3ª passada**: módulos internos dos cursos HF e das listas de exercício do IMPA — catalogados só no nível "curso existe", não "conteúdo lido". Isso só vale a pena aprofundar quando formos de fato montar a lição daquele estágio específico, não antes.

**Lacunas fechadas nesta passada**: FastAPI, Docker, e experiment tracking (os três pontos do Track 2 que seguiam sem fonte real). Combinado com a passada anterior (Stage 1, Stage 3, MCP), a trilha completa (Track 1 inteiro + Track 2 inteiro) agora tem pelo menos uma fonte verificada por área. Kaggle Learn foi descartado por redundância, não por falta de solução.

**Fonte de maior impacto da 2ª passada**: **d2l.ai** — sozinha fecha Stage 1, reforça Stage 3/5/6, e tem código em PyTorch lado a lado com a teoria. Se tivesse que escolher 1 fonte nova pra priorizar agora, seria essa.
