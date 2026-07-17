# Chapter 4 — Kubernetes Through My Projects

> Kubernetes runs and coordinates containers. In my projects, it hosts the Pharmacy API, supplies operational data to PlatformPilot, receives GitOps changes from Argo CD, and runs on AWS through Amazon EKS.

**Evidence used:** PlatformPilot application code, Pharmacy API Kubernetes manifests, Argo CD manifests, and repository documentation reviewed on 2026-07-11.

## Learning Objectives

By the end of this chapter, I should be able to:

- explain Kubernetes in simple and technical language;
- describe the control plane, worker nodes, kubelet and container runtime;
- explain declarative desired state and reconciliation;
- distinguish containers, pods, ReplicaSets and Deployments;
- explain Services, DNS, Ingress and request routing;
- describe labels, selectors, namespaces and resource identity;
- explain liveness, readiness and startup probes;
- describe ConfigMaps, Secrets, ServiceAccounts and RBAC;
- explain how Amazon EKS changes the responsibility model;
- trace a request through my Pharmacy API deployment;
- trace a monitoring request through PlatformPilot;
- explain how Argo CD implements GitOps;
- diagnose common Kubernetes failures;
- identify the production gaps in my current manifests;
- answer interview questions using evidence from my projects.

## 1. Why Kubernetes Exists

Docker packages an application into an image and runs it as a container. That solves application portability, but it does not by itself answer operational questions such as:

- Which machine should run the container?
- What happens if the container crashes?
- How do I run several copies?
- How do users find containers when their addresses change?
- How do I update the application without stopping all traffic?
- How do I store configuration and credentials?
- How do I determine whether a new instance is ready?
- How do I declare and enforce CPU or memory limits?

Kubernetes is an orchestration system that answers those questions.

### Simple explanation

Imagine managing a delivery fleet. Docker builds identical delivery vans. Kubernetes decides how many vans should operate, where they should go, replaces broken vans, routes work to available vans, and rolls out a new model gradually.

### Technical explanation

Kubernetes is a declarative container-orchestration platform. Users submit resource definitions to the Kubernetes API. Controllers continuously compare desired state with observed state and take action to reduce the difference.

```text
Desired state: 2 Pharmacy API replicas
Observed state: 1 healthy replica
Difference: 1 missing replica
Controller action: create another pod
```

This continuous control loop is called reconciliation.

## 2. Kubernetes Architecture

```text
Engineer, CI/CD or Argo CD
            |
            v
      Kubernetes API server
            |
     +------+------------------+
     |                         |
     v                         v
Cluster state store       Controllers and scheduler
     |                         |
     +------------+------------+
                  |
                  v
            Worker nodes
       +----------+----------+
       |                     |
     kubelet          container runtime
       |                     |
       +----------+----------+
                  v
                 Pods
```

### API server

The API server is the front door of the cluster. `kubectl`, Terraform, Argo CD, and PlatformPilot’s Kubernetes Python Client all communicate with it.

The API server authenticates an identity, authorises the requested action, validates the resource, and makes the desired state available to the rest of Kubernetes.

### State store

Kubernetes stores cluster state in etcd. This includes resource definitions and status data. etcd is critical control-plane data and requires protection, backup, encryption, and restricted access.

### Scheduler

The scheduler chooses a node for a pod that has not yet been assigned. It considers requested resources, constraints, affinity, taints, tolerations and other scheduling rules.

### Controllers

Controllers reconcile resources. A Deployment controller manages ReplicaSets; a ReplicaSet maintains the required pod count; node and job controllers handle their own resource types.

### Kubelet

The kubelet runs on each worker node. It watches assigned pod specifications and works with the container runtime to start and monitor containers.

### Container runtime

The runtime pulls images and runs containers. Modern Kubernetes commonly uses containerd or CRI-O through the Container Runtime Interface.

## 3. Amazon EKS and the Responsibility Model

Amazon Elastic Kubernetes Service is a managed Kubernetes service. AWS operates the Kubernetes control plane. I still own significant parts of the platform:

| AWS manages | I manage |
|---|---|
| Control-plane infrastructure | Workload manifests and application images |
| Control-plane availability | Worker capacity or selected compute model |
| Control-plane patching | Kubernetes version planning and add-on compatibility |
| Managed API endpoint | IAM, Kubernetes RBAC and workload identity |
| etcd operation for the managed control plane | VPC design, network exposure and security controls |
| Control-plane scaling | Resource requests, limits, probes and autoscaling |

Managed does not mean responsibility-free. EKS removes control-plane operations, but application and platform engineering remain my responsibility.

