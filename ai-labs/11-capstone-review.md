# 11 — Capstone: Design a Safe Operational AI Assistant

## Scenario

A Kubernetes team asks: “Why are Pods failing to start and can you fix it?” Available sources: Kubernetes events, application logs, PlatformPilot classifications and approved operational runbooks. The RAG assistant is only allowed to **read** an authorized documentation corpus.

## Your design

```text
Caller identity -> read permissions -> evidence retrieval
                                      |
                               source validation
                                      |
                                model explanation
                                      |
                           evidence/claim verification
                                      |
                     structured finding to CloudOps (separate API)
                                      |
                         engineer checks and approves
                                      |
                     narrow reviewed execution + audit
```

This diagram is a **proposed integration**, not a claim that the deployed RAG assistant currently exports to CloudOps or controls Kubernetes.

## Acceptance criteria

- [ ] A known `ImagePullBackOff` question cites the right source and explains registry/image checks.
- [ ] An unknown problem states uncertainty and avoids “No issues detected.”
- [ ] An out-of-corpus policy question returns no evidence and abstains.
- [ ] A prompt-injected runbook cannot demand secrets or elevate tool authority.
- [ ] Retrieval filters exclude documents the caller is not entitled to view.
- [ ] The model's proposed action cannot become an unapproved Kubernetes mutation.
- [ ] Execution is logged with request ID, authorized actor, approval, result and rollback context.
- [ ] Errors distinguish missing evidence from model, MCP, network and permission failures.

## Negative tests to explain

1. **Stale runbook:** source revision predates a cluster migration; how is freshness displayed?
2. **False citation:** answer cites an irrelevant chunk; what fails the claim-support check?
3. **No corpus permission:** can the user infer private source names from the response?
4. **Tool argument injection:** retrieval input embeds unexpected shell syntax; why is it never executed?
5. **Repeated request:** how do you prevent duplicate approval or execution?
6. **Timeout:** Bedrock fails after retrieval; what telemetry is retained without exposing secrets?
7. **Model drift:** embedding/reranker version changes; how is regression measured?

## Interview response framework

Describe **problem → control/data plane → trust boundaries → source evidence → quality gates → failures → measurement → trade-offs**. Be explicit about which parts were inspected in code and which experiments still need running.

### Thirty-second answer

> I separate deterministic rules, authorized retrieval and LLM explanation from privileged execution. In my RAG Ops Assistant, the source code includes hybrid retrieval, cross-encoder reranking, an MCP knowledge tool, LangGraph routing, Bedrock inference and a no-evidence path. I use tests to check API contracts and small retrieval cases, and I would strengthen production evaluation with claim-level grounding, tenant access filters and observability. CloudOps remains an independent approval gate rather than something the model can bypass.

## Keep learning

- [Chapter 10 — AI Operations](../10-AI-Operations/Chapter-10-AI-Operations.md)
- [CloudOps approval lab](../labs/06-cloudops-approval.md)
- [Phase 5 incident response](../sre-labs/07-incident-triage.md)
- [Phase 4 delivery controls](../delivery-labs/02-github-oidc-security.md)
- [RAG Ops project case study](../projects/RAG-Ops-Assistant.md)
