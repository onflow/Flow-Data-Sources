# Source: https://developers.flow.com/build/differences-vs-evm

Differences vs. EVM | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Differences vs. EVM

On this page

# Differences vs. EVM

Flow [Cadence](https://cadence-lang.org/) is designed with many improvements over prior blockchain networks. As a result, you'll notice many differences between Flow vs. other blockchains, especially Ethereum. This document will be most useful to developers who are already familiar with building on the EVM, but contains details useful to all developers. Check out [Why Flow](/build/flow) for a more general overview of the Flow blockchain.

tip

Remember, Flow also supports full [EVM](/evm/about) equivalence! You can start by moving over your existing contracts, then start building new features that take advantage of the power of Cadence.

## The Flow Cadence Account Model[​](#the-flow-cadence-account-model "Direct link to The Flow Cadence Account Model")

Key pairs establish ownership on blockchains. In other blockchains (e.g. Bitcoin and Ethereum), the user's address is also calculated based on their public key, making a unique one-to-one relationship between accounts (addresses) and public keys. This also means there is no concrete "account creation" process other than generating a valid key pair.

With the advent of smart contracts, Ethereum introduced a new account type for deploying contracts that can use storage space (i.e., to store contract bytecode). You can learn more about the distinction between EOA and Contract [accounts on Ethereum](https://ethereum.org/en/developers/docs/accounts).

The [Flow account model](/build/basics/accounts) combines the concepts of EOAs and Contract Accounts into a single account model and decouples accounts and public keys. Flow accounts are associated with one or more public keys of varying weights that specify interested parties that need to produce valid cryptographic signatures for each transaction authorized by that account.

![Screenshot 2023-08-16 at 16.43.07.png](/assets/images/Screenshot_2023-08-16_at_16.43.07-07d19a771bde1467e9b81a71112250c0.png)

This natively enables interesting use cases, like key revocation, rotation, and multi-signature transactions. All Flow accounts can use network storage (e.g., for deploying contracts and storing resources like NFTs) based on the number of FLOW tokens they hold.

warning

You must run an explicit account creation transaction on Flow to create a new account. [Flow CLI](/tools/flow-cli/accounts/create-accounts) can create an account on any network with a given public key. Doing so requires a [very small fee](/build/basics/fees#fee-structure) to be paid in FLOW.

Another key difference is that [storage](/build/basics/accounts#storage) for data and assets related to an account are stored in the account, **not** in the contract as with the EVM.

Check out the [Accounts](/build/basics/accounts) concept document to learn more about Flow accounts.

## Smart Contracts[​](#smart-contracts "Direct link to Smart Contracts")

On Flow, smart contracts can be written in [Cadence](https://cadence-lang.org/), or Solidity. Cadence syntax is user-friendly and inspired by modern languages like Swift. Notable features of Cadence that make it unique and the key power of the Flow blockchain are:

* **Resource-oriented**: Cadence introduces a new type called Resources. Resources enable onchain representation of digital assets natively and securely. Resources can only exist in one location at a time and are strictly controlled by the execution environment to avoid common mishandling mistakes. Each resource has a unique `uuid` associated with it on the blockchain. Examples of usage are fungible tokens, NFTs, or any custom data structure representing a real-world asset. Check out [Resources](https://cadence-lang.org/docs/language/resources) to learn more.
* **Capability-based**: Cadence offers a [Capability-based Security](https://en.wikipedia.org/wiki/Capability-based_security) model. This also enables the use of Resources as structures to build access control. Capabilities and [Entitlements](https://cadence-lang.org/docs/language/access-control#entitlements) can provide fine-grained access to the underlying objects for better security. For example, when users list an NFT on a Flow marketplace, they create a new Capability to the stored NFT in their account so the buyer can withdraw the asset when they provide the tokens. Check out [Capability-based Access Control](https://cadence-lang.org/docs/language/capabilities) to learn more about Capabilities on Cadence.

warning

Cadence is not compiled. All contracts are public and unobfuscated on Flow. This isn't that different from the EVM, where it's trivial to decompile a contract back into Solidity.

Check out the [Cadence](https://cadence-lang.org/) website to learn the details of the Cadence programming language.

If you are a Solidity developer, we recommend you start with Cadence's [Guide for Solidity Developers](https://cadence-lang.org/docs/solidity-to-cadence) to dive deeper into the differences between the two languages.

Here are some additional resources that can help you get started with Cadence:

* [The Cadence tutorial](https://cadence-lang.org/docs/tutorial/first-steps)
* ERC-20 equivalent on Flow is the Flow Fungible Token Standard
  + [Repository](https://github.com/onflow/flow-ft)
  + [Tutorial](https://cadence-lang.org/docs/tutorial/fungible-tokens)
* ERC-721 equivalent on Flow is the Flow Non-Fungible Token Standard
  + [Repository](https://github.com/onflow/flow-nft)
  + [Tutorial](https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1)
* Asset marketplaces with Cadence
  + [Tutorial](https://cadence-lang.org/docs/tutorial/marketplace-setup)
  + [NFT Storefront](https://github.com/onflow/nft-storefront/) is an example marketplace standard

## Transactions and Scripts[​](#transactions-and-scripts "Direct link to Transactions and Scripts")

You can interact with the state on most other blockchains by cryptographically authorizing smart contract function calls. On Flow, transactions offer rich functionality through Cadence code. This allows you to seamlessly combine multiple contracts and function calls into a single transaction that updates the blockchain state - all executing together as one unified operation.

Here is a sample transaction that mints an NFT from `ExampleNFT` contract on Testnet:

`_47

import NonFungibleToken from 0x631e88ae7f1d7c20

_47

import ExampleNFT from 0x2bd9d8989a3352a1

_47

_47

/// Mints a new ExampleNFT into recipient's account

_47

_47

transaction(recipient: Address) {

_47

_47

/// Reference to the receiver's collection

_47

let recipientCollectionRef: &{NonFungibleToken.Collection}

_47

_47

/// Previous NFT ID before the transaction executes

_47

let mintingIDBefore: UInt64

_47

_47

prepare(signer: &Account) {

_47

_47

self.mintingIDBefore = ExampleNFT.totalSupply

_47

_47

// Borrow the recipient's public NFT collection reference

_47

self.recipientCollectionRef = getAccount(recipient)

_47

.capabilities.get<&{NonFungibleToken.Collection}>(ExampleNFT.CollectionPublicPath)

_47

.borrow()

_47

?? panic("The recipient does not have a NonFungibleToken Receiver at "

_47

.concat(ExampleNFT.CollectionPublicPath.toString())

_47

.concat(" that is capable of receiving an NFT.")

_47

.concat("The recipient must initialize their account with this collection and receiver first!"))

_47

_47

}

_47

_47

execute {

_47

_47

let currentIDString = self.mintingIDBefore.toString()

_47

_47

// Mint the NFT and deposit it to the recipient's collection

_47

ExampleNFT.mintNFT(

_47

recipient: self.recipientCollectionRef,

_47

name: "Example NFT #".concat(currentIDString),

_47

description: "Example description for #".concat(currentIDString),

_47

thumbnail: "https://robohash.org/".concat(currentIDString),

_47

royalties: []

_47

)

_47

}

_47

_47

post {

_47

self.recipientCollectionRef.getIDs().contains(self.mintingIDBefore): "The next NFT ID should have been minted and delivered"

_47

ExampleNFT.totalSupply == self.mintingIDBefore + 1: "The total supply should have been increased by 1"

_47

}

_47

}`

### Authorizing Transactions[​](#authorizing-transactions "Direct link to Authorizing Transactions")

The process to authorize a transaction on Flow Cadence is more complex, but also much more powerful than an EVM transaction:

* [Accounts](/build/basics/accounts) can have multiple keys with varying weights
* Multiple accounts can sign a single transaction (`prepare` takes any number of arguments)
* Transaction computation fees can be paid by a different account, called the `Payer` account.
* The [transaction nonce](https://ethereum.org/en/developers/docs/accounts/#an-account-examined) is provided by the `Proposer` account. This enables rate control and order to be dictated by a different party if needed.
* All of the above roles can be the same account.

The same powerful concept also exists for querying the blockchain state using Scripts. Here is a sample script that fetches the `ExampleNFT` IDs owned by a given account on Testnet:

`_21

/// Script to get NFT IDs in an account's collection

_21

_21

import NonFungibleToken from 0x631e88ae7f1d7c20

_21

import ExampleNFT from 0x2bd9d8989a3352a1

_21

_21

access(all) fun main(address: Address, collectionPublicPath: PublicPath): [UInt64] {

_21

_21

let account = getAccount(address)

_21

_21

let collectionRef = account

_21

.capabilities.get<&{NonFungibleToken.Collection}>(collectionPublicPath)

_21

.borrow()

_21

?? panic("The account with address "

_21

.concat(address.toString())

_21

.concat("does not have a NonFungibleToken Collection at "

_21

.concat(ExampleNFT.CollectionPublicPath.toString())

_21

.concat(". The account must initialize their account with this collection first!")))

_21

_21

return collectionRef.getIDs()

_21

_21

}`

Check out [Transactions](/build/basics/transactions) and [Scripts](/build/basics/scripts) to learn more about the concepts. You can also read the Cadence language reference on [Transactions](/build/basics/transactions) to dive deeper.

## Flow Nodes[​](#flow-nodes "Direct link to Flow Nodes")

Developers need a blockchain node to send transactions and fetch state. Flow is based on a multi-node architecture that separates tasks like consensus and computation into separate nodes. You can learn more about the Flow architecture in the [Flow Primer](https://flow.com/primer#primer-how-flow-works).

Access Nodes are the node type that are most useful for developers, as they provide access to the Flow network [via an API](/networks/flow-networks).

## SDKs and Tools[​](#sdks-and-tools "Direct link to SDKs and Tools")

If you're already familiar with blockchain development, here's a comparison between popular software packages and Flow's tooling:

* [hardhat](https://hardhat.org/) / [Truffle](https://trufflesuite.com/) / [Foundry](https://github.com/foundry-rs/foundry)
  + [Flow CLI](https://github.com/onflow/flow-cli/) provides local development tools and the [Flow Emulator](https://github.com/onflow/flow-emulator)
* [OpenZeppelin](https://www.openzeppelin.com/)
  + [Emerald OZ](https://oz.ecdao.org/overview)
* [go-ethereum](https://geth.ethereum.org/)
  + [Flow Go SDK](https://github.com/onflow/flow-go-sdk/)
  + [FCL](https://github.com/onflow/fcl-js/) also provides Backend API for Flow in JS
* [web3.js](https://github.com/web3/web3.js)
  + [FCL](https://github.com/onflow/fcl-js/)
  + [flow-cadut](https://github.com/onflow/flow-cadut) provides more utilities for using Flow on Web
* [Remix](https://remix.ethereum.org/)
  + [Flow Playground](https://play.flow.com/) provides basic experimentation on the web
  + [Cadence VSCode Extension](https://marketplace.visualstudio.com/items?itemName=onflow.cadence) is strongly suggested to install for local development
* [Testing Smart Contracts](https://ethereum.org/en/developers/docs/smart-contracts/testing/)
  + [Cadence testing framework](https://cadence-lang.org/docs/testing-framework) enables native tests in Cadence.
  + [overflow](https://github.com/bjartek/overflow) for testing in Go.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/differences-vs-evm/index.md)

Last updated on **Feb 24, 2025** by **j pimmel**

[Previous

Why Flow](/build/flow)[Next

Contract Interaction](/build/getting-started/contract-interaction)

###### Rate this page

😞😐😊

* [The Flow Cadence Account Model](#the-flow-cadence-account-model)
* [Smart Contracts](#smart-contracts)
* [Transactions and Scripts](#transactions-and-scripts)
  + [Authorizing Transactions](#authorizing-transactions)
* [Flow Nodes](#flow-nodes)
* [SDKs and Tools](#sdks-and-tools)

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