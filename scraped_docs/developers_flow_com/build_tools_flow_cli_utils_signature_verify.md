# Source: https://developers.flow.com/build/tools/flow-cli/utils/signature-verify

Verify Signature | Flow Developer Portal



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
  + [Guides](/build/cadence/guides/account-linking)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
  + [Guides](/build/evm/guides)
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
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)

      * [Generate a Signature](/build/tools/flow-cli/utils/signature-generate)
      * [Verify Signature](/build/tools/flow-cli/utils/signature-verify)
      * [Snapshot Save](/build/tools/flow-cli/utils/snapshot-save)
      * [Development Tools](/build/tools/flow-cli/utils/tools)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Cadence Boilerplate](/build/tools/flow-cli/boilerplate)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Utils
* Verify Signature

On this page

# Verify Signature

Verify validity of a signature based on provided message and public key of the signature creator.

`_10

flow signatures verify <message> <signature> <public key>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_11

> flow signatures verify

_11

'The quick brown fox jumps over the lazy dog'

_11

b1c9eff5d829fdeaf2dad6308fc8033e3b8875bc185ef804ce5d0d980545ef5be0f98b47afc979d12272d257ce13c4b490e431bfcada485cb1d2e3f209be8d07

_11

0xc92a7c72a78f8f046a79f8a5fe1ef72424258a55eb869f13e6133301d64ad025d3362d5df9e7c82289637af1431042c4025d241fd430242368ce662d39636987

_11

_11

Valid true

_11

Message The quick brown fox jumps over the lazy dog

_11

Signature b1c9eff5d829fdeaf2...7ce13c4b490eada485cb1d2e3f209be8d07

_11

Public Key c92a7c72a78...1431042c4025d241fd430242368ce662d39636987

_11

Hash Algorithm SHA3_256

_11

Signature Algorithm ECDSA_P256`

## Arguments[​](#arguments "Direct link to Arguments")

### Message[​](#message "Direct link to Message")

* Name: `message`

Message data used for creating the signature.

### Signature[​](#signature "Direct link to Signature")

* Name: `signature`

Message signature that will be verified.

### Public Key[​](#public-key "Direct link to Public Key")

* Name: `public key`

Public key of the private key used for creating the signature.

## Flags[​](#flags "Direct link to Flags")

### Public Key Signature Algorithm[​](#public-key-signature-algorithm "Direct link to Public Key Signature Algorithm")

* Flag: `--sig-algo`
* Valid inputs: `"ECDSA_P256", "ECDSA_secp256k1"`

Specify the ECDSA signature algorithm of the key pair used for signing.

Flow supports the secp256k1 and P-256 curves.

### Public Key Hash Algorithm[​](#public-key-hash-algorithm "Direct link to Public Key Hash Algorithm")

* Flag: `--hash-algo`
* Valid inputs: `"SHA2_256", "SHA3_256"`
* Default: `"SHA3_256"`

Specify the hash algorithm of the key pair used for signing.

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

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/utils/signature-verify.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Generate a Signature](/build/tools/flow-cli/utils/signature-generate)[Next

Snapshot Save](/build/tools/flow-cli/utils/snapshot-save)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Message](#message)
  + [Signature](#signature)
  + [Public Key](#public-key)
* [Flags](#flags)
  + [Public Key Signature Algorithm](#public-key-signature-algorithm)
  + [Public Key Hash Algorithm](#public-key-hash-algorithm)
  + [Filter](#filter)
  + [Output](#output)
  + [Save](#save)
  + [Log](#log)
  + [Version Check](#version-check)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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
* [EVM](/build/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.