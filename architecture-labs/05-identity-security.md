# 05 — Security Architecture and Identity Chains

**Objective:** document each principal, permission, credential lifetime and enforcement layer. “Uses IAM” is not an architecture explanation.

## Identity chains that must not be conflated

```text
CI workflow -> OIDC federation -> temporary cloud role -> registry/plan scope
End user -> identity provider -> application role -> API route permission
Pod -> Kubernetes ServiceAccount -> Kubernetes RBAC -> cluster resources
Workload -> cloud workload identity -> scoped provider API permission
```

These systems solve different problems. The [Terraform EKS project](https://github.com/AZ1600/platform-engineering-terraform-eks) uses GitHub OIDC for a **plan-only** workflow. A plan role should not quietly become a production deploy role. The [PropertyOps project](https://github.com/AZ1600/AI-property-operations) documents Entra ID, managed identities and application roles; those must be evaluated independently of network reachability.

## Boundary checklist

| Decision | Review question |
| --- | --- |
| Authentication | Who is the principal, and how is identity verified? |
| Authorization | Which exact resource/action pair is allowed? |
| Token handling | What is lifetime, audience and revocation story? |
| Secret management | Can a token leak via logs, state, container image or CI output? |
| Network reachability | Does the caller have the required route and DNS resolution? |
| Audit | Can we link one authorized action to an attributable decision? |

**Private Link is not a substitute for authorization.** A private endpoint can help keep traffic on a private network while a compromised authorized principal remains dangerous. Likewise, role checks in a UI do not substitute for checks in the API/database path.

## Abuse-case exercise

An engineer with a `viewer` role attempts to submit a PlatformPilot finding to CloudOps and then requests execution without approval. Identify every independent gate. [PlatformPilot](https://github.com/AZ1600/platform-pilot) checks roles at the API, and [CloudOps approval-gate tests](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) confirm direct execution before approval returns 409 in the test scenario. This does not replace an enterprise threat model, policy review or production penetration test.

## Threat-model template

For each boundary record: asset, actor, entry point, trust assumption, plausible attack, preventative control, detection signal, test and unresolved risk. Cover spoofing, tampering, disclosure, denial of service and privilege escalation. Require an owner for every mitigation.

[Next: Cloud architecture trade-offs](06-cloud-tradeoffs.md)
