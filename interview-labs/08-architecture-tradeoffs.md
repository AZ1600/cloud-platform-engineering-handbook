# 08 — Explain Architecture Trade-offs, Not Tool Preferences

## Requirement-driven choices

| Decision | Good reason to choose A | Good reason to choose B | Evidence boundary |
| --- | --- | --- | --- |
| EKS vs Lambda | Long-running controlled containers and Kubernetes platform needs | Event-driven, managed scaling | Compare [Pharmacy EKS](../projects/Pharmacy-API-EKS.md) with [serverless Pharmacy](../projects/Cloud-Native-Pharmacy-Platform.md) |
| Terraform vs Bicep | Cross-provider IaC ecosystem / module composition | Native Azure resource-model integration | See [Terraform EKS](../projects/Terraform-AWS-EKS-Platform.md) and [PropertyOps](../projects/PropertyOps-Azure.md) |
| Polling vs push | Simplicity and bounded change cadence | Lower latency or event-driven propagation | Explain delivery ordering, retries and consistency |
| Rules vs LLM | Deterministic, testable, predictable action classification | Flexible explanation on difficult inputs | See [PlatformPilot](../projects/PlatformPilot.md) and [RAG Ops](../projects/RAG-Ops-Assistant.md) |
| CI direct deploy vs GitOps | Small pipeline and simpler release flow | Declarative reconciliation and audit of desired state | See [Argo CD](../projects/GitOps-ArgoCD.md) |
| Relational vs JSON file storage | Durability, concurrency and constraints | Local demo simplicity | See [OpsPilot](../projects/OpsPilot-SaaS.md) |

## How to defend a decision

1. Identify the **constraint** (latency, team skill, budget, recovery, compliance or delivery velocity).
2. List two viable options and state the decision criteria.
3. Trace a nominal request and a failure request through the chosen design.
4. Identify the cost, security and reliability responsibilities that remain.
5. Say which new measurement or requirement would justify a redesign.

## The "what changes at 10×?" exercise

**Prompt:** OpsPilot grows from a single-team demonstration into a higher-concurrency tenant-based SaaS.

Do not promise a specific throughput number. Ask about read/write traffic, tenant distribution, database bottlenecks, connection limits, external API quotas and RTO. The [OpsPilot repository contract](https://github.com/AZ1600/opspilot-saas/blob/main/lib/server/workspace-repository.ts) provides a seam between implementation and persistence. Integration tests cover scoped tenant access, but load-test evidence must be gathered separately.

**Reasonable evolution:** durable PostgreSQL, indexes from real query plans, application statelessness, idempotency of approval jobs, tenant-aware telemetry, rate limits and staged load testing.

## Practice output

Write a one-page ADR with: title, context, requirements, options, decision, consequences, security impacts, experiment, rollback and status. Compare against [Phase 7 ADR practice](../architecture-labs/10-adrs-review.md).
