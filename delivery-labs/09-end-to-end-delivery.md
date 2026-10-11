# 09 · One platform, multiple delivery contracts

The projects provide **separate implemented examples**, not a verified single end-to-end production system. This reference architecture shows how they *could* integrate.

```text
Developer PR
  -> GitHub Actions unit/lint/schema/IaC checks
  -> image build + vulnerability scan
  -> immutable registry digest + SBOM + attestations
  -> reviewed desired-state update in deployment repository
  -> Argo CD compares Git to live Kubernetes
  -> cluster rollout + readiness/smoke checks
  -> observability and evidence archive
```

## Four boundaries to defend

1. **Change authorization:** branch protections/reviews and who may dispatch publishing/deployment jobs.
2. **Credential scope:** GitHub OIDC role trust and permissions; EKS access; Kubernetes RBAC.
3. **Artifact integrity:** bind SBOM/provenance to a digest; release and deploy that digest.
4. **Runtime trust:** namespace, network policy, workload identity, approval, observability and rollback.

## Evidence matrix

| Claim | Suggested evidence |
| --- | --- |
| Checks ran | Workflow run ID and commit hash |
| Image published | ECR digest and timestamp |
| Artifact attested | Signed subject digest and verification result |
| GitOps accepted configuration | Argo sync revision and resource diff |
| Runtime healthy | Readiness, error/latency signals and smoke test |
| Recovery possible | Documented rollback/rollforward drill |

## Architecture exercise

Design how [CI/CD](https://github.com/AZ1600/platform-engineering-cicd-pipeline), [GitOps](https://github.com/AZ1600/platform-engineering-gitops-argocd), [Terraform EKS](https://github.com/AZ1600/platform-engineering-terraform-eks) and [Pharmacy EKS](https://github.com/AZ1600/pharmacy-api-eks) would cooperate. Explicitly mark which integration needs implementing. Keep infrastructure and application deploy credentials separate.

**Trade-off:** Separate repositories strengthen review boundaries but require reliable artifact promotion and revision traceability. A monorepo simplifies shared changes but broadens CI blast radius.
