# Source: https://developers.flow.com/tools/flow-cli/deployment/emulator-snapshot

Create Emulator Snapshot | Flow Developer Portal



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
* Create Emulator Snapshot

On this page

# Create Emulator Snapshot

The Flow CLI provides a command to create emulator snapshots, which are points in blockchain
history you can later jump to and reset the state to that moment. This can be useful for testing where you
establish a begining state, run tests and after revert back to the initial state.

The command syntax is:

`_10

flow emulator snapshot create|load|list {name}`

## Example Usage[​](#example-usage "Direct link to Example Usage")

### Create a new snapshot[​](#create-a-new-snapshot "Direct link to Create a new snapshot")

Create a new emulator snapshot at the current block with a name of `myInitialState`.

`_10

> flow emulator snapshot create myInitialState`

### Load an existing snapshot[​](#load-an-existing-snapshot "Direct link to Load an existing snapshot")

To jump to a previously created snapshot we use the load command in combination with the name.

`_10

> flow emulator snapshot load myInitialState`

### List all existing snapshots[​](#list-all-existing-snapshots "Direct link to List all existing snapshots")

To list all the existing snapshots we previously created and can load to we run the following command:

`_10

> flow emulator list`

To learn more about using the Emulator, have a look at the [README of the repository](https://github.com/onflow/flow-emulator).

## Flags[​](#flags "Direct link to Flags")

### Emulator Flags[​](#emulator-flags "Direct link to Emulator Flags")

You can specify any [emulator flags found here](https://github.com/onflow/flow-emulator#configuration) and they will be applied to the emulator service.

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: valid filename

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/deployment/emulator-snapshot.md)

Last updated on **Feb 22, 2025** by **Brian Doyle**

[Previous

Deploy a Project](/tools/flow-cli/deployment/deploy-project-contracts)[Next

Execute a Script](/tools/flow-cli/scripts/execute-scripts)

###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
  + [Create a new snapshot](#create-a-new-snapshot)
  + [Load an existing snapshot](#load-an-existing-snapshot)
  + [List all existing snapshots](#list-all-existing-snapshots)
* [Flags](#flags)
  + [Emulator Flags](#emulator-flags)
  + [Configuration](#configuration)
  + [Version Check](#version-check)

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