# 08 — Multi-tenant SaaS Architecture: OpsPilot

**Objective:** show isolation in identity, authorization, queries, jobs and billing. A “tenant_id” column alone does not guarantee isolation.

## Implemented layering

```text
User -> Clerk identity / controlled demo mode
     -> server-side session + business resolution
     -> role permission on API route
     -> WorkspaceRepository(businessId, ...)
     -> development file store OR PostgreSQL
     -> actions, approval events, execution jobs
```

The [OpsPilot repository contract](https://github.com/AZ1600/opspilot-saas/blob/main/lib/server/workspace-repository.ts) requires `businessId` on workspace reads and decision updates. The [PostgreSQL tenant-isolation integration test](https://github.com/AZ1600/opspilot-saas/blob/main/tests/integration/tenant-isolation.postgres.ts) creates two tenants with a shared action ID and verifies scoped operations using a guarded, isolated test database. That is useful **tested behavior in a specific environment**, not a proof of globally perfect isolation.

## Defense-in-depth

| Layer | Required check | Test idea |
| --- | --- | --- |
| Session | Identity is verified and maps to one active workspace | Forged provider user rejected |
| API | Actor has tenant-scoped permission | Staff cannot approve owner-only action |
| Repository | Every query uses verified business ID | Same action ID across tenants cannot leak |
| Database | Unique keys, transactions and indexes preserve scope | Conflicting update returns no cross-tenant row |
| Async worker | Job carries tenant and original authorization decision | Worker rejects tenant mismatch |
| Webhooks | Provider signature, event dedupe and customer mapping | Replay and wrong-customer events rejected |

## Strong guarantees vs documented implementation

Row-level security (RLS), transactional outbox, encrypted backups and automated restore drills are design options to evaluate. Do **not** claim OpsPilot uses RLS or exactly-once event delivery without locating implementation evidence. PostgreSQL tests explicitly require a local test DB configured through `OPSPILOT_TEST_DATABASE_URL`—do not run them against hosted production data.

## Incident scenario

A webhook for Tenant A's subscription carries a customer ID that happens to resemble Tenant B's. Explain the route that maps provider identity to the internal tenant, the transaction that updates billing, and the failure response if the lookup is ambiguous. The correct architecture defaults to **no cross-tenant mutation**, then raises an attributable investigation event.

[Next: AI and operational control planes](09-ai-control-plane.md)