## 4. From Image to Running Application

The Pharmacy API follows this chain:

```text
FastAPI source
  -> Docker build
  -> container image
  -> Amazon ECR repository
  -> Deployment references image
  -> node pulls image
  -> container starts inside a pod
  -> readiness probe succeeds
  -> Service can route traffic to the pod
```

Each stage creates a different failure possibility. A build can fail, ECR authentication can fail, a tag can be wrong, the node can lack network access, the process can crash, or the application can start but never become ready.

## 5. Pods

A pod is Kubernetes’ smallest deployable unit. It contains one or more containers that share:

- a network namespace and IP address;
- localhost communication;
- attached volumes;
- lifecycle and scheduling placement.

The Pharmacy API pod contains one application container. PlatformPilot reads pod metadata, phase, container state, logs and events through the Kubernetes API.

### Pod phase versus container state

A pod phase is broad: `Pending`, `Running`, `Succeeded`, `Failed` or `Unknown`. A container can be waiting with `ImagePullBackOff` or `CrashLoopBackOff` while the pod’s broad phase is less informative.

PlatformPilot improves the display by checking the first container’s waiting or terminated reason. It should eventually inspect all init and application containers.

### Pods are replaceable

A pod is not a permanent server. Deployments replace pods, and replacement pods receive new identities and usually new IP addresses. Applications should not depend on one pod name or IP remaining stable.

## 6. Deployments and ReplicaSets

The Pharmacy manifest declares:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pharmacy-api
spec:
  replicas: 2
```

This states that two application replicas should exist.

```text
Deployment pharmacy-api
        |
        v
     ReplicaSet
      /      \
     v        v
   Pod 1    Pod 2
```

The Deployment manages rollout history and creates ReplicaSets. The active ReplicaSet maintains the desired pod count.

### Desired, ready and available

- **Desired replicas:** how many the specification requests.
- **Ready replicas:** how many pass readiness checks.
- **Available replicas:** how many have been ready for the required availability period.

PlatformPilot marks a Deployment healthy when desired, ready and available are equal.

### Why two replicas matter

Two replicas can reduce the effect of one pod failure and permit rolling updates without stopping every instance. This does not guarantee high availability if both pods run on one failing node or in one failure domain. Pod anti-affinity or topology-spread constraints can distribute replicas.

## 7. Labels and Selectors

The Pharmacy Deployment gives each pod this label:

```yaml
labels:
  app: pharmacy-api
```

The Deployment selector and Service selector both match that label.

```text
Service selector app=pharmacy-api
                  |
          +-------+-------+
          v               v
   matching Pod 1   matching Pod 2
```

Labels create relationships without hardcoding pod names. If labels and selectors do not match, pods may run correctly while the Service has no endpoints.

PlatformPilot also converts a Deployment’s `matchLabels` into a selector string to find related pods. A more exact implementation can additionally follow Kubernetes owner references.

## 8. Services

Pods are replaceable, so clients need a stable address. A Kubernetes Service provides stable discovery and load distribution across matching ready pods.

The Pharmacy Service declares:

```yaml
kind: Service
spec:
  selector:
    app: pharmacy-api
  ports:
    - port: 8000
      targetPort: 8000
  type: ClusterIP
```

- `port` is the port exposed by the Service.
- `targetPort` is the port used by the application container.
- `ClusterIP` makes the Service reachable inside the cluster.

The Service does not start containers. It discovers matching ready pods and provides a stable virtual IP and DNS name.

## 9. Ingress

The Pharmacy Ingress declares the host `pharmacy.local`, matches requests beginning with `/`, and forwards them to the Service on port 8000.

```text
Client request for pharmacy.local
  -> Ingress controller
  -> Ingress rule
  -> pharmacy-api-service:8000
  -> ready Pharmacy API pod:8000
