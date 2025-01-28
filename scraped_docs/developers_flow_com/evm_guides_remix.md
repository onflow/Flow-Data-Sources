# Source: https://developers.flow.com/evm/guides/remix




Flow Remix Guide | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using EVM](/evm/using)
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
  + [Viem & Wagmi](/evm/guides/wagmi)
  + [Foundry](/evm/guides/foundry)
  + [VRF (Randomness) in Solidity](/evm/guides/vrf)
* [Clients](/evm/clients/ethers)
* [Using EVM with Cadence](/evm/cadence/interacting-with-coa)


* Guides
* Remix
On this page
# Using Remix

Remix is an open-source, web-based development environment tailored for EVM smart contract development. It offers developers a comprehensive suite of tools for writing, deploying, and testing smart contracts in Solidity. For more information, visit [Remix](https://remix.ethereum.org/).

## Add the Flow Network to MetaMask[​](#add-the-flow-network-to-metamask "Direct link to Add the Flow Network to MetaMask")

![Add Flow Network](/assets/images/Remix-adding-metamask-network-4912936e5dad423a4d858266eb9648a7.gif)

Navigate to the [Using EVM](/evm/using) page to find the button to add the Flow network information to your metamask.

## Fund Your Flow Account[​](#fund-your-flow-account "Direct link to Fund Your Flow Account")

Navigate to the [Flow Testnet Faucet](https://faucet.flow.com/fund-account) to obtain FLOW tokens necessary for deploying a smart contract.

## Deploying a Smart Contract Using Remix[​](#deploying-a-smart-contract-using-remix "Direct link to Deploying a Smart Contract Using Remix")

![Deploy Smart Contract](/assets/images/Remix-deploy-contract-flowevm-041b338f872e80325bd497587cfe7e42.gif)

### HelloWorld Smart Contract[​](#helloworld-smart-contract "Direct link to HelloWorld Smart Contract")

 `_25// SPDX-License-Identifier: MIT_25pragma solidity ^0.8.0;_25_25contract HelloWorld {_25 // Declare a public field of type string._25 string public greeting;_25_25 // Constructor to initialize the greeting._25 // In Solidity, the constructor is defined with the "constructor" keyword._25 constructor() {_25 greeting = "Hello, World!";_25 }_25_25 // Public function to change the greeting._25 // The "public" keyword makes the function accessible from outside the contract._25 function changeGreeting(string memory newGreeting) public {_25 greeting = newGreeting;_25 }_25_25 // Public function that returns the greeting._25 // In Solidity, explicit return types are declared._25 function hello() public view returns (string memory) {_25 return greeting;_25 }_25}`
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

 `_25// Import ethers from the ethers.js library_25const { ethers } = require('ethers');_25_25// Define the contract ABI_25const contractABI = ['function hello() public view returns (string memory)'];_25_25// Define the contract address_25const contractAddress = '0x8a120383e6057b1f3aef4fa9b89c2f1b0a695926';_25_25// Connect to the Ethereum network_25// This example uses the default provider from ethers.js, which connects to the Ethereum mainnet._25// For a testnet or custom RPC, use ethers.getDefaultProvider('networkName') or new ethers.providers.JsonRpcProvider(url)_25const provider = new ethers.providers.Web3Provider(window?.ethereum);_25_25// Create a new contract instance_25const contract = new ethers.Contract(contractAddress, contractABI, provider);_25_25// Call the hello function of the contract_25async function getGreeting() {_25 const greeting = await contract.hello();_25 console.log(greeting);_25}_25_25// Execute the function_25getGreeting();`

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
[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/guides/remix.md)Last updated on **Jan 10, 2025** by **Brian Doyle**[PreviousHardhat](/evm/guides/hardhat)[NextViem & Wagmi](/evm/guides/wagmi)
###### Rate this page

😞😐😊

* [Add the Flow Network to MetaMask](#add-the-flow-network-to-metamask)
* [Fund Your Flow Account](#fund-your-flow-account)
* [Deploying a Smart Contract Using Remix](#deploying-a-smart-contract-using-remix)
  + [HelloWorld Smart Contract](#helloworld-smart-contract)
  + [Steps to Deploy the HelloWorld Smart Contract](#steps-to-deploy-the-helloworld-smart-contract)
* [Calling the Deployed Smart Contract](#calling-the-deployed-smart-contract)
  + [Using Ethers.js to Call the HelloWorld Smart Contract](#using-ethersjs-to-call-the-helloworld-smart-contract)
* [Updating the Deployed Smart Contract](#updating-the-deployed-smart-contract)
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

