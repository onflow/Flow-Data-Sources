# Source: https://developers.flow.com/build/tools/flow-cli/transactions/get-transactions

Get a Transaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/super-commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

      * [Send a Transaction](/build/tools/flow-cli/transactions/send-transactions)
      * [Get a Transaction](/build/tools/flow-cli/transactions/get-transactions)
      * [Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)
      * [Build a Complex Transaction](/build/tools/flow-cli/transactions/complex-transactions)
      * [Sign a Transaction](/build/tools/flow-cli/transactions/sign-transaction)
      * [Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)
      * [Build a Complex Transaction](/build/tools/flow-cli/transactions/decode-transactions)
      * [Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)
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
* Transactions
* Get a Transaction

On this page

# Get a Transaction

The Flow CLI provides a command to fetch a transaction
that was previously submitted to an Access API.

`_10

flow transactions get <tx_id>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_44

> flow transactions get 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa --network mainnet

_44

_44

Status ✅ SEALED

_44

ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_44

Payer 18eb4ee6b3c026d2

_44

Authorizers [18eb4ee6b3c026d2]

_44

_44

Proposal Key:

_44

Address 18eb4ee6b3c026d2

_44

Index 11

_44

Sequence 17930

_44

_44

Payload Signature 0: 18eb4ee6b3c026d2

_44

Payload Signature 1: 18eb4ee6b3c026d2

_44

Envelope Signature 0: 18eb4ee6b3c026d2

_44

Signatures (minimized, use --include signatures)

_44

_44

Events:

_44

Index 0

_44

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_44

Tx ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_44

Values

_44

- amount (UFix64): 0.00100000

_44

- from ({}?): 18eb4ee6b3c026d2

_44

_44

Index 1

_44

Type A.1654653399040a61.FlowToken.TokensDeposited

_44

Tx ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_44

Values

_44

- amount (UFix64): 0.00100000

_44

- to ({}?): 5068e27f275c546c

_44

_44

Index 2

_44

Type A.18eb4ee6b3c026d2.PrivateReceiverForwarder.PrivateDeposit

_44

Tx ID 40bc4b100c1930c61381c22e0f4c10a7f5827975ee25715527c1061b8d71e5aa

_44

Values

_44

- amount (UFix64): 0.00100000

_44

- to ({}?): 5068e27f275c546c

_44

_44

_44

_44

Code (hidden, use --include code)

_44

_44

Payload (hidden, use --include payload)`

## Arguments[​](#arguments "Direct link to Arguments")

### Transaction ID[​](#transaction-id "Direct link to Transaction ID")

* Name: `<tx_id>`
* Valid Input: transaction ID.

The first argument is the ID (hash) of the transaction.

## Flags[​](#flags "Direct link to Flags")

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`

Specify fields to include in the result output. Applies only to the text output.

### Wait for Seal[​](#wait-for-seal "Direct link to Wait for Seal")

* Flag: `--sealed`
* Default: `false`

Indicate whether to wait for the transaction to be sealed
before displaying the result.

### Exclude Fields[​](#exclude-fields "Direct link to Exclude Fields")

* Flag: `--exclude`
* Valid inputs: `events`

Specify fields to exclude from the result output. Applies only to the text output.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be
used to execute the command. This flag overrides
any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be
used to create a secure GRPC client when executing the command.

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
* Valid inputs: a path in the current filesystem.

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
* Valid inputs: a path in the current filesystem.
* Default: `flow.json`

Specify the path to the `flow.json` configuration file.
You can use the `-f` flag multiple times to merge
several configuration files.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/get-transactions.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Send a Transaction](/build/tools/flow-cli/transactions/send-transactions)[Next

Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Transaction ID](#transaction-id)
* [Flags](#flags)
  + [Include Fields](#include-fields)
  + [Wait for Seal](#wait-for-seal)
  + [Exclude Fields](#exclude-fields)
  + [Host](#host)
  + [Network Key](#network-key)
  + [Network](#network)
  + [Filter](#filter)
  + [Output](#output)
  + [Save](#save)
  + [Log](#log)
  + [Configuration](#configuration)
  + [Version Check](#version-check)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
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
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.