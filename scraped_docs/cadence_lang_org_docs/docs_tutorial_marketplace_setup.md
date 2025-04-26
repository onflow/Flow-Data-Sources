# Source: https://cadence-lang.org/docs/tutorial/marketplace-setup

7. Marketplace Setup | Cadence



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)

[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)

Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)

  + [First Steps](/docs/tutorial/first-steps)
  + [Hello World](/docs/tutorial/hello-world)
  + [Resources and the Move (<-) Operator](/docs/tutorial/resources)
  + [Capabilities](/docs/tutorial/capabilities)
  + [Basic NFT](/docs/tutorial/non-fungible-tokens-1)
  + [Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)
  + [Fungible Tokens](/docs/tutorial/fungible-tokens)
  + [7. Marketplace Setup](/docs/tutorial/marketplace-setup)
  + [8. Marketplace](/docs/tutorial/marketplace-compose)
  + [9. Voting Contract](/docs/tutorial/voting)
  + [10. Composable Resources](/docs/tutorial/resources-compose)
* [Language Reference](/docs/language/)
* [Cadence 1.0 Migration Guide](/docs/cadence-migration-guide/)
* [Design Patterns](/docs/design-patterns)
* [Anti-Patterns](/docs/anti-patterns)
* [Development Standards](/docs/project-development-tips)
* [Security Best Practices](/docs/security-best-practices)
* [Cadence Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)

* Tutorial
* 7. Marketplace Setup

# 7. Marketplace Setup

warning

We're in the process of updating the Cadence tutorial series. This tutorial, and the ones following, have **not** yet been updated.

Check back, or follow us on socials. These will be updated soon!

In this tutorial, we're going to create a marketplace that uses both the fungible
and non-fungible token (NFTs) contracts that we have learned about in previous tutorials.
This page requires you to execute a series of transactions to setup your accounts to complete the Marketplace tutorial.
The next page contains the main content of the tutorial.

