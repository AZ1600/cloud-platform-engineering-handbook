#!/usr/bin/env python3
"""Basic self-tests for the Phase 9 offline documentation checker."""
from pathlib import Path
import tempfile
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify_docs


class Tests(unittest.TestCase):
    def test_local_resolution(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'index.md').write_text('# Home')
            (root / 'docs').mkdir()
            (root / 'docs' / 'index.md').write_text('# Docs')
            (root / 'public').mkdir()
            (root / 'public' / 'logo.svg').write_text('<svg/>')
            prior = verify_docs.ROOT
            try:
                verify_docs.ROOT = root
                self.assertIsNone(verify_docs.resolve_target(root / 'index.md', '/docs/'))
                self.assertIsNone(verify_docs.resolve_target(root / 'index.md', '/logo.svg'))
                self.assertIsNone(verify_docs.resolve_target(root / 'index.md', 'https://example.com/x'))
                self.assertIsNotNone(verify_docs.resolve_target(root / 'index.md', '/missing'))
            finally:
                verify_docs.ROOT = prior

    def test_strip_code_fences(self):
        text = '# Head\n```bash\n[Example](missing.md)\n```\n[Real](index.md)'
        stripped = verify_docs.strip_fences(text)
        self.assertNotIn('missing.md', stripped)
        self.assertIn('index.md', stripped)


if __name__ == '__main__':
    unittest.main()
