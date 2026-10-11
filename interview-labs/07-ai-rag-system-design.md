# 07 — AI/RAG System Design Interview

## Scenario: build an operations knowledge assistant

**Functional requirement:** answer technical questions using authorised operational documents and return traceable evidence. **Quality requirements:** privacy, bounded costs, graceful abstention, controlled actions and measurable retrieval quality.

```text
Question -> identity/corpus scope -> query embedding + keyword search
          -> hybrid candidate ranking -> cross-encoder reranking
          -> evidence threshold -> Bedrock explanation + source citations
          -> answer with evidence or explicit abstention
```

The [RAG Ops Assistant](https://github.com/AZ1600/rag-ops-assistant) contains a local NumPy embedding index, a 75% semantic / 25% keyword hybrid weighting and cross-encoder reranking in [rag_core.py](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/rag_core.py). A LangGraph flow calls an MCP knowledge-base tool and uses Bedrock for text generation. This is not evidence that all security and quality edge cases have been tested.

## Three critical follow-ups

**1. "What happens when the knowledge base lacks the answer?"** An explicit no-evidence path should abstain before producing an unsupported documentation claim. Check [tool output](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/tools.py) and [the agent](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/langgraph_agent.py). An unrelated general-chat route must not be described as corpus-grounded.

**2. "How do you test relevance?"** The repository defines a [retrieval evaluation suite](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/evaluate.py) and cases including a negative annual-leave question. Distinguish retrieval source correctness from answer faithfulness; evaluate both, along with prompt-injection resistance.

**3. "How would this assistant safely change infrastructure?"** It should not issue free-form commands based on generated text. Propose a typed, limited action contract, policy checks, engineer approval, execution record and recovery. The cross-project integration is **proposed**, not an existing autonomous executor.

## AWS cost and identity

Review task IAM role scope for Bedrock invocation, request/response token cost, embedding/reranking compute, index freshness, latency budgets and log redaction. Deployment to ECS Fargate is documented in the repository; present any live run as a dated observation, not current availability.

## Design test

Create 5 questions with expected sources, 2 unsupported questions, 2 prompt-injection documents, and 1 authorisation-negative case. Record source recall, abstention accuracy, unsupported-claim rate and cost per request.

See [AI/RAG labs](../ai-labs/index.md) and [RAG project case study](../projects/RAG-Ops-Assistant.md).
