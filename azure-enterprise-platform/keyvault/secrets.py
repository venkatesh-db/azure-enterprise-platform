from azure.keyvault.secrets import SecretClient
from auth import get_credential

def get_secret(vault_name, secret_name):
    url = f"https://{vault_name}.vault.azure.net"
    client = SecretClient(url, get_credential())
    return client.get_secret(secret_name).value
