# 02 — Terraform State, Plans and Guardrails

**Goal:** Explain the difference between validating configuration, planning against live AWS state, and modifying infrastructure. Make reviewable changes without confusing `plan` with `apply`.

## Corrected current state

The Terraform EKS repository is **not limited to a future remote-backend design**. Its [dev backend](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/environments/dev/backend.tf) declares an S3 backend, server-side encryption and `use_lockfile = true`; the real bucket is supplied during `terraform init`, including in the plan workflow. The bootstrap directory models supporting state infrastructure. Locking helps serialize competing Terraform operations; it does not replace state access control, backup/versioning, or the need to review drift.

```hcl
terraform {
  backend "s3" {
    key          = "eks/dev/terraform.tfstate"
    region       = "eu-west-2"
    encrypt      = true
    use_lockfile = true
  }
}
```

[Source: dev backend](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/environments/dev/backend.tf). Never paste a backend bucket name or state content into a public report without checking sensitivity.

## Four kinds of evidence

| Evidence | What it demonstrates | What it does **not** prove |
|---|---|---|
| `terraform fmt -check` | Canonical formatting | Valid AWS permissions or safety |
| `terraform validate` | Terraform syntax and internal consistency | Cloud resources exist |
| `terraform test` | Assertions, including mocked provider paths | Real network or runtime behavior |
| Cloud-backed `terraform plan` | Proposed changes from current state, permissions and provider observations | Changes have been applied |

The [native network guardrail tests](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/network/tests/guardrails.tftest.hcl) reject invalid CIDRs, duplicate AZs and subnet mismatches. [EKS guardrail tests](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/eks/tests/guardrails.tftest.hcl) reject unrestricted public API ranges, invalid node counts and unsupported log types.

## Reproducible *non-deploying* workflow

From a local clone of the Terraform project, with Terraform installed and a clear test environment:

```bash
terraform -chdir=modules/network fmt -check
terraform -chdir=modules/eks fmt -check
# Provider/module downloads may require Internet access.
terraform -chdir=modules/network init -backend=false
terraform -chdir=modules/network test
terraform -chdir=modules/eks init -backend=false
terraform -chdir=modules/eks test
```

Do not run `apply`, `destroy`, or a cloud-backed `plan` until costs, access and state have been reviewed. `terraform test` can perform real operations if its test setup is not mocked: read the actual `.tftest.hcl` before execution. The project's listed guardrail tests mock providers and override module outputs, but that does not generalize to every Terraform test.

## Plan-only GitHub OIDC

The [AWS plan workflow](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml) is a manually dispatched `main`-branch job with an explicit confirmation input and `id-token: write`. It assumes a GitHub OIDC IAM role, initializes S3 state, executes `terraform plan -detailed-exitcode`, displays the plan and removes the local saved plan. **No `terraform apply` is in that workflow.** OIDC avoids static cloud keys, but the role's trust conditions and permissions still require review.

## Failure lab — locked or unexpected state

**Scenario A — lock held:** A concurrent state operation prevents plan access. Stop and find the owner of the active operation. Never automatically use `force-unlock` because doing so during a legitimate apply can corrupt state.

**Scenario B — replacement (`-/+`) appears:** Inspect dependency graph, sensitive assets, availability impact and state drift. Avoid applying a surprise replacement; escalate to change review.

**Scenario C — apparently clean plan:** Ask whether the relevant resources are actually managed by this state, and whether the correct backend, workspace, account and Region were selected.

**Interview prompt:** Why is a plan-only pipeline meaningfully safer than automatic apply, yet still able to expose sensitive information through logs or saved plan files?

Next: [AWS identity boundaries](03-aws-identity-boundaries.md).
