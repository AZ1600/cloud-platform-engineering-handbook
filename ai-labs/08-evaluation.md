# 08 — Evaluate Retrieval Before Claiming Accuracy

## Evaluation surfaces

The RAG project includes [`evals/retrieval_cases.json`](https://github.com/AZ1600/rag-ops-assistant/blob/main/evals/retrieval_cases.json) with **five** representative cases: CloudOps approvals, AZ-104 Private DNS, observability reliability, PlatformPilot operations, and an unsupported annual-leave question.

[`src/evaluate.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/evaluate.py) checks:

- whether **top-1** comes from an expected source;
- whether **all returned sources** belong to the expected set (source purity);
- whether a negative/no-evidence query returns zero results.

The script reports a passed-case ratio. This is a **small retrieval regression suite**, not a calibrated generative-accuracy or hallucination guarantee. API tests in `tests/test_api.py` replace the model with `FakeAgentService`.

## Run a zero-network documentation exercise

```bash
# From the handbook root, after applying this Phase 6 package:
python3 ai-labs/examples/evaluate_sample.py
```

This runs against a **synthetic fixture** (`ai-labs/examples/retrieval-fixtures.json`), with no embedding model, Bedrock invocation or AWS credentials. It demonstrates the evaluation logic, **not the actual RAG system's current retrieval quality**.

## Metrics and denominators

| Metric | Definition | Why it matters |
| --- | --- | --- |
| Top-1 source accuracy | supported queries with correct first source / all supported queries | whether the first result identifies the relevant document |
| Source purity | queries whose returned source set contains no unexpected source / all queries | off-topic citation contamination |
| No-evidence success | unsupported questions that abstain / all unsupported questions | hallucination pressure |
| Recall@k | expected relevant docs found in top k / expected relevant docs | retrieval omissions |
| Claim support | supported claims / claims checked by reviewers | generation evidence fidelity |

Use confidence intervals or larger diversified datasets before claiming a stable success rate; five curated examples are diagnostic, not representative.

## Regression design

Create cases varying project name, acronym, paraphrase, contradictory versions, out-of-scope question, and hostile injected instructions. Store expected source IDs plus whether abstention is required. Label observed and expected outputs independently.

Record the embedding model, chunking revision, threshold, reranker revision, corpus commit and evaluator version. Otherwise a “100%” run may be impossible to reproduce.

## Real RAG validation (separate repository)

```bash
# In rag-ops-assistant after confirming model prerequisites:
python -m pytest -q tests/test_api.py
# Model-backed retrieval evaluation is a separate, potentially heavy step:
python src/evaluate.py
```

The latter may load/download transformer weights and requires an index; consult the repository README and its actual invocation before running it. Neither of these commands is part of the handbook install.

Next: [AI telemetry and cost](09-telemetry-cost.md).
