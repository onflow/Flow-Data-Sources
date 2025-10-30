# Source: https://developers.flow.com/build/tools/emulator

Flow Emulator | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

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

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* Flow Emulator

On this page

# Flow Emulator

The Flow Emulator is a lightweight tool that emulates the behavior of the real Flow network for local development and testing.

## Installation[​](#installation "Direct link to Installation")

The emulator is included with the [Flow CLI](/build/tools/flow-cli). Follow the [installation guide](/build/tools/flow-cli/install) to get started.

## Quick Start[​](#quick-start "Direct link to Quick Start")

First, create a `flow.json` configuration file:

`_10

flow init --config-only`

Then start the Flow Emulator in fork mode (defaults to mainnet when value omitted):

`_10

flow emulator --fork`

You'll see output similar to:

`_10

INFO[0000] ⚙️ Using service account 0xf8d6e0586b0a20c7 serviceAddress=f8d6e0586b0a20c7 ...

_10

INFO[0000] 🌱 Starting Flow Emulator

_10

INFO[0000] 🛠 GRPC server started on 127.0.0.1:3569

_10

INFO[0000] 📡 HTTP server started on 127.0.0.1:8080`

This starts a local Flow network with:

* gRPC server on port `3569`
* REST API on `http://localhost:8888`
* Admin API on port `8080`

## Available Commands[​](#available-commands "Direct link to Available Commands")

* `snapshot`: Create/Load/List emulator snapshots. See: [Create Emulator Snapshot](/build/tools/flow-cli/utils/snapshot-save)

## Key Flags[​](#key-flags "Direct link to Key Flags")

* **Networking**

  + `--host <string>`: Host to listen on for gRPC/REST/Admin (default: all interfaces)
  + `--port, -p <int>`: gRPC port (default `3569`)
  + `--rest-port <int>`: REST API port (default `8888`)
  + `--admin-port <int>`: Admin API port (default `8080`)
  + `--debugger-port <int>`: Debug Adapter Protocol port (default `2345`)
  + `--grpc-debug`: Enable gRPC server reflection
  + `--rest-debug`: Enable REST API debug output
* **State & Persistence**

  + `--persist`: Enable persistent storage (default disabled)
  + `--dbpath <path>`: Directory for on-disk state (default `./flowdb`)
  + `--sqlite-url <url>`: Use SQLite storage backend
  + `--redis-url <url>`: Use Redis storage backend
  + `--checkpoint-dir <path>`: Load state from checkpoint directory
  + `--state-hash <string>`: Load state from checkpoint state hash
* **Forking**

  + `--fork <string>`: Start the emulator in fork mode using a network from `flow.json`. If provided without a value, defaults to `mainnet`.
  + `--fork-host <host>`: Access node to query when forking Mainnet/Testnet
  + `--fork-height <uint>`: Starting block height when forking
* **Cadence & VM**

  + `--block-time, -b <duration>`: Time between sealed blocks (e.g. `1s`, `300ms`)
  + `--coverage-reporting`: Enable code coverage reporting
  + `--computation-reporting`: Enable computation reporting
  + `--legacy-upgrade`: Enable legacy contract upgrade behavior
  + `--scheduled-transactions`: Enable scheduled transactions (default true)
  + `--script-gas-limit <int>`: Gas limit for scripts (default `100000`)
  + `--transaction-max-gas-limit <int>`: Max transaction gas limit (default `9999`)
  + `--transaction-expiry <int>`: Transaction expiry in blocks (default `10`)
  + `--skip-tx-validation`: Skip tx signature and sequence number checks
  + `--simple-addresses`: Use sequential addresses starting with `0x01`
  + `--storage-limit`: Enforce account storage limit (default true)
  + `--storage-per-flow <decimal>`: MB of storage per 1 FLOW token
  + `--token-supply <decimal>`: Initial FLOW token supply (default `1000000000.0`)
  + `--transaction-fees`: Enable transaction fees
  + `--setup-evm`: Deploy EVM contracts (default true)
  + `--setup-vm-bridge`: Deploy VM Bridge contracts (default true)
* **Service Account & Identity**

  + `--chain-id <emulator|testnet|mainnet>`: Address generation chain (default `emulator`)
  + `--service-priv-key <hex>` / `--service-pub-key <hex>`: Service account keys
  + `--service-sig-algo <ECDSA_P256|ECDSA_secp256k1>`: Service key signature algo (default `ECDSA_P256`)
  + `--service-hash-algo <SHA3_256|SHA2_256>`: Service key hash algo (default `SHA3_256`)
  + `--min-account-balance <decimal>`: Minimum account balance / account creation cost
  + `--contracts`: Deploy common contracts on start
  + `--contract-removal`: Allow contract removal for development (default true)
  + `--init`: Initialize a new account profile
