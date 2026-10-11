# 03 — Kubernetes Troubleshooting Under Interview Pressure

## Scenario: rollout stays unavailable

The interviewer says: "A service deployed yesterday but Pods are not ready. What do you do?" Do **not** start with `kubectl delete pod`.

```bash
# Replace the example namespace and deployment with real values.
kubectl get deployments,pods -n demo
kubectl describe deployment api -n demo
kubectl get events -n demo --sort-by=.lastTimestamp
kubectl describe pod POD_NAME -n demo
kubectl logs POD_NAME -n demo --all-containers --tail=100
kubectl logs POD_NAME -n demo --previous --all-containers --tail=100
```

The commands above are **examples for a cluster where you are authorised to read resources**, not evidence that they were executed against a specific historical incident.

## Decision tree

| Observation | First hypothesis | Evidence to request |
| --- | --- | --- |
| `ImagePullBackOff` | Image name, registry auth or network path | Pod Events, registry tag existence, imagePullSecrets/node identity |
| `CrashLoopBackOff` | Process exits or fails startup/probe | Current and previous logs, restart reason, entrypoint |
| `Pending` | Scheduler cannot place workload | Scheduling Events, requests, taints, volumes |
| Ready 0/2 | Readiness failure, dependency or sidecar issue | Container statuses, probe definitions, endpoints |
| Ingress 5xx | Service selector, endpoints or ingress routing | Service/endpoints, ingress events, upstream logs |

## Source-backed discussion

[PlatformPilot's rules](https://github.com/AZ1600/platform-pilot/blob/main/backend/ai.py) map a small set of Kubernetes statuses into recommendations. They are deterministic, not proof of root cause. The fallback classifies other states as low severity, so **never equate an unrecognised state with health** without checking events and logs.

[Pharmacy EKS](../projects/Pharmacy-API-EKS.md) documents image pull and crash-loop troubleshooting, but its exact historical incident details must be distinguished from general diagnostic steps; see the [Debugging Register](../DEBUGGING-ISSUE-REGISTER.md).

## Follow-up drill

- What is the difference between a Pod phase and container waiting reason?
- Why might a Deployment have two replicas but zero available endpoints?
- How do you verify recovery without destroying useful evidence?
- What must be reviewed before a rollback or remediation?

## Expected 90-second answer

State customer impact and blast radius, identify the failing controller and Pod/container, inspect Events and logs, classify hypothesis, verify without write permissions when possible, coordinate a reversible mitigation, then confirm readiness and user-facing success.
