# 10 — PlatformPilot, CloudOps, OpsPilot and Résumé Analysis

## The same word “AI” hides different mechanisms

| System | What the checked-in code shows | Non-negotiable boundary |
| --- | --- | --- |
| PlatformPilot | fixed pod-status rules and cluster-summary logic | unknown status must not be called healthy |
| CloudOps | deterministic Decision Trace and approval-required finding workflow | trace is not an execution authority |
| OpsPilot | rule-based ingestion plus optional OpenAI structured-classification path | generated action remains pending/owner-reviewed |
| AI Resume Analyzer | browser skill-alias scoring and separate n8n/Bedrock workflow | evidence label is not employment verification |
| RAG Ops Assistant | retrieved evidence + Bedrock answers via MCP/LangGraph | no evidence must produce abstention |

## PlatformPilot: safe classification

[`backend/ai.py`](https://github.com/AZ1600/platform-pilot/blob/main/backend/ai.py) recognizes `ImagePullBackOff`, `ErrImagePull`, `CrashLoopBackOff`, and `OOMKilled`. Its fallback currently emits `No issues detected` for other statuses; **this is an identified limitation**, not a safe response for unknown degraded states.

An engineering improvement is an explicit `unclassified` result with the observed status, events and log references and no automatic repair.

## CloudOps: evidence does not equal approval

[`lib/decision-trace.ts`](https://github.com/AZ1600/cloudops-command-center/blob/main/lib/decision-trace.ts) builds five deterministic stages: **premise, reasoning, hypothesis, verification, conclusion**. Confidence values are mechanically adjusted and clamped to 0–1; they should not be presented as calibrated probabilities.

[`tests/approval-gate.test.ts`](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) asserts an execution request is blocked before an approved state. This is a valuable **code-test boundary**, not blanket proof of live production authorization.

## OpsPilot: two classification paths

[`lib/ai/ingestion-engine.ts`](https://github.com/AZ1600/opspilot-saas/blob/main/lib/ai/ingestion-engine.ts) derives categories with deterministic rules. [`lib/ai/openai-ingestion.ts`](https://github.com/AZ1600/opspilot-saas/blob/main/lib/ai/openai-ingestion.ts) conditionally requests JSON-schema-constrained model output when provider configuration is present and falls back to rules on failure. Generated actions are built with pending status; an inference result does not mean a message was sent.

## AI Resume Analyzer: interpretable scoring

[`lib/resume-scoring.js`](https://github.com/AZ1600/ai-resume-analyzer-n8n/blob/main/lib/resume-scoring.js) normalizes aliases, matches a defined role profile and computes `round(matched / required * 100)`. Skill evidence is heuristically labeled *mentioned*, *supported*, or *strong*. These labels describe résumé text patterns and are **not independently verified achievements or hiring judgments**.

The repository also describes a separate n8n + Bedrock Nova Pro workflow; do not merge that fact into a claim that deterministic scoring itself invokes Bedrock.

## Exercise

Design a common operational finding format with `source`, `observed_at`, `resource`, `evidence`, `confidence_interpretation`, `recommended_runbook` and `approval_required`. State which source fields are computed, model-generated or engineer-entered, and which service is allowed to change infrastructure.

Next: [capstone and interview exercises](11-capstone-review.md).
