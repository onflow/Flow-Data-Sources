# Source: https://cadence-lang.org/docs/tutorial/non-fungible-tokens-2

Intermediate NFTs | Cadence



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
* Intermediate NFTs

On this page

# Intermediate NFTs

In the [last tutorial](/docs/tutorial/non-fungible-tokens-1), you implemented a simple NFT that users could mint, hold, and trade, but there was a serious flaw - each user could only hold one NFT at a time. In this tutorial, you'll improve your implementation to allow it to be able to grant users multiple NFTs and the tools needed to manage them.

tip

If you're already comfortable with Cadence and have found this page looking for information on how to build production-ready NFTs, check out the [NFT Guide] and [Flow NFT Standard] repository.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Implement a collection [resource](/docs/language/resources) that can manage multiple NFTs on behalf of a user.
* Create an [entitlement](/docs/language/access-control) to limit some functionality of a [resource](/docs/language/resources) to the owner.
* Handle errors more elegantly with functions that generate error messages.

## Storing Multiple NFTs in a Collection[​](#storing-multiple-nfts-in-a-collection "Direct link to Storing Multiple NFTs in a Collection")

Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/9da6f80f-cd79-4797-a067-47a57dc54770>](https://play.flow.com/9da6f80f-cd79-4797-a067-47a57dc54770)

This tutorial continues from the last one, but we'll be doing significant refactoring. The provided starter contains the NFT resource, but removes the code and transactions for creating NFTs and capabilities to interact with them. You'll replace those with a more sophisticated approach that will allow collections of NFTs.

It also adds some constants for the paths we'll be using so we don't need to worry about typos as we add them to several transactions and scripts.

As you've likely noticed the setup and operations that we used in the previous tutorial are not very scalable. Users need a way to store multiple NFTs from a collection and tools to manage all of those NFTs from a single place.

Using a [dictionary](/docs/language/values-and-types#dictionaries) on its own to store our NFTs would solve the problem of having to use different storage paths for each NFT, but it doesn't solve all the problems.

### Resources that Own Resources[​](#resources-that-own-resources "Direct link to Resources that Own Resources")

Instead, we can use a powerful feature of Cadence, resources owning other resources! We'll define a new `Collection` resource as our NFT storage place to enable more-sophisticated ways to interact with our NFTs. This pattern comes with interesting powers and side effects.

Since the `Collection` explicitly owns the NFTs in it, the owner could transfer all of the NFTs at once by just transferring the single collection. In addition to allowing easy batch transfers, this means that if a unique NFT wants to own another unique NFT, like a CryptoKitty owning a hat accessory, the Kitty literally stores the hat in its own fields and effectively owns it.

The hat belongs to the CryptoKitty that it is stored in, and the hat can be transferred separately or along with the CryptoKitty that owns it. Cadence is a fully object-oriented language, so ownership is indicated by where an object is stored, not just an entry on a ledger.

danger

When the NFT `Collection` resource is destroyed with the `destroy` command, all the resources stored in the dictionary are also `destroy`ed.

### NFT Collection[​](#nft-collection "Direct link to NFT Collection")

Action

Add a public resource definition called `Collection` to the `IntermediateNFT` contract. In it, add a public [dictionary](/docs/language/values-and-types#dictionaries) called `ownedNFTs` that maps `NFT`s to their `Uint64` id numbers. Initialize `ownedNFTs` with an empty dictionary.

`_10

access(all) resource Collection {

_10

access(all) var ownedNFTs: @{UInt64: NFT}

_10

_10

init () {

_10

self.ownedNFTs <- {}

_10

}

_10

}`

tip

Cadence is an object-oriented language. Inside of a composite type, such as a [resource](/docs/language/resources), `self` refers to the instance of that type and **not** the contract itself.

Dictionary definitions don't usually have the `@` symbol in the type specification, but because the `myNFTs` mapping stores resources, the whole field must become a resource type. Therefore, you need the `@` symbol indicating that `ownedNFTs` is a resource type.

As a result, all the rules that apply to resources apply to this type.

### Utility Functions[​](#utility-functions "Direct link to Utility Functions")

It's helpful for a collection to be able to handle some basic operations, such as accepting an NFT into the collection, validating whether or not a token is present, or sharing a list of all token IDs.

Action

Write a function to `deposit` a token into `ownedNFTs`:

`_10

access(all) fun deposit(token: @NFT) {

_10

self.ownedNFTs[token.id] <-! token

_10

}`

tip

Notice that we're using the `<-!` force assignment operator to move the token. This will still give a runtime error if the location already has something else stored, but it won't give a typecheck error like the `<-` move operator would in this instance.

Action

Next, write a function called `idExists` that returns a `Bool` - `true` if the id is present and `false` if it is not.

Also write a function called `getIDs` that returns an array of the `UInt64` ids of all NFTs found in the collection. Make use of the built-in `keys` function present on the dictionary type.

`_10

access(all) view fun idExists(id: UInt64): Bool {

_10

return self.ownedNFTs[id] != nil

_10

}

_10

_10

access(all) view fun getIDs(): [UInt64] {

_10

return self.ownedNFTs.keys

_10

}`

## Withdrawing NFTs[​](#withdrawing-nfts "Direct link to Withdrawing NFTs")

For the NFT `Collection`, we will publish a capability to allow anyone to access the utility functions you just created - depositing NFTs into it, verifying if an NFT is in the collection, or getting the ids of all NFTs present. We'll also need functionality to withdraw an NFT and remove it from the collection, but we obviously **don't** want anyone to be able to do that.

### Capability Security[​](#capability-security "Direct link to Capability Security")

This is where an important layer of access control comes in. Cadence utilizes [capability security](/docs/language/capabilities), which means that for any given object, a user is allowed to access a field or method of that object if they either:

* Are the owner of the object
* Have a valid reference to that field or method (note that references can only be created from capabilities, and capabilities can only be created by the owner of the object)

When a user stores their NFT `Collection` in their account storage, it is by default not available for other users to access because it requires access to the authorized account object (`auth(Storage) &Account`) which is only accessible by a transaction that the owner authorizes and signs.

To give external accounts access to the `access(all)` fields and functions, the owner (usually with the help of a developer creating a transaction) creates a link to the object in storage.

This link creates a capability. From there, it could be passed as a parameter to a function for one-time-use, or it could be put in the `/public/` domain of the user's account so that anyone can access it.

You've done this already when you've written transactions to `issue` and `publish` capabilities.

### Using Entitlements[​](#using-entitlements "Direct link to Using Entitlements")

We do not want everyone in the network to be able to call our `withdraw` function though.

In Cadence, any reference can be freely up-casted or down-casted to any subtype or supertype that the reference conforms to. This means that if you had a reference of the type `&ExampleNFT.Collection`, this would expose all the `access(all)` functions on the `Collection`.

This is a powerful feature that is very useful, but it means if there is any privileged functionality on a resource that has a public capability, then this functionality cannot be `access(all)`.

It needs to use [entitlements](/docs/language/access-control#entitlements).

Entitlements enable you to restrict the scope of access at a granular level, with the option to group restrictions under similarly named entitlements. Owners of resources can then use these entitlements to grant access to the subset of actions enabled by the authorized reference.

tip

If you're used to Solidity, you can think of this as being similar to frameworks that enable you to use modifiers to limit some functions to specific addresses with the correct role, such as `onlyOwner`.

Action

Define an [entitlement](/docs/language/access-control) called `Withdraw` in your contract, at the contract level.

`_10

access(all) entitlement Withdraw`

You've now effectively created a type of lock that can only be opened by someone with the right key - or the owner of the property, who always has access natively.

Action

Implement a `withdraw` function. It should:

* Only allow `access` to addresses with the `Withdraw` [entitlement](/docs/language/access-control).
* Accept the id of the NFT to be withdrawn as an argument
* Return an error if the NFT with that id is not present in the account's `ownedNFTs`
* Return the **actual token resource**

You should end up with something similar to:

`_10

access(Withdraw) fun withdraw(withdrawID: UInt64): @NFT {

_10

let token <- self.ownedNFTs.remove(key: withdrawID)

_10

?? panic("Could not withdraw an ExampleNFT.NFT with id="

_10

.concat(withdrawID.toString())

_10

.concat("Verify that the collection owns the NFT ")

_10

.concat("with the specified ID first before withdrawing it."))

_10

_10

return <-token

_10

}`

Providing an access scope of `access(Withdraw)` locks this functionality to only the owner that has the [resource](/docs/language/resources) directly in their storage, **or** to any address possessing a reference to this resource that has the `Withdraw` entitlement.

As with other types defined in contracts, these are namespaced to the deployer and contract. The full name of `Withdraw` would be something like `0x06.IntermediateNFT.Withdraw`. More than one contract or account can declare separate and distinct entitlements with the same name.

### Issuing an Entitlement[​](#issuing-an-entitlement "Direct link to Issuing an Entitlement")

The owner of an object is the only one who can sign a transaction to create an entitled capability or reference.

In the above example, if you wanted to make the withdraw function publicly accessible,
you could issue the capability as an entitled capability by specifying all the entitlements in the capability's type specification
using the `auth` keyword:

`_10

// DANGEROUS CODE EXAMPLE - DO NOT USE

_10

let cap = self.account.capabilities.storage.issue<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>(self.CollectionStoragePath)

_10

self.account.capabilities.publish(cap, at: self.CollectionPublicPath)`

Now, anyone could borrow that capability as the entitled version it was issued as:

`_10

let entitledCollectionRef = recipient.capabilities

_10

.borrow<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)

_10

?? panic("Could not borrow a reference to the ExampleNFT.Collection")

_10

_10

let stolenNFT <- entitledCollectionRef.withdraw(withdrawID: 1)`

Later tutorials will cover more nuanced methods for sharing an [entitlement](/docs/language/access-control).

## Error Handling[​](#error-handling "Direct link to Error Handling")

Thinking ahead, many of the transactions that we might write (or other developers composing on our contracts) will need to borrow a reference to a user's collection. We can make everyone's lives easier by adding a function to help create that error in a nice and consistent manner.

Action

Write a function called `collectionNotConfiguredError` that accepts an `address` and returns a descriptive error message that the collection was not found.

`_10

access(all) fun collectionNotConfiguredError(address: Address): String {

_10

return "Could not borrow a collection reference to recipient's IntermediateNFT.Collection"

_10

.concat(" from the path ")

_10

.concat(IntermediateNFT.CollectionPublicPath.toString())

_10

.concat(". Make sure account ")

_10

.concat(address.toString())

_10

.concat(" has set up its account ")

_10

.concat("with an IntermediateNFT Collection.")

_10

}`

## Deploy the Contract[​](#deploy-the-contract "Direct link to Deploy the Contract")

Action

Deploy the `IntermediateNFT` contract with account `0x06`.

## Creating Collections[​](#creating-collections "Direct link to Creating Collections")

We'll need several transactions to manage our NFT collection. The first is one to allow users to create a collection on their account.

Action

On your own, implement a transaction in `CreateCollection.cdc` to create and save a `Collection` in the caller's account and also `issue` and `publish` a capability for that collection.

You should end up with something similar to:

`_17

import IntermediateNFT from 0x06

_17

_17

transaction {

_17

prepare(account: auth(SaveValue, Capabilities) &Account) {

_17

// You may want to make sure one doesn't exist, but the native error is descriptive as well

_17

let collection <- IntermediateNFT.createEmptyCollection()

_17

_17

account.storage.save(<-collection, to: IntermediateNFT.CollectionStoragePath)

_17

_17

log("Collection created")

_17

_17

let cap = account.capabilities.storage.issue<&IntermediateNFT.Collection>(IntermediateNFT.CollectionStoragePath)

_17

account.capabilities.publish(cap, at: IntermediateNFT.CollectionPublicPath)

_17

_17

log("Capability created")

_17

}

_17

}`

Action

Test your transaction by creating `Collections` for several accounts. Try it with accounts that do and do **not** have `Collections` already, and verify that the correct behavior occurs.

## Minting an NFT[​](#minting-an-nft "Direct link to Minting an NFT")

Action

Next, add a transaction to mint an nft and grant it to the caller. Use the `prepare` phase to `borrow` a reference to the caller's `Collection` and store it in a transaction-level field. Then, use `execute` to create the nft and use the `Collection`'s `deposit` function to save it in the `Collection`.

It's better practice to separate code that accesses accounts and storage to collect authorized references from the code that executes the changes to state.

You can pass arguments, such as the `String` for the NFT `description` by defining parameters on the `transaction`.

Your transaction should be similar to:

`_19

import IntermediateNFT from 0x06

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

Action

Test your transaction by minting several NFTs for several accounts. Try it with accounts that do and do **not** have `Collections` and verify that the correct behavior occurs.

## Printing the NFTs Owned by an Account[​](#printing-the-nfts-owned-by-an-account "Direct link to Printing the NFTs Owned by an Account")

Remember, you can use scripts to access functionality that doesn't need authorization, such as the function to `getIDs` for all the NFTs in a `Collection`.

Action

Write a script to `PrintNFTs` for the provided address.

You can also pass arguments into the `main` function in a script.

`_20

_20

import IntermediateNFT from 0x06

_20

_20

access(all) fun main(address: Address): [UInt64] {

_20

let nftOwner = getAccount(address)

_20

_20

let capability = nftOwner.capabilities.get<&IntermediateNFT.Collection>(IntermediateNFT.CollectionPublicPath)

_20

_20

let receiverRef = nftOwner.capabilities

_20

.borrow<&IntermediateNFT.Collection>(IntermediateNFT.CollectionPublicPath)

_20

?? panic(IntermediateNFT.collectionNotConfiguredError(address: address))

_20

_20

_20

log("Account "

_20

.concat(address.toString())

_20

.concat(" NFTs")

_20

)

_20

_20

return receiverRef.getIDs()

_20

}`

## Transferring NFTs[​](#transferring-nfts "Direct link to Transferring NFTs")

Finally, you'll want to provide a method for users to `Transfer` NFTs to one another. To do so, you'll need to `withdraw` the NFT from the owner's `Collection` and `deposit` it to the recipient.

This transaction is **not** bound by the `Withdraw` capability, because the caller will be the account that has the NFT in storage, which automatically possesses full entitlement to everything in its own storage. It also doesn't need the permission of or a signature from the recipient, because we gave the `deposit` function `access(all)` and published a public capability to it.

Action

Start by stubbing out a transaction that accepts a `recipientAddress` and `tokenId`. It should have a transaction-level field called `transferToken` to store the NFT temporarily, between the `prepare`, and `execute` phases.

`_13

import IntermediateNFT from 0x06

_13

_13

transaction(recipientAddress: Address, tokenId: UInt64) {

_13

let transferToken: @IntermediateNFT.NFT

_13

_13

prepare(account: auth(BorrowValue) &Account) {

_13

// TODO

_13

}

_13

_13

execute {

_13

// TODO

_13

}

_13

}`

Action

Next, in `prepare`, get a reference to the sender's `Collection` and use it to `move (<-)` the token out of their collection and into `transferToken`:

`_10

let collectionRef = account.storage

_10

.borrow<auth(IntermediateNFT.Withdraw) &IntermediateNFT.Collection>(from: IntermediateNFT.CollectionStoragePath)

_10

?? panic(IntermediateNFT.collectionNotConfiguredError(address: account.address))

_10

_10

self.transferToken <- collectionRef.withdraw(withdrawID: tokenId)`

Action

Finally, get a public reference to the recipient's account, use that to get a reference to the capability for the recipient's `Collection`, and use the `deposit` function to `move (<-)` the NFT.

`_10

let recipient = getAccount(recipientAddress)

_10

_10

let receiverRef = recipient.capabilities

_10

.borrow<&IntermediateNFT.Collection>(IntermediateNFT.CollectionPublicPath)

_10

?? panic(IntermediateNFT.collectionNotConfiguredError(address: recipient.address))

_10

_10

receiverRef.deposit(token: <-self.transferToken)

_10

_10

log("NFT ID transferred to account "

_10

.concat(recipient.address.toString()))`

Action

Test your transaction by transferring several NFTs for several accounts. Try various combinations, and use the `PrintNFTs` script to make sure the NFTs move as expected.

## Reviewing Intermediate NFTs[​](#reviewing-intermediate-nfts "Direct link to Reviewing Intermediate NFTs")

In this tutorial, you learned how to expand the functionality of your basic NFT to allow users to create collections of NFTs, then mint and trade those collections. You also learned more about the details of [entitlements](/docs/language/access-control#entitlements) and how you can use them to protect functionality so that only those who are supposed to be able to access something are able to.

Now that you have completed the tutorial, you should be able to:

* Implement a collection [resource](/docs/language/resources) that can manage multiple NFTs on behalf of a user.
* Create an [entitlement](/docs/language/access-control) to limit some functionality of a [resource](/docs/language/resources) to the owner.
* Handle errors more elegantly with functions that generate error messages.

In the next tutorial, you'll learn how to create fungible token collections.

**Tags:**

* [reference](/docs/tags/reference)
* [NFT](/docs/tags/nft)
* [Non-Fungible Token](/docs/tags/non-fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/05-non-fungible-tokens-2.md)

[Previous

Basic NFT](/docs/tutorial/non-fungible-tokens-1)[Next

Fungible Tokens](/docs/tutorial/fungible-tokens)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Storing Multiple NFTs in a Collection](#storing-multiple-nfts-in-a-collection)
  + [Resources that Own Resources](#resources-that-own-resources)
  + [NFT Collection](#nft-collection)
  + [Utility Functions](#utility-functions)
* [Withdrawing NFTs](#withdrawing-nfts)
  + [Capability Security](#capability-security)
  + [Using Entitlements](#using-entitlements)
  + [Issuing an Entitlement](#issuing-an-entitlement)
* [Error Handling](#error-handling)
* [Deploy the Contract](#deploy-the-contract)
* [Creating Collections](#creating-collections)
* [Minting an NFT](#minting-an-nft)
* [Printing the NFTs Owned by an Account](#printing-the-nfts-owned-by-an-account)
* [Transferring NFTs](#transferring-nfts)
* [Reviewing Intermediate NFTs](#reviewing-intermediate-nfts)

Got suggestions for this site?

* [It's open-source!](https://github.com/onflow/cadence-lang.org)

The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.