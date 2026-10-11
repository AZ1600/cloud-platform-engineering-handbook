# PropertyOps — Secure Azure Application Platform

> Project-led engineering notes, source-reviewed 11 October 2026. This is a repository inspection, not a fresh deployment audit.

**Repository:** [AI-property-operations](https://github.com/AZ1600/AI-property-operations)

## Problem and outcome

The project demonstrates how application requirements influence cloud architecture, identity, observability, operational workflows and deployment controls. Use the linked source to explore the current implementation rather than treating a screenshot as evidence of ongoing runtime health.

## Architecture walkthrough

FastAPI → Azure Container Apps → PostgreSQL; Microsoft Entra ID supplies application identity and roles. Bicep defines cloud infrastructure including network, private endpoints, Key Vault and monitoring. GitHub Actions uses OIDC for deployment.

## Engineering decision to explain

Review the Bicep modules and application permission checks together; networking isolation does not replace application authorization.

## Evidence map

| Question | Where to investigate |
| --- | --- |
| What is implemented? | [Source and architecture](https://github.com/AZ1600/AI-property-operations/tree/main/infra) |
| How is it verified? | [Tests or validation records](https://github.com/AZ1600/AI-property-operations/tree/main/tests) |
| What does execution look like? | [Supporting evidence](https://github.com/AZ1600/AI-property-operations/tree/main/docs/screenshots) |
| How does the project run? | [README and setup instructions](https://github.com/AZ1600/AI-property-operations#readme) |

## Reproduce and validate

1. Read the repository README and inspect documented prerequisites.
2. Confirm service versions, configuration and costs before deploying any infrastructure.
3. Run the repository's documented static checks and unit tests in an isolated environment.
4. Review CI workflows and configuration for the same revision you tested.
5. Inspect deployment evidence separately from current runtime availability.
6. Capture observations, failures, remediation and cleanup steps.

## Limits and next experiment

Public README documents Azure validation, but there is no claim of continuous uptime or external penetration testing.

**Next experiment:** document one deliberate failure scenario, its diagnostic signals and the evidence that demonstrates recovery, then link the artifacts from this page.

## Interview questions

1. What trust boundaries exist in this architecture?
2. What fails if its identity provider, data store or control plane is unavailable?
3. Which parts are validated automatically, and which require an environment?
4. How would you measure reliability and detect regressions?
5. What would you change before production use, and why?
