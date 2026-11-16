# Roadmap

## Track 1 — Math: the life of one model (NumPy only, no frameworks)
| Stage | Topic | Math | Build from scratch |
|---|---|---|---|
| 1 | Data -> numbers | vectors, matrices, normalization, statistics | load a dataset, compute stats by hand |
| 2 | Prediction (forward pass) | linear algebra, activation functions | one neuron, then a small network |
| 3 | Error (loss) | probability, MSE, cross-entropy, maximum likelihood | loss functions, checked against formulas |
| 4 | Learning (backprop) | derivatives, chain rule, gradients | backprop by hand, verify with numerical gradients |
| 5 | Optimization | gradient descent, SGD, Adam, overfitting, regularization | an optimizer from scratch |
| 6 | Answering (inference) | softmax, sampling, attention, transformers | a tiny language model |

## Track 2 — Tools (after each math stage, not before)
- Core: Python, Git/GitHub, scikit-learn, PyTorch (rebuild the NumPy projects in PyTorch).
- Production: FastAPI, Docker, experiment tracking (Weights & Biases or MLflow).
- LLMs and agents: LLM APIs, tool use, RAG, agents, MCP (build my own MCP server exposing a tool).
- Hugging Face: fine-tune a small model.

## Track 3 — Targets
- Inputs (weekly): projects shipped, commits, one write-up per project.
- Outcomes (monthly): stars, LinkedIn views, real logins, revenue.

## Workflow per chapter/task
1. Claude explains the concept and math (source from `CONTENT_LIBRARY.md`).
2. Claude poses a practical project/exercise tied to that content — problem only, no solution.
3. I write my own code and my own prediction, before seeing any AI code.
4. Claude writes its own solution, independently.
5. Comparison on 4 axes: correctness, edge cases, complexity, **autonomy** (did I catch my own gap, or only after seeing Claude's solution).
6. Commit/PR to GitHub with a short write-up (feeds weekly targets in `CLAUDE.md`).
7. Flashcards: key concepts of the chapter go to `cards/` always (not just mistakes); specific errors from the comparison go in as high-priority cards.
8. Everything logs to `progress/stage-N.md`.

## Level rubric (junior / pleno / senior)
Not a simple average — **autonomy caps the level**: if I only caught the gap after seeing Claude's solution, the chapter cannot close as senior even if the final code is correct.

| Axis | Junior | Pleno | Senior |
|---|---|---|---|
| Correctness | solves the happy path | solves + handles obvious errors | solves + covers edge cases + tests |
| Edge cases | ignores them | covers the obvious ones (empty, zero, overflow) | anticipates the non-obvious ones |
| Complexity | works, ignores cost | names the complexity | optimizes consciously (vectorization, avoids redundant loops) |
| Autonomy | only noticed the gap after seeing Claude's solution | noticed alone on review, didn't prevent it | prevented it in the first pass |

## Order
Stages 1-5 before agents and MCP. Next step: Stage 1 (single neuron in NumPy).
