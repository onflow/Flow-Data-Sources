# Source: https://developers.flow.com/evm/guides/wagmi

Viem & Wagmi | Flow Developer Portal



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
* Viem & Wagmi

On this page

info

Make sure to use `viem` version `2.9.6` or greater. This version contains flow EVM networks

# Using viem

Flow networks have been added to viem chain definitions [viem networks](https://github.com/wevm/viem/tree/main/src/chains/definitions). This allows for convenient flow network configuration when using viem and wagmi.

## Viem Flow Config[​](#viem-flow-config "Direct link to Viem Flow Config")

The configuration below uses Flow Testnet. Since this configuration is already in viem various properties are already set, like block explorer and json-rpc endpoint. See how this configuration is used in a nextjs wagmi web application below.

`_11

import { http, createConfig } from '@wagmi/core';

_11

import { flowTestnet } from '@wagmi/core/chains';

_11

import { injected } from '@wagmi/connectors';

_11

_11

export const config = createConfig({

_11

chains: [flowTestnet],

_11

connectors: [injected()],

_11

transports: {

_11

[flowTestnet.id]: http(),

_11

},

_11

});`

# Using Next.js and Wagmi

This tutorial will guide you through creating a simple web application, connect to an EVM capable wallet and interact with the "HelloWorld" smart contract to get and set greetings. We will not dive into managing transactions.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Node.js installed on your machine
* A code editor (e.g., Visual Studio Code)
* Basic knowledge of React and Next.js

## Step 1: Setting Up the Next.js Project[​](#step-1-setting-up-the-nextjs-project "Direct link to Step 1: Setting Up the Next.js Project")

This tutorial will be following [Wagmi getting-started manual tutorial](https://wagmi.sh/react/getting-started)
First, let's create a Wagmi project named `flow-evm-wagmi`. We will use npm but you are welcome to use yarn or bun.

`_10

npm create wagmi@latest

_10

_10

# project name flow-evm-wagmi

_10

# Select 'React' then 'next'`

After Wagmi automatic installation procedure.

`_10

cd flow-evm-wagmi

_10

npm install`

## Step 2: Configuring Wagmi and Connecting the Wallet[​](#step-2-configuring-wagmi-and-connecting-the-wallet "Direct link to Step 2: Configuring Wagmi and Connecting the Wallet")

Make sure you have Metamask installed and Flow network configured. [Metamask and Flow blockchain](/evm/using).
Wagmi needs to know what networks to be aware of. Let's configure to use Flow Testnet by updating config.ts file with the following:

`_11

import { http, createConfig } from '@wagmi/core';

_11

import { flowTestnet } from '@wagmi/core/chains';

_11

import { injected } from '@wagmi/connectors';

_11

_11

export const config = createConfig({

_11

chains: [flowTestnet],

_11

connectors: [injected()],

_11

transports: {

_11

[flowTestnet.id]: http(),

_11

},

_11

});`

By default Wagmi configures many wallets, MetaMask, Coinbase Wallet, and WalletConnect as wallet providers. Above we simplify the code to only be interested in the Injected Provider, which we are interested in Metamask. Verify `page.tsx` code looks like the following.

`_47

'use client'

_47

_47

import { useAccount, useConnect, useDisconnect } from 'wagmi'

_47

_47

function App() {

_47

const account = useAccount()

_47

const { connectors, connect, status, error } = useConnect()

_47

const { disconnect } = useDisconnect()

_47

_47

return (

_47

<>

_47

<div>

_47

<h2>Account</h2>

_47

_47

<div>

_47

status: {account.status}

_47

<br />

_47

addresses: {JSON.stringify(account.addresses)}

_47

<br />

_47

chainId: {account.chainId}

_47

</div>

_47

_47

{account.status === 'connected' && (

_47

<button type="button" onClick={() => disconnect()}>

_47

Disconnect

_47

</button>

_47

)}

_47

</div>

_47

_47

<div>

_47

<h2>Connect</h2>

_47

{connectors.map((connector) => (

_47

<button

_47

key={connector.uid}

_47

onClick={() => connect({ connector })}

_47

type="button"

_47

>

_47

{connector.name}

_47

</button>

_47

))}

_47

<div>{status}</div>

_47

<div>{error?.message}</div>

_47

</div>

_47

</>

_47

}

_47

_47

export default App`

![Connect Metamask](/assets/images/Connect-Metamask-05771fc62a4255dc6553d04615567caf.gif)

This step relies on an already deployed HelloWorld contract. See [Using Remix](/evm/guides/remix) to deploy a smart contract on flow evm blockchain.
Create or edit the simple `page.tsx` file in the app directory to have better styles, that's beyond this tutorial. We will modify `page.txs` to add a new `HelloWorld.tsx`. Replace `YOUR_CONTRACT_ADDRESS` with your deployed address.

## Step 3: Creating the Interface for HelloWorld Contract[​](#step-3-creating-the-interface-for-helloworld-contract "Direct link to Step 3: Creating the Interface for HelloWorld Contract")

Now, let's create a component to interact with the HelloWorld contract. Assume your contract is already deployed, and you have its address and ABI.

* Create a new file, HelloWorld.ts, in the components directory.
* Use Wagmi's hooks to read from and write to the smart contract:

`_47

import { useState } from 'react';

_47

import {

_47

useContractRead,

_47

useContractWrite,

_47

useAccount,

_47

useConnect,

_47

} from 'wagmi';

_47

import contractABI from './HelloWorldABI.json'; // Import your contract's ABI

_47

_47

const contractAddress = 'YOUR_CONTRACT_ADDRESS';

_47

_47

const HelloWorld = () => {

_47

const [newGreeting, setNewGreeting] = useState('');

_47

const { address, isConnected } = useAccount();

_47

const { connect } = useConnect();

_47

_47

const { data: greeting } = useContractRead({

_47

addressOrName: contractAddress,

_47

contractInterface: contractABI,

_47

functionName: 'hello',

_47

});

_47

_47

const { write: changeGreeting } = useContractWrite({

_47

addressOrName: contractAddress,

_47

contractInterface: contractABI,

_47

functionName: 'changeGreeting',

_47

args: [newGreeting],

_47

});

_47

_47

if (!isConnected) {

_47

return <button onClick={() => connect()}>Connect Wallet</button>;

_47

}

_47

_47

return (

_47

<div>

_47

<p>Current Greeting: {greeting}</p>

_47

<input

_47

value={newGreeting}

_47

onChange={(e) => setNewGreeting(e.target.value)}

_47

placeholder="New greeting"

_47

/>

_47

<button onClick={() => changeGreeting()}>Update Greeting</button>

_47

</div>

_47

);

_47

};

_47

_47

export default HelloWorld;`

Reminder: aReplace YOUR\_CONTRACT\_ADDRESS with the actual address of your deployed HelloWorld contract.

Also notice you need the HelloWorld contract ABI, save this to a new file called `HelloWorld.json` in the app directory.

`_48

{

_48

"abi": [

_48

{

_48

"inputs": [],

_48

"stateMutability": "nonpayable",

_48

"type": "constructor"

_48

},

_48

{

_48

"inputs": [

_48

{

_48

"internalType": "string",

_48

"name": "newGreeting",

_48

"type": "string"

_48

}

_48

],

_48

"name": "changeGreeting",

_48

"outputs": [],

_48

"stateMutability": "nonpayable",

_48

"type": "function"

_48

},

_48

{

_48

"inputs": [],

_48

"name": "greeting",

_48

"outputs": [

_48

{

_48

"internalType": "string",

_48

"name": "",

_48

"type": "string"

_48

}

_48

],

_48

"stateMutability": "view",

_48

"type": "function"

_48

},

_48

{

_48

"inputs": [],

_48

"name": "hello",

_48

"outputs": [

_48

{

_48

"internalType": "string",

_48

"name": "",

_48

"type": "string"

_48

}

_48

],

_48

"stateMutability": "view",

_48

"type": "function"

_48

}

_48

]

_48

}`

## Step 4: Integrating the HelloWorld Component[​](#step-4-integrating-the-helloworld-component "Direct link to Step 4: Integrating the HelloWorld Component")

Finally, import and use the HelloWorld component in your `pages.tsx`, throw it at the bottom of the render section.

`_22

import HelloWorld from './helloWorld'

_22

_22

// put at the bottom of the Connect section.

_22

<div>

_22

<h2>Connect</h2>

_22

{connectors.map((connector) => (

_22

<button

_22

key={connector.uid}

_22

onClick={() => connect({ connector })}

_22

type="button"

_22

>

_22

{connector.name}

_22

</button>

_22

))}

_22

<div>{status}</div>

_22

<div>{error?.message}</div>

_22

</div>

_22

_22

// 👇👇👇👇👇👇👇👇👇👇👇

_22

<div>

_22

<HelloWorld />

_22

</div>`

Now, you have a functional App that can connect to Metamask, display the current greeting from the "HelloWorld" smart contract, and update the greeting.

Test it by updating the greeting, signing a transaction in your Metamask then wait a minute then refresh the website. Handling transactions are outside of this tutorial. We'll leave that as a future task. [Checkout Wagmi documentation](https://wagmi.sh/react/getting-started)

![Update HelloWorld Greeting](/assets/images/Update-HelloWorld-Greeting-97929700145ed51e0a6226f562fda7c0.gif)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/evm/guides/wagmi.md)

Last updated on **Feb 19, 2025** by **bz**

[Previous

Rainbowkit](/evm/guides/rainbowkit)[Next

Foundry](/evm/guides/foundry)

###### Rate this page

😞😐😊

* [Viem Flow Config](#viem-flow-config)
* [Prerequisites](#prerequisites)
* [Step 1: Setting Up the Next.js Project](#step-1-setting-up-the-nextjs-project)
* [Step 2: Configuring Wagmi and Connecting the Wallet](#step-2-configuring-wagmi-and-connecting-the-wallet)
* [Step 3: Creating the Interface for HelloWorld Contract](#step-3-creating-the-interface-for-helloworld-contract)
* [Step 4: Integrating the HelloWorld Component](#step-4-integrating-the-helloworld-component)

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