# 04 — Terraform, CI/CD and GitOps Interview Scenarios

## Scenario A: `terraform plan` succeeds; production still fails

**Explain:** Plan evaluates declared changes with the available provider and state data. It does not prove app readiness, health of downstream dependencies, valid future credentials or successful rollout.

```text
Source -> fmt/validate -> lint/security checks -> terraform test
       -> AWS OIDC plan-only role -> review plan
       -> separately authorised apply -> runtime verification
```

The [Terraform EKS repository](https://github.com/AZ1600/platform-engineering-terraform-eks) intentionally keeps the automated AWS workflow **plan only**. S3 remote state and locking protect coordinated changes; access to state still requires careful IAM and sensitive-data controls.

**Questions:** How does the backend lock prevent concurrent changes? Why use provider lock files? When is `terraform import` appropriate? What is the safe path for a failed apply? What happens if state and infrastructure drift?

## Scenario B: Argo CD says OutOfSync

The [GitOps Argo CD demo](https://github.com/AZ1600/platform-engineering-gitops-argocd) configures a Git source at `manifests/`, automated sync, pruning and self-healing on a local Kubernetes demonstration. Inspect app status, rendered manifests, the sync target and controller logs before assuming that a manual Kubernetes change is the correct fix.

**Nuance:** Self-healing may revert ad hoc changes; pruning can remove resources. Neither is a substitute for release authorization or tested rollback.

**Evidence:** [Argo CD Application](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/argocd/application.yaml).

## Scenario C: supply chain trust

Distinguish **build artifact integrity** from **deployment authorization**. A signed or attested artifact helps verify provenance; IAM/OIDC and protected environments decide which actor may deploy it. Verification should also cover runtime health and rollback.

See [Phase 4 delivery labs](../delivery-labs/index.md) and the [CI/CD pipeline case study](../projects/CI-CD-Pipeline.md).

## Practice response

Prepare a 3-minute walkthrough that names a commit SHA, an immutable artifact identifier, a human review gate and a post-release health test. Do not claim that the separate learning repositories are deployed together unless demonstrated.
