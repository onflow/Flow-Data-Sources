# Source: https://developers.flow.com/build/evm/using

EVM Wallet Setup | Flow Developer Portal



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

* Solidity (EVM)
* EVM Wallet Setup

On this page

# EVM Wallet Setup

## Flow Native Wallet[​](#flow-native-wallet "Direct link to Flow Native Wallet")

The [Flow Wallet](https://wallet.flow.com) is the preferred wallet for Flow EVM. It's also compatible with Cadence transactions, and it currently sponsors all transactions on testnet and mainnet!

Flow Wallet is available on [Android](https://play.google.com/store/apps/details?id=com.flowfoundation.wallet) and [iOS](https://apps.apple.com/ca/app/flow-wallet-nfts-and-crypto/id6478996750), with desktop support using the Flow Wallet [Chrome extension](https://chromewebstore.google.com/detail/flow-reference-wallet/hpclkefagolihohboafpheddmmgdffjm). In addition to being able to transact in both EVM and Cadence environments, Flow Wallet will also allow you to view and move assets between EVM and Cadence, making it possible to manage all your assets in one place.

To use the Flow Wallet Chrome extension:

1. Open the Flow Wallet browser extension and create your account.
2. Connect to an app using Flow Wallet.

## Other EVM Wallets[​](#other-evm-wallets "Direct link to Other EVM Wallets")

Applications deployed to Flow EVM will work with popular EVM-compatible wallets such as [MetaMask](https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn), all you need to do is add the correct [RPC endpoint](/build/evm/networks) as a custom network.

### Add Flow to Browser Wallets[​](#add-flow-to-browser-wallets "Direct link to Add Flow to Browser Wallets")

### Add Manually to MetaMask[​](#add-manually-to-metamask "Direct link to Add Manually to MetaMask")

Manual method: Add Flow EVM as a custom network to MetaMask:

1. Open the MetaMask browser extension
2. Open the network selection dropdown menu by clicking the dropdown button at the top of the extension
3. Click the **`Add network`** button
4. Click **`Add a network manually`**
5. In the **`Add a network manually`** dialog that appears, enter the following information:

| Name | Value |
| --- | --- |
| Network Name | Flow EVM Mainnet |
| Description | The public RPC url for Flow Mainnet |
| RPC Endpoint | <https://mainnet.evm.nodes.onflow.org> |
| Chain ID | 747 |
| Currency Symbol | FLOW |
| Block Explorer | <https://evm.flowscan.io/> |

6. Tap the Save button to save Flow EVM as a network.

You should now be able to connect to the Flow EVM by selecting it from the network selection dropdown menu.

To additionally add the Flow EVM Testnet to MetaMask, follow the same steps as above, but use the following information:

| Name | Value |
| --- | --- |
| Network Name | Flow EVM Testnet |
| Description | The public RPC url for Flow Testnet |
| RPC Endpoint | <https://testnet.evm.nodes.onflow.org> |
| Chain ID | 545 |
| Currency Symbol | FLOW |
| Block Explorer | <https://evm-testnet.flowscan.io> |

Use the [Flow Testnet Faucet](https://faucet.flow.com/fund-account) to fund your account for testing.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/evm/using.mdx)

Last updated on **Sep 24, 2025** by **Brian Doyle**

[Previous

How it Works](/build/evm/how-it-works)[Next

Network Information](/build/evm/networks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Flow Native Wallet](#flow-native-wallet)
* [Other EVM Wallets](#other-evm-wallets)
  + [Add Flow to Browser Wallets](#add-flow-to-browser-wallets)
  + [Add Manually to MetaMask](#add-manually-to-metamask)

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