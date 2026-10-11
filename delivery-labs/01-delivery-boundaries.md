# 01 · CI is not deployment

## Distinguish each promise

| Stage | What it proves | What it does not prove |
| --- | --- | --- |
| Source checks | Code/format/test contracts satisfied | Live service correctness |
| Build | Application/image can be produced | Artifact is trusted or runnable in target |
| Vulnerability scan | Findings under the scanner's scope/policy | Absence of all exploitable vulnerabilities |
| Publish | Artifact is stored in a registry | Cluster downloaded or ran it |
| Deploy | Target accepted an update | Users can complete a workflow |
| Verify | Probes and smoke tests passed | Future availability or data correctness |

**Evidence:** The [CI/CD pipeline](https://github.com/AZ1600/platform-engineering-cicd-pipeline) separates validation from manual [ECR publication](https://github.com/AZ1600/platform-engineering-cicd-pipeline/blob/main/.github/workflows/ci.yml). The publishing workflow is triggered with `workflow_dispatch`, so a successful validation run is not a claim that deployment occurred.

## Trace the system

```text
feature branch -> pull request -> checks -> merge to main
                                             |
                                     manual publish request
                                             |
                                      OIDC / build / SBOM
                                             |
                                         ECR digest
                                             |
                           (separate deployment contract required)
                                             |
                                    runtime + smoke check
```

The final two steps are architectural handoffs, not an end-to-end claim about the CI/CD demo. [Pharmacy API EKS](https://github.com/AZ1600/pharmacy-api-eks/blob/main/.github/workflows/deploy.yml) provides a separately implemented EKS deployment example.

## Read-only lab

```bash
# Run inside a local clone of the CI/CD repository.
git status --short
ls .github/workflows
grep -n 'workflow_dispatch\|pull_request\|push' .github/workflows/*.yml
```

Identify the approval point, publishing job, target registry, source revision and verification evidence. Do not confuse branch protection *documented in a README* with policies verified as enabled right now.

## Failure exercise

A build succeeds but the service is unhealthy. What evidence is missing? Record (1) artifact digest, (2) deployment revision, (3) readiness state, (4) request-level smoke result and (5) rollback criteria.

**Interview prompt:** When can a team responsibly call a deployment successful? Separate a CI pass from an operational success criterion.
