# 09 — AI Telemetry, Latency, Reliability and Cost

## Observability goals

An assistant requires both conventional API monitoring and evidence-quality monitoring. A fast response with the wrong citations is a reliability failure, even if the HTTP status is 200.

```text
request -> retrieval -> rerank -> tool orchestration -> model -> validation
          |            |         |                  |
        timings      candidates  tool status        tokens/cost
                 -> evidence IDs and outcome
```

## Suggested metrics (design exercise, not existing dashboards)

| Signal | Suggested dimension | Avoid |
| --- | --- | --- |
| Query latency | route and outcome | user question as a metric label |
| Retrieval latency | index/version | full chunk content in logs |
| Evidence hit rate | found vs not-found | interpreting empty evidence as network failure |
| Abstention ratio | corpus and reason | pressuring model to answer unsupported questions |
| Tool failure rate | tool name and status | logging tokens or credentials |
| Bedrock errors | throttling, invalid request, timeout | unbounded retries |
| Model cost | model ID, usage count, authorized project | personal identifiers as labels |

The RAG repository documents ECS/Fargate, Bedrock and CloudWatch logging, but these suggested metric names and dashboards are **not verified as implemented**. Add them explicitly and test emitted data before claiming operational coverage.

## Distributed debugging example

A user sees a grounded answer take 12 seconds. Record timestamps for the API request, retrieval index load, embeddings, rerank, MCP hop, Bedrock tool call, second model pass and final serialization. Determine whether startup/index loading or inference drives tail latency; only then consider caching.

## Privacy and cost

Do not log raw résumé text, tenant-specific runbooks, credentials or full prompt bodies by default. Use stable non-sensitive IDs and sampled/redacted traces. Measure:

```text
monthly_estimated_cost = invocation_cost + hosting_cost + storage_cost + networking_cost
```

Bedrock pricing, invocation mode and region may change; obtain current provider pricing before estimating numbers. For a low-traffic personal project, a continuously running ECS service and load balancer may dominate total cost; measure billing rather than guessing.

## Read-only study references

- [RAG Ops ECS deployment architecture](https://github.com/AZ1600/rag-ops-assistant#aws-deployment)
- [Phase 5 SRE field guide](../sre-labs/index.md)
- [Observability handbook chapter](../09-Observability/Chapter-09-Observability.md)

Next: [safe automation comparisons](10-automation-boundaries.md).
