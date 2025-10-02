# Source: https://developers.flow.com/tools/emulator

Flow Emulator | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/quickstart)

  + [Quickstart ↙](/build/cadence/quickstart)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Basics](/build/cadence/basics/network-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* Flow Emulator

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

This starts a local Flow network with:

* gRPC server on port `3569`
* REST API on `http://localhost:8888`
* Admin API on port `8080`

## Common Options[​](#common-options "Direct link to Common Options")

`_10

# Start with verbose logging

_10

flow emulator --verbose

_10

_10

# Set custom block time (e.g., 1 second between blocks)

_10

flow emulator --block-time 1s

_10

_10

# Persist state between restarts

_10

flow emulator --persist`

For all available options, see the [CLI commands overview](/build/tools/flow-cli).

## Debugging & Testing[​](#debugging--testing "Direct link to Debugging & Testing")

* **Code Coverage**: Add `--coverage-reporting` flag and visit `http://localhost:8080/emulator/codeCoverage`
* **Debugging**: Use `#debugger()` pragma in Cadence code for breakpoints

## Additional Resources[​](#additional-resources "Direct link to Additional Resources")

For advanced configuration options, see the [Flow Emulator repository](https://github.com/onflow/flow-emulator/).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/emulator/index.md)

Last updated on **Sep 26, 2025** by **Chase Fleming**

[Previous

Flow React SDK Components](/build/tools/react-sdk/components)[Next

Flow CLI](/build/tools/flow-cli)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)
* [Quick Start](#quick-start)
* [Common Options](#common-options)
* [Debugging & Testing](#debugging--testing)
* [Additional Resources](#additional-resources)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.