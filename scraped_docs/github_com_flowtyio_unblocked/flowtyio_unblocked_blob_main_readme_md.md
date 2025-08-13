# Source: https://github.com/Flowtyio/unblocked/blob/main/README.md

# TenantService

This repo contains contract definitions made by Unblocked and include:

- TenantService
- StorefrontService
- NFTCollections

Currently, only `TenantService` is configured in this project's flow.json, but all contracts have been upgraded and are able to be staged.

Identified Tenant Serive Addresses:
- A.7960dc9ac1429491.TenantService
- A.cda0b95fd3331a7a.TenantService
- A.965411a02ca21b87.TenantService
- A.c5d17676be69bb9a.TenantService
- A.3c9e63822c614a3a.TenantService

## Staging instructions

1. Install dependencies
    ```
    npm i
    ```
1. Install the latest flow-cli:
    ```
    sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
    ```
1. Verify that the command `flow-c1` is present on your device
    ```
    flow-c1 version
    ```
1. Replace the address used in the tenant-account entry in flow.json with the address being migrated
    ```
    {
    ...
    "accounts": {
        ...
        "tenant-account": {
            "address": "0x1", // Change the address here
            "key": {
                "index": 0,
                "type": "file",
                "location": "tenant-account.pkey"
                }
            },
            ...
        },
        ...
        "deployments": {
            ...
            "mainnet": {
                "tenant-account": [
                    "TenantService"
                ]
            }
        }
    }
    ```
1. Create the file `tenant-account.pkey`
1. Put the key of the account you are migrating in this file
    1. **NOTE: Ensure that the index of the key you are using matches the key index (set to 0 currently)**
1. You can ensure that you have the necessary access to an account by running a dummy transaction which does nothing:
    ```
    flow-c1 transactions send ./transactions/dummy.cdc -signer tenant-account -n mainnet
    ```
1. Run the staging command
    ```
    flow-c1 migrate stage --network mainnet
    ```
