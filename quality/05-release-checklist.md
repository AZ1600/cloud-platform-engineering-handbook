# 05 — Release Acceptance Checklist

Use this at the end of Phase 9 and before later handbook releases.

## Automated checks

- [ ] Correct branch and clean baseline before applying a patch.
- [ ] `python3 scripts/verify_docs.py` reports no unresolved local route/path errors.
- [ ] `npm ci` and `npm run docs:build` complete successfully.
- [ ] `npm audit --omit=dev --audit-level=high` result is reviewed.
- [ ] Full `npm audit` findings are recorded, including remaining development risks.
- [ ] `git diff --check` and `git diff --cached --check` have no issues.
- [ ] CI checks run on the actual pull request commit.

## Reader experience

- [ ] Homepage, chapters, Labs, Projects and this Quality page render.
- [ ] Search and mobile menu work.
- [ ] Keyboard tab order, focus visibility and VoiceOver basics checked.
- [ ] Narrow/mobile widths and large zoom checked.
- [ ] Reduced-motion setting checked.
- [ ] Public preview/deployment checked separately from local preview.

## Claim and security review

- [ ] Project status wording matches current source and dated evidence.
- [ ] No credentials, tokens, customer data or private links were introduced.
- [ ] Remaining npm advisories have documented mitigation/acceptance owners.
- [ ] The VitePress bundle warning has a measured follow-up, not an arbitrary suppression.
- [ ] PR includes screenshots where UI behavior changed.

## Release record template

```text
Commit SHA:
Review date:
Local build:
CI run URL:
Security audit findings:
Browser/device checks:
Exceptions with owner/revisit date:
Production URL checked (if deployed):
Rollback: revert merge commit or redeploy the last known-good artifact
```

**Passing an automated script does not make the site certified secure or fully accessible.** Merge after the substantive manual checks are also recorded.
