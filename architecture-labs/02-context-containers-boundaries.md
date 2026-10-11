# 02 — Context, Containers and Trust Boundaries

**Objective:** use C4-style diagrams to distinguish the *users and external systems* from deployable units, data stores and their interactions. Keep a separate trust-boundary overlay.

## PlatformPilot example: current interfaces

```text
Engineer browser
   | bearer token, HTTPS in a suitable deployment
   v
React UI  --->  FastAPI API (viewer / operator / admin checks)
                      |                  |
                      | Kubernetes       | Prometheus HTTP queries
                      v                  v
                Kubernetes API      Prometheus
                      |
                Pods, logs, events

FastAPI -- authenticated finding export --> CloudOps API
```

The [PlatformPilot repository](https://github.com/AZ1600/platform-pilot) now includes role-scoped bearer-token API protection. **Application roles and Kubernetes RBAC are different boundaries:** passing a viewer role check does not grant a Kubernetes ServiceAccount additional privileges. The integration boundary to CloudOps uses separate credentials and contracts. Do not label the whole topology “zero trust” simply because it has bearer tokens.

## How to create the diagrams

1. **Context:** operator, the PlatformPilot system, Kubernetes, Prometheus, CloudOps and their high-level responsibilities.
2. **Containers:** frontend, FastAPI backend, cluster API, metric store and downstream API.
3. **Components:** routes, authentication dependency, Kubernetes client, Prometheus query service, finding export.
4. **Trust overlay:** browser-to-API, API-to-cluster, API-to-metrics and API-to-CloudOps; record credential source, scope, transport and denial behavior at each crossing.

| Crossing | What to verify | Failure behavior |
| --- | --- | --- |
| Browser → API | Bearer token and role for route | 401 / 403 when invalid or insufficient |
| API → Kubernetes | kubeconfig or ServiceAccount plus Kubernetes RBAC | API permissions and unavailable-cluster errors |
| API → Prometheus | Query endpoint and timeout | 502/503 mapped by metrics router |
| PlatformPilot → CloudOps | Independent ingestion token and schema | Reject invalid or unauthorised finding |

**Code evidence:** [PlatformPilot metrics router](https://github.com/AZ1600/platform-pilot/blob/main/backend/routers/metrics.py) applies viewer authorization; [CloudOps finding contract](https://github.com/AZ1600/cloudops-command-center/blob/main/contracts/operational-finding.schema.json) defines expected payloads.

## Exercise

Diagram the actual call sequence for `GET /metrics/health`. Annotate the boundary that can return 503 and explain why a process-level `/health` result alone does not prove Prometheus or Kubernetes is healthy.

[Next: State and idempotency](03-data-events-idempotency.md)
