# Source: https://developers.flow.com/tools/flow-cli/utils/tools




Development Tools | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
  + [Install Instructions](/tools/flow-cli/install)
  + [Super Commands](/tools/flow-cli/super-commands)
  + [Accounts](/tools/flow-cli/accounts/get-accounts)
  + [Keys](/tools/flow-cli/keys/generate-keys)
  + [Deploy Project](/tools/flow-cli/deployment/start-emulator)
  + [Scripts](/tools/flow-cli/scripts/execute-scripts)
  + [Transactions](/tools/flow-cli/transactions/send-transactions)
  + [Flow.json](/tools/flow-cli/flow.json/initialize-configuration)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
    - [Generate a Signature](/tools/flow-cli/utils/signature-generate)
    - [Verify Signature](/tools/flow-cli/utils/signature-verify)
    - [Snapshot Save](/tools/flow-cli/utils/snapshot-save)
    - [Development Tools](/tools/flow-cli/utils/tools)
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
* Utils
* Development Tools
On this page
# Development Tools

The Flow CLI integrates different development tools, which can now be easily started
and managed from a single place.

Currently the CLI supports starting:

* [Flow Development Wallet](https://github.com/onflow/fcl-dev-wallet)

## Flow Development Wallet[​](#flow-development-wallet "Direct link to Flow Development Wallet")

The Flow Dev Wallet is a mock Flow wallet that simulates the protocols used by FCL to interact with the Flow blockchain on behalf of simulated user accounts.

**Be sure you have the emulator running before starting this command**
*You can start it using the `flow emulator` command*.

 `_10flow dev-wallet`

*⚠️ This project implements an FCL compatible
interface, but should **not** be used as a reference for
building a production grade wallet.*

After starting dev-wallet, you can set your fcl config to use it like below:

 `_10import * as fcl from "@onflow/fcl"_10_10fcl.config()_10 // Point App at Emulator_10 .put("accessNode.api", "http://localhost:8080") _10 // Point FCL at dev-wallet (default port)_10 .put("discovery.wallet", "http://localhost:8701/fcl/authn")`

You can read more about setting up dev-wallet at [Flow Dev Wallet Project](https://github.com/onflow/fcl-dev-wallet)

## Flags[​](#flags "Direct link to Flags")

### Port[​](#port "Direct link to Port")

* Flag: `--port`
* Valid inputs: Number
* Default: `8701`

Port on which the dev wallet server will listen on.

### Emulator Host[​](#emulator-host "Direct link to Emulator Host")

* Flag: `--emulator-host`
* Valid inputs: a hostname
* Default: `http://localhost:8080`

Specifies the host configuration for dev wallet

### Configuration[​](#configuration "Direct link to Configuration")

* Flag: `--config-path`
* Short Flag: `-f`
* Valid inputs: valid filename

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

Specify a filename for the configuration files, you can provide multiple configuration
files by using `-f` flag multiple times.

### Version Check[​](#version-check "Direct link to Version Check")

* Flag: `--skip-version-check`
* Default: `false`

Skip version check during start up to speed up process for slow connections.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/utils/tools.md)Last updated on **Jan 14, 2025** by **Giovanni Sanchez**[PreviousSnapshot Save](/tools/flow-cli/utils/snapshot-save)[NextDependency Manager](/tools/flow-cli/dependency-manager)
###### Rate this page

😞😐😊

* [Flow Development Wallet](#flow-development-wallet)
* [Flags](#flags)
  + [Port](#port)
  + [Emulator Host](#emulator-host)
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

