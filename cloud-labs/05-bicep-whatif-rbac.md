# 05 — Bicep, What-If and Scoped Azure RBAC

**Goal:** Describe a reviewable, least-privilege Azure infrastructure change from module inputs through proposed changes to post-deployment validation.

## Module and ownership boundaries

The [AZ-104 lab](https://github.com/AZ1600/az104-azure-infrastructure-lab) splits compute/networking, Bastion, storage private endpoints, role assignments and backup into Bicep modules. In its [RBAC module](https://github.com/AZ1600/az104-azure-infrastructure-lab/blob/main/modules/rbac.bicep), the `Storage Blob Data Reader` role is assigned at the **storage account** scope. The name of the assignment is generated deterministically from the scope, principal resource ID and role definition.

The fact that a VM has no public IP says nothing about whether its managed identity can read a blob; conversely, granting Blob Data Reader does not make the network path private. Treat each as a separate test.

## Safe workflow

Work from a dedicated test subscription, and avoid applying anything without explicitly reviewing expected resources and costs.

```bash
az account show --query '{id:id,name:name,tenantId:tenantId}' -o json
az bicep version
az bicep build --file azuredeploy.bicep
# Read-only prediction against an existing resource group; may require Azure access:
az deployment group what-if \
  --resource-group YOUR_RG \
  --template-file azuredeploy.bicep \
  --parameters storageAccountName=YOUR_EXISTING_STORAGE
```

Read parameters in the repo before running What-If. The what-if command may reveal resource names and sensitive structure; handle output accordingly. It is a prediction, **not a guarantee** of a successful deployment or a no-impact change.

## Interpret Bicep output

- **Create:** Does the resource belong in this Region and resource group? Is the estimated cost acceptable?
- **Modify:** Will networking, identity or encryption settings be weakened?
- **Delete:** Is the resource deliberately relinquished, and has data retention been assessed?
- **No change:** Does the preview target the correct subscription, resource group and parameter values?

Be careful with cross-region differences: the AZ-104 README describes earlier compute SKU restrictions and a Denmark East compute environment alongside a UK South project foundation. A Bicep file's default `resourceGroup().location` should not be assumed to identify every deployed resource's location.

## Failure exercise — managed identity cannot read storage

1. Verify the principal object ID from the **current deployment** rather than copying a previous example.
2. Inspect the role assignment at the correct storage account scope (management-plane Reader is **not** the same as Blob Data Reader).
3. Check credential acquisition through the managed identity path.
4. Verify the Blob endpoint path and private DNS independently.
5. Consider assignment propagation time before concluding the role has failed.

Read-only checks:

```bash
az role assignment list \
  --assignee-object-id YOUR_PRINCIPAL_OBJECT_ID \
  --scope YOUR_STORAGE_RESOURCE_ID \
  -o table

az deployment group list --resource-group YOUR_RG \
  --query '[].{name:name,state:properties.provisioningState}' -o table
```

**Engineering decision record:** Document why storage-scoped Blob Data Reader is appropriate, what a narrower data scope would change, and the remaining risks of allowing a public endpoint or broad network rules.

Next: [PropertyOps deployment boundaries](06-propertyops-deployment.md).
