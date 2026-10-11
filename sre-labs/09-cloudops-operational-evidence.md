# 09 — CloudOps operational evidence and approval boundaries

## Objective

Model the handoff between a monitoring observation, a structured finding, a risk decision, and an approved operational action. Never infer permission to remediate from an alert, confidence number or AI-generated summary.

## Source-backed behavior

[CloudOps](https://github.com/AZ1600/cloudops-command-center) accepts PlatformPilot findings using a [JSON Schema contract](https://github.com/AZ1600/cloudops-command-center/blob/main/contracts/operational-finding.schema.json) with a required `approvalRequired: true`. The [Decision Trace implementation](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/decision-trace.ts) builds deterministic stages: **premise → reasoning → hypothesis → verification → conclusion**. This is an explicit evidence template, not internal AI reasoning or an automated authorization.

The [telemetry module](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/telemetry.ts) emits structured JSON operations including request ID, route, outcome, HTTP status, risk/finding context and rejection reason. Incoming safe `x-request-id` values are preserved; otherwise a new ID is generated.

The [approval gate tests](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) check that execution is blocked before approval and that status/audit evidence changes after an approval. The tests demonstrate the modeled application boundary, not actual production infrastructure change execution.

## Example decision chain

```text
Prometheus / Kubernetes observation
   -> PlatformPilot investigation (viewer)
   -> PlatformPilot findings export (operator)
   -> CloudOps contract/auth validation
   -> risk and owner routing
   -> raw evidence and deterministic Decision Trace
   -> independent engineer verification
   -> explicit human approval
   -> controlled/manual action with audit
```

**Important:** This chain is a **cross-project design narrative**. Do not claim a live shared observability-to-CloudOps deployment without separate integration evidence.

## Evidence versus audit

- Telemetry helps debug a request and measure system behavior.
- An audit trail records actor, action, approval, status, time and outcome with accountability controls.
- A trace or confidence score does not establish that a recommendation is correct or approved.
- A risk can remain `needs_approval` despite severe signals if no authorized decision has been made.

## Safe code review commands

From a separate local clone of the CloudOps repo:

```bash
npm run test
npm run typecheck
npm run contracts:validate
```

These commands test application behavior; they do not authorize or execute cloud remediation. Check the repo's `package.json` before running other scripts.

## Exercise

Draft a response for an elevated 5xx error alert. Include the original query, service owner, supporting logs or spans, time of observation, alternative explanations, bounded-confidence hypothesis, verification step, required approver, reversible change, verification query and audit record. Mark all sample values hypothetical.

Next: [Capstone and postmortem](10-capstone-postmortem.md).
