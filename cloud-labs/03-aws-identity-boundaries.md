# 03 — AWS Identity: CI, Workload and End User

**Goal:** Distinguish three credentials used in one cloud-native system, explain the trust policy at each boundary, and diagnose `403` without granting administrator privileges.

## Separate the principals

```text
GitHub workflow -> OIDC exchange -> AWS deployment role -> ECR/EKS deployment
EKS pod         -> Pod Identity role -> DynamoDB/EventBridge (AWS API)
Human/API caller -> Cognito JWT -> FastAPI tenant + role authorization
```

These are **different identities**. The GitHub role should not be the application's runtime IAM role. A valid AWS role does not substitute for an authenticated end user, and a valid Cognito token does not grant AWS IAM access by itself.

## What the Pharmacy API implements

- [GitHub Actions deploy workflow](https://github.com/AZ1600/pharmacy-api-eks/blob/main/.github/workflows/deploy.yml): manual confirmed job, `id-token: write`, ECR digest deployment and rollout verification.
- [Pod IAM trust and policy files](https://github.com/AZ1600/pharmacy-api-eks/tree/main/iam): describes the EKS Pod Identity trust boundary and required AWS permissions.
- [Kubernetes Deployment](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml): `serviceAccountName: pharmacy-api` with `automountServiceAccountToken: false`, plus hardened container settings. Pod Identity association is AWS-side configuration and is **not proved by the ServiceAccount YAML alone**.
- [FastAPI JWT validation](https://github.com/AZ1600/pharmacy-api-eks/blob/main/app/core/security.py): obtains signing keys from JWKS, checks signature/issuer, enforces client binding and tenant identity, and rejects missing auth configuration.

The older handbook statement that the Pharmacy API *currently mounts static AWS credentials* is outdated relative to the present repository's workload identity architecture. Check actual live associations separately from the code.

## Authentication versus authorization

Authentication asks **who made the request**. Authorization asks **whether this identity can perform the action on this tenant's resource**. Credential transport, verification and authorization must be considered together.

| Symptom | First boundary to investigate |
|---|---|
| GitHub deploy cannot assume role | OIDC provider, role trust conditions, repository/environment claims |
| Pod gets `AccessDeniedException` from DynamoDB | Pod Identity association, workload role policy and table ARN |
| API returns `401` | Bearer header, JWT signature, issuer, client binding, expiration |
| API returns `403` | Tenant identity, resource ownership and permitted application role |
| API returns `503` on protected endpoint | Missing OIDC configuration or failed initialization |

## Diagnostic commands (read-only when context is correct)

```bash
aws sts get-caller-identity
aws eks describe-pod-identity-association \
  --cluster-name YOUR_CLUSTER \
  --association-id YOUR_ASSOCIATION_ID
kubectl -n default get serviceaccount pharmacy-api -o yaml
kubectl -n default describe deployment pharmacy-api
```

The association ID and cluster are examples to be supplied from **your own approved environment**. Cloud identities, ARNs and policy outputs may be sensitive—redact them before publishing.

## Security review

1. Which IAM role can your GitHub repository assume? Is its trust restricted to the expected branch/environment?
2. Does the runtime role permit only the DynamoDB table and EventBridge bus it needs?
3. Does the application check resource-level tenant ownership **after** token validation?
4. What happens when the JWKS endpoint is unavailable or the issuer configuration is empty?
5. Can a stolen deploy credential modify policies or create a new privilege path?

**Exercise:** Write two hypothesis trees for `403`: one for DynamoDB's AWS-side AccessDenied and one for FastAPI's application-side Forbidden. Each tree should prescribe different evidence and a different remediation owner.

Next: [Azure Private Link and DNS](04-azure-private-link-dns.md).
