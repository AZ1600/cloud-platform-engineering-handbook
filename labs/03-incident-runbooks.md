# 03 — A disciplined Kubernetes incident investigation

**Goal:** produce defensible evidence and safe next actions before making changes.

> **Safety:** Commands in this guide are **read-only** and require an authorised context. Never paste secrets, user data or raw tokens into incident tickets or AI prompts. Do not run fault-injection on production workloads.

## Start with scope, not remediation

Record the time window, affected namespace/service, user-visible symptom, current context and what changed recently. Establish whether this is an availability, latency, security or delivery problem.

```bash
kubectl config current-context
kubectl -n NAMESPACE get deploy,pods,svc -o wide
kubectl -n NAMESPACE get events --sort-by=.metadata.creationTimestamp
kubectl -n NAMESPACE get networkpolicy
```

Ask: is the issue confined to one Pod, workload, node, namespace, cluster or upstream dependency? Don't conflate correlation with cause.

## Runbook A: CrashLoopBackOff

| Observation | Candidate cause | Next check |
|---|---|---|
| Repeated restarts | Process exits | `kubectl logs --previous` for the container |
| Exit 137 / OOMKilled | Memory limit exceeded | `kubectl describe pod`, requests/limits and memory telemetry |
| Startup/liveness failures | Probes too aggressive or app unready | Probe paths, thresholds and startup duration |
| Config or secret missing | Unresolved configuration | Pod events, ConfigMap/Secret references (do not print secret values) |

```bash
kubectl -n NAMESPACE describe pod POD
kubectl -n NAMESPACE logs POD --all-containers --tail=100
kubectl -n NAMESPACE logs POD -c CONTAINER --previous --tail=100
```

`--previous` requires a previous container instance; it won't always exist. Logs can contain sensitive information, so do not automatically publish them.

## Runbook B: Service has no ready endpoints

```bash
kubectl -n NAMESPACE get svc SERVICE -o yaml
kubectl -n NAMESPACE get pods --show-labels
kubectl -n NAMESPACE get endpointslices \
  -l kubernetes.io/service-name=SERVICE -o wide
```

Check label selector matching first; then Pod readiness, endpoint conditions, named target ports, namespace and relevant policies. Avoid restarting Pods when the actual issue is a selector typo.

## Runbook C: ImagePullBackOff

```bash
kubectl -n NAMESPACE describe pod POD
kubectl -n NAMESPACE get pod POD -o jsonpath='{.spec.containers[*].image}'
```

Investigate image reference/digest, registry auth, IAM/ECR pull permissions, network/DNS access, image existence and rate limits. A Pod image status gives a direction, not proof which boundary failed.

## Runbook D: Access denied

Find the `403` emitter (Kubernetes API, PlatformPilot, Backstage, CloudOps). Look at the caller's identity and the policy for that system. Test both an allowed and forbidden operation after a scoped fix. See [identity boundaries](02-networking-and-identity.md).

## Write an incident record

```text
Incident ID / time range:
Context / namespace / service:
Observed symptom and affected users:
Raw evidence (redacted links, commands, timestamps):
Working hypothesis (state uncertainty):
Alternative explanations:
Validation and results:
Blast radius / rollback plan:
Approved action and approver:
After-action follow-up:
```

## Review exercise

A Deployment has `replicas: 2`; `kubectl get pods` shows two Running Pods, yet traffic to its Service times out. Write **three distinct hypotheses** with one observation that would rule each out. Do not propose a Pod restart as a first response.

**Project sources:** [PlatformPilot resource API](https://github.com/AZ1600/platform-pilot/blob/main/backend/app.py) · [Observability repo](https://github.com/AZ1600/platform-engineering-observability) · [Pharmacy Kubernetes manifests](https://github.com/AZ1600/pharmacy-api-eks/tree/main/k8s).
