# Source: https://developers.flow.com/build/tools/flow-cli/scheduled-transactions

Scheduled Transactions | Flow Developer Portal



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

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Scheduled Transactions

On this page

# Scheduled Transactions

The Flow CLI provides commands to manage scheduled transactions. These commands allow you to set up a Manager resource, list scheduled transactions, get transaction details, and cancel transactions.

## What are Scheduled Transactions?[​](#what-are-scheduled-transactions "Direct link to What are Scheduled Transactions?")

Scheduled transactions enable smart contracts to schedule autonomous execution in the future without external triggers. This allows for use cases like recurring payments, automated arbitrage, and time-based contract logic.

The scheduled transactions system uses priorities (High, Medium, Low) with different execution guarantees and fee multipliers to ensure predictable performance while enabling novel autonomous blockchain patterns.

📖 **[Learn more about scheduled transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction)**

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before using the scheduled transactions commands, you must initialize a Manager resource in your account storage. The Manager resource is provided by the **FlowTransactionSchedulerUtils** core contract and provides a convenient way to group, schedule, cancel, and query scheduled transactions through a single resource.

## Why Use the Manager?[​](#why-use-the-manager "Direct link to Why Use the Manager?")

While it's possible to schedule transactions directly, **using the Manager resource is essential for proper tooling integration**. The Manager provides a standardized interface that allows CLI commands, block explorers, and other developer tools to discover and interact with your scheduled transactions.

**Key benefits of using the Manager:**

* **Tooling Integration**: CLI commands and other tools can automatically discover and manage your scheduled transactions
* **Centralized Management**: All your scheduled transactions are organized in one place for easy tracking
* **Enhanced Querying**: Query transactions by handler type, timestamp, or status through standardized interfaces
* **Metadata Access**: Tools can resolve handler views and metadata to provide richer information about your scheduled transactions

Without the Manager, your scheduled transactions exist but cannot be easily discovered or managed through tooling, requiring manual tracking and interaction.

## Commands[​](#commands "Direct link to Commands")

### Setup Manager Resource[​](#setup-manager-resource "Direct link to Setup Manager Resource")

Initialize a Manager resource in your account storage to start managing scheduled transactions.

`_10

flow schedule setup`

This command creates and stores a Manager resource at the standard storage path, allowing you to manage scheduled transactions for your account.

#### Example Usage[​](#example-usage "Direct link to Example Usage")

`_10

flow schedule setup --network testnet --signer my-account`

#### Flags[​](#flags "Direct link to Flags")

* `--signer` - The account that will own the Manager resource
* `--network` / `-n` - Network to execute on (emulator, testnet, mainnet)
* `--host` - Access API hostname
* `--config-path` / `-f` - Path to flow.json configuration file

---

### List Scheduled Transactions[​](#list-scheduled-transactions "Direct link to List Scheduled Transactions")

List all scheduled transactions for a given account that has a Manager resource.

`_10

flow schedule list <account>`

#### Arguments[​](#arguments "Direct link to Arguments")

**Account**

* Name: `account`
* Valid inputs: Flow account address (with or without `0x` prefix) or account name from flow.json

The account address or name that has scheduled transactions to list.

#### Example Usage[​](#example-usage-1 "Direct link to Example Usage")

`_10

flow schedule list 0x01cf0e2f2f715450 --network testnet`

#### Flags[​](#flags-1 "Direct link to Flags")

* `--network` / `-n` - Network to query (emulator, testnet, mainnet)
* `--host` - Access API hostname
* `--output` / `-o` - Output format (`json`, `inline`)
* `--filter` / `-x` - Filter output by property name
* `--save` / `-s` - Save output to file
* `--config-path` / `-f` - Path to flow.json configuration file

---

### Get Transaction Details[​](#get-transaction-details "Direct link to Get Transaction Details")

Get detailed information about a specific scheduled transaction by its ID.

`_10

flow schedule get <transaction-id>`

#### Arguments[​](#arguments-1 "Direct link to Arguments")

**Transaction ID**

* Name: `transaction-id`
* Valid inputs: Unsigned integer (UInt64)

The unique identifier of the scheduled transaction to retrieve.

#### Example Usage[​](#example-usage-2 "Direct link to Example Usage")

`_10

flow schedule get 123 --network testnet`

#### Flags[​](#flags-2 "Direct link to Flags")

* `--network` / `-n` - Network to query (emulator, testnet, mainnet)
* `--host` - Access API hostname
* `--output` / `-o` - Output format (`json`, `inline`)
* `--filter` / `-x` - Filter output by property name
* `--save` / `-s` - Save output to file
* `--config-path` / `-f` - Path to flow.json configuration file

---

### Cancel Scheduled Transaction[​](#cancel-scheduled-transaction "Direct link to Cancel Scheduled Transaction")

Cancel a scheduled transaction and receive a partial fee refund.

`_10

flow schedule cancel <transaction-id>`

When you cancel a scheduled transaction, a portion of the fees paid will be refunded based on the configured refund multiplier. The transaction must be in a scheduled state (not already executed or canceled).

#### Arguments[​](#arguments-2 "Direct link to Arguments")

**Transaction ID**

* Name: `transaction-id`
* Valid inputs: Unsigned integer (UInt64)

The unique identifier of the scheduled transaction to cancel.

#### Example Usage[​](#example-usage-3 "Direct link to Example Usage")

`_10

flow schedule cancel 123 --network testnet --signer my-account`

#### Flags[​](#flags-3 "Direct link to Flags")

* `--signer` - Account that owns the Manager resource containing the transaction
* `--network` / `-n` - Network to execute on (emulator, testnet, mainnet)
* `--host` - Access API hostname
* `--output` / `-o` - Output format (`json`, `inline`)
* `--config-path` / `-f` - Path to flow.json configuration file

---

## Common Flags[​](#common-flags "Direct link to Common Flags")

These flags are available across all scheduled transactions commands:

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in the configuration (`flow.json`)
* Default: `emulator`

Specify which network you want the command to use for execution.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be used to execute the commands. This flag overrides any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be used to create a secure GRPC client when executing the command.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: a path in the current filesystem
* Default: `flow.json`

Specify the path to the `flow.json` configuration file. You can use the `-f` flag multiple times to merge several configuration files.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify the format of the command results.

### Filter[​](#filter "Direct link to Filter")

* Flag: `--filter`
* Short Flag: `-x`
* Valid inputs: a case-sensitive name of the result property

Specify any property name from the result you want to return as the only value.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: a path in the current filesystem

Specify the filename where you want the result to be saved.

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see during command execution.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/scheduled-transactions.md)

Last updated on **Oct 22, 2025** by **Chase Fleming**

[Previous

Cadence Linter](/build/tools/flow-cli/lint)[Next

Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)

###### Rate this page

😞😐😊

Copy as Markdown

* [What are Scheduled Transactions?](#what-are-scheduled-transactions)* [Prerequisites](#prerequisites)* [Why Use the Manager?](#why-use-the-manager)* [Commands](#commands)
        + [Setup Manager Resource](#setup-manager-resource)+ [List Scheduled Transactions](#list-scheduled-transactions)+ [Get Transaction Details](#get-transaction-details)+ [Cancel Scheduled Transaction](#cancel-scheduled-transaction)* [Common Flags](#common-flags)
          + [Network](#network)+ [Host](#host)+ [Network Key](#network-key)+ [Configuration](#configuration)+ [Output](#output)+ [Filter](#filter)+ [Save](#save)+ [Log](#log)+ [Version Check](#version-check)

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