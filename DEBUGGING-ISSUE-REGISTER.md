# Debugging and Incident Register

> A project is not understood fully until I can explain what failed, what evidence I collected, why it failed, what changed, and how I know the change worked.

This register records debugging stories across the handbook and its projects. It deliberately separates proven events from incomplete recollections and simulated failures. That makes the stories useful in interviews without overstating the evidence.

## Evidence labels

| Label | Meaning |
|---|---|
| **Verified solved** | A repository change, build result, screenshot, log, test, or current implementation shows both the problem and the correction. |
| **Reported solved** | The project README says the issue was resolved, but the exact root cause, command sequence, or code change has not yet been recovered. |
| **Review-discovered** | Code review exposed a defect or risk. It is not described as solved until a later change and verification prove that. |
| **Simulated failure** | The failure was created intentionally for learning or demonstration. It is not a production incident. |

## The debugging method I should explain

For every issue, I should be able to walk through this sequence:

1. **Symptom:** what I or the user observed.
2. **Impact:** what stopped working or became unsafe.
3. **Scope:** whether the fault was in the browser, application, container, cluster, cloud service, permissions, data, or delivery pipeline.
4. **Evidence:** logs, events, status output, network responses, tests, diffs, or monitoring data.
5. **Root cause:** the underlying reason, not merely the error message.
6. **Fix and verification:** the change made and the proof that normal behaviour returned.
7. **Prevention:** the test, validation, alert, documentation, or design improvement that reduces recurrence.

## 1. Handbook Projects page returned 404

**Status:** Verified solved on 2026-07-18.

**Symptom:** selecting **Projects** opened `/projects/`, but VitePress displayed `404 PAGE NOT FOUND`.

**Impact:** the project catalogue could not be reached from the main navigation even though the individual Markdown case studies existed.

**Investigation:** the navigation configuration correctly linked to `/projects/`. The `projects` directory contained `README.md`, but VitePress requires `index.md` to serve the directory route.

**Root cause:** GitHub automatically displays `README.md` for a directory, while VitePress maps `/projects/` to `projects/index.md`. The two tools use different directory-entry conventions.

**Fix:** added `projects/index.md` and used VitePress's Markdown include directive to render `projects/README.md`. This keeps one catalogue source instead of maintaining two copies.

**Verification:** the production build completed, `/projects/` rendered **Project Index**, and the PlatformPilot link opened `/projects/PlatformPilot`.

**Prevention:** add a navigation smoke test that opens Home, Projects, Commands, Interview, one chapter, and one project after every site build.

## 2. OpsPilot could not safely write demo files on Vercel

