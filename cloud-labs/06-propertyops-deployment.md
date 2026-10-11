# 06 — PropertyOps: Azure Identity and Deployment Boundaries

**Goal:** Review an actual Azure application project without confusing successfully provisioned infrastructure with end-to-end private application networking.

## Request, identity and deployment paths

```text
User -> HTTPS ingress -> Azure Container Apps -> FastAPI -> PostgreSQL
             |                |                    |
      Microsoft Entra ID   managed identity     application roles
      authentication      Key Vault / ACR       and audit records

GitHub Actions -> Azure OIDC -> Azure Container Registry
                                 -> Container App image update
```

The [PropertyOps application](https://github.com/AZ1600/AI-property-operations) includes FastAPI, database models, authorization and operational triage. The [CI workflow](https://github.com/AZ1600/AI-property-operations/blob/main/.github/workflows/deploy.yml) tests on pull requests and deploys on `main`/manual events, authenticates to Azure with OIDC, builds an image tagged with the commit SHA, pushes to ACR and updates the Container App. An image tagged with a SHA is version-addressable; an immutable digest or registry tag protection is a separate supply-chain control and should not be presumed.

## Current versus future topology

The [Container Apps Environment module](https://github.com/AZ1600/AI-property-operations/blob/main/infra/modules/container-environment.bicep) currently specifies `publicNetworkAccess: 'Enabled'` and has **no VNet infrastructure-subnet reference**. The [entry Bicep file](https://github.com/AZ1600/AI-property-operations/blob/main/infra/main.bicep) explicitly calls the new VNet a foundation for a *future replacement environment*.

The private endpoints for PostgreSQL and Key Vault demonstrate infrastructure provisioning; they **do not alone prove** that the existing app currently communicates over Private Link. Preserve this distinction in screenshots, interview answers and production-readiness reviews.

## Follow the role and secret flows

The [Container App Bicep module](https://github.com/AZ1600/AI-property-operations/blob/main/infra/modules/container-app.bicep) attaches user-assigned managed identities for ACR pulls and runtime access to Key Vault. A secret named `database-url` is referenced through Key Vault. The application also has an Entra auth configuration and app-level roles. For any incident, first distinguish authentication failure, cloud resource authorization failure, database connection failure and network/DNS failure.

## Read-only cloud investigation commands

```bash
az account show --query '{name:name,id:id}' -o json
az containerapp show \
  --name YOUR_CONTAINER_APP \
  --resource-group YOUR_RG \
  --query '{image:properties.template.containers[0].image,environment:properties.environmentId,ingress:properties.configuration.ingress.external}' \
  -o json
az containerapp revision list \
  --name YOUR_CONTAINER_APP \
  --resource-group YOUR_RG -o table
```

Cloud commands require approved Azure access and should not be run with copied sample resource names against unknown subscriptions. Publicly shared evidence should be redacted.

## Failure exercise — deployment succeeds but database fails

1. Confirm the deployed image revision, event time and whether tests passed at that commit.
2. Verify the application's `DATABASE_URL` secret reference resolves, without printing the secret itself.
3. Identify where the running Container App lives and whether it can reach the configured database endpoint.
4. Test DNS resolution from the correct runtime network, then investigate NSGs/firewalls/private endpoint path as applicable.
5. Separate a DB `401/403`, TLS mismatch, timeout, and connection refused: they suggest different root causes.

**Architecture question:** What deployment migration steps would be necessary to move the app to the prepared VNet-integrated environment? Consider new environment provisioning, identity, DNS, network access, data migration assumptions, a canary, rollback and observability.

Next: [Cross-cloud troubleshooting](07-cross-cloud-troubleshooting.md).
