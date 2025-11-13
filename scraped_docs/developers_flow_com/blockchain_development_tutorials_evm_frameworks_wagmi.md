# Source: https://developers.flow.com/blockchain-development-tutorials/evm/frameworks/wagmi

Viem & Wagmi | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

* * [Flow EVM Guides](/blockchain-development-tutorials/evm)* [Flow EVM Frameworks](/blockchain-development-tutorials/evm/frameworks)* Viem & Wagmi

On this page

info

Make sure to use `viem` version `2.9.6` or greater. This version contains flow EVM networks

# Viem & Wagmi

Flow networks have been added to viem chain definitions [viem networks](https://github.com/wevm/viem/tree/main/src/chains/definitions). This allows for convenient flow network configuration when you use viem and wagmi.

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

# Use Next.js and Wagmi

This tutorial will guide you through how to create a simple web application, connect to an EVM capable wallet and interact with the "HelloWorld" smart contract to get and set greetings. We will not dive into how to manage transactions.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* `Node.js` installed on your machine.
* A code editor (such as Visual Studio Code).
* Basic knowledge of React and `Next.js`.

## Step 1: Set up the Next.js project[​](#step-1-set-up-the-nextjs-project "Direct link to Step 1: Set up the Next.js project")

This tutorial will follow [Wagmi getting-started manual tutorial](https://wagmi.sh/react/getting-started).

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

## Step 2: Configure Wagmi and connect the Wallet[​](#step-2-configure-wagmi-and-connect-the-wallet "Direct link to Step 2: Configure Wagmi and connect the Wallet")

Make sure you have Metamask installed and Flow network configured. [Metamask and Flow blockchain](/build/evm/using).
Wagmi needs to know what networks to be aware of. Let's configure to use Flow Testnet and update the `config.ts` file with the following:

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

By default, Wagmi configures many wallets, MetaMask, Coinbase Wallet, and WalletConnect as wallet providers. Above, we simplify the code to only be interested in the Injected Provider, which we are interested in Metamask. Verify `page.tsx` code looks like the following.

`_48

'use client';

_48

_48

import { useAccount, useConnect, useDisconnect } from 'wagmi';

_48

_48

function App() {

_48

const account = useAccount();

_48

const { connectors, connect, status, error } = useConnect();

_48

const { disconnect } = useDisconnect();

_48

_48

return (

_48

<>

_48

<div>

_48

<h2>Account</h2>

_48

_48

<div>

_48

status: {account.status}

_48

<br />

_48

addresses: {JSON.stringify(account.addresses)}

_48

<br />

_48

chainId: {account.chainId}

_48

</div>

_48

_48

{account.status === 'connected' && (

_48

<button type="button" onClick={() => disconnect()}>

_48

Disconnect

_48

</button>

_48

)}

_48

</div>

_48

_48

<div>

_48

<h2>Connect</h2>

_48

{connectors.map((connector) => (

_48

<button

_48

key={connector.uid}

_48

onClick={() => connect({ connector })}

_48

type="button"

_48

>

_48

{connector.name}

_48

</button>

_48

))}

_48

<div>{status}</div>

_48

<div>{error?.message}</div>

_48

</div>

_48

</>

_48

);

_48

}

_48

_48

export default App;`

![Connect Metamask](/assets/images/Connect-Metamask-05771fc62a4255dc6553d04615567caf.gif)

This step relies on an already deployed HelloWorld contract. See [Using Remix](/blockchain-development-tutorials/evm/development-tools/remix) to deploy a smart contract on flow evm blockchain. Create or edit the simple `page.tsx` file in the app directory to have better styles, that's beyond this tutorial. We will modify `page.txs` to add a new `HelloWorld.tsx`. Replace `YOUR_CONTRACT_ADDRESS` with your deployed address.

## Step 3: Create the interface for HelloWorld contract[​](#step-3-create-the-interface-for-helloworld-contract "Direct link to Step 3: Create the interface for HelloWorld contract")

Now, let's create a component to interact with the HelloWorld contract. Assume your contract is already deployed, and you have its address and ABI.

* Create a new file, `HelloWorld.ts`, in the components directory.
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

Reminder: Replace YOUR\_CONTRACT\_ADDRESS with the actual address of your deployed HelloWorld contract.

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

## Step 4: Integrate the HelloWorld Component[​](#step-4-integrate-the-helloworld-component "Direct link to Step 4: Integrate the HelloWorld Component")

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

To test it, update the greeting, sign a transaction in your Metamask, wait a minute, then refresh the website. Handling transactions are outside of this tutorial. We'll leave that as a future task. [Checkout Wagmi documentation](https://wagmi.sh/react/getting-started)

![Update HelloWorld Greeting](/assets/images/Update-HelloWorld-Greeting-97929700145ed51e0a6226f562fda7c0.gif)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/evm/frameworks/wagmi.md)

Last updated on **Nov 6, 2025** by **cshannon1218**

[Previous

Web3.js](/blockchain-development-tutorials/evm/frameworks/web3-js)[Next

Rainbowkit](/blockchain-development-tutorials/evm/frameworks/rainbowkit)

###### Rate this page

😞😐😊

Copy as Markdown

* [Viem Flow Config](#viem-flow-config)* [Prerequisites](#prerequisites)* [Step 1: Set up the Next.js project](#step-1-set-up-the-nextjs-project)* [Step 2: Configure Wagmi and connect the Wallet](#step-2-configure-wagmi-and-connect-the-wallet)* [Step 3: Create the interface for HelloWorld contract](#step-3-create-the-interface-for-helloworld-contract)* [Step 4: Integrate the HelloWorld Component](#step-4-integrate-the-helloworld-component)

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