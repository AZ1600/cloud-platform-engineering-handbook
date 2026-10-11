# 06 — AWS and Azure Architecture Trade-offs

**Objective:** choose topology based on workload and current deployment state, not the service names on a diagram.

## Three worked comparisons

| Decision | Option A | Option B | Key trade-off |
| --- | --- | --- | --- |
| API runtime | Amazon EKS + managed nodes | API Gateway + Lambda | Control plane/cluster maintenance vs managed limits and cold-start/event model |
| IaC | Terraform modules | Azure Bicep | Multi-provider tooling and state vs native Azure resource declarations |
| Data connectivity | Private endpoints + private DNS | Public endpoint + strict auth | Routing/ops complexity vs exposure and control layers |

The [Terraform EKS repository](https://github.com/AZ1600/platform-engineering-terraform-eks) implements VPC/EKS configuration and a read-only AWS plan workflow; it does not require leaving an expensive cluster running. The [PropertyOps project](https://github.com/AZ1600/AI-property-operations) documents deployed PostgreSQL and Key Vault private endpoints **and** a dedicated subnet *prepared* for future VNet-integrated Container Apps. The currently described Container Apps environment uses its existing Azure-managed network. Do not draw it inside the prepared VNet as though that integration is already complete.

## Decision tree

```text
Known steady workload + platform team + Kubernetes-specific needs?
    yes -> consider EKS and quantify operational cost
    no  -> compare managed container and serverless runtimes

Private backend needed?
    yes -> validate caller network integration, private DNS and identity

Multi-cloud policy required?
    yes -> quantify portability gains against extra complexity
```

**Availability design** still needs AZ layout, backend redundancy, route and health checks. A public endpoint with an IP allowlist can be reasonable for a restricted lab, but is not a general production baseline.

## Exercise: topology audit

Open the actual PropertyOps IaC and draw: operator, Entra ID, Container Apps, managed identity, Key Vault, PostgreSQL, both private endpoints, private DNS, the existing Container Apps environment and the prepared subnet. Use a dashed **proposed** line for any future VNet integration, and list the DNS and routing evidence needed before claiming a private end-to-end path.

[Next: Internal Developer Platforms](07-idp-platform-boundaries.md)
