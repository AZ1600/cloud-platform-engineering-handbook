# 10 — Architecture Decision Records (ADRs) and Review Gates

**Objective:** leave a durable explanation of *why* a decision was made and when it should be revisited. The decision record should be shorter than the system specification.

## Mini ADR: review-only Terraform in CI

```text
ADR-007: Plan-only AWS validation for EKS
Status: Accepted for the portfolio validation workflow
Context: Kubernetes clusters cost money and carry operational risk.
Decision: CI validates tests, security and remote-state-aware AWS plans;
          no unattended terraform apply in CI.
Alternatives: auto-apply after main merge; purely offline mock plans.
Benefits: demonstrates cloud auth and real plan validation with lower risk.
Costs: deployment is a separate manual/controlled operation.
Revisit when: a funded, governed environment and approval process exist.
Evidence: platform-engineering-terraform-eks workflow and README.
```

This is a **teaching summary** of the published repository's current plan-only approach, not a committed ADR file from that project. See [the Terraform EKS project](https://github.com/AZ1600/platform-engineering-terraform-eks).

## Record template

Copy this structure to a review document:

```text
Title / ID:
Status and date:
Driver / owner:
Context and measurable constraints:
Decision:
Alternatives (include do nothing):
Consequences (positive, negative, operational):
Security and data boundaries:
Failure and recovery:
Cost and capacity assumptions:
Validation evidence (links + test scope):
Rollback or migration path:
Triggers for reconsideration:
```

## Architecture review gates

- **Requirements:** user journey, SLO, RPO/RTO, data class and non-goals defined.
- **Safety:** identity, authorization, secrets and tenancy traced end-to-end.
- **State:** system of record, schema evolution, retries and failure handling explained.
- **Operability:** dashboard, runbook, rollout, rollback and owner identified.
- **Evidence:** statements link to implementation/tests rather than diagrams alone.
- **Economics:** reserved/idle costs, egress, burst headroom and teardown accounted for.

Never treat a passing linter as a substitute for threat modelling or a working live deployment.

## Exercise

Write two ADRs for the same requirement: (a) EKS versus managed serverless; (b) synchronous email provider call versus transactional outbox. Make opposing alternatives credible. Then review each ADR from the perspective of a security engineer, an SRE and a cost owner.

[Next: Design capstone](11-capstone-design-review.md)
