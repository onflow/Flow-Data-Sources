# Source: https://developers.flow.com/build/evm/guides/remix

Flow Remix Guide | Flow Developer Portal



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

    - [Integrating Metamask](/build/evm/guides/integrating-metamask)
    - [Hardhat](/build/evm/guides/hardhat)
    - [Remix](/build/evm/guides/remix)
    - [Rainbowkit](/build/evm/guides/rainbowkit)
    - [Viem & Wagmi](/build/evm/guides/wagmi)
    - [Foundry](/build/evm/guides/foundry)
    - [Ethers](/build/evm/guides/ethers)
    - [Web3.js](/build/evm/guides/web3-js)
* [Tools & SDKs](/build/tools)

* Solidity (EVM)
* [Guides](/build/evm/guides)
* Remix

On this page

# Using Remix

Remix is an open-source, web-based development environment tailored for EVM smart contract development. It offers developers a comprehensive suite of tools for writing, deploying, and testing smart contracts in Solidity. For more information, visit [Remix](https://remix.ethereum.org/).

## Add the Flow Network to MetaMask[​](#add-the-flow-network-to-metamask "Direct link to Add the Flow Network to MetaMask")

![Add Flow Network](/assets/images/Remix-adding-metamask-network-4912936e5dad423a4d858266eb9648a7.gif)

Navigate to the [Using EVM](/build/evm/using) page to find the button to add the Flow network information to your metamask.

## Fund Your Flow Account[​](#fund-your-flow-account "Direct link to Fund Your Flow Account")

Navigate to the [Flow Testnet Faucet](https://faucet.flow.com/fund-account) to obtain FLOW tokens necessary for deploying a smart contract.

## Deploying a Smart Contract Using Remix[​](#deploying-a-smart-contract-using-remix "Direct link to Deploying a Smart Contract Using Remix")

![Deploy Smart Contract](/assets/images/Remix-deploy-contract-flowevm-041b338f872e80325bd497587cfe7e42.gif)

### HelloWorld Smart Contract[​](#helloworld-smart-contract "Direct link to HelloWorld Smart Contract")

`_25

// SPDX-License-Identifier: MIT

_25

pragma solidity ^0.8.0;

_25

_25

contract HelloWorld {

_25

// Declare a public field of type string.

_25

string public greeting;

_25

_25

// Constructor to initialize the greeting.

_25

// In Solidity, the constructor is defined with the "constructor" keyword.

_25

constructor() {

_25

greeting = "Hello, World!";

_25

}

_25

_25

// Public function to change the greeting.

_25

// The "public" keyword makes the function accessible from outside the contract.

_25

function changeGreeting(string memory newGreeting) public {

_25

greeting = newGreeting;

_25

}

_25

_25

// Public function that returns the greeting.

_25

// In Solidity, explicit return types are declared.

_25

function hello() public view returns (string memory) {

_25

return greeting;

_25

}

_25

}`

### Steps to Deploy the HelloWorld Smart Contract[​](#steps-to-deploy-the-helloworld-smart-contract "Direct link to Steps to Deploy the HelloWorld Smart Contract")

1. Create a file named `HelloWorld.sol`.
2. Select Solidity Compiler and compile `HelloWorld.sol`.
3. Select Deploy & Run Transactions.
4. Make sure to select `Injected Provider - Metamask` in Environment dropdown.
5. Deploy the `HelloWorld` smart contract.

## Calling the Deployed Smart Contract[​](#calling-the-deployed-smart-contract "Direct link to Calling the Deployed Smart Contract")

![Call Smart Contract](/assets/images/Remix-call-getGreeting-558cf56bb12d6b95cbd0e3e272d62499.gif)

### Using Ethers.js to Call the HelloWorld Smart Contract[​](#using-ethersjs-to-call-the-helloworld-smart-contract "Direct link to Using Ethers.js to Call the HelloWorld Smart Contract")

1. Create a new `get-greeting.js` file under `scripts`.
2. Paste in the JavaScript code below.
3. Click on green play button to run.
4. Verify the greeting is "Hello World!".

`_25

// Import ethers from the ethers.js library

_25

const { ethers } = require('ethers');

_25

_25

// Define the contract ABI

_25

const contractABI = ['function hello() public view returns (string memory)'];

_25

_25

// Define the contract address

_25

const contractAddress = '0x8a120383e6057b1f3aef4fa9b89c2f1b0a695926';

_25

_25

// Connect to the Ethereum network

_25

// This example uses the default provider from ethers.js, which connects to the Ethereum mainnet.

_25

// For a testnet or custom RPC, use ethers.getDefaultProvider('networkName') or new ethers.providers.JsonRpcProvider(url)

_25

const provider = new ethers.providers.Web3Provider(window?.ethereum);

_25

_25

// Create a new contract instance

_25

const contract = new ethers.Contract(contractAddress, contractABI, provider);

_25

_25

// Call the hello function of the contract

_25

async function getGreeting() {

_25

const greeting = await contract.hello();

_25

console.log(greeting);

_25

}

_25

_25

// Execute the function

_25

getGreeting();`

Follow the steps below to change the greeting and retrieve the new greeting.

## Updating the Deployed Smart Contract[​](#updating-the-deployed-smart-contract "Direct link to Updating the Deployed Smart Contract")

![Update Smart Contract](/assets/images/Remix-update-greeting-0483aaa0c04ee4fdbcfaa4600a6580d8.gif)

1. Select the `HelloWorld.sol` file.
2. Select the `Deploy and Run Transaction` page.
3. Make sure to select `Injected Provider - Metamask` in Environment dropdown.
4. Type a new greeting in the text input next to orange `changeGreeting` button.
5. Click on the orange `changeGreeting` button.
6. Sign the Metamask transaction.
7. Verify the greeting has changed by re-running `get-greeting.js` script above.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/evm/guides/remix.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Hardhat](/build/evm/guides/hardhat)[Next

Rainbowkit](/build/evm/guides/rainbowkit)

###### Rate this page

😞😐😊

Copy as Markdown

* [Add the Flow Network to MetaMask](#add-the-flow-network-to-metamask)
* [Fund Your Flow Account](#fund-your-flow-account)
* [Deploying a Smart Contract Using Remix](#deploying-a-smart-contract-using-remix)
  + [HelloWorld Smart Contract](#helloworld-smart-contract)
  + [Steps to Deploy the HelloWorld Smart Contract](#steps-to-deploy-the-helloworld-smart-contract)
* [Calling the Deployed Smart Contract](#calling-the-deployed-smart-contract)
  + [Using Ethers.js to Call the HelloWorld Smart Contract](#using-ethersjs-to-call-the-helloworld-smart-contract)
* [Updating the Deployed Smart Contract](#updating-the-deployed-smart-contract)

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