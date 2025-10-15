# Source: https://developers.flow.com/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint

Sponsored Transactions EVM Endpoint | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    + [Sponsored Transactions EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)* Sponsored Transactions EVM Endpoint

On this page

# Gas Free EVM Endpoint

Gas fees are one of the biggest barriers to user adoption in blockchain applications. While Flow's native Cadence transactions support a separate fee payer role, EVM transactions require the sender to pay their own gas fees. This creates friction for users who need to acquire tokens before they can interact with your application.

Flow EVM's architecture provides a unique solution: you can set up a **gas-free EVM endpoint** that sponsors all transaction fees on behalf of your users. This enables seamless user experiences similar to traditional web applications, where users don't need to worry about transaction costs.

warning

This method only works in situations where you can control the RPC node used to **send** transactions, such as your backend, or if your frontend uses embedded wallets. It will **not** work on the frontend with traditional wallets, such as MetaMask.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Understand how Flow EVM's transaction model enables gas-free transactions
* Set up a custom EVM Gateway that sponsors all transaction fees
* Configure your application to use a gas-free RPC endpoint
* Implement sponsored transactions for various business scenarios
* Manage service accounts and keys for concurrent transaction processing

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

### Flow EVM and RPC Endpoints[​](#flow-evm-and-rpc-endpoints "Direct link to Flow EVM and RPC Endpoints")

This tutorial assumes you're familiar with [Flow EVM](/build/evm/using) and how RPC endpoints work. You should understand the difference between read and write operations, and how transactions are sent through RPC endpoints.

## Getting Started[​](#getting-started "Direct link to Getting Started")

This tutorial will guide you through setting up a gas-free EVM endpoint that sponsors all transaction fees for your users. The solution involves:

1. Creating a service account to act as the fee payer
2. Configuring a custom EVM Gateway with gas sponsorship enabled
3. Setting up your application to use the custom RPC endpoint

## Overview[​](#overview "Direct link to Overview")

If you've read [Using Flow EVM](/build/evm/using), you know that you use the RPC endpoint to send EVM transactions to the Flow EVM. The default RPC endpoint is actually the [EVM Gateway](https://github.com/onflow/flow-evm-gateway).

EVM transactions sent through the EVM Gateway are wrapped in a Flow Cadence transaction and sent to the Flow network. The Flow EVM Gateway's service account is the payer of that Cadence transaction.

info

In Cadence, the proposer, payer, and signer of a transaction are separate, natively.

For EVM transactions inside this Cadence transaction, the transaction fees of the EVM transaction are sent from the sender's account and applied to the EVM Gateway's service account. The EVM Gateway pays the Cadence transaction fee, but is reimbursed via the EVM transaction's gas fee, which is directed to its own EVM address as the *coinbase*.

Here are the key points of the Flow EVM Gateway:

* The EVM Gateway works as a proxy to send EVM transactions
* The EVM Gateway wraps EVM transactions into native Flow Cadence transactions
* The EVM Gateway has a service account, which is the payer and sender of all native transactions sent through the EVM Gateway
* The sender of the EVM transaction is the fee payer of its EVM transaction to the EVM Gateway's service account

### Why do we need a gas-free EVM endpoint?[​](#why-do-we-need-a-gas-free-evm-endpoint "Direct link to Why do we need a gas-free EVM endpoint?")

