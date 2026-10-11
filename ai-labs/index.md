# AI Operations & RAG Engineering — Phase 6

> A source-linked, hands-on guide to grounded AI, retrieval, inference boundaries and safe automation. **Source review: 11 October 2026.** The lessons describe checked-in implementations and tests; they do not claim current public-cloud uptime or a comprehensive model-safety audit.

## How to use this guide

Read the design, inspect the linked code, perform the offline exercise, and record which conclusions are *implemented*, *tested with fakes*, *historically demonstrated*, or merely *proposed*. Start with the system boundary before tuning models.

| Sequence | Lesson | What you should be able to demonstrate |
| --- | --- | --- |
| 01 | [System boundaries](01-system-boundaries.md) | Distinguish rules, retrieval, LLM generation, and execution |
| 02 | [Ingestion and chunking](02-ingestion-chunking.md) | Explain ingestion, indexing and document identity |
| 03 | [Hybrid retrieval and reranking](03-hybrid-retrieval.md) | Trace the actual ranking stages and thresholds |
| 04 | [Evidence and abstention](04-grounding-abstention.md) | Identify unsupported answers and fail closed |
| 05 | [Bedrock and cloud identity](05-bedrock-iam.md) | Separate task IAM, network and application permissions |
| 06 | [LangGraph and MCP](06-langgraph-mcp.md) | Follow tool routing without granting write access |
| 07 | [Prompt injection and safety](07-prompt-injection.md) | Protect instructions, citations, tools and secrets |
| 08 | [Evaluation and regression gates](08-evaluation.md) | Measure retrieval quality with reproducible cases |
| 09 | [Telemetry, latency and cost](09-telemetry-cost.md) | Define useful, privacy-safe AI telemetry |
| 10 | [Safe automation case studies](10-automation-boundaries.md) | Compare PlatformPilot, CloudOps, OpsPilot and résumé scoring |
| 11 | [Capstone and interview review](11-capstone-review.md) | Design and defend a bounded operational assistant |

## Source repositories

- [RAG Ops Assistant](https://github.com/AZ1600/rag-ops-assistant): FastAPI, LangGraph, MCP, hybrid retrieval, reranking, Bedrock, and ECS/Fargate artifacts.
- [PlatformPilot](https://github.com/AZ1600/platform-pilot): deterministic Kubernetes advice and authenticated export boundaries.
- [CloudOps Command Center](https://github.com/AZ1600/cloudops-command-center): deterministic decision traces, operational evidence and approval-gated state changes.
- [OpsPilot SaaS](https://github.com/AZ1600/opspilot-saas): rule-based classification with optional schema-constrained model classification.
- [AI Resume Analyzer](https://github.com/AZ1600/ai-resume-analyzer-n8n): deterministic résumé evidence/score and separate Bedrock workflow.

## Validation discipline

The accompanying `validate-guide.py` checks documentation links and fences; `ai-labs/examples/evaluate_sample.py` checks a **synthetic, offline** retrieval fixture. These are not substitutes for the RAG repository's integration tests, live Bedrock checks, abuse testing, or production observability.

Back to [Chapter 10 — AI Operations](../10-AI-Operations/Chapter-10-AI-Operations.md) or [the handbook home](../index.md).
