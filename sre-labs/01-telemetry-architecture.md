# 01 — Trace the telemetry architecture

## Objective

Explain each data path, who owns each component, and what happens when a path fails. Distinguish *source of evidence*, *transport*, *storage*, *visualisation*, and *decision authority*.

## Implemented, source-backed design

In [the observability repository](https://github.com/AZ1600/platform-engineering-observability), the [Compose stack](https://github.com/AZ1600/platform-engineering-observability/blob/main/docker-compose.yml) runs a local demo API, Prometheus, node-exporter, OTel Collector, Loki, Tempo, Grafana and Alertmanager. Its [Prometheus config](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/prometheus.yml) scrapes demo API `/metrics`, node-exporter and itself every 15 seconds.

- **Metrics:** Prometheus pulls counters and histograms from the app and exporters. Alert/recording rules consume those time series.
- **Traces:** the app exports OTLP spans to the Collector; the Collector forwards them to Tempo.
- **Logs:** the app writes structured JSON to a mounted file; the Collector reads it and exports to Loki.
- **Dashboards:** Grafana queries Prometheus/Loki/Tempo; it is not a source of the original telemetry.
- **Notifications:** Prometheus forwards alert state to Alertmanager, which routes selected severities to Slack when configured.

```text
Client -> demo-api --> /metrics ---scrape---> Prometheus
             |                             |           \
             |--> OTLP spans -> Collector --+--> Tempo   alerts -> Alertmanager
             |--> JSON file --> Collector ------> Loki           |
                                             Grafana             Slack
```

Reference: [OTel pipeline](https://github.com/AZ1600/platform-engineering-observability/blob/main/otel/collector.yml), [Alertmanager](https://github.com/AZ1600/platform-engineering-observability/blob/main/alertmanager/alertmanager.yml).

## Read-only diagnostics (when stack is already running)

```bash
# Inspect service health and port bindings
cd /path/to/platform-engineering-observability
docker compose ps

# Read recent logs without modifying services
docker compose logs --tail=80 prometheus otel-collector loki tempo

# Check target status from Prometheus HTTP API
curl -fsS 'http://127.0.0.1:9090/api/v1/targets' | python3 -m json.tool
```

If targets are down, check app status, DNS/network reachability, and scrape config **before** assuming there are no requests. A missing series and a healthy zero-valued series are different conditions.

## Trust and operations boundaries

- Local Compose ports bind to `127.0.0.1` in source; do not assume this is safe for remote hosting.
- The log pipeline may contain sensitive values: review redaction and retention before production use.
- The Slack webhook is a local secret mount, not an environment variable to publish in logs.
- Instrumentation can fail independently of the application. Healthy `/health` does not prove logs or spans reached storage.

## Failure table

| Symptom | First check | Next hypothesis |
| --- | --- | --- |
| No Prometheus targets | `/api/v1/targets` | Scrape target name, app down, network |
| Metrics healthy but no traces | Collector logs and OTLP endpoint | Instrumentation/exporter mismatch |
| Traces present but no logs | Collector `filelog` and mounted path | File permissions or missing resource attributes |
| Alerts fire but no Slack | Alertmanager route and secret mount | Receiver/matcher/config problem |

## Evidence exercise

Draw the end-to-end path and capture a **sanitised** target API response, if available. Write one sentence for each failure boundary you could detect and one you could not. Do not claim a system is production-monitored because local Compose works.

Next: [Prometheus/RED](02-prometheus-red.md).
