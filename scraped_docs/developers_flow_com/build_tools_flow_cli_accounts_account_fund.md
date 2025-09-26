# Source: https://developers.flow.com/build/tools/flow-cli/accounts/account-fund

Funding a Testnet Account | Flow Developer Portal



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

      * [Get an Account](/build/tools/flow-cli/accounts/get-accounts)
      * [Create an Account](/build/tools/flow-cli/accounts/create-accounts)
      * [Deploy a Contract](/build/tools/flow-cli/accounts/account-add-contract)
      * [Update a Contract](/build/tools/flow-cli/accounts/account-update-contract)
      * [Remove a Contract](/build/tools/flow-cli/accounts/account-remove-contract)
      * [Account Staking Info](/build/tools/flow-cli/accounts/account-staking-info)
      * [Funding a Testnet Account](/build/tools/flow-cli/accounts/account-fund)
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
* Accounts
* Funding a Testnet Account

On this page

# Funding a Testnet Account

info

The [Flow Testnet Faucet](https://testnet-faucet.onflow.org/) allows users to create accounts and receive 1,000 Testnet FLOW tokens for testing and development purposes. You can also fund an existing Testnet accounts without needing to create one through the site, or through the CLI.

Fund a valid Testnet Flow Account using the Flow CLI.

`_10

flow accounts fund [address|name]`

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Fund by Address[​](#fund-by-address "Direct link to Fund by Address")

`_10

> flow accounts fund 8e94eaa81771313a

_10

_10

Opening the faucet to fund 0x8e94eaa81771313a on your native browser.

_10

_10

If there is an issue, please use this link instead: https://testnet-faucet.onflow.org/fund-account?address=8e94eaa81771313a`

### Fund by Account Name[​](#fund-by-account-name "Direct link to Fund by Account Name")

`_10

> flow accounts fund testnet-account

_10

_10

Opening the faucet to fund 0x8e94eaa81771313a on your native browser.

_10

_10

If there is an issue, please use this link instead: https://testnet-faucet.onflow.org/fund-account?address=8e94eaa81771313a`

### Interactive Prompt[​](#interactive-prompt "Direct link to Interactive Prompt")

`_10

> flow accounts fund

_10

_10

? Select account to fund: (Use arrow keys)

_10

❯ testnet-account (0x8e94eaa81771313a)

_10

emulator-account (0x0ae53cb6e3f42a79)`

## Arguments[​](#arguments "Direct link to Arguments")

### Address or Account Name (Optional)[​](#address-or-account-name-optional "Direct link to Address or Account Name (Optional)")

* Name: `address|name`
* Valid Input: Flow Testnet account address or account name from `flow.json`

You can provide:

* A Flow [account address](/build/cadence/basics/accounts) (prefixed with `0x` or not)
* An account name configured in your `flow.json`
* No argument to get an interactive prompt for account selection

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/accounts/account-fund.md)

Last updated on **Sep 22, 2025** by **Chase Fleming**

[Previous

Account Staking Info](/build/tools/flow-cli/accounts/account-staking-info)[Next

Generate Keys](/build/tools/flow-cli/keys/generate-keys)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
  + [Fund by Address](#fund-by-address)
  + [Fund by Account Name](#fund-by-account-name)
  + [Interactive Prompt](#interactive-prompt)
* [Arguments](#arguments)
  + [Address or Account Name (Optional)](#address-or-account-name-optional)

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