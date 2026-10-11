# Phase 5 — Observability, SRE & Incident Response

> **Source-inspected 11 October 2026.** These are educational, project-grounded labs, not confirmation of continuous service availability or production readiness. Default commands are read-only; local failure generation is explicitly optional.

## Choose the investigation path

| Lesson | Engineering question | Repo evidence |
| --- | --- | --- |
| [01. Telemetry architecture](01-telemetry-architecture.md) | How do metrics, logs, traces and alerts travel? | Docker Compose and OTel Collector |
| [02. Prometheus and RED](02-prometheus-red.md) | How do I query rates, errors and latency without misleading myself? | Prometheus scrape and application rules |
| [03. Traces and structured logs](03-traces-and-logs.md) | How can I connect a failing request to a trace? | Collector, Loki and Tempo |
| [04. Grafana investigations](04-grafana-investigation.md) | Which dashboard or query answers the incident question? | Provisioned RED and SLO dashboards |
| [05. SLOs and budgets](05-slo-error-budgets.md) | How reliable is the user experience, over what window? | Availability/latency recording rules |
| [06. Alerts and tests](06-alerts-and-rule-tests.md) | Is the alert actionable and has its logic been tested? | promtool fixture and burn-rate rules |
| [07. Incident response](07-incident-triage.md) | How do we mitigate while preserving evidence? | Target-down and API alerts |
| [08. PlatformPilot diagnostics](08-platformpilot-diagnostics.md) | How do auth, Kubernetes and Prometheus failures differ? | FastAPI metrics router and service |
| [09. CloudOps decisions](09-cloudops-operational-evidence.md) | Who can approve action, and what is recorded? | Decision trace and operational telemetry |
| [10. Capstone & review](10-capstone-postmortem.md) | Can I explain an incident end to end? | Cross-project synthesis (proposed exercise) |

## Reference architecture

```text
FastAPI demo-api ---> Prometheus scrape ---> Recording rules and alerts
       |                                          |
       +--> OTLP traces --> OTel Collector --> Tempo         Alertmanager
       |                                          |               |
       +--> JSON logs ---> OTel Collector --> Loki            Slack (optional)
                                                    \\          /
                                                    Grafana queries

PlatformPilot -> Kubernetes API and Prometheus (a separate application)
            -> structured findings (operator role only)
            -> CloudOps ingestion -> verification -> human approval
```

**Separation of systems:** the local observability Compose stack is not a preconfigured data pipeline into PlatformPilot/CloudOps. Lessons compare implemented components, and the capstone proposes how to connect them safely rather than claiming the integration is already deployed.

## Environment and safety

- Read-only query examples assume the local observability Compose stack is **already running**. Do not start cloud resources for this handbook.
- Some examples require `curl`, `python3`, Docker and `promtool`; unavailable tools are optional, not reasons to force deployment.
- The observability stack's Docker Compose references a local Slack webhook secret. Follow its README and never put webhooks in source control.
- Be deliberate when generating `/error` or `/slow` traffic: only do so on the isolated **local demo API**, never an external or production application.
- Confirm repo revision, scrape labels and versions before copying queries.

### Evidence standard

For each exercise record: the question, time window, command/query, expected signal, observed result, decision, limitations, and rollback or cleanup if applicable. Never fabricate an incident result.

Related: [Chapter 9 — Observability](../09-Observability/Chapter-09-Observability.md) · [Engineering Evidence Guide](../projects/Engineering-Evidence-Guide.md) · [Observability repository](https://github.com/AZ1600/platform-engineering-observability).
