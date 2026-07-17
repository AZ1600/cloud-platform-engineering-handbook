# Chapter 5 — AWS Through My Projects

> AWS is the cloud platform behind my EKS, serverless pharmacy, content automation, CI/CD and AI workflow projects. This chapter explains each service through the job it performs in those systems.

**Evidence reviewed:** project READMEs, Kubernetes manifests, SAM configuration and CodeBuild specification as of 2026-07-17.

## Learning Objectives

I should be able to explain AWS accounts, Regions, Availability Zones, IAM, VPC networking, EKS, ECR, Lambda, API Gateway, DynamoDB, SQS, EventBridge, Cognito, Secrets Manager, CloudWatch, KMS, SAM and the shared-responsibility model using my own projects.

## 1. AWS in Simple Terms

AWS rents computing capabilities through APIs. Instead of buying servers, networking equipment and data-centre space, I declare or request services and pay for their use.

The important lesson is that “managed” does not mean “AWS handles everything.” AWS secures and operates the underlying cloud; I remain responsible for identities, permissions, application code, data, configuration, network exposure, monitoring and cost.

## 2. Where AWS Appears in My Portfolio

| Project | Main AWS services | Engineering purpose |
|---|---|---|
| Pharmacy API on EKS | EKS, ECR, DynamoDB, SQS, EventBridge, IAM, CloudWatch | Run and operate a containerised FastAPI workload |
| Terraform EKS | VPC, subnets, NAT, IAM, KMS, EKS, managed nodes | Provision a Kubernetes platform as code |
| Cloud-Native Pharmacy | Lambda, API Gateway, DynamoDB, Cognito, SQS, EventBridge, SAM | Build a multi-tenant serverless inventory system |
| Content Automation | Lambda, API Gateway, DynamoDB, EventBridge, Secrets Manager, SAM | Schedule and operate multi-account publishing |
| CI/CD Pipeline | IAM and ECR | Authenticate a pipeline and publish images |
| AI Resume Analyzer | Bedrock and IAM | Generate role-readiness analysis with Amazon Nova Pro |

## 3. Accounts, Regions and Availability Zones

An AWS account is a security, billing and resource boundary. A Region is a geographic AWS location such as `eu-west-2`. Availability Zones are isolated facilities within a Region.

My Pharmacy EKS manifests use `eu-west-2`; the Cloud-Native Pharmacy SAM configuration uses `us-east-1`. Region choice affects latency, service availability, data residency, cost and disaster-recovery design.

Before running a command, I should know the account and Region:

```bash
aws sts get-caller-identity
aws configure get region
```

These are recommended diagnostics. They do not prove that a deployment used a particular account unless the output is retained as evidence.

## 4. IAM — The Security Foundation

IAM decides who can perform which AWS action on which resource under which conditions.

```text
Principal + Action + Resource + Conditions -> Allow or Deny
```

Important objects:

- **User:** long-lived human or legacy programmatic identity.
- **Role:** assumable identity that supplies temporary credentials.
- **Policy:** JSON permission rules.
- **Trust policy:** defines who may assume a role.
- **Service role:** lets an AWS service act for a workload.

### IAM in my projects

- Terraform creates roles for EKS and worker nodes.
- GitHub Actions needs permission to push images to ECR.
- Lambda functions need execution roles for DynamoDB, SQS, EventBridge and Secrets Manager.
- Bedrock invocation requires model-access permissions.
- The Pharmacy EKS manifest currently mounts static AWS credentials; this should become EKS Pod Identity or IAM Roles for Service Accounts.

Least privilege means granting the smallest actions and resources required. It also means separating deployment permission from runtime permission.

## 5. VPC Networking

A VPC is a logically isolated AWS network. Subnets divide its address space. Route tables decide where traffic goes.

```text
Internet
  -> Internet Gateway
  -> public subnet resources

Private workload
  -> private subnet
  -> NAT Gateway for outbound internet access
```

The Terraform EKS project documents public and private subnets, an Internet Gateway, NAT Gateway and route tables. A common EKS design places worker nodes in private subnets while load balancers expose only approved entry points.

