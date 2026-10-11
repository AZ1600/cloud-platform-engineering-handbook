# 02 — Dependency Security Triage

The handbook is a **static VitePress site**, but the build toolchain still processes Markdown, code snippets and project dependencies. Development dependencies need attention even when `npm audit --omit=dev` reports no production advisories.

## Known observation, not a current result

Local terminal screenshots from 11 October 2026 showed **3 advisories: 2 moderate, 1 high** in the full install. Earlier evidence associated remaining advisory paths with Vite/VitePress and esbuild. The exact current advisory IDs, fixed versions and direct/transitive relationship must be established from **your current lockfile and `npm audit` output**.

## Gather the actual evidence

```bash
npm ci
npm audit
npm audit --omit=dev --audit-level=high
npm ls vitepress vite esbuild
```

The first audit can legitimately exit nonzero. The second is a separate production-dependency gate; it is **not proof** that vulnerable build-time tooling is harmless. Never commit raw audit JSON if it contains environment-specific sensitive metadata.

## Decision record template

| Field | What to capture |
| --- | --- |
| Package/advisory | Exact package, affected range, GHSA/CVE and severity |
| Reachability | Does this package process untrusted input in preview/build? |
| Fixed version | Is a non-breaking patch supported by the VitePress version in use? |
| Test | `npm ci`, `npm run docs:check`, `npm run docs:build`, browser smoke test |
| Decision | Upgrade safely, mitigate temporarily, or accept time-bounded risk |
| Owner/revisit | Named maintainer and explicit future review date |

Try a **separate dependency-fix branch** with the smallest compatible updates, and compare lockfile changes before committing. Never use `npm audit fix --force` without reviewing breaking version changes and testing the generated site.

## CI policy in this patch

`npm audit --omit=dev --audit-level=high` is enforced. A full audit of development dependencies is also run and its JSON stored as a CI artifact **without claiming it passed**. This is a deliberate visibility-first policy while advisories are being investigated, not a completed security remediation.
