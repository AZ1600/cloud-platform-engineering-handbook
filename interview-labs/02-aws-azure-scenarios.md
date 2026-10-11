# 02 — AWS and Azure Architecture Interviews

## Scenario A: deploy a private Kubernetes control plane

**Prompt:** Design an AWS EKS platform for a small team. Engineers want private API access, least-privilege CI and a way to validate changes without leaving a cluster running.

**Answer outline:**

```text
Pull request -> static checks + Terraform tests -> OIDC plan role
                                                  |
                                                plan only
Engineer-approved deployment -> VPC private subnets -> EKS + node groups
                             -> control-plane logs -> recovery/teardown
```

Connect this to the [Terraform EKS repository](https://github.com/AZ1600/platform-engineering-terraform-eks). The repository documents private cluster API access, Terraform tests, S3 state locking and a **plan-only** AWS CI workflow. Do not say its current CI automatically applies infrastructure.

**Follow-up questions:** How can an operator reach a private control plane? Which endpoints require private network access? What resources keep incurring charges? How do you recover from a failed apply? What does a successful plan *not* prove?

**Evidence:** [CI plan workflow](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml), [dev environment](https://github.com/AZ1600/platform-engineering-terraform-eks/tree/main/environments/dev).

## Scenario B: Azure workload reaches private PostgreSQL

**Prompt:** A Container App starts, but PostgreSQL resolution or connection fails after Private Link is introduced.

1. Trace DNS resolution from the actual workload network, not from an unrelated VM.
2. Confirm VNet integration and associated private DNS zone links.
3. Check the Private Endpoint status, network rules and identity separately.
4. Use platform diagnostic logs to establish whether the failure is DNS, TCP, TLS or database authentication.
5. Propose a controlled network integration migration and rollback plan.

The [PropertyOps repository](https://github.com/AZ1600/AI-property-operations) provisions PostgreSQL and Key Vault private endpoints, but documents that the **current Container Apps Environment is not yet integrated into the new dedicated VNet**. Treat a fully private workload path as a proposed next state unless independently verified.

**Evidence:** [PropertyOps architecture](https://github.com/AZ1600/AI-property-operations#azure-architecture) and [AZ-104 case study](../projects/AZ104-Azure-Infrastructure.md).

## Decision comparison

| Requirement | EKS/Terraform | Azure Container Apps/Bicep |
| --- | --- | --- |
| Deployment control | Kubernetes workload platform | Managed container app abstraction |
| Network responsibility | VPC, routing, cluster endpoint and pod traffic | Environment integration, endpoint DNS and Azure routing |
| Identity | AWS IAM + Kubernetes RBAC + workload identity | Entra, managed identity + Azure RBAC |
| Evidence to present | Plan, tests, deployment record and cluster health | What-If, deployment, name resolution and runtime logs |

## Your interview output

Prepare a 2-minute answer comparing the failure domain and operational burden of these designs. Draw identity, DNS and data flow, and name one test that would falsify your assumption.
