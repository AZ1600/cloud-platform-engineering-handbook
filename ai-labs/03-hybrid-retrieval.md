# 03 — Hybrid Retrieval, Thresholds and Reranking

## Trace the real algorithm

[`src/rag_core.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/rag_core.py) combines a normalized embedding-dot-product semantic score with token-overlap keyword coverage:

```text
hybrid_score = 0.75 * semantic_score + 0.25 * keyword_score
```

The code sorts candidates, considers the first **8**, discards candidates whose hybrid score is below **0.40**, calls a CrossEncoder reranker, keeps at most **3**, and rejects rerank scores below **-1.0**. The reranker model is `cross-encoder/ms-marco-MiniLM-L-6-v2`.

These values are **code defaults**, not empirically proven optimal values. Negative cross-encoder scores are possible; a raw rerank score is not a probability of correctness.

## Why blend search methods?

- Semantic retrieval captures paraphrases, e.g. *“private storage connectivity”* vs *“Private DNS to Blob”*.
- Lexical overlap helps with exact identifiers such as `ErrImagePull`, `OIDC`, `ClusterIP`, or a resource name.
- Cross-encoder reranking compares a full query–passage pair but costs more inference time than vector lookup.

## Examine the search path

```bash
# In the rag-ops-assistant clone:
sed -n '1,210p' src/rag_core.py
sed -n '1,180p' src/tools.py
```

`KnowledgeBaseTool.search` returns a structured object with `found`, `context`, `sources`, and `evidence`. Evidence includes `source`, `chunk_number`, `hybrid_score` and `rerank_score`.

## Trade-offs to investigate

| Symptom | Hypothesis | Test |
| --- | --- | --- |
| Correct source missing | chunking or top-8 truncation | compare recall at 8, 16 and 32 candidates |
| Many off-topic matches | hybrid threshold too low | inspect false positives across query types |
| Exact acronym missed | poor tokenization or term frequency | add a lexical regression query |
| Wrong source promoted | reranker mismatch | compare top-1 accuracy and source purity |
| Good answer with bad citation | model not limited to retrieved evidence | check support at the individual-claim level |

### Critical rule

Do not compare a raw semantic cosine value to a cross-encoder value as though they use the same scale. Never describe a `hybrid_score` of 0.65 as “65% confidence”.

## Experiment

Using [the offline evaluation lesson](08-evaluation.md), record top-1 source accuracy and source-purity counts on **synthetic fixtures**, then write down what a model-backed evaluation would need to verify.

Next: [grounding and abstention](04-grounding-abstention.md).
