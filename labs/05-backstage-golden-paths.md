# 05 — Backstage: a paved road with safe defaults

**Project:** [AZ1600/platform-engineering-backstage-portal](https://github.com/AZ1600/platform-engineering-backstage-portal).

## The product problem

Without a shared template, every service team chooses its own CI, ownership metadata, base container, Kubernetes security defaults and documentation. This increases maintenance overhead and weakens governance.

A developer portal can make a **recommended service creation path** discoverable. The underlying platform still requires policies, pipelines, IAM, infrastructure and support. Backstage is the front door, not the entire platform.

## Source-verified template workflow

The [`examples/template/template.yaml`](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/template.yaml) declares required name, description, owner, environment and GitHub location. Its scaffolder steps are:

```text
fetch:template (render files) -> publish:github (create repo)
    -> catalog:register (catalog-info.yaml)
    -> notification:send (owner)
```

The generated repo includes a FastAPI service, CI and Kubernetes manifests. A [separate generated example](https://github.com/AZ1600/backstage-generated-inventory-api) provides evidence of the template's output structure.

## Inspect the generated Deployment

[`examples/template/content/kubernetes/deployment.yaml`](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/content/kubernetes/deployment.yaml) includes:

- `replicas: 2`, rolling-update settings and `/health` probes;
- non-root execution with `runAsUser: 10001`, `RuntimeDefault` seccomp, capability drops and read-only root filesystem;
- resource requests and limits, plus a bounded writable `/tmp` volume.

**Critical limitation:** the example uses a Backstage `values.name` template variable with a `latest` image tag. A generated repository is not the same as an immutable published deployment. Before real rollout, build/publish the image and replace the image reference with a trusted registry digest or equivalent controlled release process.

## NetworkPolicy is not a magic shield

The [template policy](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/examples/template/content/kubernetes/networkpolicy.yaml) declares ingress on port 8000 for selected Pods, but it does **not** constrain ingress sources through `from`, nor does it declare `Egress` restrictions. Its behavior depends on an enforcing CNI. Document the needed caller restrictions and separate egress requirements before calling the template hardened for a particular tenant.

## Read the permission policy, not the marketing statement

The actual [`PlatformPermissionPolicy`](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/packages/backend/src/extensions/permissionPolicy.ts):

- Denies `kubernetes.proxy` for all portal users.
- Allows `catalog.entity.delete` only when the user's ownership refs include `group:default/platform-team`.
- Returns **ALLOW for other permissions** as a default.

This is **not** a comprehensive default-deny authorization model. It is a targeted policy that still needs an explicit permission inventory and review as new plugins/capabilities are added. A permission policy alone does not replace GitHub repository permissions or Kubernetes RBAC.

## Quality gates and catalogue governance

[`scripts/validate-catalog.mjs`](https://github.com/AZ1600/platform-engineering-backstage-portal/blob/main/scripts/validate-catalog.mjs) checks structure, entity type, duplicate refs, ownership and relationships. It helps catch broken catalogue links before publication.

**Review checklist:**

- [ ] Owner entity resolves; ownership is not a decorative string.
- [ ] Generated code includes an automated test and CI entry point.
- [ ] Image source/immutability are explicit.
- [ ] ServiceAccount / cloud permissions are minimal.
- [ ] NetworkPolicy matches actual intended callers and egress dependencies.
- [ ] Secret injection is defined without committing credentials.
- [ ] Template defaults are tested and versioned; exceptions can be requested.

## Local validation (in the Backstage repository)

Read `package.json` and the project's README for the current supported toolchain before running the scripts. A source-level command exists:

```bash
cd /path/to/platform-engineering-backstage-portal
node scripts/validate-catalog.mjs
```

The script requires the repository's Node dependencies (including `yaml`); install per its repo instructions first. It is not run as part of building this handbook.

## Exercise

A team requests a “production-ready” service. The generated CI succeeds, but the image is `latest`, ingress accepts any source on port 8000 and metadata names an inactive owner. Describe three separate corrections, who approves them and how you would test each one.