From the Flow [transaction model](/build/cadence/basics/transactions#Payer), we know that there is actually a Fee Payer role in native Flow transactions. When the transaction is executed, the fees for the transaction are entirely borne by the Fee Payer role. However, for EVM, the transaction model doesn't separate the signer from the payer. Therefore, when we execute transactions on the EVM, the transaction fees **must** be covered by the sender of the transaction.

If someone wants to send an EVM transaction through the default EVM Gateway, the sender's account must have enough balance to cover the transaction fees, unless they're using the Flow wallet, which also sponsors gas. Developers using embedded wallets, or holding user keys on the backend, may prefer to sponsor the transaction fees to create a more user-friendly experience, just as can be done in native Cadence transactions or paymaster solutions on other networks.

Here, we provide a solution: you can set up a sponsored transaction EVM endpoint for your backend service, and all transactions sent through this endpoint will be sponsored by your account.

### Who needs the gas-free EVM endpoint?[​](#who-needs-the-gas-free-evm-endpoint "Direct link to Who needs the gas-free EVM endpoint?")

Here are several typical business scenarios suitable for its use:

* Centralized exchanges that wish to improve internal transaction performance for users' deposits and withdrawals
* Apps with embedded wallets using social login that don't want to require users to deposit money in a new wallet before they're able to interact with the app
* Games needing to complete onchain tasks to onboard new players who wish to try the game
* Backends creating and managing large amounts of wallets on behalf of their users
* Businesses that wish to provide sponsored transactions as a service

As long as you can ensure that all your users' transactions are sent through a custom RPC endpoint, you can set up a gas-free EVM Gateway to enable gas-free transactions for your users.

## How to set up a gas-free EVM endpoint[​](#how-to-set-up-a-gas-free-evm-endpoint "Direct link to How to set up a gas-free EVM endpoint")

Most of the tasks you need to complete are in the guide to set up your own [Custom EVM Gateway](/protocol/node-ops/evm-gateway/evm-gateway-setup). In addition to those tasks, you'll need to:

1. Prepare a Service Account for the EVM Gateway to cover all transaction fees. Please refer to [Account Creation](/protocol/node-ops/evm-gateway/evm-gateway-setup#step-1---account-creation) for more details.
2. Add enough identical keys to the Service Account to support the concurrent signing of EVM transactions. This is very important because the EVM Gateway will use the Service Account to pay for the gas fees of the EVM transactions, so the Service Account needs to have enough keys to support the concurrent signing of EVM transactions. Please refer to [Account and Key Management](/protocol/node-ops/evm-gateway/evm-gateway-setup#account-and-key-management) for more details.
3. Set the correct environment variables for the EVM Gateway to enable the gas-free feature. Adjust the environment variables in the [Run the gateway](/protocol/node-ops/evm-gateway/evm-gateway-setup#run-the-gateway) section as follows:

* `COINBASE`: The address used to accept EVM transaction fees. In this case, there won't be fees to accept because all fees will be covered by the service account. Regardless, you need to set it with a valid address to ensure the EVM Gateway can start.
* `COA_ADDRESS`: This is the service account address, which will be used to pay for the gas fees of the EVM transactions. Please input the address of the Service Account you created in step 1, but without the `0x` prefix.
  + **Fund this address** to cover transaction fees.
* `COA_KEY`: You need to set the private key of the Service Account you created in step 1.
* `GAS_PRICE`: **Critical**: set this to `0` to ensure the linked service account will pay for transactions on users' behalf.

4. Follow the full guide of [Custom EVM Gateway](/protocol/node-ops/evm-gateway/evm-gateway-setup) to complete the EVM gateway setup with these adjustments, and you will get a custom RPC endpoint that will sponsor 100% of the gas fees for any EVM transaction sent through it.

## Configure the RPC Gateway[​](#configure-the-rpc-gateway "Direct link to Configure the RPC Gateway")

If you're using an embedded wallet solution, such as [Dynamic](https://www.dynamic.xyz/) or [Privy](https://www.privy.io/), you can set which RPC endpoint your app uses to read **and write** transactions. If your users are using browser extension wallets, your selected RPC is **only** used for read calls.

With [Wagmi](https://wagmi.sh/), you can configure a custom endpoint in your `config`:

`_10

const config = createConfig({

_10

chains: [flowMainnet, flowTestnet],

_10

transports: {

_10

[flowMainnet.id]: http('https://your-evm-endpoint.com'),

_10

[flowTestnet.id]: http('https://your-testnet-evm-endpoint.com'),

_10

},

_10

});`

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, we've explored how to set up a gas-free EVM endpoint for your backend service. This solution provides several significant benefits:

1. **Enhanced User Experience**: Users can execute EVM transactions without worrying about gas fees, making the platform more accessible and user-friendly
2. **Business Flexibility**: Service providers can cover transaction costs on behalf of their users
3. **Cost Management**: By centralizing gas fee payments through a service account, businesses can better manage and control their transaction costs

The implementation requires careful setup of a service account with sufficient keys for concurrent transactions and proper configuration of the EVM Gateway environment variables. While this solution requires more initial setup compared to using the default EVM Gateway, the benefits of providing a gas-free experience to users can significantly enhance your platform's usability and adoption.

Remember that this solution is most effective when you can ensure all user transactions are routed through your custom RPC endpoint. This makes it particularly suitable for centralized services and applications where you have control over the transaction routing.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint.md)

Last updated on **Sep 11, 2025** by **Brian Doyle**

[Previous

Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)[Next

Third-Party Integrations](/blockchain-development-tutorials/integrations)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)* [Prerequisites](#prerequisites)
    + [Flow EVM and RPC Endpoints](#flow-evm-and-rpc-endpoints)* [Getting Started](#getting-started)* [Overview](#overview)
        + [Why do we need a gas-free EVM endpoint?](#why-do-we-need-a-gas-free-evm-endpoint)+ [Who needs the gas-free EVM endpoint?](#who-needs-the-gas-free-evm-endpoint)* [How to set up a gas-free EVM endpoint](#how-to-set-up-a-gas-free-evm-endpoint)* [Configure the RPC Gateway](#configure-the-rpc-gateway)* [Conclusion](#conclusion)

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