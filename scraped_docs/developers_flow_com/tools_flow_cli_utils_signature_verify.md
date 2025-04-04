# Source: https://developers.flow.com/tools/flow-cli/utils/signature-verify

Verify Signature | Flow Developer Portal



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
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)

    - [Generate a Signature](/tools/flow-cli/utils/signature-generate)
    - [Verify Signature](/tools/flow-cli/utils/signature-verify)
    - [Snapshot Save](/tools/flow-cli/utils/snapshot-save)
    - [Development Tools](/tools/flow-cli/utils/tools)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/utils/signature-verify.md)

Last updated on **Mar 28, 2025** by **Jordan Ribbink**

[Previous

Generate a Signature](/tools/flow-cli/utils/signature-generate)[Next

Snapshot Save](/tools/flow-cli/utils/snapshot-save)

###### Rate this page

😞😐😊

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