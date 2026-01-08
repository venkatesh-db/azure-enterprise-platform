import yaml
from azure.mgmt.network import NetworkManagementClient
from auth import get_credential
import logging
import time

with open("config/platform.yml") as f:
    cfg = yaml.safe_load(f)

client = NetworkManagementClient(
    get_credential(),
    cfg["subscription_id"]
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("network")

logger.info("Creating VNET...")
poller = client.virtual_networks.begin_create_or_update(
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
)

while not poller.done():
    logger.info("Waiting for VNET creation to complete...")
    time.sleep(10)  # Wait for 10 seconds before checking again

logger.info("VNET created successfully.")
