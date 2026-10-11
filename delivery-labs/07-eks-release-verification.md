# 07 · EKS immutable deployment and verification

## Workflow under review

The [Pharmacy API EKS deployment workflow](https://github.com/AZ1600/pharmacy-api-eks/blob/main/.github/workflows/deploy.yml) requires explicit `workflow_dispatch` confirmation on `main`, authenticates using AWS OIDC, builds and publishes an image, retrieves its **ECR digest**, renders the Kubernetes manifest, applies resources and checks rollout plus `/health` through port-forward.

```text
main + confirmation -> AWS OIDC -> ECR image and digest
                      -> kubectl resource apply -> rollout status
                      -> service port-forward -> /health probe
```

## What can still fail?

- OIDC succeeds, but EKS authentication or Kubernetes RBAC blocks deployment.
- ECR push succeeds, but workload nodes cannot pull the digest.
- Deployment controller creates pods, but probes never pass.
- `/health` passes, but database connectivity or an actual user request fails.
- New configuration is incompatible with a previous version's database schema.

## Non-destructive evidence commands

```bash
# Requires authenticated permission in the intended cluster.
kubectl get deployments -n default
kubectl rollout status deployment/pharmacy-api -n default --timeout=60s
kubectl describe deployment pharmacy-api -n default
kubectl get events -n default --sort-by=.metadata.creationTimestamp
```

Check the active context, namespace and user **before** querying. `rollout status` observes an existing rollout; it does not initiate one.

## Rollback decision table

| Signal | First response |
| --- | --- |
| ImagePullBackOff | Examine image reference and image-pull permissions |
| Readiness fails | Inspect events/logs and dependencies |
| Error rate after rollout | Decide whether to suspend rollout or revert Git/image |
| Migration is destructive | Assess restore/forward-repair plan before any rollback |

`kubectl rollout undo` is a write operation. It is **not** executed in this lab; use only with approval and a documented compatibility plan.

**Interview:** Explain why using an immutable digest is better than deploying a mutable tag, and what else you must verify after the pods turn Ready.
