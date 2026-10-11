# Project index — October 2026

This catalogue links current repositories to architectural themes and implementation evidence. **Last repository structure/README review: 11 October 2026.** The review did not run or deploy every system.

## Flagship studies

| Case study | Engineering focus | Starting evidence |
| --- | --- | --- |
| [PlatformPilot](PlatformPilot.md) | Kubernetes observability and operational RBAC | [Backend security tests](https://github.com/AZ1600/platform-pilot/tree/main/backend/tests), [architecture](https://github.com/AZ1600/platform-pilot/blob/main/docs/ARCHITECTURE.md) |
| [CloudOps Command Center](CloudOps-Command-Center.md) | Risk processing, decision evidence and human approval | [Contract](https://github.com/AZ1600/cloudops-command-center/tree/main/contracts), [tests](https://github.com/AZ1600/cloudops-command-center/tree/main/tests) |
| [OpsPilot SaaS](OpsPilot-SaaS.md) | Multi-tenant product workflows, RBAC and persistence | [Integration tests](https://github.com/AZ1600/opspilot-saas/tree/main/tests/integration), [schema](https://github.com/AZ1600/opspilot-saas/blob/main/database/schema.sql) |
| [PropertyOps on Azure](PropertyOps-Azure.md) | Secure Azure application infrastructure | [Bicep modules](https://github.com/AZ1600/AI-property-operations/tree/main/infra), [deployment evidence](https://github.com/AZ1600/AI-property-operations/tree/main/docs/screenshots) |

## Infrastructure and delivery

| Project | What to learn |
| --- | --- |
| [Terraform AWS EKS](Terraform-AWS-EKS-Platform.md) | Modular IaC, Terraform native tests, cloud OIDC plan validation |
| [Pharmacy API on EKS](Pharmacy-API-EKS.md) | Cognito auth, Pod Identity, DynamoDB and Kubernetes resilience |
| [AZ-104 Azure Infrastructure](AZ104-Azure-Infrastructure.md) | Bastion, VNet, scoped RBAC, Private Link, Bicep and backup |
| [Backstage Developer Portal](Backstage-Developer-Portal.md) | Software catalog, developer golden paths and service scaffolding |
| [GitOps with Argo CD](GitOps-ArgoCD.md) | Declarative delivery and reconciliation in local Kubernetes |
| [CI/CD Pipeline](CI-CD-Pipeline.md) | Container scanning, SBOMs, ECR and attestations |
| [Observability Platform](Observability-Platform.md) | Metrics, traces, logs, SLOs and rule tests |
| [Cloud-Native Pharmacy Platform](Cloud-Native-Pharmacy-Platform.md) | Multi-tenant serverless inventory workflow and integration status |

## AI systems and automation

| Project | What to learn |
| --- | --- |
| [RAG Ops Assistant](RAG-Ops-Assistant.md) | Bedrock, LangGraph, MCP, retrieval evaluation and AWS ECS |
| [AI Resume Analyzer](AI-Resume-Analyzer.md) | Deterministic scoring, n8n and Bedrock workflow integration |
| [AI Content Automation](AI-Content-Automation-Platform.md) | Lambda, OAuth, AWS scheduling and human-reviewed publishing |

## Reference and plans

The [Cloud Control Plane](Cloud-Control-Plane.md) is a **vision/reference page**, not a deployed unified control plane. The separately generated [Backstage inventory API](https://github.com/AZ1600/backstage-generated-inventory-api) is a scaffold demonstration. The [ASP.NET migration utility](https://github.com/AZ1600/migrationASP.NET) is retained as reference material; authorship/provenance is not established here. The portfolio source and this handbook are documentation repositories rather than application case studies.

## Where to go next

- [Evidence guide](Engineering-Evidence-Guide.md) — what counts as implementation proof, and how to avoid overclaiming.
- [Technology-to-project map](../TECHNOLOGY-PROJECT-MAP.md) — historical technology cross-reference (may require updating).
- [Command reference](../13-Command-Reference/Chapter-13-Commands.md) — project commands and troubleshooting context.

**Maintainer note:** Older project pages include earlier verification dates; use the source links above for fresh source artifacts and update the individual case study before making a current production claim.
