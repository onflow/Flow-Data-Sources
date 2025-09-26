# Source: https://developers.flow.com/build/tools/flow-cli/commands

Commands Overview | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/quickstart)

  + [Quickstart ↙](/build/cadence/quickstart)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Basics](/build/cadence/basics/network-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
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
* Commands Overview

On this page

# Commands Overview

Flow CLI provides a set of powerful commands that simplify your development workflow. These "super commands" handle complex tasks automatically, letting you focus on writing your smart contracts while the CLI manages the rest.

## Project Lifecycle[​](#project-lifecycle "Direct link to Project Lifecycle")

### 1. Initialize a Project[​](#1-initialize-a-project "Direct link to 1. Initialize a Project")

Start a new Flow project with `flow init`:

`_10

flow init my-project`

This creates:

* `flow.json` - Project configuration
* `cadence/` directory structure
* Example contracts, scripts, and tests
* Emulator account setup

**Options:**

`_10

# Configuration only (no project structure)

_10

flow init --config-only

_10

_10

# Global configuration

_10

flow init --global

_10

_10

# Custom service account

_10

flow init --service-private-key <key>`

📖 **[Learn more about project initialization](/build/tools/flow-cli/flow.json/initialize-configuration)**

### 2. Generate Project Files[​](#2-generate-project-files "Direct link to 2. Generate Project Files")

Create new files with the `flow generate` command:

`_11

# Generate a new contract

_11

flow generate contract MyToken

_11

_11

# Generate a new script

_11

flow generate script GetBalance

_11

_11

# Generate a new transaction

_11

flow generate transaction TransferTokens

_11

_11

# Generate a new test

_11

flow generate test MyToken`

**Generated Structure:**

`_10

cadence/

_10

├── contracts/

_10

│ └── MyToken.cdc

_10

├── scripts/

_10

│ └── GetBalance.cdc

_10

├── transactions/

_10

│ └── TransferTokens.cdc

_10

└── tests/

_10

└── MyToken_test.cdc`

📖 **[Learn more about generating Cadence boilerplate](/build/tools/flow-cli/generate)**

### 3. Run Tests[​](#3-run-tests "Direct link to 3. Run Tests")

Test your contracts with `flow test`:

`_11

# Run all tests

_11

flow test

_11

_11

# Run specific test file

_11

flow test cadence/tests/MyToken_test.cdc

_11

_11

# Run with coverage

_11

flow test --coverage

_11

_11

# Run with verbose output

_11

flow test --verbose`

📖 **[Learn more about testing](/build/tools/flow-cli/tests)**

### 4. Deploy Contracts[​](#4-deploy-contracts "Direct link to 4. Deploy Contracts")

Deploy your contracts with `flow project deploy`:

`_11

# Deploy to emulator

_11

flow project deploy

_11

_11

# Deploy to testnet

_11

flow project deploy --network=testnet

_11

_11

# Deploy to mainnet

_11

flow project deploy --network=mainnet

_11

_11

# Update existing contracts

_11

flow project deploy --update`

📖 **[Learn more about project deployment](/build/tools/flow-cli/deployment/deploy-project-contracts)**

## Configuration Management[​](#configuration-management "Direct link to Configuration Management")

### Add Configuration Items[​](#add-configuration-items "Direct link to Add Configuration Items")

Use `flow config add` to manage your project configuration:

`_10

# Add an account

_10

flow config add account --name my-account --address 0x123 --private-key abc123

_10

_10

# Add a contract

_10

flow config add contract --name MyToken --filename ./cadence/contracts/MyToken.cdc

_10

_10

# Add a deployment

_10

flow config add deployment --network testnet --account my-account --contract MyToken`

### Remove Configuration Items[​](#remove-configuration-items "Direct link to Remove Configuration Items")

`_10

# Remove an account

_10

flow config remove account my-account

_10

_10

# Remove a contract

_10

flow config remove contract MyToken

_10

_10

# Remove a deployment

_10

flow config remove deployment testnet my-account MyToken`

📖 **[Learn more about configuration management](/build/tools/flow-cli/flow.json/manage-configuration)**

## Account Management[​](#account-management "Direct link to Account Management")

### List Accounts[​](#list-accounts "Direct link to List Accounts")

`_10

# List all configured accounts with status

_10

flow accounts list`

### Create Accounts[​](#create-accounts "Direct link to Create Accounts")

`_10

# Interactive account creation

_10

flow accounts create

_10

_10

# Create with specific network

_10

flow accounts create --network testnet

_10

_10

# Create with custom key

_10

flow accounts create --key <private-key>`

### Fund Accounts[​](#fund-accounts "Direct link to Fund Accounts")

`_10

# Interactive funding prompt

_10

flow accounts fund

_10

_10

# Fund by account name from flow.json

_10

flow accounts fund testnet-account

_10

_10

# Fund by address

_10

flow accounts fund 0x8e94eaa81771313a`

### Manage Account Keys[​](#manage-account-keys "Direct link to Manage Account Keys")

`_10

# Generate new key pair

_10

flow keys generate

_10

_10

# Decode a key

_10

flow keys decode <key>

_10

_10

# Derive public key from private key

_10

flow keys derive <private-key>`

📖 **[Learn more about account management](/build/tools/flow-cli/accounts/create-accounts)**

## Contract Interactions[​](#contract-interactions "Direct link to Contract Interactions")

### Execute Scripts[​](#execute-scripts "Direct link to Execute Scripts")

`_10

# Run a script

_10

flow scripts execute cadence/scripts/GetBalance.cdc

_10

_10

# Run with arguments

_10

flow scripts execute cadence/scripts/GetBalance.cdc --arg 0x123

_10

_10

# Run on specific network

_10

flow scripts execute cadence/scripts/GetBalance.cdc --network testnet`

### Send Transactions[​](#send-transactions "Direct link to Send Transactions")

`_10

# Send a transaction

_10

flow transactions send cadence/transactions/TransferTokens.cdc

_10

_10

# Send with arguments

_10

flow transactions send cadence/transactions/TransferTokens.cdc --arg 0x123 --arg 100

_10

_10

# Send with specific signer

_10

flow transactions send cadence/transactions/TransferTokens.cdc --signer my-account`

### Get System Transactions[​](#get-system-transactions "Direct link to Get System Transactions")

`_10

# Get system transaction from latest block

_10

flow transactions get-system latest

_10

_10

# Get specific system transaction by ID

_10

flow transactions get-system latest 07a8...b433

_10

_10

# Get system transaction from specific block height

_10

flow transactions get-system 12345`

📖 **[Learn more about scripts](/build/tools/flow-cli/scripts/execute-scripts)** | **[Learn more about transactions](/build/tools/flow-cli/transactions/send-transactions)**

## Dependency Management[​](#dependency-management "Direct link to Dependency Management")

### Install Dependencies[​](#install-dependencies "Direct link to Install Dependencies")

`_10

# Install a contract dependency

_10

flow dependencies install testnet://8a4dce54554b225d.NumberFormatter

_10

_10

# Install from mainnet

_10

flow dependencies install mainnet://f233dcee88fe0abe.FungibleToken

_10

_10

# Install with specific account

_10

flow dependencies install testnet://8a4dce54554b225d.NumberFormatter --account my-account`

### Manage Dependencies[​](#manage-dependencies "Direct link to Manage Dependencies")

`_10

# List installed dependencies

_10

flow dependencies list

_10

_10

# Discover available contracts

_10

flow dependencies discover

_10

_10

# Install a contract dependency

_10

flow dependencies install testnet://8a4dce54554b225d.NumberFormatter`

📖 **[Learn more about dependency management](/build/tools/flow-cli/dependency-manager)**

## Development Workflow[​](#development-workflow "Direct link to Development Workflow")

### Local Development[​](#local-development "Direct link to Local Development")

1. **Start the emulator:**

`_10

flow emulator start`

2. **Deploy contracts:**

`_10

flow project deploy`

3. **Run tests:**

`_10

flow test`

4. **Execute scripts:**

`_10

flow scripts execute cadence/scripts/GetBalance.cdc`

5. **Send transactions:**

`_10

flow transactions send cadence/transactions/TransferTokens.cdc`

### Testnet Deployment[​](#testnet-deployment "Direct link to Testnet Deployment")

1. **Configure testnet account:**

`_10

flow config add account --name testnet-account --address 0x123 --private-key abc123`

2. **Deploy to testnet:**

`_10

flow project deploy --network=testnet`

3. **Test on testnet:**

`_10

flow scripts execute cadence/scripts/GetBalance.cdc --network=testnet`

## Import Schema[​](#import-schema "Direct link to Import Schema")

Use simplified imports in your Cadence code:

`_10

// Instead of complex import paths

_10

import FungibleToken from 0x9a0766d93b6608b7

_10

_10

// Use simple contract names

_10

import "FungibleToken"`

The CLI automatically resolves imports based on your `flow.json` configuration.

## Best Practices[​](#best-practices "Direct link to Best Practices")

### 1. Use Configuration Commands[​](#1-use-configuration-commands "Direct link to 1. Use Configuration Commands")

Instead of manually editing `flow.json`, use CLI commands:

`_10

# ✅ Good

_10

flow config add account --name my-account --address 0x123

_10

_10

# ❌ Avoid

_10

# Manually editing flow.json`

### 2. Test Locally First[​](#2-test-locally-first "Direct link to 2. Test Locally First")

Always test on emulator before deploying:

`_11

# 1. Start emulator

_11

flow emulator start

_11

_11

# 2. Deploy locally

_11

flow project deploy

_11

_11

# 3. Run tests

_11

flow test

_11

_11

# 4. Deploy to testnet

_11

flow project deploy --network=testnet`

### 3. Use Descriptive Names[​](#3-use-descriptive-names "Direct link to 3. Use Descriptive Names")

Choose clear names for accounts and contracts:

`_10

# ✅ Good

_10

flow config add account --name testnet-deployer

_10

flow generate contract MyNFT

_10

_10

# ❌ Avoid

_10

flow config add account --name acc1

_10

flow generate contract c1`

### 4. Secure Your Keys[​](#4-secure-your-keys "Direct link to 4. Secure Your Keys")

Use secure key management:

`_10

# Use file-based keys

_10

flow config add account --name my-account --key-file ./keys/my-account.key

_10

_10

# Use environment variables

_10

FLOW_PRIVATE_KEY=abc123 flow project deploy`

📖 **[Learn more about security best practices](/build/tools/flow-cli/flow.json/security)**

## Related Documentation[​](#related-documentation "Direct link to Related Documentation")

* **[Configuration Management](/build/tools/flow-cli/flow.json/manage-configuration)** - Learn how to manage your `flow.json` file
* **[Project Deployment](/build/tools/flow-cli/deployment/deploy-project-contracts)** - Deploy contracts to different networks
* **[Account Management](/build/tools/flow-cli/accounts/create-accounts)** - Create and manage Flow accounts
* **[Testing](/build/tools/flow-cli/tests)** - Write and run tests for your contracts
* **[Security](/build/tools/flow-cli/flow.json/security)** - Secure your private keys and configuration

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/commands.md)

