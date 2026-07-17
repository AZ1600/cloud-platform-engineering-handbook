# PlatformPilot — Complete Learning Case Study

> An operations dashboard that reads Kubernetes cluster data through a FastAPI backend and presents health, resources, events, logs, and rule-based recommendations in a React interface.

**Repository:** <https://github.com/AZ1600/platform-pilot>  
**Status:** Working learning project; not yet production-ready  
**Code reviewed:** 2026-07-11  
**Main stack:** React 19, Vite, React Router, FastAPI, Python 3.12, Kubernetes Python Client

## 1. What You Built

PlatformPilot gives an engineer a browser-based view of a Kubernetes cluster. Instead of repeatedly running `kubectl` commands, the user can open pages for pods, deployments, nodes, namespaces, cluster events, logs, and health recommendations.

The project contains three main layers:

1. A React frontend that displays the information.
2. A FastAPI backend that exposes HTTP endpoints.
3. The Kubernetes Python Client, which reads information from the cluster API.

The current recommendation feature is a deterministic rule engine. It is labelled “AI” in the interface, but it does not currently call a language model or machine-learning service. This is not a weakness in a learning project: simple, explainable rules are often the safest first version of operational automation.

## 2. The Problem It Solves

Kubernetes exposes a large amount of operational data, but engineers normally access it through several commands:

```bash
kubectl get pods
kubectl get deployments
kubectl get nodes
kubectl get namespaces
kubectl get events
kubectl logs <pod-name>
kubectl describe deployment <deployment-name>
```

That workflow is powerful, but information is distributed across commands and raw output. PlatformPilot creates one interface that:

- summarises cluster health;
- identifies non-running pods and degraded deployments;
- exposes recent events and pod logs;
- supports resource search and filtering;
- suggests a likely cause, owner, severity, and next action.

The real engineering value is not simply the dashboard. It is the integration boundary between a web application and the Kubernetes control plane.

## 3. Architecture in Plain Language

Imagine a receptionist between a visitor and a secured records room:

- The React frontend is the visitor asking for information.
- FastAPI is the receptionist receiving and translating the request.
- The Kubernetes Python Client is the authorised records clerk.
- The Kubernetes API server is the records room.

The browser does not access Kubernetes directly. It asks FastAPI, and FastAPI uses Kubernetes credentials available on its host.

```text
Browser
  |
  | HTTP GET http://127.0.0.1:8000/...
  v
React application
  |
  | fetch()
  v
FastAPI routes in backend/app.py
  |
  | Python function calls
  v
backend/kubernetes_client.py
  |
  | authenticated Kubernetes API calls
  v
Kubernetes API server
  |
  v
Pods, deployments, nodes, namespaces, events and logs
```

## 4. Repository Structure

```text
platform-pilot/
├── backend/
│   ├── app.py                 # HTTP API routes and cluster summary logic
│   ├── ai.py                  # Rule-based pod analysis
│   ├── kubernetes_client.py   # Kubernetes API access and data shaping
│   ├── requirements.txt       # Pinned Python packages
│   └── Dockerfile             # Backend container image
├── frontend/
│   ├── src/
│   │   ├── components/        # Shared UI elements
│   │   ├── pages/             # Dashboard and resource pages
│   │   ├── services/api.js    # Frontend-to-backend requests
│   │   ├── App.jsx            # Browser routes
│   │   └── main.jsx           # React entry point
│   ├── package.json
│   └── vite.config.js
├── screenshots/
└── README.md
```

## 5. Backend Startup — What Happens First

When Python imports `backend/kubernetes_client.py`, this line runs immediately:

```python
config.load_kube_config()
```

It loads the same kubeconfig normally used by `kubectl`, usually from `~/.kube/config`. That file identifies the cluster and contains or references credentials.

The module then creates two clients:

```python
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()
```

- `CoreV1Api` reads core resources such as pods, nodes, namespaces, services, ConfigMaps, Secrets, events, and logs.
- `AppsV1Api` reads application-controller resources such as Deployments.

FastAPI is created in `backend/app.py`:

```python
app = FastAPI(title="PlatformPilot API")
```

Uvicorn imports that `app` object and listens on port 8000.

### Why this matters

