# Source: https://developers.flow.com/build/tools/clients/fcl-js/transactions

Transactions | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                          * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                                * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Transactions

On this page

# Transactions

Transactions let you send Cadence code to the Flow blockchain that permanently alters its state.

We assume you have read the [Scripts Documentation](/build/tools/clients/fcl-js/scripts): ./scripts.md before this, as transactions are sort of scripts with more required things.

While `query` is used to send scripts to the chain, `mutate` is used to build and send transactions. Just like [scripts](/build/tools/clients/fcl-js/scripts), `fcl.mutate` is a [JavaScript Tagged Template Literal](https://styled-components.com/docs/advanced#tagged-template-literals) that we can pass Cadence code into.

Unlike scripts, they require a little more information, things like a proposer, authorizations and a payer, which may be a little confusing and overwhelming.

## Send your first transaction[​](#send-your-first-transaction "Direct link to Send your first transaction")

There is a lot to unpack in the following code snippet. It sends a transaction to the Flow blockchain. For the transaction, the current user authorizes it as both the `proposer` and the `payer`.

Something that is unique to Flow is the one who pays for the transaction doesn't always need to be the one who performs the transaction. Proposers and Payers are special kinds of authorizations that are always required for a transaction.

* The `proposer` acts similar to the `nonce` in Ethereum transactions, and helps prevent repeat attacks.
* The `payer` is who will be paying for the transaction.
  If these are not set, Flow Client Library (FCL) defaults to the current user for all roles.

`fcl.mutate` will return a `transactionId`. We can pass the response directly to `fcl.tx` and then use the `onceExecuted` method which resolves a promise when a transaction result is available.

`` _17

import * as fcl from '@onflow/fcl';

_17

_17

const transactionId = await fcl.mutate({

_17

cadence: `

_17

transaction {

_17

execute {

_17

log("Hello from execute")

_17

}

_17

}

_17

`,

_17

proposer: fcl.currentUser,

_17

payer: fcl.currentUser,

_17

limit: 50,

_17

});

_17

_17

const transaction = await fcl.tx(transactionId).onceExecuted();

_17

console.log(transaction); // The transactions status and events after being executed ``

## Authorize a transaction[​](#authorize-a-transaction "Direct link to Authorize a transaction")

The below code snippet is the same as the above one, except for one extremely important difference. Our Cadence code this time has a prepare statement, and we use the `fcl.currentUser` when constructing our transaction.

The `prepare` statement's arguments directly map to the order of the authorizations in the `authorizations` array. Four authorizations means four `&Account`s as arguments passed to `prepare`. In this case though there is only one, and it is the `currentUser`.

These authorizations are important as you can only access or modify an account's storage if you have that account's authorization.

`` _21

import * as fcl from '@onflow/fcl';

_21

_21

const transactionId = await fcl.mutate({

_21

cadence: `

_21

transaction {

_21

prepare(acct: &Account) {

_21

log("Hello from prepare")

_21

}

_21

execute {

_21

log("Hello from execute")

_21

}

_21

}

_21

`,

_21

proposer: fcl.currentUser,

_21

payer: fcl.currentUser,

_21

authorizations: [fcl.currentUser],

_21

limit: 50,

_21

});

_21

_21

const transaction = await fcl.tx(transactionId).onceExecuted();

_21

console.log(transaction); // The transactions status and events after being executed ``

To learn more about `mutate`, check out the [API documentation](/build/tools/clients/fcl-js/packages-docs/fcl/mutate).

## Query transaction results[​](#query-transaction-results "Direct link to Query transaction results")

When you query transaction results (for example, via HTTP/REST endpoints like `GET /v1/transaction_results/{id}`), you can provide either:

* A **transaction ID** (256-bit hash as hex string).
* A **scheduled transaction ID** (UInt64 as decimal string).

The returned result always includes `transaction_id` as the underlying native transaction ID. For scheduled transactions, this will be the system transaction ID that executed the scheduled callback.

Learn more about [Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions).

## Transaction finality[​](#transaction-finality "Direct link to Transaction finality")

As of **FCL v1.15.0**, it is now recommended to use use `onceExecuted` in most cases, which leads to a 2.5x reduction in latency when you wait for a transaction result. For example, the following code snippet should be updated from:

`_10

import * as fcl from '@onflow/fcl';

_10

const result = await fcl.tx(txId).onceSealed();`

to:

`_10

import * as fcl from '@onflow/fcl';

_10

const result = await fcl.tx(txId).onceExecuted();`

Developers who manually subscribe to transaction statuses should update their listeners to treat "executed" as the final status (see the [release notes](https://github.com/onflow/fcl-js/releases/tag/%40onflow%2Ffcl%401.15.0)). For example, the following code snippet should be updated from:

`_10

import * as fcl from '@onflow/fcl';

_10

import { TransactionExecutionStatus } from '@onflow/typedefs';

_10

_10

fcl.tx(txId).subscribe((txStatus) => {

_10

if (txStatus.status === TransactionExecutionStatus.SEALED) {

_10

console.log('Transaction executed!');

_10

}

_10

});`

`_11

import * as fcl from '@onflow/fcl';

_11

import { TransactionExecutionStatus } from '@onflow/typedefs';

_11

_11

fcl.tx(txId).subscribe((txStatus) => {

_11

if (

_11

// SEALED status is no longer necessary

_11

txStatus.status === TransactionExecutionStatus.EXECUTED

_11

) {

_11

console.log('Transaction executed!');

_11

}

_11

});`

The "executed" status corresponds to soft finality, which indicates that the transaction has been included in a block and a transaction status is available, backed by a cryptographic proof. Only in rare cases should a developer need to wait for "sealed" status in their applications and you can learn more about the different transaction statuses on Flow [here](/build/cadence/basics/transactions#transaction-status).

See the following video for demonstration of how to update your code to wait for "executed" status:

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/transactions.md)

Last updated on **Dec 9, 2025** by **cshannon1218**

[Previous

Scripts](/build/tools/clients/fcl-js/scripts)[Next

Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)

###### Rate this page

😞😐😊

Copy as Markdown

* [Send your first transaction](#send-your-first-transaction)* [Authorize a transaction](#authorize-a-transaction)* [Query transaction results](#query-transaction-results)* [Transaction finality](#transaction-finality)

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