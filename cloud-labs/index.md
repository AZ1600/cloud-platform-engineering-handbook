# AWS & Azure Infrastructure — Phase 3 Field Guide

> **Source-reviewed 11 October 2026.** These are learning and inspection exercises built from public repository files. Commands marked *read-only* query systems but may require permissions. Configuration examples are illustrative; they are not instructions to create paid cloud resources without a separate cost/security review.

This field guide builds on [AWS Chapter 5](../05-AWS/Chapter-05-AWS.md), [Terraform Chapter 7](../07-Terraform/Chapter-07-Terraform.md), and the [Kubernetes/platform labs](../labs/index.md). Each lesson separates **what the repository currently implements**, **what is documented as prior cloud validation**, and **what remains a proposed exercise**.

## Learning route

| Lesson | Outcome | Repository evidence |
|---|---|---|
| [01 — AWS VPC to EKS](01-aws-vpc-eks-path.md) | Trace private workloads, ingress, endpoints, and availability trade-offs | Terraform EKS |
| [02 — Terraform state and plans](02-terraform-plan-state.md) | Explain S3 locking, guardrail tests, saved plans and CI | Terraform EKS |
| [03 — AWS identity boundaries](03-aws-identity-boundaries.md) | Distinguish GitHub OIDC, EKS Pod Identity and Cognito | Pharmacy API EKS |
| [04 — Azure Private Link](04-azure-private-link-dns.md) | Diagnose network/DNS path separately from identity | AZ-104 / PropertyOps |
| [05 — Bicep and RBAC](05-bicep-whatif-rbac.md) | Review modules, What-If and scoped access | AZ-104 Azure Lab |
| [06 — PropertyOps deployment](06-propertyops-deployment.md) | Identify deployed vs prepared networking and CI trust | PropertyOps |
| [07 — Cross-cloud troubleshooting](07-cross-cloud-troubleshooting.md) | Practise safe hypothesis-led incident investigation | All four repositories |
| [08 — Cost and cleanup](08-cost-and-lifecycle.md) | Prevent unattended EKS, NAT, Bastion and other charges | Terraform and Azure projects |
| [09 — Interview & review](09-interview-exercises.md) | Explain a design with evidence, alternatives, failures and gaps | All four repositories |

## Working principles

1. **Start with scope:** record account/subscription, Region, resource group, cluster, and identity before running commands.
2. **Read before changing:** inspect the actual source and state before any apply, deployment, credential modification or cleanup.
3. **Do not confuse boundaries:** AWS IAM, Kubernetes RBAC, application authorization and network controls address different problems.
4. **Never claim a live system solely from code:** a manifest proves a declared configuration, not a running deployment.
5. **Keep durable evidence:** record the commit SHA, command, time, expected result, observed result and redacted output.

## Useful project links

- [Terraform EKS source](https://github.com/AZ1600/platform-engineering-terraform-eks)
- [Pharmacy API EKS source](https://github.com/AZ1600/pharmacy-api-eks)
- [AZ-104 lab source](https://github.com/AZ1600/az104-azure-infrastructure-lab)
- [PropertyOps source](https://github.com/AZ1600/AI-property-operations)
- [Engineering Evidence Guide](../projects/Engineering-Evidence-Guide.md)

> **Lab safety:** Never paste production tokens, Terraform state, bearer credentials or connection strings into public issues, screenshots or documentation. Prefer dedicated sandbox subscriptions/accounts and explicitly approved maintenance windows.