Loading local kubeconfig is suitable for local development. It is not the normal production approach for a pod running inside Kubernetes. An in-cluster deployment would normally call `config.load_incluster_config()` and use a Kubernetes ServiceAccount with carefully limited RBAC permissions.

## 6. CORS — Why the Browser Is Allowed to Call FastAPI

The frontend development server runs on port 5173 or 5174. The API runs on port 8000. Browsers treat those as different origins, even though both use localhost.

FastAPI therefore configures CORS for four local development origins. It permits all HTTP methods and headers for those origins.

Without CORS permission, the browser would block frontend JavaScript from reading the API response. CORS is a browser control; it is not authentication and does not protect the API from direct requests.

## 7. Frontend Request Flow

`frontend/src/services/api.js` centralises most API calls:

```javascript
const API_URL = "http://127.0.0.1:8000";
```

For example, opening the Pods page triggers this flow:

```text
Pods.jsx mounts
  -> useEffect() calls getPods()
  -> fetch("http://127.0.0.1:8000/pods")
  -> FastAPI pods() route
  -> list_pods()
  -> Kubernetes list_namespaced_pod(namespace="default")
  -> Python converts resource objects into small dictionaries
  -> FastAPI serialises the list to JSON
  -> React stores it in state
  -> the table renders
```

The page repeats the request every ten seconds. React clears the interval when the component unmounts, preventing an abandoned timer from continuing in the background.

## 8. Pod Status — More Than the Kubernetes Phase

Kubernetes gives each pod a broad phase such as `Pending`, `Running`, `Succeeded`, `Failed`, or `Unknown`. Useful troubleshooting states such as `CrashLoopBackOff` and `ImagePullBackOff` are usually found inside container state rather than the top-level pod phase.

The client therefore starts with `pod.status.phase`, then checks the first container:

```text
Pod phase
  -> if first container is waiting, use waiting.reason
  -> otherwise, if terminated, use terminated.reason
```

This makes the dashboard more useful than showing only `Pending` or `Running`.

### Current limitation

Only `container_statuses[0]` is inspected. A multi-container pod could have a healthy first container and a failed sidecar. A stronger implementation would inspect every init container and application container and return per-container states.

## 9. Pod Analysis — What “AI” Currently Means

`backend/ai.py` maps four exact status strings to recommendations:

| Status | Severity | Interpreted cause | Suggested owner |
|---|---|---|---|
| `ImagePullBackOff` | High | Image cannot be pulled | Platform Engineering |
| `ErrImagePull` | High | Image pull failed | Platform Engineering |
| `CrashLoopBackOff` | Critical | Application repeatedly crashes | Application Team |
| `OOMKilled` | Critical | Container exceeded memory limit | Application Team |

Anything else receives a low-severity “No issues detected” response.

This is a rules engine because the same input always produces the same predefined output. It is transparent, cheap, fast, and easy to test.

### Important limitation

The fallback is unsafe for an unknown failure. A pod could be `Pending`, `Error`, `CreateContainerConfigError`, or `Evicted` and receive “No issues detected.” The fallback should say that the state is unclassified and needs investigation, not that nothing is wrong.

### Sensible evolution

1. Expand tested deterministic rules.
2. Include events, logs, restart counts, and container states as evidence.
3. Return confidence and evidence fields.
4. Optionally use a language model to explain the evidence.
5. Keep remediation execution separate and approval-gated.

## 10. API Endpoint Map

| Endpoint | Purpose | Kubernetes scope |
|---|---|---|
| `GET /` | API identification | None |
| `GET /health` | Process-level health response | None |
| `GET /pods` | List pods and interpreted status | `default` namespace |
| `GET /deployments` | List deployment replica health | `default` namespace |
| `GET /deployments/{name}` | Deployment conditions and related pods | `default` namespace |
| `GET /nodes` | List node readiness and versions | Cluster-wide |
| `GET /nodes/{name}` | Node capacity and runtime details | Cluster-wide |
| `GET /namespaces` | List namespaces | Cluster-wide |
| `GET /namespaces/{name}` | Count namespace resources | Selected namespace |
| `GET /events/recent` | Ten most recent events | Cluster-wide |
| `GET /events/{pod}` | Events for one pod | `default` namespace |
| `GET /logs/{pod}` | Last 100 log lines | `default` namespace |
| `GET /risks` | Non-running pod rules | `default` namespace |
| `GET /analysis` | Issues with events, logs and rules | `default` namespace |
| `GET /analysis/{pod}` | Detailed analysis for one pod | `default` namespace |
| `GET /cluster-summary` | Combined health view | Mixed/all namespaces |
| `GET /dashboard` | Older dashboard summary | `default` namespace |

