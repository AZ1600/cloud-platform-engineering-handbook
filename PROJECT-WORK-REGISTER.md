# Project and Work Register

> A dated inventory of the projects represented by this handbook and the evidence used to describe them.

**GitHub account audited:** `AZ1600`  
**Last repository inventory:** 2026-07-17  
**Owned repositories found:** 15

## Why This Register Exists

This file answers four questions:

1. What have I worked on?
2. What engineering area does each project demonstrate?
3. Where is the corresponding handbook explanation?
4. How strong is the available evidence?

Repository ownership is not automatically proof that every line is original work. The handbook distinguishes original builds, learning projects, reference material and planned work.

## Portfolio Register

| Repository | What the project demonstrates | Handbook case study | Evidence reviewed |
|---|---|---|---|
| [`platform-pilot`](https://github.com/AZ1600/platform-pilot) | React/FastAPI Kubernetes operations dashboard, metrics and rule-based analysis | [PlatformPilot](projects/PlatformPilot.md) | README, frontend/backend source, Dockerfile and package scripts |
| [`cloudops-command-center`](https://github.com/AZ1600/cloudops-command-center) | Infrastructure-risk ingestion, owner routing, approvals, audit and remediation workflow | [CloudOps](projects/CloudOps-Command-Center.md) | README and package scripts |
| [`opspilot-saas`](https://github.com/AZ1600/opspilot-saas) | Multi-tenant operational SaaS, authentication, PostgreSQL, roles, billing foundation and approvals | [OpsPilot SaaS](projects/OpsPilot-SaaS.md) | README and package scripts |
| [`pharmacyEKS-`](https://github.com/AZ1600/pharmacyEKS-) | FastAPI container deployed on EKS with Kubernetes and AWS integrations | [Pharmacy API on EKS](projects/Pharmacy-API-EKS.md) | README and Kubernetes manifests |
| [`CloudNativePharmacyPlatform`](https://github.com/AZ1600/CloudNativePharmacyPlatform) | Serverless multi-tenant API, Cognito, DynamoDB, SQS, EventBridge and SAM | [Cloud-Native Pharmacy](projects/Cloud-Native-Pharmacy-Platform.md) | README, CodeBuild specification and SAM configuration |
| [`platform-engineering-terraform-eks`](https://github.com/AZ1600/platform-engineering-terraform-eks) | Terraform-provisioned VPC, IAM, KMS, EKS and managed nodes | [Terraform EKS](projects/Terraform-AWS-EKS-Platform.md) | README and documented validation workflow |
| [`platform-engineering-gitops-argocd`](https://github.com/AZ1600/platform-engineering-gitops-argocd) | GitOps reconciliation from GitHub through Argo CD to EKS | [GitOps with Argo CD](projects/GitOps-ArgoCD.md) | README and Kubernetes manifests |
| [`platform-engineering-cicd-pipeline`](https://github.com/AZ1600/platform-engineering-cicd-pipeline) | GitHub Actions container build and publication to Amazon ECR | [CI/CD Pipeline](projects/CI-CD-Pipeline.md) | README and documented workflow |
| [`platform-engineering-observability`](https://github.com/AZ1600/platform-engineering-observability) | Prometheus and Grafana running with Docker Compose | [Observability](projects/Observability-Platform.md) | README and Compose configuration |
| [`platform-engineering-backstage-portal`](https://github.com/AZ1600/platform-engineering-backstage-portal) | Backstage software catalogue, TechDocs and internal developer portal | [Backstage Portal](projects/Backstage-Developer-Portal.md) | README and package scripts |
| [`AI-Powered-Content-Automation-Platform`](https://github.com/AZ1600/AI-Powered-Content-Automation-Platform) | Serverless OAuth, planning, queueing and scheduled X publishing | [Content Automation](projects/AI-Content-Automation-Platform.md) | README, SAM deployment commands and repository structure |
| [`ai-resume-analyzer-n8n`](https://github.com/AZ1600/ai-resume-analyzer-n8n) | n8n workflow, JavaScript scoring and AWS Bedrock analysis | [AI Resume Analyzer](projects/AI-Resume-Analyzer.md) | README and Compose configuration |
| [`cloud-platform-engineering-handbook`](https://github.com/AZ1600/cloud-platform-engineering-handbook) | This project-led learning and interview handbook | [Handbook README](README.md) | Local working tree and GitHub repository metadata |
| [`migrationASP.NET`](https://github.com/AZ1600/migrationASP.NET) | AWS Elastic Beanstalk migration-assistant material | Not presented as an original flagship project | README resembles upstream AWS documentation; personal contribution not established |

`AZ1600.github.io` was found during the GitHub inventory but is intentionally excluded from the handbook project portfolio at the owner's request.

## Work Streams Covered

### Application and API engineering

- React and Next.js interfaces.
- FastAPI and Next.js API routes.
- Python and TypeScript application logic.
- PostgreSQL and DynamoDB persistence.
- OAuth, Clerk and Cognito identity boundaries.

### Cloud engineering

- Amazon EKS, ECR, Lambda, API Gateway and DynamoDB.
- SQS, EventBridge, Secrets Manager, KMS, IAM and CloudWatch.
- AWS SAM, CloudFormation and Terraform infrastructure as code.
- VPC, subnets, NAT, worker nodes and managed control planes.

### Platform engineering

- Kubernetes operations and troubleshooting.
- Argo CD GitOps and declarative delivery.
- Backstage service catalogue and developer portal.
- CI/CD validation and container publication.
- Approval-gated operational workflows and audit history.

### Observability and operations

- Prometheus metric collection.
- Grafana dashboarding.
- Kubernetes events and pod logs.
- Health endpoints, probes and runtime diagnostics.
- Risk, incident, execution and audit workflows.

### AI and automation

- Deterministic operational rules.
- AWS Bedrock and Amazon Nova Pro analysis.
- n8n workflow automation.
- Serverless scheduling and publishing.
- Human approval before consequential actions.

## Evidence Labels Used Throughout the Handbook

- **Code verified:** confirmed in source or infrastructure files.
- **Repository documented:** described in the repository README.
- **Demonstrated:** supported by screenshots, test output or deployed behaviour.
- **Derived command:** valid command derived directly from committed configuration, such as a `package.json` script.
- **Recommended command:** useful operational command, but not evidence that it was previously executed.
- **Planned:** future work, never represented as already implemented.

## Updating This Register

Whenever a project is added or materially changed:

1. Add or update its row here.
2. Update the [Project Index](projects/README.md).
3. Add verified commands to the [Command Reference](13-Command-Reference/Chapter-13-Commands.md).
4. Connect new technologies in the [Technology-to-Project Evidence Map](TECHNOLOGY-PROJECT-MAP.md).
5. Update the project case study with code evidence, decisions, failures and lessons.
