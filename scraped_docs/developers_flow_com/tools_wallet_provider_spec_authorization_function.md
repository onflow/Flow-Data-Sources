# Source: https://developers.flow.com/tools/wallet-provider-spec/authorization-function




Authorization Function | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [Flow Emulator](/tools/emulator)
* [Clients](/tools/clients)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
  + [Authorization Function](/tools/wallet-provider-spec/authorization-function)
  + [Introduction](/tools/wallet-provider-spec/custodial)
  + [Provable Authn](/tools/wallet-provider-spec/provable-authn)
  + [User Signature](/tools/wallet-provider-spec/user-signature)


* [Wallet Provider Spec](/tools/wallet-provider-spec)
* Authorization Function
On this page
# Authorization Function

## Overview[​](#overview "Direct link to Overview")

An Authorization Function is a function which enables the JS-SDK and FCL to know which Flow account fulfills which signatory role in a transaction and how to recieve a signature on behalf of the supplied account.

## How to Use an Authorization Function[​](#how-to-use-an-authorization-function "Direct link to How to Use an Authorization Function")

An authorization function is a function that you may use in place of an authorization in the Flow JS-SDK and FCL. An authorization is a concept that is used when denoting a proposer, payer or authorizer for a transaction. An authorization can either be a data structure represenating an authorization, or a function which when called returns an authorization called an Authorization Function. In this document we discuss the latter.

To use an Authorization Function, you specify that Authorization Function as the authorization for a proposer, payer or authorizer for a transaction.

> `fcl.currentUser().authorization` which is aliased to `fcl.authz` is itself an authorization function. It tells the underlying js-sdk the current users flow account will be used for the signatory role and supplies a signing function that enables the application to request a signature from the users wallet.

Example 1:

 `_10import * as fcl from "@onflow/fcl"_10_10const myAuthorizationFunction = ... // An Authorization Function_10_10const response = fcl.send([_10 fcl.transaction`transaction() { prepare(acct: &Account) {} execute { log("Hello, Flow!") } }`,_10 fcl.proposer(myAuthorizationFunction),_10 fcl.payer(myAuthorizationFunction),_10 fcl.authorizers([ myAuthorizationFunction ])_10])`

The builder functions, `fcl.proposer`, `fcl.payer` and `fcl.authorizations` each consume the Authorization Function and set it as the resolve field on the internal Account object it creates.

