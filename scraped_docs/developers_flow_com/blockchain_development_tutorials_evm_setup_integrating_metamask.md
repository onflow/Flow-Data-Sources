# Source: https://developers.flow.com/blockchain-development-tutorials/evm/setup/integrating-metamask

Integrating Metamask | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            + [Flow EVM Setup](/blockchain-development-tutorials/evm/setup)

              - [Integrating Metamask](/blockchain-development-tutorials/evm/setup/integrating-metamask)+ [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)

                + [Flow EVM Development Tools](/blockchain-development-tutorials/evm/development-tools)

                  + [Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/evm/image-gallery)* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Flow EVM Guides](/blockchain-development-tutorials/evm)* [Flow EVM Setup](/blockchain-development-tutorials/evm/setup)* Integrating Metamask

On this page

# Wallets & Configurations

This document shows how to integrate the Flow Network programmatically with your app via MetaMask.

If you want to add it to your wallet now, click the buttons below, or follow the [manual process](/build/evm/using).

## Metamask[​](#metamask "Direct link to Metamask")

To integrate additional networks into MetaMask can pose challenges for users who lack technical expertise and may lead to errors. If you simplify this process, you can greatly enhance user onboarding for your application. This guide demonstrates how to create a straightforward button within your frontend application to streamline the addition of the Flow network to MetaMask.

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

### Add Flow network[​](#add-flow-network "Direct link to Add Flow network")

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

If you use this approach to add the Flow network to Metamask, you can avoid manual user data entry and ensure that users are ready to interact with your dApp!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/evm/setup/integrating-metamask.mdx)

Last updated on **Nov 12, 2025** by **Brian Doyle**

[Previous

Flow EVM Setup](/blockchain-development-tutorials/evm/setup)[Next

Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)

###### Rate this page

😞😐😊

Copy as Markdown

* [Metamask](#metamask)
  + [EIP-3035 & MetaMask](#eip-3035--metamask)+ [Flow Network configuration](#flow-network-configuration)+ [Add Flow network](#add-flow-network)+ [User Experience](#user-experience)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.