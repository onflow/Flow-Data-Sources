# Source: https://developers.flow.com/build/tools/flow-cli/transactions/decode-transactions

Build a Complex Transaction | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                      - [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              * [Send a Transaction](/build/tools/flow-cli/transactions/send-transactions)* [Get a Transaction](/build/tools/flow-cli/transactions/get-transactions)* [Build a Transaction](/build/tools/flow-cli/transactions/build-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/complex-transactions)* [Sign a Transaction](/build/tools/flow-cli/transactions/sign-transaction)* [Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)* [Build a Complex Transaction](/build/tools/flow-cli/transactions/decode-transactions)* [Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)* [Profile a Transaction](/build/tools/flow-cli/transactions/profile-transactions)- [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Transactions* Build a Complex Transaction

On this page

# Build a Complex Transaction

The Flow CLI provides a command to decode a transaction from RLP in a file. It uses same transaction format as get command

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

The first argument is the filename that contains the transaction RLP.

## Flags[​](#flags "Direct link to Flags")

### Include fields[​](#include-fields "Direct link to Include fields")

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

### Version check[​](#version-check "Direct link to Version check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/decode-transactions.md)

Last updated on **Dec 15, 2025** by **cshannon1218**

[Previous

Send Signed Transaction](/build/tools/flow-cli/transactions/send-signed-transactions)[Next

Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)* [Arguments](#arguments)
    + [Filename](#filename)* [Flags](#flags)
      + [Include fields](#include-fields)+ [Output](#output)+ [Save](#save)+ [Version check](#version-check)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.