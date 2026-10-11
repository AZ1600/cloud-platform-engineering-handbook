# Kubernetes & Platform Engineering — Hands-on Field Guide

> **Phase 2 · October 2026** — A practical extension to the existing [Kubernetes chapter](/04-Kubernetes/Chapter-04-Kubernetes) and [Platform Engineering chapter](/06-Platform-Engineering/Chapter-06-Platform-Engineering). The original 14 chapters remain intact.

## Who this is for

Engineers who know the Kubernetes vocabulary but want to reason about what actually happens during deployment, access checks, troubleshooting and incident response. The teaching examples connect directly to the **AZ1600** repositories, not to hypothetical production customers.

## Reading and lab path

| Sequence | Guide | Demonstrate your understanding by… |
|---|---|---|
| 01 | [The Kubernetes control loops](01-kubernetes-control-loops.md) | Tracing a Deployment from desired state to ready endpoints |
| 02 | [Networking, identity and security](02-networking-and-identity.md) | Distinguishing a Service, NetworkPolicy, Kubernetes RBAC and cloud IAM |
| 03 | [Safe incident investigation](03-incident-runbooks.md) | Diagnosing symptoms without immediately mutating workloads |
| 04 | [PlatformPilot deep dive](04-platformpilot-api.md) | Explaining API role checks and identifying a trust boundary |
| 05 | [Backstage golden paths](05-backstage-golden-paths.md) | Reviewing a generated service for security and ownership |
| 06 | [CloudOps decision and approval](06-cloudops-approval.md) | Explaining why a finding cannot authorize execution |
| 07 | [Integrated platform scenario](07-integrated-scenario.md) | Tracing a service from creation through an incident |
| 08 | [Review and interview exercises](08-review-exercises.md) | Defending decisions using source evidence and trade-offs |

## Lab prerequisites and guardrails

- `git`, `kubectl` and a **local, disposable Kubernetes cluster** if you want to practise cluster reads. `kind` or Docker Desktop Kubernetes is suitable. The **handbook build itself does not need Kubernetes**.
- Do **not** run commands against a shared, customer or production cluster. Check the active context before any `kubectl` command.
- A command marked **read-only** retrieves information. Commands that create/change/delete resources appear only with an explicit lab-only warning.
- Treat logs and events as potentially sensitive. Redact tokens, personal data, internal addresses and credentials before saving evidence.
- Source paths were inspected on **11 October 2026**. GitHub `main` may evolve; compare the current source before treating examples as an exact implementation contract.

Check context (read-only):

```bash
kubectl config current-context
kubectl cluster-info
kubectl auth can-i list pods --all-namespaces
```

If the context is unexpected, stop. Being able to list resources does not mean you are authorised to administer them.

## What “verified” means here

| Classification | Meaning |
|---|---|
| **Code inspected** | The named file contains the implementation discussed; this is not proof of a successful deployment |
| **Test present** | An automated test is present in GitHub; it is not a claim that the suite was run during this handbook update |
| **Documented deployment** | The repository documents a deployment or shows a screenshot of a particular run; not a current-uptime claim |
| **Proposed lab / design** | An exercise or improvement, not an implemented production feature |

**Reference implementations:** [PlatformPilot](https://github.com/AZ1600/platform-pilot), [Backstage Developer Portal](https://github.com/AZ1600/platform-engineering-backstage-portal), [CloudOps Command Center](https://github.com/AZ1600/cloudops-command-center), [Pharmacy API on EKS](https://github.com/AZ1600/pharmacy-api-eks), [GitOps with Argo CD](https://github.com/AZ1600/platform-engineering-gitops-argocd).
