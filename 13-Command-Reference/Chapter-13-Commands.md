# Chapter 13 — Commands Used Across My Projects

> A project-based command reference. Every command includes its purpose, context and evidence level so I understand what I am running instead of memorising syntax.

**Last verified against repositories:** 2026-07-17

## 1. How to Use This Reference

Before running a command:

1. Confirm the current directory.
2. Understand which account, cluster, region, database or repository it affects.
3. Replace placeholders deliberately.
4. Run read-only validation before mutation where possible.
5. Never paste real credentials into a command that may enter shell history.
6. Treat `deploy`, `apply`, `destroy`, `delete` and database schema commands as state-changing operations.

Labels used below:

- **Repository verified:** present in a README or committed script.
- **Derived from configuration:** supported by `package.json`, Compose or another committed configuration file.
- **Recommended diagnostic:** added to explain and operate the project safely.

## 2. Git and Repository Workflow

### Clone PlatformPilot

```bash
git clone https://github.com/AZ1600/platform-pilot.git
cd platform-pilot
```

**Purpose:** create a local copy and enter its root directory.  
**Evidence:** repository verified in PlatformPilot README.

### Inspect changes before committing

```bash
git status --short
git diff
```

**Purpose:** show changed/untracked files and inspect unstaged content.  
**Evidence:** recommended diagnostic used while maintaining this handbook.

### Search handbook files

```bash
rg --files
rg -n "search text" .
```

**Purpose:** list files or find text with line numbers.  
**Evidence:** commands used to inspect and maintain this handbook.

## 3. PlatformPilot

### Backend environment

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

**Purpose:** create an isolated Python environment, install pinned dependencies and start the FastAPI development server.  
**Evidence:** repository verified.

Windows activation:

```powershell
venv\Scripts\activate
```

### Frontend environment

```bash
cd frontend
npm install
npm run dev
```

**Purpose:** install frontend dependencies and start Vite’s development server.  
**Evidence:** repository verified.

### Frontend validation and production preview

```bash
npm run lint
npm run build
npm run preview
```

**Purpose:** lint source, create a production bundle and serve the built bundle locally.  
**Evidence:** derived from `frontend/package.json`.

### Confirm local dependencies

```bash
curl http://127.0.0.1:8000/health
kubectl cluster-info
kubectl get pods -A
```

**Purpose:** check FastAPI process health and Kubernetes access.  
**Evidence:** recommended diagnostics; the health endpoint is code verified.

## 4. CloudOps Command Center

### Install and run

```bash
npm install
npm run dev
```

**Purpose:** install dependencies and start the Next.js development server.  
**Evidence:** repository verified.

### Full validation

```bash
npm run lint
npm run typecheck
npm run test
npm run build
```

**Purpose:** check style/static rules, TypeScript types, Vitest tests and production compilation.  
**Evidence:** repository verified.

### Apply the configured database schema

```bash
npm run db:apply
```

**Purpose:** run `scripts/apply-schema.mjs` against the configured database.  
**Risk:** state-changing; verify `DATABASE_URL` and target environment first.  
**Evidence:** repository verified and package-script verified.

### Start a built production server

```bash
npm run build
npm run start
```

**Purpose:** build and start Next.js in production mode.  
**Evidence:** derived from `package.json`.

## 5. OpsPilot SaaS

### Install and run

```bash
npm install
npm run dev
```

**Evidence:** repository verified.

### Validate application quality

```bash
npm run test
npm run lint
npm run typecheck
npm run build
npm run check:config
```

**Purpose:** run unit tests, linting, type analysis, production build and runtime configuration checks.  
**Evidence:** repository verified.

### Database checks

```bash
npm run db:check
npm run db:schema
```

**Purpose:** check database connectivity/configuration, then apply the schema.  
**Risk:** `db:schema` changes the configured database; inspect environment variables first.  
**Evidence:** repository and package-script verified.

### Reproducible CI installation

```bash
npm ci
npm run test
npm run lint
npm run typecheck
npm run build
```

