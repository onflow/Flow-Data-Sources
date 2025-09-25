# Source: https://developers.flow.com/build/tools/flow-cli/transactions/sign-transaction

Sign a Transaction | Flow Developer Portal



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
    - [Commands Overview](/build/tools/flow-cli/commands)
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
* Sign a Transaction

On this page

# Sign a Transaction

The Flow CLI provides a command to sign transactions with options to specify
authorizer accounts, payer accounts and proposer accounts.

Use this functionality in the following order:

1. Use the `build` command to build the transaction.
2. Use this command (`sign`) to sign with each account specified in the build process.
3. Use the `send-signed` command to submit the signed transaction to the Flow network.

`_10

flow transactions sign <built transaction filename>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_41

> flow transactions sign ./built.rlp --signer alice \

_41

--filter payload --save signed.rlp

_41

_41

Hash b03b18a8d9d30ff7c9f0fdaa80fcaab242c2f36eedb687dd9b368326311fe376

_41

Payer f8d6e0586b0a20c7

_41

Authorizers [f8d6e0586b0a20c7]

_41

_41

Proposal Key:

_41

Address f8d6e0586b0a20c7

_41

Index 0

_41

Sequence 6

_41

_41

No Envelope Signatures

_41

_41

Payload Signature 0:

_41

Address f8d6e0586b0a20c7

_41

Signature b5b1dfed2a899037...164e1b224a7ac924018e7033b68b0df86769dd54

_41

Key Index 0

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

f90184f...a199bfd9b837a11a0885f9104b54014750f5e3e5bfe4a5795968b0df86769dd54c0`

## Arguments[​](#arguments "Direct link to Arguments")

### Built Transaction Filename or Remote Server URL[​](#built-transaction-filename-or-remote-server-url "Direct link to Built Transaction Filename or Remote Server URL")

* Name: `built transaction filename | --from-remote-url <url>`
* Valid inputs: Any filename and path valid on the system or --from-remote-url flag and fully qualified remote server url.

Specify the filename containing valid transaction payload that will be used for signing.
To be used with the `flow transaction build` command.

When --from-remote-url flag is used the value needs to be a fully qualified url to transaction RLP
Example: `flow transaction sign --from-remote-url https://fully/qualified/url --signer alice`

## Flags[​](#flags "Direct link to Flags")

### From Remote Url[​](#from-remote-url "Direct link to From Remote Url")

* Flag: `--from-remote-url`
* Valid input: `http(s)://fully/qualified/server/url`

Specify this flag with a fully qualified url to transaction RLP. The RLP will be fetched from server then signed. The resulting signed RLP is then posted to the remote url. This feature is to support protocol level multiple signature transaction coordination between multiple signers.
Note: --yes flag is not supported and will fail `sign` command when this flag is used. This forces the user to verify the cadence code.

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`

Specify fields to include in the result output. Applies only to the text output.

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

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

* Flag: `--conf`
* Short Flag: `-f`
* Valid inputs: valid filename

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/sign-transaction.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Build a Complex Transaction](/build/tools/flow-cli/transactions/complex-transactions)[Next

Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Built Transaction Filename or Remote Server URL](#built-transaction-filename-or-remote-server-url)
* [Flags](#flags)
  + [From Remote Url](#from-remote-url)
  + [Include Fields](#include-fields)
  + [Signer](#signer)
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
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.