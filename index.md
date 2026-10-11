---
layout: home
hero:
  name: "Cloud & Platform Engineering Handbook"
  text: "Understand it. Build it. Prove it."
  tagline: "A living field guide to AWS, Azure, Kubernetes, delivery, reliability and AI operations, grounded in source code, tests and deployment artifacts."
  actions:
    - theme: brand
      text: Browse case studies
      link: /projects/
    - theme: alt
      text: Start learning
      link: /01-Cloud-Fundamentals/Chapter-01-Cloud-Computing
    - theme: alt
      text: Evidence standards
      link: /projects/Engineering-Evidence-Guide
features:
  - icon: "🧭"
    title: Four connected flagship systems
    details: PlatformPilot, CloudOps, OpsPilot SaaS and PropertyOps illustrate different layers of cloud and platform engineering.
    link: /projects/
  - icon: "🔐"
    title: Security by design
    details: Learn IAM, application RBAC, workload identity, private networking and approval boundaries from project artifacts.
    link: /projects/Engineering-Evidence-Guide
  - icon: "⚙️"
    title: Reproducible infrastructure
    details: AWS Terraform, Azure Bicep, Kubernetes manifests, delivery pipelines and testing practices.
    link: /07-Terraform/Chapter-07-Terraform
  - icon: "📈"
    title: Build systems you can operate
    details: Follow metrics, traces, SLOs, evidence handling and incident investigation.
    link: /09-Observability/Chapter-09-Observability
  - icon: "🤖"
    title: Grounded AI operations
    details: Study retrieval, orchestration, RAG evaluations and human-in-the-loop action workflows.
    link: /projects/RAG-Ops-Assistant
  - icon: "📚"
    title: Learn and explain
    details: Topic chapters, a command reference and engineering interview preparation.
    link: /12-Interview-Preparation/Chapter-12-Interview-Preparation
---

## What changed in this edition

The project index has been refreshed against public repository structures and READMEs inspected on **11 October 2026**, including new Azure, AI and infrastructure projects. Previous chapters remain available as learning resources and may contain older dated observations; always inspect linked source for the current implementation.

## Choose a learning path

**Platform engineer:** [PlatformPilot](/projects/PlatformPilot) → [CloudOps Command Center](/projects/CloudOps-Command-Center) → [Backstage](/projects/Backstage-Developer-Portal) → [Observability](/projects/Observability-Platform).

**Cloud engineer:** [Terraform EKS](/projects/Terraform-AWS-EKS-Platform) → [Pharmacy EKS](/projects/Pharmacy-API-EKS) → [PropertyOps on Azure](/projects/PropertyOps-Azure) → [AZ-104 Lab](/projects/AZ104-Azure-Infrastructure).

**AI operations engineer:** [RAG Ops Assistant](/projects/RAG-Ops-Assistant) → [CloudOps](/projects/CloudOps-Command-Center) → [OpsPilot SaaS](/projects/OpsPilot-SaaS).

> **Evidence convention:** repository contents demonstrate implemented artifacts, screenshots document specific runs, and live uptime, customer usage, security certification or ongoing cloud deployment are *not* assumed.

<!-- phase2-kubernetes-platform-start -->
## Hands-on Kubernetes & Platform Engineering

Follow the new [Kubernetes and Platform Engineering field guide](/labs/) to investigate workloads, inspect access boundaries and understand how PlatformPilot, Backstage and CloudOps fit together. Includes source-linked security reviews, incident runbooks and a capstone scenario. The existing learning chapters remain available.

<!-- phase3-aws-azure-depth -->
## New: AWS and Azure infrastructure deep dives

The [Phase 3 field guide](/cloud-labs/) develops cloud engineering workflows through Terraform EKS, Pharmacy API, AZ-104 and PropertyOps. Follow read-only diagnostics, identity and networking boundaries, configuration review and interview scenarios.

<!-- phase4-cicd-gitops-devsecops -->
## New: CI/CD, GitOps and DevSecOps deep dives

Explore the [Phase 4 delivery field guide](/delivery-labs/) for source-linked security gates, AWS OIDC, SBOM and provenance, local Argo CD reconciliation, immutable EKS deployment, incident runbooks and technical review exercises.

<!-- phase5-observability-sre -->
## New: Observability, SRE and incident response deep dives

Follow the [Phase 5 SRE field guide](/sre-labs/) for source-linked Prometheus queries, OpenTelemetry traces, Loki logs, Tempo investigation, error budgets, alert testing, PlatformPilot failure boundaries and approval-gated CloudOps incident workflows. Local demos are not represented as production availability evidence.

<!-- phase6-ai-ops-rag -->
## New: AI Operations and RAG Engineering deep dives

Explore the [Phase 6 AI/RAG field guide](/ai-labs/) for evidence-grounded retrieval, source citations, LangGraph/MCP routing, Bedrock identity, evaluation, prompt-injection boundaries and approval-safe automation.

<!-- phase7-architecture-system-design -->
## New: Architecture and system design deep dives

Use the [Phase 7 architecture field guide](/architecture-labs/) to move from requirements and trust-boundary diagrams to data consistency, failure recovery, multi-tenant SaaS, developer platforms, safe AI automation and architecture decision records. Examples cite real source; cross-project integrations are labelled proposed.
