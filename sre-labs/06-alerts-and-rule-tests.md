# 06 — Actionable alerts, burn rates and rule testing

## Objective

Explain how alert rules become reliable operational controls: meaningful thresholds, time windows, severity, service owner, evidence and tests.

## Existing rule logic

The project defines [application alerts](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/application.yml), [SLO rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/slo.yml), and [burn-rate rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/burn-rate.yml).

| Alert | Condition in current lab | Severity |
| --- | --- | --- |
| `DemoApiHigh5xxErrorRate` | Greater than 10% 5xx over 5m, pending for 1m | critical |
| `DemoApiHighP95Latency` | P95 exceeds 1s over 5m, pending 1m | warning |
| `DemoApiAvailabilityFastBurn` | 1m and 5m burn rate both greater than 4, pending 1m | critical |
| `DemoApiAvailabilitySlowBurn` | 5m and 15m burn rate both greater than 1, pending 2m | warning |

The combined window condition reduces alert noise but must be tuned for actual traffic volume and user impact. The short durations here are **local learning choices**, not universal production thresholds.

## Evaluate rules without generating incidents

In the observability repository (not the handbook), provided that `promtool` is installed:

```bash
promtool check config prometheus/prometheus.yml
promtool test rules prometheus/tests/rules.test.yml
```

The [fixture](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/tests/rules.test.yml) supplies synthetic counters and verifies alerts, labels and annotations. It checks representative target-down, 5xx and availability burn-rate cases. Do not claim it tests every possible latency/error edge case.

## Alertmanager notification path

The [Alertmanager config](https://github.com/AZ1600/platform-engineering-observability/blob/main/alertmanager/alertmanager.yml) groups by alertname/job and routes warning/critical alerts to Slack. The webhook is read from a mounted file, and resolved notifications are enabled. A Slack delivery failure should not be mistaken for an alert rule failure; inspect both hops separately.

## Design rubric

1. **Signal:** Does this reflect user impact or actionable risk?
2. **Context:** Which service, environment, owner, dashboard and runbook?
3. **Sensitivity:** Does this need a page, a ticket, or just a dashboard?
4. **Noise:** What are duplicate notifications, missing data and planned maintenance effects?
5. **Test:** Can a deterministic synthetic series prove the alert transitions to firing and resolved?
6. **Safety:** Can the investigation begin without taking action on infrastructure?

## Practical review

Examine the `DemoApiHighP95Latency` histogram metric and compare its name and labels against the demo app's available histogram families. If they differ, fix/verify the mismatch in the **observability repository** with a new rule test; do not silently change the handbook and assume the production alert works.

Next: [incident triage](07-incident-triage.md).
