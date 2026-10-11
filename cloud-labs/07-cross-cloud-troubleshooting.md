# 07 — AWS and Azure Troubleshooting Scenarios

**Goal:** Investigate a failure without guessing a root cause or changing security controls to make symptoms disappear.

## The six-question investigation template

1. **Scope:** account, subscription, Region, environment, identity, resource and timestamp.
2. **Signal:** exact status code, event, metric or command output; retain sanitized evidence.
3. **Impact:** affected callers, namespaces, tenants, dependency and duration.
4. **Hypotheses:** at least two plausible explanations with discriminating tests.
5. **Verification:** read-only queries first; changes require approval and rollback.
6. **Closure:** correction made, follow-up test, monitoring and remaining uncertainty.

## Scenario A — EKS API unreachable

**Observed:** `kubectl get nodes` times out. Does not prove nodes are down.

Potential hypotheses: wrong kubeconfig context; private-only EKS endpoint reached from outside VPC; VPN/DNS failure; caller IAM access; control-plane availability. Verify current identity and context *before* editing cluster endpoint exposure. If `kubectl` cannot connect at all, distinguish TCP/DNS timeout from a Kubernetes `Forbidden` response—these are different boundaries.

Repository: [Terraform EKS dev settings](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/environments/dev/main.tf).

## Scenario B — Cognito token accepted, wrong tenant's resource requested

**Observed:** Authenticated request produces an application `403`. Check token tenant identity and server-side ownership lookup. Never change role mapping solely to silence a tenant authorization error. An authenticated subject and a valid signing key are necessary but not sufficient for resource access.

Repository: [Pharmacy token security implementation](https://github.com/AZ1600/pharmacy-api-eks/blob/main/app/core/security.py).

## Scenario C — Azure Blob access times out

**Observed:** Azure VM cannot retrieve a blob. Distinguish DNS resolution, routing to Private Endpoint, outbound firewall/NSG, credential acquisition and RBAC. `403` often indicates authentication/authorization or service policy; timeout commonly points to network path, but corroborate with the actual logs.

Repository: [AZ-104 Private Endpoint and DNS](https://github.com/AZ1600/az104-azure-infrastructure-lab/blob/main/modules/storage-private-endpoint.bicep).

## Scenario D — PropertyOps has a private endpoint but still uses a public path

**Observed:** Private resources are present, while the Container App is not connected to the VNet. This is a *topology mismatch*, not necessarily a broken endpoint. Inspect `infra/main.bicep` and `infra/modules/container-environment.bicep` before claiming a private runtime path. A future migration should have a separate change plan, test environment and rollback.

Repository: [PropertyOps Bicep entry point](https://github.com/AZ1600/AI-property-operations/blob/main/infra/main.bicep).

## Evidence worksheet

| Field | Entry to fill in |
|---|---|
| Source revision | Commit SHA + file path |
| Incident time | UTC timestamp |
| Scope | Account/subscription/Region and namespace/resource group |
| Observable symptom | Exact HTTP status/exit code/event without credentials |
| Hypothesis A/B | Alternative causes |
| Read-only test | Command and expected discriminating result |
| Confirmed result | Observation, not assumption |
| Change decision | Owner, approval and rollback |
| Confidence/limitations | What is **not** yet known |

## Exercise

Write a 10-minute incident response narrative for two scenarios above. Explain what data you would not disclose in a public GitHub issue. Then write a prevention measure (test, policy-as-code, monitoring alert, runbook or topology change) for each.

Next: [Cost and lifecycle](08-cost-and-lifecycle.md).
