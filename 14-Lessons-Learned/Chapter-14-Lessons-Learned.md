# Chapter 14 — Lessons Learned Across My Projects

> Lessons are useful when they connect an observation to a future engineering behaviour.

## 1. Working Is Not the Same as Production-Ready

PlatformPilot and the Pharmacy manifests demonstrate real integration, but production readiness also requires authentication, least privilege, tests, observability, configuration, resource controls and recovery.

**Future behaviour:** describe current capability and production gaps separately.

## 2. Use Exact Language

PlatformPilot’s current analysis is deterministic rules, not a language model. Image publication is not deployment. A dashboard is not observability by itself.

**Future behaviour:** use terminology that matches implementation.

## 3. Identity Is Part of Architecture

Mounted AWS credentials and broad cluster access may make a demo work but expand risk.

**Future behaviour:** design human, pipeline and workload identity at the beginning; prefer temporary credentials, OIDC and workload roles.

## 4. Namespace Is Part of Kubernetes Identity

Pod name alone is insufficient across a cluster. PlatformPilot mixes default/all-namespace operations.

**Future behaviour:** include namespace in API routes, data models, permissions and diagnostics.

## 5. Contracts Need Tests

PlatformPilot’s AI Summary page expects flat values while the API returns nested objects.

**Future behaviour:** define response schemas/types and add contract tests between frontend and backend.

## 6. Unknown Does Not Mean Healthy

An unrecognised pod status currently falls back to “No issues detected.”

**Future behaviour:** represent unknown/unclassified state explicitly and require investigation evidence.

## 7. Immutable Artifacts Improve Trust

Using `latest` with `IfNotPresent` can run stale or ambiguous images.

**Future behaviour:** tag/digest images immutably and promote the exact verified artifact.

## 8. Asynchronous Systems Require Idempotency

SQS, EventBridge and scheduled publishing can retry or duplicate delivery.

**Future behaviour:** use stable event IDs, conditional state transitions and safe repeat processing.

## 9. Managed Services Shift Responsibility

Lambda removes server management; EKS removes control-plane operation. Neither removes application, permission, data, monitoring or cost responsibility.

**Future behaviour:** document the shared-responsibility boundary for every service choice.

## 10. Infrastructure State Is Sensitive

Terraform state is essential management data and may contain sensitive attributes.

**Future behaviour:** use protected remote state, locking, encryption, access control and backups; never commit state.

## 11. Alerts Need Owners and Actions

Seeing a risk is not enough. CloudOps demonstrates routing, runbooks, approval and audit.

**Future behaviour:** connect alerts to impact, owner, runbook and verification.

## 12. AI Must Be Bound by Evidence and Permission

Models can explain but also hallucinate. Operational execution can cause real impact.

**Future behaviour:** normalise evidence, validate typed output, require appropriate approval, execute narrowly and audit results.

## 13. Platform Value Is User Outcome

Backstage, Argo CD, Terraform and dashboards are ingredients. The platform succeeds when developers can complete safe workflows with less cognitive load.

**Future behaviour:** measure adoption, lead time, failure clarity, recovery and user satisfaction.

## 14. Commands Need Context

A command without account, cluster, region, directory or risk context is incomplete.

**Future behaviour:** maintain the project command reference with purpose, evidence, risk and verification.

## 15. Documentation Is Engineering Work

Writing these chapters exposed contract, identity, naming, configuration and production gaps that a project README alone did not reveal.

**Future behaviour:** update architecture, commands, decisions and lessons as part of the definition of done.

## 16. Incident/Lesson Template

For each future issue record:

```text
Date and system
Symptom and impact
Detection source
Investigation and evidence
Root cause
Mitigation
Permanent fix
Prevention/test/alert
Owner and follow-up
```

Do not call a simulated or learning failure a production incident.

## 17. Next Priorities

1. Add tests and fix known PlatformPilot correctness issues.
2. Replace static credentials and introduce workload identity.
3. Use immutable images and complete CI/GitOps linkage.
4. Protect Terraform state and validate infrastructure in CI.
5. Instrument a real service and provision observability as code.
6. Deepen remaining project case studies from implementation files.

## Related Material

- [Debugging and Issue Register](../DEBUGGING-ISSUE-REGISTER.md)
- [PlatformPilot](../projects/PlatformPilot.md)
- [Architecture](../11-Architecture/Chapter-11-Architecture.md)
- [Interview Preparation](../12-Interview-Preparation/Chapter-12-Interview-Preparation.md)
