# Source: https://developers.flow.com/build/tools/flow-cli/transactions/get-system-transactions

Get a System Transaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [@onflow/react-sdk](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                    - [Keys](/build/tools/flow-cli/keys/generate-keys)

                      - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                        - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            * [Send a Transaction](/build/tools/flow-cli/transactions/send-transactions)* [Get a Transaction](/build/tools/flow-cli/transactions/get-transactions)* [Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/complex-transactions)* [Sign a Transaction](/build/tools/flow-cli/transactions/sign-transaction)* [Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/decode-transactions)* [Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)- [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Transactions* Get a System Transaction

On this page

# Get a System Transaction

The Flow CLI provides a command to fetch the system transaction for a given block reference. You can optionally provide a transaction ID to target a specific system transaction within that block.

`_10

flow transactions get-system <block_id|latest|block_height> [tx_id]`

warning

Querying with a system transaction ID (`[tx_id]`) is part of the Forte network upgrade and is currently available on Flow Emulator (CLI v2.7.0+) and [Flow Testnet](/protocol/flow-networks/accessing-testnet). See the announcement for context: [Forte: Introducing Actions & Agents](https://flow.com/post/forte-introducing-actions-agents-supercharging-composability-and-automation).

## Use Cases[​](#use-cases "Direct link to Use Cases")

* System chunk transaction for protocol operations: see [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events) and [Staking rewards via system chunk](/protocol/staking/staking-rewards).
* Transactions related to scheduled transactions: see [Introduction to Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction). Consider `--include fee-events` for scheduled transaction fee details.

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_23

> flow transactions get-system latest --network mainnet

_23

_23

Status ✅ SEALED

_23

ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_23

Payer —

_23

Authorizers []

_23

_23

Proposal Key: —

_23

_23

No Payload Signatures

_23

No Envelope Signatures

_23

_23

Events:

_23

Index 0

_23

Type A.1654653399040a61.FlowToken.TokensDeposited

_23

Tx ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_23

Values

_23

- amount (UFix64): 0.00100000

_23

- to ({}?): 5068e27f275c546c

_23

_23

Code (hidden, use --include code)

_23

_23

Payload (hidden, use --include payload)`

Select a specific system transaction within the block by ID:

`_10

> flow transactions get-system latest 07a8...b433 --network mainnet`

## Arguments[​](#arguments "Direct link to Arguments")

### Block Reference[​](#block-reference "Direct link to Block Reference")

* Name: `<block_id|latest|block_height>`
* Valid Input: a block ID (hex), the keyword `latest`, or a block height (number).

The first argument is a reference to the block whose system transaction you want to fetch.

### Transaction ID (optional)[​](#transaction-id-optional "Direct link to Transaction ID (optional)")

* Name: `[tx_id]`
* Valid Input: a transaction ID (hex).

Optionally narrow the result to a specific system transaction within the referenced block.

## Flags[​](#flags "Direct link to Flags")

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`, `fee-events`

Specify fields to include in the result output. Applies only to the text output.

### Exclude Fields[​](#exclude-fields "Direct link to Exclude Fields")

* Flag: `--exclude`
* Valid inputs: `events`

Specify fields to exclude from the result output. Applies only to the text output.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or host address.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the host address of the Access API that will be
used to execute the command. This flag overrides
any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be
used to create secure client connections when executing the command.

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in the configuration (`flow.json`)
* Default: `emulator`

Specify which network you want the command to use for execution.

### Filter[​](#filter "Direct link to Filter")

* Flag: `--filter`
* Short Flag: `-x`
* Valid inputs: a case-sensitive name of the result property.

Specify any property name from the result you want to return as the only value.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify the format of the command results.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: a path in the current file system.

Specify the filename where you want the result to be saved

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see during command execution.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: a path in the current file system.
* Default: `flow.json`

Specify the path to the `flow.json` configuration file.
You can use the `-f` flag multiple times to merge
several configuration files.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

## Notes[​](#notes "Direct link to Notes")

System transactions currently cover:

* System chunk transactions used by protocol operations. See an overview of system chunks and service events: [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events).
* Scheduled transaction execution. Learn more: [Introduction to Scheduled Transaction].

More resources:

* [Staking rewards via system chunk](/protocol/staking/staking-rewards)
* [Epoch schedule and system chunk transactions](/protocol/staking/schedule)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/get-system-transactions.md)

Last updated on **Sep 24, 2025** by **Brian Doyle**

[Previous

Build a Complex Transaction](/build/tools/flow-cli/transactions/decode-transactions)[Next

Initialize Configuration](/build/tools/flow-cli/flow.json/initialize-configuration)

###### Rate this page

😞😐😊

Copy as Markdown

* [Use Cases](#use-cases)* [Example Usage](#example-usage)* [Arguments](#arguments)
      + [Block Reference](#block-reference)+ [Transaction ID (optional)](#transaction-id-optional)* [Flags](#flags)
        + [Include Fields](#include-fields)+ [Exclude Fields](#exclude-fields)+ [Host](#host)+ [Network Key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version Check](#version-check)* [Notes](#notes)

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