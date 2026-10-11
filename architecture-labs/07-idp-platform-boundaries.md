# 07 — Internal Developer Platform Architecture

**Objective:** separate *service creation*, *source control*, *delivery control* and *runtime control*. The platform creates a safe path; it should not bypass environment approvals.

## Current source-backed building blocks

The [Backstage scaffolder template](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/template.yaml) takes service name, owner, environment and monitoring inputs. Its `fetch:template`, `publish:github`, `catalog:register` and notification steps outline service creation and catalog enrollment. A successful template run does not establish that the service is production-ready or that deployment was approved.

The [Argo CD example](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/argocd/application.yaml) points to Git manifests, enables self-heal and prune, and binds to an AppProject. It demonstrates reconciliation for an NGINX GitOps demo. It is *not* evidence that the Backstage template automatically installs to the cluster via Argo CD today.

## Proposed integration (not currently one connected pipeline)

```text
Developer -> Backstage -> repository + catalog entry
                                  |
                           GitHub Actions checks
                                  |
                     reviewed manifest/config PR
                                  |
                            Argo CD desired state
                                  |
                          Kubernetes workload
                                  |
               telemetry + owner + incident feedback
```

The template owns the developer experience; CI checks artifacts; GitOps controls runtime reconciliation; Kubernetes controls the actual workload; an approval system controls operations. These are distinct authority layers.

## Governance choices

Define who can create repositories, who can edit production manifests, who can approve changes, and who can disable/override automatic prune. Require immutable image references, provenance and tests where appropriate. Keep an escape path for emergency rollback with recorded ownership and review.

## Exercise

Propose one golden-path service named `orders-api` using a **hypothetical** team `commerce`. Produce an ownership model, repo policy, CI required checks, Argo CD AppProject scope, deployment environment, SLO and deletion/recovery plan. Name two controls that a malicious generated template must not override.

[Next: Multi-tenant SaaS](08-saas-tenant-architecture.md)