## 11. Cluster Health Score

The backend starts at 100 and subtracts:

```text
15 points for every non-running pod
20 points for every degraded deployment
25 points for every non-ready node
minimum score = 0
```

A deployment is considered healthy when:

```text
desired replicas == ready replicas == available replicas
```

This is an understandable demonstration formula, not a real service-level health model.

### Why the score can mislead

- A completed Job pod may be `Succeeded`, not `Running`, and be counted as failed.
- System and application pods are weighted equally.
- One broken pod in a 100-pod cluster has the same penalty as one broken pod in a 2-pod cluster.
- The score ignores restart count, readiness, latency, traffic, error rate, resource pressure, and business criticality.
- A single unhealthy node may subtract points even when workloads have safely moved elsewhere.

A production score should be based on explicit service-level signals and should expose the evidence behind every deduction.

## 12. Deployments

The list view compares desired, ready, and available replicas. The details route then:

1. Reads the Deployment from the default namespace.
2. Reads its label selector.
3. Converts the selector into a Kubernetes label query.
4. Lists matching pods.
5. Returns deployment conditions.
6. Creates a simple health recommendation.

This demonstrates an important Kubernetes relationship:

```text
Deployment -> ReplicaSet -> Pods
```

The current code finds related pods through labels rather than directly reading the ReplicaSet ownership chain. This usually works when labels are designed correctly, but owner references provide a more exact relationship.

## 13. Nodes

Node readiness is derived from the `Ready` condition. The details page also displays:

- kubelet version;
- operating system and architecture;
- kernel version;
- container runtime;
- CPU, memory, and pod capacity.

The backend also returns allocatable resources, but the current page displays capacity only.

Capacity is the total resource known to the node. Allocatable is what Kubernetes can offer to pods after reserving resources for the operating system and Kubernetes components. For scheduling and platform decisions, allocatable is usually the more useful value.

## 14. Namespaces

The namespace details route counts pods, deployments, services, ConfigMaps, and Secrets. It returns only the Secret count, not Secret contents.

### Important permission lesson

Even counting Secrets requires the backend identity to have `list` permission on Secrets. A monitoring dashboard often does not need that permission at all. Least privilege means removing permissions that do not create enough user value.

### Current health limitation

The namespace logic checks only whether `pod.status.phase != "Running"`. A pod in `CrashLoopBackOff` can still have a top-level `Running` phase, so the namespace may appear healthy while a container is repeatedly failing.

## 15. Events and Logs

Events explain Kubernetes control-plane observations such as scheduling failures, image pull failures, probe failures, and back-off behaviour. Logs expose application output from a container.

For pod details, PlatformPilot combines:

```text
resource status + Kubernetes events + last 100 log lines + rule recommendation
```

That is the right general troubleshooting model: never diagnose from one signal alone.

### Current limitations

- Events and logs are always read from the `default` namespace.
- Pod name alone is used as the identifier.
- Multi-container pods do not let the user select a container.
- Previous container logs are not requested after a crash.
- The frontend fetches logs every five seconds rather than streaming them.
- Error strings from the Kubernetes client may be returned directly to the browser.

## 16. React Application Structure

`App.jsx` uses React Router to map browser paths to pages. `Navbar.jsx` exposes those routes to the user.

React state holds API data, search text, selected filters, errors, and timestamps. `useEffect` starts requests when pages mount. List pages derive filtered arrays without changing the original API data.

The frontend currently polls:

- dashboard, pods, deployments, nodes, and namespaces every 10 seconds;
- pod logs every 5 seconds;
- detail views generally once when the route parameter changes.

Polling is simple and appropriate for a first version. At larger scale it can create unnecessary load. A future version could use configurable refresh intervals, caching, conditional requests, Server-Sent Events, or WebSockets.

