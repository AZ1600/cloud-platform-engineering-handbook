# 10 · CI/CD, GitOps and DevSecOps review exercises

Use the project source, not memorized cloud-service descriptions. For each answer give the **problem → architecture → trade-off → failure case → evidence**.

## Scenario questions

1. A PR passes lint and unit tests. Is the service deployed? What further evidence would you ask for?
2. GitHub's AWS OIDC role assumption fails on a feature branch, but works on `main`. How do `sub` claims and trust conditions affect diagnosis?
3. An image was scanned on Monday and later developed a HIGH advisory. Why is an earlier pass insufficient?
4. How does a registry digest differ from a tag, and what should provenance attest?
5. An `OutOfSync` Argo CD application self-heals repeatedly while an operator changes live resources. Who owns the desired state and exception process?
6. Terraform CI validation succeeds, but an AWS-backed plan fails due to access or state. Why can both results be true?
7. Why are `terraform plan` and `terraform apply` separated in the EKS infrastructure pipeline?
8. An EKS rollout reports success, but tenants get errors. What application-level checks are missing?
9. What are the security implications of enabling Argo CD `prune` in a multi-team cluster?
10. Compare a static AWS key, GitHub OIDC, EKS Pod Identity and a Kubernetes ServiceAccount.

## Self-review rubric

| Criterion | A strong answer provides |
| --- | --- |
| Accuracy | Source-backed description, no invented deployment |
| Boundaries | Accounts, repos, identities, clusters, namespaces |
| Detection | Logs, statuses, tests, evidence timestamps |
| Prevention | Least privilege and reviewed change controls |
| Recovery | Approved fallback and verification steps |
| Limits | Explicit gaps and safe next improvement |

## Practical submission

Create a one-page architecture decision record (ADR) evaluating **manual ECR publish → GitOps desired-state update**. Include assumptions, alternatives, who can approve, how you verify SBOM/provenance and digest, failure handling, rollback, and evidence that integration really occurred.

Related reading: [Chapter 8](../08-CICD/Chapter-08-CICD.md), [EKS release](07-eks-release-verification.md), [Terraform CI](05-terraform-ci-quality-gates.md).
