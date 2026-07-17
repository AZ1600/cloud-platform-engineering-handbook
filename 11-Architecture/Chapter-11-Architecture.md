# Chapter 11 — Architecture Through My Projects

> Architecture is the set of important structural decisions and trade-offs that shape a system. A diagram is useful only when I can explain why each boundary exists and what happens when it fails.

## 1. My Architecture Method

For every project, explain:

```text
users/problem -> functional and quality requirements -> components
-> request/data flow -> trust boundaries -> failure modes
-> observability -> deployment -> trade-offs -> evolution
```

## 2. Requirements Before Services

Functional requirements describe capabilities. Quality attributes describe security, availability, latency, scale, cost, operability and maintainability.

Do not begin with “I want to use Kubernetes.” Begin with the workload and constraints, then justify Kubernetes or another model.

## 3. PlatformPilot Architecture

```text
React -> FastAPI -> Kubernetes Python Client -> Kubernetes API
                   -> Prometheus HTTP API (documented current direction)
```

Strengths: clear frontend/backend boundary and structured Kubernetes API access. Current risks: unauthenticated backend, local kubeconfig, mixed namespace scope, polling load and limited rule analysis.

## 4. EKS Pharmacy Architecture

```text
Client -> Ingress -> ClusterIP Service -> FastAPI pods
                                      -> DynamoDB/EventBridge/SQS
Image pipeline -> ECR -> EKS nodes
```

Kubernetes gives workload control and portability; it adds cluster, identity, networking and rollout responsibility.

## 5. Serverless Pharmacy Architecture

```text
Client -> Cognito identity -> API Gateway -> Lambda -> DynamoDB
                                              -> SQS consumer
                                              -> EventBridge consumer
```

This reduces server/cluster operations and fits event-driven work. It adds managed-service coupling, asynchronous consistency, retry/idempotency requirements and service-specific cost behaviour.

## 6. Comparing the Two Pharmacy Designs

| Concern | EKS version | Serverless version |
|---|---|---|
| Runtime control | High | Lower/managed |
| Scaling | Kubernetes configuration | Lambda/service-managed |
| Idle cost | Cluster/nodes may continue | Mostly usage based |
| Portability | Container/Kubernetes oriented | AWS service oriented |
| Operations | Cluster and workload | Functions/events/service limits |
| Best learning value | Kubernetes platform operations | Event-driven managed architecture |

Neither is universally better. The requirement determines the trade-off.

## 7. OpsPilot and CloudOps

Both use dashboard/API/data layers plus approval workflows. OpsPilot centres business operations and multi-tenancy; CloudOps centres infrastructure signals, ownership and remediation.

The shared safety pattern is:

```text
signal -> recommendation -> authorised approval -> narrow execution -> audit
```

## 8. Content Automation

```text
Browser -> API Gateway -> Lambda -> DynamoDB/Secrets Manager
EventBridge schedule -> publisher Lambda -> X API -> activity state
```

Key architecture concerns are OAuth security, rate limits, retries, duplicate publishing, schedule correctness and failure visibility.

## 9. State and Consistency

Identify system of record, transient state and derived views. Asynchronous workflows are eventually consistent. Use idempotency keys, conditional writes and explicit state transitions where duplicate processing is possible.

## 10. Availability and Failure Domains

Redundancy must cross the failure domain that matters. Two pods on one node do not protect against node loss. Multi-AZ infrastructure does not protect against an application bug deployed everywhere.

Design graceful degradation and define recovery priorities.

## 11. Security Architecture

Draw trust boundaries:

- external user to application;
- application to database/cloud API;
- CI to AWS;
- pod to Kubernetes/AWS;
- AI recommendation to executor.

At each boundary identify identity, authorisation, encryption, validation, audit and failure behaviour.

## 12. Data Architecture

Choose storage from access, consistency, query, retention and recovery needs. DynamoDB design begins with access patterns; PostgreSQL supports relational constraints and flexible querying; local JSON is convenient development state, not a production multi-instance database.

## 13. Architecture Decision Records

Record context, decision, alternatives, consequences and status. Example decisions:

- EKS versus Lambda;
- polling versus streaming;
- rules versus LLM analysis;
- GitOps versus pipeline-direct deployment;
- static credentials versus workload identity.

## 14. Architecture Review Checklist

- [ ] User and problem are explicit.
- [ ] Current and planned architecture are separated.
- [ ] Request/event flow is traceable.
- [ ] Identity and permissions are shown.
- [ ] Data ownership and consistency are defined.
- [ ] Failure, retry and recovery are described.
- [ ] Observability supports the failure modes.
- [ ] Deployment and rollback are understood.
- [ ] Cost drivers are identified.
- [ ] Decisions and alternatives are recorded.

## 15. Interview Explanation Formula

> The problem was __. The main requirements were __. I separated the system into __ because __. A request flows __. The main security boundary is __. The biggest failure risk is __ and I detect/recover using __. I chose __ over __ because __. In the next version I would __.

## Related Material

- [Project Index](../projects/README.md)
- [Technology-to-Project Map](../TECHNOLOGY-PROJECT-MAP.md)
