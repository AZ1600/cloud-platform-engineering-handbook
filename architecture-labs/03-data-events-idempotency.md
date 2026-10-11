# 03 — State, Events and Idempotency

**Objective:** distinguish authoritative state from cache, event, derived view and audit trail. Retries, crashes and duplicate delivery are normal conditions, not rare exceptions.

## Write the state machine first

```text
pending -> approved -> queued -> completed
    |         |             |
    +--> dismissed         +--> failed
```

This is a **design illustration**, not an assertion of every state name implemented in OpsPilot. In a real review, extract exact state transitions from `lib/server` and the schema before finalising the diagram.

## OpsPilot's relevant evidence

The [workspace repository contract](https://github.com/AZ1600/opspilot-saas/blob/main/lib/server/workspace-repository.ts) includes `read(businessId)`, `updateActionDecision(businessId, actionId, status, actor)` and `updateExecutionJobStatus(...)`. The [approval idempotency tests](https://github.com/AZ1600/opspilot-saas/blob/main/tests/approval-idempotency.test.ts) exercise repeated approval after a job was marked completed or failed and expect a single execution job and approval event. This is concrete but scoped test coverage—not an exact-once delivery guarantee across arbitrary external systems.

## Reliable retry design

1. Generate an idempotency key from **tenant + action + intended transition**; never share a global key across tenants.
2. Enforce uniqueness transactionally at the database layer, not only in browser state.
3. Commit the state transition and outbox record together if asynchronous dispatch is added.
4. Let workers claim jobs atomically; record attempt counts and final status.
5. Treat external webhooks as **at least once**. Use inbox deduplication and provider-specific event IDs.
6. Keep audit records separate from noisy operational logs; never allow a recomputation to erase a prior decision.

A small duplicate-safe handler might return a previous result for a known idempotency key rather than creating another job. That is a **proposed** generic approach; don't assume the repository implements a transactional outbox.

## Trade-off table

| Pattern | Works well when | Main risk |
| --- | --- | --- |
| Synchronous database transaction | State change fits one database | Long requests and tight coupling |
| Outbox + worker | External side effects or retries required | Delivery lag, duplicate handling |
| Saga | Multiple services participate | Compensating actions and debugging |
| Event sourcing | Audit/replay drives product requirements | Projection evolution and complexity |

## Failure drill

Two workers receive the same approved action while the first crashes after making a provider request but before recording success. Write the **observable recovery protocol** and state whether the provider supports idempotency tokens. If it does not, design a manual reconciliation step instead of claiming exactly-once execution.

[Next: Reliability and capacity](04-reliability-capacity.md)
