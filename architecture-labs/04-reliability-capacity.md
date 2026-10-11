# 04 — Reliability, Capacity and Recovery

**Objective:** make failure domains, RTO/RPO, load envelopes and alerting explicit before picking redundancy techniques.

## Work backwards from user impact

For an API request, distinguish DNS, load balancer, compute instance/pod, database, external identity service and queue. Each has its own failure modes and observability. Two replicas on a single node do not protect against node failure, and a multi-AZ cluster does not protect from an application bug shipped to every replica.

The [Terraform EKS repository](https://github.com/AZ1600/platform-engineering-terraform-eks) defines multi-AZ private networking and managed node group configuration. The project deliberately supports **plan-only CI**; this is not proof that a live multi-AZ EKS service is currently running. Use a plan and separate deployment evidence to identify actual versus proposed availability.

## Back-of-envelope capacity (illustrative)

Assume an API has 120 requests/second at peak and one replica can sustain 45 requests/second while meeting its measured latency objective. `ceil(120 / 45) = 3` replicas to meet steady-state throughput. At 60% desired utilisation, `ceil(120 / (45 × 0.60)) = 5`. These are *hypothetical* numbers, not benchmark data. Autoscaling also needs startup time, saturation metrics and downstream database capacity.

| Failure | Detection | Mitigation | Verification |
| --- | --- | --- | --- |
| Crash-looping Pod | Restart count, events, readiness | Revert bad deploy or fix configuration | Ready replicas, error rate normal |
| Database unavailable | Query errors, connection saturation | Fail safely; restore or fail over | Writes verified without duplication |
| Missing IAM permission | Explicit access denied | Scoped policy review | Retest intended action only |
| Unhealthy dependency | SLI or targeted canary | Circuit breaker or degraded mode | Dependency and user path recover |

## Runbooks need reversibility

For each change, record trigger, blast radius, preflight, expected state, abort condition, rollback and post-change verification. An automatic restart may destroy valuable forensic evidence; capture logs and events when feasible and safe.

## Exercise

Design a recovery test for the [Pharmacy API on EKS](../projects/Pharmacy-API-EKS.md): distinguish a missing image, a permission error, a slow dependency and an OOM kill. Map each to a signal, owner and **read-only** investigation command. Define one user-facing SLI and a justified alert duration.

[Next: Security architecture](05-identity-security.md)
