# Source: https://developers.flow.com/evm/clients/web3-js

Web3.js on Flow Blockchain | Flow Developer Portal



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
* Web3.js

On this page

# Web3.js

[Web3.js](https://web3js.org/) is a Javascript library for building on EVM-compatible networks.

It allows developers to interact with smart contracts, send transactions, and retrieve data from the network.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

info

This guide assumes you have the latest version of [Node.js](https://nodejs.org/en) installed.

To install `web3` in your project, run the following command:

`_10

npm install web3`

## Initializing Web3 with Flow[​](#initializing-web3-with-flow "Direct link to Initializing Web3 with Flow")

To use `web3` in your project, start by importing the module and initializing your `Web3` instance with a Flow RPC endpoint.

`_10

const { Web3 } = require('web3');

_10

const web3 = new Web3('https://testnet.evm.nodes.onflow.org');`

**Note:** If you want to connect to the Flow testnet, replace the above URL with `https://mainnet.evm.nodes.onflow.org`.

## Querying The Blockchain[​](#querying-the-blockchain "Direct link to Querying The Blockchain")

`web3` provides a number of methods for querying the blockchain, such as getting the latest block number, querying account balances, and more.

You can try using some of these methods to verify that your `web3` instance is working correctly.

`_15

// Get the latest block number

_15

const blockNumber = await web3.eth.getBlockNumber();

_15

console.log(blockNumber); // Latest block number

_15

_15

// Get the balance of an account

_15

const balance = await web3.eth.getBalance('0x1234'); // Replace with any address

_15

console.log(balance); // Balance in attoFlow

_15

_15

// Get the chain ID

_15

const chainId = await web3.eth.getChainId();

_15

console.log(chainId);

_15

_15

// Get the gas price

_15

const gasPrice = await web3.eth.getGasPrice();

_15

console.log(gasPrice); // Gas price in attoFlow`

For more information about other queries you can make `web3`, please see the [official documentation](https://docs.web3js.org/).

## Interacting with Smart Contracts[​](#interacting-with-smart-contracts "Direct link to Interacting with Smart Contracts")

The `web3` library allows developers to interact with smart contracts via the `web3.eth.Contract` API.

For this example we will use the following `Storage` contract.

We recommend deploying your own contract, which can be done using [Hardhat](/evm/guides/hardhat) or [Remix](/evm/guides/remix).

`_14

// SPDX-License-Identifier: MIT

_14

pragma solidity ^0.8.0;

_14

_14

contract Storage {

_14

uint256 public storedData;

_14

_14

function store(uint256 x) public {

_14

storedData = x;

_14

}

_14

_14

function retrieve() public view returns (uint256) {

_14

return storedData;

_14

}

_14

}`

The ABI for this contract can be generated using the [`solc` compiler](https://docs.soliditylang.org/en/latest/installing-solidity.html), or another tool such as [Hardhat](/evm/guides/hardhat) or [Remix](/evm/guides/remix).

Now that we have both the ABI and address of the contract, we can create a new `Contract` object for use in our application.

`_40

// Replace with the ABI of the deployed contract

_40

const abi = [

_40

{

_40

inputs: [],

_40

stateMutability: 'nonpayable',

_40

type: 'constructor',

_40

},

_40

{

_40

inputs: [

_40

{

_40

internalType: 'uint256',

_40

name: 'x',

_40

type: 'uint256',

_40

},

_40

],

_40

name: 'store',

_40

outputs: [],

_40

stateMutability: 'nonpayable',

_40

type: 'function',

_40

},

_40

{

_40

inputs: [],

_40

name: 'retrieve',

_40

outputs: [

_40

{

_40

internalType: 'uint256',

_40

name: '',

_40

type: 'uint256',

_40

},

_40

],

_40

stateMutability: 'view',

_40

type: 'function',

_40

},

_40

];

_40

_40

// Replace with the address of the deployed contract

_40

const contractAddress = '0x4c7784ae96e7cfcf0224a95059573e96f03a4e70';

_40

_40

// Create a new contract object with the ABI and address

_40

const contract = new web3.eth.Contract(abi, contractAddress);`

We can now interact with the contract on the network by using the `contract` object.

### Reading State[​](#reading-state "Direct link to Reading State")

State can be read from the contract by using the `call` function with one of the contract's methods. This will not change the state and will not send a transaction.

`_10

// Retrieve the current value stored in the contract

_10

// (this is using the `retrieve` method from the contract with no arguments)

_10

const result = await contract.methods.retrieve().call();

_10

_10

console.log(result); // Current value stored in the contract`

### Changing State[​](#changing-state "Direct link to Changing State")

We can mutate the state of the contract by sending a transaction to the network.

In order to send a transaction to the network, you will need an account with sufficient funds to pay for the transaction.

info

If you do not have an account yet, you can create one using the following command from your project's root directory:

`_10

node -e "console.log(require('web3').eth.accounts.create())"`

Note that this is not a secure way to generate an account, and you should use a more secure method in a production environment.

You can fund your account using the [Flow Faucet](https://faucet.flow.com/fund-account).

We can use the `privateKeyToAccount` function to create an `Web3Account` object from our account's private key.

`_10

// You must replace this with the private key of the account you wish to use

_10

const account = web3.eth.accounts.privateKeyToAccount('0x1234');`

Then, we can sign a transaction using the user's account and send it to the network.

`_18

const newValue = 1337; // Replace with any value you want to store

_18

_18

// Sign a transaction that stores a new value in the contract

_18

// (this is using the `store` method from the contract with the new value as an argument)

_18

let signed = await account.signTransaction({

_18

from: account.address,

_18

to: contractAddress,

_18

data: contract.methods.store(newValue).encodeABI(),

_18

gas: 10000000n, // Replace with the gas limit you want to use

_18

gasPrice: await web3.eth.getGasPrice(), // Replace with the gas price you want to use

_18

});

_18

_18

// Send signed transaction to the network

_18

const result = await web3.eth.sendSignedTransaction(signed.rawTransaction);

_18

_18

// { status: 1, transactionHash: '0x1234', ... }

_18

// status=1 means the transaction was successful

_18

console.log(result);`

Now that the transaction has been sent, the contract's state should have been updated. We can verify this by querying the contract's state again:

`_10

const result = await contract.methods.retrieve().call();

_10

console.log(result); // New value stored in the contract`

For more information about using smart contracts in web3.js, see the [official documentation](https://docs.web3js.org/libdocs/Contract).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/clients/web3-js.md)

Last updated on **Feb 22, 2025** by **Brian Doyle**

[Previous

Ethers](/evm/clients/ethers)[Next

Interacting with COAs](/evm/cadence/interacting-with-coa)

###### Rate this page

😞😐😊

* [Prerequisites](#prerequisites)
* [Initializing Web3 with Flow](#initializing-web3-with-flow)
* [Querying The Blockchain](#querying-the-blockchain)
* [Interacting with Smart Contracts](#interacting-with-smart-contracts)
  + [Reading State](#reading-state)
  + [Changing State](#changing-state)

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