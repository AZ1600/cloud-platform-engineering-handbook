# 01 — Trace an AWS VPC to an EKS Workload

**Goal:** Explain *why each hop exists* from GitHub source to a running, healthy Kubernetes service, and identify where the network can fail.

## Verified repository structure

In [the Terraform EKS dev environment](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/environments/dev/main.tf), a network module supplies `vpc_id` and **private subnet IDs** to an EKS module. The [network module](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/network/main.tf) defines public and private subnets and currently sets `single_nat_gateway = true`. The [EKS module](https://github.com/AZ1600/platform-engineering-terraform-eks/blob/main/modules/eks/main.tf) declares private API access, logging, encrypted worker storage and managed node groups.

```text
Developer / CI             AWS control plane
      |                          |
      | Terraform plan           | EKS API and IAM
      v                          v
GitHub OIDC -> AWS plan role -> EKS control plane
                                  |
                      private worker subnets
                         |             |
                         v             v
                    worker node    worker node
                         \             /
                          pod replicas
                               |
                            Service
                               |
                 ingress / approved client path
```

This is a conceptual diagram, **not** a claim that all depicted resources are currently running. The Terraform repository explicitly distinguishes earlier deployment evidence from the plan-only validation workflow.

## Why private subnets matter

A private worker node should not require a directly reachable public IP. For outbound package/image/API access, it may depend on NAT or private service endpoints; NAT is **not** an ingress path. A *single* NAT gateway lowers a development environment's cost but creates an availability dependency for cross-AZ egress. Availability Zones and multiple replicas reduce some failure modes, but not every shared dependency.

## Trace the application layer

The [Pharmacy workload manifest](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml) declares two replicas, probes, topology spreading, non-root execution and explicit requests/limits. Its `image: REPLACE_IMAGE_URI` is intentionally a deployment-time placeholder. The [deploy workflow](https://github.com/AZ1600/pharmacy-api-eks/blob/main/.github/workflows/deploy.yml) resolves an immutable ECR digest and renders the manifest before applying it.

## Read-only investigation sequence

Only when you have an approved cluster context:

```bash
aws sts get-caller-identity
aws configure get region
kubectl config current-context
kubectl get nodes -o wide
kubectl get deployment,pods,service -A
kubectl describe deployment pharmacy-api -n default
kubectl get endpointslices -A
```

Do not assume `-n default` is the correct namespace in another environment. Inspect the actual manifest first. `aws eks update-kubeconfig` changes local configuration, so treat it as a separate, deliberate step.

## Failure exercise — service has no endpoints

**Observation:** `/health` does not respond through the Service even though Deployment replicas appear ready.

1. Inspect Service selectors and Deployment pod labels in Git, then compare to the cluster.
2. Query EndpointSlices in the actual namespace; absence of endpoints indicates a routing/selection problem, not necessarily an application crash.
3. Check readiness probe state and pod events.
4. Form competing hypotheses: selector mismatch; readiness failure; wrong namespace; policy or DNS limitation.
5. Record which observation confirms or falsifies each hypothesis before any change.

**Trade-off prompt:** Would you pay for an additional NAT gateway, replace NAT egress with suitable AWS VPC endpoints, or accept the risk in a short-lived lab? Explain impact, cost and the workload's dependency graph.

**Evidence to capture:** Terraform path and commit SHA, selected Kubernetes objects (redacted), one hypothesis, a command result, and an explicit limit of what you validated.

Next: [Terraform state and plans](02-terraform-plan-state.md).
