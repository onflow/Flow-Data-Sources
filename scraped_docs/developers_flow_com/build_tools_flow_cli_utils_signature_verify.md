# Source: https://developers.flow.com/build/tools/flow-cli/utils/signature-verify

Verify Signature | Flow Developer Portal



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

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    * [Generate a Signature](/build/tools/flow-cli/utils/signature-generate)* [Verify Signature](/build/tools/flow-cli/utils/signature-verify)* [Snapshot Save](/build/tools/flow-cli/utils/snapshot-save)* [Development Tools](/build/tools/flow-cli/utils/tools)- [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Utils* Verify Signature

On this page

# Verify Signature

Verify validity of a signature based on provided message and public key of the signature creator.

`_10

flow signatures verify <message> <signature> <public key>`

## Example use[​](#example-use "Direct link to Example use")

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

Message data used to create the signature.

### Signature[​](#signature "Direct link to Signature")

* Name: `signature`

Message signature that will be verified.

### Public Key[​](#public-key "Direct link to Public Key")

* Name: `public key`

Public key of the private key used to create the signature.

## Flags[​](#flags "Direct link to Flags")

### Public key signature algorithm[​](#public-key-signature-algorithm "Direct link to Public key signature algorithm")

* Flag: `--sig-algo`
* Valid inputs: `"ECDSA_P256", "ECDSA_secp256k1"`

Specify the ECDSA signature algorithm of the key pair used for signing.

Flow supports the secp256k1 and P-256 curves.

### Public key hash algorithm[​](#public-key-hash-algorithm "Direct link to Public key hash algorithm")

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

Specify the log level. Control how much output you want to see while the command executes.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/utils/signature-verify.md)

Last updated on **Dec 15, 2025** by **cshannon1218**

[Previous

Generate a Signature](/build/tools/flow-cli/utils/signature-generate)[Next

Snapshot Save](/build/tools/flow-cli/utils/snapshot-save)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example use](#example-use)* [Arguments](#arguments)
    + [Message](#message)+ [Signature](#signature)+ [Public Key](#public-key)* [Flags](#flags)
      + [Public key signature algorithm](#public-key-signature-algorithm)+ [Public key hash algorithm](#public-key-hash-algorithm)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Version Check](#version-check)

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