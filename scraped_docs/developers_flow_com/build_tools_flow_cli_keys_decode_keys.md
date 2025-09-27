# Source: https://developers.flow.com/build/tools/flow-cli/keys/decode-keys

Decode Public Keys | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/quickstart)

  + [Quickstart ↙](/build/cadence/quickstart)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Basics](/build/cadence/basics/network-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)

      * [Generate Keys](/build/tools/flow-cli/keys/generate-keys)
      * [Decode Public Keys](/build/tools/flow-cli/keys/decode-keys)
      * [Derive Public Key](/build/tools/flow-cli/keys/derive-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
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
* Keys
* Decode Public Keys

On this page

# Decode Public Keys

The Flow CLI provides a command to decode encoded public account keys.

`_10

flow keys decode <rlp|pem> <encoded public key>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Decode RLP Encoded Public Key[​](#decode-rlp-encoded-public-key "Direct link to Decode RLP Encoded Public Key")

`_10

> flow keys decode rlp f847b84084d716c14b051ad6b001624f738f5d302636e6b07cc75e4530af7776a4368a2b586dbefc0564ee28384c2696f178cbed52e62811bcc9ecb59568c996d342db2402038203e8

_10

_10

Public Key 84d716c1...bcc9ecb59568c996d342db24

_10

Signature algorithm ECDSA_P256

_10

Hash algorithm SHA3_256

_10

Weight 1000

_10

Revoked false`

### Decode PEM Encoded Public Key From File[​](#decode-pem-encoded-public-key-from-file "Direct link to Decode PEM Encoded Public Key From File")

`_10

> flow keys decode pem --from-file key.pem

_10

_10

Public Key d479b3c...c4615360039a6660a366a95f

_10

Signature algorithm ECDSA_P256

_10

Hash algorithm UNKNOWN

_10

Revoked false`

## Arguments[​](#arguments "Direct link to Arguments")

### Encoding[​](#encoding "Direct link to Encoding")

* Valid inputs: `rlp`, `pem`

First argument specifies a valid encoding of the public key provided.

### Optional: Public Key[​](#optional-public-key "Direct link to Optional: Public Key")

* Name: `encoded public key`
* Valid inputs: valid encoded key content

Optional second argument provides content of the encoded public key.
If this argument is omitted the `--from-file` must be used instead.

## Flags[​](#flags "Direct link to Flags")

### From File[​](#from-file "Direct link to From File")

* Flag: `--from-file`
* Valid inputs: valid filepath

Provide file with the encoded public key.

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

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/keys/decode-keys.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Generate Keys](/build/tools/flow-cli/keys/generate-keys)[Next

Derive Public Key](/build/tools/flow-cli/keys/derive-keys)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
  + [Decode RLP Encoded Public Key](#decode-rlp-encoded-public-key)
  + [Decode PEM Encoded Public Key From File](#decode-pem-encoded-public-key-from-file)
* [Arguments](#arguments)
  + [Encoding](#encoding)
  + [Optional: Public Key](#optional-public-key)
* [Flags](#flags)
  + [From File](#from-file)
  + [Filter](#filter)
  + [Output](#output)
  + [Save](#save)
  + [Version Check](#version-check)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
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