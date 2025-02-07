# Source: https://developers.flow.com/tools/flow-cli/install




Install Instructions | Flow Developer Portal





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
* Install Instructions
On this page
# Install Instructions

The Flow CLI can be installed on macOS, Windows (7 or greater) and most Linux systems.

> Note: If you need to install the pre-release version of the Flow CLI supporting Cadence 1.0, please refer to the [Cadence 1.0 migration guide instructions](https://cadence-lang.org/docs/cadence-migration-guide#install-cadence-10-cli).

## macOS[​](#macos "Direct link to macOS")

### Homebrew[​](#homebrew "Direct link to Homebrew")

 `_10brew install flow-cli`
### From a pre-built binary[​](#from-a-pre-built-binary "Direct link to From a pre-built binary")

*This installation method only works on x86-64.*

This script downloads and installs the appropriate binary for your system:

 `_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

To update, simply re-run the installation command above.

It is currently not possible to install earlier versions of the Flow CLI with Homebrew.

## Linux[​](#linux "Direct link to Linux")

### From a pre-built binary[​](#from-a-pre-built-binary-1 "Direct link to From a pre-built binary")

*This installation method only works on x86-64.*

This script downloads and installs the appropriate binary for your system:

 `_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`

To update, simply re-run the installation command above.

### Install a specific version[​](#install-a-specific-version "Direct link to Install a specific version")

To install a specific version of Flow CLI newer than v0.42.0, append the version tag to the command (e.g. the command below installs CLI version v0.44.0).

 `_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)" -- v0.44.0`

To install a version older than v0.42.0, refer to [Installing versions before 0.42.0](#installing-versions-before-0420) below.

## Windows[​](#windows "Direct link to Windows")

### From a pre-built binary[​](#from-a-pre-built-binary-2 "Direct link to From a pre-built binary")

*This installation method only works on Windows 10, 8.1, or 7 (SP1, with [PowerShell 3.0](https://www.microsoft.com/en-ca/download/details.aspx?id=34595)), on x86-64.*

1. Open PowerShell ([Instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell?view=powershell-7#finding-powershell-in-windows-10-81-80-and-7))
2. In PowerShell, run:
   
    `_10iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"`

To update, simply re-run the installation command above.

# Upgrade the Flow CLI

## macOS[​](#macos-1 "Direct link to macOS")

### Homebrew[​](#homebrew-1 "Direct link to Homebrew")

 `_10brew upgrade flow-cli`
### From a pre-built binary[​](#from-a-pre-built-binary-3 "Direct link to From a pre-built binary")

*This update method only works on x86-64.*

This script downloads and updates the appropriate binary for your system:

 `_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`
## Linux[​](#linux-1 "Direct link to Linux")

### From a pre-built binary[​](#from-a-pre-built-binary-4 "Direct link to From a pre-built binary")

*This update method only works on x86-64.*

This script downloads and updates the appropriate binary for your system:

 `_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"`
## Windows[​](#windows-1 "Direct link to Windows")

### From a pre-built binary[​](#from-a-pre-built-binary-5 "Direct link to From a pre-built binary")

*This update method only works on Windows 10, 8.1, or 7 (SP1, with [PowerShell 3.0](https://www.microsoft.com/en-ca/download/details.aspx?id=34595)), on x86-64.*

1. Open PowerShell ([Instructions](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-windows-powershell?view=powershell-7#finding-powershell-in-windows-10-81-80-and-7))
2. In PowerShell, run:
   
    `_10iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"`

# Uninstalling Flow CLI

To remove the flow CLI you can run the following command if it was previously installed using a pre-built binary.

* macOS: `rm /usr/local/bin/flow`
* Linux: `rm ~/.local/bin/flow`
* Windows: `rm ~/Users/{user}/AppData/Flow/flow.exe`

If you installed it using Hombrew you can remove it using: `brew uninstall flow-cli`.

## Installing versions before 0.42.0[​](#installing-versions-before-0420 "Direct link to Installing versions before 0.42.0")

If you want to install versions before v0.42.0 you have to use a different install command.

**Linux/macOS**

 `_10https://raw.githubusercontent.com/onflow/flow-cli/v0.41.3/install.ps1_10_10sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/v0.41.3/install.sh)" -- v0.41.2`

**Windows**

 `_10iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"`[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/flow-cli/install.md)Last updated on **Jan 23, 2025** by **Brian Doyle**[PreviousFlow CLI](/tools/flow-cli)[NextSuper Commands](/tools/flow-cli/super-commands)
###### Rate this page

😞😐😊

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
* [Installing versions before 0.42.0](#installing-versions-before-0420)
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

