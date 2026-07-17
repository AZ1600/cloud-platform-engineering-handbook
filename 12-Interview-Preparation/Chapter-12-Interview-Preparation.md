# Chapter 12 — Interview Preparation From My Projects

> The goal is not to memorise definitions. It is to explain concepts, prove where I used them, discuss trade-offs and be honest about limitations.

## 1. Answer Structure

Use:

```text
Definition -> project example -> implementation flow
-> decision/trade-off -> failure/lesson -> improvement
```

## 2. Tell Me About Yourself

> I am building toward cloud and platform engineering through hands-on projects. I have provisioned EKS with Terraform, deployed a FastAPI workload with Docker and Kubernetes, implemented GitOps with Argo CD, built observability with Prometheus/Grafana, created a Backstage developer portal and built operational applications such as PlatformPilot and CloudOps. I document the architecture, commands, security boundaries and lessons in my own engineering handbook so I can explain not only what I used, but why and how it works.

Adapt this to real employment history and the role; do not recite it mechanically.

## 3. Flagship Project: PlatformPilot

### Short answer

> PlatformPilot is a React/FastAPI Kubernetes operations dashboard. The backend uses the official Kubernetes Python Client to retrieve resources, events and logs; the frontend presents health and rule-based recommendations. It taught me API contracts, Kubernetes state, polling, kubeconfig/RBAC and the gap between a demo and production platform.

### Follow-ups to prepare

- Why use a client library rather than `kubectl`?
- How would in-cluster authentication work?
- Is the current analysis really AI?
- How would you secure and scale it?
- Which confirmed bug did you find and how would you test it?

Answers are developed in the [PlatformPilot case study](../projects/PlatformPilot.md).

## 4. AWS Questions

### EKS versus Lambda

EKS provides container/runtime control and Kubernetes portability but requires cluster/workload operations. Lambda reduces server management and scales per event but adds service limits, cold starts and AWS-specific integration. My two pharmacy projects demonstrate both models.

### SQS versus EventBridge

SQS durably buffers work for consumers; EventBridge routes events or schedules targets. My serverless pharmacy uses asynchronous low-stock processing, and content automation uses EventBridge scheduling.

### Least privilege

Grant each human, pipeline and workload only required actions/resources. Replace static pod credentials with workload identity and replace long-lived CI keys with OIDC roles.

## 5. Kubernetes Questions

### Deployment versus pod

A pod runs containers. A Deployment manages ReplicaSets, desired replicas and rolling updates. My Pharmacy Deployment requests two pods.

### Service and Ingress

The ClusterIP Service selects ready Pharmacy pods with labels. NGINX Ingress matches host/path and forwards to that Service.

### Troubleshooting

Inspect desired state, status, conditions, events, related resources, current/previous logs and node/network state. Explain ImagePullBackOff and CrashLoopBackOff from my project evidence.

## 6. Terraform Questions

Prepare state purpose/protection, plan versus apply, drift, modules, remote backend, provider locking and safe destroy. Connect every answer to the EKS dependency graph.

## 7. CI/CD and GitOps Questions

- CI validates and creates an immutable artifact.
- Delivery promotes it; deployment changes the environment.
- Argo CD reconciles Git desired state to live EKS state.
- OIDC provides temporary AWS credentials to GitHub Actions.
- Verification and rollback must include user/runtime evidence.

## 8. Observability Questions

Explain metrics, logs, traces and events; golden signals; SLI/SLO; alert actionability; Prometheus labels/cardinality; and how PlatformPilot combines events/logs.

## 9. Platform Engineering Questions

Explain platform as product, internal users, paved roads, self-service, Backstage catalogue, ownership, governance and success metrics. Emphasise the integrated workflow rather than listing tools.

## 10. AI Questions

Be precise: PlatformPilot currently uses deterministic rules. The resume analyser uses Bedrock/Nova Pro. Discuss grounding, hallucination, schemas, privacy, prompt injection, human approval and safe execution.

## 11. Behavioural STAR Method

- **Situation:** relevant context.
- **Task:** responsibility and desired outcome.
- **Action:** what I personally did and why.
- **Result:** evidence and lesson.

Do not invent production incidents or metrics. A learning-project debugging story is valid when labelled honestly.

## 12. Strong Project Stories

Prepare these evidence-based stories:

1. Diagnosing Kubernetes image/startup failures in Pharmacy EKS.
2. Finding PlatformPilot’s frontend/backend summary mismatch.
3. Comparing EKS and serverless Pharmacy architectures.
4. Creating GitOps reconciliation with Argo CD.
5. Building an approval boundary in CloudOps/OpsPilot.
6. Designing OAuth token storage and scheduling in Content Automation.

## 13. Questions to Ask the Interviewer

- Who are the platform’s users and biggest current pain points?
- How are infrastructure and application ownership divided?
- What does the deployment and rollback path look like?
- How are reliability and developer experience measured?
- What decisions would this role own in the first six months?

## 14. Honesty Rules

- Say “repository documented” when code was not deeply verified.
- Say “rule engine” instead of “AI” when that is accurate.
- Separate local/demo from production.
- Separate implemented from planned.
- Explain the contribution personally made.
- Never invent scale, availability, savings or users.

## 15. Practice Checklist

- [ ] I can give 30-second and two-minute explanations for each flagship project.
- [ ] I can draw architectures without notes.
- [ ] I can trace request/event flows.
- [ ] I can explain one decision and alternative per project.
- [ ] I can explain one failure and diagnostic method per project.
- [ ] I can identify security, reliability and cost responsibilities.
- [ ] I can state limitations confidently and propose priorities.
- [ ] I can answer behavioural questions with truthful evidence.

## Related Material

- [Architecture](../11-Architecture/Chapter-11-Architecture.md)
- [Project Register](../PROJECT-WORK-REGISTER.md)
- [Command Reference](../13-Command-Reference/Chapter-13-Commands.md)
