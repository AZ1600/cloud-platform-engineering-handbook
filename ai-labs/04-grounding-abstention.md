# 04 — Ground Answers and Abstain Without Evidence

## Failure mode

A fluent answer can be wrong even when retrieval returns plausible text. The objective is not to maximize the number of answered questions; it is to answer **only questions supported by authorized, sufficiently relevant evidence**.

## Source-backed behavior

The [`KnowledgeBaseTool`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/tools.py) returns `found: false` and empty `sources`/`evidence` for empty questions and insufficient matches. [`src/langgraph_agent.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/langgraph_agent.py) includes a hard no-evidence guard in its tool-routing path. [`tests/test_api.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/tests/test_api.py) tests the API's response shape using a **fake agent**, not a real Bedrock call.

```text
Knowledge question
   -> retrieval/tool call
   -> zero supported chunks?
       yes -> fixed abstention + empty evidence
       no  -> bounded context -> model answer -> source/evidence metadata
```

## A useful answer contract

The checked-in FastAPI response model is:

```json
{
  "answer": "Check the documented Private DNS and Blob network path.",
  "sources": ["az104-infrastructure-lab.md"],
  "evidence": [
    {
      "chunk_number": 15,
      "source": "az104-infrastructure-lab.md",
      "rerank_score": 6.02,
      "hybrid_score": 0.58
    }
  ]
}
```

This example resembles the **fake-agent API test fixture**, not a captured production response. Returning a source ID proves that the API can carry citations; it does not by itself prove that every sentence is supported by that source.

## Claim support audit

For each sentence in a generated answer, annotate:

| Check | Question |
| --- | --- |
| Source exists | Is this source present and from the allowed corpus? |
| Relevant span | Does an exact paragraph support this specific assertion? |
| Freshness | Could the implementation have changed after indexing? |
| Entitlement | Was the caller permitted to see the document? |
| Contradiction | Does another trusted source disagree? |
| Confidence | Are uncertainty and limitations communicated accurately? |

## Exercises

1. Ask about a source absent from the knowledge base, such as a company annual-leave policy. Expected behavior: **abstain**, not generate.
2. Ask a multi-part question where one part is supported and the other is not; inspect whether the answer distinguishes them.
3. Supply conflicting dated documents and require revision-specific citations.

**Production improvement:** use claim-level evidence checks and source-hash/version fields; surface a visible unsupported-claim outcome rather than relying only on prompting.

Next: [Bedrock and IAM](05-bedrock-iam.md).