**Status:** Verified solved in repository commit [`9d8385e`](https://github.com/AZ1600/opspilot-saas/commit/9d8385e638c97ba840216e31cc370caa8aa4a573).

**Symptom:** the local file repository and Gmail OAuth token store used `process.cwd()/data`. That works on a normal development machine but is not a safe writable location for a Vercel serverless runtime.

**Impact:** workspace or OAuth-token writes could fail after deployment even though local development worked.

**Investigation:** compare the runtime environment with the local environment. The application was relying on a persistent writable project directory, but a serverless deployment has a read-only application bundle and only temporary writable storage.

**Root cause:** the storage path was coupled to the local filesystem model.

**Fix:** introduced `getWritableDataDir()`:

- use `OPSPILOT_FILE_STORAGE_DIR` when explicitly configured;
- use `/tmp/opspilot-data` when `VERCEL` is present;
- otherwise use the local `data` directory.

Both the workspace store and OAuth token store were changed to use that function.

**Verification:** the commit shows every affected write path using the shared runtime-aware directory function. Runtime health and deployment validation should still be checked after each deployment.

**Important production lesson:** `/tmp` is ephemeral. It is acceptable for a temporary demo fallback, not durable SaaS storage. Production workspace data belongs in PostgreSQL, and production OAuth tokens need encrypted durable storage.

**Prevention:** test file-dependent code in a production-like runtime and keep persistence behind a repository abstraction.

## 3. CloudOps risk scan gave insufficient visible feedback

**Status:** Verified solved in repository commit [`53633da`](https://github.com/AZ1600/cloudops-command-center/commit/53633daa0b744f7eed6134fe719319faefa3a433).

**Symptom:** running or resetting a risk scan changed application state, but the interface did not clearly confirm that a scan had completed or distinguish one scan run from another.

**Impact:** an operator could click the action and be unsure whether anything happened. This is an operational UX problem because ambiguous feedback encourages repeated actions and weakens trust.

**Root cause:** the state transition existed, but the interface did not expose a scan-completion state.

**Fix:** added a `scanRunCount`, incremented it during reset, and displayed an `aria-live="polite"` scan-status panel containing:

- the scan run number;
- the number of risks found;
- the number of signal sources; and
- how many risks were waiting for approval.

**Verification:** the commit connects the counter to the action and renders the resulting values visibly and accessibly.

**Prevention:** every long-running or state-changing action should have loading, success, empty, and error states. Add a component test that triggers a scan and asserts that the completion message changes.

## 4. Terraform EKS screenshots did not use the expected filenames

**Status:** Verified solved in repository commit [`90d328d`](https://github.com/AZ1600/platform-engineering-terraform-eks/commit/90d328d435b60babf815278ea6de46348e2d95e3).

**Symptom:** documentation screenshot names did not match the intended references.

**Impact:** evidence images could appear broken or become difficult to associate with the commands they prove.

**Root cause:** documentation assets and their expected names had drifted.

**Fix:** corrected the assets to `kubectl-get-nodes.png` and `kubectl-get-pods.png`.

**Prevention:** use predictable lowercase filenames and run a Markdown link/image check in CI.

## 5. Pharmacy API on EKS troubleshooting

**Status:** Reported solved in the repository README; the exact incident timelines still need reconstruction.

The README explicitly reports work on:

- `ImagePullBackOff`;
- `CrashLoopBackOff`;
- container runtime and Python import errors; and
- IAM permissions for Kubernetes workloads.

Those statements are useful evidence that the failure classes were encountered, but they are not yet enough to claim a precise root cause or permanent fix. Until logs, commands, manifests, commits, or a personal account confirm the details, I should explain the investigation method and say that the exact incident record is incomplete.

### ImagePullBackOff investigation

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl get events --sort-by=.lastTimestamp
aws ecr describe-images --repository-name <repository> --region eu-west-2
```

Check whether the image name and tag exist, whether the node can authenticate to ECR, and whether networking permits the pull. The final handbook entry must record which one was the actual cause and the exact manifest or IAM change that fixed it.

### CrashLoopBackOff investigation

```bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
```

The current and previous logs distinguish application startup failure from probe, configuration, permission, dependency, or command problems. The final story must include the real traceback or event and the change that stopped the restart loop.

### Python import/runtime investigation

Reproduce the container locally, read the full traceback, inspect `WORKDIR`, `COPY`, the startup command, package layout, and installed requirements. Record the exact import that failed and whether the correction was a package path, Docker build context, dependency, or Uvicorn module change.

### IAM investigation

Identify the exact denied AWS action and the identity used by the pod. Confirm whether permissions came from the worker-node role, mounted credentials, or IRSA. The permanent fix should grant only the required actions to a workload-specific role and then re-run the failed request.

## 6. PlatformPilot defects found during review

**Status:** Review-discovered; do not describe these as solved yet.

| Finding | Why it matters | Required fix and proof |
|---|---|---|
| Frontend expects flat summary fields while the API returns nested objects | The AI Summary can display missing or incorrect values | Align the schema and TypeScript type; add a frontend/backend contract test |
| Unknown pod states can fall back to “No issues detected” | An unrecognised failure can be presented as healthy | Return `unclassified`; test Pending, Evicted, config errors, and unknown reasons |
| Only the first container status is inspected | A failed sidecar or init container can be missed | Inspect every init and application container; test multi-container pods |
| Some resource operations assume the default namespace | Results and links can refer to the wrong workload | Include namespace in routes and resource identity; test duplicate names across namespaces |
| Local kubeconfig is the only authentication path | The backend is not ready for safe in-cluster deployment | Add ServiceAccount authentication and least-privilege RBAC; verify with `kubectl auth can-i` |

These are strong engineering lessons, but honesty matters: discovering a defect is not the same as fixing it.

## How to reconstruct an incomplete debugging story

For each reported issue, recover as much of the following as possible:

- the approximate date;
- the exact error message or screenshot;
- the command that exposed the useful evidence;
- the wrong configuration, code, permission, or assumption;
- the file or cloud setting that changed;
- the successful verification output; and
- what would prevent the same problem now.

If the evidence no longer exists, write **“reconstructed from memory”** and avoid invented command output.

## Interview explanation pattern

Use a concise structure:

> While building **[project]**, I observed **[symptom and impact]**. I first checked **[evidence]**, which ruled out **[alternative]** and showed **[root cause]**. I changed **[specific code/configuration]** and verified the fix with **[test, log, status, or deployment]**. To prevent recurrence, I would add **[test, validation, alert, or design improvement]**.

That answer demonstrates diagnosis, evidence, technical judgement, verification, and learning—not just command memorisation.
