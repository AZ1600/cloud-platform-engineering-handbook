# 08 — PlatformPilot Kubernetes and Prometheus diagnostics

## Objective

Distinguish **application API access failure**, **Prometheus connectivity/query failure**, and **Kubernetes workload failure**. These have different owners and corrective actions.

## Verified source behavior

The [PlatformPilot metrics router](https://github.com/AZ1600/platform-pilot/blob/main/backend/routers/metrics.py) protects its `/metrics` endpoints with `require_role("viewer")` and maps Prometheus connection errors to **503**, failed queries to **502**, and unexpected integration errors to **500**. Authentication and role enforcement are application concerns; they do not replace Kubernetes service-account permissions or network policy.

The [Prometheus service](https://github.com/AZ1600/platform-pilot/blob/main/backend/services/prometheus_service.py) queries Prometheus's `/api/v1/query` with a timeout, counts healthy and unhealthy scrape targets using `up`, and combines kube-state-metrics-based resource queries for Kubernetes views. Data quality still depends on exporters and the selected cluster context.

| Observation | Interpretation to verify | First boundary |
| --- | --- | --- |
| 401 from protected API | Missing/invalid PlatformPilot token | API auth |
| 403 on export | Authenticated viewer lacks operator privilege | App role policy |
| 503 from metrics route | Prometheus unreachable | Service / port-forward / DNS |
| 502 from metrics route | Query/API response failed | PromQL or Prometheus API |
| 200 with empty series | Metric absent, scrape missing, or truly no objects | Telemetry freshness |

## Safe lab approach

Use tests rather than hardcoding or sharing real bearer tokens:

- [Security and route tests](https://github.com/AZ1600/platform-pilot/blob/main/backend/tests/test_rbac_routes.py) exercise 401/403/503 behavior.
- [Prometheus integration code](https://github.com/AZ1600/platform-pilot/blob/main/backend/services/prometheus_service.py) shows the exact exception types and query path.
- [CloudOps export route](https://github.com/AZ1600/platform-pilot/blob/main/backend/routers/cloudops.py) requires at least `operator` and exports findings after analysis.

```text
Browser -> PlatformPilot FastAPI -> role gate -> metrics router -> Prometheus
                                       |
                                   Kubernetes API (other routes)
                                       |
                            CloudOps export (operator only)
```

## Investigation worksheet

For a broken cluster dashboard, record: the failing endpoint, HTTP status, authentication role, whether `/auth/me` works, Prometheus target health, Kubernetes API reachability, exporter availability, last-known data time, and relevant request ID if available. Avoid treating a 200 as proof all external dependencies are healthy.

## Production hardening questions

- Are static role tokens sufficient for multiple users, rotation and audit attribution?
- Do you limit cluster API permissions to read-only where possible?
- What breaks if Prometheus becomes unavailable or reports stale data?
- Can operators export findings without authorizing execution?

**Boundary:** the local observability demo stack and PlatformPilot are distinct repos. This lesson reviews comparable technologies; it does not assert they are already wired together.

Next: [CloudOps approval evidence](09-cloudops-operational-evidence.md).
