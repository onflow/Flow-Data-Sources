# Source: https://developers.flow.com/tools/emulator

Flow Emulator | Flow Developer Portal



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

Then start the Flow Emulator:

`_10

flow emulator`

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

## Common Options[​](#common-options "Direct link to Common Options")

`_14

# Start with verbose logging

_14

flow emulator --verbose

_14

_14

# Set custom block time (e.g., 1 second between blocks)

_14

flow emulator --block-time 1s

_14

_14

# Persist state between restarts

_14

flow emulator --persist

_14

_14

# Change the gRPC and REST API ports

_14

flow emulator --port 9000 --rest-port 9001

_14

_14

# For a complete list of available flags, run:

_14

flow emulator --help`

For all available options, see the [CLI commands overview](/build/tools/flow-cli).

## Debugging & Testing[​](#debugging--testing "Direct link to Debugging & Testing")

* **Code Coverage**: Add `--coverage-reporting` flag and visit `http://localhost:8080/emulator/codeCoverage`
* **Debugging**: Use `#debugger()` pragma in Cadence code for breakpoints

## Snapshots[​](#snapshots "Direct link to Snapshots")

The Flow CLI provides a command to create emulator snapshots, which are points in blockchain history you can later jump to and reset the state to that moment. This can be useful for testing where you establish a beginning state, run tests and after revert back to the initial state.

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

To learn more about using the Emulator, have a look at the [README of the repository](https://github.com/onflow/flow-emulator).

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

For advanced configuration options, see the [Flow Emulator repository](https://github.com/onflow/flow-emulator/).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/emulator/index.md)

Last updated on **Oct 9, 2025** by **Brian Doyle**

[Previous

Components](/build/tools/react-sdk/components)[Next

Flow CLI](/build/tools/flow-cli)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)* [Quick Start](#quick-start)* [Common Options](#common-options)* [Debugging & Testing](#debugging--testing)* [Snapshots](#snapshots)
          + [Create a new snapshot](#create-a-new-snapshot)+ [Load an existing snapshot](#load-an-existing-snapshot)+ [List all existing snapshots](#list-all-existing-snapshots)* [Additional Resources](#additional-resources)

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