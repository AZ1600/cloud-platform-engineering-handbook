# Chapter 6 — Platform Engineering Through My Projects

> Platform engineering builds reusable internal products that make safe, supported engineering work easier. My Backstage, PlatformPilot, CloudOps, GitOps and infrastructure projects demonstrate different layers of a platform.

## 1. Why Platform Engineering Exists

As organisations grow, every team solving cloud access, deployment, observability and ownership independently creates duplication and cognitive load.

Platform engineering creates a supported path:

```text
Developer need -> self-service interface/API/template
               -> policy and automation
               -> infrastructure/toolchain
               -> feedback and operational evidence
```

## 2. Platform as a Product

The platform team has users: application developers, operators and service owners. A platform should solve their real workflows, have documentation/support, measure adoption and improve from feedback.

A collection of tools is not automatically a platform.

## 3. My Platform Layers

| Layer | Project evidence |
|---|---|
| Experience/interface | Backstage portal, PlatformPilot, CloudOps |
| Service ownership | Backstage catalogue, CloudOps service catalogue |
| Infrastructure | Terraform EKS |
| Delivery | GitHub Actions, ECR, Argo CD |
| Runtime | EKS and Kubernetes |
| Observability | Prometheus, Grafana, PlatformPilot |
| Governance | approvals, RBAC, IAM, audit history |

## 4. Internal Developer Platform

An IDP is the integrated set of capabilities; a developer portal is one interface into it. Backstage provides the portal/catalogue experience, but the actual platform also needs APIs, templates, pipelines, infrastructure and support.

## 5. Backstage Concepts

My Backstage project demonstrates:

- software catalogue and entity metadata;
- ownership and dependency relationships;
- TechDocs;
- GitHub and Kubernetes integration direction;
- extensible plugins.

Entities should identify owner, lifecycle, system and relationships. Catalogue quality depends on accurate metadata and clear ownership.

## 6. Self-Service and Paved Roads

A paved road is a recommended, supported path—not an absolute prison.

Example:

```text
Service template -> repository -> CI checks -> image registry
                 -> deployment manifest -> GitOps -> observability
```

The path should include security and reliability defaults. Exceptions need an explicit process.

## 7. PlatformPilot

PlatformPilot provides a Kubernetes operations interface over pods, deployments, nodes, namespaces, events and logs. Its value is reducing the effort to assemble operational context.

It also illustrates platform risks: the backend becomes a privileged gateway, so authentication, RBAC, namespace boundaries, audit and safe error handling are part of the product.

## 8. CloudOps Command Center

CloudOps turns infrastructure signals into explainable risks, owner routing, runbooks, approval, simulated execution and audit history.

```text
signal -> evidence/risk -> owner -> runbook -> approval -> execution -> audit
```

This is a platform workflow because it connects detection, ownership and governed action rather than only displaying alerts.

## 9. Service Ownership

Every production service should have an owner, lifecycle, repository, documentation, dependencies, operational links and escalation path.

Ownership does not mean one person is blamed. It means responsibility for decisions and response is discoverable.

## 10. Golden Paths and Templates

Templates can create repositories, CI, deployment configuration, documentation and ownership metadata. Good templates are versioned, tested and maintainable. They should not generate opaque infrastructure that users cannot operate.

## 11. Governance

Governance becomes usable when encoded into the path:

- IAM/RBAC defaults;
- CI policy checks;
- approved base images;
- required ownership metadata;
- deployment approvals;
- audit records;
- cost tags and quotas.

## 12. Developer Experience

Developer experience includes time to first successful deployment, documentation findability, feedback speed, failure clarity and support burden.

Useful platform measures:

- adoption and successful self-service rate;
- lead time and deployment frequency;
- change failure and recovery time;
- template completion time;
- support requests and common failure reasons;
- user satisfaction.

## 13. Build Versus Buy

Build when the workflow differentiates the organisation or requires integration unavailable elsewhere. Buy/adopt when a mature tool solves the commodity problem. Most platforms combine both.

My projects adopt Kubernetes, Argo CD, Backstage, Prometheus and Grafana, then build tailored workflows and interfaces around them.

## 14. Platform Security

Platforms concentrate privilege. Protect:

- user and workload identity;
- tenant/environment boundaries;
- secrets and temporary credentials;
- action authorisation and approval;
- audit integrity;
- supply chain and templates;
- safe defaults and restricted escape paths.

## 15. Anti-Patterns

- Building a portal before understanding user problems.
- Calling a tool collection a platform.
- Making every workflow mandatory before it is reliable.
- Hiding infrastructure so completely that users cannot debug.
- Measuring only platform uptime instead of user outcomes.
- Giving the platform broad administrator access without boundaries.

## 16. Interview Explanation

> I see platform engineering as product engineering for internal users. My Terraform EKS project provides infrastructure, GitHub Actions and Argo CD provide delivery, Prometheus/Grafana and PlatformPilot provide feedback, Backstage provides catalogue/portal capabilities, and CloudOps adds ownership and approval-gated remediation. The platform value is the integrated, supported workflow with safe defaults—not the individual tools.

## 17. Mastery Checklist

- [ ] I can distinguish a portal, IDP and platform team.
- [ ] I can identify users and outcomes for my platform projects.
- [ ] I can draw my platform layers.
- [ ] I can explain catalogue ownership and metadata.
- [ ] I can define a paved road and exception path.
- [ ] I can explain governance as code/defaults.
- [ ] I can name meaningful platform success metrics.
- [ ] I can discuss build-versus-buy trade-offs.

## Related Material

- [Backstage Portal](../projects/Backstage-Developer-Portal.md)
- [PlatformPilot](../projects/PlatformPilot.md)
- [CloudOps](../projects/CloudOps-Command-Center.md)
- [GitOps](../projects/GitOps-ArgoCD.md)
