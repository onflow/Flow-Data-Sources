# Source: https://developers.flow.com/blockchain-development-tutorials/integrations/gelato-sw

Gelato Smart Wallet | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Actions](/blockchain-development-tutorials/defi)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Integrations](/blockchain-development-tutorials/integrations/crossmint)

  + [Crossmint Integration Guide](/blockchain-development-tutorials/integrations/crossmint)
  + [Gelato Smart Wallet](/blockchain-development-tutorials/integrations/gelato-sw)

* Integrations
* Gelato Smart Wallet

On this page

# Gelato Smart Wallet Integration Guide

Gas fees are one of the biggest barriers to blockchain adoption. Users often need to hold native tokens just to pay for transaction fees, creating friction in onboarding and limiting the types of applications that can be built. Gelato Smart Wallet solves this problem by enabling **gasless transactions** on Flow EVM through sponsored transactions.

With Gelato Smart Wallet, you can:

* **Eliminate gas fees** for your users by sponsoring their transactions
* **Improve user experience** with seamless onboarding that doesn't require users to hold FLOW tokens
* **Support EIP-7702** for enhanced smart wallet functionality
* **Scale your dApp** by removing the cost barrier for user interactions
* **Leverage Flow's low gas costs** to provide affordable sponsored transactions

This tutorial will guide you through setting up Gelato Smart Wallet to enable gasless transactions on Flow EVM. You'll learn how to configure the necessary API keys, fund your sponsorship account, and implement gasless transaction functionality in your applications.

info

This tutorial focuses on **EIP-7702** implementation with Gelato Smart Wallet on Flow EVM. EIP-7702 provides a streamlined experience for users by maintaining the same address as their EOA while adding smart wallet capabilities, enabling enhanced features like gasless transactions and improved user experience.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Configure a Gelato Smart Wallet account with proper API keys and funding setup
* Implement gasless transaction functionality using the Gelato Smart Wallet SDK
* Estimate and execute sponsored transactions on Flow EVM
* Integrate EIP-7702 features for enhanced user experience
* Troubleshoot common issues with Gelato Smart Wallet integration

## Prerequisites of using Gelato Smart Wallet[​](#prerequisites-of-using-gelato-smart-wallet "Direct link to Prerequisites of using Gelato Smart Wallet")

You need to set up the following in the Gelato App to create a Gelato Sponsor API Key:

### Step 1. Create Your Gelato Account[​](#step-1-create-your-gelato-account "Direct link to Step 1. Create Your Gelato Account")

