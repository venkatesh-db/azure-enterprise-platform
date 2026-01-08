import yaml
from azure.mgmt.compute import ComputeManagementClient
from auth import get_credential

with open("config/platform.yml") as f:
    cfg = yaml.safe_load(f)

client = ComputeManagementClient(
    get_credential(),
    cfg["subscription_id"]
)

print("Creating VM Scale Set...")

client.virtual_machine_scale_sets.begin_create_or_update(
    cfg["resource_group"],
    cfg["vmss"]["name"],
    {
        "location": cfg["location"],
        "sku": {
            "name": cfg["vm"]["size"],
            "capacity": cfg["vmss"]["capacity"]
        },
        "upgrade_policy": {"mode": "Automatic"},
        "virtual_machine_profile": {
            "storage_profile": {
                "image_reference": {
                    "id": "/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Compute/images/golden-image-v1"
                    .format(cfg["subscription_id"], cfg["resource_group"])
                }
            },
            "os_profile": {
                "computer_name_prefix": "vmss"
            }
        }
    }
).result()

print("VMSS created")