During the resolve phase of the Flow JS-SDK and FCL, when [`resolveAccounts`](https://github.com/onflow/fcl-js/blob/master/packages/sdk/src/resolve/resolve.js#L58) is called, the resolve field on each internal Account object is called, which means each Authorization Function is called appropriately and the account is *resolved* into the data structure the authorizationFunction returns. These accounts are then deduped based on the a mix of the `addr`, `keyId` and `tempId` so that only a single signature request happens per `address` `keyId` pair. When [`resolveSignatures`](https://github.com/onflow/fcl-js/blob/master/packages/sdk/src/resolve/resolve.js#L62) is called the signing function for each `address` `keyId` pair is called returning a composite signature for each signatory role.

## How to Create An Authorization Function[​](#how-to-create-an-authorization-function "Direct link to How to Create An Authorization Function")

Fortunately, creating an Authorization Function is relatively straight forward.

An Authorization Function needs to be able to do at minimum two things.

* Who will sign -- Know which account is going to sign and the keyId of the key it will use to sign
* How they sign -- Know how to get a signature for the supplied account and key from the first piece.

The Authorization Function has a concept of an account. An account represent a possible signatory for the transaction, it includes the who is signing as well as the how it will be signed. The Authorization Function is passed an empty Account and needs to return an Account, your job when making an Authorization Function is mostly to fill in this Account with the information so that the account you want to sign things can.

Lets say we knew up front the account, keyId and had a function that could sign things.

 `_10const ADDRESS = "0xba1132bc08f82fe2"_10const KEY_ID = 1 // this account on testnet has three keys, we want the one with an index of 1 (has a weight of 1000)_10const sign = msg => { /* ... returns signature (for the key above) for supplied message ... */ }`

Our Authorization Function becomes about filling things in:

Example 2:

 `_18const authorizationFunction = async (account) => {_18 // authorization function need to return an account_18 return {_18 ...account, // bunch of defaults in here, we want to overload some of them though_18 tempId: `${ADDRESS}-${KEY_ID}`, // tempIds are more of an advanced topic, for 99% of the times where you know the address and keyId you will want it to be a unique string per that address and keyId_18 addr: ADDRESS, // the address of the signatory_18 keyId: Number(KEY_ID), // this is the keyId for the accounts registered key that will be used to sign, make extra sure this is a number and not a string_18 signingFunction: async signable => {_18 // Singing functions are passed a signable and need to return a composite signature_18 // signable.message is a hex string of what needs to be signed._18 return {_18 addr: ADDRESS, // needs to be the same as the account.addr_18 keyId: Number(KEY_ID), // needs to be the same as account.keyId, once again make sure its a number and not a string_18 signature: sign(signable.message), // this needs to be a hex string of the signature, where signable.message is the hex value that needs to be signed_18 }_18 }_18 }_18}`
## Async stuff[​](#async-stuff "Direct link to Async stuff")

Both the Authorization Function, and the accounts Signing Function can be asynchronous. This means both of these functions can go and get the information needed elsewhere. Say each of your users had a `userId`. From this `userId` say you had an api call that could return the corresponding address and key that is needed for the Authorization Functions account. You could also have another endpoint that when posted the signable (includes what needs to be signed) and the `userId` it can return with the composite signature if your api decides its okay to sign (the signable has all sorts of info to help you decide). An authorization function that can do that could look something like this.

Example 3:

 `_22const getAccount = (userId) => fetch(`/api/user/${userId}/account`).then(d => d.json())_22const getSignature = (userId, signable) = fetch(`/api/user/${userId}/sign`, {_22 method: "POST",_22 headers: { "Content-Type": "application/json"},_22 body: JSON.stringify(signable),_22})_22_22function authz (userId) {_22 return async function authorizationFunction (account) {_22 const {addr, keyId} = await getAccount(userId)_22_22 return {_22 ...account,_22 tempId: `${addr}-${keyId}`,_22 addr: addr,_22 keyId: Number(keyId),_22 signingFunction: signable => {_22 return getSignature(userId, signable)_22 }_22 }_22 }_22}`

The above **Example 3** is the same as **Example 2**, but the information is gathered during the execution of the authorization function based on the supplied user id.

## How to create a Signing Function[​](#how-to-create-a-signing-function "Direct link to How to create a Signing Function")

Creating a signing function is also relatively simple!

To create a signing function you specify a function which consumes a payload and returns a signature data structure.

Example 3:

 `_17const signingFunction = ({_17 message, // The encoded string which needs to be used to produce the signature._17 addr, // The address of the Flow Account this signature is to be produced for._17 keyId, // The keyId of the key which is to be used to produce the signature._17 roles: {_17 proposer, // A Boolean representing if this signature to be produced for a proposer._17 authorizer, // A Boolean representing if this signature to be produced for a authorizer._17 payer, // A Boolean representing if this signature to be produced for a payer._17 }, _17 voucher, // The raw transactions information, can be used to create the message for additional safety and lack of trust in the supplied message._17}) => {_17 return {_17 addr, // The address of the Flow Account this signature was produced for._17 keyId, // The keyId for which key was used to produce the signature._17 signature: produceSignature(message) // The hex encoded string representing the signature of the message._17 }_17}`[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/wallet-provider-spec/authorization-function.md)Last updated on **Jan 10, 2025** by **Ali Serag**[PreviousWallet Provider Spec](/tools/wallet-provider-spec)[NextIntroduction](/tools/wallet-provider-spec/custodial)
###### Rate this page

😞😐😊

* [Overview](#overview)
* [How to Use an Authorization Function](#how-to-use-an-authorization-function)
* [How to Create An Authorization Function](#how-to-create-an-authorization-function)
* [Async stuff](#async-stuff)
* [How to create a Signing Function](#how-to-create-a-signing-function)
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

