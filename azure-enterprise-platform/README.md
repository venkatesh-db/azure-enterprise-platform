
# Azure Enterprise Platform Automation

This repository automates Azure infrastructure using:
- Azure VM Scale Sets
- Golden Images (Packer)
- DSC configuration
- Python Azure SDKs
- Azure Key Vault
- Cross-platform CI/CD

## Prerequisites
- Azure subscription
- Python 3.9+
- Azure CLI
- Packer

## Execution Order
1. Network
2. Storage
3. Golden Image
4. VM Scale Set

## Run Locally
```bash
python3 python/network.py
python3 python/storage.py
packer build images/packer-golden-image.json
python3 python/vmss.py