Sign up on the [Gelato App](https://app.gelato.cloud/) to establish an account. This account is the foundation for setting up relay tasks and managing gas sponsorships.

### Step 2. Deposit Funds into 1Balance[​](#step-2-deposit-funds-into-1balance "Direct link to Step 2. Deposit Funds into 1Balance")

To use Gelato for sponsored transactions, you need to deposit funds into 1Balance according to your target environment:

* Mainnets: Deposit USDC.
* Testnets: Deposit Sepolia ETH.

Click the `1Balance` tab to link your wallet first.

![Link Wallet](/assets/images/gelato-1balance-1-85cc09f16ebfcdc18907739dc1a4b2bf.png)

And then deposit some Sepolia ETH(SEP) testnet funds.

![Deposit Funds into 1Balance](/assets/images/gelato-1balance-2-9a756d9b56f821bdf6fce443aaedc6f0.png)

If you need to fund your account, you can use one of the following third-party faucets:

* [Google Cloud Sepolia Faucet](https://cloud.google.com/application/web3/faucet/ethereum/sepolia)
* [Alchemy Sepolia Faucet](https://www.alchemy.com/faucets/ethereum-sepolia)
* [Chainlink Sepolia Faucet](https://faucets.chain.link/sepolia)
* [Metamask Sepolia Faucet](https://docs.metamask.io/developer-tools/faucet/)

### Step 3. Create a Relay App[​](#step-3-create-a-relay-app "Direct link to Step 3. Create a Relay App")

Select the `Relay` tab in the Gelato App and switch to the `Testnet` environment.

Now you can create a new *Relay App* with the Flow EVM network.  
For Testnet, you can first allow `Any contract` to call your relay app.

![Create a Relay App](/assets/images/gelato-relay-1-e4a4a6f4ce619e22652c4e245ac3e98b.png)

warning

You'll need to add more information for your smart contracts at a later date.

When set to a specific contract instead of `Any contract`, the API keys will only allow sponsored transactions for calls to the designated methods within the ABI of that contract.

### Step 4. Create/Obtain an API Key[​](#step-4-createobtain-an-api-key "Direct link to Step 4. Create/Obtain an API Key")

After creating the Relay App, navigate to its dashboard to locate your Sponsor API Key.

![Create a Sponsor API Key](/assets/images/gelato-relay-2-51faaf58b72056e7af60b50e22b940a0.png)

This key links your Gelato setup with 1Balance for gas sponsorship.

Copy the API key to your clipboard.

## Send Gasless Transactions for your users[​](#send-gasless-transactions-for-your-users "Direct link to Send Gasless Transactions for your users")

After you have created a Sponsor API Key and deposited funds into 1Balance, you can use gasless transactions features for your users.

With the Gelato Smart Wallet SDK, developers can easily set up sponsored transactions for their applications in just a few simple steps, enabling seamless onboarding and interaction without requiring users to hold native tokens.

note

You can find the examples in the [Gelato Smart Wallet SDK](https://github.com/gelatodigital/smartwallet/tree/master/examples) repository.

### Step 1. Install all relevant dependencies[​](#step-1-install-all-relevant-dependencies "Direct link to Step 1. Install all relevant dependencies")

* pnpm
* bun
* yarn
* npm

`_10

pnpm add @gelatonetwork/smartwallet viem`

`_10

bun add @gelatonetwork/smartwallet viem`

`_10

yarn add @gelatonetwork/smartwallet viem`

`_10

npm install @gelatonetwork/smartwallet viem`

### Step 2. Setup Smart Wallet Account[​](#step-2-setup-smart-wallet-account "Direct link to Step 2. Setup Smart Wallet Account")

Import required dependencies:

`_11

import { createGelatoSmartWalletClient, sponsored } from "@gelatonetwork/smartwallet";

_11

import { gelato } from "@gelatonetwork/smartwallet/accounts";

_11

import { createWalletClient, createPublicClient, http, type Hex } from "viem";

_11

import { generatePrivateKey, privateKeyToAccount } from "viem/accounts";

_11

import { flowTestnet } from "viem/chains";

_11

_11

// Create a public client for the Flow Testnet

_11

const publicClient = createPublicClient({

_11

chain: flowTestnet,

_11

transport: http(),

_11

});`

You can set up a Smart Account as per your needs.  
Once you create the `gelato` account, the Gelato Smart Account address will be the same as your EOA, enabling EIP-7702 features.

`_10

// Prepare a normal EOA account

_10

const privateKey = (process.env.PRIVATE_KEY ?? generatePrivateKey()) as Hex;

_10

const owner = privateKeyToAccount(privateKey);

_10

_10

// Wrap the EOA account into a Gelato Smart account

_10

const account = await gelato({

_10

owner,

_10

client: publicClient,

_10

});`

Then you need to create a standard viem wallet client with the Gelato Smart Account.

`_10

const client = createWalletClient({

_10

account,

_10

chain: flowTestnet,

_10

transport: http()

_10

});`

Once you have a standard viem wallet client, you can wrap it into a Gelato Smart Wallet client with the sponsor API key.

`_10

const sponsorApiKey = process.env.SPONSOR_API_KEY;

_10

if (!sponsorApiKey) {

_10

throw new Error("SPONSOR_API_KEY is not set");

_10

}

_10

_10

const swc = await createGelatoSmartWalletClient(client, {

_10

apiKey: sponsorApiKey

_10

});`

### Step 3. Estimate or Send a Gasless Transaction[​](#step-3-estimate-or-send-a-gasless-transaction "Direct link to Step 3. Estimate or Send a Gasless Transaction")

Now you can estimate or send a gasless transaction with the Gelato Smart Wallet client.

To estimate the fee and gas for a gasless transaction, you can use the `estimate` method.

`` _13

const response = await swc.estimate({

_13

payment: sponsored(sponsorApiKey),

_13

calls: [

_13

{

_13

to: "0xa8851f5f279eD47a292f09CA2b6D40736a51788E",

_13

data: "0xd09de08a",

_13

value: 0n

_13

}

_13

]

_13

});

_13

_13

console.log(`Estimated fee: ${formatEther(BigInt(response.fee.amount))} FLOW`);

_13

console.log(`Estimated gas: ${JSON.stringify(response.gas)} GAS`); ``

To send a gasless transaction, you can use the `execute` method.

`_14

const results = await smartWalletClient.execute({

_14

payment : sponsored(sponsorApiKey),

_14

calls: [

_14

{

_14

to: "0xa8851f5f279eD47a292f09CA2b6D40736a51788E",

_14

data: "0xd09de08a",

_14

value: 0n

_14

}

_14

]

_14

});

_14

_14

console.log("userOp hash:", results?.id);

_14

const txHash = await results?.wait();

_14

console.log("transaction hash",txHash);`

Or you can use `prepare` + `send` to send a gasless transaction.

`` _27

const preparedCalls = await swc.prepare({

_27

payment: sponsored(sponsorApiKey),

_27

calls: [

_27

{

_27

to: "0xa8851f5f279eD47a292f09CA2b6D40736a51788E",

_27

data: "0xd09de08a",

_27

value: 0n

_27

}

_27

]

_27

});

_27

_27

// Other actions can be performed here

_27

_27

const results = await swc.send({

_27

preparedCalls

_27

});

_27

_27

// You can listen for events from the Gelato Smart Wallet client

_27

results.on("submitted", (status: GelatoTaskStatus) => {

_27

console.log(`Transaction submitted: ${status.transactionHash}`);

_27

});

_27

results.on("success", async (status: GelatoTaskStatus) => {

_27

console.log(`Transaction successful: ${status.transactionHash}`);

_27

});

_27

results.on("error", (error: Error) => {

_27

console.error(`Transaction failed: ${error.message}`);

_27

}); ``

---

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you successfully integrated Gelato Smart Wallet to enable gasless transactions on Flow EVM. You learned how to set up the necessary infrastructure, configure API keys, fund sponsorship accounts, and implement gasless transaction functionality in your applications. The implementation demonstrates how Flow's low gas costs combined with Gelato's sponsored transaction infrastructure can create seamless user experiences that eliminate the friction of gas fees.

Now that you have completed the tutorial, you should be able to:

* Configure a Gelato Smart Wallet account with proper API keys and funding setup
* Implement gasless transaction functionality using the Gelato Smart Wallet SDK
* Estimate and execute sponsored transactions on Flow EVM
* Integrate EIP-7702 features for enhanced user experience
* Troubleshoot common issues with Gelato Smart Wallet integration

The combination of Flow's efficient gas pricing and Gelato's sponsored transaction infrastructure opens up new possibilities for building user-friendly dApps. By eliminating the need for users to hold native tokens for gas fees, you can create onboarding experiences that rival traditional Web2 applications while maintaining the security and transparency of blockchain technology.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/integrations/gelato-sw.mdx)

Last updated on **Aug 17, 2025** by **0xLisanAlGaib**

[Previous

Minting Platform Integration](/blockchain-development-tutorials/integrations/crossmint/minting-platform)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)
* [Prerequisites of using Gelato Smart Wallet](#prerequisites-of-using-gelato-smart-wallet)
  + [Step 1. Create Your Gelato Account](#step-1-create-your-gelato-account)
  + [Step 2. Deposit Funds into 1Balance](#step-2-deposit-funds-into-1balance)
  + [Step 3. Create a Relay App](#step-3-create-a-relay-app)
  + [Step 4. Create/Obtain an API Key](#step-4-createobtain-an-api-key)
* [Send Gasless Transactions for your users](#send-gasless-transactions-for-your-users)
  + [Step 1. Install all relevant dependencies](#step-1-install-all-relevant-dependencies)
  + [Step 2. Setup Smart Wallet Account](#step-2-setup-smart-wallet-account)
  + [Step 3. Estimate or Send a Gasless Transaction](#step-3-estimate-or-send-a-gasless-transaction)
* [Conclusion](#conclusion)

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