# GitOps with Argo CD

> A declarative continuous-delivery project in which Argo CD synchronises Kubernetes manifests stored in GitHub to Amazon EKS.

**Repository:** <https://github.com/AZ1600/platform-engineering-gitops-argocd>  
**Last verified:** 2026-07-11 against the repository README

## How It Works

```text
GitHub desired state -> Argo CD reconciliation -> Amazon EKS -> application resources
```

Git becomes the declared source of truth. Argo CD compares that desired state with the cluster and reconciles differences. This supports repeatability, visible change history, drift detection, and rollback through version control.

## Verified Scope

- Kubernetes Deployment and Service manifests.
- Argo CD application shown healthy and synchronised.
- Amazon EKS target environment.
- Screenshots demonstrating Argo CD and Kubernetes resources.

## Production Questions

- Is synchronisation automatic or manual?
- Are pruning and self-healing enabled?
- How are secrets kept out of Git?
- What promotion model separates development, staging, and production?
- What policy prevents an unsafe manifest from reaching the cluster?