## 17. A Confirmed Frontend/Backend Contract Bug

The `/cluster-summary` endpoint returns nested values:

```json
{
  "pods": {"running": 10, "failed": 1},
  "deployments": {"healthy": 3, "degraded": 1}
}
```

`AISummary.jsx` tries to read flat values:

```javascript
summary.running_pods
summary.failed_pods
summary.healthy_deployments
summary.degraded_deployments
```

Those properties do not exist, so the page can show undefined values. The correct references are:

```javascript
summary.pods.running
summary.pods.failed
summary.deployments.healthy
summary.deployments.degraded
```

This is a useful API-contract lesson. Frontend and backend types or contract tests would catch the mismatch before release.

## 18. Docker

The backend Dockerfile:

1. Starts with `python:3.12-slim`.
2. Sets `/app` as the working directory.
3. Copies and installs Python requirements.
4. Copies the backend source.
5. documents port 8000.
6. starts Uvicorn on all network interfaces.

The repository does not currently contain a frontend Dockerfile or root Compose file at the paths reviewed.

### Containerisation issue to understand

The backend calls `load_kube_config()`. A container will not automatically contain the developer’s kubeconfig. Mounting personal kubeconfig into the container can work locally but exposes powerful credentials. In Kubernetes, use in-cluster configuration and a restricted ServiceAccount instead.

### Production hardening

- Run as a non-root user.
- Use a `.dockerignore`.
- Include health checks.
- Scan dependencies and the resulting image.
- Pin the base image by digest where reproducibility requires it.
- Avoid copying credentials or unnecessary files into the image.

## 19. Security Model

The current API has no authentication or authorisation. Anyone who can reach it can request cluster inventory and logs within the backend identity’s permissions.

This matters because operational data can reveal:

- workload and namespace names;
- container output and application errors;
- cluster versions and node details;
- internal architecture and deployment state.

A production version needs:

1. User authentication.
2. Application-level roles and permissions.
3. Kubernetes RBAC with least privilege.
4. Namespace scoping.
5. Audit logging.
6. TLS and trusted network boundaries.
7. Input validation and safe error responses.
8. Rate limiting and request timeouts.
9. Secret and credential management.

The empty `.gitignore` should also be corrected before local files are added. Kubeconfigs, environment files, tokens, build output, and editor files must never be committed accidentally.

## 20. Reliability and Error Handling

Several backend Kubernetes calls have no local exception handling. If the cluster is unavailable, credentials expire, or permission is denied, FastAPI may return a generic server error.

The frontend request helpers call `res.json()` without checking `res.ok`. An HTTP 403 or 500 therefore may not be handled cleanly.

The `/health` endpoint always says healthy if the FastAPI process can answer. It does not prove that Kubernetes is reachable. A clearer model uses:

- liveness: the API process is alive;
- readiness: required dependencies can be reached;
- dependency status: Kubernetes access and latency are reported separately.

## 21. Namespace Consistency

Some endpoints use only `default`, while the cluster summary reads all namespaces. This creates an inconsistent experience:

- the dashboard may report an incident in another namespace;
- opening pod analysis by name searches only default;
- events and logs by pod name also use default;
- identical pod names can exist in different namespaces.

Resource routes should use namespace explicitly, for example:

```text
GET /namespaces/{namespace}/pods/{pod}
GET /namespaces/{namespace}/pods/{pod}/logs
GET /namespaces/{namespace}/deployments/{deployment}
```

## 22. Performance and Scale

Every browser poll can trigger multiple live Kubernetes API calls. `/cluster-summary` reads pods, deployments, nodes, namespaces, and events in one request. With several users polling every ten seconds, the backend can repeatedly perform the same expensive work.

Future improvements include:

- short-lived server-side caching;
- one shared background collector;
- pagination and label/namespace filters;
- API timeouts and concurrency limits;
- Kubernetes watch streams;
- response-size limits for events and logs;
- metrics for request rate, latency, error rate, cache hits, and upstream calls.

## 23. Testing Strategy

No test suite was found in the files reviewed. A sensible test pyramid is:

### Unit tests

- every pod-status rule;
- unknown-status fallback;
- health-score calculation;
- pod and deployment data transformation;
- log cleaning;
- node readiness logic.

