# Source: https://cadence-lang.org/docs/tutorial/marketplace-setup

Marketplace Setup | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/docs)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Language Reference](/docs/language)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Tutorial](/docs/tutorial/first-steps)

  + [First Steps](/docs/tutorial/first-steps)
  + [Hello World](/docs/tutorial/hello-world)
  + [Resources and the Move (<-) Operator](/docs/tutorial/resources)
  + [Capabilities](/docs/tutorial/capabilities)
  + [Basic NFT](/docs/tutorial/non-fungible-tokens-1)
  + [Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)
  + [Fungible Tokens](/docs/tutorial/fungible-tokens)
  + [Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [Marketplace](/docs/tutorial/marketplace-compose)
  + [Voting Contract](/docs/tutorial/voting)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [JSON-Cadence Format](/docs/json-cadence-spec)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Tutorial
* Marketplace Setup

On this page

# Marketplace Setup

In the [Marketplace Tutorial](/docs/tutorial/marketplace-compose), we're going to create a marketplace that uses both the fungible and non-fungible token (NFT) contracts that we have learned about in previous tutorials. First, you'll execute a series of transactions to set up the accounts that you'll need to complete the marketplace tutorial. Next, you'll build the marketplace itself.

warning

If you're farther along with your Cadence learning journey and found this page looking for a production-ready marketplace, check out the [NFTStorefront repo](https://github.com/onflow/nft-storefront)!

## Objectives[​](#objectives "Direct link to Objectives")

In this tutorial, you'll simply execute transactions that you've already written and validate that the setup is complete. It's only necessary because the playground is not actually a blockchain, so the state is transient.

## Getting started[​](#getting-started "Direct link to Getting started")

Open the starter code for this tutorial in the Flow Playground: [play.flow.com/463a9a08-deb0-455a-b2ed-4583ea6dcb64](https://play.flow.com/463a9a08-deb0-455a-b2ed-4583ea6dcb64).

Your goal for this exercise is to set up the ephemeral playground into the state the blockchain would be in when you begin building a marketplace. It's also a great chance to practice some of what you've learned already. You'll need to:

* Deploy the NFT contract on account `0x06`.
* Deploy the fungible token contract on account `0x07`.
* Set up account `0x08` and `0x09` to handle NFTs and tokens compatible with the simplified contracts you've built.
* Give fungible tokens to `0x08`.
* Give an NFT to `0x09`.

To start, you'll need to deploy some copies of the contracts you've built in the previous tutorials, and call transactions you've already built. For your convenience, they've been provided in the starter playground.

1. Open the `ExampleToken` contract. This is the same contract from the fungible token tutorial.
2. Deploy the `ExampleToken` code to account `0x06`.
3. Switch to the `IntermediateNFT` contract.
4. Deploy the NFT code to account `0x07` by selecting it as the deploying signer.

## Account setup transactions[​](#account-setup-transactions "Direct link to Account setup transactions")

Next, you'll need to execute transactions to set up accounts `0x08` and `0x09` to be able to work with the contracts for the marketplace. You've already built these transactions in previous exercises.

tip

**Remember**: On Flow, accounts must maintain a balance of $FLOW proportional to the amount of storage the account is using. Furthermore, placing something in the storage of an account requires that the receiving account has a capability that can accept the asset type. As a result, accounts can **not** accept arbitrary data (including tokens!) from random contracts without first executing a transaction to allow it.

This might seem like a burden, but it's **great!** Thanks to this feature, one of the most common causes of burning assets is impossible on Flow. You can **not** send property to a random address — only those that know how to receive it!

### NFT setup[​](#nft-setup "Direct link to NFT setup")

Open the `NFT Setup` transaction:

`_16

import IntermediateNFT from 0x07

_16

_16

transaction() {

_16

prepare(acct: auth(SaveValue, Capabilities) &Account) {

_16

// Create an empty NFT collection

_16

acct.storage.save(<-IntermediateNFT.createEmptyCollection(), to: IntermediateNFT.CollectionStoragePath)

_16

_16

// Create a public capability for the Collection

_16

let cap = acct.capabilities.storage.issue<&IntermediateNFT.Collection>(IntermediateNFT.CollectionStoragePath)

_16

acct.capabilities.publish(cap, at: IntermediateNFT.CollectionPublicPath)

_16

}

_16

_16

execute {

_16

log("Empty NFT Collection Created")

_16

}

_16

}`

This transaction will:

* `prepare` an account reference with permissions to create and save capabilities.
* Call `createEmptyCollection()` from the `IntermediateNFT` contract to create a collection.
* Create and publish public capabilities for the NFT collection.

Run the transaction using `0x08` as the signer, then run it again for `0x09`.

### Fungible token setup[​](#fungible-token-setup "Direct link to Fungible token setup")

Open the `Fungible Token Setup` transaction:

`_19

import ExampleToken from 0x06

_19

_19

transaction() {

_19

prepare(acct: auth(SaveValue, Capabilities) &Account) {

_19

// Create a vault and save it in account storage

_19

acct.storage.save(<-ExampleToken.createEmptyVault(), to: ExampleToken.VaultStoragePath)

_19

_19

// Create and publish a receiver for the fungible tokens

_19

let cap = acct.capabilities.storage.issue<&ExampleToken.Vault>(

_19

ExampleToken.VaultStoragePath

_19

)

_19

_19

acct.capabilities.publish(cap, at: ExampleToken.VaultPublicPath)

_19

}

_19

_19

execute {

_19

log("Vault Created")

_19

}

_19

}`

This transaction will:

* Instantiate a constant for and borrow a reference to the `ExampleToken` contract.
* Create and add an empty `ExampleToken` vault.
* Add the `Receiver` [capability](/docs/language/capabilities) and [publish](/docs/language/accounts/capabilities#publishing-capabilities) it.

Run the transaction using `0x08` as the signer, then run it again for `0x09`.

## Minting NFTs[​](#minting-nfts "Direct link to Minting NFTs")

Now that you've set up both accounts to be able to receive NFTs, it's time to give account `0x08` an NFT to sell to `0x09`.

Reminder

The `IntermediateNFT` contract allows **anyone** to freely mint NFTs. You wouldn't want this ability in production, but it is in here to streamline the tutorial.

You've already written a transaction to mint an NFT, so we've provided it here. You just need to call it:

`_19

import IntermediateNFT from 0x07

_19

_19

transaction(description: String) {

_19

let receiverRef: &IntermediateNFT.Collection

_19

_19

prepare(account: auth(BorrowValue) &Account) {

_19

self.receiverRef = account.capabilities

_19

.borrow<&IntermediateNFT.Collection>(IntermediateNFT.CollectionPublicPath)

_19

?? panic(IntermediateNFT.collectionNotConfiguredError(address: account.address))

_19

}

_19

_19

execute {

_19

let newNFT <- IntermediateNFT.mintNFT(description: description)

_19

_19

self.receiverRef.deposit(token: <-newNFT)

_19

_19

log("NFT Minted and deposited to minter's Collection")

_19

}

_19

}`

Mint an NFT with account `0x08`.

## Minting fungible tokens[​](#minting-fungible-tokens "Direct link to Minting fungible tokens")

You've also set up both accounts to be able to receive non-fungible tokens from `ExampleToken`.

Reminder

The `ExampleToken` contract only allows the owner of the contract to mint NFTs.

You've already written a transaction to mint fungible tokens, so we've provided it here. You just need to call it:

`_26

import ExampleToken from 0x06

_26

_26

transaction(recipient: Address, amount: UFix64) {

_26

let mintingRef: &ExampleToken.VaultMinter

_26

var receiver: Capability<&{ExampleToken.Receiver}>

_26

_26

prepare(signer: auth(BorrowValue) &Account) {

_26

self.mintingRef = signer.storage.borrow<&ExampleToken.VaultMinter>(from: /storage/CadenceFungibleTokenTutorialMinter)

_26

?? panic(ExampleToken.vaultNotConfiguredError(address: recipient))

_26

_26

let recipient = getAccount(recipient)

_26

_26

// Consider further error handling if this fails

_26

self.receiver = recipient.capabilities.get<&{ExampleToken.Receiver}>

_26

(ExampleToken.VaultPublicPath)

_26

_26

}

_26

_26

execute {

_26

// Mint tokens and deposit them into the recipient's Vault

_26

self.mintingRef.mintTokens(amount: amount, recipient: self.receiver)

_26

_26

log("Tokens minted and deposited to account "

_26

.concat(self.receiver.address.toString()))

_26

}

_26

}`

Call `Mint Tokens` with account `0x06` as the signer to grant 40 tokens to `0x09` and 20 tokens to `0x08`.

## Validating the setup[​](#validating-the-setup "Direct link to Validating the setup")

We've provided a script called `Validate Setup` that you can use to make sure you've completed the setup correctly.

Run the `Validate Setup` script and resolve any issues.

The script should not panic, and you should see something like this output:

`_10

...64807.OwnerInfo(acct8Balance: 40.00000000, acct9Balance: 40.00000000, acct8IDs: [1], acct9IDs: [])`

## Conclusion[​](#conclusion "Direct link to Conclusion")

With your playground now in the correct state, you're ready to continue with the next tutorial.

Now that you have completed this tutorial, you are able to:

* Set up accounts and deploy contracts required for a basic NFT marketplace on Flow.
* Configure account storage and capabilities for fungible and non-fungible tokens.
* Validate the correct setup of accounts and assets in preparation for marketplace operations.

You do not need to open a new playground session for the marketplace tutorial. You can just continue using this one.

## Reference solution[​](#reference-solution "Direct link to Reference solution")

warning

You are **not** saving time by skipping to the reference implementation. You'll learn much faster by doing the tutorials as presented!

Reference solutions are functional, but may not be optimal.

* [Reference Solution](https://play.flow.com/463a9a08-deb0-455a-b2ed-4583ea6dcb64)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/07-marketplace-setup.md)

[Previous

Fungible Tokens](/docs/tutorial/fungible-tokens)[Next

Marketplace](/docs/tutorial/marketplace-compose)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Getting started](#getting-started)
* [Account setup transactions](#account-setup-transactions)
  + [NFT setup](#nft-setup)
  + [Fungible token setup](#fungible-token-setup)
* [Minting NFTs](#minting-nfts)
* [Minting fungible tokens](#minting-fungible-tokens)
* [Validating the setup](#validating-the-setup)
* [Conclusion](#conclusion)
* [Reference solution](#reference-solution)