### Security groups

Security groups are stateful virtual firewalls attached to AWS resources. Rules should express required flows rather than broad “allow all” access.

### NAT trade-off

A NAT Gateway simplifies outbound access for private subnets but adds hourly and data-processing cost. VPC endpoints can keep supported AWS-service traffic private and reduce some NAT use.

## 6. Amazon EKS

EKS provides a managed Kubernetes control plane. AWS operates control-plane infrastructure; I manage workload manifests, worker capacity, access, networking choices, add-ons, observability and application reliability.

My EKS work connects:

```text
Terraform -> VPC/IAM/KMS/EKS/nodes
CI/CD -> ECR image
Kubernetes Deployment -> Pharmacy API pods
Service/Ingress -> application traffic
Argo CD -> Git-defined desired state
PlatformPilot -> Kubernetes operational visibility
```

See [Kubernetes Through My Projects](../04-Kubernetes/Chapter-04-Kubernetes.md) for the workload layer.

## 7. Amazon ECR

ECR stores container images. The Pharmacy Deployment references an ECR image in `eu-west-2`; the CI/CD project builds, tags and pushes an image to ECR.

```text
Source -> Docker build -> test/scan -> tag -> ECR push
      -> Kubernetes image pull -> running pod
```

I should use immutable release tags or digests instead of `latest`, enable scanning, restrict push/pull permissions and define image-retention rules.

## 8. AWS Lambda

Lambda runs functions in response to events without requiring me to manage servers.

I still configure:

- runtime, handler, memory and timeout;
- execution role and environment variables;
- networking and concurrency;
- retry and failure destinations;
- logging and alarms.

### In the Cloud-Native Pharmacy project

API Gateway invokes a Lambda for inventory operations. Low-stock work is processed asynchronously through SQS and EventBridge consumers.

### In Content Automation

Lambda functions implement OAuth, plan storage, queue operations, dashboard data and publishing. EventBridge schedules the publisher.

### Key failure concepts

Lambda can retry asynchronous events. SQS may redeliver. Functions must therefore be idempotent: processing the same event twice should not create an incorrect duplicate outcome.

## 9. API Gateway

API Gateway provides an HTTP entry point, routing requests to Lambda.

It can handle routes, stages, authentication integration, throttling, CORS and request/response mapping. It is not a substitute for application authorisation: the code must still ensure that the authenticated tenant may access the requested resource.

Content Automation exposes routes for OAuth, plans, queueing, publishing, activity and its dashboard. The route is only the entrance; Lambda, IAM, data access and error handling complete the request.

## 10. DynamoDB

DynamoDB is a managed key-value/document database. Good design starts from access patterns, not from copying relational tables.

The Cloud-Native Pharmacy README documents tenant isolation using:

```text
PK = TENANT#{tenant_id}
SK = DRUG#{drug_id}
```

The application must derive the tenant from trusted identity claims—not accept an arbitrary tenant ID from the request.

I should be able to explain partition keys, sort keys, conditional writes, indexes, consistency, throughput modes, hot partitions, backups and point-in-time recovery.

## 11. SQS

SQS is a managed message queue. It decouples the API from background work:

```text
Inventory update -> queue message -> consumer -> low-stock action
```

Important properties:

- messages are retained until deleted or expired;
- visibility timeout hides a message during processing;
- standard queues can deliver more than once;
- failed messages can move to a dead-letter queue;
- consumers must be idempotent.

SQS absorbs temporary spikes and dependency failures, but it creates eventual consistency: the background result may appear later than the API response.

## 12. EventBridge

EventBridge routes events using rules and can trigger schedules.

- Cloud-Native Pharmacy publishes low-stock events for loosely coupled consumers.
- Content Automation uses EventBridge to trigger scheduled publishing.

SQS emphasises durable work buffering; EventBridge emphasises routing events to interested targets. A design may use both because they solve different problems.

## 13. Cognito and OAuth

Cognito authenticates Cloud-Native Pharmacy users and issues JWTs. The application validates issuer, audience, signature and expiry, then authorises tenant access.

