# 01 — An Answer Framework That Holds Up to Follow-Ups

## The six-part response

1. **Problem:** who needed what, and under which constraints?
2. **Design:** a short request/event path and the important boundaries.
3. **Decision:** selected option, rejected alternative and reason.
4. **Proof:** an exact file, test, workflow or observed run.
5. **Limit:** what was not established, or where the approach fails.
6. **Next step:** smallest test or change that reduces uncertainty.

For a quick screening answer, use **problem → choice → proof → limit**. For deep technical interviews, use all six parts and offer a diagram.

## Worked example: observability

**Question:** "How do you know an alert tells you about user impact?"

**Evidence-backed practice response:** The [observability project](https://github.com/AZ1600/platform-engineering-observability) instruments HTTP requests and records availability and latency SLIs. Its [SLO rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/slo.yml) and [burn-rate rules](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/rules/burn-rate.yml) compare observed failures against the configured error budget. [Rule tests](https://github.com/AZ1600/platform-engineering-observability/blob/main/prometheus/tests/rules.test.yml) cover representative alert behaviour. These are short lab windows, not proof of production SLO compliance. In a live service I would validate the SLI against actual user journeys and adjust alert windows and paging thresholds.

**Follow-up:** "What happens when there is zero request traffic?" Check how the recorded SLI suppresses a numeric sample when request volume is zero; distinguish no data from a 0% success rate.

## Evidence ledger for every answer

| Field | Example |
| --- | --- |
| Claim | "The project includes alert rule tests" |
| Source | `prometheus/tests/rules.test.yml` |
| Evidence level | Test code exists; run status not rechecked |
| Boundary | Local demonstration, no uptime guarantee |
| Next check | Execute the documented promtool test in a clean checkout |

## Practice prompts

- Explain a Terraform design choice without using the phrase "best practice" as a substitute for reasoning.
- Describe what you personally built in a learning project without implying you operated it at enterprise scale.
- Compare test existence, passing CI at a named commit and recent cloud deployment evidence.

## Self-check

- [ ] Did I identify the user problem before naming a tool?
- [ ] Did I explain a rejected alternative?
- [ ] Can someone follow the implementation link and verify the claim?
- [ ] Did I qualify whether a result was documented, simulated or observed?

See [Chapter 12](../12-Interview-Preparation/Chapter-12-Interview-Preparation.md) and the [engineering evidence standard](../projects/Engineering-Evidence-Guide.md).