When you are done with the tutorial, check out the [NFTStorefront repo](https://github.com/onflow/nft-storefront)
for an example of a production ready marketplace that you can use right now on testnet or mainnet!

---

Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/7355d51c-066b-46be-adab-a3da6c28b645>](https://play.flow.com/7355d51c-066b-46be-adab-a3da6c28b645)

The tutorial will be asking you to take various actions to interact with this code.

If you have already completed the Marketplace tutorial, please move on to [Composable Resources: Kitty Hats](/docs/tutorial/resources-compose).

This guide will help you quickly get the playground to the state you need to complete the Marketplace tutorial.
The marketplace tutorial uses the Fungible Token and Non-Fungible token contracts
to allow users to buy and sell NFTs with fungible tokens.

---

Action

Some of the code in these setup instructions has intentional errors built into it.
You should understand enough about Cadence to be able to fix these tutorials on your own.
All of the errors involve concepts that you have learned in previous tutorials

1. Open the `ExampleToken` contract. This is the same contract from the fungible token tutorial.
2. Deploy the `ExampleToken` code to account `0x06`.
3. Switch to the `ExampleNFT` contract (Contract 2)
4. Deploy the NFT code to account `0x07` by selecting it as the deploying signer.
5. Run the transaction in "Setup 6". This is the `SetupAccount6Transaction.cdc` file.
   Use account `0x06` as the only signer to set up account `0x06`'s storage.

SetupAccount6Transaction.cdc

`_25

// SetupAccount6Transaction.cdc

_25

_25

import ExampleToken from 0x06

_25

import ExampleNFT from 0x07

_25

_25

// This transaction sets up account 0x06 for the marketplace tutorial

_25

// by publishing a Vault reference and creating an empty NFT Collection.

_25

transaction {

_25

prepare(acct: auth(SaveValue) &Account) {

_25

// Create a public Receiver capability to the Vault

_25

let receiverCap = acct.capabilities.storage.issue<&{ExampleToken.Receiver}>(

_25

/storage/CadenceFungibleTokenTutorialVault

_25

)

_25

acct.capabilities.publish(receiverCap, at: /public/CadenceFungibleTokenTutorialReceiver)

_25

_25

// store the empty NFT Collection in account storage

_25

acct.storage.save(<-ExampleNFT.createEmptyCollection(nftType: nil), to: ExampleNFT.CollectionStoragePath)

_25

_25

log("Collection created for account 2")

_25

_25

// create a public capability for the Collection

_25

let cap = acct.capabilities.storage.issue<&ExampleNFT.Collection>(ExampleNFT.CollectionStoragePath)

_25

acct.capabilities.publish(cap, at: ExampleNFT.CollectionStoragePath)

_25

}

_25

}`

7. Run the second transaction, "Setup 7". This is the `SetupAccount7Transaction.cdc` file.
   Use account `0x07` as the only signer to set up account `0x07`'s storage.

SetupAccount7Transaction.cdc

`_44

// SetupAccount7Transaction.cdc

_44

_44

import ExampleToken from 0x06

_44

import ExampleNFT from 0x07

_44

_44

// This transaction adds an empty Vault to account 0x07

_44

// and mints an NFT with id=1 that is deposited into

_44

// the NFT collection on account 0x06.

_44

transaction {

_44

_44

// Private reference to this account's minter resource

_44

let minterRef: &ExampleNFT.NFTMinter

_44

_44

prepare(acct: auth(BorrowValue, SaveValue, StorageCapabilities, PublishCapability) &Account) {

_44

// create a new vault instance

_44

let vaultA <- ExampleToken.createEmptyVault()

_44

_44

// Store the vault in the account storage

_44

acct.storage.save(<-vaultA, to: ExampleToken.VaultStoragePath)

_44

_44

// Create a public Receiver capability to the Vault

_44

let receiverCap = acct.capabilities.storage.issue<&ExampleToken.Vault>(

_44

ExampleToken.VaultStoragePath

_44

)

_44

acct.capabilities.publish(receiverCap, at: ExampleToken.VaultPublicPath)

_44

}

_44

execute {

_44

// Get the recipient's public account object

_44

let recipient = getAccount(0x06)

_44

_44

// Get the Collection reference for the receiver

_44

// getting the public capability and borrowing a reference from it

_44

let receiverRef = recipient.capabilities

_44

.borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)

_44

?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"

_44

.concat(" from the path ")

_44

.concat(ExampleNFT.CollectionPublicPath.toString())

_44

.concat(". Make sure account 0x06 has set up its account ")

_44

.concat("with an ExampleNFT Collection."))

_44

_44

// Mint an NFT and deposit it into account 0x06's collection

_44

receiverRef.deposit(token: <-ExampleNFT.mintNFT())

_44

}

_44

}`

8. Run the transaction in "Setup 6". This is the `SetupAccount6TransactionMinting.cdc` file.
   Use account `0x06` as the only signer to mint fungible tokens for account 6 and 7.

SetupAccount6TransactionMinting.cdc

`_35

// SetupAccount6TransactionMinting.cdc

_35

_35

import ExampleToken from 0x06

_35

import ExampleNFT from 0x07

_35

_35

// This transaction mints tokens for both accounts using

_35

// the minter stored on account 0x06.

_35

transaction {

_35

_35

// Public Vault Receiver References for both accounts

_35

let acct6Capability: Capability<&{ExampleToken.Receiver}>

_35

let acct7Capability: Capability<&{ExampleToken.Receiver}>

_35

_35

// Private minter references for this account to mint tokens

_35

let minterRef: &ExampleToken.VaultMinter

_35

_35

prepare(acct: auth(SaveValue, StorageCapabilities, BorrowValue) &Account) {

_35

// Get the public object for account 0x07

_35

let account7 = getAccount(0x07)

_35

_35

// Retrieve public Vault Receiver references for both accounts

_35

self.acct6Capability = acct.capabilities.get<&{ExampleToken.Receiver}>(/public/CadenceFungibleTokenTutorialReceiver)

_35

self.acct7Capability = account7.capabilities.get<&{ExampleToken.Receiver}>(/public/CadenceFungibleTokenTutorialReceiver)

_35

_35

// Get the stored Minter reference for account 0x06

_35

self.minterRef = acct.storage.borrow<&ExampleToken.VaultMinter>(from: /storage/CadenceFungibleTokenTutorialMinter)

_35

?? panic("Could not borrow owner's vault minter reference")

_35

}

_35

_35

execute {

_35

// Mint tokens for both accounts

_35

self.minterRef.mintTokens(amount: 20.0, recipient: self.acct7Capability)

_35

self.minterRef.mintTokens(amount: 10.0, recipient: self.acct6Capability)

_35

}

_35

}`

9. Run the script `CheckSetupScript.cdc` file in Script 1 to ensure everything is set up.

CheckSetupScript.cdc

`_87

// CheckSetupScript.cdc

_87

_87

import ExampleToken from 0x06

_87

import ExampleNFT from 0x07

_87

_87

/// Allows the script to return the ownership info

_87

/// of all the accounts

_87

access(all) struct OwnerInfo {

_87

access(all) let acct6Balance: UFix64

_87

access(all) let acct7Balance: UFix64

_87

_87

access(all) let acct6IDs: [UInt64]

_87

access(all) let acct7IDs: [UInt64]

_87

_87

init(balance1: UFix64, balance2: UFix64, acct6IDs: [UInt64], acct7IDs: [UInt64]) {

_87

self.acct6Balance = balance1

_87

self.acct7Balance = balance2

_87

self.acct6IDs = acct6IDs

_87

self.acct7IDs = acct7IDs

_87

}

_87

}

_87

_87

// This script checks that the accounts are set up correctly for the marketplace tutorial.

_87

//

_87

// Account 0x06: Vault Balance = 40, NFT.id = 1

_87

// Account 0x07: Vault Balance = 20, No NFTs

_87

access(all) fun main(): OwnerInfo {

_87

// Get the accounts' public account objects

_87

let acct6 = getAccount(0x06)

_87

let acct7 = getAccount(0x07)

_87

_87

// Get references to the account's receivers

_87

// by getting their public capability

_87

// and borrowing a reference from the capability

_87

let acct6ReceiverRef = acct6.capabilities.get<&{ExampleToken.Balance}>

_87

(/public/CadenceFungibleTokenTutorialReceiver)

_87

.borrow()

_87

?? panic("Could not borrow a balance reference to "

_87

.concat("0x06's ExampleToken.Vault")

_87

.concat(". Make sure 0x06 has set up its account ")

_87

.concat("with an ExampleToken Vault and valid capability."))

_87

_87

let acct7ReceiverRef = acct7.capabilities.get<&{ExampleToken.Balance}>

_87

(/public/CadenceFungibleTokenTutorialReceiver)

_87

.borrow()

_87

?? panic("Could not borrow a balance reference to "

_87

.concat("0x07's ExampleToken.Vault")

_87

.concat(". Make sure 0x07 has set up its account ")

_87

.concat("with an ExampleToken Vault and valid capability."))

_87

_87

let returnArray: [UFix64] = []

_87

_87

// verify that the balances are correct

_87

if acct6ReceiverRef.balance != 40.0 || acct7ReceiverRef.balance != 20.0 {

_87

panic("Wrong balances!")

_87

}

_87

_87

// Find the public Receiver capability for their Collections

_87

let acct6Capability = acct6.capabilities.get<&{ExampleNFT.NFTReceiver}>(ExampleNFT.CollectionPublicPath)

_87

let acct7Capability = acct7.capabilities.get<&{ExampleNFT.NFTReceiver}>(ExampleNFT.CollectionPublicPath)

_87

_87

// borrow references from the capabilities

_87

let nft1Ref = acct6Capability.borrow()

_87

?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"

_87

.concat(" from the path ")

_87

.concat(ExampleNFT.CollectionPublicPath.toString())

_87

.concat(". Make sure account 0x06 has set up its account ")

_87

.concat("with an ExampleNFT Collection."))

_87

_87

let nft2Ref = acct7Capability.borrow()

_87

?? panic("Could not borrow a collection reference to 0x07's ExampleNFT.Collection"

_87

.concat(" from the path ")

_87

.concat(ExampleNFT.CollectionPublicPath.toString())

_87

.concat(". Make sure account 0x07 has set up its account ")

_87

.concat("with an ExampleNFT Collection."))

_87

_87

// verify that the collections are correct

_87

if nft1Ref.getIDs()[0] != 1 || nft2Ref.getIDs().length != 0 {

_87

panic("Wrong Collections!")

_87

}

_87

_87

// Return the struct that shows the account ownership info

_87

return OwnerInfo(balance1: acct6ReceiverRef.balance,

_87

balance2: acct7ReceiverRef.balance,

_87

acct6IDs: nft1Ref.getIDs(),

_87

acct7IDs: nft2Ref.getIDs())

_87

}`

10. The script should not panic and you should see something like this output

`_10

"Account 6 Balance"

_10

40.00000000

_10

"Account 7 Balance"

_10

20.00000000

_10

"Account 6 NFTs"

_10

[1]

_10

"Account 7 NFTs"

_10

[]`

---

With your playground now in the correct state, you're ready to continue with the next tutorial.

You do not need to open a new playground session for the marketplace tutorial. You can just continue using this one.

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/07-marketplace-setup.md)

[Previous

Fungible Tokens](/docs/tutorial/fungible-tokens)[Next

8. Marketplace](/docs/tutorial/marketplace-compose)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.