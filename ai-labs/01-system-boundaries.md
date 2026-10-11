# 01 — Map the AI System Boundaries

## Problem

Calling every rule-based classifier an “agent” hides the very different reliability and security properties of deterministic logic, retrieval, text generation, and privileged actions.

## Architecture drawn from the projects

```text
Public request -> FastAPI -> LangGraph
                             |         \
                        Bedrock       MCP knowledge tool
                                          |
                                   Hybrid search + rerank
                                          |
                                   Evidence + source IDs
                             \
                         grounded answer

PlatformPilot signals -> rules -> CloudOps finding
                                    |
                           human verification + approval
                                    |
                         controlled execution workflow
```

The RAG assistant implements a read-oriented knowledge-base search tool. The CloudOps execution boundary is a **separate** system and should never be inferred to be an MCP tool simply because the projects are discussed together.

## Four different trust decisions

| Layer | Input | Output | Safety requirement |
| --- | --- | --- | --- |
| Deterministic classifier | known events, state | labels, explanations | test unknown and malformed cases |
| Retriever | question and indexed documents | ranked source chunks | enforce document authorization and provenance |
| LLM | instructions + scoped context | natural-language answer | check grounding, schemas, uncertainty |
| Executor | validated typed command | state change | authorization, preview, approval and idempotency |

### Concrete evidence

- [`src/api.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/api.py) defines `/health`, `/ask`, and response fields `answer`, `sources`, `evidence`.
- [`backend/ai.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/ai.py) maps named pod failures to fixed recommendations.
- [`lib/decision-trace.ts`](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/decision-trace.ts) creates deterministic five-step traces; the trace itself cannot authorize remediation.

## Exercise: label each claim

1. “The code includes a handler for OOMKilled.” — **implemented**, if verified in source.
2. “The assistant explains a real incident correctly.” — requires a captured test case and result.
3. “CloudOps automatically fixes Kubernetes.” — **not established** by the decision-trace code.
4. “RAG answers always cite correct sources.” — an evaluation hypothesis, not a default fact.

## Design review

Draw separate arrows for **identity**, **data flow**, **model inference**, and **state-changing authority**. Which boundary would you revoke first if untrusted documentation started instructing the assistant to deploy a new image?

Continue to [ingestion and chunking](02-ingestion-chunking.md).
