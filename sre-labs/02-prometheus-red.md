# 02 — Prometheus, RED and query correctness

## Objective

Read application traffic through **Rate, Errors, Duration (RED)** and avoid common PromQL mistakes such as rate over gauges, division by zero, cardinality explosions or confusing scrape success with application success.

## Real metrics and labels

The [demo app's Prometheus config](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/prometheus.yml) names the scrape job `demo-api`. The [application rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/application.yml) use `http_requests_total` and duration histogram buckets. The repository excludes `handler="/metrics"` from request SLI calculations so scraper traffic does not inflate user activity.

Example read-only PromQL in the Prometheus expression browser:

```text
# Requests per second over 5m
sum(rate(http_requests_total{job="demo-api",handler!="/metrics"}[5m]))
```

```text
# Fraction of 5xx responses over 5m; guard the denominator
sum(rate(http_requests_total{job="demo-api",handler!="/metrics",status=~"5.."}[5m]))
/
clamp_min(sum(rate(http_requests_total{job="demo-api",handler!="/metrics"}[5m])), 0.000001)
```

```text
# P95 seconds over a 5m histogram (verify metric family exists)
histogram_quantile(0.95,
  sum by (le) (
    rate(http_request_duration_highr_seconds_bucket{job="demo-api"}[5m])
  )
)
```

A histogram quantile requires a histogram bucket family and a meaningful request volume. Low request counts make short-window percentiles noisy. Check units in Grafana instead of comparing seconds to milliseconds.

## How to query safely

```bash
# Non-mutating Prometheus instant query
curl -fsSG \
  --data-urlencode 'query=up{job="demo-api"}' \
  'http://127.0.0.1:9090/api/v1/query' | python3 -m json.tool
```

A reported `up=1` proves the target could be scraped during a scrape; **it does not prove customer transactions succeed**. `up=0` signals a scrape failure, not necessarily a total service outage.

## Cardinality and labeling

Bad series labels: `user_id`, email, raw URL with IDs, `request_id`, trace ID. These create unbounded time series and cost. Prefer controlled labels such as `service`, `handler`, `status`, `environment`; use logs/traces to carry unique IDs.

## Diagnostic exercise

1. Examine [target rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/targets.yml) and identify what scrape failure detects.
2. Compare `/metrics` (scraper) to `/work` (user request) and explain why exclusions matter.
3. Explain what a no-traffic window should mean for a service SLO.
4. Inspect [RED dashboard configuration](https://github.com/AZ1600/platform-engineering-observability/blob/main/grafana/dashboards/demo-api-red.json) and label each panel by question, unit and time window.

**Review:** differentiate a 5xx counter, a five-minute rate, a histogram bucket and `histogram_quantile`.

Next: [OpenTelemetry and logs](03-traces-and-logs.md).
