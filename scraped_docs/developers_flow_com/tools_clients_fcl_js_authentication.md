# Source: https://developers.flow.com/tools/clients/fcl-js/authentication




Authentication | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)


* [Clients](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* Authentication
On this page
# Authentication

The concept of authentication in FCL is tied closely to FCL's concept of `currentUser`. In fact `fcl.authenticate` and `fcl.unauthenticate` are both aliases to `fcl.currentUser.authenticate()` and `fcl.currentUser.unauthenticate()` respectively. So let's look at `currentUser`.

As a dapp developer, using FCL, our current thought is to enable three main pieces of functionality.

* How to know the `currentUser` and if they are logged in.
* How to log a user in.
* How to log a user out.

Due to the nature of how FCL works, logging a user in and signing a user up are the same thing.

# Knowing things about the current user

FCL provides two ways of getting the current users information. One way is a promise that returns a snapshot of the info, while the other way allows you to subscribe to info, calling a callback function with the latest info anytime it changes.

### Snapshot of Current User[​](#snapshot-of-current-user "Direct link to Snapshot of Current User")

 `_10import * as fcl from "@onflow/fcl"_10_10const currentUser = await fcl.currentUser.snapshot()_10console.log("The Current User", currentUser)`
### Subscribe to Current User[​](#subscribe-to-current-user "Direct link to Subscribe to Current User")

 `_10import * as fcl from "@onflow/fcl"_10_10// Returns an unsubscribe function_10const unsubscribe = fcl.currentUser.subscribe(currentUser => {_10 console.log("The Current User", currentUser)_10})`
# Actually Authenticating and Unauthenticating

The TL;DR is to call `fcl.authenticate()` and `fcl.unauthenticate()` respectively.

On Flow mainnet, you wont even need to configure anything for this to work, the users of your dapp will go through the authentication process and be able to use any FCL compatible wallet providers.

During development you will probably want to configure your dapp to use [`@onflow/dev-wallet`](https://github.com/onflow/fcl-dev-wallet).
The [Quick Start](/build/getting-started/fcl-quickstart) guide will walk you through using it.

We know this can all be fairly overwhelming, we are committed to help though. If you run into any problems, reach out to us on [Discord](https://discord.gg/flow), we are more than happy to help out.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/authentication.md)Last updated on **Jan 23, 2025** by **Brian Doyle**[PreviousSDK Reference](/tools/clients/fcl-js/sdk-guidelines)[NextHow to Configure FCL](/tools/clients/fcl-js/configure-fcl)
###### Rate this page

😞😐😊

* [Snapshot of Current User](#snapshot-of-current-user)
* [Subscribe to Current User](#subscribe-to-current-user)
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

