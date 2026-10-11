# Weekend Platform Evolution Roadmap

This roadmap turns my separate portfolio repositories into one connected platform-engineering system. It records what I am building, why the order matters, what can realistically be completed during the weekend, and what remains for the following 30, 60, and 90 days.

## Weekend sprint

**Dates:** Saturday 18 July 2026 and Sunday 19 July 2026
**Primary outcome:** demonstrate one evidence-based Kubernetes finding moving from PlatformPilot into CloudOps Command Center, through review and approval, with an audit trail.

The weekend is not intended to rebuild every repository. Its purpose is to establish the architecture, contracts, security boundaries, tests, and documentation needed for the projects to evolve safely.

## Problem being solved

Platform teams receive signals from Kubernetes, AWS, CI/CD, Terraform, and monitoring systems. A signal alone does not tell an engineer:

- what failed;
- what evidence proves it;
- which service and environment are affected;
- how serious it is;
- who owns the service;
- what action is safe;
- whether the action was approved;
- whether the action worked;
- how the decision can be audited later.

The connected platform will turn raw operational signals into explainable, owner-routed, approval-gated work.

## Repository roles

| Repository | Responsibility in the connected platform | Current evidence | Next evolution |
| --- | --- | --- | --- |
| PlatformPilot | Collect Kubernetes workload evidence | React/Vite frontend, FastAPI backend, Kubernetes Python client, Prometheus integration, logs, events, incidents, and AI summaries | Produce a reliable, versioned finding contract and use a secure cluster-access model |
| CloudOps Command Center | Evaluate, route, approve, and audit operational risks | Next.js risk engine, evidence, confidence, owner routing, runbooks, approval queue, execution log, Terraform import, GitHub Actions import, Vitest, and persistence boundary | Ingest PlatformPilot findings and persist their complete decision lifecycle |
| Backstage Developer Portal | Provide service identity, ownership, documentation, and self-service workflows | Backstage catalog, GitHub and Kubernetes integration foundations, TechDocs, and catalog graph | Become the authoritative service-ownership source and provide golden-path templates |
| OpsPilot SaaS | Demonstrate a multi-tenant commercial product layer | Next.js, Clerk, Neon Postgres, workspace RBAC, Stripe foundation, approvals, execution queue, health checks, and CI | Reuse proven tenant, authentication, billing, and audit patterns without merging its business domain into CloudOps |
| Terraform EKS | Provision repeatable infrastructure | Terraform and EKS modules and project evidence | Add environment separation, policy checks, drift evidence, and cost estimates |
| Argo CD GitOps | Reconcile approved application state | GitOps deployment workflow | Receive approved version changes through pull requests rather than direct cluster mutation |
| Observability Platform | Supply metrics and operational context | Prometheus, Grafana, Docker, and CloudWatch evidence | Add shared service identifiers and correlated logs, metrics, and traces |
| Pharmacy platforms | Act as realistic reference workloads | EKS and AWS serverless implementations | Supply controlled failure scenarios and measurable business/operational outcomes |
| Engineering Handbook | Preserve engineering knowledge and evidence | Project case studies, commands, debugging register, architecture, and interview explanations | Record every contract, decision, failure, fix, test, and limitation from this programme |

## Target workflow

```text
Pharmacy workload on Kubernetes
        |
        v
PlatformPilot collects Kubernetes evidence
        |
        v
Versioned operational finding
        |
        v
CloudOps validates and stores the finding
        |
        +--> ownership from service catalogue
        +--> evidence, severity, confidence, and impact
        +--> runbook and rollback information
        |
        v
Authorised person approves or dismisses
        |
        v
Controlled action or GitOps pull request
        |
        v
Verification, audit event, and incident record
```

## Shared finding contract

The first integration should use a small, explicit contract. It must be versioned before more signal sources are added.

```json
{
  "schemaVersion": "1.0",
  "findingId": "finding-123",
  "source": "platform-pilot",
  "observedAt": "2026-07-18T12:00:00Z",
  "cluster": "development-eks",
  "namespace": "pharmacy",
  "resource": {
    "kind": "Pod",
    "name": "pharmacy-api-abc123"
  },
  "service": "pharmacy-api",
  "category": "workload-health",
  "severity": "high",
  "confidence": 0.92,
  "summary": "The pharmacy API pod is repeatedly restarting.",
  "evidence": [],
  "recommendedRunbook": "crash-loop-investigation",
  "approvalRequired": true,
  "correlationId": "incident-456"
}
```

The contract must not include cluster credentials, tokens, secrets, full environment-variable values, or unnecessary personal data.

## Security boundaries

