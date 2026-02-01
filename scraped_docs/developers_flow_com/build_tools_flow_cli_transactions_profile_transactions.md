# Source: https://developers.flow.com/build/tools/flow-cli/transactions/profile-transactions

Profile a Transaction | Flow Developer Portal



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

* * [Tools & SDKs](/build/tools)* [Flow CLI](/build/tools/flow-cli)* Transactions* Profile a Transaction

On this page

# Profile a Transaction

The Flow CLI provides a command to profile the computational performance of sealed transactions on any Flow network. This diagnostic tool generates detailed CPU profiles in the industry-standard `pprof` format, allowing you to analyze exactly where computation is being spent during transaction execution.

info

The command works by forking the blockchain state and replaying the transaction in an isolated environment, ensuring accurate profiling results that match the original execution. Learn more about state forking in the [Fork Testing guide](/build/tools/flow-cli/fork-testing).

`_10

flow transactions profile <tx_id> --network <network_name> [flags]`

## Use Cases[​](#use-cases "Direct link to Use Cases")

Transaction profiling helps developers:

* **Optimize Transaction Costs**: Identify computational bottlenecks and optimize gas-heavy operations
* **Debug High Gas Usage**: Understand why a transaction consumed more computation than expected
* **Analyze Production Transactions**: Profile real transactions on mainnet or testnet to understand actual performance
* **Compare Implementations**: Evaluate different approaches by comparing their computational profiles
* **Find Performance Issues**: Trace computation usage through contract calls and dependencies

## Example Usage[​](#example-usage "Direct link to Example Usage")

Profile a mainnet transaction:

`_16

> flow transactions profile 07a8...b433 --network mainnet

_16

_16

Transaction Profiling Report

_16

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

_16

_16

Transaction ID: 07a8...b433

_16

Network: mainnet

_16

Block Height: 12345678

_16

Status: SEALED

_16

Events emitted: 5

_16

Computation: 1234

_16

_16

Profile saved: profile-07a8b433.pb.gz

_16

_16

Analyze with:

_16

go tool pprof -http=:8080 profile-07a8b433.pb.gz`

Profile with custom output location:

`_10

> flow transactions profile 0xabc123 --network testnet --output my-profile.pb.gz

_10

_10

Profile saved: my-profile.pb.gz`

Profile an emulator transaction:

`_10

> flow transactions profile 0xdef456 --network emulator`

## Analyzing Profile Data[​](#analyzing-profile-data "Direct link to Analyzing Profile Data")

