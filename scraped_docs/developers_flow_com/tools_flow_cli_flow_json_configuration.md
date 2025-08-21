# Source: https://developers.flow.com/tools/flow-cli/flow.json/configuration

Configuration | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/react-sdk)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/react-sdk](/tools/react-sdk)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Commands Overview](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)

    - [Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)
    - [Configuration](/tools/flow-cli/flow.json/configuration)
    - [Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)
    - [Security](/tools/flow-cli/flow.json/security)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Flow CLI](/tools/flow-cli)
* Flow.json
* Configuration

On this page

# Configuration

The `flow.json` file is the central configuration file for your Flow project. It tells the Flow CLI how to interact with networks, manage accounts, deploy contracts, and organize your project structure.

## Quick Start[​](#quick-start "Direct link to Quick Start")

When you run `flow init`, a basic `flow.json` file is created for you:

`_15

{

_15

"networks": {

_15

"emulator": "127.0.0.1:3569",

_15

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_15

"testnet": "access.devnet.nodes.onflow.org:9000"

_15

},

_15

"accounts": {

_15

"emulator-account": {

_15

"address": "f8d6e0586b0a20c7",

_15

"key": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee"

_15

}

_15

},

_15

"deployments": {},

_15

"contracts": {}

_15

}`

This gives you everything you need to get started with local development. As your project grows, you'll add more configuration to support different networks and deployment targets.

## Configuration Sections[​](#configuration-sections "Direct link to Configuration Sections")

### Networks[​](#networks "Direct link to Networks")

The `networks` section defines which Flow networks your project can connect to.

`_10

"networks": {

_10

"emulator": "127.0.0.1:3569",

_10

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_10

"testnet": "access.devnet.nodes.onflow.org:9000"

_10

}`

**Common Networks:**

* `emulator`: Your local development environment
* `testnet`: Flow's test network for development and testing
* `mainnet`: Flow's production network

**Secure Connections:**
For enhanced security, you can specify network keys:

`_10

"networks": {

_10

"testnetSecure": {

_10

"host": "access-001.devnet30.nodes.onflow.org:9001",

_10

"key": "ba69f7d2e82b9edf25b103c195cd371cf0cc047ef8884a9bbe331e62982d46daeebf836f7445a2ac16741013b192959d8ad26998aff12f2adc67a99e1eb2988d"

_10

}

_10

}`

### Accounts[​](#accounts "Direct link to Accounts")

The `accounts` section defines the accounts you can use for transactions and deployments.

#### Simple Account Format[​](#simple-account-format "Direct link to Simple Account Format")

`_10

"accounts": {

_10

"my-account": {

_10

"address": "f8d6e0586b0a20c7",

_10

"key": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee"

_10

}

_10

}`

#### Advanced Account Format[​](#advanced-account-format "Direct link to Advanced Account Format")

For more control over key management:

`_12

"accounts": {

_12

"my-account": {

_12

"address": "f8d6e0586b0a20c7",

_12

"key": {

_12

"type": "hex",

_12

"index": 0,

_12

"signatureAlgorithm": "ECDSA_P256",

_12

"hashAlgorithm": "SHA3_256",

_12

"privateKey": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee"

_12

}

_12

}

_12

}`

**Key Types:**

* `hex`: Standard hex-encoded private key
* `file`: Read key from a separate file
* `bip44`: Derive from mnemonic phrase
* `google-kms`: Use Google Cloud KMS

**File-Based Keys:**
For better security, you can store private keys in separate files:

`_10

"accounts": {

_10

"admin-account": {

_10

"address": "f8d6e0586b0a20c7",

_10

"key": {

_10

"type": "file",

_10

"location": "./keys/admin.key"

_10

}

_10

}

_10

}`

The key file should contain only the hex-encoded private key (e.g., `ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee`).

**Special Address Values:**

* `"service"`: Use the default service account (emulator only)

### Contracts[​](#contracts "Direct link to Contracts")

The `contracts` section maps contract names to their source files.

#### Simple Contract Format[​](#simple-contract-format "Direct link to Simple Contract Format")

`_10

"contracts": {

_10

"MyContract": "./cadence/contracts/MyContract.cdc",

_10

"AnotherContract": "./cadence/contracts/AnotherContract.cdc"

_10

}`

#### Advanced Contract Format with Aliases[​](#advanced-contract-format-with-aliases "Direct link to Advanced Contract Format with Aliases")

Use aliases when contracts are already deployed on specific networks:

