# Source: https://developers.flow.com/build/basics/flow-token

FLOW Coin | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)

  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [MEV Resistance](/build/basics/mev-resistance)
  + [Events](/build/basics/events)
  + [FLOW Coin](/build/basics/flow-token)
  + [Smart Contracts ↙](/build/basics/smart-contracts)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Flow Protocol
* FLOW Coin

On this page

# FLOW Coin

## Introduction[​](#introduction "Direct link to Introduction")

This section contains information about the FLOW Coin for individual backers, wallet providers, custodians and node operators.

### FLOW as a Native Coin[​](#flow-as-a-native-coin "Direct link to FLOW as a Native Coin")

FLOW is the default coin for the Flow protocol, meaning it is used for all protocol-level fee payments,
rewards and staking transactions. FLOW implements the standard [Flow Fungible Token interface](https://github.com/onflow/flow-ft),
which all other on-chain fungible tokens also conform to. This interface is defined in Cadence,
Flow's native smart-contract programming language, which makes it easy to write applications that
interact with FLOW.

## How to Get FLOW[​](#how-to-get-flow "Direct link to How to Get FLOW")

There are two ways to acquire FLOW Coins as yield:

1. [Earn FLOW as a Validator or Delegator](/networks/staking/technical-overview): Receive newly-minted FLOW as a reward for running a node.
2. [Earn FLOW as a Community Contributor](https://github.com/onflow/developer-grants): Flow offers grants for selected proposals as well as RFPs for teams to submit proposals for funded development

## How to Use FLOW[​](#how-to-use-flow "Direct link to How to Use FLOW")

With FLOW, you can:

* Spend
* Stake
* Delegate
* Hold
* Vote
* Send and share
* Create, develop, and grow your dapp

### Spending FLOW[​](#spending-flow "Direct link to Spending FLOW")

All you need to spend FLOW is an account and a tool for signing transactions
(a wallet, custodian, or other signing service).
The FCL (Flow Client Library) makes it super duper easy to go to any dapp,
login with your account, have a great time,
and then sign with the wallet of your choice only once you decide to make a purchase.

### Staking FLOW[​](#staking-flow "Direct link to Staking FLOW")

[You can use FLOW to operate a staked node.](/networks/staking/technical-overview) Node operators receive newly-minted FLOW
as a reward for helping to secure the network.

### Delegating FLOW[​](#delegating-flow "Direct link to Delegating FLOW")

[You can use FLOW for stake delegation.](/networks/staking/technical-overview) Delegators receive newly-minted FLOW
as a reward for helping to secure the network.

### Holding FLOW[​](#holding-flow "Direct link to Holding FLOW")

If you have already purchased FLOW and wish to hold it, you have a couple of options:

* For relatively small, short term holdings - most people use a wallet.
  Wallets are used to help you sign transactions (verify your actions) when using your FLOW tokens.
* For larger, long term holdings - you may want to use a custody provider to keep your funds safe.

You can find wallets and custodians supporting Flow in the [Flow Port](https://port.onflow.org/)

### Voting with FLOW[​](#voting-with-flow "Direct link to Voting with FLOW")

Participating in the Flow community is more than just running a node or building a dapp.
It's also about engaging in discussion, debate, and decision making about the protocol,
the content on it, and the people impacted by it.
You can use your Flow account to submit votes to community polls and other governance related activities.

### Sending and Sharing FLOW[​](#sending-and-sharing-flow "Direct link to Sending and Sharing FLOW")

If you simply want to share the love and bring your friends to Flow, it's easier than an edible arrangement.

It is possible to use the Flow blockchain without holding any FLOW coins yourself.
Free to play games, trials, community polls,
and other community activities can all take place with only an account
(which may be created on a person's behalf)
and a small fixed fee which may be paid by a user agent.

The protocol requires some FLOW coins to process these transactions,
but (and this is the cool part!) a product can support users who do not themselves hold FLOW
while still providing that user with all the underlying security guarantees the Flow protocol provides.

Transferring FLOW, creating accounts, and updating keys are all actions made easy on [Flow Port](https://port.flow.com/)

### Submitting Transactions and Updating Users[​](#submitting-transactions-and-updating-users "Direct link to Submitting Transactions and Updating Users")

Transactions are submitted using a Flow SDK via the Access API.

On Flow, a transaction is identified by its hash - the hash that exists as soon as that transaction is signed and submitted to an Access or Collection node.
Results of transactions can be queried by transaction hash through the Access API.
A user can check the status of a transaction at any time via the [Flow Block Explorer](https://flowscan.io/).

To expose these results natively in your app, you can use a Flow SDK to fetch transaction results,
[for example using the Flow Go SDK](https://github.com/onflow/flow-go-sdk#querying-transaction-results).

Using a Flow SDK you can also fetch account state by address from a Flow Access API,
[for example using the Flow Go SDK](https://github.com/onflow/flow-go-sdk#querying-accounts).

Once the transaction is sealed, an event is emitted and you will be able to read transaction events and update the user.

The Flow SDKs also allow polling for events using the Flow Access API,
[for example using the Flow Go SDK](https://github.com/onflow/flow-go-sdk#querying-events).

## How to Build with FLOW[​](#how-to-build-with-flow "Direct link to How to Build with FLOW")

To get started building on Flow, please see the [Flow App Quickstart](/build/getting-started/fcl-quickstart)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/flow-token.md)

Last updated on **Mar 31, 2025** by **Josh Hannan**

[Previous

Events](/build/basics/events)[Next

Smart Contracts ↙](/build/basics/smart-contracts)

###### Rate this page

😞😐😊

* [Introduction](#introduction)
  + [FLOW as a Native Coin](#flow-as-a-native-coin)
* [How to Get FLOW](#how-to-get-flow)
* [How to Use FLOW](#how-to-use-flow)
  + [Spending FLOW](#spending-flow)
  + [Staking FLOW](#staking-flow)
  + [Delegating FLOW](#delegating-flow)
  + [Holding FLOW](#holding-flow)
  + [Voting with FLOW](#voting-with-flow)
  + [Sending and Sharing FLOW](#sending-and-sharing-flow)
  + [Submitting Transactions and Updating Users](#submitting-transactions-and-updating-users)
* [How to Build with FLOW](#how-to-build-with-flow)

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