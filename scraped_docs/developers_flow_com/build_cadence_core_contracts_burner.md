# Source: https://developers.flow.com/build/cadence/core-contracts/burner

Flow Burner Contract Address | Flow Developer Portal



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

    - [Fungible Token](/build/cadence/core-contracts/fungible-token)
    - [Flow Token](/build/cadence/core-contracts/flow-token)
    - [Service Account](/build/cadence/core-contracts/service-account)
    - [Flow Fees](/build/cadence/core-contracts/flow-fees)
    - [Staking Table](/build/cadence/core-contracts/staking-contract-reference)
    - [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)
    - [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)
    - [NFT Metadata](/build/cadence/core-contracts/nft-metadata)
    - [NFT Storefront](/build/cadence/core-contracts/nft-storefront)
    - [Staking Collection](/build/cadence/core-contracts/staking-collection)
    - [Account Linking](/build/cadence/core-contracts/hybrid-custody)
    - [EVM](/build/cadence/core-contracts/evm)
    - [Burner](/build/cadence/core-contracts/burner)
    - [VM Bridge](/build/cadence/core-contracts/bridge)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [EVM Wallet Setup](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
* [Tools & SDKs](/build/tools)

* Cadence
* [Core Smart Contracts](/build/cadence/core-contracts)
* Burner

# Contract

The [Burner](https://github.com/onflow/flow-ft/blob/master/contracts/utility/Burner.cdc) contract provides a way for resources to define
custom logic that is executed when the resource is destroyed.
Resources that want to utilize this functionality should implement
the `Burner.Burnable` interface which requires that they include
a `burnCallback()` function that includes the custom logic.

It is recommended that regardless of the resource, all users and developers
should use `Burner.burn()` when destroying a resource instead of `destroy`.

| Network | Contract Address |
| --- | --- |
| Cadence Testing Framework | `0x0000000000000001` |
| Emulator | `0xee82856bf20e2aa6` |
| Testnet | [`0x294e44e1ec6993c6`](https://contractbrowser.com/account/0x294e44e1ec6993c6) |
| Mainnet | [`0xd8a7e05a7ac670c0`](https://contractbrowser.com/account/0xd8a7e05a7ac670c0) |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/14-burner.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

EVM](/build/cadence/core-contracts/evm)[Next

VM Bridge](/build/cadence/core-contracts/bridge)

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