Content Automation uses OAuth to connect X accounts. OAuth delegates limited access without collecting a user’s password. I must understand scopes, state, redirect URIs, access tokens, refresh tokens, expiry and revocation.

Authentication proves identity. Authorisation decides what that identity may do.

## 14. Secrets Manager and KMS

Secrets Manager stores credentials and tokens with controlled IAM access and optional rotation. Content Automation uses it for OAuth material.

KMS manages encryption keys and is documented in the Terraform EKS platform. Encryption needs both key protection and carefully scoped permission to decrypt.

Secrets must not appear in source, images, screenshots, shell history or logs.

## 15. CloudWatch

CloudWatch receives AWS metrics and logs and can raise alarms.

For my projects, useful signals include:

- Lambda errors, duration, throttles and concurrent executions;
- API Gateway latency and 4xx/5xx responses;
- SQS age of oldest message and dead-letter count;
- DynamoDB throttling and consumed capacity;
- EKS/application logs and node/workload metrics;
- EventBridge failed invocations.

A dashboard shows information. An alert connects a defined condition to an actionable response.

## 16. AWS SAM and CloudFormation

SAM extends CloudFormation with serverless resource types. My two serverless projects use SAM.

```bash
sam build
sam deploy --guided
```

`sam build` prepares artifacts. `sam deploy` creates a CloudFormation change and updates the stack. `CAPABILITY_IAM` acknowledges that the template may create or modify IAM resources.

Infrastructure as code improves repeatability, but templates still require review, state awareness, parameter control and cleanup.

## 17. Cost Understanding

Main cost drivers across my projects include:

- EKS control plane and worker compute;
- NAT Gateway hours and processed data;
- load balancers and data transfer;
- Lambda invocations and duration;
- DynamoDB storage/read/write usage;
- API Gateway requests;
- CloudWatch ingestion and retention;
- Secrets Manager secret-months and API calls;
- Bedrock tokens/model usage.

Cost control uses budgets, tags, right-sizing, retention policies, cleanup and architecture decisions—not only choosing smaller instances.

## 18. Security Review Questions

- Which identity makes this request?
- Which IAM policy allows it?
- Can permission be limited to one resource or tenant?
- Is data encrypted in transit and at rest?
- Is the service public, private or reached through a controlled endpoint?
- Where are secrets stored and rotated?
- Which actions are logged and alarmed?
- What happens if credentials are stolen?

## 19. Interview Explanation

> I have used AWS in two operating models. In my EKS work, Terraform provisions the network, IAM, encryption, cluster and nodes; ECR supplies images; Kubernetes runs the workload. In my serverless projects, API Gateway invokes Lambda, DynamoDB stores state, SQS buffers work, EventBridge routes or schedules events, Cognito or OAuth handles identity, and SAM deploys the stack. I can explain both what AWS manages and what remains my responsibility: code, access, data, reliability, monitoring and cost.

## 20. Mastery Checklist

- [ ] I can trace one EKS request and one serverless request.
- [ ] I can explain IAM permission and trust policies.
- [ ] I can explain public/private subnets and NAT cost.
- [ ] I can compare EKS and Lambda operational responsibility.
- [ ] I can explain ECR tags versus digests.
- [ ] I can design an idempotent SQS consumer.
- [ ] I can distinguish SQS buffering from EventBridge routing.
- [ ] I can explain DynamoDB keys from access patterns.
- [ ] I can explain Cognito authentication and tenant authorisation.
- [ ] I can identify useful CloudWatch alarms.
- [ ] I can explain SAM build/deploy and CloudFormation stacks.
- [ ] I can name the primary cost drivers in my projects.

## Related Material

- [Technology-to-Project Map](../TECHNOLOGY-PROJECT-MAP.md)
- [Project Commands](../13-Command-Reference/Chapter-13-Commands.md)
- [Cloud-Native Pharmacy](../projects/Cloud-Native-Pharmacy-Platform.md)
- [Content Automation](../projects/AI-Content-Automation-Platform.md)
- [Terraform EKS](../projects/Terraform-AWS-EKS-Platform.md)
