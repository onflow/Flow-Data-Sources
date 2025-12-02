# Source: https://developers.flow.com/blockchain-development-tutorials/evm/frameworks/web3-js

Web3.js on Flow Blockchain | Flow Developer Portal



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

              + [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)

                - [Ethers](/blockchain-development-tutorials/evm/frameworks/ethers)- [Web3.js](/blockchain-development-tutorials/evm/frameworks/web3-js)- [Viem & Wagmi](/blockchain-development-tutorials/evm/frameworks/wagmi)- [Rainbowkit](/blockchain-development-tutorials/evm/frameworks/rainbowkit)+ [Flow EVM Development Tools](/blockchain-development-tutorials/evm/development-tools)

                  + [Build a Fully-Onchain Image Gallery](/blockchain-development-tutorials/evm/image-gallery)* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Flow EVM Guides](/blockchain-development-tutorials/evm)* [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)* Web3.js

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

## Initialize Web3 with Flow[​](#initialize-web3-with-flow "Direct link to Initialize Web3 with Flow")

To use `web3` in your project, first import the module and initialize your `Web3` instance with a Flow RPC endpoint.

`_10

const { Web3 } = require('web3');

_10

const web3 = new Web3('https://testnet.evm.nodes.onflow.org');`

**Note:** If you want to connect to the Flow testnet, replace the above URL with `https://mainnet.evm.nodes.onflow.org`.

## Query The blockchain[​](#query-the-blockchain "Direct link to Query The blockchain")

`web3` provides a number of methods for how to query the blockchain, such as to retrieve the latest block number, query account balances, and more.

You can try with some of these methods to verify that your `web3` instance works correctly.

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

For more information about other queries you can make `web3`, see the [Web3.js](https://web3js.org/) official documentation.

## Interact with smart contracts[​](#interact-with-smart-contracts "Direct link to Interact with smart contracts")

The `web3` library allows developers to interact with smart contracts via the `web3.eth.Contract` API.

For this example we will use the following `Storage` contract.

We recommend that you deploy your own contract, which you can do with [Hardhat] or [Remix].

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

You can generate the ABI for this contract with the [`solc` compiler](https://docs.soliditylang.org/en/latest/installing-solidity.html), or another tool such as [Hardhat]or [Remix].

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

We can now interact with the contract on the network ith the `contract` object.

### Read state[​](#read-state "Direct link to Read state")

State can be read from the contract via the `call` function with one of the contract's methods. This will not change the state and will not send a transaction.

`` _10

// Retrieve the current value stored in the contract

_10

// (this is using the `retrieve` method from the contract with no arguments)

_10

const result = await contract.methods.retrieve().call();

_10

_10

console.log(result); // Current value stored in the contract ``

### Change state[​](#change-state "Direct link to Change state")

To mutate the state of the contract, we can send a transaction to the network.

In order to send a transaction to the network, you will need an account with sufficient funds to pay for the transaction.

info

If you do not have an account yet, you can create one with the following command from your project's root directory:

`_10

node -e "console.log(require('web3').eth.accounts.create())"`

This is not a secure way to generate an account, and you should use a more secure method in a production environment.

You can fund your account with the [Flow Faucet](https://faucet.flow.com/fund-account).

We can use the `privateKeyToAccount` function to create an `Web3Account` object from our account's private key.

`_10

// You must replace this with the private key of the account you wish to use

_10

const account = web3.eth.accounts.privateKeyToAccount('0x1234');`

Then, we can sign a transaction with the user's account and send it to the network.

`` _18

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

console.log(result); ``

Now that the transaction was sent, the contract's state was updated. To verify this, we can query the contract's state again:

`_10

const result = await contract.methods.retrieve().call();

_10

console.log(result); // New value stored in the contract`

For more information about how to use smart contracts in web3.js, see the [official documentation].

[Hardhat]: ../development-tools/hardhat.md)
[Remix]: ../development-tools/remix.md).
[official documentation]: <https://docs.web3js.org/libdocs/Contract>

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/evm/frameworks/web3-js.md)

Last updated on **Nov 19, 2025** by **cshannon1218**

[Previous

Ethers](/blockchain-development-tutorials/evm/frameworks/ethers)[Next

Viem & Wagmi](/blockchain-development-tutorials/evm/frameworks/wagmi)

###### Rate this page

😞😐😊

Copy as Markdown

* [Prerequisites](#prerequisites)* [Initialize Web3 with Flow](#initialize-web3-with-flow)* [Query The blockchain](#query-the-blockchain)* [Interact with smart contracts](#interact-with-smart-contracts)
        + [Read state](#read-state)+ [Change state](#change-state)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.