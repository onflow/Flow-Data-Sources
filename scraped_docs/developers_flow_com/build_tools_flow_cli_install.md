# Source: https://developers.flow.com/build/tools/flow-cli/install

Install Instructions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Guides](/build/cadence/guides/account-linking)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
  + [Guides](/build/evm/guides)
* [Tools & SDKs](/build/tools)

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)

    - [Install Instructions](/build/tools/flow-cli/install)
    - [Commands Overview](/build/tools/flow-cli/super-commands)
    - [Accounts](/build/tools/flow-cli/accounts/get-accounts)
    - [Keys](/build/tools/flow-cli/keys/generate-keys)
    - [Deploy Project](/build/tools/flow-cli/deployment/start-emulator)
    - [Scripts](/build/tools/flow-cli/scripts/execute-scripts)
    - [Transactions](/build/tools/flow-cli/transactions/send-transactions)
    - [Flow.json](/build/tools/flow-cli/flow.json/initialize-configuration)
    - [Flow Entities](/build/tools/flow-cli/get-flow-data/get-blocks)
    - [Utils](/build/tools/flow-cli/utils/signature-generate)
    - [Dependency Manager](/build/tools/flow-cli/dependency-manager)
    - [Running Cadence Tests](/build/tools/flow-cli/tests)
    - [Cadence Linter](/build/tools/flow-cli/lint)
    - [Flow Interaction Templates (FLIX)](/build/tools/flow-cli/flix)
    - [Cadence Boilerplate](/build/tools/flow-cli/boilerplate)
    - [Data Collection](/build/tools/flow-cli/data-collection)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Flow CLI](/build/tools/flow-cli)
* Install Instructions

On this page

# Install Instructions

The Flow CLI can be installed on macOS, Windows (7 or greater) and most Linux systems.

## macOS[​](#macos "Direct link to macOS")

### Homebrew[​](#homebrew "Direct link to Homebrew")

`_10

brew install flow-cli`

### From a pre-built binary[​](#from-a-pre-built-binary "Direct link to From a pre-built binary")

*This installation method only works on x86-64.*

This script downloads and installs the appropriate binary for your system:

`_10

sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

To update, simply re-run the installation command above.

It is currently not possible to install earlier versions of the Flow CLI with Homebrew.

## Linux[​](#linux "Direct link to Linux")

### From a pre-built binary[​](#from-a-pre-built-binary-1 "Direct link to From a pre-built binary")

*This installation method only works on x86-64.*

This script downloads and installs the appropriate binary for your system:

`_10

sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

To update, simply re-run the installation command above.

### Install a specific version[​](#install-a-specific-version "Direct link to Install a specific version")

To install a specific version of Flow CLI, the version tag can be appended to the installation command. For example, to install version v2.0.0:

`_10

sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)" -- v2.0.0`

## Windows[​](#windows "Direct link to Windows")

### From a pre-built binary[​](#from-a-pre-built-binary-2 "Direct link to From a pre-built binary")

*This installation method only works on Windows 10, 8.1, or 7 (SP1, with [PowerShell 3.0](https://www.microsoft.com/en-ca/download/details.aspx?id=34595)), on x86-64.*

1. Open PowerShell ([Instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell?view=powershell-7#finding-powershell-in-windows-10-81-80-and-7))
2. In PowerShell, run:

   `_10

   iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"`

To update, simply re-run the installation command above.

# Upgrade the Flow CLI

## macOS[​](#macos-1 "Direct link to macOS")

### Homebrew[​](#homebrew-1 "Direct link to Homebrew")

`_10

brew upgrade flow-cli`

### From a pre-built binary[​](#from-a-pre-built-binary-3 "Direct link to From a pre-built binary")

*This update method only works on x86-64.*

This script downloads and updates the appropriate binary for your system:

`_10

sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

## Linux[​](#linux-1 "Direct link to Linux")

### From a pre-built binary[​](#from-a-pre-built-binary-4 "Direct link to From a pre-built binary")

*This update method only works on x86-64.*

This script downloads and updates the appropriate binary for your system:

`_10

sudo sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

## Windows[​](#windows-1 "Direct link to Windows")

### From a pre-built binary[​](#from-a-pre-built-binary-5 "Direct link to From a pre-built binary")

*This update method only works on Windows 10, 8.1, or 7 (SP1, with [PowerShell 3.0](https://www.microsoft.com/en-ca/download/details.aspx?id=34595)), on x86-64.*

1. Open PowerShell ([Instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell?view=powershell-7#finding-powershell-in-windows-10-81-80-and-7))
2. In PowerShell, run:

   `_10

   iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"`

## Uninstalling Flow CLI[​](#uninstalling-flow-cli "Direct link to Uninstalling Flow CLI")

To remove the flow CLI you can run the following command if it was previously installed using a pre-built binary.

* macOS: `rm /usr/local/bin/flow`
* Linux: `rm ~/.local/bin/flow`
* Windows: `rm ~/Users/{user}/AppData/Flow/flow.exe`

If you installed it using Hombrew you can remove it using: `brew uninstall flow-cli`.

## Next Steps[​](#next-steps "Direct link to Next Steps")

Now that you have the Flow CLI installed, you can:

* **[Get started with Flow CLI commands](/build/tools/flow-cli/super-commands)** - Learn the essential commands for project development
* **[Initialize a new project](/build/tools/flow-cli/flow.json/initialize-configuration)** - Create your first Flow project
* **[Configure your project](/build/tools/flow-cli/flow.json/configuration)** - Set up your `flow.json` configuration file

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/flow-cli/install.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Flow CLI](/build/tools/flow-cli)[Next

Commands Overview](/build/tools/flow-cli/super-commands)

###### Rate this page

😞😐😊

Copy as Markdown

* [macOS](#macos)
  + [Homebrew](#homebrew)
  + [From a pre-built binary](#from-a-pre-built-binary)
* [Linux](#linux)
  + [From a pre-built binary](#from-a-pre-built-binary-1)
  + [Install a specific version](#install-a-specific-version)
* [Windows](#windows)
  + [From a pre-built binary](#from-a-pre-built-binary-2)
* [macOS](#macos-1)
  + [Homebrew](#homebrew-1)
  + [From a pre-built binary](#from-a-pre-built-binary-3)
* [Linux](#linux-1)
  + [From a pre-built binary](#from-a-pre-built-binary-4)
* [Windows](#windows-1)
  + [From a pre-built binary](#from-a-pre-built-binary-5)
* [Uninstalling Flow CLI](#uninstalling-flow-cli)
* [Next Steps](#next-steps)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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
* [EVM](/build/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.