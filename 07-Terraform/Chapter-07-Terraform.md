# Chapter 7 — Terraform Through My EKS Platform

> Terraform turns infrastructure requirements into version-controlled desired state. My Terraform EKS project uses it to define AWS networking, IAM, encryption, the EKS cluster and managed worker nodes.

## Learning Objectives

I should be able to explain providers, resources, data sources, variables, outputs, modules, dependency graphs, state, backends, plan/apply/destroy, drift, lifecycle and security using my EKS project.

## 1. Why Terraform Exists

Manual console changes are difficult to reproduce, review and audit. Terraform represents infrastructure in configuration and compares it with recorded state and provider-observed resources.

```text
Configuration + State + Provider observations
                 -> Plan
                 -> approved Apply
                 -> updated infrastructure and state
```

Terraform is declarative: I describe the desired result rather than scripting every API step.

## 2. My EKS Infrastructure Scope

The repository documents provisioning of:

- VPC, public/private subnets, Internet Gateway and NAT Gateway;
- route tables and security groups;
- IAM cluster and node roles;
- KMS encryption;
- Amazon EKS control plane;
- managed node group and EC2 workers.

This makes the project a platform foundation, not just one virtual machine.

## 3. Core Terraform Objects

### Provider

The AWS provider translates Terraform resource operations into AWS API calls. Provider configuration includes Region and obtains credentials from the supported AWS credential chain.

### Resource

A resource declares an object Terraform manages, such as a VPC, subnet, IAM role or EKS cluster.

### Data source

A data source reads an existing object without taking ownership of its lifecycle.

### Variables and outputs

Variables make configuration reusable. Outputs expose useful values such as cluster name or endpoint. Sensitive outputs still enter state and must be protected.

### Modules

A module packages related resources behind inputs and outputs. Modules reduce repetition but do not remove the need to understand what they create.

## 4. Dependency Graph

Terraform derives dependencies from references.

```text
VPC
  -> subnets/routes
  -> EKS network configuration
IAM roles
  -> EKS cluster and nodes
KMS key
  -> EKS secret encryption
EKS cluster
  -> managed node group
```

Explicit `depends_on` is reserved for dependencies Terraform cannot infer cleanly.

## 5. State

State maps Terraform resource addresses to real infrastructure. It can contain resource identifiers and sensitive values.

Losing state can make Terraform unable to manage resources safely. Concurrent state writes can corrupt workflows.

The repository lists remote state in S3 as a future improvement. A team-ready design should use a protected remote backend, encryption, versioning and state locking supported by the chosen backend strategy.

Never commit local state or state backups to Git.

## 6. The Safe Workflow

```bash
terraform fmt -check -recursive
terraform init
terraform validate
terraform plan
terraform apply
```

- `fmt` normalises style.
- `init` installs providers/modules and configures the backend.
- `validate` checks internal configuration validity.
- `plan` previews proposed operations.
- `apply` performs an approved plan.

A valid configuration is not necessarily secure, reliable or affordable. Review the plan for resource count, replacements, exposure, IAM and cost.

## 7. Plan Reading

Terraform symbols normally mean:

- `+` create;
- `~` update in place;
- `-` destroy;
- `-/+` replace;
- `<=` read a data source.

Replacement of networking, databases or clusters deserves special attention because it can cause downtime or data loss.

## 8. Apply and Idempotence

After a successful apply, a new plan should normally show no changes if configuration and external reality are unchanged.

Terraform is not perfectly idempotent when provider APIs return unstable values or another actor changes managed resources. That is why provider versions, drift control and clear ownership matter.

## 9. Drift

Drift occurs when real infrastructure changes outside Terraform.

```text
Engineer edits security group in console
  -> configuration unchanged
  -> next refresh/plan detects difference
  -> team decides to revert or codify the change
```

Do not automatically apply every drift correction without understanding why the change occurred.

## 10. Destroy and Cleanup

```bash
terraform plan -destroy
terraform destroy
```

Destroy is useful for learning-environment cost control, but it is destructive. Confirm account, workspace, backend and protected resources. Some resources may block deletion because of dependencies or safety settings.

## 11. Variables and Environments

Avoid hardcoding account-specific values. Use typed variables, validation and environment-specific value files that contain no secrets.

Separate environments can use different state and controlled inputs. Terraform workspaces are one option, but separate directories/backends may provide clearer isolation for materially different environments.

## 12. IAM in Terraform

Terraform needs deployment permissions to create AWS infrastructure. The infrastructure it creates also contains runtime roles.

