# Source: https://developers.flow.com/tools/flow-cli/transactions/get-transactions

Get a Transaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)

    - [Send a Transaction](/tools/flow-cli/transactions/send-transactions)
    - [Get a Transaction](/tools/flow-cli/transactions/get-transactions)
    - [Build a Transaction](/tools/flow-cli/transactions/build-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/complex-transactions)
    - [Sign a Transaction](/tools/flow-cli/transactions/sign-transaction)
    - [Send Signed Transaction](/tools/flow-cli/transactions/send-signed-transactions)
    - [Build a Complex Transaction](/tools/flow-cli/transactions/decode-transactions)
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
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/transactions/get-transactions.md)

Last updated on **Mar 31, 2025** by **Josh Hannan**

[Previous

Send a Transaction](/tools/flow-cli/transactions/send-transactions)[Next

Build a Transaction](/tools/flow-cli/transactions/build-transactions)

###### Rate this page

😞😐😊

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