# Source: https://developers.flow.com/build/tools/flow-cli/flow.json/manage-configuration

Manage Configuration | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/super-commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

      * [Initialize Configuration](/build/tools/flow-cli/flow.json/initialize-configuration)
      * [Configuration](/build/tools/flow-cli/flow.json/configuration)
      * [Manage Configuration](/build/tools/flow-cli/flow.json/manage-configuration)
      * [Security](/build/tools/flow-cli/flow.json/security)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Flow.json
* Manage Configuration

On this page

# Manage Configuration

Instead of manually editing `flow.json`, use the Flow CLI's `config` commands to add, remove, and manage your project configuration. These commands provide validation and ensure your configuration is properly formatted.

## Basic Commands[​](#basic-commands "Direct link to Basic Commands")

`_10

# Add configuration items

_10

flow config add <account|contract|network|deployment>

_10

_10

# Remove configuration items

_10

flow config remove <account|contract|network|deployment>`

## Adding Configuration[​](#adding-configuration "Direct link to Adding Configuration")

### Add an Account[​](#add-an-account "Direct link to Add an Account")

`_10

flow config add account`

You can use flags to specify account details:

`_10

flow config add account \

_10

--name my-testnet-account \

_10

--address f8d6e0586b0a20c7 \

_10

--private-key ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee \

_10

--sig-algo ECDSA_P256 \

_10

--hash-algo SHA3_256 \

_10

--key-index 0`

**Available flags:**

* `--name`: Account name
* `--address`: Account address
* `--private-key`: Private key
* `--sig-algo`: Signature algorithm (default: ECDSA\_P256)
* `--hash-algo`: Hash algorithm (default: SHA3\_256)
* `--key-index`: Key index (default: 0)

**What gets added to `flow.json`:**

`_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "f8d6e0586b0a20c7",

_10

"key": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee"

_10

}

_10

}`

### Add a Contract[​](#add-a-contract "Direct link to Add a Contract")

`_10

flow config add contract`

You can use flags to specify contract details:

`_10

flow config add contract \

_10

--name MyToken \

_10

--filename ./cadence/contracts/MyToken.cdc \

_10

--testnet-alias 9a0766d93b6608b7 \

_10

--mainnet-alias f233dcee88fe0abe`

**Available flags:**

* `--name`: Contract name
* `--filename`: Path to contract source file
* `--testnet-alias`: Address for testnet alias
* `--mainnet-alias`: Address for mainnet alias
* `--emulator-alias`: Address for emulator alias

**What gets added to `flow.json`:**

`_10

"contracts": {

_10

"MyToken": {

_10

"source": "./cadence/contracts/MyToken.cdc",

_10

"aliases": {

_10

"testnet": "9a0766d93b6608b7",

_10

"mainnet": "f233dcee88fe0abe"

_10

}

_10

}

_10

}`

### Add a Network[​](#add-a-network "Direct link to Add a Network")

`_10

flow config add network`

You can use flags to specify network details:

`_10

flow config add network \

_10

--name custom-testnet \

_10

--host access-001.devnet30.nodes.onflow.org:9001 \

_10

--network-key ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d`

**Available flags:**

* `--name`: Network name
* `--host`: Flow Access API host address
* `--network-key`: Network key for secure connections

**What gets added to `flow.json`:**

`_10

"networks": {

_10

"custom-testnet": {

_10

"host": "access-001.devnet30.nodes.onflow.org:9001",

_10

"key": "ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d"

_10

}

_10

}`

### Add a Deployment[​](#add-a-deployment "Direct link to Add a Deployment")

`_10

flow config add deployment`

You can use flags to specify deployment details:

`_10

flow config add deployment \

_10

--network testnet \

_10

--account my-testnet-account \

_10

--contract MyToken`

**Available flags:**

* `--network`: Network name for deployment
* `--account`: Account name for deployment
* `--contract`: Contract name(s) to deploy (can specify multiple)

**What gets added to `flow.json`:**

`_10

"deployments": {

_10

"testnet": {

_10

"my-testnet-account": ["MyToken"]

_10

}

_10

}`

## Removing Configuration[​](#removing-configuration "Direct link to Removing Configuration")

### Remove an Account[​](#remove-an-account "Direct link to Remove an Account")

`_10

flow config remove account my-testnet-account`

### Remove a Contract[​](#remove-a-contract "Direct link to Remove a Contract")

`_10

flow config remove contract MyToken`

### Remove a Network[​](#remove-a-network "Direct link to Remove a Network")

`_10

flow config remove network custom-testnet`

### Remove a Deployment[​](#remove-a-deployment "Direct link to Remove a Deployment")

`_10

flow config remove deployment my-testnet-account testnet`

**Note:** This removes all deployments for the specified account on the specified network.

## Configuration File Management[​](#configuration-file-management "Direct link to Configuration File Management")

### Using Custom Configuration Files[​](#using-custom-configuration-files "Direct link to Using Custom Configuration Files")

`_10

# Use a specific configuration file

_10

flow config add account --config-path ./config/flow.json

_10

_10

# Use multiple configuration files (merged in order)

_10

flow config add account -f flow.json -f private.json`

### Configuration File Priority[​](#configuration-file-priority "Direct link to Configuration File Priority")