`_10

"contracts": {

_10

"FungibleToken": {

_10

"source": "./cadence/contracts/FungibleToken.cdc",

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

**When to Use Aliases:**

* For core contracts already deployed on mainnet/testnet
* To avoid redeploying dependencies
* To use the official versions of common contracts

### Deployments[​](#deployments "Direct link to Deployments")

The `deployments` section defines which contracts get deployed to which accounts on which networks.

`_10

"deployments": {

_10

"emulator": {

_10

"emulator-account": ["MyContract", "AnotherContract"]

_10

},

_10

"testnet": {

_10

"my-testnet-account": ["MyContract"]

_10

}

_10

}`

**Format:** `"NETWORK": { "ACCOUNT": ["CONTRACT1", "CONTRACT2"] }`

**Important Notes:**

* Don't deploy contracts that have aliases defined for that network
* Contracts are deployed in dependency order automatically
* You can deploy the same contract to multiple accounts (but not in the same deploy command)

### Emulators[​](#emulators "Direct link to Emulators")

Customize emulator settings (optional):

`_10

"emulators": {

_10

"custom-emulator": {

_10

"port": 3600,

_10

"serviceAccount": "emulator-account"

_10

}

_10

}`

## Complete Example[​](#complete-example "Direct link to Complete Example")

Here's a complete `flow.json` for a project with multiple contracts and networks:

`_39

{

_39

"networks": {

_39

"emulator": "127.0.0.1:3569",

_39

"testnet": "access.devnet.nodes.onflow.org:9000",

_39

"mainnet": "access.mainnet.nodes.onflow.org:9000"

_39

},

_39

_39

"accounts": {

_39

"emulator-account": {

_39

"address": "f8d6e0586b0a20c7",

_39

"key": "ae1b44c0f5e8f6992ef2348898a35e50a8b0b9684000da8b1dade1b3bcd6ebee"

_39

},

_39

"testnet-account": {

_39

"address": "3ae53cb6e3f42a79",

_39

"key": "12332967fd2bd75234ae9037dd4694c1f00baad63a10c35172bf65fbb8ad1111"

_39

}

_39

},

_39

_39

"contracts": {

_39

"FungibleToken": {

_39

"source": "./cadence/contracts/FungibleToken.cdc",

_39

"aliases": {

_39

"testnet": "9a0766d93b6608b7",

_39

"mainnet": "f233dcee88fe0abe"

_39

}

_39

},

_39

"MyToken": "./cadence/contracts/MyToken.cdc",

_39

"MyNFT": "./cadence/contracts/MyNFT.cdc"

_39

},

_39

_39

"deployments": {

_39

"emulator": {

_39

"emulator-account": ["FungibleToken", "MyToken", "MyNFT"]

_39

},

_39

"testnet": {

_39

"testnet-account": ["MyToken", "MyNFT"]

_39

}

_39

}

_39

}`

## Managing Configuration[​](#managing-configuration "Direct link to Managing Configuration")

Instead of editing `flow.json` manually, use the CLI commands:

`_11

# Add an account

_11

flow config add account

_11

_11

# Add a contract

_11

flow config add contract

_11

_11

# Add a deployment

_11

flow config add deployment

_11

_11

# Remove configuration

_11

flow config remove account my-account`

## Best Practices[​](#best-practices "Direct link to Best Practices")

1. **Use CLI commands** when possible instead of manual editing
2. **Keep private keys secure** - consider using file-based keys for production
3. **Use aliases** for core contracts to avoid redeployment
4. **Test on emulator first** before deploying to testnet
5. **Use different accounts** for different networks
6. **Backup your configuration** before making major changes

## Related Commands[​](#related-commands "Direct link to Related Commands")

* [`flow init`](/tools/flow-cli/flow.json/initialize-configuration) - Initialize a new project
* [`flow config add`](/tools/flow-cli/flow.json/manage-configuration) - Add configuration items
* [`flow project deploy`](/tools/flow-cli/deployment/deploy-project-contracts) - Deploy contracts
* [`flow accounts create`](/tools/flow-cli/accounts/create-accounts) - Create new accounts

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/flow.json/configuration.md)

Last updated on **Aug 19, 2025** by **Chase Fleming**

[Previous

Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)[Next

Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)

###### Rate this page

😞😐😊

Copy as Markdown

* [Quick Start](#quick-start)
* [Configuration Sections](#configuration-sections)
  + [Networks](#networks)
  + [Accounts](#accounts)
  + [Contracts](#contracts)
  + [Deployments](#deployments)
  + [Emulators](#emulators)
* [Complete Example](#complete-example)
* [Managing Configuration](#managing-configuration)
* [Best Practices](#best-practices)
* [Related Commands](#related-commands)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.