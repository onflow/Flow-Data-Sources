# Source: https://developers.flow.com/build/tools/clients/fcl-js/authentication

Authentication | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [@onflow/react-sdk](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)* [WalletConnect 2.0 Manual Configuration](/build/tools/clients/fcl-js/wallet-connect)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Authentication

On this page

# Authentication

Authentication in FCL is closely tied to the concept of `currentUser`. In fact, `fcl.authenticate` and `fcl.unauthenticate` are simply aliases for `fcl.currentUser.authenticate()` and `fcl.currentUser.unauthenticate()`, respectively. So, let’s take a closer look at `currentUser`.

As an onchain app developer using FCL, the primary authentication functionalities revolve around:

* Determining the `currentUser` and whether they are logged in.
* Logging a user in.
* Logging a user out.

Due to the way FCL works, logging in and signing up are essentially the same process.

# Retrieving Information About the Current User

FCL provides two ways to get information about the current user:

1. **A promise-based method** that returns a snapshot of the user’s data.
2. **A subscription-based method** that triggers a callback function with the latest user information whenever it changes.

### Snapshot of the Current User[​](#snapshot-of-the-current-user "Direct link to Snapshot of the Current User")

`_10

import * as fcl from '@onflow/fcl';

_10

_10

const currentUser = await fcl.currentUser.snapshot();

_10

console.log('The Current User:', currentUser);`

### Subscribe to the Current User[​](#subscribe-to-the-current-user "Direct link to Subscribe to the Current User")

`_10

import * as fcl from '@onflow/fcl';

_10

_10

// Returns an unsubscribe function

_10

const unsubscribe = fcl.currentUser.subscribe((currentUser) => {

_10

console.log('The Current User:', currentUser);

_10

});`

# Authenticating and Unauthenticating

The TL;DR: Call `fcl.authenticate()` to log in and `fcl.unauthenticate()` to log out.

On Flow mainnet, no additional configuration is needed—your app’s users will go through the authentication process and be able to use any FCL-compatible wallet provider.

During development, you’ll likely want to configure your app to use [`@onflow/dev-wallet`](https://github.com/onflow/fcl-dev-wallet). The [Quick Start](/blockchain-development-tutorials/cadence/getting-started) guide will walk you through setting it up.

We also recommend using the [FCL Discovery Service](/build/tools/clients/fcl-js/discovery) to help users discover and connect to FCL-compatible wallets.

Whether you're new to building onchain, or an established veteran, we’re here to help. If you run into any issues, reach out to us on [Discord](https://discord.gg/flow) — we’re happy to assist!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/authentication.md)

Last updated on **Sep 24, 2025** by **Felipe Cevallos**

[Previous

Type Definitions](/build/tools/clients/fcl-js/packages-docs/types)[Next

How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)

###### Rate this page

😞😐😊

Copy as Markdown

* [Snapshot of the Current User](#snapshot-of-the-current-user)* [Subscribe to the Current User](#subscribe-to-the-current-user)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.