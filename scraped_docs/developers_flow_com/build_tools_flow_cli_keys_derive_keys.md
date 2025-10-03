# Source: https://developers.flow.com/build/tools/flow-cli/keys/derive-keys

Derive Public Key | Flow Developer Portal



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

                      * [Generate Keys](/build/tools/flow-cli/keys/generate-keys)* [Decode Public Keys](/build/tools/flow-cli/keys/decode-keys)* [Derive Public Key](/build/tools/flow-cli/keys/derive-keys)- [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)

                        - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Keys* Derive Public Key

On this page

# Derive Public Key

The Flow CLI provides a command to derive Public Key from a Private Key.

`_10

flow keys derive <private key>`

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Derive Public Key from a Private Key[​](#derive-public-key-from-a-private-key "Direct link to Derive Public Key from a Private Key")

`_10

> flow keys derive c778170793026a9a7a3815dabed68ded445bde7f40a8c66889908197412be89f`

### Example response[​](#example-response "Direct link to Example response")

`_10

> flow keys generate

_10

_10

🔴️ Store Private Key safely and don't share with anyone!

_10

Private Key c778170793026a9a7a3815dabed68ded445bde7f40a8c66889908197412be89f

_10

Public Key 584245c57e5316d6606c53b1ce46dae29f5c9bd26e9e8...aaa5091b2eebcb2ac71c75cf70842878878a2d650f7`

## Arguments[​](#arguments "Direct link to Arguments")

### Private Key[​](#private-key "Direct link to Private Key")

* Name: `private key`
* Valid inputs: valid private key content

## Flags[​](#flags "Direct link to Flags")

### Signature Algorithm[​](#signature-algorithm "Direct link to Signature Algorithm")

* Flag: `--sig-algo`
* Valid inputs: `"ECDSA_P256", "ECDSA_secp256k1"`

Specify the ECDSA signature algorithm for the key pair.

Flow supports the secp256k1 and P-256 curves.

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/keys/derive-keys.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Decode Public Keys](/build/tools/flow-cli/keys/decode-keys)[Next

Start Emulator](/build/tools/flow-cli/deployment/start-emulator)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)
  + [Derive Public Key from a Private Key](#derive-public-key-from-a-private-key)+ [Example response](#example-response)* [Arguments](#arguments)
    + [Private Key](#private-key)* [Flags](#flags)
      + [Signature Algorithm](#signature-algorithm)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)

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