### API tests

- response schema for every route;
- correct 404 and permission responses;
- namespace and resource-name validation;
- Kubernetes client failures;
- `/cluster-summary` contract used by React.

### Frontend tests

- loading, success, empty, and error states;
- search and filtering;
- nested summary fields;
- interval cleanup;
- inaccessible API and non-JSON errors.

### Integration tests

- run against a disposable `kind` or `k3d` cluster;
- deploy healthy and intentionally broken workloads;
- verify events, logs, status interpretation, and recommendations.

## 24. How to Debug PlatformPilot

### Frontend shows “Loading” forever

1. Open browser developer tools.
2. Check the Network tab for the API request.
3. Confirm FastAPI is listening on port 8000.
4. Check CORS errors in the browser console.
5. Open the endpoint directly.
6. Confirm the response shape matches the page.

### Backend fails during startup

1. Read the Python traceback.
2. Check that kubeconfig exists and the current context is correct.
3. Run `kubectl cluster-info`.
4. Confirm package versions are installed.
5. Check whether the process can read the kubeconfig and referenced credential files.

### API returns a Kubernetes permission error

1. Identify the exact verb and resource: for example, `list pods` or `get pods/log`.
2. Identify the user or ServiceAccount used by the backend.
3. Test with `kubectl auth can-i`.
4. Grant only the minimum required permission.
5. Avoid using cluster-admin as a shortcut.

### Pod analysis looks wrong

1. Compare the displayed status with `kubectl get pod`.
2. Inspect every container with `kubectl describe pod`.
3. Read current and previous logs.
4. Review Kubernetes events.
5. Check whether the status has a rule in `ai.py`.

### Status of the known findings