```

An Ingress resource is only configuration. An Ingress controller must be installed to implement it. The manifest selects the NGINX ingress class.

On AWS, an alternative is the AWS Load Balancer Controller, which can provision an Application Load Balancer. The correct choice depends on requirements, cost, existing platform standards and desired AWS integration.

## 10. Health Probes

The Pharmacy Deployment uses HTTP liveness and readiness probes against `/` on port 8000.

### Liveness

Liveness asks whether the container should be restarted. Repeated liveness failure causes kubelet to restart it.

### Readiness

Readiness asks whether the pod should receive traffic. Failure removes the pod from Service endpoints without necessarily restarting it.

### Startup

A startup probe is useful for slow-starting applications. Until it succeeds, liveness and readiness timing does not punish a legitimate long startup.

### Project improvement

Using `/` can prove that the HTTP process responds, but a dedicated endpoint makes intent clearer:

```text
/live  -> process is functioning
/ready -> required startup and dependency conditions are satisfied
```

A readiness endpoint should be designed carefully. If every transient dependency problem makes all replicas unready, the Service may remove every endpoint and create a larger outage.

## 11. Configuration and Secrets

The Pharmacy manifest provides `TABLE_NAME` and `AWS_DEFAULT_REGION` directly as environment values. It mounts a Kubernetes Secret called `aws-credentials` at `/root/.aws`.

### ConfigMap

A ConfigMap stores non-secret configuration such as feature flags, endpoints or ordinary environment settings.

### Secret

A Kubernetes Secret stores sensitive values in a resource intended for controlled access. Base64 encoding is not encryption. Secrets still require RBAC, encryption at rest, secure delivery and careful log handling.

### Important project lesson

Mounting long-lived AWS credentials into a pod creates rotation and exposure risk. On EKS, workload identity should normally use EKS Pod Identity or IAM Roles for Service Accounts so the pod obtains temporary credentials for a narrowly scoped IAM role.

The identity chain should become:

```text
Pod -> Kubernetes ServiceAccount -> trusted AWS workload identity
    -> temporary credentials -> permitted AWS resources only
```

## 12. ServiceAccounts and RBAC

Kubernetes authentication answers “who are you?” Authorisation answers “may you perform this action?”

- A ServiceAccount is a workload identity inside Kubernetes.
- A Role defines permissions within a namespace.
- A ClusterRole defines reusable or cluster-scoped permissions.
- A RoleBinding grants a Role or ClusterRole in one namespace.
- A ClusterRoleBinding grants cluster-wide access.

PlatformPilot needs read access to selected resources and pod logs. Its current code also lists nodes, namespaces and Secrets counts, which expands the required permissions.

A production design should begin with the user experience and grant only required verbs and resources. Avoid granting `cluster-admin` simply because it makes development easier.

## 13. Namespaces

Namespaces organise namespaced resources and support policy, quota and access boundaries. They are not full security isolation by themselves.

The current Pharmacy and Argo CD manifests do not declare a namespace, so `kubectl apply` places them in the active/default namespace unless another namespace is supplied.

PlatformPilot mixes scopes:

- some list routes read only `default`;
- the cluster summary reads all namespaces;
- pod events and logs use only the default namespace;
- node and namespace routes are cluster-wide.

Because identical pod names can exist in different namespaces, production routes should identify both namespace and name.

## 14. Kubernetes Networking

The normal request path is:

```text
External client
  -> load balancer or Ingress endpoint
  -> Ingress controller
  -> ClusterIP Service
  -> ready pod IP
  -> containerPort 8000
```

Important concepts:

- Every pod receives cluster networking.
- A Service selects endpoints using labels.
- Cluster DNS resolves Service names.
- NetworkPolicy can restrict allowed pod traffic when supported by the network plugin.
- Ingress handles HTTP routing but does not replace all network-security controls.

## 15. Resource Requests and Limits

The reviewed Pharmacy and Argo CD example Deployments do not declare CPU or memory requests and limits.

- A request influences scheduling and represents expected resource need.
- A limit sets a maximum enforced by the runtime.

Without requests, the scheduler lacks useful placement information. Without limits, a container may consume excessive resources. Poorly selected memory limits can cause `OOMKilled`, which PlatformPilot recognises.

Requests and limits should be chosen from measured workload behaviour, not copied blindly.

## 16. Image Management

The Pharmacy Deployment references an ECR image ending in `:latest` and uses `imagePullPolicy: IfNotPresent`. The Argo CD example also uses `nginx:latest`.

This combination can produce stale or ambiguous deployments:

- `latest` can point to different content over time;
- `IfNotPresent` can reuse an older local image;
- a manifest does not identify the exact release;
- rollback and audit become harder.

Prefer an immutable version or digest:

```yaml
image: repository/pharmacy-api:1.2.3
```

or:

```yaml
image: repository/pharmacy-api@sha256:<digest>
```

CI should build, test, scan, publish and record the exact image. GitOps should deploy that immutable reference.

## 17. GitOps with Argo CD

The Argo CD project stores an NGINX Deployment and Service in GitHub.

```text
Engineer changes manifest
  -> commit and push
  -> Argo CD observes Git revision
  -> compares desired state with live EKS state
  -> synchronises approved difference
  -> reports health and sync status