Last updated on **Sep 24, 2025** by **Chase Fleming**

[Previous

Install Instructions](/build/tools/flow-cli/install)[Next

Get an Account](/build/tools/flow-cli/accounts/get-accounts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Project Lifecycle](#project-lifecycle)
  + [1. Initialize a Project](#1-initialize-a-project)
  + [2. Generate Project Files](#2-generate-project-files)
  + [3. Run Tests](#3-run-tests)
  + [4. Deploy Contracts](#4-deploy-contracts)
* [Configuration Management](#configuration-management)
  + [Add Configuration Items](#add-configuration-items)
  + [Remove Configuration Items](#remove-configuration-items)
* [Account Management](#account-management)
  + [List Accounts](#list-accounts)
  + [Create Accounts](#create-accounts)
  + [Fund Accounts](#fund-accounts)
  + [Manage Account Keys](#manage-account-keys)
* [Contract Interactions](#contract-interactions)
  + [Execute Scripts](#execute-scripts)
  + [Send Transactions](#send-transactions)
  + [Get System Transactions](#get-system-transactions)
* [Dependency Management](#dependency-management)
  + [Install Dependencies](#install-dependencies)
  + [Manage Dependencies](#manage-dependencies)
* [Development Workflow](#development-workflow)
  + [Local Development](#local-development)
  + [Testnet Deployment](#testnet-deployment)
* [Import Schema](#import-schema)
* [Best Practices](#best-practices)
  + [1. Use Configuration Commands](#1-use-configuration-commands)
  + [2. Test Locally First](#2-test-locally-first)
  + [3. Use Descriptive Names](#3-use-descriptive-names)
  + [4. Secure Your Keys](#4-secure-your-keys)
* [Related Documentation](#related-documentation)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.