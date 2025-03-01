# Source: https://developers.flow.com/tools/flow-cli/transactions/decode-transactions

Build a Complex Transaction | Flow Developer Portal



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
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Transactions
* Build a Complex Transaction

On this page

# Build a Complex Transaction

The Flow CLI provides a command to decode a transaction
from RLP in a file. It uses same transaction format as get command

`_10

flow transactions decode <file>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_19

> flow transactions decode ./rlp-file.rlp

_19

_19

ID c1a52308fb906358d4a33c1f1d5fc458d3cfea0d570a51a9dea915b90d678346

_19

Payer 83de1a7075f190a1

_19

Authorizers [83de1a7075f190a1]

_19

_19

Proposal Key:

_19

Address 83de1a7075f190a1

_19

Index 1

_19

Sequence 1

_19

_19

No Payload Signatures

_19

_19

Envelope Signature 0: 83de1a7075f190a1

_19

Signatures (minimized, use --include signatures)

_19

_19

Code (hidden, use --include code)

_19

_19

Payload (hidden, use --include payload)`

## Arguments[​](#arguments "Direct link to Arguments")

### Filename[​](#filename "Direct link to Filename")

* Name: `<file_name>`
* Valid Input: file name.

The first argument is the filename containing the transaction RLP.

## Flags[​](#flags "Direct link to Flags")

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`, `signatures`

Specify fields to include in the result output. Applies only to the text output.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/transactions/decode-transactions.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Send Signed Transaction](/tools/flow-cli/transactions/send-signed-transactions)[Next

Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)

###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
* [Arguments](#arguments)
  + [Filename](#filename)
* [Flags](#flags)
  + [Include Fields](#include-fields)
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