**Purpose:** install exactly from the lockfile and execute the CI validation chain.  
**Evidence:** repository verified.

## 6. Pharmacy API — Docker and EKS

### Build and run the container locally

```bash
docker build -t pharmacy-api .
docker run -p 8000:8000 pharmacy-api
```

**Purpose:** build the application image and map host port 8000 to container port 8000.  
**Evidence:** repository verified.

### Deploy Kubernetes resources

```bash
kubectl apply -f k8s/
```

**Purpose:** create or update the Deployment, Service and Ingress from committed manifests.  
**Risk:** changes the active Kubernetes context; run `kubectl config current-context` first.  
**Evidence:** repository verified.

### Verify the deployment

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress
kubectl rollout status deployment/pharmacy-api
```

**Purpose:** inspect desired/ready replicas, pods, network services, ingress and rollout completion.  
**Evidence:** first three are repository verified; remaining commands are recommended diagnostics derived from the manifests.

### Troubleshoot a pod

```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
kubectl get events --sort-by=.metadata.creationTimestamp
```

**Purpose:** inspect status/conditions/events, current logs, previous crashed-container logs and chronological events.  
**Evidence:** recommended diagnostics supporting the documented ImagePullBackOff and CrashLoopBackOff lessons.

## 7. Terraform AWS EKS Platform

### Format and initialise

```bash
terraform fmt -check -recursive
terraform init
```

**Purpose:** check formatting and initialise providers/modules/backend.  
**Evidence:** recommended workflow; Terraform usage is repository documented.

### Validate and plan

```bash
terraform validate
terraform plan
```

**Purpose:** validate configuration and preview infrastructure changes.  
**Evidence:** repository verified.

### Apply infrastructure

```bash
terraform apply
```

**Purpose:** create or update VPC, networking, IAM, KMS, EKS and node resources described by the configuration.  
**Risk:** changes AWS resources and can create cost. Review the plan first.  
**Evidence:** repository verified.

### Validate the EKS cluster

```bash
kubectl get nodes
kubectl get pods -A
```

**Purpose:** confirm worker registration and inspect workloads across namespaces.  
**Evidence:** repository verified.

### Destroy the learning environment

```bash
terraform plan -destroy
terraform destroy
```

**Purpose:** preview then remove Terraform-managed resources.  
**Risk:** destructive. Confirm workspace, state and AWS account before approval.  
**Evidence:** destroy is demonstrated in repository screenshots; plan-first command is a safety recommendation.

## 8. Cloud-Native Pharmacy Platform — AWS SAM

### Run the unit test

```bash
python3 -m unittest test_create_drug_lambda.py
```

**Purpose:** execute the committed Lambda unit test.  
**Evidence:** repository verified and CodeBuild verified.

### Build and guided deployment

```bash
sam build
sam deploy --guided
```

**Purpose:** build serverless artifacts and interactively create deployment configuration.  
**Risk:** deployment creates or changes AWS resources and IAM roles.  
**Evidence:** repository verified.

### Automated CodeBuild sequence

```bash
python -m pip install --upgrade pip
pip install aws-sam-cli
python -m unittest test_create_drug_lambda.py
sam build
```

The committed `buildspec.yml` then calls `sam deploy` with stack name, region, S3 resolution, IAM capability and environment parameters.

**Evidence:** code verified from `buildspec.yml`.  
**Security note:** pass environment-specific values through protected build configuration; do not hardcode secrets.

## 9. AI-Powered Content Automation Platform

### Build and deploy

From the repository root:

```bash
sam build -t templates/template.yaml
sam deploy --config-file samconfig.toml --region eu-west-2
```

**Purpose:** build the Lambda/API infrastructure from the selected template and deploy using committed SAM configuration.  
**Risk:** changes AWS resources and may invoke IAM, API Gateway, Lambda, DynamoDB, EventBridge and Secrets Manager operations.  
**Evidence:** repository verified. The machine-specific absolute `cd` path in the README is intentionally not reproduced.

### API workflow examples

```text
GET  /oauth/x/start?account_id=account1
POST /x/plan
POST /x/plan/queue
POST /x/post
POST /x/queue/publish
GET  /x/queue?account_id=account1
GET  /x/activity?account_id=account1
GET  /dashboard
```

**Purpose:** document the application’s account connection, planning, queue, publishing, activity and dashboard flows.  
**Evidence:** repository verified. These are HTTP route definitions, not shell commands.

## 10. AI Resume Analyzer — n8n and Bedrock

### Start n8n

```bash
docker compose up -d
docker compose ps
docker compose logs -f n8n
```

**Purpose:** start the n8n container, inspect status and follow logs. The interface is exposed on port 5678 by the committed Compose file.  
**Evidence:** derived from `docker-compose.yml`.

### Stop the workflow environment

```bash
docker compose down
```

The named `n8n_data` volume remains unless explicitly removed. Do not add `--volumes` unless deletion is intended.

## 11. Observability — Prometheus and Grafana

### Start the stack

```bash
docker compose up -d
```

**Purpose:** start Prometheus on port 9090 and Grafana on port 3000.  
**Evidence:** repository verified.

### Inspect and stop

```bash
docker compose ps
docker compose logs -f prometheus
docker compose logs -f grafana
docker compose down
```

**Purpose:** inspect health/logs and stop containers.  
**Evidence:** derived from the committed Compose services.

## 12. Backstage Developer Portal

The repository requires Node 22 or 24 and declares Yarn 4.4.1.

### Start and validate

```bash
yarn start
yarn lint:all
yarn prettier:check
yarn tsc:full
yarn test
```

**Purpose:** start Backstage, lint the repository, check formatting, run full TypeScript checking and execute tests.  
**Evidence:** derived from `package.json`.

### Build deliverables

```bash
yarn build:all
yarn build:backend
yarn build-image
```

**Purpose:** build all workspaces, build the backend and create the backend image.  
**Evidence:** derived from `package.json`.

### End-to-end tests

```bash
yarn test:e2e
```

**Purpose:** run Playwright tests.  
**Evidence:** derived from `package.json`.

## 13. GitOps with Argo CD

### Validate the committed Kubernetes manifests

```bash
kubectl apply --dry-run=client -f manifests/
kubectl diff -f manifests/
```

**Purpose:** client-side validation followed by comparison with the active cluster.  
**Evidence:** recommended commands derived from the committed manifest directory.

### Apply manually for learning

```bash
kubectl apply -f manifests/
kubectl get deployment nginx
kubectl get service nginx-service
```

**Purpose:** demonstrate the manifests without Argo CD. In the GitOps path, Argo CD should normally perform reconciliation from Git.  
**Evidence:** derived from committed resources.

## 14. Platform Engineering CI/CD Pipeline

The primary “commands” are encoded as GitHub Actions steps:

```text
checkout source
authenticate to AWS
log in to Amazon ECR
build Docker image
tag image
push image to ECR
```

The important lesson is that CI/CD configuration is executable documentation. To reproduce it manually, inspect the workflow first; do not invent registry URLs, regions or credentials.

## 15. Command Safety Checklist

- [ ] I know my current directory.
- [ ] I know the Git branch and changed files.
- [ ] I know the AWS account and region.
- [ ] I know the current Kubernetes context and namespace.
- [ ] I reviewed Terraform or Kubernetes changes before applying.
- [ ] I know which database `DATABASE_URL` targets.
- [ ] I am not exposing credentials in shell history or logs.
- [ ] I know whether the command is read-only, state-changing or destructive.
- [ ] I know how to verify success.
- [ ] I know the rollback or cleanup path.

## 16. Related Handbook Material

- [Project and Work Register](../PROJECT-WORK-REGISTER.md)
- [Technology-to-Project Map](../TECHNOLOGY-PROJECT-MAP.md)
- [Kubernetes Through My Projects](../04-Kubernetes/Chapter-04-Kubernetes.md)
- [PlatformPilot Case Study](../projects/PlatformPilot.md)
- [Project Index](../projects/README.md)
