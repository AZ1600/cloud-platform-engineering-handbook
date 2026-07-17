# CloudOps Command Center

> An AI-powered platform engineering assistant that turns infrastructure signals into explainable, owner-routed, approval-gated remediation workflows.

**Status:** Frontend-first MVP with production-foundation features documented  
**Repository:** <https://github.com/AZ1600/cloudops-command-center>  
**Last verified:** 2026-07-11 against the repository README

## Verified Workflow

```text
Infrastructure signals
  -> risk engine
  -> evidence and impact explanation
  -> service-owner routing
  -> runbook-based remediation
  -> approval queue
  -> simulated execution
  -> audit log
```

The project uses Next.js, React, TypeScript, Vitest, and GitHub Actions. Its README documents mock signal sources plus live GitHub Actions and Terraform plan import flows, role-aware approvals, a Postgres-ready repository layer, and audit history.

## Verified Debugging Story

The risk-scan action changed state without giving the operator strong confirmation that the scan had completed. Commit [`53633da`](https://github.com/AZ1600/cloudops-command-center/commit/53633daa0b744f7eed6134fe719319faefa3a433) added a scan-run counter and an accessible live status containing the risk, source, and approval counts.

See [CloudOps risk scan gave insufficient visible feedback](../DEBUGGING-ISSUE-REGISTER.md#_3-cloudops-risk-scan-gave-insufficient-visible-feedback).

## Case-Study Checklist

- [ ] Write the problem statement and user workflow
- [ ] Add the repository and current architecture
- [ ] Inventory only technologies present in the codebase
- [ ] Document one important design decision
- [x] Document one debugging or reliability lesson
- [ ] Add test, deployment, and observability evidence
- [ ] Prepare a 30-second interview explanation

Use the [project case-study template](../templates/project-case-study-template.md) to expand this chapter after inspecting the repository.
