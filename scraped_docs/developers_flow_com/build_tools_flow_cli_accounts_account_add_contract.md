# Source: https://developers.flow.com/build/tools/flow-cli/accounts/account-add-contract

Deploy a Contract | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              - [Install Instructions](/build/tools/flow-cli/install)- [Commands Overview](/build/tools/flow-cli/commands)- [Accounts](/build/tools/flow-cli/accounts/get-accounts)

                    * [Get an Account](/build/tools/flow-cli/accounts/get-accounts)* [Create an Account](/build/tools/flow-cli/accounts/create-accounts)* [Deploy a Contract](/build/tools/flow-cli/accounts/account-add-contract)* [Update a Contract](/build/tools/flow-cli/accounts/account-update-contract)* [Remove a Contract](/build/tools/flow-cli/accounts/account-remove-contract)* [Account Staking Info](/build/tools/flow-cli/accounts/account-staking-info)* [Funding a Testnet Account](/build/tools/flow-cli/accounts/account-fund)- [Keys](/build/tools/flow-cli/keys/generate-keys)

                      - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                        - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                          - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                            - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                              - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                  - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Accounts* Deploy a Contract

On this page

# Deploy a Contract

Deploy a new contract to a Flow account using the Flow CLI.

`_10

flow accounts add-contract <filename> [<argument> <argument>...] [flags]`

⚠️ Deprecation notice: using name argument in adding contract command will be deprecated soon.

`_10

flow accounts add-contract <name> <filename> [<argument> <argument>...] [flags]`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_18

> flow accounts add-contract ./FungibleToken.cdc

_18

_18

Contract 'FungibleToken' deployed to the account 0xf8d6e0586b0a20c7

_18

_18

Address 0xf8d6e0586b0a20c7

_18

Balance 99999999999.70000000

_18

Keys 1

_18

_18

Key 0 Public Key 640a5a359bf3536d15192f18d872d57c98a96cb871b92b70cecb0739c2d5c37b4be12548d3526933c2cda9b0b9c69412f45ffb6b85b6840d8569d969fe84e5b7

_18

Weight 1000

_18

Signature Algorithm ECDSA_P256

_18

Hash Algorithm SHA3_256

_18

Revoked false

_18

Sequence Number 6

_18

Index 0

_18

_18

Contracts Deployed: 1

_18

Contract: 'FungibleToken'`

**Testnet Example**

`_18

> flow accounts add-contract ./FungibleToken.cdc --signer alice --network testnet

_18

_18

Contract 'FungibleToken' deployed to the account 0xf8d6e0586b0a20c7

_18

_18

Address 0xf8d6e0586b0a20c7

_18

Balance 99999999999.70000000

_18

Keys 1

_18

_18

Key 0 Public Key 640a5a359bf3536d15192f18d872d57c98a96cb871b92b70cecb0739c2d5c37b4be12548d3526933c2cda9b0b9c69412f45ffb6b85b6840d8569d969fe84e5b7

_18

Weight 1000

_18

Signature Algorithm ECDSA_P256

_18

Hash Algorithm SHA3_256

_18

Revoked false

_18

Sequence Number 6

_18

Index 0

_18

_18

Contracts Deployed: 1

_18

Contract: 'FungibleToken'`

*Make sure alice account is defined in flow.json*

## Arguments[​](#arguments "Direct link to Arguments")

### Name[​](#name "Direct link to Name")

* Name: `name`
* Valid inputs: any string value.

Name of the contract as it is defined in the contract source code.

⚠️ Deprecation notice: use filename argument only, no need to use name argument.

### Filename[​](#filename "Direct link to Filename")

* Name: `filename`
* Valid inputs: a path in the current filesystem.

Path to the file containing the contract source code.

### Arguments[​](#arguments-1 "Direct link to Arguments")

* Name: `argument`
* Valid inputs: valid [cadence values](https://cadencelang.dev/docs/1.0/json-cadence-spec)
  matching argument type in transaction code.

Input arguments values matching corresponding types in the source code and passed in the same order.

Example:

`_10

> flow accounts add-contract ./contract.cdc Hello 2`

Transaction code:

`_10

access(all) contract HelloWorld {

_10

init(a:String, b:Int) {

_10

}

_10

}`

## Flags[​](#flags "Direct link to Flags")

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used to sign the transaction.

### Arguments JSON[​](#arguments-json "Direct link to Arguments JSON")

* Flag: `--args-json`
* Valid inputs: arguments in JSON-Cadence form.
* Example: `flow accounts add-contract ./tx.cdc '[{"type": "String", "value": "Hello"}]'`

Arguments passed to the Cadence transaction in Cadence JSON format.
Cadence JSON format contains `type` and `value` keys and is
[documented here](https://cadencelang.dev/docs/1.0/json-cadence-spec).

### Include Fields[​](#include-fields "Direct link to Include Fields")

* Flag: `--include`
* Valid inputs: `contracts`

Specify fields to include in the result output. Applies only to the text output.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be
used to execute the command. This flag overrides
any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be
used to create a secure GRPC client when executing the command.

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in the configuration (`flow.json`).
* Default: `emulator`

Specify which network you want the command to use for execution.

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

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see during command execution.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: a path in the current filesystem.
* Default: `flow.json`

Specify the path to the `flow.json` configuration file.
You can use the `-f` flag multiple times to merge
several configuration files.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/accounts/account-add-contract.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Create an Account](/build/tools/flow-cli/accounts/create-accounts)[Next

Update a Contract](/build/tools/flow-cli/accounts/account-update-contract)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Usage](#example-usage)* [Arguments](#arguments)
    + [Name](#name)+ [Filename](#filename)+ [Arguments](#arguments-1)* [Flags](#flags)
      + [Signer](#signer)+ [Arguments JSON](#arguments-json)+ [Include Fields](#include-fields)+ [Host](#host)+ [Network Key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version Check](#version-check)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.