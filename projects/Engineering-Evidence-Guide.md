# Engineering Evidence Guide

This handbook aims to explain systems with traceable implementation evidence rather than broad technology claims.

## Evidence levels

| Label | Meaning | What it does not prove |
| --- | --- | --- |
| Implemented | Files contain the feature/configuration | Correct runtime behaviour |
| Tested | Test code and documented commands exist | Tests have passed recently |
| CI validated | A specific GitHub Actions run passed | Production environment parity |
| Locally demonstrated | Screenshots or commands show a local run | Cloud readiness |
| Cloud validated | Evidence from a particular AWS/Azure deployment | Current live availability |
| Planned | Design or roadmap, not implemented | Delivered feature |

## Template for new case studies

1. **Problem:** user/operator pain point and boundaries.
2. **System path:** request, data, identity, failure and deployment flow.
3. **Design trade-offs:** choice, alternatives, risks and cost.
4. **Proof:** links to source, tests, workflows, cloud artifacts, screenshots and README.
5. **Reproduction:** prerequisites, safe steps, tests, observability and teardown.
6. **Limitations:** missing controls, untested paths and version assumptions.
7. **Learning:** one failure story and next experiment.

## Interview-ready claim review

Before using a portfolio claim in an interview, attach an exact source file or dated run artifact, label its evidence level and write one sentence about what it does **not** establish. Verify personal contribution independently: repository ownership does not prove authorship of every change. For reusable examples and negative claims, see [Phase 8 portfolio evidence practice](../interview-labs/10-evidence-portfolio-audit.md).

## Security and claims

Do not publish cloud secrets, tokens, access keys, personal records or confidential screenshots. Do not claim audit, security certification, zero downtime, production use or cost savings without verifiable evidence. A screenshot is evidence of a moment, not continuous production health. Recheck all links and deployment prerequisites when refreshing a project.
