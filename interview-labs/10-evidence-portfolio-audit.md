# 10 — Engineering Evidence and Portfolio Readiness Audit

## A defensible project page

A hiring reviewer should be able to answer: What problem did this solve? What was actually built? Which part was yours? Why this design? Where are the tests? What failed? What was measured? What remains unfinished?

## Evidence ladder

| Claim type | Required example of proof | Must not be mistaken for |
| --- | --- | --- |
| Source implemented | Specific file and current revision | A passing runtime result |
| Test exists | Named test file and assertion | A passing CI run |
| CI passed | Workflow run URL + commit SHA + date | Production deployment |
| Local run demonstrated | Command output/screenshot + date and environment | Cloud availability |
| Cloud validated | Deployment/log/health artifact + date/environment | Continual uptime |
| Production operation | Maintained monitoring, ownership and service-level evidence | Personal project documentation alone |
| Proposed improvement | ADR/roadmap and test plan | Implemented functionality |

## Five-minute review checklist

1. Open the GitHub repository and verify README links resolve.
2. Check that the diagram matches source code and deployment boundaries.
3. Click through 1–2 important source files and one test file.
4. Look for evidence of negative tests and failure handling.
5. Distinguish security controls present in code from comprehensive security validation.
6. Check for leaked secrets, personal data or active resource identifiers before publishing screenshots.
7. Verify that no obsolete technologies, deployment states or counts are represented as current.
8. Review costs and documented cleanup for cloud-based reproductions.
9. Confirm who authored/reviewed changes and what contributions you can truthfully explain.
10. End each case study with an explicit next improvement.

## Example claim classification

**Claim:** "OpsPilot has PostgreSQL tenant-isolation integration tests." **Supported by:** [test source](https://github.com/AZ1600/opspilot-saas/blob/main/tests/integration/tenant-isolation.postgres.ts). **Acceptable:** test exists. **Not established by that link alone:** those tests passed today, no tenant-leak paths remain, or regulatory compliance.

**Claim:** "CloudOps blocks execution before approval in its test scenario." **Supported by:** [approval-gate test](https://github.com/AZ1600/cloudops-command-center/blob/main/tests/approval-gate.test.ts). **Acceptable:** the negative-case assertion exists. **Not established:** a verified production execution boundary under all roles and integrations.

Use the [Engineering Evidence Guide](../projects/Engineering-Evidence-Guide.md) and the [Project Register](../PROJECT-WORK-REGISTER.md). Some register dates reflect older inventories and should be treated as historical snapshots rather than current GitHub repository counts.

## Interview deliverable

For each flagship project produce a 1-page evidence card: **problem, architecture, personal contribution, exact sources/tests, validation status/date, key trade-off, incident/lesson, limitation and next experiment**.
