# 07 — Integrated scenario: service creation to incident review

**Purpose:** practise connecting separate codebases while clearly distinguishing a **design exercise** from an already deployed end-to-end service.

## Reference architecture (conceptual integration)

```text
Developer
   |
   v
Backstage Scaffolder ---> GitHub repository + catalogue record
   |                                |
   |                                v
   |                         CI + container image
   |                                |
   |                                v
   |                        Kubernetes / Argo CD
   |                                |
   |                                v
   +-------------------------> Prometheus + events
                                    |
                                    v
                            PlatformPilot analysis
                                    |
                            authenticated export
                                    v
                          CloudOps risk / evidence
                                    |
                           owner + human approval
                                    v
                            controlled action log
```

Each arrow represents an integration **to verify**. The repos implement many of these individual components, but this diagram is a **target operating model**, not proof that all components are connected in a single continuously running cluster.

## Step 1 — Generate a service

Review the [Backstage template](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/template.yaml). Identify which parameters determine owner, environment and repo URL. Confirm the template's `publish:github` visibility is `public` before using real service details.

**Evidence to collect:** template values (redacted), generated `catalog-info.yaml`, CI definitions, app health handler and manifest diff.

## Step 2 — Assess deployment safety

Inspect the generated Deployment's image, probes, security context, requests/limits and NetworkPolicy. Compare with the [Pharmacy API manifest](https://github.com/AZ1600/pharmacy-api-eks/blob/main/k8s/deployment.yaml), which uses Pod Identity and a non-root container.

**Decision question:** Is the image immutable? Does the policy restrict source/egress traffic? What is the rollback plan? Record missing guarantees explicitly.

## Step 3 — Investigate an incident (tabletop, no fault injection)

Scenario: Service traffic fails after a deployment while Pods still show `Running`.

1. Check Deployment rollout and Pod readiness.
2. Check Service selector, EndpointSlices, DNS, port mapping and policies.
3. Compare the timestamp of the change with application logs and events.
4. Note at least two alternative hypotheses and how you would falsify them.
5. Prepare a redacted evidence package for review.

Use [read-only runbooks](03-incident-runbooks.md); do not deliberately break a production service.

## Step 4 — Evaluate PlatformPilot output

[PlatformPilot's export route](https://github.com/AZ1600/platform-pilot/blob/main/backend/routers/cloudops.py) is restricted to operator+ API roles and generates finding IDs and timestamps. Ask which observations were captured and whether the underlying Kubernetes identity has narrower permissions.

## Step 5 — Receive a CloudOps risk

Verify the [finding schema](https://github.com/AZ1600/cloudops-command-center/blob/main/contracts/operational-finding.schema.json), evidence provenance and approval requirement. Consult the [approval tests](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts) to show that direct execution before approval is rejected.

## Definition of done for a reproducible integration lab

- [ ] A local or disposable test cluster is selected and identified.
- [ ] Generated service is deployed from an immutable or trusted controlled image.
- [ ] Catalog owner, environment and CI status are documented.
- [ ] Traffic and metrics can be observed with timestamps and safe redaction.
- [ ] A synthetic finding satisfies the schema and authenticates to the receiver.
- [ ] Negative tests show unauthenticated ingest and early execution are rejected.
- [ ] Every action has an owner, audit trail and rollback plan.
- [ ] Cleanup instructions are safe, explicit and limited to the lab environment.

## Interview prompt

> “What makes this an internal platform rather than four tools installed alongside each other?”

Discuss a supported workflow and its users, the integration contract, ownership, policy-as-default, measured outcomes and the ability to diagnose failures across boundaries. Note which integration links remain unproven.
