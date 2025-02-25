# Source: https://developers.flow.com/tools/clients/fcl-js

Flow Client Library (FCL) | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

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
* Flow Client Library (FCL)

On this page

# Flow Client Library (FCL)

The Flow Client Library (FCL) JS is a package used to interact with user wallets and the Flow blockchain. When using FCL for authentication, dapps are able to support all FCL-compatible wallets on Flow and their users without any custom integrations or changes needed to the dapp code.

It was created to make developing applications that connect to the Flow blockchain easy and secure. It defines a standardized set of communication patterns between wallets, applications, and users that is used to perform a wide variety of actions for your dapp. FCL also offers a full featured SDK and utilities to interact with the Flow blockchain.

While FCL itself is a concept and standard, FCL JS is the javascript implementation of FCL and can be used in both browser and server environments. All functionality for connecting and communicating with wallet providers is restricted to the browser. We also have FCL Swift implementation for iOS, see [FCL Swift](https://github.com/zed-io/fcl-swift) contributed by [@lmcmz](https://github.com/lmcmz).

---

## Getting Started[​](#getting-started "Direct link to Getting Started")

### Requirements[​](#requirements "Direct link to Requirements")

* Node version `v12.0.0 or higher`.

### Installation[​](#installation "Direct link to Installation")

To use the FCL JS in your application, install using **yarn** or **npm**

`_10

npm i -S @onflow/fcl`

`_10

yarn add @onflow/fcl`

#### Importing[​](#importing "Direct link to Importing")

**ES6**

`_10

import * as fcl from '@onflow/fcl';`

**Node.js**

`_10

const fcl = require('@onflow/fcl');`

---

## FCL for Dapps[​](#fcl-for-dapps "Direct link to FCL for Dapps")

#### Wallet Interactions[​](#wallet-interactions "Direct link to Wallet Interactions")

* *Wallet Discovery* and *Sign-up/Login*: Onboard users with ease. Never worry about supporting multiple wallets.
  Authenticate users with any [FCL compatible wallet](/tools/clients/fcl-js#current-wallet-providers).

`_10

// in the browser

_10

import * as fcl from '@onflow/fcl';

_10

_10

fcl.config({

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn', // Endpoint set to Testnet

_10

});

_10

_10

fcl.authenticate();`

![FCL Default Discovery UI](/assets/images/discovery-c2c95d28a66e86c570491a36e37e0afa.png)

> **Note**: A [Dapper Wallet](https://meetdapper.com/developers) developer account is required. To enable Dapper Wallet inside FCL, you need to [follow this guide](https://docs.meetdapper.com/quickstart).

* *Interact with smart contracts*: Authorize transactions via the user's chosen wallet
* *Prove ownership of a wallet address*: Signing and verifying user signed data

[Learn more about wallet interactions >](/tools/clients/fcl-js/api#wallet-interactions)

#### Blockchain Interactions[​](#blockchain-interactions "Direct link to Blockchain Interactions")

* *Query the chain*: Send arbitrary Cadence scripts to the chain and receive back decoded values

`_16

import * as fcl from '@onflow/fcl';

_16

_16

const result = await fcl.query({

_16

cadence: `

_16

access(all) fun main(a: Int, b: Int, addr: Address): Int {

_16

log(addr)

_16

return a + b

_16

}

_16

`,

_16

args: (arg, t) => [

_16

arg(7, t.Int), // a: Int

_16

arg(6, t.Int), // b: Int

_16

arg('0xba1132bc08f82fe2', t.Address), // addr: Address

_16

],

_16

});

_16

console.log(result); // 13`

* *Mutate the chain*: Send arbitrary transactions with your own signatures or via a user's wallet to perform state changes on chain.

`_14

import * as fcl from '@onflow/fcl';

_14

// in the browser, FCL will automatically connect to the user's wallet to request signatures to run the transaction

_14

const txId = await fcl.mutate({

_14

cadence: `

_14

import Profile from 0xba1132bc08f82fe2

_14

_14

transaction(name: String) {

_14

prepare(account: auth(BorrowValue) &Account) {

_14

account.storage.borrow<&{Profile.Owner}>(from: Profile.privatePath)!.setName(name)

_14

}

_14

}

_14

`,

_14

args: (arg, t) => [arg('myName', t.String)],

_14

});`

[Learn more about on-chain interactions >](/tools/clients/fcl-js/api#on-chain-interactions)

#### Utilities[​](#utilities "Direct link to Utilities")

* Get account details from any Flow address
* Get the latest block
* Transaction status polling
* Event polling
* Custom authorization functions

[Learn more about utilities >](/tools/clients/fcl-js/api#pre-built-interactions)

## Next Steps[​](#next-steps "Direct link to Next Steps")

See the [Flow App Quick Start](/build/getting-started/fcl-quickstart).

See the full [API Reference](/tools/clients/fcl-js/api) for all FCL functionality.

Learn Flow's smart contract language to build any script or transactions: [Cadence](https://cadence-lang.org/docs).

Explore all of Flow [docs and tools](/).

---

## FCL for Wallet Providers[​](#fcl-for-wallet-providers "Direct link to FCL for Wallet Providers")

Wallet providers on Flow have the flexibility to build their user interactions and UI through a variety of ways:

* Front channel communication via Iframe, pop-up, tab, or extension
* Back channel communication via HTTP

FCL is agnostic to the communication channel and is configured to create both custodial and non-custodial wallets. This enables users to interact with wallet providers without needing to download an app or extension.

The communication channels involve responding to a set of pre-defined FCL messages to deliver the requested information to the dapp. Implementing a FCL compatible wallet on Flow is as simple as filling in the responses with the appropriate data when FCL requests them. If using any of the front-channel communication methods, FCL also provides a set of [wallet utilities](https://github.com/onflow/fcl-js/blob/master/packages/fcl/src/wallet-utils/index.js) to simplify this process.

### Current Wallet Providers[​](#current-wallet-providers "Direct link to Current Wallet Providers")

* [Flow Wallet](https://wallet.flow.com/)
* [Dapper Wallet](https://www.meetdapper.com/)
* [Blocto](https://blocto.portto.io/en/)
* [NuFi](https://nu.fi)
* [Ledger](https://ledger.com) (limited transaction support)

### Wallet Discovery[​](#wallet-discovery "Direct link to Wallet Discovery")

It can be difficult to get users to discover new wallets on a chain. To solve this, we created a wallet discovery service that can be configured and accessed through FCL to display all available Flow wallet providers to the user. This means:

* Dapps can display and support all FCL compatible wallets that launch on Flow without needing to change any code
* Users don't need to sign up for new wallets - they can carry over their existing one to any dapp that uses FCL for authentication and authorization.

The discovery feature can be used via API, allowing you to customize your own UI or use the default UI without any additional configuration.

### Building a FCL compatible wallet[​](#building-a-fcl-compatible-wallet "Direct link to Building a FCL compatible wallet")

* Read the [wallet guide](https://github.com/onflow/fcl-js/blob/master/packages/fcl/src/wallet-provider-spec/draft-v3.md) to understand the implementation details.
* Review the architecture of the [Flow Dev Wallet](https://github.com/onflow/fcl-dev-wallet) for an overview.
* If building a non-custodial wallet, see the [Account API](https://github.com/onflow/flow-account-api) and the [FLIP](https://github.com/onflow/flow/pull/727) on derivation paths and key generation.

---

## Support[​](#support "Direct link to Support")

Notice an problem or want to request a feature? [Add an issue](https://github.com/onflow/fcl-js/issues).

Discuss FCL with the community on the [forum](https://forum.onflow.org/c/developer-tools/flow-fcl/22).

Join the Flow community on [Discord](https://discord.gg/flow) to keep up to date and to talk to the team.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/index.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Clients](/tools/clients)[Next

FCL Reference](/tools/clients/fcl-js/api)

###### Rate this page

😞😐😊

* [Getting Started](#getting-started)
  + [Requirements](#requirements)
  + [Installation](#installation)
* [FCL for Dapps](#fcl-for-dapps)
* [Next Steps](#next-steps)
* [FCL for Wallet Providers](#fcl-for-wallet-providers)
  + [Current Wallet Providers](#current-wallet-providers)
  + [Wallet Discovery](#wallet-discovery)
  + [Building a FCL compatible wallet](#building-a-fcl-compatible-wallet)
* [Support](#support)

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