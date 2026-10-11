#!/usr/bin/env python3
"""Offline local-target checker for the VitePress handbook.

Checks markdown local links, image paths, and quoted VitePress `link:` routes.
Does not fetch external URLs, check anchor fragments, or assess content quality.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"node_modules", ".git", ".vitepress", ".vercel"}
LINKS = re.compile(r"!?\[[^\]\n]*\]\(([^)]+)\)")
NAV = re.compile(r"\blink\s*:\s*([\"'])(/[^\"']+)\1")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")


def strip_fences(content):
    output = []
    marker = None
    for line in content.splitlines():
        m = FENCE.match(line)
        if m:
            mchar = m.group(1)[0]
            width = len(m.group(1))
            if marker is None:
                marker = (mchar, width)
            elif marker[0] == mchar and width >= marker[1]:
                marker = None
            output.append("")
        elif marker:
            output.append("")
        else:
            # Inline code snippets commonly contain illustrative Markdown links.
            output.append(re.sub(r"`+[^`\n]+`+", "", line))
    return "\n".join(output)


def resolve_target(source, value):
    raw = value.strip()
    if raw.startswith("<") and ">" in raw:
        raw = raw[1:raw.find(">")]
    elif " " in raw:
        raw = raw.split(" ", 1)[0]  # optional Markdown link title
    if not raw or raw.startswith(("#", "//")):
        return None
    url = urlsplit(raw)
    if url.scheme or url.netloc:
        return None
    path = unquote(url.path)
    if not path:
        return None
    if path.startswith("/"):
        stem = ROOT / path.lstrip("/")
        public_stem = ROOT / "public" / path.lstrip("/")
        candidates = [stem, public_stem]
    else:
        candidates = [source.parent / path]
    expanded = []
    for candidate in candidates:
        expanded.append(candidate)
        if not candidate.suffix:
            expanded.append(Path(str(candidate) + ".md"))
            expanded.append(candidate / "index.md")
            expanded.append(candidate / "README.md")
        elif candidate.suffix == ".html":
            expanded.append(candidate.with_suffix(".md"))
    if any(p.is_file() for p in expanded):
        return None
    return f"unresolved local target: {value}"


def check_tree(root=ROOT):
    findings = []
    markdown_files = sorted(
        p for p in root.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(root).parts)
    )
    for page in markdown_files:
        content = strip_fences(page.read_text(encoding="utf-8"))
        for match in LINKS.finditer(content):
            issue = resolve_target(page, match.group(1))
            if issue:
                line = content.count("\n", 0, match.start()) + 1
                findings.append(f"{page.relative_to(root)}:{line}: {issue}")
    config = root / ".vitepress" / "config.mts"
    if not config.is_file():
        findings.append("Missing .vitepress/config.mts")
    else:
        for m in NAV.finditer(config.read_text(encoding="utf-8")):
            issue = resolve_target(root / "index.md", m.group(2))
            if issue:
                findings.append(f".vitepress/config.mts: {issue}")
    return markdown_files, findings


def main():
    global ROOT
    if len(sys.argv) > 1:
        ROOT = Path(sys.argv[1]).resolve()
    pages, issues = check_tree(ROOT)
    if issues:
        print(f"Documentation integrity failed: {len(issues)} issues across {len(pages)} Markdown files")
        for issue in issues:
            print("  " + issue)
        return 1
    print(f"Documentation integrity passed: {len(pages)} Markdown files, local targets, and sidebar routes")
    print("Note: external URLs and fragment IDs are not checked; manual checks still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
