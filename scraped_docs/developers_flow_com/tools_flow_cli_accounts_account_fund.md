# Source: https://developers.flow.com/tools/flow-cli/accounts/account-fund

Funding a Testnet Account | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)

    - [Get an Account](/tools/flow-cli/accounts/get-accounts)
    - [Create an Account](/tools/flow-cli/accounts/create-accounts)
    - [Deploy a Contract](/tools/flow-cli/accounts/account-add-contract)
    - [Update a Contract](/tools/flow-cli/accounts/account-update-contract)
    - [Remove a Contract](/tools/flow-cli/accounts/account-remove-contract)
    - [Account Staking Info](/tools/flow-cli/accounts/account-staking-info)
    - [Funding a Testnet Account](/tools/flow-cli/accounts/account-fund)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Accounts
* Funding a Testnet Account

On this page

# Funding a Testnet Account

info

The [Flow Testnet Faucet](https://testnet-faucet.onflow.org/) allows users to create accounts and receive 1,000 Testnet FLOW tokens for testing and development purposes. You can also fund an existing Testnet accounts without needing to create one through the site, or through the CLI.

Fund a valid Testnet Flow Account using the Flow CLI.

`_10

flow accounts fund <address>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_10

> flow accounts fund 8e94eaa81771313a

_10

_10

Opening the faucet to fund 0x8e94eaa81771313a on your native browser.

_10

_10

If there is an issue, please use this link instead: https://testnet-faucet.onflow.org/fund-account?address=8e94eaa81771313a`

## Arguments[​](#arguments "Direct link to Arguments")

### Address[​](#address "Direct link to Address")

* Name: `address`
* Valid Input: Flow Testnet account address.

Flow [account address](/build/basics/accounts) (prefixed with `0x` or not).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/accounts/account-fund.md)

Last updated on **Mar 6, 2025** by **Giovanni Sanchez**

[Previous

Account Staking Info](/tools/flow-cli/accounts/account-staking-info)[Next

Generate Keys](/tools/flow-cli/keys/generate-keys)

###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Address](#address)

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