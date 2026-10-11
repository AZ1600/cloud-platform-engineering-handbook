# 05 — SRE Incident Response Interview Exercise

## Hypothetical incident

A demonstration service shows an elevated HTTP 5xx ratio and high P95 latency after a release. Treat this as a **mock exercise**, not a claim about an actual outage.

Your first 60 seconds should establish customer impact, when symptoms began, what changed and who owns the response.

## Investigation sequence

1. **Impact:** affected route, environment, estimated customer scope and time window.
2. **Signals:** request rate, error ratio, latency, saturation and scrape health.
3. **Correlation:** link deployment time, logs, traces and infrastructure events.
4. **Hypothesis:** choose the simplest test that distinguishes application regression from dependency failure.
5. **Mitigation:** choose a controlled rollback, feature flag or traffic shift with appropriate authorization.
6. **Recovery:** verify error and latency indicators plus user journeys; don't equate "Pods Running" with recovery.
7. **Learning:** create timeline, root-cause hypotheses, actions, owner and follow-up tests.

## Existing evidence

The [observability project](https://github.com/AZ1600/platform-engineering-observability) includes Prometheus application rules, Grafana dashboards, Loki logs, Tempo tracing and a smoke test. [Its rule test fixture](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/tests/rules.test.yml) tests selected alerts. These are lab artifacts and do not establish any service's ongoing uptime.

**Example PromQL** (match the actual metric labels in your environment):

```text
sum(rate(http_requests_total{job="demo-api",status=~"5..",handler!="/metrics"}[5m]))
/
sum(rate(http_requests_total{job="demo-api",handler!="/metrics"}[5m]))
```

A zero denominator requires explicit no-traffic handling; do not report a fabricated 0% or 100% SLI.

## Interviewer follow-ups

- What is the difference between an SLI, SLO and SLA?
- Why use multi-window burn-rate paging rather than a single momentary threshold?
- How do you avoid changing systems before establishing evidence?
- How do you report uncertainty when the root cause remains unknown?

## Postmortem fields

**Trigger, timeline, user impact, detection, evidence links, contributing conditions, mitigation, recovery proof, corrective actions, owners and due dates.** A blameless postmortem still identifies technical and process gaps.

See [SRE labs](../sre-labs/index.md) and [Chapter 9](../09-Observability/Chapter-09-Observability.md).
