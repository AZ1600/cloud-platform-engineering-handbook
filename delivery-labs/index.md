# CI/CD, GitOps & DevSecOps — Engineering Field Guide

> **Phase 4 · Source-reviewed 11 October 2026.** These lessons analyse repository code and configuration, not the present state of cloud infrastructure. Start with read-only and local validation. Never deploy or push to an external registry without reviewing permissions and costs.

## Learning objectives

By the end, explain the difference between building, publishing, deploying and verifying an artifact; map GitHub workflow permissions onto AWS OIDC; distinguish an SBOM from an attestation; diagnose image and GitOps sync failures; and describe a safe release/rollback plan.

| Lesson | Focus | Anchoring repository |
| --- | --- | --- |
| [01 · Delivery boundaries](01-delivery-boundaries.md) | CI, delivery, deployment and evidence | [CI/CD Pipeline](https://github.com/AZ1600/platform-engineering-cicd-pipeline) |
| [02 · GitHub OIDC & identity](02-github-oidc-security.md) | Trust policies and least-privilege jobs | [Terraform EKS](https://github.com/AZ1600/platform-engineering-terraform-eks) |
| [03 · Hardened containers](03-container-security.md) | Image pinning and runtime defence | [CI/CD Pipeline](https://github.com/AZ1600/platform-engineering-cicd-pipeline) |
| [04 · SBOM & attestations](04-sbom-attestations.md) | Supply-chain evidence and provenance | [CI/CD Pipeline](https://github.com/AZ1600/platform-engineering-cicd-pipeline) |
| [05 · Infrastructure quality gates](05-terraform-ci-quality-gates.md) | Terraform validation, tests, scanning, plans | [Terraform EKS](https://github.com/AZ1600/platform-engineering-terraform-eks) |
| [06 · Argo CD reconciliation](06-argocd-gitops.md) | Desired state, sync, drift and prune | [GitOps Argo CD](https://github.com/AZ1600/platform-engineering-gitops-argocd) |
| [07 · EKS release engineering](07-eks-release-verification.md) | Artifact digest, rollout, health, rollback | [Pharmacy API EKS](https://github.com/AZ1600/pharmacy-api-eks) |
| [08 · Incident troubleshooting](08-failed-pipeline-runbooks.md) | Failed builds, access, scans, syncing | Multiple repositories |
| [09 · Connected architecture](09-end-to-end-delivery.md) | Evidence trail, trust boundaries and handoffs | Multiple repositories |
| [10 · Review exercises](10-interview-exercises.md) | Interview and design practice | Multiple repositories |

## Evidence standard

- **Implemented in source:** a concrete workflow or manifest can be inspected.
- **Documented or previously demonstrated:** the README/screenshots say an action occurred; not proof of current uptime.
- **Proposed improvement:** a recommendation, not an existing capability.

See the [Engineering Evidence Guide](../projects/Engineering-Evidence-Guide.md), [Chapter 8](../08-CICD/Chapter-08-CICD.md) and [Phase 3 cloud labs](../cloud-labs/index.md).

::: warning Safe lab operating model
Prefer inspecting checked-in workflow files and running non-destructive local checks. Commands that assume AWS, EKS or Argo CD access are diagnostic examples only. Require an authorized context and explicit review before any write, push, sync, rollback, apply or prune.
:::
