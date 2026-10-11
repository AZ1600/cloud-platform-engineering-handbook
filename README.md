# Cloud & Platform Engineering Handbook

*A living, project-led knowledge base by Olawale Azeez.*

[Portfolio](https://az1600.github.io/) · [GitHub](https://github.com/AZ1600) · [Project index](projects/README.md) · [Evidence standard](projects/Engineering-Evidence-Guide.md)

## Purpose

This handbook connects foundational knowledge to implementation. Topics cover Linux, cloud infrastructure, Docker, Kubernetes, AWS, Azure, Terraform, CI/CD, GitOps, observability, secure operations and AI systems. Every significant technical claim should be tied to code, configuration, tests, reproducible commands, a verified screenshot or a clearly marked engineering decision.

## Start with project-led learning

| Learning path | Suggested sequence |
| --- | --- |
| Platform engineering | [PlatformPilot](projects/PlatformPilot.md) → [CloudOps](projects/CloudOps-Command-Center.md) → [Backstage](projects/Backstage-Developer-Portal.md) |
| AWS cloud engineering | [Terraform EKS](projects/Terraform-AWS-EKS-Platform.md) → [Pharmacy API](projects/Pharmacy-API-EKS.md) → [RAG Ops](projects/RAG-Ops-Assistant.md) |
| Azure cloud engineering | [AZ-104 infrastructure lab](projects/AZ104-Azure-Infrastructure.md) → [PropertyOps](projects/PropertyOps-Azure.md) |
| Observability/SRE | [Observability platform](projects/Observability-Platform.md) → [PlatformPilot](projects/PlatformPilot.md) → [CloudOps](projects/CloudOps-Command-Center.md) |
| Product and AI operations | [OpsPilot SaaS](projects/OpsPilot-SaaS.md) → [RAG Ops](projects/RAG-Ops-Assistant.md) → [AI resume analyzer](projects/AI-Resume-Analyzer.md) |

## Learning chapters

Use the existing chapters under `01-Cloud-Fundamentals` through `14-Lessons-Learned` to study concepts, then return to the relevant implementation. Consult the [command reference](13-Command-Reference/Chapter-13-Commands.md) before reproducing commands.

## Technical writing standard

1. State the problem and why the technology was selected.
2. Draw the request/data/control path and trust boundaries.
3. Link to the implementation and the relevant test or validation artifact.
4. Distinguish *implemented*, *locally validated*, *cloud validated*, *documented*, and *planned*.
5. Record a failure mode, a trade-off, and an explicit next improvement.
6. Recheck links, secrets, deployment costs, and version assumptions before publication.

See [Engineering Evidence Guide](projects/Engineering-Evidence-Guide.md) for a reusable case-study checklist.

## Platform evolution roadmap

The [Weekend Platform Evolution Roadmap](WEEKEND-PLATFORM-EVOLUTION-ROADMAP.md) connects PlatformPilot, CloudOps Command Center, Backstage, GitOps and observability into a coordinated engineering platform. It documents the planned integration milestones and 30/60/90-day evolution strategy.

## Freshness and scope

The project catalogue was refreshed on **2026-10-11** from public GitHub repository trees and READMEs. This is a source inspection, not a fresh execution of all CI pipelines, cloud workloads or performance benchmarks. Some older learning chapters preserve earlier dated observations; they should not be treated as current audit results.

## Build locally

```bash
npm ci
npm run docs:dev
npm run docs:build
```

The documentation site uses VitePress. Avoid treating this educational reference as production operational guidance without verifying current provider documentation, security requirements and deployment context.

<!-- phase2-kubernetes-platform-start -->
## Kubernetes and Platform Engineering — hands-on deep dives

The [Phase 2 field guide](labs/index.md) extends Chapters 4 and 6 with practical investigation steps, role and identity boundaries, real repository code reviews and review exercises. It uses PlatformPilot, the Backstage developer portal, CloudOps and related workload manifests as evidence. Source references were inspected on **11 October 2026**; live deployment and CI status are not implied.

<!-- phase3-aws-azure-depth -->
## AWS and Azure Infrastructure — Phase 3 field guide

Continue with the [AWS/Azure hands-on labs](cloud-labs/index.md), covering VPC-to-EKS flow, Terraform state and guardrails, AWS identity boundaries, Azure Private Link, Bicep What-If, PropertyOps deployment topology, incident troubleshooting and cost-aware lifecycle controls. The lessons are grounded in source reviewed **11 October 2026**; live deployment health is not assumed.

<!-- phase4-cicd-gitops-devsecops -->
## CI/CD, GitOps and DevSecOps — practical delivery field guide

The [Phase 4 delivery labs](delivery-labs/index.md) connect real GitHub Actions, ECR publication, OIDC, container hardening, SBOM and attestation evidence, Argo CD reconciliation, Terraform CI and EKS release verification. The labs distinguish implemented workflows from proposed integrations, and avoid cloud writes by default.

<!-- phase5-observability-sre -->
## Observability, SRE and incident response — Phase 5 field guide

The [Phase 5 SRE labs](sre-labs/index.md) expand Chapter 9 with source-backed telemetry architecture, RED metrics, PromQL, traces/log correlation, Grafana, SLOs and burn-rate alerts, rule tests, incident response, PlatformPilot and CloudOps diagnostic boundaries, and a capstone postmortem. The material distinguishes source review from live deployment validation.

<!-- phase6-ai-ops-rag -->
## AI Operations and RAG Engineering — Phase 6 field guide

The [Phase 6 AI/RAG labs](ai-labs/index.md) connect RAG Ops Assistant, Bedrock, LangGraph, MCP, PlatformPilot, CloudOps, OpsPilot and résumé-scoring projects. They separate implemented source behavior, mocked API tests, synthetic evaluation fixtures and production-hardening proposals.
