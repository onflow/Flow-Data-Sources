# Source: https://developers.flow.com/build/tools/flow-cli/deployment/project-contracts

Add Project Contracts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          * [Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)* [Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)- [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Deploy Project* Add Project Contracts

On this page

# Add Project Contracts

## Generate a Contract[​](#generate-a-contract "Direct link to Generate a Contract")

Create a new contract file with the Flow CLI:

`_10

flow generate contract Foo`

This command creates `cadence/contracts/Foo.cdc` with a basic contract template and automatically adds it to your `flow.json` configuration.

## Add a contract to configuration[​](#add-a-contract-to-configuration "Direct link to Add a contract to configuration")

If you have a contract file, add it to your project configuration with the CLI:

`_10

flow config add contract`

Follow the interactive prompts:

1. **Contract name**: Enter the contract name (for exxample, `Foo`)
2. **Contract filename**: Enter the path to your contract file (for example, `./cadence/contracts/Foo.cdc`)
3. **Add aliases**: Optionally add network aliases for dependencies

You can also use flags to specify all details at once:

`_10

flow config add contract \

_10

--name Foo \

_10

--filename ./cadence/contracts/Foo.cdc`

**What gets added to `flow.json`:**

`_10

{

_10

"contracts": {

_10

"Foo": "./cadence/contracts/Foo.cdc"

_10

}

_10

}`

## Configure contract deployment targets[​](#configure-contract-deployment-targets "Direct link to Configure contract deployment targets")

After a contract is added to your configuration, configure deployment targets with the CLI:

`_10

flow config add deployment`

Follow the interactive prompts:

1. **Network**: Select the network (for example, `testnet`, `mainnet`, `emulator`)
2. **Account**: Select the account to deploy to (for example, `my-testnet-account`)
3. **Contract**: Select the contract to deploy (for example, `Foo`)
4. **Deploy more contracts**: Choose `yes` to add additional contracts to the same deployment

You can also use flags to specify all details:

`_10

flow config add deployment \

_10

--network testnet \

_10

--account my-testnet-account \

_10

--contract Foo`

**What gets added to `flow.json`:**

`_10

{

_10

"deployments": {

_10

"testnet": {

_10

"my-testnet-account": ["Foo"]

_10

}

_10

}

_10

}`

## Add multiple contracts to a deployment[​](#add-multiple-contracts-to-a-deployment "Direct link to Add multiple contracts to a deployment")

To deploy multiple contracts to the same account, run the deployment configuration command multiple times or use the interactive prompt to add more contracts:

`_10

flow config add deployment --network testnet --account my-testnet-account --contract Bar`

This adds `Bar` to the existing deployment:

`_10

{

_10

"deployments": {

_10

"testnet": {

_10

"my-testnet-account": ["Foo", "Bar"]

_10

}

_10

}

_10

}`

## Remove contracts and deployments[​](#remove-contracts-and-deployments "Direct link to Remove contracts and deployments")

Remove contracts or deployments using the CLI:

`_10

# Remove a contract from configuration

_10

flow config remove contract Foo

_10

_10

# Remove a contract from a specific deployment

_10

flow config remove deployment testnet my-testnet-account Foo`

## Best Practices[​](#best-practices "Direct link to Best Practices")

* **Use CLI commands**: Always use `flow config add` and `flow config remove` rather than manually edit `flow.json`
* **Generate contracts**: Use `flow generate contract` to create new contracts with proper structure
* **Verify configuration**: Use `flow accounts list` and check your `flow.json` to verify your configuration
* **Network-specific deployments**: Configure separate deployments for each network (emulator, testnet, mainnet)

For more information, see [Manage Configuration](/build/tools/flow-cli/flow.json/manage-configuration) and [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/deployment/project-contracts.md)

Last updated on **Dec 10, 2025** by **cshannon1218**

[Previous

Derive Public Key](/build/tools/flow-cli/keys/derive-keys)[Next

Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Generate a Contract](#generate-a-contract)* [Add a contract to configuration](#add-a-contract-to-configuration)* [Configure contract deployment targets](#configure-contract-deployment-targets)* [Add multiple contracts to a deployment](#add-multiple-contracts-to-a-deployment)* [Remove contracts and deployments](#remove-contracts-and-deployments)* [Best Practices](#best-practices)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.