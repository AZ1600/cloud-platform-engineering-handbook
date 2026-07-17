# OpsPilot SaaS

> An AI-assisted operations platform that converts business signals into prioritised, owner-approved actions for small service businesses.

**Repository:** <https://github.com/AZ1600/opspilot-saas>  
**Last verified:** 2026-07-11 against the repository README

## Problem and Solution

Operational work is often fragmented across email, invoices, messages, notes, and workflows. OpsPilot classifies those signals into revenue opportunities, customer risks, recommended actions, and execution tasks while retaining an approval boundary before action.

## Verified Architecture

```text
User -> Next.js dashboard -> API routes
     -> AI classification and business rules
     -> repository layer
     -> local JSON or Neon PostgreSQL
```

## Engineering Areas Demonstrated

- Multi-tenant workspace resolution and role-based access control.
- Clerk authentication and invited-user joining.
- Neon PostgreSQL persistence with a development repository fallback.
- Owner approval, dismissal, audit, impact, and execution workflows.
- Stripe billing foundation and webhooks.
- GitHub Actions validation with tests, linting, type checks, and builds.
- Vercel deployment and runtime health diagnostics.

The deeper chapter will verify which integrations are live, optional, mocked, or represented as integration boundaries.

## Verified Debugging Story

The local JSON and OAuth-token stores originally wrote beneath `process.cwd()/data`. That local filesystem assumption was unsafe on Vercel. Commit [`9d8385e`](https://github.com/AZ1600/opspilot-saas/commit/9d8385e638c97ba840216e31cc370caa8aa4a573) introduced a shared runtime-aware data directory, using `/tmp/opspilot-data` for the Vercel demo fallback and retaining PostgreSQL as the durable production design.

See [OpsPilot could not safely write demo files on Vercel](../DEBUGGING-ISSUE-REGISTER.md#_2-opspilot-could-not-safely-write-demo-files-on-vercel) for the symptom, diagnosis, fix, verification, limitation, and prevention lesson.
