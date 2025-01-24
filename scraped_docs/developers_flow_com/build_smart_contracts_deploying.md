# Source: https://developers.flow.com/build/smart-contracts/deploying




Deploying Contracts | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
  + [Learn Cadence ↗️](/build/learn-cadence)
  + [Smart Contracts on Flow](/build/smart-contracts/overview)
  + [Deploying Contracts](/build/smart-contracts/deploying)
  + [Testing Your Contracts](/build/smart-contracts/testing)
  + [Best Practices](/build/smart-contracts/best-practices/security-best-practices)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Writing and Deploying Smart Contracts
* Deploying Contracts
On this page
# Deploying Contracts

In order to deploy your smart contracts to the mainnet, you need a funded account. If you want to get started on Testnet, look below for information on how to get started.

info

Make sure you handle your mainnet account keys appropriately. Using a Key Management Service is the best practice.

### Creating an Account[​](#creating-an-account "Direct link to Creating an Account")

There are two simple methods of creating an account on testnet. **Interactive** and **Manual**, both use the Flow CLI. On mainnet you will have to fund your newly created account, there is no faucet.
Make sure to install the Flow CLI. [Flow CLI](/tools/flow-cli/accounts/create-accounts) has a interactive mode for generating keys.

tip

Anyone can deploy and update contracts on mainnet. Audits are encouraged but not mandatory to deploying contracts to mainnet. Take every precauction to reduce issues and protect users.

### Create and deploy a mainnet project[​](#create-and-deploy-a-mainnet-project "Direct link to Create and deploy a mainnet project")

The tool of choice is Flow CLI, there are quickstarts and guides that use Flow CLI, [Getting Started](/build/getting-started/flow-cli)

* It is highly encouraged to test your contracts, transactions and scripts on Testnet, have strong smart contract test coverage and follow any additional guidelines set out here: [Smart Contract Testing Guidelines](/build/smart-contracts/testing).
* Follow the Flow CLI instructions to [Create a Project](/tools/flow-cli). You have the Flow CLI installed and ran `flow init` in your project folder and generating a `flow.json` file
* Mainnet account: You completed the mainnet account setup, (see above) and have your key pair and mainnet address ready.
* [Deploy your project](/tools/flow-cli/deployment/deploy-project-contracts), notice that your account now has contracts deployed on mainnet.
* [Deploy a contract](/tools/flow-cli/accounts/account-add-contract) to mainnet. You can deploy contracts individually using the `account-add-contract` command.

info

All your contract deployment addresses are stored in `flow.json`. Mainnet, Testnet and local (emulator) are stored as well.

### Deploy updated contracts on mainnet[​](#deploy-updated-contracts-on-mainnet "Direct link to Deploy updated contracts on mainnet")

Contracts can be updated and retain the contract address. You can use the [Flow CLI contract update command](/tools/flow-cli/accounts/account-update-contract) to re-deploy an updated version of your contract:

warning

