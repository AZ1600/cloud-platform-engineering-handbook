# Chapter 9 — Observability Through My Projects

> Observability is the ability to understand a system’s internal condition from the signals it produces. My projects use Prometheus, Grafana, Kubernetes events/logs, health endpoints and audit histories.

## 1. Monitoring and Observability

Monitoring checks known conditions. Observability supports investigation of conditions that were not predicted in advance.

```text
System -> metrics + logs + traces + events
       -> collection/storage -> queries/dashboards/alerts -> investigation/action
```

A dashboard is not an observability strategy by itself.

## 2. My Evidence

- Observability project: a local Docker Compose stack with Prometheus, Grafana, OpenTelemetry Collector, Loki, Tempo, Alertmanager, application instrumentation, SLI/SLO rules and promtool tests.
- PlatformPilot: Kubernetes resources, events, logs, health scores and Prometheus integration documented in the current README.
- Pharmacy API: Kubernetes probes and CloudWatch evidence.
- OpsPilot: runtime health diagnostics.
- CloudOps and OpsPilot: decision/execution audit histories.

## 3. Metrics

Metrics are numeric time series, such as request count, error count, duration or memory use.

A Prometheus series consists of a metric name and labels:

```text
http_requests_total{method="GET",status="200"}
```

Labels make filtering powerful but create cardinality. Never use unbounded values such as request IDs as metric labels.

## 4. Prometheus

Prometheus normally pulls metrics from configured targets at a scrape interval and stores samples locally.

My Compose project mounts `prometheus/prometheus.yml` and exposes port 9090.

Important concepts:

- target and scrape job;
- exporter or application `/metrics` endpoint;
- label and time series;
- PromQL query;
- recording and alert rules;
- retention and storage;
- target health.

## 5. Grafana

Grafana queries data sources and presents panels and dashboards. My project exposes it on port 3000.

A good dashboard answers an operational question. It has units, time range, thresholds and links from summary to detail. Grafana does not create data that Prometheus never collected.

## 6. Logs

Logs record discrete events. PlatformPilot retrieves the last 100 pod log lines; Pharmacy evidence includes application logs.

Useful structured fields include timestamp, level, service, environment, request/correlation ID, event and safe context.

Never log passwords, tokens, full credentials or unnecessary personal data.

## 7. Kubernetes Events

Events describe observations by Kubernetes components: scheduling, image pulls, probes and controller actions. They are temporary diagnostic evidence, not a durable application log store.

PlatformPilot combines status, events and logs, which is stronger than diagnosing from only one signal.

## 8. Traces

Distributed tracing follows request work through spans, parent-child relationships and trace IDs. The current dedicated observability project instruments a demo FastAPI app with OpenTelemetry, exports spans through an OpenTelemetry Collector to Tempo, and links structured Loki logs to traces by trace ID. This is demonstrated locally; it is not proof of tracing across all portfolio services or a production tracing deployment.

Tracing across a multi-service SaaS/API chain would extend the existing local demonstration.

## 9. Health Checks

- **Liveness:** should the process be restarted?
- **Readiness:** should it receive traffic?
- **Dependency health:** which external service is degraded?

PlatformPilot’s `/health` proves the FastAPI process can answer, not that Kubernetes is reachable. Pharmacy uses root-path liveness/readiness probes; dedicated endpoints would make their intent clearer.

## 10. Golden Signals

For user-facing services, begin with:

- latency;
- traffic;
- errors;
- saturation.

For asynchronous work, also measure queue depth, age of oldest message, processing duration, retry count and dead-letter messages.

## 11. SLIs, SLOs and SLAs

- **SLI:** measured reliability indicator.
- **SLO:** target for that indicator.
- **SLA:** external commitment with consequences.

Example: percentage of successful publishing jobs completed within five minutes. An SLO should reflect user experience, not simply CPU usage.

## 12. Alerting

An alert should be actionable and connected to an owner/runbook.

Good alerts indicate user impact or impending exhaustion. Avoid alerting on every transient error. Use duration and grouping to reduce noise.

## 13. Project-Specific Signals

### PlatformPilot

- API request latency/error rate;
- Kubernetes API call failures/latency;
- data freshness and poll count;
- cache hit rate when caching is added.

### Pharmacy API

- request latency/error rate;
- pod restarts/readiness;
- DynamoDB throttles;
- SQS oldest-message age and DLQ count;
- EventBridge failed targets.

### OpsPilot and CloudOps

- ingestion success/failure;
- recommendation and approval counts;
- execution success/failure;
- database latency;
- audit-event completeness.

## 14. Audit History Is Not the Same as Logs

Operational logs help engineers debug. An audit event records who did what to which object, when and with what result. Audit records need integrity, retention and access controls appropriate to accountability.

## 15. Running My Stack

```bash
docker compose up -d
docker compose ps
docker compose logs -f prometheus
docker compose logs -f grafana
```

The current Compose file mounts a named Grafana volume and provisions dashboards and data sources. The lab also includes an Alertmanager secret mount. Check current Compose volume and secret definitions before cleaning up; deleting volumes can still remove persisted local state.

## 16. Investigation Method

```text
Confirm impact -> choose time window -> inspect golden signals
-> correlate deploy/config change -> move from metric to logs/events/traces
-> form and test hypothesis -> mitigate -> preserve evidence -> prevent recurrence
```

Do not restart first and investigate later unless immediate mitigation outweighs evidence loss.

## 17. Interview Explanation

> I built a local Compose observability lab with instrumented FastAPI, Prometheus, Grafana, OpenTelemetry Collector, Loki, Tempo and Alertmanager. It includes SLO/error-budget rules, alert tests, dashboard provisioning and a telemetry smoke test. PlatformPilot separately exposes Kubernetes and Prometheus diagnostics, and CloudOps implements traceable approval decisions. My next challenge is an independently verified multi-service integration and longer-window, user-centered SLOs.

## 18. Mastery Checklist

- [ ] I can distinguish monitoring and observability.
- [ ] I can explain metric names, labels and cardinality.
- [ ] I can explain Prometheus scraping and target health.
- [ ] I can design a Grafana panel around a question.
- [ ] I can distinguish logs, events, traces and audit records.
- [ ] I can define golden signals and an SLO.
- [ ] I can identify useful queue/serverless/Kubernetes alerts.
- [ ] I can conduct an evidence-led investigation.

## Related Material

- [Observability Project](../projects/Observability-Platform.md)
- [PlatformPilot](../projects/PlatformPilot.md)
- [Command Reference](../13-Command-Reference/Chapter-13-Commands.md)

<!-- phase5-observability-sre -->
## 19. Advanced Observability and SRE Field Guide

The [Phase 5 SRE labs](../sre-labs/index.md) contain detailed reviews of the existing Prometheus recording rules, alert tests, OTLP-to-Tempo tracing, structured logs to Loki, Grafana investigations, error-budget math, PlatformPilot error boundaries, CloudOps approval traces and an evidence-led incident capstone. These exercises extend this conceptual chapter without implying always-on production deployment.
