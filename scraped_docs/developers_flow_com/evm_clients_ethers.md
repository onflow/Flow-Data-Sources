# Source: https://developers.flow.com/evm/clients/ethers

Ethers.js on Flow Blockchain | Flow Developer Portal



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
* [Clients](/evm/clients/ethers)

  + [Ethers](/evm/clients/ethers)
  + [Web3.js](/evm/clients/web3-js)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)

* Clients
* Ethers

On this page

# Ethers.js

[ethers.js](https://docs.ethers.org/v5/) is a powerful JavaScript library for interacting with Ethereum and other EVM-compatible blockchain networks.

In this guide, we'll walk you through how to use ethers.js to interact with smart contracts on the Flow Blockchain.

---

## Installation[​](#installation "Direct link to Installation")

To begin using ethers.js in your project, you'll need to install the package. You can do this by running the following command:

`_10

bashCopy code

_10

npm install --save ethers`

## Setup[​](#setup "Direct link to Setup")

After installing ethers.js, the next step is to import it into your project.

You can do this by adding the following line of code at the beginning of your JavaScript file:

`_10

const ethers = require('ethers');`

## Connecting to Flow[​](#connecting-to-flow "Direct link to Connecting to Flow")

To connect to the Flow Blockchain using ethers.js, you need to create a new `JsonRpcProvider` instance with the appropriate RPC URL for Flow:

`_10

const ethers = require('ethers');

_10

_10

const url = 'https://testnet.evm.nodes.onflow.org/';

_10

const provider = new ethers.providers.JsonRpcProvider(url);`

**Note:** If you want to connect to the Flow testnet, replace the above URL with `https://mainnet.evm.nodes.onflow.org`.

## Reading Data from the Blockchain[​](#reading-data-from-the-blockchain "Direct link to Reading Data from the Blockchain")

Once your provider is set up, you can start reading data from the Flow Blockchain. For instance, to retrieve the latest block number, you can use the `getBlockNumber` method:

`_10

async function getLatestBlock() {

_10

const latestBlock = await provider.getBlockNumber();

_10

console.log(latestBlock);

_10

}`

## Writing Data to the Blockchain[​](#writing-data-to-the-blockchain "Direct link to Writing Data to the Blockchain")

To send transactions or write data to the Flow Blockchain, you need to create a `Signer`. This can be done by initializing a new `Wallet` object with your private key and the previously created `Provider`:

`_10

const privateKey = 'YOUR_PRIVATE_KEY';

_10

const signer = new ethers.Wallet(privateKey, provider);`

**Note:** Replace `'YOUR_PRIVATE_KEY'` with the actual private key of the wallet you want to use.

## Interacting with Smart Contracts[​](#interacting-with-smart-contracts "Direct link to Interacting with Smart Contracts")

ethers.js also enables interaction with smart contracts on the Flow Blockchain. To do this, create a `Contract` object using the ABI (Application Binary Interface) and the address of the deployed contract:

`_10

const abi = [

_10

// ABI of deployed contract

_10

];

_10

_10

const contractAddress = 'CONTRACT_ADDRESS';

_10

_10

// read-only contract instance

_10

const contract = new ethers.Contract(contractAddress, abi, provider);`

For contracts that require writing, you'll need to provide a `Signer` object instead of a `Provider`:

`_10

// write-enabled contract instance

_10

const contract = new ethers.Contract(contractAddress, abi, signer);`

**Note:** Replace `'CONTRACT_ADDRESS'` with the actual address of your deployed contract.

After setting up your `Contract` object, you can call methods on the smart contract as needed:

`_10

async function setValue(value) {

_10

const tx = await contract.set(value);

_10

console.log(tx.hash);

_10

}

_10

_10

async function getValue() {

_10

const value = await contract.get();

_10

console.log(value.toString());

_10

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/clients/ethers.md)

Last updated on **Feb 27, 2025** by **Vishal**

[Previous

VRF (Randomness) in Solidity](/evm/guides/vrf)[Next

Web3.js](/evm/clients/web3-js)

###### Rate this page

😞😐😊

* [Installation](#installation)
* [Setup](#setup)
* [Connecting to Flow](#connecting-to-flow)
* [Reading Data from the Blockchain](#reading-data-from-the-blockchain)
* [Writing Data to the Blockchain](#writing-data-to-the-blockchain)
* [Interacting with Smart Contracts](#interacting-with-smart-contracts)

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