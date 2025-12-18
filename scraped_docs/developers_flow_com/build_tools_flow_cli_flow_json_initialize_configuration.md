# Source: https://developers.flow.com/build/tools/flow-cli/flow.json/initialize-configuration

Initialize Configuration | Flow Developer Portal



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

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                * [Initialize Configuration](/build/tools/flow-cli/flow.json/initialize-configuration)* [Configuration](/build/tools/flow-cli/flow.json/configuration)* [Manage Configuration](/build/tools/flow-cli/flow.json/manage-configuration)* [Security](/build/tools/flow-cli/flow.json/security)- [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Flow.json* Initialize Configuration

On this page

# Initialize Configuration

The `flow init` command creates a new Flow project with a basic `flow.json` configuration file. This is the first step in setting up any Flow project.

## Basic Usage[​](#basic-usage "Direct link to Basic Usage")

`_10

flow init`

This command will:

* Create a new `flow.json` configuration file
* Set up default networks (emulator, testnet, mainnet)
* Create an emulator service account
* Generate a basic project structure with `cadence/` directories
* Give you options for project scaffolding

## Project Structure[​](#project-structure "Direct link to Project Structure")

After running `flow init`, you'll have:

`_10

my-project/

_10

├── flow.json

_10

├── emulator-account.pkey

_10

└── cadence/

_10

├── contracts/

_10

├── scripts/

_10

├── transactions/

_10

└── tests/`

## Configuration Only[​](#configuration-only "Direct link to Configuration Only")

If you only want to generate the `flow.json` file without creating the full project structure, use the `--config-only` flag:

`_10

flow init --config-only`

This is useful when:

* You already have a project structure
* You want to add Flow configuration to an existing project
* You're setting up configuration for a specific environment

## Global Configuration[​](#global-configuration "Direct link to Global Configuration")

You can create a global `flow.json` file that applies to all Flow projects on your system:

`_10

flow init --global`

**Global configuration locations:**

* **macOS/Linux:** `~/flow.json`
* **Windows:** `C:\Users\$USER\flow.json`

**Priority order:**

1. Local `flow.json` (highest priority)
2. Global `flow.json` (lowest priority)

Local configuration files will override global settings for overlapping properties.

## Error Handling[​](#error-handling "Direct link to Error Handling")

If a `flow.json` file already exists, you'll see this error:

`_10

❌ Command Error: configuration already exists at: flow.json`

**Solutions:**

* Delete the existing `flow.json` file first
* Initialize in a different directory
* Use `--config-only` to create a new config in a different location

## Flags[​](#flags "Direct link to Flags")

### Configuration Only[​](#configuration-only-1 "Direct link to Configuration Only")

`_10

flow init --config-only`

Creates only the `flow.json` file without project structure.

### Global Flags[​](#global-flags "Direct link to Global Flags")

The following global flags are also available:

`_10

# Log level

_10

flow init --log debug

_10

_10

# Output format

_10

flow init --output json

_10

_10

# Approve prompts automatically

_10

flow init --yes`

**Available log levels:** `debug`, `info`, `error`, `none`

## Next Steps[​](#next-steps "Direct link to Next Steps")

After initializing your configuration:

1. **Review the generated `flow.json`** - Understand the default setup
2. **Add your contracts** - Use `flow config add contract`
3. **Create accounts** - Use `flow accounts create` or `flow config add account`
4. **Configure deployments** - Use `flow config add deployment`
5. **Start developing** - Run `flow emulator start`

## Related Commands[​](#related-commands "Direct link to Related Commands")

* [`flow config add`](/build/tools/flow-cli/flow.json/manage-configuration) - Add configuration items
* [`flow accounts create`](/build/tools/flow-cli/accounts/create-accounts) - Create new accounts
* [`flow project deploy`](/build/tools/flow-cli/deployment/deploy-project-contracts) - Deploy contracts

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/flow.json/initialize-configuration.md)

Last updated on **Oct 9, 2025** by **Brian Doyle**

[Previous

Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)[Next

Configuration](/build/tools/flow-cli/flow.json/configuration)

###### Rate this page

😞😐😊

Copy as Markdown

* [Basic Usage](#basic-usage)* [Project Structure](#project-structure)* [Configuration Only](#configuration-only)* [Global Configuration](#global-configuration)* [Error Handling](#error-handling)* [Flags](#flags)
            + [Configuration Only](#configuration-only-1)+ [Global Flags](#global-flags)* [Next Steps](#next-steps)* [Related Commands](#related-commands)

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