# 04 — Azure Private Link, DNS and Network Scope

**Goal:** Explain why a Private Endpoint alone is insufficient to prove that an application is using a private network path.

## AZ-104 lab evidence

The [AZ-104 entry Bicep](https://github.com/AZ1600/az104-azure-infrastructure-lab/blob/main/azuredeploy.bicep) provisions a compute VNet and a Blob storage private endpoint. The [private-endpoint module](https://github.com/AZ1600/az104-azure-infrastructure-lab/blob/main/modules/storage-private-endpoint.bicep) configures a private DNS zone, VNet link, endpoint and DNS zone group. The README documents a private Linux VM using system-assigned identity and scoped `Storage Blob Data Reader` access.

```text
Linux VM (no public IP)
  | DNS resolves storage account hostname
  v
Private DNS zone linked to compute VNet
  | resolves to private endpoint IP
  v
Private Endpoint NIC -> Azure Blob Storage data plane

Separately:
VM managed identity -> Microsoft Entra ID -> Storage Blob Data Reader
```

Private connectivity, authentication and permission are three distinct checks. Private DNS is scoped: resolving a private address on a laptop outside the VNet may require VPN or another connected path. A public DNS lookup outside the VNet cannot conclusively test in-VNet resolution.

## Investigation order

1. Confirm **where** the client actually runs and which VNet/subnet its network interface uses.
2. Check whether the DNS zone is linked to the **client VNet** and the endpoint has an approved connection.
3. From a diagnostic host **inside that VNet**, resolve the service hostname and record the resulting private address.
4. Confirm TCP 443 reachability to that private address (without uploading secrets).
5. Finally test application authentication and data-plane RBAC; network access alone never grants data permissions.

Illustrative read-only CLI checks (requires Azure login, correct subscription, and substituted resource details):

```bash
az account show --query '{id:id,name:name}' -o json
az network private-endpoint list --resource-group YOUR_RG -o table
az network private-dns zone list --resource-group YOUR_RG -o table
az network private-dns link vnet list \
  --resource-group YOUR_RG \
  --zone-name 'privatelink.blob.core.windows.net' -o table
```

## Important PropertyOps distinction

The [PropertyOps Bicep network module](https://github.com/AZ1600/AI-property-operations/blob/main/infra/modules/network.bicep) provisions a VNet, a **reserved Container Apps subnet** and a private-endpoint subnet. The [entry Bicep](https://github.com/AZ1600/AI-property-operations/blob/main/infra/main.bicep) explicitly notes that the existing Container Apps Environment cannot be migrated *in place* to the new VNet. It provisions the network for a **future replacement environment**, while deploying private endpoints separately. Therefore, **do not assert that current PropertyOps application traffic is already fully private** merely because private endpoints exist.

## Failure lab — DNS resolves publicly

Possible causes: the test is executed outside the linked VNet; the wrong DNS zone is linked; custom DNS forwarders do not resolve the `privatelink` domain; or the client belongs to the current non-VNet-integrated Container Apps environment.

**Evidence and decision:** Identify the client network before updating any DNS setting. Validate with a host actually inside the intended network. Record whether this was code inspection, read-only cloud observation, or a demonstrated request path.

Next: [Bicep, What-If and RBAC](05-bicep-whatif-rbac.md).
