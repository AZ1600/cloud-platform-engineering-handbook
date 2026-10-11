# 01 — Kubernetes: from declared state to healthy traffic

**Goal:** explain why a running Pod does not necessarily mean a working service, and identify which controller or boundary to inspect.

## The API is the point of coordination

```text
kubectl / Argo CD / automation
           |
           v
       API server  <---- authentication + authorization + admission
           |
           +--> persisted desired state
           |
           +--> Deployment controller --> ReplicaSet --> Pod specifications
           |                                          |
           +--> scheduler ----------------------------+--> node selection
                                                      |
                                                  kubelet/runtime
                                                      |
                                                 readiness result
                                                      |
Service selector -> EndpointSlice controller --> eligible endpoints
```

Controllers **reconcile** desired and observed state; they do not promise immediate success. Scheduling, image pulls, process startup, readiness and routing are separate stages.

## Evidence from Pharmacy API on EKS

[Inspect its Deployment manifest](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml). It declares:

- Two desired replicas and rolling-update settings (`maxUnavailable: 0`, `maxSurge: 1`).
- A named ServiceAccount, non-root execution, restricted capabilities and a read-only root filesystem.
- Startup, readiness and liveness probes at `/health`.
- CPU/memory requests and limits, plus a topology-spread preference.

**What these settings do not guarantee:** two ready replicas at every instant, high availability across zones, database availability, correctly scoped IAM permissions, or completed deployment. `whenUnsatisfiable: ScheduleAnyway` is a preference rather than a hard placement rule.

## Read-only investigation sequence

Use these commands only on an authorised context. Replace `NAMESPACE` and `DEPLOYMENT` with actual values.

```bash
kubectl config current-context
kubectl -n NAMESPACE get deployments
kubectl -n NAMESPACE get deploy DEPLOYMENT -o wide
kubectl -n NAMESPACE describe deploy DEPLOYMENT
kubectl -n NAMESPACE get replicasets
kubectl -n NAMESPACE get pods -o wide
kubectl -n NAMESPACE get events --sort-by=.metadata.creationTimestamp
```

Follow the reference chain:

1. **Deployment:** desired vs updated, ready and available replicas. Is rollout stalled?
2. **ReplicaSet:** which revision created the current Pods?
3. **Pod:** scheduled? image pulled? container started? readiness passing?
4. **Service:** selector matches the Pod labels?
5. **EndpointSlices:** are ready backends published for that Service?

```bash
kubectl -n NAMESPACE get service SERVICE -o yaml
kubectl -n NAMESPACE get pods --show-labels
kubectl -n NAMESPACE get endpointslices \
  -l kubernetes.io/service-name=SERVICE -o wide
```

**Key distinction:** A Pod phase of `Running` means the Pod is bound to a node and has running container(s); it does not imply application readiness, successful authorization or working network access.

## Probe reasoning

| Probe | Question it answers | Common failure consequence |
|---|---|---|
| Startup | Has the process initialized within its allowed window? | Repeated restart after threshold |
| Readiness | May this Pod receive Service traffic now? | Endpoint withheld from ready backends |
| Liveness | Should Kubernetes restart the process? | Restart loop if too aggressive |

`/health` must reflect the contract intended for each probe. A single basic liveness endpoint can be inappropriate as a deep dependency check; an unavailable downstream service should not automatically trigger mass restart loops.

## Failure walkthrough: Pod is Running, Service fails

**Hypothesis A:** wrong `spec.selector` or Pod labels. Compare YAML; EndpointSlices may have no usable backends.

**Hypothesis B:** readiness is failing. Inspect the Pod description, readiness events, application logs and probe response.

**Hypothesis C:** traffic is blocked. Check network policy semantics, DNS and client source separately.

Write an incident note with **observation → hypothesis → validation → result → next action**. A log line by itself is evidence, not an established root cause.

## Knowledge check

1. Why can two desired replicas result in zero Service endpoints?
2. What changes first after `kubectl apply`: a controller's desired state, a Pod's readiness or traffic routing?
3. What is the operational cost of an incorrectly configured liveness probe?
4. Which field in the Pharmacy manifest shows that topology spreading is soft rather than mandatory?

**Code evidence:** [Pharmacy Deployment](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml) · [PlatformPilot Kubernetes client](https://github.com/AZ1600/platform-pilot/blob/main/backend/kubernetes_client.py) · [Argo CD Application](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/argocd/application.yaml).
