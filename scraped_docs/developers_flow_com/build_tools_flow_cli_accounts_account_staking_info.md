# Source: https://developers.flow.com/build/tools/flow-cli/accounts/account-staking-info

Account Staking Info | Flow Developer Portal



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

                      * [Get an Account](/build/tools/flow-cli/accounts/get-accounts)* [Create an Account](/build/tools/flow-cli/accounts/create-accounts)* [Deploy a Contract](/build/tools/flow-cli/accounts/account-add-contract)* [Update a Contract](/build/tools/flow-cli/accounts/account-update-contract)* [Remove a Contract](/build/tools/flow-cli/accounts/account-remove-contract)* [Account Staking Info](/build/tools/flow-cli/accounts/account-staking-info)* [Funding a Testnet Account](/build/tools/flow-cli/accounts/account-fund)- [Keys](/build/tools/flow-cli/keys/generate-keys)

                        - [Deploy Project](/build/tools/flow-cli/deployment/project-contracts)

                          - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)

                            - [Transactions](/build/tools/flow-cli/transactions/send-transactions)

                              - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)

                                - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)

                                  - [Utils](/build/tools/flow-cli/utils/signature-generate)

                                    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)- [Running Cadence Tests](/build/tools/flow-cli/tests)- [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)- [Cadence Linter](/build/tools/flow-cli/lint)- [Scheduled Transactions](/build/tools/flow-cli/scheduled-transactions)- [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)- [Fork Testing](/build/tools/flow-cli/fork-testing)- [Data Collection](/build/tools/flow-cli/data-collection)+ [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Accounts* Account Staking Info

On this page

# Account Staking Info

Retrieve staking information for the account on the Flow network with Flow CLI.

`_10

flow accounts staking-info <address>`

## Example usage[​](#example-usage "Direct link to Example usage")

`_26

> accounts staking-info 535b975637fb6bee --host access.testnet.nodes.onflow.org:9000

_26

_26

Account Staking Info:

_26

ID: "ca00101101010100001011010101010101010101010101011010101010101010"

_26

Initial Weight: 100

_26

Networking Address: "ca00101101010100001011010101010101010101010101011010101010101010"

_26

Networking Key: "ca00101101010100001011010101010101010101010101011010101010101010ca00101101010100001011010101010101010101010101011010101010101010"

_26

Role: 1

_26

Staking Key: "ca00101101010100001011010101010101010101010101011010101010101010ca00101101010100001011010101010101010101010101011010101010101010ca00101101010100001011010101010101010101010101011010101010101010"

_26

Tokens Committed: 0.00000000

_26

Tokens To Unstake: 0.00000000

_26

Tokens Rewarded: 82627.77000000

_26

Tokens Staked: 250000.00000000

_26

Tokens Unstaked: 0.00000000

_26

Tokens Unstaking: 0.00000000

_26

Node Total Stake (including delegators): 250000.00000000

_26

_26

_26

Account Delegation Info:

_26

ID: 7

_26

Tokens Committed: 0.00000000

_26

Tokens To Unstake: 0.00000000

_26

Tokens Rewarded: 30397.81936000

_26

Tokens Staked: 100000.00000000

_26

Tokens Unstaked: 0.00000000

_26

Tokens Unstaking: 0.00000000`

## Arguments[​](#arguments "Direct link to Arguments")

### Address[​](#address "Direct link to Address")

* Name: `address`
* Valid Input: Flow account address.

Flow [account address](/build/cadence/basics/accounts) (prefixed with `0x` or not).

## Flags[​](#flags "Direct link to Flags")

### Include fields[​](#include-fields "Direct link to Include fields")

* Flag: `--include`
* Valid inputs: `contracts`

Specify fields to include in the result output. Applies only to the text output.

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
* Valid inputs: a case-sensitive name of the result property

Specify any property name from the result you want to return as the only value.

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify the format of the command results.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: a path in the current filesystem

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
* Valid inputs: a path in the current filesystem
* Default: `flow.json`

Specify the path to the `flow.json` configuration file.
You can use the `-f` flag multiple times to merge
several configuration files.

### Version check[​](#version-check "Direct link to Version check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/accounts/account-staking-info.md)

Last updated on **Dec 10, 2025** by **cshannon1218**

[Previous

Remove a Contract](/build/tools/flow-cli/accounts/account-remove-contract)[Next

Funding a Testnet Account](/build/tools/flow-cli/accounts/account-fund)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example usage](#example-usage)* [Arguments](#arguments)
    + [Address](#address)* [Flags](#flags)
      + [Include fields](#include-fields)+ [Host](#host)+ [Network key](#network-key)+ [Network](#network)+ [Filter](#filter)+ [Output](#output)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version check](#version-check)

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