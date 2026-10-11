# 06 — Security Architecture and DevSecOps Interviews

## Trace the trust boundary, not the product logo

**Prompt:** "How would you let GitHub Actions deploy an AWS container without storing an access key?"

Explain GitHub's OIDC token, AWS role trust policy conditions scoped to repository and branch/environment, STS short-lived credentials, narrowly scoped ECR/deploy permissions and the distinction between the CI role and the application's task role.

**Do not confuse** a role trust policy (who can assume it) with a permissions policy (what assumed credentials may do). Review the [RAG ECS deployment](https://github.com/AZ1600/rag-ops-assistant) and [delivery security labs](../delivery-labs/index.md).

## Cross-cloud boundaries

| Boundary | Control questions |
| --- | --- |
| User to API | Authentication, authorization, tenant scope, rate limiting |
| API to database | Workload identity, network path, query scope, auditing |
| GitHub to AWS/Azure | Federated trust conditions, environment approvals, expiry |
| Kubernetes to AWS | ServiceAccount, workload identity, pod privilege, IAM policy |
| Retrieval tool to documents | Corpus authorization, tainted content, access filtering |
| Recommendation to execution | Explicit approval, idempotency, audit and rollback |

## Concrete review prompts

- A valid token accesses another business's record: where should the tenant filter be enforced?
- An image vulnerability scan passes: what *else* is needed before deployment?
- A secret appears in a build log: how do you contain, revoke, rotate and prevent recurrence?
- A Bedrock prompt contains instructions copied from a retrieved document: why is that lower-trust text?

**Evidence:** OpsPilot defines [PostgreSQL tenant-isolation tests](https://github.com/AZ1600/opspilot-saas/blob/main/tests/integration/tenant-isolation.postgres.ts); CloudOps defines an [approval-gate test](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts). Tests demonstrate stated scenarios but require an observed run for a pass claim.

## Practice

Draw the principal, resource, trust boundary, authorization check and audit record for one project. Specify a negative test that should be denied, and state which claims still need penetration or deployment testing.
