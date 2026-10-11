# 03 — Accessibility and Performance Review

## Keyboard and screen-reader smoke test

1. Navigate Home → chapters → lab → search → Projects using only **Tab**, **Shift+Tab**, **Enter** and **Escape**.
2. Check focus is visible in light and dark themes, and does not disappear behind the sticky header.
3. Use VoiceOver (macOS) to inspect headings, lists, tables, links and code examples. Confirm links make sense out of context.
4. At 375 px width and at 200% zoom, verify the sidebar opens, text does not overlap and tables scroll without cutting off adjacent content.
5. Enable **Reduce Motion** in macOS and check feature-card hover animation is no longer distracting.
6. Check image alt text and external link wording, especially on project evidence screenshots.

The included CSS improves reduced-motion and keyboard-visible focus behavior. It is **not** a WCAG audit or a guarantee about every screen reader.

## Bundles above 500 kB

Prior builds emitted a Vite/Rollup warning for large minified JavaScript chunks. Do not merely increase `chunkSizeWarningLimit` to hide it. Record the actual bundle sizes, identify major contributors, inspect browser network transfer, and evaluate chunk splitting only if it improves user experience.

```bash
npm run docs:build
find .vitepress/dist/assets -type f -name '*.js' -exec ls -lh {} +
```

Measure page-load behavior on mobile or a throttled connection; do not claim a specific performance score without a dated measurement.

## Manual results record

| Test | Date/device | Pass/issue | Evidence/fix |
| --- | --- | --- | --- |
| Keyboard navigation | To verify | Pending | Add result |
| VoiceOver headings/links | To verify | Pending | Add result |
| Mobile width and zoom | To verify | Pending | Add result |
| Reduced motion | To verify | Pending | Add result |
| Light/dark contrast | To verify | Pending | Add result |
| Bundle/network profile | To verify | Pending | Add result |
