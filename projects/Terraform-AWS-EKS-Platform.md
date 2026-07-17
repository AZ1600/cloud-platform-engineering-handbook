# Terraform AWS EKS Platform

> An infrastructure-as-code project for defining an Amazon EKS platform with Terraform.

**Status:** Project named in the supplied brief; implementation details pending verification  
**Repository:** <https://github.com/AZ1600/platform-engineering-terraform-eks>  
**Last verified:** 2026-07-11 against the repository README

## Core Engineering Narrative

This project should demonstrate how a Kubernetes platform on AWS can be represented as reviewable, repeatable infrastructure code. The finished case study should explain the infrastructure boundary, module design, state handling, networking, cluster access, security, deployment workflow, cost considerations, and teardown process.

## Architecture Questions

- Does the project create or reuse a VPC?
- Which public and private subnets exist, and why?
- How are the EKS control plane and worker capacity configured?
- Which IAM roles and policies are created?
- Where is Terraform state stored and locked?
- How are versions and providers constrained?
- What is installed in the cluster after creation?
- How are changes reviewed and safely applied?

## Evidence Checklist

- [ ] Repository and version constraints linked
- [ ] Module and state strategy documented
- [ ] Network diagram added
- [ ] IAM and Kubernetes access boundaries explained
- [ ] Plan/apply/destroy workflow tested
- [ ] CI checks and security scans linked
- [ ] Cost and cleanup guidance included
- [ ] One trade-off and one lesson learned recorded

## Verified Documentation Debugging Story

Repository evidence shows a filename correction for the Kubernetes proof screenshots. Commit [`90d328d`](https://github.com/AZ1600/platform-engineering-terraform-eks/commit/90d328d435b60babf815278ea6de46348e2d95e3) standardised them as `kubectl-get-nodes.png` and `kubectl-get-pods.png`. The prevention lesson is to validate Markdown image paths automatically in CI.

See [Terraform EKS screenshots did not use the expected filenames](../DEBUGGING-ISSUE-REGISTER.md#_4-terraform-eks-screenshots-did-not-use-the-expected-filenames).

## Related Handbook Chapters

- [Cloud Computing Fundamentals](../01-Cloud-Fundamentals/Chapter-01-Cloud-Computing.md)
- [Linux Fundamentals](../02-Linux/Chapter-02-Linux.md)
- [Kubernetes Fundamentals](../04-Kubernetes/Chapter-04-Kubernetes.md)
- [AWS Fundamentals](../05-AWS/Chapter-05-AWS.md)
