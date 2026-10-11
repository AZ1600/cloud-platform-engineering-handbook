# 08 — Cost, Lifecycle and Reproducible Cleanup

**Goal:** Identify non-obvious cloud lab costs and document safe, deliberate cleanup. **This page does not instruct an automatic destroy.**

## Cloud labs create billable resources

| AWS resources to consider | Azure resources to consider |
|---|---|
| EKS cluster hours and worker node compute | Azure Bastion hours and public IP resources |
| NAT gateway hours/data processing | Azure Container Apps environments, compute and networking |
| Load balancers and logs | Private endpoints, DNS and managed PostgreSQL |
| ECR storage and image retention | Azure Container Registry and Key Vault operations |
| S3 state, CloudWatch, data transfer | Recovery Services vault, backup storage and Log Analytics |

Actual pricing, quotas, billing and regional availability change; confirm rates and budgets for the chosen Region and account before deploying anything. A stopped VM can still generate disk, IP, backup or networking charges. Removing a compute resource may not remove attached data or separately managed services.

## Repository-specific trade-offs

The [Terraform network module](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/network/main.tf) selects a single NAT gateway, trading some resilience for lower lab cost. Its [GitHub workflow](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml) performs AWS-backed **plan only** rather than continuously applying expensive EKS infrastructure.

The [AZ-104 README](https://github.com/AZ1600/az104-azure-infrastructure-lab) documents VM deallocation and backup/restore experiments; backups and Bastion are billable independently of whether the VM is actively serving traffic. PropertyOps separates network foundations from the existing runtime, and this can lead to costs for prepared resources even when that future network isn't used by the application.

## Before provisioning

1. Capture a list of resources and expected monthly/hourly expense, including supporting services.
2. Define an owner and an explicit lab expiration time.
3. Configure budget alerts and service-specific limits where supported.
4. Record tags, resource group names, Terraform state location and recovery requirements.
5. Ensure the cleanup procedure has been peer-reviewed and tested in an isolated lab, not production.

## Before deleting

- Verify current account/subscription and Region.
- Identify backups, persistent data, logs, public DNS and shared infrastructure.
- Confirm infrastructure ownership: Terraform may not manage every related resource.
- Obtain explicit approval before running `terraform destroy`, deleting resource groups or modifying shared network controls.
- Review a proposed plan and capture evidence of every affected resource.
- Validate the final invoice/remaining resources after cleanup using read-only inventory commands.

## Cost interview exercise

A two-AZ EKS lab is intended for a two-hour demonstration. Discuss the cost of leaving the NAT gateway, managed nodes, load balancer and control plane running for a month. Compare leaving the environment online, reproducibly recreating it, and using plan-only CI. Which approach would you recommend for a personal portfolio, and what testing limitations does each introduce?

Next: [Interview and review exercises](09-interview-exercises.md).
