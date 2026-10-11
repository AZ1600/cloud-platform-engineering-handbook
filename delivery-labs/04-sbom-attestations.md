# 04 · SBOM, provenance and artifact attestations

## Three separate questions

- **SBOM:** What components are reported as present in this software artifact?
- **Provenance:** How, where and from which inputs was the artifact built?
- **Attestation:** What signed claim about an identified artifact is available to verify?

None independently certifies that code is safe. The security argument depends on linking evidence to the **same artifact digest** that is deployed.

## Source trace

The [CI/CD ECR publishing workflow](https://github.com/AZ1600/platform-engineering-cicd-pipeline/blob/main/.github/workflows/ci.yml) creates a CycloneDX SBOM, validates its JSON structure, uploads it as a workflow artifact, pushes a Git-SHA-tagged image to ECR, retrieves the registry digest, then uses `actions/attest` for provenance and SBOM attestations.

```text
Source commit -> Docker build -> CycloneDX SBOM
                           -> ECR push -> sha256 digest
                                        |          |
                                        v          v
                                   provenance   SBOM claim
```

## Read-only examination

```bash
# Run in a local clone, no cloud access required.
grep -n 'Generate CycloneDX\|attest\|image_digest\|docker push' .github/workflows/ci.yml
```

Review whether the pipeline verifies the integrity of downloaded actions/images, how artifacts are retained, and whether deployment consumes the exact digest. Publishing and attesting alone do not prove downstream verification is enforced.

## Threat review

| Threat | Defensible requirement |
| --- | --- |
| Tag overwritten | Record and deploy immutable digest |
| Compromised build dependency | Pin/verify inputs, scan and review SBOM |
| Provenance unrelated to deployed image | Check attestation subject digest against deployed digest |
| Vulnerability database incomplete | Treat scan as a point-in-time signal |

**Interview:** Why does an SBOM plus passing Trivy scan not prove that a deployment is secure?
