# Source: https://developers.flow.com/build/tools/flow-cli/transactions/send-transactions

Send a Transaction | Flow Developer Portal



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

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Transactions* Send a Transaction

On this page

# Send a Transaction

The Flow CLI provides a command to sign and send transactions to
any Flow Access API.

`_10

flow transactions send <code filename> [<argument> <argument>...] [flags]`

## Example use[​](#example-use "Direct link to Example use")

`_22

> flow transactions send ./tx.cdc "Hello"

_22

_22

Status ✅ SEALED

_22

ID b04b6bcc3164f5ee6b77fa502c3a682e0db57fc47e5b8a8ef3b56aae50ad49c8

_22

Payer f8d6e0586b0a20c7

_22

Authorizers [f8d6e0586b0a20c7]

_22

_22

Proposal Key:

_22

Address f8d6e0586b0a20c7

_22

Index 0

_22

Sequence 0

_22

_22

No Payload Signatures

_22

_22

Envelope Signature 0: f8d6e0586b0a20c7

_22

Signatures (minimized, use --include signatures)

_22

_22

Events: None

_22

_22

Code (hidden, use --include code)

_22

_22

Payload (hidden, use --include payload)`

Multiple arguments example:

`_10

> flow transactions send tx1.cdc Foo 1 2 10.9 0x1 '[123,222]' '["a","b"]'`

Transaction code:

`_10

transaction(a: String, b: Int, c: UInt16, d: UFix64, e: Address, f: [Int], g: [String]) {

_10

prepare(authorizer: &Account) {}

_10

}`

In the above example, the `flow.json` file would look something like this:

`_10

{

_10

"accounts": {

_10

"my-testnet-account": {

_10

"address": "a2c4941b5f3c7151",

_10

"key": "12c5dfde...bb2e542f1af710bd1d40b2"

_10

}

_10

}

_10

}`

JSON arguments from a file example:

`_10

> flow transactions send tx1.cdc --args-json "$(cat args.json)"`

## Arguments[​](#arguments "Direct link to Arguments")

### Code filename[​](#code-filename "Direct link to Code filename")

* Name: `code filename`
* Valid inputs: Any filename and path valid on the system.

The first argument is a path to a Cadence file that contains the transaction to be executed.

### Arguments[​](#arguments-1 "Direct link to Arguments")

* Name: `argument`
* Valid inputs: valid [cadence values](https://cadencelang.dev/docs/1.0/json-cadence-spec) that matches the argument type in transaction code.

Input arguments values that match types which correspond in the source code and passed in the same order. to can pass a `nil` value to optional arguments, send the transaction like this: `flow transactions send tx.cdc nil`.

## Flags[​](#flags "Direct link to Flags")

### Include fields[​](#include-fields "Direct link to Include fields")

* Flag: `--include`
* Valid inputs: `code`, `payload`

Specify fields to include in the result output. Applies only to the text output.

### Code[​](#code "Direct link to Code")

* Flag: `--code`

⚠️ No longer supported: use filename argument.

### Results[​](#results "Direct link to Results")

* Flag: `--results`

⚠️ No longer supported: all transactions will provide result.

### Exclude fields[​](#exclude-fields "Direct link to Exclude fields")

* Flag: `--exclude`
* Valid inputs: `events`

Specify fields to exclude from the result output. Applies only to the text output.

### Signer[​](#signer "Direct link to Signer")

* Flag: `--signer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`).

Specify the name of the account that will be used to sign the transaction.

### Proposer[​](#proposer "Direct link to Proposer")

* Flag: `--proposer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used as the proposer in the transaction.

### Payer[​](#payer "Direct link to Payer")

* Flag: `--payer`
* Valid inputs: the name of an account defined in the configuration (`flow.json`)

Specify the name of the account that will be used as the payer in the transaction.

### Authorizer[​](#authorizer "Direct link to Authorizer")

* Flag: `--authorizer`
* Valid inputs: the name of a single or multiple comma-separated accounts defined in the configuration (`flow.json`)

Specify the name of the account(s) that will be used as authorizer(s) in the transaction. If you want to provide multiple authorizers, separate them with commas (for example, `alice,bob`)

### Arguments JSON[​](#arguments-json "Direct link to Arguments JSON")

* Flag: `--args-json`
* Valid inputs: arguments in JSON-Cadence form.
* Example: `flow transactions send ./tx.cdc '[{"type": "String", "value": "Hello World"}]'`

Arguments passed to the Cadence transaction in Cadence JSON format.
The Cadence JSON format contains `type` and `value` keys and is
[documented here](https://cadencelang.dev/docs/1.0/json-cadence-spec).

### Compute Limit[​](#compute-limit "Direct link to Compute Limit")

* Flag: `--compute-limit`
* Valid inputs: an integer greater than zero.
* Default: `1000`

Specify the compute unit (gas) limit for this transaction.

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname.
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be used to execute the command. This flag overrides any host defined by the `--network` flag.

### Network key[​](#network-key "Direct link to Network key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be used to create a secure GRPC client when you execute the command.

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in the configuration (`flow.json`)
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

Specify the filename where you want to save the result.

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

Specify the path to the `flow.json` configuration file. You can use the `-f` flag multiple times to merge several configuration files.

### Version check[​](#version-check "Direct link to Version check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/send-transactions.md)

Last updated on **Dec 15, 2025** by **cshannon1218**

[Previous

Execute a Script](/build/tools/flow-cli/scripts/execute-scripts)[Next

Get a Transaction](/build/tools/flow-cli/transactions/get-transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example use](#example-use)* [Arguments](#arguments)
    + [Code filename](#code-filename)+ [Arguments](#arguments-1)* [Flags](#flags)
      + [Include fields](#include-fields)+ [Code](#code)+ [Results](#results)+ [Exclude fields](#exclude-fields)+ [Signer](#signer)+ [Proposer](#proposer)+ [Payer](#payer)+ [Authorizer](#authorizer)+ [Arguments JSON](#arguments-json)+ [Compute Limit](#compute-limit)+ [Host](#host)+ [Network key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version check](#version-check)

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