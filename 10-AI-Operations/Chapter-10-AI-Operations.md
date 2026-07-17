# Chapter 10 — AI Operations Through My Projects

> AI operations should turn evidence into understandable assistance while keeping permissions, uncertainty and consequential actions under control.

## 1. What AI Operations Means Here

My projects use three approaches:

- deterministic rules in PlatformPilot;
- infrastructure risk classification and approval workflows in CloudOps;
- LLM analysis through AWS Bedrock in the AI Resume Analyzer;
- optional AI boundaries and business rules in OpsPilot.

These should not all be described as the same kind of AI.

## 2. Rules Versus Models

### Deterministic rules

```text
status == CrashLoopBackOff -> Critical -> inspect startup logs
```

Rules are explainable, fast and testable but cover only anticipated cases. PlatformPilot’s current `ai.py` is a rule engine.

### Language model

A language model generates output from prompt/context. It can explain complex evidence but may produce unsupported statements and variable results.

The AI Resume Analyzer sends structured skill/readiness context to Amazon Nova Pro through Bedrock.

## 3. Evidence-Grounded Analysis

An operational recommendation should show:

- observed signal;
- source and timestamp;
- affected resource;
- interpretation;
- confidence/uncertainty;
- recommended action;
- owner and approval requirement.

The model should explain evidence, not invent missing telemetry.

## 4. PlatformPilot Analysis

PlatformPilot maps ImagePullBackOff, ErrImagePull, CrashLoopBackOff and OOMKilled to predefined severity, cause, recommendation and owner.

Current limitation: unknown non-running states fall back to “No issues detected.” A safe fallback should say “unclassified; investigate” and include events/logs.

## 5. CloudOps Workflow

```text
infrastructure signal -> risk engine -> evidence and impact
-> owner routing -> runbook -> approval -> simulated execution -> audit
```

The approval boundary is essential. Recommendation and execution are separate decisions.

## 6. OpsPilot Workflow

OpsPilot turns business signals into revenue/customer risk and recommended actions. It supports a rule-based local classifier and an optional OpenAI boundary documented by the repository.

Multi-tenant data, user roles and approval rules are security boundaries around the intelligence layer.

## 7. AI Resume Analyzer

```text
resume data -> n8n -> skill extraction -> JavaScript score
            -> Bedrock/Nova Pro -> explanation and recommendations
```

The deterministic score and model narrative should remain distinguishable. Career recommendations need transparent criteria and careful handling of personal data.

## 8. Prompt Design

A strong prompt defines role, task, trusted evidence, output schema, prohibited claims and uncertainty behaviour.

Structured outputs make validation easier. Prompt text is application logic and should be versioned and tested.

## 9. Hallucination and Validation

Models can create plausible unsupported claims. Controls include:

- supply only relevant trusted context;
- require evidence references;
- use schemas/enums;
- validate resources and commands;
- reject unsupported output;
- never execute free-form model commands directly;
- evaluate with known examples and adversarial inputs.

## 10. Security and Privacy

- Minimise data sent to a model.
- Remove secrets and unnecessary personal information.
- Control model/service access with IAM.
- Define retention and audit policy.
- Treat external content as untrusted prompt input.
- Prevent prompt injection from gaining tool permission.

## 11. Human-in-the-Loop Design

Approval should show evidence, proposed change, scope, risk, preview and rollback. The approver must actually have authority and sufficient context.

Low-risk reversible actions may be automated after strong evidence; high-impact actions need stricter approval and policy.

## 12. Evaluation

Measure more than “the answer looks good”:

- classification precision/recall;
- unsupported-claim rate;
- recommendation acceptance and override rate;
- time to useful diagnosis;
- unsafe action rate;
- latency and model cost;
- performance across failure types and user groups.

## 13. Failure Modes

- missing/stale evidence;
- unknown rule classified as healthy;
- model hallucination;
- prompt injection;
- overprivileged tool access;
- duplicate execution;
- approval fatigue;
- untraceable output;
- sensitive-data leakage.

## 14. Safe Architecture

```text
signals -> normalisation -> deterministic checks
        -> optional model explanation
        -> schema/policy validation
        -> human approval
        -> narrow executor
        -> verification and audit
```

The executor should accept a limited typed action, not arbitrary shell text.

## 15. Interview Explanation

> I use AI assistance as one layer of an operational system. PlatformPilot currently uses transparent deterministic rules; CloudOps connects risks to evidence, owners, runbooks and approval; my Bedrock/n8n project uses a language model to explain structured résumé analysis. I separate recommendation from execution, validate outputs, minimise permissions and measure unsupported claims rather than calling every rule “AI.”

## 16. Mastery Checklist

- [ ] I can distinguish rules, classifiers and LLM generation.
- [ ] I can describe PlatformPilot’s exact rules and limitation.
- [ ] I can explain evidence grounding and uncertainty.
- [ ] I can design a structured prompt/output contract.
- [ ] I can explain prompt injection and permission boundaries.
- [ ] I can design approval and audit around an action.
- [ ] I can define evaluation metrics for operational assistance.
- [ ] I can explain why arbitrary model-generated commands are unsafe.

## Related Material

- [PlatformPilot](../projects/PlatformPilot.md)
- [CloudOps](../projects/CloudOps-Command-Center.md)
- [OpsPilot](../projects/OpsPilot-SaaS.md)
- [AI Resume Analyzer](../projects/AI-Resume-Analyzer.md)
