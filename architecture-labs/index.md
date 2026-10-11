# Architecture & System Design — Phase 7 Field Guide

> Source-informed learning material inspected **11 October 2026**. Repository files demonstrate code/configuration, not live uptime, security accreditation, load-test results or currently provisioned cloud resources. Proposals are explicitly marked.

Architecture starts with a user need and a constraint—not a cloud service. These eleven lessons build a repeatable method for discussing system boundaries, failure, identity, state, costs and evidence.

## Learning sequence

| Lesson | Decision you should be able to defend |
| --- | --- |
| [01 — Requirements and quality attributes](01-requirements-quality.md) | What are we optimizing for, and how do we measure it? |
| [02 — Context, containers, trust boundaries](02-context-containers-boundaries.md) | What crosses each boundary? |
| [03 — State, events and idempotency](03-data-events-idempotency.md) | What prevents duplicate work and inconsistent writes? |
| [04 — Reliability and capacity](04-reliability-capacity.md) | What fails, how do we detect it, and how do we recover? |
| [05 — Security architecture](05-identity-security.md) | Which identity can do exactly what? |
| [06 — AWS and Azure decisions](06-cloud-tradeoffs.md) | What is implemented versus planned in each cloud? |
| [07 — Internal Developer Platforms](07-idp-platform-boundaries.md) | Where do templates, delivery and runtime authority differ? |
| [08 — Multi-tenant SaaS](08-saas-tenant-architecture.md) | How are tenants isolated at every layer? |
| [09 — AI and operational control planes](09-ai-control-plane.md) | Why must evidence and approval be separate from actions? |
| [10 — ADRs and architecture reviews](10-adrs-review.md) | How do we record alternatives and consequences? |
| [11 — Capstone and interview exercises](11-capstone-design-review.md) | Can we review an end-to-end design with explicit trade-offs? |

## Source map

- [OpsPilot](https://github.com/AZ1600/opspilot-saas): multi-tenant repository contract, isolated PostgreSQL tests and approval idempotency.
- [CloudOps](https://github.com/AZ1600/cloudops-command-center): deterministic Decision Trace and approval gate.
- [PlatformPilot](https://github.com/AZ1600/platform-pilot): Kubernetes API and Prometheus access, application RBAC.
- [Backstage portal](https://github.com/AZ1600/platform-engineering-backstage-portal): scaffolder template with repository publish and catalog registration.
- [Argo CD GitOps](https://github.com/AZ1600/platform-engineering-gitops-argocd): reconciled NGINX demo and isolated AppProject.
- [Terraform EKS](https://github.com/AZ1600/platform-engineering-terraform-eks): reusable infrastructure and plan-only AWS CI.
- [PropertyOps](https://github.com/AZ1600/AI-property-operations): deployed Azure components and prepared-but-unused Container Apps VNet subnet.
- [RAG Ops Assistant](https://github.com/AZ1600/rag-ops-assistant): read-only retrieval tool, model boundary and no-evidence guard.

## Evidence convention

**Implemented** means a source artifact is present; **tested** names the actual test scope; **deployed evidence** is historical unless freshly checked; **proposed** means a design exercise. Never convert a diagram into a claim about production state.

**Safe exercises:** inspect repository code, sketch boundaries, and complete checklists. No cloud writes or production remediation are required.

Return to [Chapter 11](../11-Architecture/Chapter-11-Architecture.md) or [the project index](../projects/README.md).
