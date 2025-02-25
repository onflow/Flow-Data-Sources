# Source: https://developers.flow.com/tools/flow-cli/deployment/start-emulator

Start Emulator | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)

  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)

    - [Start Emulator](/tools/flow-cli/deployment/start-emulator)
    - [Add Project Contracts](/tools/flow-cli/deployment/project-contracts)
    - [Deploy a Project](/tools/flow-cli/deployment/deploy-project-contracts)
    - [Create Emulator Snapshot](/tools/flow-cli/deployment/emulator-snapshot)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/deployment/start-emulator.md)

Last updated on **Feb 18, 2025** by **BT.Wood(Tang Bo Hao)**

[Previous

Derive Public Key](/tools/flow-cli/keys/derive-keys)[Next

Add Project Contracts](/tools/flow-cli/deployment/project-contracts)

###### Rate this page

😞😐😊

* [Initial Configuration](#initial-configuration)
* [Starting the Emulator](#starting-the-emulator)
  + [Example Output](#example-output)
* [Customizing the Emulator](#customizing-the-emulator)
* [Learn More](#learn-more)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.