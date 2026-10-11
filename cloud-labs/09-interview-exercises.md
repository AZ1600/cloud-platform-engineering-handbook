# 09 — AWS/Azure Architecture Review and Interview Exercises

**Goal:** Explain architecture decisions at the level expected of a cloud/platform engineer: boundaries, trade-offs, evidence, monitoring, failure and honest limitations.

## Architecture review prompts

### AWS 1 — Private EKS endpoint

Why does the Terraform dev environment use private EKS API access, and what remote administration options exist? How would you allow CI to reach the API without opening it to everyone? Cite: [dev EKS module](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/environments/dev/main.tf).

### AWS 2 — Pod Identity versus end-user identity

Explain how an API caller's Cognito claims differ from a pod's AWS credentials. Give an example of an authorization check that belongs in FastAPI even when AWS IAM grants DynamoDB access. Cite: [Pharmacy API auth](https://github.com/AZ1600/pharmacy-api-eks/blob/main/app/core/security.py).

### Terraform 3 — Plan and apply

Why does CI intentionally stop at plan? What is contained in remote state, and why is S3 lockfile protection useful? What could make a plan unsafe to publish in a CI log? Cite: [AWS Terraform workflow](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/.github/workflows/terraform-plan.yml).

### Azure 4 — Private Endpoint path

A private endpoint exists, but an Azure Container App still connects publicly. What must you inspect before saying traffic is private? Cite: [PropertyOps main Bicep](https://github.com/AZ1600/AI-property-operations/blob/main/infra/main.bicep) and [Container Apps environment](https://github.com/AZ1600/AI-property-operations/blob/main/infra/modules/container-environment.bicep).

### Azure 5 — Least privilege

A managed identity can authenticate but cannot read Blob data. How do you differentiate a missing `Storage Blob Data Reader` assignment from a DNS or firewall issue? Cite: [AZ-104 RBAC module](https://github.com/AZ1600/az104-azure-infrastructure-lab/blob/main/modules/rbac.bicep).

### Operational 6 — Recovery and cost

A lab was left running while the owner is away. What resources could continue billing after VM deallocation, and what preapproved controls should prevent it? How would you demonstrate safe cleanup without destroying production data?

## Structured answer format

For any prompt, use:

1. **Problem and objective** in one or two sentences.
2. **Architecture sketch** (request path plus identity and network boundaries).
3. **Implementation evidence** with GitHub path and code revision.
4. **Failure mode** and a read-only diagnostic command.
5. **Trade-off** (security, availability, developer experience, operational burden, cost).
6. **Status and limit** (implemented, tested locally, cloud-evidenced, still proposed).
7. **Next hardening change** with a measurable validation criterion.

## Self-assessment rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Source grounding | No code reference | General repository | Exact path and revision |
| Trust boundaries | None | One | Identity + network + application |
| Failure handling | Guess | Diagnostic | Evidence-driven alternatives |
| Operational maturity | No trade-off | Describes trade-off | Tests and safe recovery plan |
| Honest scope | Unclear | Partial | Implemented vs proposed explicit |

Score your own answer out of 10. This is a learning exercise, not a claim about a project's production readiness.

## Completion checklist

- [ ] I can map AWS and Azure control/data planes separately.
- [ ] I can locate the S3 remote backend and distinguish plan-only CI from deployment.
- [ ] I can distinguish GitHub OIDC, Pod Identity, Cognito and Entra ID.
- [ ] I can show why Private Endpoint provisioning does not prove private application routing.
- [ ] I can trace a failed request to IAM/RBAC, DNS, network policy or application code.
- [ ] I can write a cost-aware, approval-based teardown checklist.
- [ ] I can explain one improvement I have not implemented yet without exaggerating its status.

Return to the [Phase 3 field guide](index.md) or the [Engineering Evidence Guide](../projects/Engineering-Evidence-Guide.md).
