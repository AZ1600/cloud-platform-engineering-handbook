# 11 — Capstone: Review a Safe Cross-project Operations Platform

**Scenario (proposed):** a platform team wants Kubernetes workload health, context from curated engineering documentation and a controlled way to propose remediation. It must not grant a model or documentation reader infrastructure write access.

## Produce an architecture pack

Use [PlatformPilot](../projects/PlatformPilot.md), [CloudOps](../projects/CloudOps-Command-Center.md), [RAG Ops](../projects/RAG-Ops-Assistant.md), [Backstage](../projects/Backstage-Developer-Portal.md) and [Observability](../projects/Observability-Platform.md) as **separate source-backed building blocks**. There is no verified end-to-end production integration of all five systems.

```text
Cluster metrics/events/logs --> PlatformPilot read API
                                  |
                                  v
                          structured finding
                                  |
Docs --> RAG read-only retrieval -+--> evidence review
                                  |
                                  v
                         CloudOps approval queue
                                  |
                     policy checks + owner sign-off
                                  |
                           narrow action executor
                                  |
                           verification + audit
```

The RAG-to-CloudOps line is a design proposal; show it dashed in a formal diagram. A safe path should preserve raw observations, independent authorization and a chance to abstain.

## Deliverables

1. **Context and container diagrams:** users, trust boundaries, data stores and external systems; identify which arrows already exist.
2. **Three quality attributes:** measurable availability, response latency and correctness of authorization (set hypothetical targets, mark them as unmeasured).
3. **Failure design:** missing Prometheus, stale retrieval index, replayed finding and unreachable CloudOps store.
4. **Security:** least-privilege permission table for viewer, finding exporter, approver and executor.
5. **State:** idempotency key, approval transitions and audit retention ownership.
6. **Operations:** SLO/alert, rollout and rollback, data backup and crisis runbook.
7. **Economics:** cost drivers for cloud cluster, logging, data retention and model calls.
8. **ADR:** explain whether to integrate synchronously or through a durable queue.

## Self-review rubric

Score 0 = missing, 1 = described but unverified, 2 = linked to relevant evidence or a concrete test plan. Total possible: 16.

| Dimension | 0 / 1 / 2 |
| --- | --- |
| Requirements and measurable quality attributes | |
| Request, event and trust-boundary clarity | |
| Least privilege and authorization | |
| State, retries and idempotency | |
| Resilience and rollback | |
| Observability and incident response | |
| Costs and lifecycle | |
| Evidence status and alternatives | |

## Interview practice

Explain the architecture in two minutes, then answer: What happens if CloudOps is down? Which record is authoritative for approval? How do you avoid double execution? Can an untrusted RAG chunk force a tool call? What protects Tenant B from Tenant A's finding? Why did you choose this messaging model? What is one consciously accepted risk?

**Acceptance criterion:** every major claim is either linked to a repository artifact, tested in a named environment or clearly marked *proposed*. Prefer a small, correct, explainable architecture over a large diagram with unsupported “production-grade” labels.

[Return to the architecture index](index.md)
