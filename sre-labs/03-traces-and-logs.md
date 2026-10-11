# 03 — OpenTelemetry traces and structured logs

## Objective

Understand why a log line can answer *what happened* while a trace shows *where time was spent* within one request. Practise correlation rather than guessing from timestamps alone.

## Source review

The [Collector configuration](https://github.com/AZ1600/platform-engineering-observability/blob/main/otel/collector.yml) includes OTLP gRPC on `4317`, OTLP HTTP on `4318`, a `filelog/demo-api` receiver, `memory_limiter` and `batch` processors, an OTLP exporter to Tempo, and an OTLP HTTP exporter to Loki. The trace and log pipelines are distinct; success of one does not imply success of the other.

The demo application's `/work` path creates nested spans. Its JSON logs include fields such as `service`, `route`, `status_code`, `trace_id`, `span_id`, and `duration_seconds` (see [README evidence](https://github.com/AZ1600/platform-engineering-observability#distributed-tracing)).

```text
Request /work
  span: HTTP server
    span: perform-demo-work
      span: database-simulation

Log event: trace_id=... span_id=... status_code=...
                         |
                         v
                Grafana Loki -> Tempo
```

## Read-only checks when running locally

```bash
# Collector can emit errors for a broken exporter
docker compose logs --tail=120 otel-collector

# Query Tempo for a service's traces (local demo only)
curl -fsSG \
  --data-urlencode 'q={ resource.service.name = "demo-api" }' \
  --data-urlencode 'limit=5' \
  'http://127.0.0.1:3200/api/search' | python3 -m json.tool
```

The [smoke script](https://github.com/AZ1600/platform-engineering-observability/blob/main/scripts/observability-smoke.sh) separately verifies a metric, a Loki log stream and a Tempo trace. That is substantially stronger than checking only HTTP `/ready` endpoints.

## Debugging the missing-trace case

1. Verify request generation occurred during the selected time interval.
2. Confirm the application's endpoint and OTLP protocol agree with the Collector.
3. Check Collector receiver, pipeline processors, exporter and Tempo readiness.
4. Compare trace service name labels before assuming Grafana has a bug.
5. Check sampling and retention; not all spans are guaranteed to be retained.

## Privacy and reliability concerns

Do not store bearer tokens, passwords, raw personal data, or database connection strings in span attributes or logs. Avoid user IDs in metric labels. Correlation IDs should cross boundaries securely without becoming authentication credentials.

## Exercise

Write a miniature trace-to-log investigation: symptom, trace ID (placeholder only), responsible span, corroborating log, hypothesis and test. Identify what you could prove without production data.

Next: [Grafana investigations](04-grafana-investigation.md).