The generated `.pb.gz` file can be analyzed using Go's pprof tools. If you don't have Go installed, see the [Go installation guide](https://go.dev/doc/install).

### Interactive Web Interface[​](#interactive-web-interface "Direct link to Interactive Web Interface")

Open the profile in an interactive web interface:

`_10

go tool pprof -http=:8080 profile-07a8b433.pb.gz`

Then navigate to `http://localhost:8080` in your browser.

The pprof web interface provides several visualization options:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| View Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | **Flame Graph** Visual representation of call stacks with computation costs|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | **Graph** Directed graph showing call relationships|  |  |  |  | | --- | --- | --- | --- | | **Top** List of functions sorted by computation usage|  |  | | --- | --- | | **Source** Source code annotated with computation costs | | | | | | | | | |

### Command-Line Analysis[​](#command-line-analysis "Direct link to Command-Line Analysis")

View top computation consumers:

`_10

go tool pprof -top profile-07a8b433.pb.gz`

List all functions with costs:

`_10

go tool pprof -list=. profile-07a8b433.pb.gz`

Generate a flame graph image:

`_10

go tool pprof -png profile-07a8b433.pb.gz > profile.png`

For comprehensive information on analyzing computation profiles, see the [Cadence Computation Profiling guide](/build/cadence/advanced-concepts/computation-profiling).

## How It Works[​](#how-it-works "Direct link to How It Works")

The profiling process:

1. **Fetches the Transaction**: Retrieves the target sealed transaction by ID from the specified network
2. **Forks Blockchain State**: Creates a fork of the blockchain state from the block immediately before the transaction's block (uses the same forking mechanism as [Fork Testing](/build/tools/flow-cli/fork-testing))
3. **Replays Execution**: Replays all prior transactions in the same block to recreate the exact state
4. **Profiles Target Transaction**: Executes the target transaction with Cadence runtime profiling enabled
5. **Exports Profile**: Saves the profiling data to a pprof-compatible file

This ensures the profile accurately reflects the transaction's execution in its original context.

info

The transaction profiling command uses Flow's state forking capabilities under the hood to create an accurate execution environment. Learn more about state forking in the [Fork Testing guide](/build/tools/flow-cli/fork-testing).

## Arguments[​](#arguments "Direct link to Arguments")

### Transaction ID[​](#transaction-id "Direct link to Transaction ID")

* Name: `<tx_id>`
* Valid Input: transaction ID (with or without `0x` prefix)

The transaction ID to profile. The transaction must be sealed.

## Flags[​](#flags "Direct link to Flags")

### Network[​](#network "Direct link to Network")

* Flag: `--network`
* Short Flag: `-n`
* Valid inputs: the name of a network defined in `flow.json`
* **Required**

Specify which network the transaction was executed on (e.g., `mainnet`, `testnet`, `emulator`).

### Output[​](#output "Direct link to Output")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: valid file path
* Default: `profile-{tx_id_prefix}.pb.gz`

Custom output file path for the profile data. The file will be saved in compressed pprof format (`.pb.gz`).

### Host[​](#host "Direct link to Host")

* Flag: `--host`
* Valid inputs: an IP address or hostname
* Default: `127.0.0.1:3569` (Flow Emulator)

Specify the hostname of the Access API that will be used to fetch transaction data. This flag overrides any host defined by the `--network` flag.

### Network Key[​](#network-key "Direct link to Network Key")

* Flag: `--network-key`
* Valid inputs: A valid network public key of the host in hex string format

Specify the network public key of the Access API that will be used to create a secure GRPC client when executing the command.

### Filter[​](#filter "Direct link to Filter")

* Flag: `--filter`
* Short Flag: `-x`
* Valid inputs: a case-sensitive name of the result property

Specify any property name from the result you want to return as the only value.

### Output Format[​](#output-format "Direct link to Output Format")

* Flag: `--output`
* Short Flag: `-o`
* Valid inputs: `json`, `inline`

Specify the format of the command results displayed in the console.

### Save[​](#save "Direct link to Save")

* Flag: `--save`
* Short Flag: `-s`
* Valid inputs: a path in the current filesystem

Specify the filename where you want the result summary to be saved.

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

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

## Requirements[​](#requirements "Direct link to Requirements")

### Transaction Must Be Sealed[​](#transaction-must-be-sealed "Direct link to Transaction Must Be Sealed")

Only sealed transactions can be profiled. Attempting to profile a pending or finalized transaction will result in an error.

`_10

Error: transaction is not sealed (status: PENDING)`

Wait for the transaction to be sealed before profiling, or use a different transaction.

### Network Configuration[​](#network-configuration "Direct link to Network Configuration")

The network must be properly configured in your `flow.json` file:

`_10

{

_10

"networks": {

_10

"mainnet": "access.mainnet.nodes.onflow.org:9000",

_10

"testnet": "access.devnet.nodes.onflow.org:9000"

_10

}

_10

}`

### Go Toolchain (for analysis)[​](#go-toolchain-for-analysis "Direct link to Go Toolchain (for analysis)")

To analyze the generated profile files, you need Go installed on your system. The `pprof` tool is included in the standard Go distribution.

Install Go from: <https://go.dev/doc/install>

## Related Documentation[​](#related-documentation "Direct link to Related Documentation")

* **[Cadence Computation Profiling](/build/cadence/advanced-concepts/computation-profiling)** - Comprehensive guide on profiling and optimization
* **[Fork Testing Guide](/build/tools/flow-cli/fork-testing)** - Learn more about the state forking capabilities used by this command
* **[Testing Strategy](/build/cadence/smart-contracts/testing-strategy)** - How profiling fits into your overall testing and optimization workflow
* **[Transaction Fees](/build/cadence/basics/fees)** - Understanding computation costs and fee optimization

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/transactions/profile-transactions.md)

Last updated on **Jan 31, 2026** by **Jordan Ribbink**

[Previous

Get a System Transaction](/build/tools/flow-cli/transactions/get-system-transactions)[Next

Initialize Configuration](/build/tools/flow-cli/flow.json/initialize-configuration)

###### Rate this page

😞😐😊

Copy as Markdown

* [Use Cases](#use-cases)* [Example Usage](#example-usage)* [Analyzing Profile Data](#analyzing-profile-data)
      + [Interactive Web Interface](#interactive-web-interface)+ [Command-Line Analysis](#command-line-analysis)* [How It Works](#how-it-works)* [Arguments](#arguments)
          + [Transaction ID](#transaction-id)* [Flags](#flags)
            + [Network](#network)+ [Output](#output)+ [Host](#host)+ [Network Key](#network-key)+ [Filter](#filter)+ [Output Format](#output-format)+ [Save](#save)+ [Log](#log)+ [Configuration](#configuration)+ [Version Check](#version-check)* [Requirements](#requirements)
              + [Transaction Must Be Sealed](#transaction-must-be-sealed)+ [Network Configuration](#network-configuration)+ [Go Toolchain (for analysis)](#go-toolchain-for-analysis)* [Related Documentation](#related-documentation)

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