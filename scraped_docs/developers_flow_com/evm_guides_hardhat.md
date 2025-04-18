# Source: https://developers.flow.com/evm/guides/hardhat

Flow Hardhat Guide | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why EVM on Flow](/evm/about)
* [How it Works](/evm/how-it-works)
* [Using Flow EVM](/evm/using)
* [Network Information](/evm/networks)
* [EVM Quickstart](/evm/quickstart)
* [Fees](/evm/fees)
* [Accounts](/evm/accounts)
* [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
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
  + [Ethers](/evm/guides/ethers)
  + [Web3.js](/evm/guides/web3-js)

* Guides
* Hardhat

On this page

# Flow Hardhat Guide

Hardhat is an Ethereum development tool designed to facilitate the deployment, testing, and debugging of smart contracts. It provides a streamlined experience for developers working with Solidity contracts.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Node[​](#node "Direct link to Node")

Node v18 or higher, available for [download here](https://nodejs.org/en/download).

For those new to Hardhat, we recommend exploring the [official documentation](https://hardhat.org/tutorial/creating-a-new-hardhat-project) to get acquainted. The following instructions utilize `npm` to initialize a project and install dependencies:

### Wallet[​](#wallet "Direct link to Wallet")

You'll also need a wallet that supports EVM. For this guide, a MetaMask account and its corresponding private key will work.

`_10

mkdir hardhat-example

_10

cd hardhat-example

_10

_10

npm init

_10

_10

npm install --save-dev hardhat

_10

_10

npx hardhat init`

> When prompted, select TypeScript and to use `@nomicfoundation/hardhat-toolbox` to follow along with this guide.

### Fund Your Wallet[​](#fund-your-wallet "Direct link to Fund Your Wallet")

To deploy smart contracts, ensure your wallet has **$FLOW**. Obtain funds by navigating to the Flow [Faucet](https://faucet.flow.com/fund-account) and entering your wallet address.

## Deploying a Smart Contract with Hardhat[​](#deploying-a-smart-contract-with-hardhat "Direct link to Deploying a Smart Contract with Hardhat")

This section guides you through the process of deploying smart contracts on the Flow network using Hardhat.

### Configuration[​](#configuration "Direct link to Configuration")

First, incorporate the Testnet network into your `hardhat.config.ts`:

`_15

import { HardhatUserConfig } from 'hardhat/config';

_15

import '@nomicfoundation/hardhat-toolbox';

_15

_15

const config: HardhatUserConfig = {

_15

solidity: '0.8.24',

_15

networks: {

_15

testnet: {

_15

url: 'https://testnet.evm.nodes.onflow.org',

_15

accounts: [`<PRIVATE_KEY>`], // In practice, this should come from an environment variable and not be commited

_15

gas: 500000, // Example gas limit

_15

},

_15

},

_15

};

_15

_15

export default config;`

To keep this example straightforward, we've included the account's private key directly in `hardhat.config.ts`. However, it is crucial to avoid committing private keys to your Git repository for security reasons. Instead, opt for using environment variables for safer handling of sensitive information.

### Deploying HelloWorld Smart Contract[​](#deploying-helloworld-smart-contract "Direct link to Deploying HelloWorld Smart Contract")

## HelloWorld Smart Contract[​](#helloworld-smart-contract "Direct link to HelloWorld Smart Contract")

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

Deploying:

1. Create a file named `HelloWorld.sol` under `contracts` directory.
2. Add above `HelloWorld.sol` contract code to new file.
3. Create a `deploy.ts` file in `scripts` directory.
4. Paste in the following TypeScript code.

`_18

import { ethers } from 'hardhat';

_18

_18

async function main() {

_18

const [deployer] = await ethers.getSigners();

_18

_18

console.log('Deploying contracts with the account:', deployer.address);

_18

_18

const deployment = await ethers.deployContract('HelloWorld');

_18

_18

console.log('HelloWorld address:', await deployment.getAddress());

_18

}

_18

_18

main()

_18

.then(() => process.exit(0))

_18

.catch((error) => {

_18

console.error(error);

_18

process.exit(1);

_18

});`

5. Run `npx hardhat run scripts/deploy.ts --network testnet` in the project root.
6. Copy the deployed `HelloWorld` address. This address will be used in other scripts.

Output should look like this (with the exception that your address will be different):

`_10

❯ npx hardhat run scripts/deploy.ts --network testnet

_10

Deploying contracts with the account: ...

_10

HelloWorld address: 0x3Fe94f43Fb5CdB8268A801f274521a07F7b99dfb`

You can now search for your deployed contract on the [Flowscan block explorer](https://evm-testnet.flowscan.io/)!

### Get HelloWorld Contract Greeting[​](#get-helloworld-contract-greeting "Direct link to Get HelloWorld Contract Greeting")

Now, we want to get the greeting from the deployed `HelloWorld` smart contract.

`_23

import { ethers } from 'hardhat';

_23

import HelloWorldABI from '../artifacts/contracts/HelloWorld.sol/HelloWorld.json';

_23

_23

async function main() {

_23

// Replace with your contract's address

_23

const contractAddress = '0x3Fe94f43Fb5CdB8268A801f274521a07F7b99dfb';

_23

// Get hardhat provider

_23

const provider = ethers.provider;

_23

// Create a new contract instance

_23

const helloWorldContract = new ethers.Contract(

_23

contractAddress,

_23

HelloWorldABI.abi,

_23

provider,

_23

);

_23

// Call the greeting function

_23

const greeting = await helloWorldContract.hello();

_23

console.log('The greeting is:', greeting);

_23

}

_23

_23

main().catch((error) => {

_23

console.error(error);

_23

process.exit(1);

_23

});`

Steps:

1. Create a `getGreeting.ts` file in the `scripts` directory.
2. Paste contents of script above. Make sure to update the contract address with the one from deployment in earlier step.
3. Call script to get the greeting, `npx hardhat run scripts/getGreeting.ts --network testnet`
4. The output should be as follows:

`_10

❯ npx hardhat run scripts/getGreeting.ts --network testnet

_10

The greeting is: Hello, World!`

### Update Greeting on HelloWorld Smart Contract[​](#update-greeting-on-helloworld-smart-contract "Direct link to Update Greeting on HelloWorld Smart Contract")

Next, we'll add a script to update the greeting and log it.

`_38

import { ethers } from 'hardhat';

_38

import HelloWorldABI from '../artifacts/contracts/HelloWorld.sol/HelloWorld.json';

_38

_38

async function main() {

_38

const contractAddress = '0x3Fe94f43Fb5CdB8268A801f274521a07F7b99dfb';

_38

_38

const newGreeting = process.env.NEW_GREETING;

_38

if (!newGreeting) {

_38

console.error('Please set the NEW_GREETING environment variable.');

_38

process.exit(1);

_38

}

_38

_38

// Signer to send the transaction (e.g., the first account from the hardhat node)

_38

const [signer] = await ethers.getSigners();

_38

_38

// Contract instance with signer

_38

const helloWorldContract = new ethers.Contract(

_38

contractAddress,

_38

HelloWorldABI.abi,

_38

signer,

_38

);

_38

_38

console.log('The greeting is:', await helloWorldContract.hello());

_38

_38

// Create and send the transaction

_38

const tx = await helloWorldContract.changeGreeting(newGreeting);

_38

console.log('Transaction hash:', tx.hash);

_38

_38

// Wait for the transaction to be mined

_38

await tx.wait().catch((error: Error) => {});

_38

console.log('Greeting updated successfully!');

_38

console.log('The greeting is:', await helloWorldContract.hello());

_38

}

_38

_38

main().catch((error) => {

_38

console.error(error);

_38

process.exit(1);

_38

});`

Here are the steps to follow:

1. Create an `updateGreeting.ts` script in the `scripts` directory.
2. Paste in the TypeScript above, make sure to update the contract address with the one from deployment in earlier step.
3. Call the new script, `NEW_GREETING='Howdy!' npx hardhat run ./scripts/updateGreeting.ts --network testnet`
4. The output should be

`_10

❯ NEW_GREETING='Howdy!' npx hardhat run ./scripts/updateGreeting.ts --network testnet

_10

The greeting is: Hello, World!

_10

Transaction hash: 0x03136298875d405e0814f54308390e73246e4e8b4502022c657f04f3985e0906

_10

Greeting updated successfully!

_10

The greeting is: Howdy!`

### Verifying Contract[​](#verifying-contract "Direct link to Verifying Contract")

To verify your contract on [Flowscan](https://evm-testnet.flowscan.io/), you can update your Hardhat config file as such including the correct chainID, apiURL and browserURL:

`_37

import { HardhatUserConfig } from 'hardhat/config';

_37

import '@nomicfoundation/hardhat-toolbox';

_37

import "@nomicfoundation/hardhat-verify";

_37

_37

const PRIVATE_KEY = vars.get("EVM_PRIVATE_KEY");

_37

_37

const config: HardhatUserConfig = {

_37

solidity: '0.8.24',

_37

networks: {

_37

testnet: {

_37

url: 'https://testnet.evm.nodes.onflow.org',

_37

accounts: [PRIVATE_KEY], // In practice, this should come from an environment variable and not be commited

_37

gas: 500000, // Example gas limit

_37

},

_37

},

_37

etherscan: {

_37

apiKey: {

_37

// Is not required by blockscout. Can be any non-empty string

_37

'testnet': "abc"

_37

},

_37

customChains: [

_37

{

_37

network: "testnet",

_37

chainId: 545,

_37

urls: {

_37

apiURL: "https://evm-testnet.flowscan.io/api",

_37

browserURL: "https://evm-testnet.flowscan.io/",

_37

}

_37

}

_37

]

_37

},

_37

sourcify: {

_37

enabled: false

_37

}

_37

};

_37

_37

export default config;`

The [verify](https://docs.blockscout.com/developer-support/verifying-a-smart-contract/hardhat-verification-plugin) plugin requires you to include constructor arguments with the verify task and ensures that they correspond to expected ABI signature. However, Blockscout ignores those arguments, so you may specify any values that correspond to the ABI. Execute the following command to verify the contract:

`_10

npx hardhat verify --network testnet DEPLOYED_CONTRACT_ADDRESS "Constructor argument 1"`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/guides/hardhat.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Integrating Metamask](/evm/guides/integrating-metamask)[Next

Remix](/evm/guides/remix)

###### Rate this page

😞😐😊

* [Prerequisites](#prerequisites)
  + [Node](#node)
  + [Wallet](#wallet)
  + [Fund Your Wallet](#fund-your-wallet)
* [Deploying a Smart Contract with Hardhat](#deploying-a-smart-contract-with-hardhat)
  + [Configuration](#configuration)
  + [Deploying HelloWorld Smart Contract](#deploying-helloworld-smart-contract)
* [HelloWorld Smart Contract](#helloworld-smart-contract)
  + [Get HelloWorld Contract Greeting](#get-helloworld-contract-greeting)
  + [Update Greeting on HelloWorld Smart Contract](#update-greeting-on-helloworld-smart-contract)
  + [Verifying Contract](#verifying-contract)

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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