```

GitOps provides version-controlled desired state, visible changes, drift detection and repeatability. It does not automatically make every change safe. Validation, review, secret management, promotion and rollback design are still required.

### Key Argo CD concepts

- **Application:** connects a source repository/path to a target cluster/namespace.
- **Desired state:** manifests stored at the selected Git revision.
- **Live state:** resources currently observed in the cluster.
- **Sync:** action that reconciles live state toward desired state.
- **OutOfSync:** live and desired state differ.
- **Health:** Argo CD’s assessment of resource operation.
- **Prune:** delete resources removed from Git.
- **Self-heal:** reverse unauthorised or accidental live drift.

## 18. PlatformPilot’s Kubernetes Integration

PlatformPilot uses the official Python client, not shell commands. At module import, it calls `load_kube_config()`, then creates CoreV1 and AppsV1 clients.

```text
React page
  -> FastAPI endpoint
  -> kubernetes_client.py
  -> authenticated Kubernetes API request
  -> simplified Python dictionary
  -> JSON response
  -> dashboard table or analysis card
```

This design is better than parsing `kubectl` text because the client returns structured resource objects. For in-cluster deployment, local kubeconfig should be replaced with in-cluster configuration and a restricted ServiceAccount.

See the [complete PlatformPilot case study](../projects/PlatformPilot.md) for endpoint, security, contract and scaling details.

## 19. Common Failure States

### ImagePullBackOff and ErrImagePull

Kubernetes cannot retrieve the image. Check:

- image name and tag;
- whether the image exists in ECR;
- node or workload registry permissions;
- registry connectivity;
- architecture compatibility.

### CrashLoopBackOff

The container starts and repeatedly exits. Check:

- current and previous logs;
- command and entry point;
- environment variables and mounted files;
- dependency connectivity;
- probe configuration;
- application exceptions.

### OOMKilled

The container exceeded its memory limit. Check actual memory behaviour, leaks, concurrency and limit choice before simply increasing the limit.

### Pending

The pod cannot yet run. Check scheduler events, resource requests, node capacity, selectors, taints, volumes and quotas.

### Service has no endpoints

Check that Service selectors match pod labels and that pods are Ready.

### Ingress returns an error

Check DNS/host matching, controller presence, ingress class, Service name and port, endpoints, controller logs and network controls.

## 20. My Kubernetes Troubleshooting Method

Use evidence in layers:

```text
Desired resource
  -> observed status
  -> conditions
  -> events
  -> related resources
  -> current and previous logs
  -> node and network state