If you see `Error Code: 1103`, your new account does not have enough funds to complete the transaction. Make sure you have enough FLOW and your account is set up correctly, check [Flowdiver](https://flowdiver.io/) to verify.

Once all your contracts are deployed, you can visit [flow-view-source](https://flow-view-source.com/) or run the [Flow CLI get account command](/tools/flow-cli/accounts/get-accounts) to confirm the deployment.

### Sporks[​](#sporks "Direct link to Sporks")

Currently, **historical event data is not migrated between sporks,** so you'll need to design your application with this in mind. We recognize the usefulness of historical event data and plan on adding a means of accessing it in the near future. Past spork transactional data is available, [See Previous Spork Access Node Info](/networks/node-ops/node-operation/past-sporks)

More Information on [Sporks](/networks/node-ops/node-operation/spork)

### Testnet[​](#testnet "Direct link to Testnet")

The Flow test network, known as Flow Testnet, exists to help developers test their software and smart contracts against a live network. It's also used as a means of releasing and testing new protocol and smart contract features before they are integrated into Flow's main network (Mainnet).

When the Flow protocol is updated or a new version of Cadence is released, those updates will always be made available on the [Flow Emulator](/tools/emulator) *before* they're integrated into Flow Testnet or Flow Mainnet.

## Getting Started on Testnet[​](#getting-started-on-testnet "Direct link to Getting Started on Testnet")

If you need to create a flow.json file to store information about accounts and contracts use the `flow init` command to create a project

info

To create accounts and generate keys, make sure to install [Flow CLI](/tools/flow-cli/install). Flow CLI provides convenient functions to simplifies interacting with the blockchain.

### Creating an Account[​](#creating-an-account-1 "Direct link to Creating an Account")

There is a simple Flow CLI command to run to create an account. `flow accounts create` command will create a new account and generate a key pair then add the account to your flow.json. The command will try and You can also use the [Testnet Faucet](https://testnet-faucet-v2.onflow.org/) to create and fund an account.

More information about [Flow CLI](/tools/flow-cli/accounts/create-accounts) and creating accounts.

### Creating and deploying a Project[​](#creating-and-deploying-a-project "Direct link to Creating and deploying a Project")

Flow CLI can be used to create a Cadence project and stay organized, [Flow CLI: Create a project](/tools/flow-cli). This will make deployment much easiler and help with the iterative development process.

After you have a project created and want to deploy your Cadence; contracts, transactions and scripts.
`flow accounts add-contract <CONTRACT_PATH> --signer <ACCOUNT_NAME> --network testnet` will deploy your contract to testnet.
More information on how to use Flow CLI to [deploy](/tools/flow-cli/deployment/deploy-project-contracts).

Make sure Flow project was initialized in the previous step and the `flow.json` is present.

### Making Use of Core Contracts[​](#making-use-of-core-contracts "Direct link to Making Use of Core Contracts")

Flow Testnet comes with some useful contracts already deployed, called **core contracts.** More information and import addresses for the [core contracts](/build/core-contracts).

Once your accounts are set up and you're ready to develop, you can look over [some code examples from the Flow Go SDK](https://github.com/onflow/flow-go-sdk/tree/master/examples).

### Breaking Changes[​](#breaking-changes "Direct link to Breaking Changes")

The Flow blockchain is improved continuously and thus version updates to Cadence, Flow node software, and the Flow SDKs will contain important updates as well as breaking changes.

You should anticipate future updates and join the community ([Forum](https://forum.onflow.org/) or [Discord](https://discord.com/invite/J6fFnh2xx6)) to stay tuned on important announcements. Notices and guidelines for changes will be provided as early as possible.

### Testnet Sporking[​](#testnet-sporking "Direct link to Testnet Sporking")

"Sporking" (soft forking) is the process of upgrading the Flow network node software and migrating the chain state from one version to another.

Currently, **historical event data is not migrated between sporks.** You'll need to design your application with this in mind. We recognize the usefulness of historical event data and plan on adding a means of accessing it in the near future. Only one previous spork data is available through old Access Node.

warning

Flow Testnet is explicitly for experimentation and testing and should not be used to exchange "real value" (e.g. developing a fiat money on/off-ramp for your testnet application).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/smart-contracts/deploying.md)Last updated on **Jan 3, 2025** by **Brian Doyle**[PreviousSmart Contracts on Flow](/build/smart-contracts/overview)[NextTesting Your Contracts](/build/smart-contracts/testing)
###### Rate this page

😞😐😊

* [Creating an Account](#creating-an-account)
* [Create and deploy a mainnet project](#create-and-deploy-a-mainnet-project)
* [Deploy updated contracts on mainnet](#deploy-updated-contracts-on-mainnet)
* [Sporks](#sporks)
* [Testnet](#testnet)
* [Getting Started on Testnet](#getting-started-on-testnet)
  + [Creating an Account](#creating-an-account-1)
  + [Creating and deploying a Project](#creating-and-deploying-a-project)
  + [Making Use of Core Contracts](#making-use-of-core-contracts)
  + [Breaking Changes](#breaking-changes)
  + [Testnet Sporking](#testnet-sporking)
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
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)
Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)
Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)
More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)
Copyright © 2025 Flow, Inc. Built with Docusaurus.

