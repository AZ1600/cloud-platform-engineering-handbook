# Cloud-Native Multi-Tenant Pharmacy Platform

> A serverless inventory platform with tenant-isolated data, authenticated APIs, and asynchronous low-stock processing.

**Repository:** <https://github.com/AZ1600/CloudNativePharmacyPlatform>  
**Last verified:** 2026-07-11 against the repository README

## Verified Architecture

```text
Client -> API Gateway -> Lambda -> DynamoDB
            ^                       |
            |                       `-> low-stock event
         Cognito                         |-> SQS -> consumer
                                        `-> EventBridge -> consumer
```

## Important Patterns

- Amazon Cognito JWT authentication.
- DynamoDB tenant partitioning with `PK = TENANT#{tenant_id}`.
- AWS SAM and CloudFormation infrastructure as code.
- SQS, EventBridge, retries, and dead-letter queue patterns.
- Tests, build specification, and deployment configuration.

## Connection to the EKS Pharmacy Project

This serverless version and [the EKS version](Pharmacy-API-EKS.md) make a valuable architecture comparison. The handbook will examine managed serverless operations against container orchestration: control, scaling, portability, operational burden, event handling, and cost.
