# 05 — Bedrock, ECS Task Identity and Runtime Boundaries

## What the repository documents

The [RAG Ops Assistant](https://github.com/AZ1600/rag-ops-assistant) describes an ARM64 Fargate service behind an ALB, with a task role for Bedrock, an ECR-hosted container, and CloudWatch logging. [`src/langgraph_agent.py`](https://github.com/AZ1600/rag-ops-assistant/blob/main/src/langgraph_agent.py) constructs a `bedrock-runtime` client in `eu-west-2`, uses the Bedrock Converse API and a `global.amazon.nova-2-lite-v1:0` model identifier.

The checked-in example [`deploy/ecs/bedrock-task-policy.example.json`](https://github.com/AZ1600/rag-ops-assistant/blob/main/deploy/ecs/bedrock-task-policy.example.json) lists limited Bedrock invocation actions and **placeholder** account/region ARNs. It is not evidence of the exact role policy deployed today.

## Separate the IAM roles

```text
GitHub Actions -> OIDC -> deploy role (CI publish/deploy)
Fargate agent  -> task execution role (pull image / ship logs)
RAG application -> ECS task role -> Bedrock InvokeModel
```

Do not put AWS access keys into the Docker image. Task role credentials are obtained via the ECS credential provider chain and scoped by IAM. Validate the actual model/region permission combination and relevant inference-profile ARNs before a cloud test.

## Different control planes

| Boundary | What it controls |
| --- | --- |
| ALB allowlist and HTTPS | who can reach the HTTP entry point |
| Security group between ALB and task | which network peer can reach the container |
| Application authentication | which caller can query which knowledge base |
| ECS task IAM role | which Bedrock actions the application can invoke |
| Retrieval access filter | which source chunks may become prompt context |

The README documents an ALB allowlist limited to an owner's `/32` and a Fargate task in a **public subnet with a public IP**, with inbound access restricted by its security group. Do **not** describe this as a private-subnet deployment. An IP allowlist is not a substitute for application authentication and document-level authorization.

## Safe checks (read-only)

```bash
# Run only with explicitly approved AWS account and credentials.
aws sts get-caller-identity
aws ecs describe-services --cluster YOUR_CLUSTER --services YOUR_SERVICE --region eu-west-2
aws ecs describe-task-definition --task-definition YOUR_TASK_FAMILY --region eu-west-2
```

Never paste account credentials or full private prompt/evidence content into an issue or pull request. These checks do not change cloud resources, but may return infrastructure metadata.

## Review question

How would you restrict a future multi-tenant assistant so a valid Bedrock task role cannot read another tenant's retrieved content? Answer in terms of **retriever filtering and application identity**, not IAM alone.

Next: [LangGraph and MCP](06-langgraph-mcp.md).
