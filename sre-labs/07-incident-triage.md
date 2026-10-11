# 07 — Incident triage and safe response

## Objective

Build a repeatable response from detection to verified recovery, without confusing monitoring alerts with permission to change production infrastructure.

## Example: Demo API 5xx alert

**Exercise scenario (not a real current incident):** error ratio rises above the local demo threshold. The on-call engineer confirms the affected time window and any recent change, checks both traffic and errors, reads correlated logs/traces, identifies mitigation options, asks for approval where policy requires it, verifies recovery and records an incident timeline.

```text
Alert -> validate freshness/impact -> assess severity/owner
      -> gather RED + logs + traces + deployment context
      -> form hypothesis -> choose reversible mitigation
      -> obtain approval when required -> execute in scope
      -> verify SLI and stability -> record follow-up
```

## Read-only first response

```bash
# Only if the local Compose stack is already running
curl -fsS 'http://127.0.0.1:9090/api/v1/alerts' | python3 -m json.tool
curl -fsSG --data-urlencode 'query=up{job="demo-api"}' \
  'http://127.0.0.1:9090/api/v1/query' | python3 -m json.tool

# For a Kubernetes deployment, use the appropriate context and namespace:
kubectl config current-context
kubectl -n YOUR_NAMESPACE get deployments,pods
kubectl -n YOUR_NAMESPACE get events --sort-by=.lastTimestamp
```

Do not run destructive commands, restart deployments or trigger `/error` on a shared system just because the handbook suggests investigating a failure. If you don't have an environment, review the repository fixtures and design the investigation on paper.

## Triage worksheet

| Time (UTC) | Observation/source | Hypothesis | Decision/owner |
| --- | --- | --- | --- |
| T+0 | Alert name, labels and rule expression | User errors may be elevated | Confirm volume and impact |
| T+5 | Prometheus count/rate and dashboard time range | Regression vs instrumentation issue | Check deployment and logs |
| T+10 | Trace + structured log ID (sanitised) | Particular handler may fail | Reproduce safely, validate cause |
| T+15 | Approved action and blast radius | Reversible mitigation | Execute only in authorized environment |
| T+30 | SLI trend, customer checks and alert resolved | Recovery stable? | Monitor and document |

These times are **illustrative**, not measured performance.

## Operational pitfalls

- Retrying repeatedly can worsen overload; check rate limits and dependency saturation.
- Rolling back code may not roll back a database schema; verify compatibility first.
- A green health endpoint can coexist with failures on a critical workflow.
- An alert resolving is not sufficient proof of customer recovery; verify user journeys.
- Preserve essential logs/events before restarting short-lived workloads where practical.

## Post-incident outputs

Produce an incident summary, factual timeline, contributing conditions, customer impact assessment, what helped/hindered detection, action and approval record, rollback status, prevention work with owners and review date.

Next: [PlatformPilot diagnostics](08-platformpilot-diagnostics.md).
