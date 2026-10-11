# 02 — Networking, workload identity and access boundaries

**Goal:** distinguish traffic routing, network policy, API authorization and cloud identity—four controls that do different jobs.

## Trace an incoming request

```text
Client -> DNS -> Ingress/Gateway (when configured) -> Kubernetes Service
       -> EndpointSlice -> ready Pod -> application handler
```

A Service gives a stable virtual destination and selects backends using labels. It does **not** enforce application authorization, guarantee that the destination accepts a connection, or make an application publicly reachable by itself.

**Read-only diagnostic commands:**

```bash
kubectl config current-context
kubectl -n NAMESPACE get svc -o wide
kubectl -n NAMESPACE describe svc SERVICE
kubectl -n NAMESPACE get endpointslices \
  -l kubernetes.io/service-name=SERVICE
kubectl -n NAMESPACE get networkpolicy
```

A missing endpoint may be caused by selector mismatch or readiness; a populated endpoint can still fail because of policy, wrong port, listener errors or external routing configuration.

## Four different security controls

| Boundary | Controls | Does *not* replace |
|---|---|---|
| Kubernetes RBAC | Who may read/change objects through the Kubernetes API | Application-level roles or cloud IAM |
| NetworkPolicy | Which connections are allowed between selected Pods and peers (if CNI enforces it) | TLS, JWT validation or encryption |
| Kubernetes ServiceAccount | Pod-associated identity for Kubernetes API access | AWS IAM permissions by itself |
| AWS Pod Identity / Azure managed identity | Workload access to supported cloud APIs | Kubernetes API RBAC or app authorization |

**Important:** Kubernetes network policies take effect only if the cluster networking implementation supports enforcement. Policies are additive; a policy with ingress-only rules does not automatically restrict egress. A permissive ingress rule that specifies only a port may allow traffic from more sources than intended.

## Real-source inspection: pharmacy workload

The [Pharmacy API Deployment](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml) uses `serviceAccountName: pharmacy-api`, `automountServiceAccountToken: false`, non-root settings and probes. Its [Pod Identity policy/trust files](https://github.com/AZ1600/pharmacy-api-eks/tree/main/iam) illustrate the AWS-side identity boundary.

The manifest alone does not prove the required EKS associations are currently configured. Verify role association, least-privilege permissions and API calls in the environment when performing an actual deployment review.

## Safe RBAC inspection

```bash
kubectl auth can-i get pods -n NAMESPACE
kubectl auth can-i list pods -n NAMESPACE
kubectl -n NAMESPACE get serviceaccounts
kubectl -n NAMESPACE get roles,rolebindings
```

With authorised administrative access you can inspect ClusterRoles/ClusterRoleBindings too, but avoid broad requests for privileged role bindings in shared environments without explicit approval.

### Why “allowed” does not prove end-to-end success

A permitted API read says nothing about whether the API is reachable, whether the workload is healthy, whether the user can access a specific business operation, or whether a token has expired.

## Investigate a `403 Forbidden`

1. Identify **which service** returned `403`: Kubernetes API, PlatformPilot FastAPI, Backstage or cloud provider.
2. Establish identity and subject/role used at that boundary.
3. Inspect only that boundary's policy and logs; don't grant cluster-admin to make an app 403 disappear.
4. Confirm least-privilege remediation using an explicit negative test.

**Related:** [PlatformPilot application RBAC](04-platformpilot-api.md), [Backstage permissions](05-backstage-golden-paths.md), and [CloudOps approval](06-cloudops-approval.md).

## Exercises

- Explain why a Kubernetes `RoleBinding` cannot make a PlatformPilot viewer token into an operator token.
- Compare NetworkPolicy's connectivity enforcement with TLS authentication in one paragraph.
- Identify the possible blast radius when the Backstage server can proxy arbitrary Kubernetes API requests.
