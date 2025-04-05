# Source: https://developers.flow.com/tools/flow-cli/transactions/build-transactions

Build a Transaction | Flow Developer Portal



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
* Build a Transaction

On this page

# Build a Transaction

The Flow CLI provides a command to build a transactions with options to specify
authorizer accounts, payer account and proposer account.

The `build` command doesn't produce any signatures and instead
is designed to be used with the `sign` and `send-signed` commands.

Use this functionality in the following order:

1. Use this command (`build`) to build the transaction.
2. Use the `sign` command to sign with each account specified in the build process.
3. Use the `send-signed` command to submit the signed transaction to the Flow network.

`_10

flow transactions build <code filename> [<argument> <argument>...] [flags]`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_41

> flow transactions build ./transaction.cdc "Meow" \

_41

--authorizer alice \

_41

--proposer bob \

_41

--payer charlie \

_41

--filter payload --save built.rlp

_41

_41

ID e8c0a69952fbe50a66703985e220307c8d44b8fa36c76cbca03f8c43d0167847

_41

Payer e03daebed8ca0615

_41

Authorizers [f3fcd2c1a78f5eee]

_41

_41

Proposal Key:

_41

Address 179b6b1cb6755e31

_41

Index 0

_41

Sequence 1

_41

_41

No Payload Signatures

_41

_41

No Envelope Signatures

_41

_41

_41

Arguments (1):

_41

- Argument 0: {"type":"String","value":"Meow"}

_41

_41

_41

Code

_41

_41

transaction(greeting: String) {

_41

let guest: Address

_41

_41

prepare(authorizer: &Account) {

_41

self.guest = authorizer.address

_41

}

_41

_41

execute {

_41

log(greeting.concat(",").concat(self.guest.toString()))

_41

}

_41

}

_41

_41

_41

Payload:

_41

f9013df90138b8d17472616e...73616374696f6e286eeec0c0`

JSON arguments from a file example:

`_10

> flow transactions build tx1.cdc --args-json "$(cat args.json)"`

## Arguments[​](#arguments "Direct link to Arguments")

### Code Filename[​](#code-filename "Direct link to Code Filename")

* Name: `filename`
* Valid inputs: Any filename and path valid on the system.

The first argument is a path to a Cadence file containing the
transaction to be executed.

### Arguments[​](#arguments-1 "Direct link to Arguments")

* Name: `argument`
* Valid inputs: valid [cadence values](https://cadencelang.dev/docs/1.0/json-cadence-spec)
  matching argument type in transaction code.

Input arguments values matching corresponding types in the source code and passed in the same order.
For passing complex argument values see [send transaction](/tools/flow-cli/transactions/send-transactions#example-usage) document.

## Flags[​](#flags "Direct link to Flags")

### Payer[​](#payer "Direct link to Payer")

* Flag: `--payer`
* Valid Inputs: Flow address or account name from configuration.
* Default: service account

Specify account address that will be paying for the transaction.
Read more about payers [here](/build/basics/transactions).

### Proposer[​](#proposer "Direct link to Proposer")

* Flag: `--proposer`
* Valid inputs: Flow address or account name from configuration.
* Default: service account

Specify a name of the account that is proposing the transaction.
Account must be defined in flow configuration.

### Proposer Key Index[​](#proposer-key-index "Direct link to Proposer Key Index")

* Flag: `--proposer-key-index`
* Valid inputs: number of existing key index
* Default: 0

Specify key index for the proposer account.

### Authorizer[​](#authorizer "Direct link to Authorizer")

* Flag: `--authorizer`
* Valid Inputs: Flow address or account name from configuration.
* Default: service account

Additional authorizer addresses to add to the transaction.
Read more about authorizers [here](/build/basics/transactions).

### Arguments JSON[​](#arguments-json "Direct link to Arguments JSON")

* Flag: `--args-json`
* Valid inputs: arguments in JSON-Cadence form.
* Example: `flow transactions build ./tx.cdc '[{"type": "String", "value": "Hello World"}]'`

Arguments passed to the Cadence transaction in Cadence JSON format.
Cadence JSON format contains `type` and `value` keys and is
[documented here](https://cadencelang.dev/docs/1.0/json-cadence-spec).

### Gas Limit[​](#gas-limit "Direct link to Gas Limit")

* Flag: `--gas-limit`
* Valid inputs: an integer greater than zero.
* Default: `1000`

Specify the gas limit for this transaction.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be
used to execute the commands.

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

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`

Specify fields to include in the result output. Applies only to the text output.

### Filter[​](#filter "Direct link to Filter")

* Flag: `--filter`
* Short Flag: `-x`
* Valid inputs: case-sensitive name of the result property.

Specify any property name from the result you want to return as the only value.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify in which format you want to display the result.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: valid filename

Specify the filename where you want the result to be saved.

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see while command execution.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: valid filename

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/transactions/build-transactions.md)

Last updated on **Mar 31, 2025** by **Josh Hannan**

[Previous

Get a Transaction](/tools/flow-cli/transactions/get-transactions)[Next

Build a Complex Transaction](/tools/flow-cli/transactions/complex-transactions)

###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Code Filename](#code-filename)
  + [Arguments](#arguments-1)
* [Flags](#flags)
  + [Payer](#payer)
  + [Proposer](#proposer)
  + [Proposer Key Index](#proposer-key-index)
  + [Authorizer](#authorizer)
  + [Arguments JSON](#arguments-json)
  + [Gas Limit](#gas-limit)
  + [Host](#host)
  + [Network Key](#network-key)
  + [Network](#network)
  + [Include Fields](#include-fields)
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