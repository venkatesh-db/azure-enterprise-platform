import yaml
from azure.mgmt.storage import StorageManagementClient
from auth import get_credential

with open("config/platform.yml") as f:
    cfg = yaml.safe_load(f)

client = StorageManagementClient(
    get_credential(),
    cfg["subscription_id"]
)

print("Creating Storage Account...")

client.storage_accounts.begin_create(
    cfg["resource_group"],
    cfg["storage"]["account"],
    {
        "location": cfg["location"],
        "sku": {"name": "Standard_LRS"},
        "kind": "StorageV2"
    }
).result()

print("Storage created")
