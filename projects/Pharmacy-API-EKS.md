# Pharmacy API on Amazon EKS

> A FastAPI backend containerised with Docker and deployed to Amazon EKS with AWS-native data, messaging, event, identity, registry, and monitoring services.

**Repository:** <https://github.com/AZ1600/pharmacyEKS->  
**Last verified:** 2026-07-11 against the repository README

## Problem and Learning Goal

This project demonstrates the complete path from backend code to an operated Kubernetes workload on AWS. It is especially useful because it connects application development with containerisation, image delivery, orchestration, identity, persistence, events, monitoring, and troubleshooting.

## Verified Architecture

```text
Client -> Kubernetes Service on EKS -> FastAPI pod
                                      |-> DynamoDB
                                      |-> EventBridge
                                      `-> SQS

Docker image -> Amazon ECR -> EKS worker nodes
Logs and monitoring -> CloudWatch
```

## Verified Engineering Evidence

- Python 3.11, FastAPI, and Uvicorn backend.
- Docker image published through Amazon ECR.
- Kubernetes deployment, service, ingress, health checks, and readiness probes.
- DynamoDB persistence plus SQS and EventBridge integration.
- Screenshots of the EKS cluster, running deployment, pods, and logs.
- Documented troubleshooting of ImagePullBackOff, CrashLoopBackOff, runtime errors, imports, and IAM permissions.

## Reported Debugging Work

The repository README reports that these issues were resolved, but it does not preserve the exact root cause and fix for each one. The handbook therefore treats them as **reported solved**, not fully reconstructed incidents.

The [Pharmacy API on EKS troubleshooting register](../DEBUGGING-ISSUE-REGISTER.md#_5-pharmacy-api-on-eks-troubleshooting) explains the evidence to collect for image pulls, restart loops, Python imports, and IAM failures, and identifies the missing details that should be recovered from logs, manifests, commits, screenshots, or memory.

## Deeper Study Questions

- How does the workload receive AWS permissions, and is IRSA used?
- What delivery strategy, resource limits, and autoscaling settings are configured?
- How are idempotency and failure handling implemented around events and messages?
- What application and infrastructure resources are created outside the repository?
