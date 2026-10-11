# 09 — STAR Stories Without Inflating Evidence

> Use these as **research outlines**, not autobiography scripts. Add only actions you personally performed and results you can document. Do not assign yourself ownership of an entire repository or claim an incident affected production users without proof.

## Story A — OpsPilot storage path and serverless runtime

**Situation (documented):** a local file/OAuth token path assumed a writable project directory. **Task:** make the demo fallback compatible with a serverless runtime without representing ephemeral `/tmp` as durable storage. **Action to verify personally:** examine the storage helper and the actual commit; explain the shared abstraction and why it matters. **Result evidence:** [documented fix commit](https://github.com/AZ1600/opspilot-saas/commit/9d8385e638c97ba840216e31cc370caa8aa4a573). **Limit:** persistence across cold starts is not guaranteed with temporary storage.

Answer follow-up: Why is PostgreSQL the appropriate durable data layer? How would you test a deployment where the filesystem is read-only?

## Story B — CloudOps risk scan feedback

**Situation (documented):** a risk scan state transition was not obvious in the UI. **Task:** make the operation observable to the user. **Action to verify personally:** trace the scan run counter and accessible status text. **Result evidence:** [documented commit](https://github.com/AZ1600/cloudops-command-center/commit/53633daa0b744f7eed6134fe719319faefa3a433). **Limit:** no quantified user efficiency improvement has been verified.

Answer follow-up: Why can ambiguous confirmation lead to unsafe repeated operations? What component test would you add?

## Story C — VitePress project index routing

**Situation (documented):** `/projects/` returned a 404 despite a `projects/README.md`. **Task:** make the project index routable. **Action to verify personally:** explain that VitePress maps a directory URL to `index.md` and GitHub displays `README.md` by convention. **Result evidence:** [Debugging and Issue Register](../DEBUGGING-ISSUE-REGISTER.md). **Limit:** this is a documentation-routing bug, not a customer-facing production incident.

## Story D — EKS image pull/startup triage

The [Pharmacy EKS case study](../projects/Pharmacy-API-EKS.md) describes image pull and crash-loop work; however, the [Issue Register](../DEBUGGING-ISSUE-REGISTER.md) notes that exact incident timelines need reconstruction. Prepare the diagnostic approach now; fill a real STAR only after recovering concrete Events/logs, changed manifest or commit, and recovery proof.

## Truth checklist for each story

- [ ] I can specify **my own contribution** rather than claiming everything in the repository.
- [ ] I have a verifiable before/after artifact or state that a reviewer can inspect.
- [ ] Results are measured only where a metric exists.
- [ ] The story is labelled verified, reported, simulated or review-discovered.
- [ ] I can explain what I would improve next.

## Personal rehearsal template

**S:** [When/where; avoid unsupported production claims]

**T:** [Your actual responsibility and criteria]

**A:** [Exact investigation and change you personally performed]

**R:** [Link a commit/test/output; distinguish observation from inference]

**L:** [Limitation and prevention action]
