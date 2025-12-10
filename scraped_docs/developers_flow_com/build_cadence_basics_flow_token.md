# Source: https://developers.flow.com/build/cadence/basics/flow-token

FLOW Coin | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          - [Network Architecture ↗️](/build/cadence/basics/network-architecture)- [Blocks](/build/cadence/basics/blocks)- [Collections](/build/cadence/basics/collections)- [Accounts](/build/cadence/basics/accounts)- [Transactions](/build/cadence/basics/transactions)- [Scripts](/build/cadence/basics/scripts)- [Fees](/build/cadence/basics/fees)- [MEV Resistance](/build/cadence/basics/mev-resistance)- [Events](/build/cadence/basics/events)- [FLOW Coin](/build/cadence/basics/flow-token)- [Smart Contracts ↙](/build/cadence/basics/smart-contracts)+ [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Basics* FLOW Coin

On this page

# FLOW Coin

This section contains information about the FLOW Coin for individual backers, wallet providers, custodians and node operators.

### FLOW as a Native Coin[​](#flow-as-a-native-coin "Direct link to FLOW as a Native Coin")

FLOW is the default coin for the Flow protocol, meaning it is used for all protocol-level fee payments, rewards and staking transactions. FLOW implements the standard [Flow Fungible Token interface](https://github.com/onflow/flow-ft), which all other onchain fungible tokens also conform to. This interface is defined in Cadence, Flow's native smart-contract programming language, which makes it easy to write applications that interact with FLOW.

## How to Get FLOW[​](#how-to-get-flow "Direct link to How to Get FLOW")

There are two ways to acquire FLOW Coins as yield:

1. [Earn FLOW as a Validator or Delegator](/protocol/staking/technical-overview): Receive newly-minted FLOW as a reward when you run a node.
2. [Earn FLOW as a Community Contributor](https://github.com/onflow/developer-grants): Flow offers grants for selected proposals as well as RFPs for teams to submit proposals for funded development

## How to use FLOW[​](#how-to-use-flow "Direct link to How to use FLOW")

With FLOW, you can:

* Spend
* Stake
* Delegate
* Hold
* Vote
* Send and share
* Create, develop, and grow your dapp

### Spend FLOW[​](#spend-flow "Direct link to Spend FLOW")

All you need to spend FLOW is an account and a tool to sign transactions (a wallet, custodian, or other signing service). The FCL (Flow Client Library) makes it super duper easy to go to any dapp, login with your account, have a great time, and then sign with the wallet of your choice only once you decide to make a purchase.

### Stake FLOW[​](#stake-flow "Direct link to Stake FLOW")

[You can use FLOW to operate a staked node.](/protocol/staking/technical-overview) Node operators receive newly-minted FLOW as a reward for helping to secure the network.

### Delegate FLOW[​](#delegate-flow "Direct link to Delegate FLOW")

[You can use FLOW for stake delegation.](/protocol/staking/technical-overview) Delegators receive newly-minted FLOW as a reward for helping to secure the network.

### Hold FLOW[​](#hold-flow "Direct link to Hold FLOW")

If you have already purchased FLOW and wish to hold it, you have a couple of options:

* For relatively small, short term holdings - most people use a wallet.
  Wallets are used to help you sign transactions (verify your actions) when you use your FLOW tokens.
* For larger, long term holdings - you may want to use a custody provider to keep your funds safe.

You can find wallets and custodians that support Flow in the [Flow Port](https://port.flow.com/)

### Vote with FLOW[​](#vote-with-flow "Direct link to Vote with FLOW")

Participation in the Flow community means more than just run a node or build a dapp. It's also about engaging in discussion, debate, and decision making about the protocol, the content on it, and the people that it impacts. You can use your Flow account to submit votes to community polls and other governance related activities.

### Send and share FLOW[​](#send-and-share-flow "Direct link to Send and share FLOW")

If you simply want to share the love and bring your friends to Flow, it's easier than an edible arrangement.

It is possible to use the Flow blockchain and not hold any FLOW coins yourself. Free to play games, trials, community polls, and other community activities can all take place with only an account (which may be created on a person's behalf) and a small fixed fee which may be paid by a user agent.

The protocol requires some FLOW coins to process these transactions, but (and this is the cool part!) a product can support users who do not themselves hold FLOW and still provide that user with all the underlying security guarantees the Flow protocol provides.

It's easy to transfer FLOW, create accounts, and update keys on [Flow Port](https://port.flow.com/)

### Submit transactions and update users[​](#submit-transactions-and-update-users "Direct link to Submit transactions and update users")

Transactions are submitted with a Flow SDK via the Access API.

On Flow, a transaction is identified by its hash - the hash that exists as soon as that transaction is signed and submitted to an Access or Collection node. Results of transactions can be queried by transaction hash through the Access API. A user can check the status of a transaction at any time via the [Flow Block Explorer](https://flowscan.io/).

To expose these results natively in your app, you can use a Flow SDK to [fetch transaction results](https://github.com/onflow/flow-go-sdk#querying-transaction-results).

With a Flow SDK, you can also [fetch account state by address](https://github.com/onflow/flow-go-sdk#querying-accounts) from a Flow Access API.

After the transaction is sealed, an event is emitted and you will be able to read transaction events and update the user.

The Flow SDKs also allow [polling for events] with the Flow Access API.

## How to build with FLOW[​](#how-to-build-with-flow "Direct link to How to build with FLOW")

To get started with Flow, see the [Flow App Quickstart]

[polling for events]: <https://github.com/onflow/flow-go-sdk#querying-events>)
[Flow App Quickstart]: ../../../blockchain-development-tutorials/cadence/getting-started/building-a-frontend-app.md

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/basics/flow-token.md)

Last updated on **Dec 2, 2025** by **cshannon1218**

[Previous

Events](/build/cadence/basics/events)[Next

Smart Contracts ↙](/build/cadence/basics/smart-contracts)

###### Rate this page

😞😐😊

Copy as Markdown

* [FLOW as a Native Coin](#flow-as-a-native-coin)* [How to Get FLOW](#how-to-get-flow)* [How to use FLOW](#how-to-use-flow)
      + [Spend FLOW](#spend-flow)+ [Stake FLOW](#stake-flow)+ [Delegate FLOW](#delegate-flow)+ [Hold FLOW](#hold-flow)+ [Vote with FLOW](#vote-with-flow)+ [Send and share FLOW](#send-and-share-flow)+ [Submit transactions and update users](#submit-transactions-and-update-users)* [How to build with FLOW](#how-to-build-with-flow)

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