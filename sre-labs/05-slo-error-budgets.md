# 05 — SLIs, SLOs and error budgets

## Objective

Explain why an SLO is a measurable reliability objective for a user-visible behavior and how the error budget makes release decisions more defensible.

## Implemented example

The [recording rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/slo.yml) use an **availability SLO of 99%** (non-5xx responses) and a **latency SLO of 95% of requests completed within one second**. Lab recording rules use **five-minute windows** for demonstration; these are *not* evidence of a sustained monthly SLO.

| Indicator | Good event | Budget (bad events) |
| --- | --- | --- |
| Availability | HTTP response status is not 5xx | 1% for 99% target |
| Latency | Request duration at most 1 second | 5% for 95% target |

### Calculate one example

For 10,000 eligible requests during a defined window, 150 5xx responses means availability of **98.5%**, below a 99% objective. A 1% error budget permits 100 bad events; 150 bad events uses **150%** of that window's budget. This example is arithmetic, **not a measured project outcome**.

```text
Availability = good / total
Error ratio = bad / total
Burn rate = observed error ratio / allowed error ratio
```

For example, 4% errors against 1% allowance is **4x** burn rate. This represents a pace of budget consumption, not a statement that 4% of a month's total budget is gone.

## Read the implementation critically

- No request traffic should not silently become a 0% availability sample. The repo's SLI rules intentionally avoid emitting a ratio for empty request windows.
- Short windows help a local exercise but are volatile; production objectives require longer windows, explicit event inclusion rules, and honest handling of low volume.
- `demo_api:error_budget_availability_remaining:5m` is a short-window normalized signal, **not an accounting ledger of remaining monthly budget**.
- Consider whether a single HTTP 200 counts as success when the user workflow spans multiple calls.

## Read-only query examples

```text
demo_api:sli_availability_ratio:5m
```

```text
demo_api:sli_latency_under_1s_ratio:5m
```

```text
demo_api:error_budget_availability_remaining:5m
```

## Exercise

Define an SLI for CloudOps **approved risk ingestion** or PlatformPilot **fresh cluster state**, including unit, excluded events, measurement window, target, data source, and what happens on no traffic. Label this as a **design proposal**, not an implemented recording rule.

Next: [burn-rate alerts](06-alerts-and-rule-tests.md).