The API contract, namespace identity, multi-container inspection, unknown-state handling, and authentication findings are currently **review-discovered defects**. They must not be described as solved until code changes and tests prove the correction. They are tracked in the [PlatformPilot debugging backlog](../DEBUGGING-ISSUE-REGISTER.md#_6-platformpilot-defects-found-during-review).

## 25. Engineering Decisions and Trade-offs

| Decision | Benefit | Trade-off |
|---|---|---|
| React single-page interface | Fast interactive navigation and reusable UI | Requires client-side state and API contract management |
| FastAPI backend | Clear Python API and automatic docs | Needs security, error handling, and operational hardening |
| Kubernetes Python Client | Structured API access without shelling out to `kubectl` | Credentials and RBAC must be handled carefully |
| Poll every 5–10 seconds | Easy to implement and understand | Repeated load and delayed updates |
| Rule-based recommendations | Explainable and deterministic | Limited coverage and no contextual reasoning |
| Local kubeconfig | Fast local development | Unsuitable for a deployed production service |
| Default-namespace resource routes | Simple first version | Incomplete and inconsistent cluster visibility |

## 26. Production-Readiness Roadmap

### Phase 1 — Correctness

- Fix the AI Summary response mismatch.
- Make namespace part of resource identity.
- Inspect all pod containers.
- Treat unknown failures as unclassified, not healthy.
- Add consistent HTTP errors and response schemas.
- Add backend and frontend tests.

### Phase 2 — Configuration and packaging

- Move API URL into environment configuration.
- Add frontend containerisation or a documented hosting model.
- Add `.gitignore` and `.dockerignore` rules.
- Support local and in-cluster Kubernetes configuration explicitly.
- Add CI for lint, tests, builds, and scans.

### Phase 3 — Security

- Add user authentication and roles.
- Create least-privilege Kubernetes RBAC.
- Remove unnecessary Secret-listing permission.
- Add audit events, rate limits, TLS, and safe error responses.
- Perform threat modelling.

### Phase 4 — Operations

- Add dependency-aware health endpoints.
- Instrument API latency, errors, and Kubernetes calls.
- Add caching or shared collection.
- Add structured logs and request correlation.
- Define availability and freshness objectives.

### Phase 5 — Evidence-based intelligence

- Analyse events, logs, conditions, restart counts, and resource pressure together.
- Show evidence and confidence for each recommendation.
- Add more deterministic rules and tests.
- Introduce an optional language-model explanation layer.
- Keep all cluster-changing actions approval-gated and auditable.

## 27. How to Explain PlatformPilot in an Interview

### 30-second answer

PlatformPilot is a React and FastAPI operations dashboard that reads Kubernetes resources through the official Python client. It centralises pod, deployment, node, namespace, event, and log visibility and applies explainable rules to common failure states. Building it taught me how frontend API contracts, Kubernetes authentication, RBAC, resource state, polling, and operational diagnostics fit together.

### Two-minute answer

The React frontend calls a FastAPI service, and the service uses the Kubernetes Python Client rather than executing shell commands. I transform Kubernetes resource objects into smaller JSON responses for the UI. The dashboard calculates a simple health view from pod, deployment, and node state. Detail pages combine status with events and logs, and a rule engine classifies known failures such as CrashLoopBackOff, ImagePullBackOff, and OOMKilled.

The current version is intentionally a learning-stage system. During review I identified production gaps including local kubeconfig usage, default-namespace assumptions, no authentication, a frontend/backend response mismatch, limited failure rules, and no tests. My next steps are correctness and contract tests first, then namespace-aware APIs, in-cluster ServiceAccount authentication with least-privilege RBAC, observability, caching, and evidence-based recommendations.

### Likely follow-up questions

**Why not call `kubectl` from FastAPI?**  
The official client provides structured objects, avoids parsing command output, and gives clearer control over configuration and errors.

**How would you deploy it inside Kubernetes?**  
Build images, deploy the API and frontend, use in-cluster configuration, attach a restricted ServiceAccount, configure networking and ingress, add health probes, and inject environment-specific settings without copying kubeconfig into an image.

**Is it really AI?**  
The current implementation is a deterministic rules engine. I would describe it honestly as AI-assisted product direction with rule-based analysis today. A future language-model layer should explain verified evidence, not invent diagnoses.

**What is the biggest security concern?**  
The backend is an unauthenticated gateway to cluster data using whatever permissions its Kubernetes identity has. Authentication, application authorisation, and least-privilege RBAC are essential before broader deployment.

**What would you fix first?**  
Correctness: fix the API contract mismatch, namespace resource identities, unknown failure handling, and tests. Security and production architecture should be built on correct behaviour.

## 28. What This Project Proves

PlatformPilot proves practical understanding of:

- React routing, state, effects, filtering, and polling;
- API design with FastAPI;
- Kubernetes client authentication and resource APIs;
- pods, deployments, nodes, namespaces, events, logs, and conditions;
- container packaging;
- operational diagnosis and recommendation design;
- the difference between a working demo and a production platform.

The most valuable lesson is that platform engineering connects software development with safe operations. A useful interface is only one part of the system; identity, permissions, evidence, failure handling, contracts, testing, and observability determine whether the tool can be trusted.

## 29. Personal Mastery Checklist

You should be able to answer these without memorising the README:

- [ ] Draw the request path from browser to Kubernetes API.
- [ ] Explain why FastAPI exists between React and Kubernetes.
- [ ] Explain what kubeconfig contains and why it is sensitive.
- [ ] Distinguish pod phase from container waiting or terminated reason.
- [ ] Explain desired, ready, and available deployment replicas.
- [ ] Explain capacity versus allocatable node resources.
- [ ] Explain why events and logs are complementary.
- [ ] Describe exactly how the rules engine works.
- [ ] Explain why the current fallback can misclassify failures.
- [ ] Identify the AI Summary API-contract bug.
- [ ] Explain why pod name without namespace is insufficient.
- [ ] Describe the current authentication and RBAC risk.
- [ ] Explain polling and its scaling trade-off.
- [ ] Propose unit, API, frontend, and integration tests.
- [ ] Separate what is working today from what is planned.

## 30. Related Handbook Chapters

- [Cloud Computing Fundamentals](../01-Cloud-Fundamentals/Chapter-01-Cloud-Computing.md)
- [Linux Fundamentals](../02-Linux/Chapter-02-Linux.md)
- [Docker Fundamentals](../03-Docker/Chapter-03-Docker.md)
- [Kubernetes Fundamentals](../04-Kubernetes/Chapter-04-Kubernetes.md)
- [Handbook Writing Guide](../HANDBOOK-WRITING-GUIDE.md)
