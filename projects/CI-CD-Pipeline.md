# Platform Engineering CI/CD Pipeline

> A GitHub Actions pipeline that builds a Docker image and publishes it to Amazon ECR after changes reach the main branch.

**Repository:** <https://github.com/AZ1600/platform-engineering-cicd-pipeline>  
**Last verified:** 2026-07-11 against the repository README

## Delivery Flow

```text
Git push -> GitHub Actions -> Docker build -> AWS authentication
         -> ECR login -> image tag -> ECR push
```

## What It Demonstrates

- Automated container build and publication.
- GitHub Actions workflow design.
- AWS IAM and secret-based authentication.
- Amazon ECR image storage.
- Evidence of a successful workflow and published image.

## Production Improvements

- Prefer GitHub OIDC and short-lived AWS credentials over long-lived access keys.
- Add automated tests, linting, dependency checks, and image scanning before publication.
- Use immutable tags connected to a commit or release.
- Add a controlled deployment stage rather than treating image publication as deployment.
- Separate environment approvals and rollback procedures.
