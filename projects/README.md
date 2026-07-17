# Project Index

This index connects the handbook to the engineering projects behind it. It is designed to make the knowledge base useful for learning, interviews, portfolio reviews, and future project work.

For the dated inventory of all owned repositories, including the handbook and reference material, see the [Project and Work Register](../PROJECT-WORK-REGISTER.md). For commands grouped by project, see [Commands Used Across My Projects](../13-Command-Reference/Chapter-13-Commands.md).

## Project Portfolio

| Project | Purpose | Confirmed technologies | Status in this handbook |
|---|---|---|---|
| [PlatformPilot](PlatformPilot.md) | AI-assisted Kubernetes operations dashboard | React 19, FastAPI, Python 3.12, Kubernetes Python Client | Repository verified; detailed study in progress |
| [CloudOps Command Center](CloudOps-Command-Center.md) | Explainable, approval-gated infrastructure risk remediation | Next.js, React, TypeScript, Vitest, GitHub Actions | Repository verified; detailed study in progress |
| [Terraform AWS EKS Platform](Terraform-AWS-EKS-Platform.md) | Reproducible Kubernetes platform on AWS | Terraform, AWS, EKS | Repository verified; detailed study in progress |
| [Pharmacy API on EKS](Pharmacy-API-EKS.md) | Cloud-native pharmacy API deployed to Amazon EKS | FastAPI, Docker, EKS, ECR, DynamoDB, SQS, EventBridge | Repository verified; initial study created |
| [GitOps with Argo CD](GitOps-ArgoCD.md) | Declarative continuous delivery to Amazon EKS | Argo CD, Kubernetes, GitHub, EKS | Repository verified; initial study created |
| [Backstage Developer Portal](Backstage-Developer-Portal.md) | Internal developer portal and software catalogue | Backstage, TypeScript, Node.js, Docker, Kubernetes, TechDocs | Repository verified; initial study created |
| [OpsPilot SaaS](OpsPilot-SaaS.md) | AI-assisted operations SaaS for small service businesses | Next.js, TypeScript, PostgreSQL, Neon, Clerk, Stripe, Vitest | Repository verified; initial study created |
| [AI Content Automation](AI-Content-Automation-Platform.md) | Serverless multi-account social publishing operations | Lambda, API Gateway, DynamoDB, EventBridge, Secrets Manager, SAM | Repository verified; initial study created |
| [AI Resume Analyzer](AI-Resume-Analyzer.md) | Automated role-readiness and skill-gap analysis | n8n, AWS Bedrock, Amazon Nova Pro, JavaScript, Docker Compose | Repository verified; initial study created |
| [Cloud-Native Pharmacy Platform](Cloud-Native-Pharmacy-Platform.md) | Multi-tenant serverless inventory and low-stock workflows | Lambda, API Gateway, DynamoDB, Cognito, SQS, EventBridge, SAM | Repository verified; initial study created |
| [CI/CD Pipeline](CI-CD-Pipeline.md) | Automated container build and publication to ECR | GitHub Actions, Docker, ECR, IAM | Repository verified; initial study created |
| [Observability Platform](Observability-Platform.md) | Local metrics collection and dashboard visualisation | Prometheus, Grafana, Docker Compose | Repository verified; initial study created |
| [Cloud Control Plane](Cloud-Control-Plane.md) | Future platform combining cloud, Kubernetes, observability, automation, and AI assistance | Planned; to be selected | Vision documented |

## Project-to-Knowledge Map

| Knowledge area | Strongest project evidence |
|---|---|
| Kubernetes operations | PlatformPilot, Pharmacy API |
| AWS application architecture | Pharmacy API, AI Content Automation |
| Infrastructure as code | Terraform AWS EKS, AI Content Automation with AWS SAM |
| GitOps and continuous delivery | GitOps with Argo CD |
| Internal developer platforms | Backstage Developer Portal |
| Cloud risk and remediation workflows | CloudOps Command Center |
| Production-style SaaS foundations | OpsPilot SaaS |
| Serverless and event-driven automation | AI Content Automation |
| AI-assisted operational workflows | PlatformPilot, CloudOps, OpsPilot |
| Generative AI workflow automation | AI Resume Analyzer |
| CI and container publication | Platform Engineering CI/CD Pipeline |
| Metrics and dashboards | Platform Engineering Observability |

## Full GitHub Inventory

The authenticated account inventory found 15 owned repositories on 2026-07-11:

- 12 engineering repositories represented in this handbook;
- this handbook repository itself;
- `migrationASP.NET`, retained as a reference/migration lab pending confirmation of provenance and personal contribution;
- `AZ1600.github.io`, intentionally excluded from the handbook project portfolio.

Repository ownership alone is not enough to call work an original project. The final handbook will distinguish original builds, guided labs, upstream code, experiments, and future concepts.

Repository README files were verified on 2026-07-11. Deeper chapters will verify implementation files before making code-level or production-readiness claims.

## Evidence Standard

A strong project case study should link to evidence wherever possible:

- source repository and tagged release;
- architecture diagram;
- setup and deployment instructions;
- API or interface screenshots;
- infrastructure and pipeline configuration;
- monitoring dashboard or alert example;
- test output or quality checks;
- incident note, trade-off record, or architecture decision record;
- short demonstration video.

## Adding the Next Project

1. Copy the [project case-study template](../templates/project-case-study-template.md).
2. Replace every placeholder with verified information from the project.
3. Add the project to both tables on this page.
4. Link the case study to relevant handbook chapters.
5. Record at least one decision and one lesson learned.
6. Add evidence before describing the case study as complete.
