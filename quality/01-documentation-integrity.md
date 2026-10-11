# 01 — Documentation Integrity and Link Checking

## Why this matters

A VitePress build can complete even when an external destination has moved or a claim is outdated. Validate **local route targets**, navigation references and files separately from rendering.

## Reproduce on your branch

```bash
python3 scripts/verify_docs.py
npm ci
npm run docs:build
git diff --check
```

The offline script checks:

- the presence of VitePress sidebar and navigation targets from `link: "/..."` entries;
- relative Markdown links and image paths that refer to local files;
- absolute site paths under the repository or `public/` directory;
- whether the expected chapter and lab entry pages exist;
- whether a referenced local route can be resolved case-sensitively (important when deploying from macOS to Linux).

It deliberately **does not** resolve external URLs or validate fragment IDs such as `#troubleshooting`. It ignores references in fenced code blocks. Report real broken links from this check and fix them, but do not remove working links just to silence a scanner.

## Smoke test

After running `npm run docs:dev` or `npm run docs:preview`, verify the homepage, Projects, one chapter, one Phase 2–8 lab, Interview, search, and this page. Test navigation through keyboard focus, not only pointer clicks.

## Failure classification

| Symptom | First investigation |
| --- | --- |
| VitePress shows 404 | Is the link mapped to `index.md` or an existing `.md` file? |
| Works on Mac, broken after deploy | Verify file-name case and the hosting base path |
| Menu entry missing | Check `.vitepress/config.mts` sidebar/nav separately from Markdown |
| Browser works but Markdown checker fails | Inspect a dynamic/generated route or unusual Markdown syntax; record a justified exclusion |

## Evidence to retain

Record the commit SHA, checker/build output, public deployment URL if available, and one manual browser check result. Success in a local browser is not evidence of a live deployed site.
