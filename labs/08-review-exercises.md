# 08 — Exercises, code-review prompts and interview answers

Use this page as a self-assessment. Do not memorise only tool names: connect a user problem to a specific implementation, failure scenario, verification command and trade-off.

## Practical review rubric

Score each scenario from **0 to 3**:

- **0** — Cannot explain the system or its trust boundary.
- **1** — Names services and commands but provides little causal reasoning.
- **2** — Explains the flow, evidence and one relevant failure mode.
- **3** — Explains design alternatives, negative tests, operational recovery and remaining limitations.

| Topic | Question | Source starting point |
|---|---|---|
| Deployments | Why can two running Pods yield zero Service endpoints? | [Pharmacy Deployment](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml) |
| Rollout | What is the difference between desired, ready and available replicas? | [Kubernetes control loops](01-kubernetes-control-loops.md) |
| RBAC | Why do app roles and Kubernetes roles differ? | [PlatformPilot security](https://github.com/AZ1600/platform-pilot/blob/main/backend/core/security.py) |
| Fail-closed | Why return 503 when auth has no configured tokens? | [PlatformPilot RBAC tests](https://github.com/AZ1600/platform-pilot/blob/main/backend/tests/test_rbac_routes.py) |
| Golden path | What does a generated service *not* prove? | [Backstage template](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/template.yaml) |
| Portal governance | Is the Backstage policy default deny? | [Permission policy](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/packages/backend/src/extensions/permissionPolicy.ts) |
| NetworkPolicy | Does an ingress-only policy restrict egress? | [Generated policy](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/content/kubernetes/networkpolicy.yaml) |
| Operational evidence | Can a trace confidence be treated as calibrated probability? | [Decision Trace](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/decision-trace.ts) |
| Approval | Which negative test proves early execution is blocked? | [Approval gate](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) |
| Integration | How would you prove each system boundary works? | [Scenario](07-integrated-scenario.md) |

## Worked answer: “what happens when a Pod is unhealthy?”

1. Clarify whether “unhealthy” means not scheduled, not running, not ready, restarting or serving incorrect responses.
2. Read Deployment/Pod state, events and logs in an authorised namespace.
3. Correlate with a release and with metrics; compare competing hypotheses.
4. Check Service endpoints separately from Pod status.
5. Verify cause, blast radius and rollback before changes; document the result.

The answer should *not* open with “restart the Pod”. Restarts may hide evidence and reintroduce the same configuration error.

## Worked answer: “why use Backstage?”

A portal addresses discovery and self-service. The value comes from consistent ownership, tested templates, secure delivery, observable services and supported exception paths. Compare the actual template, generated deployment and permission policy to avoid overstating maturity.

## Worked answer: “what controls AI-assisted remediation?”

The observer submits structured evidence; the receiver authenticates and validates the finding, constructs a reviewable record and enforces approval as a server-side state transition. The output of analysis is **not** an execution credential. See [CloudOps](06-cloudops-approval.md).

## Evidence-driven capstone

Choose one of the three reference repos. Produce a one-page note containing:

- **System map:** caller, server, storage, platform API and trust boundaries.
- **One success path:** exact source file or tests supporting it.
- **One denied path:** expected HTTP status or policy decision and the test that proves it.
- **One failure path:** symptoms, read-only investigation and remediation prerequisites.
- **Two production gaps:** explain the missing evidence or configuration, not just a wishlist.
- **What is unverified:** environment status, current CI health and integration depth.

Attach source hyperlinks, not private logs or secret values. If you have not run a test or deployment, say **“test present in repository”** or **“deployment documented”**, not **“verified live”**.

## Next studies

Continue with [Observability](/09-Observability/Chapter-09-Observability), [Terraform](/07-Terraform/Chapter-07-Terraform), [CI/CD](/08-CICD/Chapter-08-CICD), and the [engineering evidence guide](/projects/Engineering-Evidence-Guide).
