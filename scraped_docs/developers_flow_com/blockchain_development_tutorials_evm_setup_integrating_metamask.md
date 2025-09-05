# Source: https://developers.flow.com/blockchain-development-tutorials/evm/setup/integrating-metamask

Integrating Metamask | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)

  + [Flow EVM Setup](/blockchain-development-tutorials/evm/setup)

    - [Integrating Metamask](/blockchain-development-tutorials/evm/setup/integrating-metamask)
  + [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)
  + [Flow EVM Development Tools](/blockchain-development-tutorials/evm/development-tools)
  + [Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/evm/image-gallery)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Flow EVM Setup](/blockchain-development-tutorials/evm/setup)
* Integrating Metamask

On this page

# Wallets & Configurations

This document shows how to integrate the Flow Network programmatically with your Dapp via MetaMask.

If you want to add it to your wallet now, you can click the buttons below, or follow the [manual process](/build/evm/using).

## Metamask[​](#metamask "Direct link to Metamask")

Integrating additional networks into MetaMask can pose challenges for users who lack technical expertise and may lead to errors. Simplifying this process can greatly enhance user onboarding for your application. This guide demonstrates how to create a straightforward button within your frontend application to streamline the addition of the Flow network to MetaMask.

### EIP-3035 & MetaMask[​](#eip-3035--metamask "Direct link to EIP-3035 & MetaMask")

[EIP-3035](https://eips.ethereum.org/EIPS/eip-3085) is an Ethereum Improvement Proposal that defines an RPC method for adding Ethereum-compatible chains to wallet applications. Since March 2021 MetaMask has implemented that EIP as part of their MetaMask [Custom Networks API](https://consensys.io/blog/connect-users-to-layer-2-networks-with-the-metamask-custom-networks-api).

### Flow Network configuration[​](#flow-network-configuration "Direct link to Flow Network configuration")

To add the Flow Testnet network to Metamask, add the following network configuration:

`_11

export const TESTNET_PARAMS = {

_11

chainId: '0x221',

_11

chainName: 'Flow',

_11

rpcUrls: ['https://testnet.evm.nodes.onflow.org'],

_11

nativeCurrency: {

_11

name: 'Flow',

_11

symbol: 'FLOW',

_11

decimals: 18,

_11

},

_11

blockExplorerUrls: ['https://evm-testnet.flowscan.io/']

_11

};`

### Adding Flow Network[​](#adding-flow-network "Direct link to Adding Flow Network")

To add this configuration to MetaMask, call the `wallet_addEthereumChain` method which is exposed by the web3 provider.

`_12

function addFlowTestnet() {

_12

injected.getProvider().then((provider) => {

_12

provider

_12

.request({

_12

method: 'wallet_addEthereumChain',

_12

params: [TESTNET_PARAMS],

_12

})

_12

.catch((error: any) => {

_12

console.log(error);

_12

});

_12

});

_12

}`

The variable, `injected`, is initialized as a `web3-react/injected-connector` used to interface with MetaMask APIs. Usage for other popular web frameworks is similar.

The typical usage would be to expose this button if you get errors when attempting to connect to MetaMask (i.e. `Wrong Network` or `Error Connecting`).

### User Experience[​](#user-experience "Direct link to User Experience")

Users of your app will need to first approve a connection to Metamask. After doing this, if you don't detect a successful Web3 network connection, you may present a dialog asking them to add the Flow network to their wallet.

![Metamask Network](/assets/images/metamask-network-333fcb5893290b25f7a8d706672cebf1.png)

After they approve, your app will be connected to the Flow network.

By using this approach to add the Flow network to Metamask, you can avoid manual user data entry and ensure that users are ready to interact with your dApp!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/evm/setup/integrating-metamask.mdx)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Flow EVM Setup](/blockchain-development-tutorials/evm/setup)[Next

Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Metamask](#metamask)
  + [EIP-3035 & MetaMask](#eip-3035--metamask)
  + [Flow Network configuration](#flow-network-configuration)
  + [Adding Flow Network](#adding-flow-network)
  + [User Experience](#user-experience)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
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