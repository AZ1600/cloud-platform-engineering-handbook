# Handbook Quality & Security Review

> Phase 9 — a documented **review process**, not a security certification, penetration test, or declaration that the documentation is production-ready.

This handbook has accumulated substantial coverage across cloud, Kubernetes, delivery, reliability, AI and system design. Quality now means **checking claims, navigation, dependency risk, accessibility and publication paths** before declaring a release ready.

## Start here

1. [Documentation integrity](01-documentation-integrity.md): internal routes, sidebar links, images and reproducible builds.
2. [Dependency security](02-dependency-security.md): triage remaining development advisories without forced upgrades.
3. [Accessibility and performance](03-accessibility-performance.md): keyboard, screen-reader, mobile and bundle review.
4. [Source freshness and claims](04-source-freshness.md): avoid turning project code or old screenshots into unverified current claims.
5. [Release acceptance checklist](05-release-checklist.md): what to verify before merging and publishing.

## Evidence baseline — 11 October 2026

- The public repository contains a VitePress 1.6.4-based handbook and a committed lockfile. This is source inspection, not a fresh production or security audit.
- Previous local installation screenshots reported **3 npm advisories (2 moderate, 1 high)**. Their details and current status must be rechecked with `npm audit` after `npm ci`.
- Previous VitePress builds succeeded but warned about client chunks larger than 500 kB. Investigate impact with measurements before changing bundling settings.
- The historical project register still carries a **July 2026** baseline and must not imply a current count or live deployment state.
- There was no checked-in handbook-specific GitHub Actions documentation-check workflow at review time; the Phase 9 patch proposes one.

## Release rule

Publish only after the local build, internal-link checks, relevant security review, and manual reader checks. Record all exceptions with an owner and a next review date. Avoid portraying informational checks as passing enforcement gates.
