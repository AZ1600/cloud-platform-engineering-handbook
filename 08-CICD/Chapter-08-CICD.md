# Chapter 8 — CI/CD and GitOps Through My Projects

> CI proves that a change is buildable and testable. Delivery moves a verified artifact toward an environment. GitOps reconciles environment state from version control.

## 1. The Problem

Manual build and deployment steps are inconsistent, difficult to audit and easy to forget. Automation creates a repeatable path from change to evidence to release.

```text
Code change -> validation -> build -> immutable artifact
            -> approval -> deployment -> verification -> rollback if needed
```

## 2. CI, Delivery and Deployment

- **Continuous Integration:** frequently combine changes and run automated validation.
- **Continuous Delivery:** keep a verified release ready for controlled deployment.
- **Continuous Deployment:** automatically release every qualifying change.

Pushing an image to ECR is artifact publication, not proof that an application was deployed successfully.

## 3. My CI/CD Evidence

| Project | Pipeline evidence |
|---|---|
| CI/CD Pipeline | GitHub Actions builds a Docker image and pushes it to ECR |
| CloudOps | lint, typecheck, Vitest and Next.js build |
| OpsPilot | config check, tests, lint, typecheck and build |
| Cloud-Native Pharmacy | CodeBuild runs a unit test, SAM build and SAM deploy |
| Argo CD GitOps | Git manifests reconcile to EKS |
| PlatformPilot | frontend lint/build scripts; full CI remains an improvement |

## 4. GitHub Actions Concepts

- **Workflow:** YAML automation definition.
- **Event:** trigger such as push, pull request or manual dispatch.
- **Job:** group of steps running on a runner.
- **Step:** command or reusable action.
- **Runner:** machine executing the job.
- **Artifact:** retained output such as build results or test reports.
- **Environment:** protected deployment target with secrets and approvals.

## 5. Quality Gates

CloudOps verifies:

```bash
npm run lint
npm run typecheck
npm run test
npm run build
```

Each finds a different problem. Linting checks rules and maintainability; type checking detects invalid assumptions; tests validate behaviour; build confirms production compilation.

OpsPilot adds `npm run check:config`, recognising that correct code can still fail with invalid runtime configuration.

## 6. Container Pipeline

The CI/CD project demonstrates:

```text
Git push -> GitHub Actions -> AWS authentication -> ECR login
         -> Docker build -> image tag -> ECR push
```

Production improvements:

- use GitHub OIDC and a short-lived AWS role;
- test and scan before publication;
- tag with commit SHA or semantic version;
- produce provenance/SBOM where required;
- deploy the exact digest;
- protect production environments.

## 7. Secrets and OIDC

Long-lived AWS access keys in repository secrets can leak and require rotation. OIDC lets GitHub exchange a signed workflow identity for temporary AWS credentials under a role trust policy.

The role should restrict repository, branch/environment and required AWS actions.

## 8. Build Once, Promote the Same Artifact

Rebuilding separately for each environment can produce different content. A stronger model builds once, records the digest, then promotes the same artifact through environments with different configuration.

```text
commit -> image digest abc123 -> development -> staging -> production
```

## 9. GitOps with Argo CD

My Argo CD project stores Kubernetes desired state in GitHub.

```text
Manifest commit -> Argo CD comparison -> OutOfSync
                -> sync -> EKS resources -> health status
```

Key concepts are desired state, live state, drift, sync, health, prune and self-heal. Automatic sync increases speed but also increases the importance of review, policy checks and safe rollback.

## 10. CI and GitOps Together

```text
Application repository
  -> CI tests/builds/scans image
  -> publishes immutable ECR digest
  -> updates deployment repository
  -> Argo CD reconciles EKS
```

CI creates verified artifacts. GitOps controls environment state. Separating them improves auditability.

## 11. Database Changes

CloudOps and OpsPilot include schema commands. Database migrations need sequencing, backup, compatibility and rollback planning.

Prefer backward-compatible changes:

1. add new structure;
2. deploy code supporting old and new;
3. migrate data;
4. remove old structure later.

## 12. Deployment Strategies

- **Rolling:** gradually replace replicas.
- **Blue/green:** switch traffic between complete environments.
- **Canary:** expose a small percentage to the new version.
- **Recreate:** stop old before starting new; simplest but causes downtime.

The correct strategy depends on state, traffic, compatibility, observability and rollback speed.

## 13. Verification and Rollback

A successful pipeline only means its commands succeeded. Deployment verification should include rollout status, readiness, errors, latency and a critical user workflow.

Rollback must cover application, configuration, infrastructure and database compatibility—not only image version.

## 14. Failure Diagnosis

- Install failure: lockfile/runtime mismatch or unavailable registry.
- Test failure: behaviour regression or unstable test.
- Build failure: type, bundling or environment assumption.
- Authentication failure: trust policy, token or permission.
- Image push failure: ECR login, name/tag or network.
- GitOps failure: invalid manifest, target access, unhealthy resource or sync policy.

Read the first meaningful error and identify which boundary failed before rerunning.

## 15. Interview Explanation

> My delivery work covers two connected paths. GitHub Actions validates applications and builds/publishes images to ECR. Argo CD then treats Git manifests as Kubernetes desired state and reconciles them to EKS. I distinguish CI evidence, artifact publication and actual deployment. My production improvements are OIDC credentials, immutable digests, security scans, protected environments, deployment verification and tested rollback.

## 16. Mastery Checklist

- [ ] I can distinguish CI, delivery and deployment.
- [ ] I can explain every validation gate in CloudOps and OpsPilot.
- [ ] I can trace source to ECR digest to EKS pod.
- [ ] I can explain OIDC versus stored AWS keys.
- [ ] I can explain GitOps desired/live state and drift.
- [ ] I can describe rolling, blue/green and canary trade-offs.
- [ ] I can explain safe database change sequencing.
- [ ] I can define verification and rollback evidence.

## Related Material

- [CI/CD Project](../projects/CI-CD-Pipeline.md)
- [GitOps Project](../projects/GitOps-ArgoCD.md)
- [Command Reference](../13-Command-Reference/Chapter-13-Commands.md)
