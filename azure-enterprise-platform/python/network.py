
import yaml
from azure.mgmt.network import NetworkManagementClient
from auth import get_credential

with open("config/platform.yml") as f:
    cfg = yaml.safe_load(f)

client = NetworkManagementClient(
    get_credential(),
    cfg["subscription_id"]
)

print("Creating VNET...")

client.virtual_networks.begin_create_or_update(
    cfg["resource_group"],
    cfg["network"]["vnet"],
    {
        "location": cfg["location"],
        "address_space": {"address_prefixes": ["10.0.0.0/16"]},
        "subnets": [{
            "name": cfg["network"]["subnet"],
            "address_prefix": "10.0.1.0/24"
        }]
    }
).result()

print("VNET created")
