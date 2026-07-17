# Technology-to-Project Evidence Map

This is the bridge between what I learn and what I build. It prevents me from listing a technology without understanding where I used it, why I used it, and what engineering responsibility came with it.

## How to Read This Map

For every technology I claim, I should be able to explain five things:

1. **Definition:** What is it?
2. **Problem:** What problem does it solve?
3. **Project evidence:** Where did I use it?
4. **Implementation:** How does data or control flow through it?
5. **Trade-off:** Why was it appropriate, and what alternative could I have used?

## AWS and Cloud Services

| Technology | Where I used it | What it does in my project | What I must be able to explain |
|---|---|---|---|
| Amazon EKS | Pharmacy API, Terraform EKS, Argo CD GitOps | Runs Kubernetes workloads on AWS | Managed control plane, worker nodes, networking, IAM, Kubernetes RBAC, cost and operational responsibility |
| Amazon ECR | Pharmacy API, CI/CD Pipeline | Stores versioned container images | Registry authentication, repository, image tags, push/pull flow, scanning and immutable releases |
| AWS Lambda | Cloud-Native Pharmacy, AI Content Automation | Runs event-driven application functions without managing servers | Invocation, execution role, timeout, memory, concurrency, retries, cold starts and idempotency |
| API Gateway | Cloud-Native Pharmacy, AI Content Automation | Exposes HTTP endpoints in front of Lambda | Routes, methods, authentication, validation, throttling, CORS and error responses |
| DynamoDB | Pharmacy API, Cloud-Native Pharmacy, AI Content Automation | Stores drug, tenant, plan, queue and activity data | Partition keys, sort keys, access patterns, conditional writes, consistency, indexes and hot partitions |
| Amazon SQS | Pharmacy API, Cloud-Native Pharmacy | Buffers asynchronous work and low-stock processing | Visibility timeout, retries, dead-letter queues, duplicate delivery and idempotent consumers |
| EventBridge | Pharmacy API, Cloud-Native Pharmacy, AI Content Automation | Routes domain events or triggers scheduled publishing | Event buses, rules, targets, schedules, retry behaviour and loose coupling |
| Secrets Manager | AI Content Automation | Protects OAuth credentials and tokens | Encryption, IAM access, rotation, retrieval and avoiding secrets in code or logs |
| Amazon Cognito | Cloud-Native Pharmacy | Authenticates users and supplies JWT identity | User pools, tokens, claims, authorisation and tenant identity |
| CloudWatch | Pharmacy projects | Provides AWS logs and monitoring | Log groups, metrics, alarms, retention and the difference between logs and metrics |
| AWS Bedrock | AI Resume Analyzer | Runs Amazon Nova Pro for résumé analysis | Model invocation, prompt input, output validation, privacy, cost and hallucination risk |
| AWS SAM | Cloud-Native Pharmacy, AI Content Automation | Defines and deploys serverless resources as code | Template structure, build/package/deploy flow, CloudFormation and environment configuration |
| IAM | All AWS projects | Controls which identities can perform which AWS actions | Principal, action, resource, effect, least privilege, trust policies and temporary credentials |

## Kubernetes and Containers

| Technology | Where I used it | What it does in my project | What I must be able to explain |
|---|---|---|---|
| Kubernetes API | PlatformPilot | Supplies pod, deployment, node, namespace, event and log data | API server, authentication, authorisation, resource objects and client libraries |
| Pods | PlatformPilot, Pharmacy API | Run one or more application containers | Pod lifecycle, phase versus container state, restart behaviour and ephemeral identity |
| Deployments | PlatformPilot, Pharmacy API, Argo CD | Maintain desired application replicas and rolling updates | Desired, ready and available replicas; ReplicaSets; rollout and rollback |
| Services | Pharmacy API, Argo CD | Give changing pods a stable network endpoint | Selectors, ClusterIP, ports, DNS and load balancing |
| Namespaces | PlatformPilot | Organise resources and provide a policy boundary | Namespaced versus cluster resources, naming, RBAC and quotas |
| Kubernetes events | PlatformPilot | Explain scheduler and controller observations | Why events help diagnosis, their temporary nature and how they differ from application logs |
| RBAC | Required by PlatformPilot and EKS projects | Limits Kubernetes API permissions | Role, ClusterRole, RoleBinding, ServiceAccount and least privilege |
| Docker images | PlatformPilot backend, Pharmacy API, CI/CD | Package code, runtime and dependencies | Image layers, Dockerfile, build context, tags, registry and security scanning |
| Docker Compose | Observability, AI Resume Analyzer | Runs multiple local containers together | Services, networks, volumes, environment variables and development versus production use |