- PlatformPilot begins with read-only Kubernetes permissions.
- A hosted frontend must never receive a user's `kubeconfig` or service-account token.
- Cluster access belongs in a backend or an in-cluster agent with least-privilege permissions.
- CloudOps validates every incoming finding instead of trusting the sender.
- AI-generated text cannot authorise an operational change.
- Approval is checked on the server, not only hidden or shown in the browser.
- Every decision and execution attempt creates an audit event.
- Remediation commands are allow-listed and linked to a documented rollback.
- Secrets remain in managed secret stores and are redacted from logs and evidence.

## Saturday plan: understand and stabilise

### 1. Repository audit

- confirm frameworks, application boundaries, test commands, and deployment models;
- identify duplicated capabilities and select one owner for each responsibility;
- separate verified implementation from roadmap statements;
- record current defects and missing evidence.

### 2. Architecture and contracts

- finalise the finding schema;
- document lifecycle states: `detected`, `triaged`, `awaiting_approval`, `approved`, `dismissed`, `executing`, `succeeded`, and `failed`;
- define ownership, authentication, authorisation, audit, retry, and rollback boundaries;
- add example valid and invalid payloads.

### 3. PlatformPilot correctness

- inspect every container in a pod;
- distinguish `unknown` from `healthy`;
- discover and validate namespaces;
- align frontend and backend response contracts;
- return structured Kubernetes errors;
- create recorded fixtures for `CrashLoopBackOff` and `ImagePullBackOff`.

## Sunday plan: connect and prove

### 1. First integration

- generate one finding from a recorded PlatformPilot fixture;
- submit it to a CloudOps ingestion boundary;
- validate the schema and reject malformed input;
- prevent duplicate processing using `findingId`;
- display evidence, severity, confidence, service, and ownership.

### 2. Approval and audit

- require an authorised role for approval;
- record approval, dismissal, execution, and failure events;
- retain the original evidence alongside later decisions;
- keep execution simulated until the safety boundary is tested.

### 3. Verification

- run lint, type checking, unit tests, integration tests, and production builds;
- prove that malformed and duplicate findings are handled safely;
- demonstrate the chosen failure from detection to resolution;
- record commands, output, screenshots, defects, and limitations in the handbook.

## Weekend definition of done

The sprint is complete only when:

- the architecture and repository responsibilities are documented;
- the finding contract has valid and invalid examples;
- one PlatformPilot failure fixture produces a deterministic finding;
- CloudOps validates and displays that finding;
- the finding cannot execute without server-side approval;
- duplicate events do not create duplicate incidents;
- automated validation passes in both repositories;
- the debugging register explains failures encountered honestly;
- unfinished or simulated behaviour is labelled clearly;
- completed changes are committed and pushed intentionally.

## 30-day roadmap: reliable foundation

- finish PlatformPilot correctness fixes and contract tests;
- introduce a read-only cluster agent design;
- persist CloudOps finding lifecycle and audit events;
- integrate Backstage catalogue ownership;
- add OpenTelemetry identifiers across the first workflow;
- add CI validation for the shared contract;
- create five repeatable failure fixtures;
- establish service-level indicators for ingestion success, latency, and duplicates.

## 60-day roadmap: safe automation

- generate remediation pull requests instead of directly mutating production;
- add signed webhook or service authentication;
- integrate Argo CD deployment and rollback status;
- add notification routing;
- correlate GitHub Actions, Terraform, Kubernetes, and monitoring events;
- add policy-as-code checks and approval separation;
- create development, staging, and production configuration boundaries.

## 90-day roadmap: product evidence

- support multiple clusters and workspaces;
- complete tenant and role isolation testing;
- add cost per cluster, service, finding, and AI operation;
- measure detection time, acknowledgement time, resolution time, and false-positive rate;
- run load, resilience, and recovery tests;
- publish an end-to-end demonstration and architecture case study;
- interview real platform engineers or small teams and adjust the roadmap using their problems rather than assumptions.

## Decision log

### D-001: Connect existing capabilities before adding new ones

CloudOps already models evidence, confidence, owners, runbooks, approvals, execution events, and audit history. PlatformPilot already reads Kubernetes resources, events, logs, and Prometheus data. The first improvement is therefore an integration contract, not another dashboard or another independent AI feature.

### D-002: Keep OpsPilot's domain separate

OpsPilot solves business operations problems for small service companies. Its authentication, tenant, billing, approval, and persistence patterns can inform CloudOps, but the products should not be merged into one confusing application.

### D-003: Keep remediation approval-gated

The initial integration remains read-only and uses simulated execution. Real changes will be introduced only after authentication, authorisation, allow-listing, rollback, audit, and failure handling are verified.

## Questions this programme must answer

- Which user experiences the problem often enough to use the platform?
- What evidence makes a finding trustworthy?
- How is service ownership established and kept current?
- What happens when PlatformPilot or CloudOps is unavailable?
- How are duplicates, late events, and conflicting findings handled?
- Which actions are safe to automate, and which always need a person?
- What measurable outcome improved because the platform existed?
