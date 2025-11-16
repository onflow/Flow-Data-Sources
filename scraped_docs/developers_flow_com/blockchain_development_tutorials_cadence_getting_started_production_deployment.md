# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/getting-started/production-deployment

Production Deployment | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            - [Cadence Environment Setup](/blockchain-development-tutorials/cadence/getting-started/cadence-environment-setup)- [Smart Contract Interaction](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)- [Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)- [Production Deployment](/blockchain-development-tutorials/cadence/getting-started/production-deployment)+ [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  + [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)* Production Deployment

On this page

# Production deployment

You've developed locally with the emulator, integrated external dependencies, built sophisticated transactions, implemented comprehensive testing, and created a frontend interface. Now it's time to take your application live and deploy it to Flow's public networks.

This tutorial will guide you through deploying your Counter application to both testnet and mainnet, ensuring your contracts and frontend work seamlessly in production environments. You'll learn the essential practices for how to manage live blockchain applications, from security considerations to monitoring and maintenance.

## What you'll learn[​](#what-youll-learn "Direct link to What you'll learn")

After you complete this tutorial, you'll be able to:

* **Deploy contracts to Flow testnet** with proper account setup and funding.
* **Configure your application** for different network environments (emulator, testnet, mainnet).
* **Deploy to mainnet** with security best practices and production considerations.
* **Update frontend configuration** to work with live networks.
* **Implement monitoring and maintenance** practices for production applications.
* **Understand the deployment pipeline** from development to production.

**Prerequisites:**

* Completed all previous tutorials ([Environment Setup], [Smart Contract Interaction], [Building a Frontend App]).
* Counter contract and frontend app working locally.
* Flow CLI installed and configured.

## Deploy to Testnet[​](#deploy-to-testnet "Direct link to Deploy to Testnet")

Testnet is Flow's public test network that mirrors mainnet functionality without using real FLOW tokens. It's the perfect environment to test your application in a live blockchain environment before you commit to mainnet deployment.

### Understanding Flow networks[​](#understanding-flow-networks "Direct link to Understanding Flow networks")

Flow has several networks for different purposes:

* **Emulator**: Local development environment (what you currently use).
* **Testnet**: Public test network with free test tokens.
* **Mainnet**: Production network with real Flow tokens.

Each network has its own:

* Access nodes and APIs.
* Account addresses and contract deployments.
* Token economics (free on testnet, real value on mainnet).

### Create a testnet account[​](#create-a-testnet-account "Direct link to Create a testnet account")

First, you'll need a testnet account to deploy your contracts. You can create one with the Flow CLI:

`_10

flow accounts create --network testnet`

When prompted:

1. **Account name**: Enter `testnet-account`
2. **Select "Testnet" Network**

This creates a new account on testnet and adds it to your `flow.json` configuration. The CLI will show you the account address and save the private key locally.

### Fund your testnet account[​](#fund-your-testnet-account "Direct link to Fund your testnet account")

To deploy contracts and send transactions on testnet, you need Flow tokens. Flow provides a faucet service to get free testnet tokens.

1. Visit the [Flow Testnet Faucet](https://faucet.flow.com/).
2. Enter your testnet account address.
3. Complete any required verification (captcha, and so on).
4. Request tokens (you'll receive 1000 FLOW tokens).

This command automatically requests tokens from the testnet faucet for your account.

`_10

flow accounts fund --network testnet testnet-account`

**Verify funding:**

Check your account balance:

`_10

flow accounts list`

You will see your account details with a balance of Flow tokens.

### Configure testnet deployment[​](#configure-testnet-deployment "Direct link to Configure testnet deployment")

Update your `flow.json` to include testnet deployment configuration. The `NumberFormatter` contract already exists on testnet, so you only need to deploy your Counter contract.

`_10

flow config add deployment`

Follow the prompts:

1. **Network**: `testnet`
2. **Account**: `testnet-account`
3. **Contract**: `Counter`
4. **Deploy more contracts**: `yes`
5. **Contract**: `NumberFormatter`

Your `flow.json` now includes a testnet deployment section:

`_18

{

_18

"deployments": {

_18

"emulator": {

_18

"default": [

_18

"Counter"

_18

],

_18

"emulator-account": [

_18

"NumberFormatter"

_18

]

_18

},

_18

"testnet": {

_18

"testnet-account": [

_18

"Counter",

_18

"NumberFormatter"

_18

]

_18

}

_18

}

_18

}`

### Deploy Counter contract to testnet[​](#deploy-counter-contract-to-testnet "Direct link to Deploy Counter contract to testnet")

Deploy your Counter contract to the public testnet:

`_10

flow project deploy --network testnet`

You will see output similar to:

`_10

Deploying 2 contracts for accounts: testnet-account

_10

_10

Counter -> 0x9942a81bc6c3c5b7 (d8fe130e5b2212a5c7b3c34fe6e74ede80c750bc4c57e57788e81b247dcd7fe0)

_10

NumberFormatter -> 0x9942a81bc6c3c5b7 (9a550aeefa5ede62cb95f0549084b2ab7abf3a493cf853d50c1c377a7be733b2)

_10

_10

🎉 All contracts deployed successfully`

### Test your testnet deployment[​](#test-your-testnet-deployment "Direct link to Test your testnet deployment")

Verify your contract works on testnet with this script:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc --network testnet`

You should see:

`_10

Result: "0"`

Test a transaction to increment the counter:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc --network testnet --signer testnet-account`

Run the script again to verify the increment worked:

`_10

flow scripts execute cadence/scripts/GetCounter.cdc --network testnet`

`_10

Result: "1"`

Perfect! Your Counter contract is now live on testnet and works correctly.

### Update frontend for testnet[​](#update-frontend-for-testnet "Direct link to Update frontend for testnet")

Now update your `Next.js` application to connect to testnet instead of the emulator.

**Update `src/app/layout.tsx`:**

`_27

'use client';

_27

_27

import { FlowProvider } from '@onflow/react-sdk';

_27

import flowJson from '../flow.json';

_27

_27

export default function RootLayout({

_27

children,

_27

}: {

_27

children: React.ReactNode;

_27

}) {

_27

return (

_27

<html>

_27

<body>

_27

<FlowProvider

_27

config={{

_27

accessNodeUrl: 'access.devnet.nodes.onflow.org:9000',

_27

flowNetwork: 'testnet',

_27

discoveryWallet: ' https://fcl-discovery.onflow.org/testnet/authn',

_27

}}

_27

flowJson={flowJson}

_27

>

_27

{children}

_27

</FlowProvider>

_27

</body>

_27

</html>

_27

);

_27

}`

**Key changes:**

* `accessNodeUrl`: Changed from localhost to Flow's testnet REST API.
* `flowNetwork`: Changed from 'emulator' to 'testnet'.
* `discoveryWallet`: Updated to use testnet wallet discovery.

### Test your testnet frontend[​](#test-your-testnet-frontend "Direct link to Test your testnet frontend")

Start your frontend application:

`_10

npm run dev`

Visit `http://localhost:3000` and you will see:

1. **Counter value**: Displays the current count from your testnet contract.
2. **Connect Wallet**: You can now connect with various Flow wallets (not just Dev Wallet).
3. **Increment functionality**: Transactions are sent to the live testnet.
4. **Real transaction costs**: Small amounts of testnet Flow are used for gas.

**Important**: When you connect your wallet, make sure to:

* Switch your wallet to Testnet network.
* Use an account that has testnet Flow tokens.
* Confirm you're interacting with the correct contract address.

## Deploy to mainnet[​](#deploy-to-mainnet "Direct link to Deploy to mainnet")

Mainnet deployment is the final step in your application's journey. Unlike testnet, mainnet uses real Flow tokens and serves real users, so additional security considerations and best practices are essential.

### Create a mainnet account[​](#create-a-mainnet-account "Direct link to Create a mainnet account")

For mainnet, you'll need to acquire Flow tokens through exchanges or other means, as there's no faucet.

**Option 1: Use Flow Wallet**

1. Download and install [Flow Wallet](https://wallet.flow.com/).
2. Create a new wallet and securely store your recovery phrase.
3. Purchase Flow tokens from a supported exchange.
4. Transfer tokens to your Flow Wallet.

**Option 2: Use Flow CLI**

`_10

flow accounts create --network mainnet`

When prompted:

1. **Account name**: Enter `mainnet-account`
2. **Select "Mainnet" Network**

### Acquire FLOW tokens[​](#acquire-flow-tokens "Direct link to Acquire FLOW tokens")

You can purchase Flow tokens from major exchanges like [Coinbase](https://www.coinbase.com/en-in/how-to-buy/flow), [Moonpay](https://www.moonpay.com/buy/flow), and [Binance](https://www.binance.com/en-IN/how-to-buy/flow).

To obtain Flow directly from the Flow Wallet, click "Buy" in your account.

![flow-wallet-icons](/assets/images/flow-wallet-icons-ce189e72f967cba8eadb9e8a5b9ba7d5.png)

Then, click on a provider to purchase FLOW.

![provider](/assets/images/provider-d9c0033cd40f0bfee9f4c4e82aea5296.png)

### Configure mainnet deployment[​](#configure-mainnet-deployment "Direct link to Configure mainnet deployment")

Add mainnet deployment configuration to your `flow.json`:

`_10

flow config add deployment --network mainnet`

Follow the prompts:

1. **Network**: `mainnet`
2. **Account**: `mainnet-account`
3. **Contract**: `Counter`
4. **Deploy more contracts**: `yes`
5. **Contract**: `NumberFormatter`

Your `flow.json` will now include mainnet configuration:

`_33

{

_33

"dependencies": {

_33

"NumberFormatter": {

_33

"source": "testnet://8a4dce54554b225d.NumberFormatter",

_33

"aliases": {

_33

"mainnet": "1654653399040a61",

_33

"testnet": "8a4dce54554b225d"

_33

}

_33

}

_33

},

_33

"deployments": {

_33

"emulator": {

_33

"default": [

_33

"Counter"

_33

],

_33

"emulator-account": [

_33

"NumberFormatter"

_33

]

_33

},

_33

"testnet": {

_33

"testnet-account": [

_33

"Counter",

_33

"NumberFormatter"

_33

]

_33

},

_33

"mainnet": {

_33

"mainnet-account": [

_33

"Counter",

_33

"NumberFormatter"

_33

]

_33

}

_33

}

_33

}`

### Deploy to mainnet[​](#deploy-to-mainnet-1 "Direct link to Deploy to mainnet")

Deploy your Counter contract to mainnet:

`_10

flow project deploy --network mainnet`

**⚠️ Important**: This deployment costs real FLOW tokens and you can't undo it.

You will see output similar to:

`_10

Deploying 2 contracts for accounts: mainnet-account

_10

_10

Counter -> 0xABC123DEF456789 (contract deployed successfully)

_10

NumberFormatter -> 0x123456789ABC (contract deployed successfully)

_10

_10

🎉 All contracts deployed successfully`

### Production frontend configuration[​](#production-frontend-configuration "Direct link to Production frontend configuration")

Create a production build of your frontend configured for mainnet:

**Update `src/app/layout.tsx` for production:**

`_27

'use client';

_27

_27

import { FlowProvider } from '@onflow/react-sdk';

_27

import flowJson from '../flow.json';

_27

_27

export default function RootLayout({

_27

children,

_27

}: {

_27

children: React.ReactNode;

_27

}) {

_27

return (

_27

<html>

_27

<body>

_27

<FlowProvider

_27

config={{

_27

accessNodeUrl: 'access.mainnet.nodes.onflow.org:9000',

_27

flowNetwork: 'mainnet',

_27

discoveryWallet: 'https://fcl-discovery.onflow.org/authn',

_27

}}

_27

flowJson={flowJson}

_27

>

_27

{children}

_27

</FlowProvider>

_27

</body>

_27

</html>

_27

);

_27

}`

Build your production frontend:

`_10

npm run build`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/getting-started/production-deployment.md)

Last updated on **Nov 14, 2025** by **0xLisanAlGaib**

[Previous

Building a Frontend App](/blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app)[Next

Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

###### Rate this page

😞😐😊

Copy as Markdown

* [What you'll learn](#what-youll-learn)* [Deploy to Testnet](#deploy-to-testnet)
    + [Understanding Flow networks](#understanding-flow-networks)+ [Create a testnet account](#create-a-testnet-account)+ [Fund your testnet account](#fund-your-testnet-account)+ [Configure testnet deployment](#configure-testnet-deployment)+ [Deploy Counter contract to testnet](#deploy-counter-contract-to-testnet)+ [Test your testnet deployment](#test-your-testnet-deployment)+ [Update frontend for testnet](#update-frontend-for-testnet)+ [Test your testnet frontend](#test-your-testnet-frontend)* [Deploy to mainnet](#deploy-to-mainnet)
      + [Create a mainnet account](#create-a-mainnet-account)+ [Acquire FLOW tokens](#acquire-flow-tokens)+ [Configure mainnet deployment](#configure-mainnet-deployment)+ [Deploy to mainnet](#deploy-to-mainnet-1)+ [Production frontend configuration](#production-frontend-configuration)

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