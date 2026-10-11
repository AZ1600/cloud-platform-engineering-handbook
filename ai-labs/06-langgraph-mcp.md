# 06 — LangGraph Orchestration and MCP Tool Contracts

## The operational flow

The [agent service](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/langgraph_agent.py) starts an MCP subprocess, discovers tools, converts tool schemas for Bedrock Converse, compiles a LangGraph graph, and reuses that service across FastAPI requests. The [MCP server](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/mcp_server.py) exposes `search_knowledge_base(question)`.

```text
Question -> Bedrock node
             | tool_use
             v
          MCP client -> search_knowledge_base
             |
          ranked evidence
             |
          no evidence? -> hard abstain
             |
          evidence -> Bedrock answer -> sources + evidence
```

The tool shown is a **read-only retrieval tool**, not a general shell or Kubernetes mutation tool. Names like `search_knowledge_base` are part of the explicit interface; a model should not be permitted to invent new tool names or permissions.

## Boundary-specific errors

- A tool could return `found: false`: this is a valid result, not a transport exception.
- An MCP process could exit or return malformed JSON: report a tool-service failure, not an unsupported-document answer.
- Bedrock might be unavailable or throttled: use a bounded retry strategy, not an unbounded loop.
- An agent may repeatedly request tools: define invocation and time limits before scaling beyond a lab.

## Tool contract review

The declared input requires a `question` string. The returned object includes evidence metadata and a `found` status. For production, add:

1. maximum request length and execution time;
2. caller-derived document entitlements;
3. an allowlisted tool registry and input schema validation;
4. output size/secret redaction limits;
5. stable correlation IDs and bounded retries;
6. metrics for tool success, abstentions, and timeouts.

## Failure injection exercise

Draw expected behavior for:

```text
MCP process unavailable
Retrieval index missing
Valid search with zero relevant results
Bedrock throttle on second invocation
User asks the model to execute a shell command
```

In the current documented RAG tool surface, the last case should **not gain execution capability**. Tool permissions must be enforced in code and IAM rather than delegated to model instructions.

Next: [prompt injection and data safety](07-prompt-injection.md).
