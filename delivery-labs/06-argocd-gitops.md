# 06 · Argo CD reconciliation, drift and guarded sync

## What the repository actually demonstrates

[GitOps with Argo CD](https://github.com/AZ1600/platform-engineering-gitops-argocd) is documented using a **local Docker Desktop Kubernetes cluster**. It is an instructional model that could later be adapted to EKS; do not describe it as presently deployed on EKS.

```text
Pull request -> YAML/schema validation -> approved main branch
                                          |
                                     Argo CD watches Git
                                          |
                               desired vs live comparison
                                          |
                                  sync and health state
```

[Workflow validation](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/.github/workflows/validate-manifests.yaml) runs Yamllint and Kubeconform (including Argo CRD schemas). [Application](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/argocd/application.yaml) enables automated sync, `prune`, `selfHeal` and `CreateNamespace`. [AppProject](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/argocd/project.yaml) constrains destination, source and resource kinds.

## Safe observation commands

```bash
# Requires an authorized local cluster with Argo CD already installed.
kubectl -n argocd get applications
kubectl -n nginx get deployment,service,pods
kubectl -n nginx describe deployment nginx
```

These are read-only inspection commands. Do **not** run `kubectl delete`, `argocd app sync --prune` or direct manifest changes against a shared cluster during this exercise.

## Understanding drift

If someone manually changes the live replica count, Argo CD can detect and (with self-heal enabled) reconcile back to Git. That is desirable for intended policy, but it also means emergency manual changes may be reverted. Incident responders should coordinate temporary overrides and document them in Git.

## Review exercise

What happens if a mistaken deletion lands on `main` with pruning enabled? Identify required PR review, schema checks, project boundaries, observability, backup strategy and change recovery. Sync status `Synced` is not a guarantee that application-level tests passed.

**Interview:** Compare GitOps reconciliation with Terraform's plan/apply and with an imperative `kubectl apply`.
