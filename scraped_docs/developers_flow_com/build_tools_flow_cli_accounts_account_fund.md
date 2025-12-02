# Source: https://developers.flow.com/build/tools/flow-cli/accounts/account-fund

Funding a Testnet Account | Flow Developer Portal



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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                    * [Get an Account](/build/tools/flow-cli/accounts/get-accounts)* [Create an Account](/build/tools/flow-cli/accounts/create-accounts)* [Deploy a Contract](/build/tools/flow-cli/accounts/account-add-contract)* [Update a Contract](/build/tools/flow-cli/accounts/account-update-contract)* [Remove a Contract](/build/tools/flow-cli/accounts/account-remove-contract)* [Account Staking Info](/build/tools/flow-cli/accounts/account-staking-info)* [Funding a Testnet Account](/build/tools/flow-cli/accounts/account-fund)- [Keys](/build/tools/flow-cli/keys/generate-keys)

                      - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                        - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Accounts* Funding a Testnet Account

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
  + [Fund by Address](#fund-by-address)+ [Fund by Account Name](#fund-by-account-name)+ [Interactive Prompt](#interactive-prompt)* [Arguments](#arguments)
    + [Address or Account Name (Optional)](#address-or-account-name-optional)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.