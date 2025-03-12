# Source: https://developers.flow.com/evm/guides/integrating-metamask

Integrating Metamask | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Networks](/evm/networks)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
* [Data Indexers](/evm/data-indexers)
* [Faucets ↙](/evm/faucets)
* [Block Explorers ↙](/evm/block-explorers)
* [Guides](/evm/guides/integrating-metamask)

  + [Integrating Metamask](/evm/guides/integrating-metamask)
  + [Hardhat](/evm/guides/hardhat)
  + [Remix](/evm/guides/remix)
  + [Rainbowkit](/evm/guides/rainbowkit)
  + [Viem & Wagmi](/evm/guides/wagmi)
  + [Foundry](/evm/guides/foundry)
  + [VRF (Randomness) in Solidity](/evm/guides/vrf)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)

* Guides
* Integrating Metamask

On this page

# Wallets & Configurations

This document shows how to integrate the Flow Network programmatically with your Dapp via MetaMask.

If you want to add it to your wallet now, you can click the buttons below, or follow the [manual process](/evm/using).

## Metamask[​](#metamask "Direct link to Metamask")

Integrating additional networks into MetaMask can pose challenges for users who lack technical expertise and may lead to errors. Simplifying this process can greatly enhance user onboarding for your application. This guide demonstrates how to create a straightforward button within your frontend application to streamline the addition of the Flow network to MetaMask.

### EIP-3035 & MetaMask[​](#eip-3035--metamask "Direct link to EIP-3035 & MetaMask")

[EIP-3035](https://eips.ethereum.org/EIPS/eip-3085) is an Ethereum Improvement Proposal that defines an RPC method for adding Ethereum-compatible chains to wallet applications. Since March 2021 MetaMask has implemented that EIP as part of their MetaMask [Custom Networks API](https://consensys.io/blog/connect-users-to-layer-2-networks-with-the-metamask-custom-networks-api).

### Flow Network configuration[​](#flow-network-configuration "Direct link to Flow Network configuration")

To add the Flow Testnet network to Metamask, add the following network confgiuration:

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/guides/integrating-metamask.mdx)

Last updated on **Feb 27, 2025** by **Chase Fleming**

[Previous

Block Explorers ↙](/evm/block-explorers)[Next

Hardhat](/evm/guides/hardhat)

###### Rate this page

😞😐😊

* [Metamask](#metamask)
  + [EIP-3035 & MetaMask](#eip-3035--metamask)
  + [Flow Network configuration](#flow-network-configuration)
  + [Adding Flow Network](#adding-flow-network)
  + [User Experience](#user-experience)

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