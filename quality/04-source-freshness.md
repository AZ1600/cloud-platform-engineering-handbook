# 04 — Source Freshness and Claims

## A code repository is not a live deployment monitor

Each project explanation should identify the inspected revision, artifacts and what remains unverified. Use explicit labels: **implemented**, **tested in committed fixtures**, **CI run verified**, **locally demonstrated**, **cloud validated at a time**, or **planned**.

## Known drift candidates (review, do not blindly rewrite)

- [`PROJECT-WORK-REGISTER.md`](../PROJECT-WORK-REGISTER.md) originated as a **17 July 2026** inventory. It is a historical list, not today's repository count or activity audit.
- GitOps project descriptions must distinguish Argo CD on **local Docker Desktop Kubernetes** from a production EKS deployment. A manifest declaring GitOps intent does not demonstrate a live EKS rollout.
- Observability descriptions should reflect the source's Prometheus/Grafana, OpenTelemetry, Loki, Tempo and alert-testing content, and still distinguish a local Docker Compose deployment from production SRE coverage.
- The EKS Terraform project documents **plan-only CI** and historical deployments; a passing plan is not evidence that an active EKS cluster exists today.
- PropertyOps documents deployed Azure Private Endpoints and a prepared VNet subnet, but its current Container Apps environment is **not yet** on that dedicated VNet.
- RAG Ops Assistant has code, tests, retrieval cases and deployment evidence. Mocked API tests and source review are not proof of current model quality or uptime.

## Review loop

1. Open the linked file at a specific commit or date.
2. Write an evidence-backed one-sentence claim.
3. Identify what could be stale or unverified.
4. Cite a test/build screenshot or run only if it actually occurred.
5. Update both chapter and project case study if they repeat the claim.
6. Add a revisit date for cloud/provider-specific behaviors.

## Portfolio boundaries

The public website should avoid invented availability, financial returns, hiring outcomes, number of customers, certified security status and team contribution claims. A plausible architecture diagram is still only a diagram if no deployment proves it.
