#!/usr/bin/env python3
"""Synthetic documentation fixture only. No model, cloud or repo evaluation."""
import json
from pathlib import Path

CASES = Path(__file__).with_name("retrieval-fixtures.json")

def evaluate(case):
    expected = set(case["expected_sources"])
    found = case["returned_sources"]
    if not case["expect_evidence"]:
        return not found
    return bool(found) and found[0] in expected and all(x in expected for x in found)

def main():
    cases = json.loads(CASES.read_text(encoding="utf-8"))
    assert cases and any(not x["expect_evidence"] for x in cases)
    result = [evaluate(x) for x in cases]
    for n, (case, passed) in enumerate(zip(cases, result), 1):
        print(f"{n:02d} {'PASS' if passed else 'FAIL'}: {case['question']}")
    print(f"Synthetic fixture: {sum(result)}/{len(result)} passed")
    if not all(result):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
