# 01 — Requirements Before Services

**Objective:** translate a business objective into decisions you can test. Selecting EKS, Lambda or Container Apps before knowing the constraint is a solution looking for a problem.

## Capture the workload

Example brief: *A property manager needs a request reviewed, approved and audited. Operators must not be able to bypass approval.*

| Type | Requirement | Acceptance signal |
| --- | --- | --- |
| Functional | Create a maintenance request and review a triage proposal | API and UI flow tested |
| Security | Only an authorised reviewer can approve | Forbidden-path tests and audit actor |
| Reliability | A repeated approval request must not create duplicate actions | Retry/idempotency test |
| Operability | An engineer can trace a failed decision | Correlation ID, event, outcome |
| Recovery | Lost API process does not erase durable approvals | Persistent repository and restore rehearsal |
| Cost | Environment can be stopped without untracked spend | IaC plan, budget and teardown evidence |

**Non-functional requirements require a unit and window.** “Fast” is untestable; “P95 request latency below 400 ms over a 30-day rolling period under the agreed workload” is testable, although that target is a *sample*, not a measured result from the user's repositories.

## Separate constraints from assumptions

For each system, document workload shape, traffic pattern, RPO/RTO, data classification, tenancy, team size, budget and compliance obligations. Put unknowns in an assumption register with the validation owner. Do not silently assume 99.99% availability from a single running container.

## Trace each requirement to evidence

The [PropertyOps repository](https://github.com/AZ1600/AI-property-operations) documents human approval and Microsoft Entra roles; inspect authentication and state-transition routes to verify the exact enforcement. The [OpsPilot PostgreSQL isolation test](https://github.com/AZ1600/opspilot-saas/blob/main/tests/integration/tenant-isolation.postgres.ts) is narrower evidence: it tests isolation under its configured local test database rather than every possible deployed configuration.

## Architecture exercise

Create a one-page brief for either PropertyOps or OpsPilot with a maximum of **three** priorities, two measurable quality requirements, three failure modes and one explicit non-goal. Then pick **two competing runtimes** and explain why each meets or misses the priorities. Include a rollback and ownership plan.

**Review question:** what observation would cause you to revisit your choice?

[Next: Context, containers and boundaries](02-context-containers-boundaries.md)