```

Useful commands:

```bash
kubectl get pods -A
kubectl describe pod <pod> -n <namespace>
kubectl logs <pod> -n <namespace>
kubectl logs <pod> -n <namespace> --previous
kubectl get deployment <name> -n <namespace>
kubectl rollout status deployment/<name> -n <namespace>
kubectl get service,endpoints -n <namespace>
kubectl get events -n <namespace> --sort-by=.metadata.creationTimestamp
kubectl auth can-i list pods --as=system:serviceaccount:<namespace>:<service-account>
```

Commands provide evidence; they should not replace understanding of the resource relationship.

## 21. Production Review of My Pharmacy Manifests

### What is already demonstrated

- Deployment with two replicas.
- ECR-hosted application image.
- container port 8000.
- liveness and readiness probes.
- ClusterIP Service with label selection.
- NGINX Ingress routing.
- AWS region and table configuration.
- Kubernetes Secret volume mounting.

### What I would improve

- Replace `:latest` with an immutable release tag or digest.
- Replace static credential mounting with EKS workload identity.
- Use a non-root container and pod security context.
- Add measured CPU and memory requests and limits.
- Add dedicated liveness, readiness and possibly startup endpoints.
- Use ConfigMaps or deployment configuration for non-secret values.
- Remove the unrelated hardcoded table name and use environment-specific configuration.
- Declare a namespace and ServiceAccount.
- Add RBAC, NetworkPolicy, disruption budget and topology spread where required.
- Define rollout behaviour and rollback evidence.
- Add TLS and a production DNS/load-balancer strategy.
- Validate manifests in CI.

## 22. Interview Questions and Answers

### What problem does Kubernetes solve?

Kubernetes schedules and operates containerised workloads. It maintains desired replica count, replaces failed pods, provides service discovery, manages rolling updates, injects configuration, applies resource and security policy, and exposes workload state through an API.

### What is the difference between a pod and a Deployment?

A pod is the running unit containing one or more containers. A Deployment is a higher-level controller that manages ReplicaSets, desired pod count and rolling application updates. In my Pharmacy API, the Deployment requests two pods and replaces them when needed.

### How does traffic reach the Pharmacy API?

The client matches the Ingress host and path. The NGINX Ingress controller forwards the request to the ClusterIP Service on port 8000. The Service selects Ready pods with `app: pharmacy-api` and forwards traffic to their container port 8000.

### What is the difference between liveness and readiness?

Liveness determines whether kubelet should restart a container. Readiness determines whether a pod should receive Service traffic. My Pharmacy manifest uses HTTP probes for both, but I would replace the generic root path with endpoints designed for their separate meanings.

### How should an EKS pod access AWS services?

Prefer a workload identity such as EKS Pod Identity or IAM Roles for Service Accounts. Map a Kubernetes ServiceAccount to a narrowly scoped IAM role and use temporary credentials. My current Pharmacy manifest mounts static credentials, which I would replace before production.

### How does PlatformPilot access Kubernetes?

The FastAPI backend uses the official Kubernetes Python Client. Locally it loads kubeconfig and calls CoreV1 and AppsV1 APIs. In Kubernetes, I would use in-cluster configuration and least-privilege RBAC.

### What does Argo CD add?

Argo CD continuously compares Git-defined desired state with live cluster state. It exposes drift and can synchronise approved changes. My GitOps project uses GitHub manifests, Argo CD and EKS to demonstrate that reconciliation path.

## 23. Practical Labs Based on My Projects

### Lab 1 — Trace the Pharmacy request

Draw and then verify the path from Ingress to Service endpoints to pods. Explain every port and selector.

### Lab 2 — Create an image failure

Change a test Deployment to a nonexistent tag. Observe pod state, events and PlatformPilot output. Restore an immutable valid tag.

### Lab 3 — Test readiness

Make the readiness endpoint fail without terminating the process. Observe Service endpoints and compare this with a liveness failure.

### Lab 4 — Verify RBAC

Create a read-only ServiceAccount for a test namespace. Use `kubectl auth can-i` to prove allowed and denied operations.

### Lab 5 — Demonstrate GitOps drift

Change a managed resource manually, observe Argo CD OutOfSync state, and explain the result before synchronising or self-healing.

### Lab 6 — Replace AWS credentials

Design the transition from the mounted `aws-credentials` Secret to an EKS workload identity. Document the IAM trust and permission boundary.

## 24. Personal Mastery Checklist

- [ ] I can draw the Kubernetes control plane and worker-node components.
- [ ] I can explain reconciliation using my two-replica Pharmacy Deployment.
- [ ] I can distinguish pod phase and container state.
- [ ] I can trace traffic through Ingress, Service and pod.
- [ ] I can explain labels and selectors using my manifests.
- [ ] I can explain desired, ready and available replicas.
- [ ] I can explain liveness, readiness and startup probes.
- [ ] I can explain ConfigMaps, Secrets and why base64 is not encryption.
- [ ] I can explain ServiceAccounts, Roles and bindings.
- [ ] I can explain why static AWS credentials in a pod are risky.
- [ ] I can explain requests, limits and OOMKilled.
- [ ] I can explain why `latest` plus `IfNotPresent` is unreliable.
- [ ] I can describe Argo CD desired state, live state, sync and drift.
- [ ] I can explain exactly how PlatformPilot calls the Kubernetes API.
- [ ] I can diagnose ImagePullBackOff, CrashLoopBackOff, Pending and missing endpoints.
- [ ] I can separate what my manifests currently implement from production improvements.

## 25. Key Takeaways

- Kubernetes is a reconciliation system, not merely a place to run containers.
- Pods are replaceable; Deployments maintain desired application state.
- Services use labels to provide stable access to Ready pods.
- Ingress requires a controller and routes external HTTP traffic to Services.
- Probes have different meanings and must represent real application health.
- Kubernetes Secrets require permission and encryption controls; encoding is not protection.
- EKS manages the control plane, not my workload security or reliability.
- PlatformPilot demonstrates programmatic Kubernetes API access and also exposes why RBAC matters.
- Argo CD turns Git into desired state, but safe delivery still requires validation and governance.
- My current manifests prove real learning and also contain specific improvements I can explain honestly.

## Related Material

- [PlatformPilot complete case study](../projects/PlatformPilot.md)
- [Pharmacy API on EKS](../projects/Pharmacy-API-EKS.md)
- [GitOps with Argo CD](../projects/GitOps-ArgoCD.md)
- [Terraform AWS EKS Platform](../projects/Terraform-AWS-EKS-Platform.md)
- [Docker Fundamentals](../03-Docker/Chapter-03-Docker.md)
- [Technology-to-Project Evidence Map](../TECHNOLOGY-PROJECT-MAP.md)
