# Source: https://developers.flow.com/build/cadence/smart-contracts/deploying

Deploying Contracts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            - [Learn Cadence ↗️](/build/cadence/learn-cadence)- [Smart Contracts on Flow](/build/cadence/smart-contracts/overview)- [Deploying Contracts](/build/cadence/smart-contracts/deploying)- [Testing Smart Contracts](/build/cadence/smart-contracts/testing)- [Best Practices](/build/cadence/smart-contracts/best-practices/security-best-practices)+ [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Writing and Deploying Smart Contracts* Deploying Contracts

On this page

# Deploying Contracts

Deploying smart contracts to Flow's networks is the final step in bringing your blockchain application to life. This guide covers everything you need to know to deploy your Cadence contracts to both Flow Testnet and Mainnet, from account creation to contract updates.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

After completing this guide, you'll be able to:

* **Create and fund accounts** on Flow Testnet and Mainnet
* **Deploy contracts** using Flow CLI with proper configuration
* **Update existing contracts** while preserving their addresses
* **Understand the differences** between testnet and mainnet deployment
* **Follow security best practices** for production deployments

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before deploying contracts, make sure you have:

* **Flow CLI installed** and configured
* **A Flow project** with contracts ready for deployment
* **Basic understanding** of Cadence smart contracts
* **Completed testing** of your contracts locally

## Deployment Workflow[​](#deployment-workflow "Direct link to Deployment Workflow")

The recommended deployment workflow follows this progression:

1. **Emulator Deployment** - Deploy and test your contracts locally (free, instant)
2. **Testnet Deployment** - Deploy and test your contracts on Flow Testnet (free)
3. **Mainnet Deployment** - Deploy to Flow Mainnet once testing is complete (costs FLOW tokens)
4. **Contract Updates** - Update contracts as needed using the update command

This approach ensures your contracts work correctly before committing real resources to mainnet deployment.

## Deploy to Emulator[​](#deploy-to-emulator "Direct link to Deploy to Emulator")

The Flow Emulator is your local development environment where you can deploy and test contracts instantly without any network costs or delays. This is the first step in your deployment journey.

### Start the Emulator[​](#start-the-emulator "Direct link to Start the Emulator")

First, start the [Flow Emulator](/build/tools/emulator). In a second terminal:

`_10

flow emulator start`

### Create an Emulator Account[​](#create-an-emulator-account "Direct link to Create an Emulator Account")

Create a local account for testing:

`_10

flow accounts create --network emulator`

When prompted:

1. **Account name**: Enter `emulator-account`
2. Select `emulator` as the network when prompted

This creates a new account on the emulator and adds it to your `flow.json` configuration.

### Configure Emulator Deployment[​](#configure-emulator-deployment "Direct link to Configure Emulator Deployment")

Update your `flow.json` to include emulator deployment configuration:

`_10

flow config add deployment`

Follow the prompts:

1. **Network**: `emulator`
2. **Account**: `emulator-account`
3. **Contract**: `YourContract`
4. **Deploy more contracts**: `no` (or `yes` if you have multiple contracts)

Your `flow.json` will now include an emulator deployment section:

`_10

{

_10

"deployments": {

_10

"emulator": {

_10

"emulator-account": ["YourContract"]

_10

}

_10

}

_10

}`

### Deploy Contract to Emulator[​](#deploy-contract-to-emulator "Direct link to Deploy Contract to Emulator")

Deploy your contract to the local emulator:

`_10

flow project deploy --network emulator`

warning

You cannot deploy the same contract to multiple accounts on the same network with one deployment command. If you attempt to do so, you will see:

❌ Command Error: the same contract cannot be deployed to multiple accounts on the same network

Edit `flow.json` to remove the duplicate.

You will see output similar to:

`_10

Deploying 1 contracts for accounts: emulator-account

_10

_10

YourContract -> 0xf8d6e0586b0a20c7 (contract deployed successfully)

_10

_10

🎉 All contracts deployed successfully`

### Test Your Emulator Deployment[​](#test-your-emulator-deployment "Direct link to Test Your Emulator Deployment")

Verify your contract works by running scripts and transactions:

`_10

# Run a script to read contract state

_10

flow scripts execute cadence/scripts/YourScript.cdc --network emulator

_10

_10

# Send a transaction to interact with your contract

_10

flow transactions send cadence/transactions/YourTransaction.cdc --network emulator --signer emulator-account`

info

The emulator provides instant feedback and is perfect for rapid development and testing. All transactions are free and execute immediately.

## Deploy to Testnet[​](#deploy-to-testnet "Direct link to Deploy to Testnet")

For a more complete quickstart, visit the [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction) guide.

* You should test your contracts, transactions and scripts on Testnet, have strong smart contract test coverage and follow the additional guidelines set out here: [Smart Contract Testing Guidelines](/build/cadence/smart-contracts/testing).
* Use `flow init` to [Create a Project](/build/tools/flow-cli) if you need one to practice deployment with.

### Create a Testnet Account[​](#create-a-testnet-account "Direct link to Create a Testnet Account")

First, you'll need a testnet account to deploy your contracts. Create one with:

`_10

flow accounts create --network testnet`

info

For security reasons, Flow Cadence does not allow accounts to have the same address on testnet, mainnet, and/or the emulator.

When prompted:

1. **Account name**: Enter `testnet-account`
2. Select `testnet` as the network when prompted

This creates a new account on testnet and adds it to your `flow.json` configuration. It also saves the private key for the new account in `<account-name>.pkey` and uses this file to import the key because `flow.json` will be visible in the repo.

danger

As with any other blockchain network, **anyone** with access to the private key for an account can access that account at any time without you knowing.

### Fund Your Testnet Account[​](#fund-your-testnet-account "Direct link to Fund Your Testnet Account")

To deploy contracts and send transactions on testnet, you need FLOW tokens. Flow provides a faucet service to get free testnet tokens.

`_10

flow accounts fund testnet-account`

This will open the faucet in your browser. You can also navigate there manually.

1. Visit the [Testnet Faucet](https://faucet.flow.com/)
2. Enter your testnet account address
3. Complete any required verification (captcha, etc.)
4. Request tokens (you'll receive 100000 testnet FLOW tokens)

Check your account balance:

`_10

flow accounts list`

You will see your account details with a balance of FLOW tokens.

### Configure Testnet Deployment[​](#configure-testnet-deployment "Direct link to Configure Testnet Deployment")

Update your `flow.json` to include testnet deployment configuration:

`_10

flow config add deployment`

Follow the prompts:

1. **Network**: `testnet`
2. **Account**: `testnet-account`
3. **Contract**: `YourContract`
4. **Deploy more contracts**: `no` (or `yes` if you have multiple contracts)

Your `flow.json` will now include a testnet deployment section:

`_10

{

_10

"deployments": {

_10

"testnet": {

_10

"testnet-account": ["YourContract"]

_10

}

_10

}

_10

}`

### Deploy Contract to Testnet[​](#deploy-contract-to-testnet "Direct link to Deploy Contract to Testnet")

Deploy your contract to the public testnet:

`_10

flow project deploy --network testnet`

You will see output similar to:

`_10

Deploying 1 contracts for accounts: testnet-account

_10

_10

YourContract -> 0x9942a81bc6c3c5b7 (contract deployed successfully)

_10

_10

🎉 All contracts deployed successfully`

## Deploy to Mainnet[​](#deploy-to-mainnet "Direct link to Deploy to Mainnet")

Once you've successfully tested your contracts on testnet, you can deploy to mainnet. You'll need a mainnet account with real FLOW tokens.

### Create a Mainnet Account[​](#create-a-mainnet-account "Direct link to Create a Mainnet Account")

For mainnet, you'll need to acquire FLOW tokens through exchanges or other means, as there's no faucet.

`_10

flow accounts create --network mainnet`

When prompted:

1. **Account name**: Enter `mainnet-account`
2. **Select "Mainnet" Network**

### Acquire FLOW Tokens[​](#acquire-flow-tokens "Direct link to Acquire FLOW Tokens")

You can purchase FLOW tokens from major exchanges. Make sure your mainnet account has sufficient FLOW tokens to cover deployment costs. Flow is a very efficient network, so even 1.0 FLOW is sufficient to deploy large numbers of contracts.

### Configure Mainnet Deployment[​](#configure-mainnet-deployment "Direct link to Configure Mainnet Deployment")

Add mainnet deployment configuration to your `flow.json`:

`_10

flow config add deployment --network mainnet`

Follow the prompts:

1. **Network**: `mainnet`
2. **Account**: `mainnet-account`
3. **Contract**: `YourContract`
4. **Deploy more contracts**: `no` (or `yes` if you have multiple contracts)

Your `flow.json` should now include mainnet configuration:

`_10

{

_10

"deployments": {

_10

"mainnet": {

_10

"mainnet-account": ["YourContract"]

_10

}

_10

}

_10

}`

### Deploy to Mainnet[​](#deploy-to-mainnet-1 "Direct link to Deploy to Mainnet")

Deploy your contracts to mainnet:

`_10

flow project deploy --network mainnet`

warning

This deployment costs (a relatively small amount of) real FLOW tokens and cannot be undone. You can however redeploy your contracts to update them, or delete them.

You should see output similar to:

`_10

Deploying 1 contracts for accounts: mainnet-account

_10

_10

YourContract -> 0xABC123DEF456789 (contract deployed successfully)

_10

_10

🎉 All contracts deployed successfully`

info

All your contract deployment addresses are stored in `flow.json`. Mainnet, Testnet and local (emulator) are stored as well.

## Deploy updated contracts on mainnet[​](#deploy-updated-contracts-on-mainnet "Direct link to Deploy updated contracts on mainnet")

Contracts can be updated and retain the contract address. You can use the [Flow CLI contract update command](/build/tools/flow-cli/accounts/account-update-contract) to redeploy an updated version of your contract:

`_10

flow accounts update-contract ./YourContract.cdc --signer mainnet-account --network mainnet`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/smart-contracts/deploying.md)

Last updated on **Oct 9, 2025** by **Brian Doyle**

[Previous

Smart Contracts on Flow](/build/cadence/smart-contracts/overview)[Next

Testing Smart Contracts](/build/cadence/smart-contracts/testing)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [Prerequisites](#prerequisites)* [Deployment Workflow](#deployment-workflow)* [Deploy to Emulator](#deploy-to-emulator)
        + [Start the Emulator](#start-the-emulator)+ [Create an Emulator Account](#create-an-emulator-account)+ [Configure Emulator Deployment](#configure-emulator-deployment)+ [Deploy Contract to Emulator](#deploy-contract-to-emulator)+ [Test Your Emulator Deployment](#test-your-emulator-deployment)* [Deploy to Testnet](#deploy-to-testnet)
          + [Create a Testnet Account](#create-a-testnet-account)+ [Fund Your Testnet Account](#fund-your-testnet-account)+ [Configure Testnet Deployment](#configure-testnet-deployment)+ [Deploy Contract to Testnet](#deploy-contract-to-testnet)* [Deploy to Mainnet](#deploy-to-mainnet)
            + [Create a Mainnet Account](#create-a-mainnet-account)+ [Acquire FLOW Tokens](#acquire-flow-tokens)+ [Configure Mainnet Deployment](#configure-mainnet-deployment)+ [Deploy to Mainnet](#deploy-to-mainnet-1)* [Deploy updated contracts on mainnet](#deploy-updated-contracts-on-mainnet)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.