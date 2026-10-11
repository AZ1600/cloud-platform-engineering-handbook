# 06 — CloudOps: from evidence to controlled action

**Project:** [AZ1600/cloudops-command-center](https://github.com/AZ1600/cloudops-command-center).

## Why alert visibility is not sufficient

An alert contains a signal; a safe operational action also requires source authenticity, scoped impact, evidence, ownership, validation, approval and an auditable decision. The danger is treating generated analysis as permission to modify infrastructure.

## Ingestion contract

[`contracts/operational-finding.schema.json`](https://github.com/AZ1600/cloudops-command-center/blob/main/contracts/operational-finding.schema.json) defines a versioned shape:

- Required: `schemaVersion`, `findingId`, `source`, `observedAt`, `environment`, `service`, `category`, `severity`, `confidence`, `summary`, `evidence`, `approvalRequired`.
- `source` is fixed to `platform-pilot` for this integration; `approvalRequired` must be `true`.
- `confidence` is constrained to the range `0..1`; `evidence` requires one or more strings.
- Unknown properties are rejected by the JSON Schema (`additionalProperties: false`).

**Security principle:** schema validation is necessary but not authentication. Verify the sender token and trust boundary separately. A valid-looking finding can still be stale or misleading; maintain provenance and timestamps.

## Deterministic Decision Trace

[`lib/decision-trace.ts`](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/decision-trace.ts) creates the steps:

```text
premise -> reasoning -> hypothesis -> verification -> conclusion
```

Step IDs and dependencies make the trace reviewable. The code clamps adjusted confidence values to `0..1`. **Do not treat these values as statistically calibrated probabilities**, or the steps as hidden model reasoning. The trace is a structured decision-support artifact with fixed templates.

The verification step requires the operator to check current evidence, blast radius and rollback planning. The conclusion preserves manual review.

## Approval is a state transition, not a button colour

The [approval-gate tests](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) include a case where execution is attempted before approval. The expected response is HTTP `409 Conflict`; after an approval step, the test checks subsequent execution and audit state.

```text
new finding -> needs_approval
     |             |
     |        [reject early execution]
     v             |
engineer verification
     |
reviewed approval
     |
controlled execution record
     |
audit trail
```

A UI disabling an action is only user experience. The **server-side API** must enforce ordering even when invoked directly. Test the rejection path and preserved state, not merely success after clicking a button.

## Trust boundary walkthrough

| Boundary | Required check | What could go wrong |
|---|---|---|
| PlatformPilot → CloudOps | Authenticated sender and validated schema | Spoofed or malformed finding |
| Finding → interpretation | Evidence, timestamps, limits on confidence | Stale data treated as current fact |
| Recommendation → approval | Human actor, permissions, verification | AI-generated advice treated as authorization |
| Approval → execution | Recheck state, scope, idempotency, audit | Double action or bypass |

The repository contains demo and integration paths; that is not by itself proof of a fully operational, continuously available remediation control plane.

## Run the targeted test in the CloudOps clone

```bash
cd /path/to/cloudops-command-center
npm ci
npx vitest run tests/approval-gate.test.ts
```

This is **local reproduction guidance** based on a test present in the repository; the handbook patch does not run the CloudOps suite.

## Failure exercise

A finding reports unhealthy Pods, but by the time the reviewer opens the risk the cluster has recovered. Should the approval stay available? Propose a freshness check, verification requirements, expiration policy and resulting audit entry. Explain how a second click/retry avoids duplicate execution.