* **Logging & Output**

  + `--verbose, -v`: Verbose logging
  + `--log-format <text|JSON>`: Logging output format (default `text`)
* **Snapshots**

  + `--snapshot`: Enable snapshots in the emulator

## Examples[​](#examples "Direct link to Examples")

`_32

# Verbose logs

_32

flow emulator --verbose

_32

_32

# Custom ports

_32

flow emulator --port 9000 --rest-port 9001 --admin-port 9002

_32

_32

# Custom block time (1 second between blocks)

_32

flow emulator --block-time 1s

_32

_32

# Persist state on disk

_32

flow emulator --persist --dbpath ./flowdb

_32

_32

# Fork from Mainnet using flow.json

_32

flow emulator --fork

_32

_32

# Fork from Testnet using flow.json and pin to a height

_32

flow emulator --fork testnet --fork-height 12345678

_32

_32

# Fork from Testnet at a specific height

_32

flow emulator --fork-host access.devnet.nodes.onflow.org:9000 --fork-height 12345678

_32

_32

# Disable fees and use simple addresses for local testing

_32

flow emulator --transaction-fees=false --simple-addresses

_32

_32

# Enable code coverage reporting

_32

flow emulator --coverage-reporting

_32

_32

# Change the gRPC and REST API ports

_32

flow emulator --port 9000 --rest-port 9001

_32

_32

# For a complete list of available flags, run:

_32

flow emulator --help`

For the complete and current list of flags, run:

`_10

flow emulator --help`

## Debugging & Testing[​](#debugging--testing "Direct link to Debugging & Testing")

* **Code Coverage**: Add `--coverage-reporting` flag and visit `http://localhost:8080/emulator/codeCoverage`
* **Debugging**: Use `#debugger()` pragma in Cadence code for breakpoints
* **Fork mode note**: When using `flow emulator --fork`, only Flow chain state is available. External oracles/APIs and cross-chain reads are not live; mock these or run local stub services for E2E.

## Snapshots[​](#snapshots "Direct link to Snapshots")

The Flow CLI provides a command to create emulator snapshots, which are points in blockchain history you can later jump to and reset the state to that moment. This can be useful for testing where you establish a beginning state, run tests and after revert back to the initial state.

### Quick snapshot workflow[​](#quick-snapshot-workflow "Direct link to Quick snapshot workflow")

`_10

# 1) Start the emulator with snapshots enabled (in a separate terminal)

_10

flow emulator --snapshot

_10

_10

# 2) Create a snapshot at the current state

_10

flow emulator snapshot create baseline

_10

_10

# 3) Make changes, run tests, etc.

_10

_10

# 4) Reset the emulator back to the snapshot

_10

flow emulator snapshot load baseline`

### Create a new snapshot[​](#create-a-new-snapshot "Direct link to Create a new snapshot")

Create a new emulator snapshot at the current block with a name of `myInitialState`.

`_10

flow emulator snapshot create myInitialState`

### Load an existing snapshot[​](#load-an-existing-snapshot "Direct link to Load an existing snapshot")

To jump to a previously created snapshot we use the load command in combination with the name.

`_10

flow emulator snapshot load myInitialState`

### List all existing snapshots[​](#list-all-existing-snapshots "Direct link to List all existing snapshots")

To list all the existing snapshots we previously created and can load to run:

`_10

flow emulator list`

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

To learn more about using the Emulator, please have a look at the [public GitHub repository](https://github.com/onflow/flow-emulator).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/emulator/index.md)

Last updated on **Oct 29, 2025** by **Jordan Ribbink**

[Previous

Components](/build/tools/react-sdk/components)[Next

Flow CLI](/build/tools/flow-cli)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)* [Quick Start](#quick-start)* [Available Commands](#available-commands)* [Key Flags](#key-flags)* [Examples](#examples)* [Debugging & Testing](#debugging--testing)* [Snapshots](#snapshots)
              + [Quick snapshot workflow](#quick-snapshot-workflow)+ [Create a new snapshot](#create-a-new-snapshot)+ [Load an existing snapshot](#load-an-existing-snapshot)+ [List all existing snapshots](#list-all-existing-snapshots)* [Additional Resources](#additional-resources)

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