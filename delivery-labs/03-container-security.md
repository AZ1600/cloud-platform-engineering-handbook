# 03 · Hardened container delivery

## Defensive layers

| Layer | Control | Evidence |
| --- | --- | --- |
| Build source | Pinned base image digest | [CI/CD Dockerfile](https://github.com/AZ1600/platform-engineering-cicd-pipeline/blob/main/Dockerfile) |
| Container process | Non-root UID | Repository Dockerfile |
| Runtime | Read-only filesystem, restricted capabilities, no new privileges | [CI/CD repository documentation](https://github.com/AZ1600/platform-engineering-cicd-pipeline#readme) |
| Vulnerability management | Trivy HIGH/CRITICAL gate | [CI/CD workflows](https://github.com/AZ1600/platform-engineering-cicd-pipeline/tree/main/.github/workflows) |
| Kubernetes | Digest, probes, resource limits and seccomp | [Argo CD NGINX deployment](https://github.com/AZ1600/platform-engineering-gitops-argocd/blob/main/manifests/deployment.yaml) |

## Commands for an isolated local image

```bash
# Illustration; use the image name from YOUR local clone.
docker image inspect YOUR_LOCAL_IMAGE
docker history YOUR_LOCAL_IMAGE
# If Trivy is installed:
trivy image --severity HIGH,CRITICAL YOUR_LOCAL_IMAGE
```

Do not assume the image's pinned digest remains free of findings: scanner databases and upstream vulnerabilities change.

## Dangerous shortcuts

- Replacing a failing severity gate with `--exit-code 0` silently removes enforcement.
- `:latest` tags may change between review and deployment.
- Running as non-root is useful but does not replace network controls, seccomp, sandboxing or dependency updates.
- A pass using `--ignore-unfixed` excludes findings under that policy, **not** all findings.

## Review exercise

What would break if the filesystem is read-only? Check temp paths, PID files, logs and writable volume mounts before deploying. Why does the Argo CD demo use a memory-backed `/tmp` volume?

**Interview:** Explain image immutability versus reproducible builds. A digest identifies specific bytes; a reproducible build additionally requires stable inputs and toolchains.
