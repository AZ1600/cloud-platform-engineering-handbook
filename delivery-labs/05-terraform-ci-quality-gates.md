# 05 · Terraform CI security gates versus AWS plan

## Separate non-cloud checks from AWS-backed checks

The [Terraform EKS repository](https://github.com/AZ1600/platform-engineering-terraform-eks) separates:

1. [Terraform CI](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-ci.yml): format, init without backend, validation and native module guardrail tests.
2. [Terraform Security](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-security.yml): TFLint and Trivy configuration scanning.
3. [Manual AWS Plan](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml): confirmed workflow dispatch on `main`, short-lived AWS credentials, remote state and **plan only**.

The third path can contact cloud APIs and incur minor charges if infrastructure/state services exist. It intentionally has no CI `terraform apply` step.

## Read-only/static checks

```bash
# Run in a local Terraform repository clone with Terraform installed.
terraform fmt -check -recursive
# From an isolated module directory, after init -backend=false:
terraform validate
```

### Plan exit codes

A detailed-exitcode Terraform plan returns `0` for no changes, `2` for changes, and `1` for an error. Treating `2` as workflow failure would be incorrect. The plan workflow explicitly handles the exit codes.

## Review questions

- What does `terraform validate` miss that an AWS-backed plan may detect?
- Why must `terraform test` include negative tests for invalid subnets or public EKS exposure?
- Where do S3 backend state and locking configuration live? Who may read them?
- Why should plan artifacts be handled as potentially sensitive?
- Why is CI not automatically authorized to `apply` or `destroy`?

**Evidence:** [EKS module guardrails](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/eks/tests/guardrails.tftest.hcl), [network guardrails](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/network/tests/guardrails.tftest.hcl).

**Interview:** Propose a secured Terraform apply process with review, state protection, scoped credentials, cost visibility and an explicit change window.
