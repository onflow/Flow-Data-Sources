# Source: https://developers.flow.com/tools/clients/fcl-js/transactions




Transactions | Flow Developer Portal





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
* Transactions
# Transactions

Transactions let you send Cadence code to the Flow blockchain that permanently alters its state.

We are assuming you have read the [Scripts Documentation](/tools/clients/fcl-js/scripts) before this, as transactions are sort of scripts with more required things.

While `query` is used for sending scripts to the chain, `mutate` is used for building and sending transactions. Just like [scripts](/tools/clients/fcl-js/scripts), `fcl.mutate` is a [JavaScript Tagged Template Literal](https://styled-components.com/docs/advanced#tagged-template-literals) that we can pass Cadence code into.

Unlike scripts, they require a little more information, things like a proposer, authorizations and a payer, which may be a little confusing and overwhelming.

# Sending your first Transaction

There is a lot to unpack in the following code snippet.
It sends a transaction to the Flow blockchain. For the transaction, the current user is authorizing it as both the `proposer` and the `payer`.
Something that is unique to Flow is the one paying for the transaction doesn't always need to be the one performing the transaction.
Proposers and Payers are special kinds of authorizations that are always required for a transaction.
The `proposer` acts similar to the `nonce` in Ethereum transactions, and helps prevent repeat attacks.
The `payer` is who will be paying for the transaction.
If these are not set, FCL defaults to using the current user for all roles.

`fcl.mutate` will return a `transactionId`. We can pass the response directly to `fcl.tx` and then use the `onceSealed` method which resolves a promise when the transaction is sealed.

 `_17import * as fcl from "@onflow/fcl"_17_17const transactionId = await fcl.mutate({_17 cadence: `_17 transaction {_17 execute {_17 log("Hello from execute")_17 }_17 }_17 `,_17 proposer: fcl.currentUser,_17 payer: fcl.currentUser,_17 limit: 50_17})_17_17const transaction = await fcl.tx(transactionId).onceSealed()_17console.log(transaction) // The transactions status and events after being sealed`
# Authorizing a transaction

The below code snippet is the same as the above one, except for one extremely important difference.
Our Cadence code this time has a prepare statement, and we are using the `fcl.currentUser` when constructing our transaction.

The `prepare` statement's arguments directly map to the order of the authorizations in the `authorizations` array.
Four authorizations means four `&Account`s as arguments passed to `prepare`. In this case though there is only one, and it is the `currentUser`.

These authorizations are important as you can only access/modify an accounts storage if you have the said accounts authorization.

 `_21import * as fcl from "@onflow/fcl"_21_21const transactionId = await fcl.mutate({_21 cadence: `_21 transaction {_21 prepare(acct: &Account) {_21 log("Hello from prepare")_21 }_21 execute {_21 log("Hello from execute")_21 }_21 }_21 `,_21 proposer: fcl.currentUser,_21 payer: fcl.currentUser,_21 authorizations: [fcl.currentUser],_21 limit: 50_21})_21_21const transaction = await fcl.tx(transactionId).onceSealed()_21console.log(transaction) // The transactions status and events after being sealed`

To learn more about `mutate`, check out the [API documentation](/tools/clients/fcl-js/api#mutate).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/transactions.md)Last updated on **Jan 27, 2025** by **j pimmel**[PreviousScripts](/tools/clients/fcl-js/scripts)[NextSigning and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)Documentation

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

