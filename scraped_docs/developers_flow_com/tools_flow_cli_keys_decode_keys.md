# Source: https://developers.flow.com/tools/flow-cli/keys/decode-keys

Decode Public Keys | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)

    - [Generate Keys](/tools/flow-cli/keys/generate-keys)
    - [Decode Public Keys](/tools/flow-cli/keys/decode-keys)
    - [Derive Public Key](/tools/flow-cli/keys/derive-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
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
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/keys/decode-keys.md)

Last updated on **Mar 6, 2025** by **Chase Fleming**

[Previous

Generate Keys](/tools/flow-cli/keys/generate-keys)[Next

Derive Public Key](/tools/flow-cli/keys/derive-keys)

###### Rate this page

😞😐😊

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