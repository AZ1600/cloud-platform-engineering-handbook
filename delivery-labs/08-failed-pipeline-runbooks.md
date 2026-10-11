# 08 · Diagnostic runbooks for failed delivery

> These are **triage templates**, not instructions to override approvals or weaken controls. Capture timestamps, run IDs, commit hashes and redacted error messages; do not print tokens, secrets or unredacted plan files into tickets.

## Scenario A: CI green, ECR publish denied

1. Confirm the publishing workflow was actually invoked (`workflow_dispatch` rather than PR checks).
2. Record branch/ref, AWS account (if already logged), job permission and assumed role name.
3. Compare AWS trust-policy subject with the workflow context; check ECR repository-scope permissions.
4. If the trust/permission contract is wrong, prepare a least-privilege change for review. Do not use static credentials as an emergency bypass.

## Scenario B: Trivy blocks a release

1. Record image digest, scanner DB date, vulnerability IDs and fix availability.
2. Determine whether a fixed base image/dependency exists.
3. Rebuild and rerun tests/scans with a reviewed image update.
4. If an exception is necessary, use a time-bound recorded approval rather than disabling the security gate.

## Scenario C: Argo CD shows `OutOfSync`

1. Verify desired revision and destination application/namespace.
2. Inspect live-vs-desired diff and AppProject resource scope.
3. Classify drift: intended change, manual mutation or incomplete sync.
4. Review impact of prune/self-heal before any corrective sync.

## Scenario D: `rollout status` times out

```bash
# Authorized read-only investigation.
kubectl get pods -n default -o wide
kubectl describe deployment pharmacy-api -n default
kubectl get events -n default --sort-by=.metadata.creationTimestamp
```

Investigate image pulls, probes, capacity, scheduling, DNS and dependencies. Avoid treating a longer timeout as a fix.

## Incident record template

| Field | Capture |
| --- | --- |
| Change | Commit, workflow run, digest, target environment |
| Symptom | What failed and when |
| Blast radius | Affected service, tenants or namespaces |
| Evidence | Redacted logs, manifests, metrics and events |
| Hypothesis | What might explain the symptoms |
| Action | Approved change, owner and rollback plan |
| Result | Validation after remediation |

[Next: combine these into an end-to-end delivery story](09-end-to-end-delivery.md).
