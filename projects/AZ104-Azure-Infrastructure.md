# AZ-104 Azure Infrastructure Lab — Network and Identity

> Project-led engineering notes, source-reviewed 11 October 2026. This is a repository inspection, not a fresh deployment audit.

**Repository:** [az104-azure-infrastructure-lab](https://github.com/AZ1600/az104-azure-infrastructure-lab)

## Problem and outcome

The project demonstrates how application requirements influence cloud architecture, identity, observability, operational workflows and deployment controls. Use the linked source to explore the current implementation rather than treating a screenshot as evidence of ongoing runtime health.

## Architecture walkthrough

Bicep modules organize VNet networking, compute, Bastion, private storage endpoints, role assignments and recovery-vault resources. What-if and deployment artifacts document the learning workflow.

## Engineering decision to explain

Distinguish control-plane RBAC from data-plane permissions; use private DNS and scoped managed identity rather than relying on isolation alone.

## Evidence map

| Question | Where to investigate |
| --- | --- |
| What is implemented? | [Source and architecture](https://github.com/AZ1600/az104-azure-infrastructure-lab/tree/main/modules) |
| How is it verified? | [Tests or validation records](https://github.com/AZ1600/az104-azure-infrastructure-lab/tree/main/docs/screenshots) |
| What does execution look like? | [Supporting evidence](https://github.com/AZ1600/az104-azure-infrastructure-lab/tree/main/docs/troubleshooting.md) |
| How does the project run? | [README and setup instructions](https://github.com/AZ1600/az104-azure-infrastructure-lab#readme) |

## Reproduce and validate

1. Read the repository README and inspect documented prerequisites.
2. Confirm service versions, configuration and costs before deploying any infrastructure.
3. Run the repository's documented static checks and unit tests in an isolated environment.
4. Review CI workflows and configuration for the same revision you tested.
5. Inspect deployment evidence separately from current runtime availability.
6. Capture observations, failures, remediation and cleanup steps.

## Limits and next experiment

Practical infrastructure lab; review Azure cost and teardown instructions before running deployment.

**Next experiment:** document one deliberate failure scenario, its diagnostic signals and the evidence that demonstrates recovery, then link the artifacts from this page.

## Interview questions

1. What trust boundaries exist in this architecture?
2. What fails if its identity provider, data store or control plane is unavailable?
3. Which parts are validated automatically, and which require an environment?
4. How would you measure reliability and detect regressions?
5. What would you change before production use, and why?
