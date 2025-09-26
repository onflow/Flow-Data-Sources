# Source: https://developers.flow.com/build/tools/flow-cli/deployment/start-emulator

Start Emulator | Flow Developer Portal



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

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)

      * [Start Emulator](/build/tools/flow-cli/deployment/start-emulator)
      * [Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)
      * [Deploy a Project](/build/tools/flow-cli/deployment/deploy-project-contracts)
      * [Create Emulator Snapshot](/build/tools/flow-cli/deployment/emulator-snapshot)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Generating Cadence Boilerplate](/build/tools/flow-cli/generate)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Deploy Project
* Start Emulator

On this page

# Start Emulator

The Flow Emulator is a lightweight development tool that mimics the behavior of the real Flow network. It is bundled with the [Flow CLI](https://docs.onflow.org/flow-cli/), which makes starting and configuring the emulator straightforward.

## Initial Configuration[​](#initial-configuration "Direct link to Initial Configuration")

The emulator requires a configuration file (`flow.json`). If you don’t already have one, create it using the `flow init` command:

`_10

flow init`

This initializes a default configuration file that the emulator will use.

## Starting the Emulator[​](#starting-the-emulator "Direct link to Starting the Emulator")

To start the emulator with default settings, use the following command:

`_10

flow emulator`

This will start the emulator with the configuration defined in `flow.json`.

### Example Output[​](#example-output "Direct link to Example Output")

When you run the `flow emulator` command, you will see output similar to the following:

`_10

INFO[0000] ⚙️ Using service account 0xf8d6e0586b0a20c7 serviceAddress=f8d6e0586b0a20c7 ...

_10

INFO[0000] 🌱 Starting Flow Emulator

_10

INFO[0000] 🛠 GRPC server started on 127.0.0.1:3569

_10

INFO[0000] 📡 HTTP server started on 127.0.0.1:8080`

## Customizing the Emulator[​](#customizing-the-emulator "Direct link to Customizing the Emulator")

You can customize the emulator behavior by using flags. Here are some examples:

Change the gRPC and REST API ports:

`_10

flow emulator --port 9000 --rest-port 9001`

Enable persistence of state across restarts:

`_10

flow emulator --persist`

Enable detailed logs for debugging:

`_10

flow emulator --verbose`

For a complete list of available flags, run:

`_10

flow emulator --help`

## Learn More[​](#learn-more "Direct link to Learn More")

To explore advanced features like snapshots, rollbacks, and debugging, visit the [Flow Emulator README](https://github.com/onflow/flow-emulator).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/deployment/start-emulator.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Derive Public Key](/build/tools/flow-cli/keys/derive-keys)[Next

Add Project Contracts](/build/tools/flow-cli/deployment/project-contracts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Initial Configuration](#initial-configuration)
* [Starting the Emulator](#starting-the-emulator)
  + [Example Output](#example-output)
* [Customizing the Emulator](#customizing-the-emulator)
* [Learn More](#learn-more)

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