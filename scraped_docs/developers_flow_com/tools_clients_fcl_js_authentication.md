# Source: https://developers.flow.com/tools/clients/fcl-js/authentication

Authentication | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* Authentication

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

import * as fcl from "@onflow/fcl"

_10

_10

const currentUser = await fcl.currentUser.snapshot()

_10

console.log("The Current User:", currentUser)`

### Subscribe to the Current User[​](#subscribe-to-the-current-user "Direct link to Subscribe to the Current User")

`_10

import * as fcl from "@onflow/fcl"

_10

_10

// Returns an unsubscribe function

_10

const unsubscribe = fcl.currentUser.subscribe(currentUser => {

_10

console.log("The Current User:", currentUser)

_10

})`

# Authenticating and Unauthenticating

The TL;DR: Call `fcl.authenticate()` to log in and `fcl.unauthenticate()` to log out.

On Flow mainnet, no additional configuration is needed—your app’s users will go through the authentication process and be able to use any FCL-compatible wallet provider.

During development, you’ll likely want to configure your app to use [`@onflow/dev-wallet`](https://github.com/onflow/fcl-dev-wallet). The [Quick Start](/build/getting-started/fcl-quickstart) guide will walk you through setting it up.

We also recommend using the [FCL Discovery Service](/tools/clients/fcl-js/discovery) to help users discover and connect to FCL-compatible wallets.

Whether you're new to building onchain, or an established veteran, we’re here to help. If you run into any issues, reach out to us on [Discord](https://discord.gg/flow) — we’re happy to assist!

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/authentication.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

SDK Reference](/tools/clients/fcl-js/sdk-guidelines)[Next

How to Configure FCL](/tools/clients/fcl-js/configure-fcl)

###### Rate this page

😞😐😊

* [Snapshot of the Current User](#snapshot-of-the-current-user)
* [Subscribe to the Current User](#subscribe-to-the-current-user)

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