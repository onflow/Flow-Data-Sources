# Source: https://developers.flow.com/tools/flow-cli/flow.json/initialize-configuration

Initialize Configuration | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
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

    - [Initialize Configuration](/tools/flow-cli/flow.json/initialize-configuration)
    - [Configuration](/tools/flow-cli/flow.json/configuration)
    - [Manage Configuration](/tools/flow-cli/flow.json/manage-configuration)
    - [Security](/tools/flow-cli/flow.json/security)
  + [Flow Entities](/tools/flow-cli/get-flow-data/get-blocks)
  + [Utils](/tools/flow-cli/utils/signature-generate)
  + [Dependency Manager](/tools/flow-cli/dependency-manager)
  + [Running Cadence Tests](/tools/flow-cli/tests)
  + [Cadence Linter](/tools/flow-cli/lint)
  + [Flow Interaction Templates (FLIX)](/tools/flow-cli/flix)
  + [Cadence Boilerplate](/tools/flow-cli/boilerplate)
  + [Data Collection](/tools/flow-cli/data-collection)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Flow CLI](/tools/flow-cli)
* Flow.json
* Initialize Configuration

On this page

# Initialize Configuration

Flow CLI uses a state to operate which is called configuration (usually `flow.json` file).
Before using commands that require this configuration we must initialize the project by
using the init command. Read more about [state configuration here](/tools/flow-cli/flow.json/configuration).

`_10

flow init`

## Example Usage[​](#example-usage "Direct link to Example Usage")

`_10

> flow init

_10

_10

Configuration initialized

_10

Service account: 0xf8d6e0586b0a20c7

_10

_10

Start emulator by running: 'flow emulator'

_10

Reset configuration using: 'flow init --reset'`

### Error Handling[​](#error-handling "Direct link to Error Handling")

Existing configuration will cause the error below.
You should initialize in an empty folder or reset configuration using `--reset` flag
or by removing the configuration file first.

`_10

❌ Command Error: configuration already exists at: flow.json, if you want to reset configuration use the reset flag`

## Global Configuration[​](#global-configuration "Direct link to Global Configuration")

Flow supports global configuration which is a `flow.json` file saved in your home
directory and loaded as the first configuration file wherever you execute the CLI command.

Please be aware that global configuration has the lowest priority and is overwritten
by any other configuration file if they exist (if `flow.json` exist in your current
directory it will overwrite properties in global configuration, but only those which overlap).

You can generate a global configuration using `--global` flag.

Command example: `flow init --global`.

Global flow configuration is saved as:

* MacOs: `~/flow.json`
* Linux: `~/flow.json`
* Windows: `C:\Users\$USER\flow.json`

## Flags[​](#flags "Direct link to Flags")

### Reset[​](#reset "Direct link to Reset")

* Flag: `--reset`

Using this flag will reset the existing configuration and create a new one.

### Global[​](#global "Direct link to Global")

* Flag: `--global`

Using this flag will create a global Flow configuration.

### Service Private Key[​](#service-private-key "Direct link to Service Private Key")

* Flag: `--service-private-key`
* Valid inputs: a hex-encoded private key in raw form.

Private key used on the default service account.

### Service Key Signature Algorithm[​](#service-key-signature-algorithm "Direct link to Service Key Signature Algorithm")

* Flag: `--service-sig-algo`
* Valid inputs: `"ECDSA_P256", "ECDSA_secp256k1"`
* Default: `"ECDSA_P256"`

Specify the ECDSA signature algorithm for the provided public key.

Flow supports the secp256k1 and P-256 curves.

### Service Key Hash Algorithm[​](#service-key-hash-algorithm "Direct link to Service Key Hash Algorithm")

* Flag: `--service-hash-algo`
* Valid inputs: `"SHA2_256", "SHA3_256"`
* Default: `"SHA3_256"`

Specify the hashing algorithm that will be paired with the public key
upon account creation.

### Log[​](#log "Direct link to Log")

* Flag: `--log`
* Short Flag: `-l`
* Valid inputs: `none`, `error`, `debug`
* Default: `info`

Specify the log level. Control how much output you want to see while command execution.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/flow.json/initialize-configuration.md)

Last updated on **Mar 31, 2025** by **Josh Hannan**

[Previous

Build a Complex Transaction](/tools/flow-cli/transactions/decode-transactions)[Next

Configuration](/tools/flow-cli/flow.json/configuration)

###### Rate this page

😞😐😊

* [Example Usage](#example-usage)
  + [Error Handling](#error-handling)
* [Global Configuration](#global-configuration)
* [Flags](#flags)
  + [Reset](#reset)
  + [Global](#global)
  + [Service Private Key](#service-private-key)
  + [Service Key Signature Algorithm](#service-key-signature-algorithm)
  + [Service Key Hash Algorithm](#service-key-hash-algorithm)
  + [Log](#log)

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