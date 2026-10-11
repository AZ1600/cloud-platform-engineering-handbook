# 04 — PlatformPilot: API design, roles and the Kubernetes boundary

**Project:** [AZ1600/platform-pilot](https://github.com/AZ1600/platform-pilot) · **Primary evidence:** [`backend/app.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/app.py), [`backend/core/security.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/core/security.py), [`backend/tests/test_rbac_routes.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/tests/test_rbac_routes.py).

## What the implementation does

```text
React browser
   | bearer token
   v
FastAPI routes -> app-level role dependency -> Kubernetes client
   |                   |
   |                   + viewer / operator / admin token configuration
   +-> Prometheus / analysis routes
   +-> POST /cloudops/findings (operator+)
                             |
                             v
                  CloudOps ingest boundary
```

The application aggregates Kubernetes resources, logs, events, health signals and related analysis. **The backend is a high-value boundary** because it can read information about workloads. A frontend hiding an action is not equivalent to backend authorization.

## Two distinct role systems

1. **PlatformPilot API roles:** the source defines `viewer`, `operator`, `admin` with increasing ranks, supplied through environment-configured bearer tokens.
2. **Kubernetes RBAC:** the identity used by the backend Kubernetes client controls what the backend may actually read or change in the cluster.

A PlatformPilot viewer cannot call its operator export route, but this does not change the Kubernetes client's permissions. Restrict both boundaries independently.

## Read the security code with precision

In [`core/security.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/core/security.py):

- If no role tokens are configured, protected routes fail with `503` instead of falling back to anonymous access.
- A missing or invalid bearer token returns `401`.
- `require_role('viewer')` permits viewer, operator and admin; `require_role('operator')` excludes viewer.
- `secrets.compare_digest` compares the supplied token to configured values.

**Limitations to discuss:** a shared environment token is not a per-person identity; rotation, individual audit attribution, session lifecycle, rate limiting and secret distribution need careful treatment. The existence of checks does not prove deployment hardening.

## Evidence in tests

The [RBAC route tests](https://github.com/AZ1600/platform-pilot/blob/main/backend/tests/test_rbac_routes.py) explicitly cover:

| Test condition | Expected HTTP result |
|---|---|
| Public `/health` without auth | `200` |
| No tokens configured and protected `/pods` | `503` |
| Missing/incorrect token with configured auth | `401` |
| Viewer requesting normal protected read | `200` (mocked data) |
| Viewer POSTing `/cloudops/findings` | `403` |

**Run these tests only in the PlatformPilot clone**, not from inside the handbook:

```bash
cd /path/to/platform-pilot/backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests/test_rbac_routes.py -q
```

Install dependencies only in a trusted isolated environment. This command is **reproduction guidance**, not a claim that the test was executed during the handbook refresh.

## Trace a protected export

[`backend/routers/cloudops.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/routers/cloudops.py) uses `require_role('operator')`, calls a summary generator, assigns finding IDs/UTC timestamps and delegates exports to `cloudops_export_service`.

```text
operator credentials -> PlatformPilot API -> incident detection
  -> finding ID + time + environment + cluster
  -> CloudOps ingestion -> validation -> reviewable risk
```

The exporter does not make the sender's findings intrinsically trustworthy. The receiver must authenticate the sender and validate payload shape and authorization separately.

## Improvement exercise

Design (but don't assume implemented): short-lived per-user identity, explicit token rotation, least-privilege Kubernetes read-only ServiceAccount, scoped namespaces, monitoring of denied calls, output redaction and an audit trail linking actor to export action.

### Interview prompt

> “If PlatformPilot's frontend only displays read-only buttons for viewers, why would backend authorization still be necessary?”

Answer by naming the API trust boundary, direct HTTP requests, backend role dependency and separate cluster credentials.