These are different trust boundaries:

- Terraform execution role: allowed to provision/change infrastructure.
- EKS cluster role: lets EKS call required AWS services.
- node role: lets worker nodes join and operate.
- workload role: lets a specific pod access specific AWS services.

Policies should be constructed and reviewed deliberately. Broad wildcard permission is not a production shortcut.

## 13. EKS Networking Through Terraform

The project connects VPC resources to EKS. I should be able to explain:

- CIDR selection and overlap risk;
- public versus private subnet roles;
- route-table association;
- Internet Gateway versus NAT Gateway;
- EKS endpoint exposure;
- security-group traffic;
- how worker nodes reach ECR and AWS APIs.

## 14. KMS Encryption

The project documents KMS for encryption. A key requires a key policy, lifecycle decision and authorised decrypt identities. Deleting or disabling a key can make protected data inaccessible.

Encryption at rest complements—not replaces—access control, network protection and audit logs.

## 15. Validation After Apply

The repository verifies cluster operation with:

```bash
kubectl get nodes
kubectl get pods -A
```

These commands confirm node registration and system workloads, but complete validation should also check cluster access, add-ons, DNS, network paths, workload scheduling and security controls.

## 16. CI/CD for Terraform

A safe pull-request workflow should run:

```text
format check -> validate -> security/policy scan -> plan
            -> human review -> protected apply
```

The plan belongs to the exact code and state snapshot that produced it. An apply should not silently use an unrelated plan after the branch or state changes.

Use short-lived CI credentials such as GitHub OIDC rather than long-lived AWS keys.

## 17. Secrets and Sensitive Data

Do not place secrets directly in `.tf` or committed variable files. Marking a variable `sensitive` hides some CLI output but does not remove it from state.

Protect the backend and prefer secret references or runtime retrieval where appropriate.

## 18. Common Problems

### State lock or backend failure

Confirm no active apply is running. Never force-unlock casually; identify the owning operation first.

### Access denied

Read the AWS action and resource in the error, confirm the caller with STS and adjust only the necessary permission.

### Dependency or deletion error

Find the real AWS dependency. Avoid manual deletion unless its effect on state is understood.

### Unexpected replacement

Review the attribute forcing replacement and assess downtime, data and network impact before approval.

### Provider/version changes

Use version constraints and commit the dependency lock file. Review provider upgrades like application dependencies.

## 19. Project Explanation

> My Terraform EKS project defines the AWS platform from the network upward: VPC and subnets, routing and NAT, IAM roles, KMS encryption, the managed EKS control plane and managed worker nodes. I use `init`, `validate` and `plan` before `apply`, then verify nodes and system pods with kubectl. The main production improvements are protected remote state, CI plan review, short-lived deployment credentials and stronger policy/security validation.

## 20. Interview Questions

### Why does Terraform need state?

State maps configuration addresses to real provider objects and stores attributes needed for dependency and change planning. It must be protected because it can contain sensitive infrastructure data.

### What is the difference between plan and apply?

Plan previews changes for the current configuration, state and provider observations. Apply performs approved changes. A saved plan gives stronger assurance that the reviewed operations are the ones executed.

### What is drift?

Drift is a difference created outside the Terraform workflow. A plan can detect it; the team must decide whether configuration or reality is authoritative.

### Why use modules?

Modules package a coherent capability behind inputs/outputs, encouraging consistency and reuse. Poor modules can hide complexity, so their resources and versions must still be understood.

## 21. Mastery Checklist

- [ ] I can explain provider, resource, data source, variable, output and module.
- [ ] I can draw my EKS dependency graph.
- [ ] I can explain what state contains and how to protect it.
- [ ] I can read create/update/destroy/replace plan symbols.
- [ ] I can explain drift and safe reconciliation.
- [ ] I can distinguish Terraform, cluster, node and workload IAM roles.
- [ ] I can explain the VPC path used by EKS nodes.
- [ ] I can describe a protected CI plan/apply workflow.
- [ ] I can explain why `sensitive` does not remove secrets from state.
- [ ] I can safely preview cleanup before destroy.

## Related Material

- [Terraform EKS Case Study](../projects/Terraform-AWS-EKS-Platform.md)
- [AWS Through My Projects](../05-AWS/Chapter-05-AWS.md)
- [Kubernetes Through My Projects](../04-Kubernetes/Chapter-04-Kubernetes.md)
- [Project Commands](../13-Command-Reference/Chapter-13-Commands.md)
