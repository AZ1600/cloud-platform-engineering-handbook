# Platform Engineering Observability

> A local observability stack using Prometheus for metric collection and Grafana for visualisation.

**Repository:** <https://github.com/AZ1600/platform-engineering-observability>  
**Last verified:** 2026-07-11 against the repository README

## How It Works

```text
Instrumented targets -> Prometheus scrape and storage -> Grafana data source -> dashboards
```

Docker Compose runs the components locally. Repository screenshots show the Prometheus interface and targets plus Grafana data-source and dashboard configuration.

## Concepts to Explain Deeply

- Metrics, labels, time series, scrape targets, and queries.
- The difference between monitoring, observability, dashboards, and alerting.
- Golden signals and service-level indicators.
- Cardinality, retention, and resource consumption.
- Dashboard evidence versus actionable alerts.

## Next Engineering Steps

- Add a deliberately instrumented application target.
- Store Prometheus and Grafana data in persistent volumes.
- Provision dashboards and data sources as code.
- Define alert rules and route them through Alertmanager.
- Document one failure investigation using metrics.