When using multiple configuration files with `-f` flag:

1. Files are merged from left to right
2. Later files override earlier ones for overlapping properties
3. Non-overlapping properties are combined

**Example:**

`_10

flow config add account -f flow.json -f private.json`

If both files have an `admin-account`, the one from `private.json` will be used.

### Security Best Practices[​](#security-best-practices "Direct link to Security Best Practices")

For better security, consider using separate configuration files for sensitive data:

**Main configuration file (`flow.json`):**

`_11

{

_11

"accounts": {

_11

"my-testnet-account": {

_11

"address": "3ae53cb6e3f42a79",

_11

"key": {

_11

"type": "file",

_11

"location": "./my-testnet-account.key"

_11

}

_11

}

_11

}

_11

}`

**Private key file (`my-testnet-account.key`):**

`_10

334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111`

**Private configuration file (`private.json`):**

`_10

{

_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "3ae53cb6e3f42a79",

_10

"key": "334232967f52bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_10

}

_10

}

_10

}`

⚠️ **Important:** Always add private files to `.gitignore` to prevent committing sensitive data to source control.

## Validation[​](#validation "Direct link to Validation")

The `config add` command validates all inputs:

* **Account addresses** must be valid Flow addresses (16-character hex)
* **Private keys** must be valid hex-encoded keys
* **Contract sources** must point to existing `.cdc` files
* **Network hosts** must be valid host:port combinations
* **Deployments** must reference existing accounts and contracts

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Use CLI commands** instead of manual editing when possible
2. **Validate your configuration** by running `flow config add` commands
3. **Use descriptive names** for accounts and contracts
4. **Keep sensitive data separate** using multiple config files
5. **Test deployments** on emulator before adding to testnet/mainnet

## Common Use Cases[​](#common-use-cases "Direct link to Common Use Cases")

### Setting Up a New Project[​](#setting-up-a-new-project "Direct link to Setting Up a New Project")

`_14

# Initialize project

_14

flow init

_14

_14

# Add your contracts

_14

flow config add contract --name MyToken --filename ./cadence/contracts/MyToken.cdc

_14

flow config add contract --name MyNFT --filename ./cadence/contracts/MyNFT.cdc

_14

_14

# Create accounts for different networks

_14

flow config add account --name emulator-account --address f8d6e0586b0a20c7 --private-key ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee

_14

flow config add account --name testnet-account --address 3ae53cb6e3f42a79 --private-key 12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111

_14

_14

# Configure deployments

_14

flow config add deployment --network emulator --account emulator-account --contract MyToken --contract MyNFT

_14

flow config add deployment --network testnet --account testnet-account --contract MyToken --contract MyNFT`

### Adding to Existing Project[​](#adding-to-existing-project "Direct link to Adding to Existing Project")

`_10

# Add new contract

_10

flow config add contract --name NewContract --filename ./cadence/contracts/NewContract.cdc

_10

_10

# Add deployment for new contract

_10

flow config add deployment --network testnet --account testnet-account --contract NewContract`

### Managing Multiple Environments[​](#managing-multiple-environments "Direct link to Managing Multiple Environments")

`_10

# Use separate config files for different environments

_10

flow config add account --name admin-account --address f8d6e0586b0a20c7 --private-key ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee -f flow.json

_10

flow config add account --name admin-account --address f1d6e0586b0a20c7 --private-key 3335dfdeb0ff03a7a73ef39788563b62c89adea67bbb21ab95e5f710bd1d40b7 -f private.json`

## Related Commands[​](#related-commands "Direct link to Related Commands")

* [`flow init`](/build/tools/flow-cli/flow.json/initialize-configuration) - Initialize a new project
* [`flow project deploy`](/build/tools/flow-cli/deployment/deploy-project-contracts) - Deploy contracts
* [`flow accounts create`](/build/tools/flow-cli/accounts/create-accounts) - Create new accounts

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/flow.json/manage-configuration.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Configuration](/build/tools/flow-cli/flow.json/configuration)[Next

Security](/build/tools/flow-cli/flow.json/security)

###### Rate this page

😞😐😊

Copy as Markdown

* [Basic Commands](#basic-commands)
* [Adding Configuration](#adding-configuration)
  + [Add an Account](#add-an-account)
  + [Add a Contract](#add-a-contract)
  + [Add a Network](#add-a-network)
  + [Add a Deployment](#add-a-deployment)
* [Removing Configuration](#removing-configuration)
  + [Remove an Account](#remove-an-account)
  + [Remove a Contract](#remove-a-contract)
  + [Remove a Network](#remove-a-network)
  + [Remove a Deployment](#remove-a-deployment)
* [Configuration File Management](#configuration-file-management)
  + [Using Custom Configuration Files](#using-custom-configuration-files)
  + [Configuration File Priority](#configuration-file-priority)
  + [Security Best Practices](#security-best-practices)
* [Validation](#validation)
* [Best Practices](#best-practices)
* [Common Use Cases](#common-use-cases)
  + [Setting Up a New Project](#setting-up-a-new-project)
  + [Adding to Existing Project](#adding-to-existing-project)
  + [Managing Multiple Environments](#managing-multiple-environments)
* [Related Commands](#related-commands)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.