## Platform Engineering and Delivery

| Technology or pattern | Where I used it | What it does | What I must be able to explain |
|---|---|---|---|
| GitHub Actions | CI/CD Pipeline, CloudOps, OpsPilot | Automates validation, builds and publication | Trigger, job, runner, step, secret/OIDC, artifact, failure and environment approval |
| Argo CD | GitOps project | Reconciles Git-defined Kubernetes state into EKS | Desired versus live state, sync, drift, health, pruning, self-healing and rollback |
| Terraform | Terraform EKS | Defines AWS and EKS infrastructure declaratively | Provider, resource, module, variable, output, state, plan, apply, drift and destroy |
| Backstage | Developer Portal | Provides a software catalogue and developer platform interface | Entities, ownership, catalog descriptors, TechDocs, plugins and software templates |
| Service catalogue | Backstage, CloudOps | Records services, owners and operational metadata | Ownership, metadata quality, lifecycle, dependencies and governance |
| Approval gates | CloudOps, OpsPilot | Keep recommendations separate from execution | Authorisation, auditability, safe previews, rejection and rollback |
| Multi-tenancy | OpsPilot, Cloud-Native Pharmacy | Separates data and permissions between customers | Tenant identity, data isolation, access checks and noisy-neighbour risk |

## Observability

| Technology | Where I used it | What it does | What I must be able to explain |
|---|---|---|---|
| Prometheus | Observability project | Scrapes and stores labelled time-series metrics | Targets, exporters, labels, PromQL, scrape interval, retention and cardinality |
| Grafana | Observability project | Queries data sources and displays dashboards | Data source, panel, dashboard, variables and the difference between visualisation and alerting |
| Application logs | PlatformPilot, Pharmacy API | Record runtime events and errors | Structured logs, severity, timestamps, correlation, retention and sensitive-data handling |
| Health checks | PlatformPilot, Pharmacy API, OpsPilot | Indicate process or dependency health | Liveness versus readiness, dependency checks and avoiding false-positive health |
| Audit history | CloudOps, OpsPilot | Records decisions and operational actions | Actor, action, target, time, outcome, immutability and investigation value |

## AI and Automation

| Technology or pattern | Where I used it | What it does | What I must be able to explain |
|---|---|---|---|
| Deterministic rules | PlatformPilot, OpsPilot local classifier | Maps known signals to predictable outputs | Why rules are explainable, how fallbacks work and how rules are tested |
| LLM analysis | AI Resume Analyzer; optional boundaries in OpsPilot | Generates natural-language analysis from structured context | Prompt design, grounding, validation, privacy, cost and hallucinations |
| n8n | AI Resume Analyzer | Orchestrates parsing, scoring, model calls and output | Nodes, data passing, credentials, error paths and reproducible workflow exports |
| Human approval | CloudOps, OpsPilot | Prevents automatic execution of unverified recommendations | Human-in-the-loop design, permissions, evidence, audit and failure recovery |
| OAuth | AI Content Automation; Gmail foundation in OpsPilot | Delegates access to external accounts without sharing passwords | Authorisation code flow, redirect URI, scopes, state, access token, refresh token and secure storage |

## Full Project Explanation Formula

When explaining any project, use this sequence:

```text
Problem
  -> user and desired outcome
  -> architecture
  -> request/data flow
  -> technology choices
  -> security boundary
  -> failure modes
  -> observability
  -> delivery method
  -> trade-offs
  -> lessons and next version
```

## Example: “I Used SQS”

Weak answer:

> I used SQS in my pharmacy project.

Strong answer:

> In my cloud-native pharmacy platform, an inventory update can create a low-stock event. I use SQS to decouple the API request from background processing so the caller does not wait for the alert workflow. The queue buffers work and allows the consumer to retry failures. Because SQS can deliver a message more than once, the consumer must be idempotent. A dead-letter queue captures messages that repeatedly fail so they can be investigated without blocking successful work.

The strong answer proves understanding of the service, the project flow, and the operational trade-off.

## Evidence Levels

Use these labels while writing chapters:

- **Code verified:** confirmed directly in application or infrastructure files.
- **Repository documented:** stated in the repository README and awaiting deeper code verification.
- **Demonstrated:** supported by screenshots, test results, deployment output, or a running system.
- **Planned:** a future improvement; never present it as implemented.
