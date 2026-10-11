# 04 — Grafana as an investigation interface

## Objective

Move from symptom to evidence by selecting the correct data source and timeframe. Dashboards are useful when they answer a question; they are not proof that instrumentation is complete.

## Provisioned artifacts

The observability project provisions [RED dashboard JSON](https://github.com/AZ1600/platform-engineering-observability/blob/main/grafana/dashboards/demo-api-red.json), [SLO dashboard JSON](https://github.com/AZ1600/platform-engineering-observability/blob/main/grafana/dashboards/demo-api-slo.json), and data sources for Prometheus, Loki and Tempo. Its Compose config mounts a **Grafana persistent volume**, correcting the outdated earlier handbook claim that changes would always be lost on container recreation.

## Investigation route

```text
1. Define impacted service, tenant/environment, symptom and timeframe
2. RED dashboard: traffic, errors, duration
3. Prometheus target and rule state: is telemetry valid?
4. Loki: filter relevant service and severity for the same timeframe
5. Tempo: follow correlated trace ID to the slow/failing span
6. Check Kubernetes events/deployments or recent changes as appropriate
7. State verified facts separately from hypotheses
```

Useful read-only API checks for local Compose:

```bash
curl -fsS http://127.0.0.1:3000/api/health | python3 -m json.tool
curl -fsS http://127.0.0.1:9090/-/ready
```

Grafana health alone does not mean the Prometheus, Loki and Tempo data sources are correctly configured. Inspect panel query errors and source permissions separately.

## Dashboard hygiene checklist

- Show unit, aggregation, time window and datasource.
- Include request volume alongside percentiles and error percentages.
- Identify missing data distinctly from zero, particularly for idle services.
- Avoid exposing secrets in dashboard URLs or public annotations.
- Link the alert's service, environment and runbook to its dashboard.
- Review the dashboard JSON as code and capture before/after changes.

## Scenario

An error-rate panel spikes. The corresponding logs are empty. Is it a monitoring outage? Possible explanations include a different query selector, wrong time range, or a broken log pipeline. Check metrics and Collector independently before drawing conclusions.

**Evidence:** screenshot alone can document a moment; a reproducible query, time window and a matching source revision provide a stronger chain.

Next: [SLOs](05-slo-error-budgets.md).
