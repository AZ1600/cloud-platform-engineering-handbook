# 02 · GitHub Actions OIDC and least privilege

## The identity path

```text
GitHub runner -> OIDC token with repository/ref claims
              -> AWS IAM role trust policy
              -> STS temporary credentials
              -> scoped ECR / Terraform / EKS operations
```

**Verified examples:** [CI/CD ECR publishing workflow](https://github.com/AZ1600/platform-engineering-cicd-pipeline/blob/main/.github/workflows/ci.yml), [Terraform plan workflow](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml) and [Pharmacy deployment workflow](https://github.com/AZ1600/pharmacy-api-eks/blob/main/.github/workflows/deploy.yml).

## Review what must be true

1. Workflow permissions include only what is necessary; `id-token: write` permits requesting an identity token, **not** arbitrary AWS access.
2. The AWS role trust policy narrows the OIDC issuer, intended audience and `sub` conditions (repository and branch/environment).
3. Role permission policies scope ECR, Terraform plan or EKS deployment operations appropriately.
4. Job-level conditions prevent inappropriate triggers. Protected environments/required reviewers belong in repository configuration and need separate verification.
5. The runner identity and target AWS account are checked; no long-lived AWS access keys are required.

::: tip Critical distinction
OIDC establishes *who the workflow is*. IAM trust controls *who may assume a role*. IAM permission policies define *what the assumed role may do*. Kubernetes RBAC still governs cluster operations after AWS authentication.
:::

## Safe code review

```bash
# In a local repository clone — read only.
grep -R -n 'id-token: write\|role-to-assume\|allowed-account-ids' .github/workflows
```

### Failure matrix

| Symptom | Investigate |
| --- | --- |
| `AccessDenied` on assume role | Subject/audience trust constraints and workflow ref |
| AWS role assumed but ECR denied | IAM policy and repository ARN scope |
| AWS role assumed but kubectl forbidden | EKS access mapping and Kubernetes RBAC |
| Wrong target account | Account ID verification and runner environment |

Do not broaden trust to all repositories or remove review gates to make a failing workflow pass.

**Interview:** Compare a GitHub OIDC role with a Kubernetes ServiceAccount and EKS Pod Identity. These are different authentication paths and authorization surfaces.
