# 10 — Capstone: SRE incident and postmortem

## Scenario (hypothetical)

A service begins returning 5xx errors after a deployment. Prometheus availability and latency signals move outside the team's objective. An operator wants to push a remediation into CloudOps. Your job is to show a safe diagnosis and handoff **without claiming a running integration or making an infrastructure change**.

## Deliverables

1. An architecture sketch: app → telemetry collectors → Grafana, alert rule → Alertmanager, PlatformPilot/Kubernetes diagnostic step, CloudOps governance step.
2. Two read-only queries: request failure rate and one latency/target metric, with labels and time window.
3. One correlation example linking a sanitised structured log to a trace/span.
4. A falsifiable root-cause hypothesis and at least one competing explanation.
5. A safety decision: what action requires owner/human approval and how would it be rolled back?
6. A one-page blameless postmortem and three prioritized follow-up tasks with owners, evidence and target dates.

## Suggested local-only practice

If—and only if—the isolated [observability demo](https://github.com/AZ1600/platform-engineering-observability) is already running and you have permission, compare its normal `/work` endpoint with the intentional `/error` and `/slow` endpoints. They create local telemetry and can trigger local notifications. Do not run them against a remotely hosted instance or production integration.

Read-only source tests provide an alternative when you cannot run Docker:

- [Prometheus synthetic rule tests](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/tests/rules.test.yml)
- [PlatformPilot RBAC tests](https://github.com/AZ1600/platform-pilot/blob/main/backend/tests/test_rbac_routes.py)
- [CloudOps approval gate tests](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts)

## Postmortem template

### Summary and impact

Describe what users could not do. If impact is unknown, explicitly say it is not yet quantified.

### Timeline (UTC)

| Time | Observed fact / evidence link | Decision / actor |
| --- | --- | --- |
| T0 | First documented symptom | Detection |
| T1 | Verified dashboard and logs | Triage |
| T2 | Approved change or safe mitigation | Response |
| T3 | SLI and workflow recover | Verification |

### Technical cause and contributing factors

Separate verified mechanism from assumptions; mention where metrics, logs or traces were missing.

### What went well / what can improve

Comment on notification clarity, owner routing, recovery steps and evidence retention. Keep focus on systems and processes.

### Prevention and follow-up

Each action has owner, priority, acceptance criteria, relevant test and due date. Suggest one alert/rule test and one observability data-quality check.

## Interview review (explain out loud)

1. What does `up=1` prove, and what does it not prove?
2. How do counters, rates and histogram quantiles differ?
3. When does a 99% SLO allow you to pause risky releases?
4. Why can an application pass `/health` while traces are missing?
5. What is the difference between 401/403 and a Prometheus 503?
6. Does an alert or an AI hypothesis authorize remediation?
7. How do you distinguish audit history from operational logs?
8. What is the testable definition of recovery for this user journey?
9. Why should recording-rule test fixtures accompany alert rule changes?
10. Which claims can you verify from these three repos, and which would require live environment evidence?

Finish: [Phase 5 overview](index.md) · [Chapter 9](../09-Observability/Chapter-09-Observability.md).
