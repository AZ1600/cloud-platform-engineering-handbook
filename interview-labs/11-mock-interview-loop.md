# 11 — Mock Interview Loop and Scorecard

## A 45-minute practice session

| Time | Segment | Prompt |
| --- | --- | --- |
| 0–5 min | Introduction | Explain your background and selected role without reciting a project list |
| 5–15 min | Systems | Design a safe service deployment, including network and IAM boundaries |
| 15–25 min | Troubleshooting | Diagnose a failing Kubernetes rollout or missing database connectivity |
| 25–35 min | Deep dive | Explain one repository's code path, security test and unproven assumption |
| 35–42 min | Behaviour | Give one truthful STAR story with a source-linked result |
| 42–45 min | Reflection | State the next experiment and questions for the interviewer |

The interviewer chooses *one* of the following challenge paths:

- **Platform engineer:** PlatformPilot → Kubernetes API and Prometheus → CloudOps approval boundary.
- **Cloud engineer:** Terraform EKS plan-only validation → VPC/EKS identity → observed deployment verification.
- **SRE:** demo API 5xx rate → SLO burn → telemetry correlation → approved mitigation.
- **AI engineer:** RAG hybrid retrieval → no-evidence abstention → prompt-injection safety → evaluation.

## Scoring rubric (0–4 per dimension)

| Dimension | 0 | 2 | 4 |
| --- | --- | --- | --- |
| Problem framing | No requirement | Partial constraints | User impact and measurable constraints |
| Architecture | Cannot trace path | Happy path only | Trust, data, identity and failure paths |
| Evidence | Unsupported claims | Vague README references | Exact source/test and evidence level |
| Safety and reliability | No risks named | Generic risks | Prioritized, testable mitigations |
| Trade-offs | Tool preference | One alternative | Clear decision criteria and counterfactual |
| Communication | Unclear | Mostly organized | Concise answer, responds to follow-ups |

**Total: 0–24 points.** Use the score for rehearsal only, not as a measure of professional competency or hiring probability.

## Coaching notes

A strong interview answer says "I do not know whether that is deployed right now; here is how I would verify it" when appropriate. Encourage drawing and correction. Penalise invented metrics, insecure advice and treating source code as proof of live reliability.

## Practice log

| Date | Track | Score /24 | Evidence to verify | Next rehearsal |
| --- | --- | --- | --- | --- |
| YYYY-MM-DD | Your track | — | Code file, test or run artifact | Specific follow-up |

## Final portfolio audit

Before applying, make sure the [portfolio evidence review](10-evidence-portfolio-audit.md) passes for three projects and that each project has a clear explanation at 30 seconds, two minutes and ten minutes.
