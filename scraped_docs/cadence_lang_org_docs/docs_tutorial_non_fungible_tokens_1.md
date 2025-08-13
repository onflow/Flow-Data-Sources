# Source: https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1

Basic NFT | Cadence



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
  + [9. Voting Contract](/docs/tutorial/voting)
  + [10. Composable Resources](/docs/tutorial/resources-compose)
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
* Basic NFT

On this page

# Basic NFT

In this tutorial, we're going to deploy, store, and transfer **Non-Fungible Tokens (NFTs)**. The NFT is an integral part of blockchain technology. An NFT is a digital asset that represents ownership of something unique and indivisible. Unlike fungible tokens, which operate more like money, you can't divide an NFT, and the owner is likely to be upset if you were to swap one for another without their consent. Examples of NFTs include: [CryptoKitties](https://www.cryptokitties.co/), [Top Shot Moments](https://nbatopshot.com/), tickets to a really fun concert, or even real property such as a horse or a house!

Production-quality NFTs on Flow implement the [Flow NFT Standard](https://github.com/onflow/flow-nft), which defines a basic set of properties for NFTs on Flow.

This tutorial teaches you a basic method of creating simple NFTs to illustrate important language concepts, but will not use the full NFT Standard for the sake of simplicity.

tip

If you're already comfortable with Cadence and have found this page looking for information on how to build production-ready NFTs, check out the [NFT Guide](https://developers.flow.com/build/guides/nft) and [Flow NFT Standard](https://github.com/onflow/flow-nft) repository.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Deploy a basic NFT contract and type definitions.
* Create an NFT object and store it in a user's account storage.
* Write a transaction to mint an NFT and create a capability so others can view it.
* Transfer an NFT from one account to another.
* Use a script to see if an NFT is stored in an account.
* Implement and utilize a dictionary in Cadence.

## NFTs on Cadence[​](#nfts-on-cadence "Direct link to NFTs on Cadence")

Instead of being represented in a central ledger, like in most smart contract languages, Cadence represents each NFT as a **[resource](/docs/language/resources) object that users store in their accounts**. This strategy is a response to the lessons learned by the Flow team (the Chief Architect of Flow is the original proposer and co-author of the [ERC-721 NFT standard](https://github.com/ethereum/eips/issues/721)).

It allows NFTs to benefit from the resource ownership rules that are enforced by the [type system](/docs/language/values-and-types/) — resources can only have a single owner, they cannot be duplicated, and they cannot be lost due to accidental or malicious programming errors. These protections ensure that owners know that their NFT is safe and can represent an asset that has real value, and helps prevent developers from breaking this trust with easy-to-make programming mistakes.

When users on Flow want to **transact** with each other, they can do so **peer-to-peer**, without having to interact with a central NFT contract, by calling resource-defined methods in both users' accounts.

NFTs in a real-world context make it possible to trade assets and prove who the owner of an asset is. On Flow, NFTs are interoperable: they can be used in different smart contracts and app contexts in an account.

## The simplest possible NFT[​](#the-simplest-possible-nft "Direct link to The simplest possible NFT")

Open the starter code for this tutorial in the Flow Playground: [play.flow.com/ea3aadb6-1ce6-4734-9792-e8fd334af7dc](https://play.flow.com/ea3aadb6-1ce6-4734-9792-e8fd334af7dc).

At their core, NFTs are simply a way to create true ownership of unique digital property. The simplest possible implementation is a resource with a unique id number.

Implement a simple NFT by creating a [resource](/docs/language/resources) with a constant `id` that is assigned in `init`. The `id` should be public:

`_10

access(all) resource NFT {

_10

_10

access(all) let id: UInt64

_10

_10

init(initID: UInt64) {

_10

self.id = initID

_10

}

_10

}`

### Adding basic metadata[​](#adding-basic-metadata "Direct link to Adding basic metadata")

An NFT is also usually expected to include some metadata like a name, description, traits, or a picture. Historically, most of this metadata has been stored off-chain, and the on-chain token only contains a URL or something similar that points to the off-chain metadata.

This practice was necessary due to the original costs of doing anything onchain, but it created the illusion that the actual content of an NFT was permanent and onchain. Unfortunately, the metadata and images for many older NFT collections can vanish (and sadly, sometimes *have* vanished) at any time.

In Flow, storing this data offchain is possible, but you can—*and normally should*—store all the metadata associated with a token directly on-chain. Unlike many other blockchain networks, **you do not need to consider string storage or manipulation as particularly expensive**.

tip

This tutorial describes a simplified implementation. Check out the [the NFT metadata guide](https://developers.flow.com/build/advanced-concepts/metadata-views) if you want to learn how to do this in production.

Add a public `metadata` variable to your NFT. For now, it can be a simple `String`-to-`String` [dictionary](/docs/language/values-and-types/dictionaries#dictionary-types). Update the `init` to also initialize a `description` in your metadata. It should now look similar to:

`_10

access(all) resource NFT {

_10

access(all) let id: UInt64

_10

access(all) var metadata: {String: String}

_10

_10

init(initID: UInt64, initDescription: String) {

_10

self.id = initID

_10

self.metadata = {"description": initDescription}

_10

}

_10

}`

### Creating the NFT[​](#creating-the-nft "Direct link to Creating the NFT")

As with any complex type in any language, now that you've created the definition for the type, you need to add a way to instantiate new instances of that type, since these instances are the NFTs. This simple NFT type must be initialized with an id number and a `String` description.

Traditionally, NFTs are provided with id numbers that indicate the order in which they were minted. To handle this, you can use a simple counter:

1. Add a public, contract-level field to keep track of the last assigned id number.

   `_10

   access(contract) var counter: UInt64`

   * You're going to immediately get an error in the editor with `counter`.
   * Contract-level fields must be initialized in the `init` function.
2. Add an `init` function to the `BasicNFT` contract and initialize `counter` to zero:

   `_10

   init() {

   _10

   self.counter = 0

   _10

   }`
3. Add a public function to increment the counter and `create` and `return` an `NFT` with a provided description.

warning

We're creating a **public** function that allows **anyone** to provide **any** string. Take care when building real apps that will be exposed to humanity.

`_10

access(all) fun mintNFT(description: String): @NFT {

_10

self.counter = self.counter + 1

_10

return <- create NFT(initID: self.counter, initDescription: description)

_10

}`

Remember, when you work with a [resource](/docs/language/resources), you must use the [move operator](/docs/language/operators/assign-move-force-swap#move-operator--) (`<-`) to **move** it from one location to another.

## Adding an NFT to your account[​](#adding-an-nft-to-your-account "Direct link to Adding an NFT to your account")

You've gone through the trouble of creating this NFT contract — you deserve the first NFT!

Protect yourself from snipers by updating the `init` function to give yourself the first `NFT`. You'll need to mint it and save it to your account storage:

`_10

self

_10

.account

_10

.storage

_10

.save(<-self.mintNFT(description: "First one for me!"), to: /storage/BasicNFTPath)`

### NFT capability[​](#nft-capability "Direct link to NFT capability")

Saving the NFT to your account will give you one, but it will be locked away where no apps can see or access it. Since you've just learned how to create capabilities in the previous tutorial, you can use the same techniques here to create a capability to give others the ability to access the NFT.

warning

In Cadence, users own and control their data. A user can destroy a capability such as this whenever they choose. If you want complete control over NFTs or other data, you'd need to store it directly in the contract.

Most of the time, you probably won't want to do this because it will limit what your users can do with their own property without your permission. You don't want to end up in a situation where your users would buy more of your umbrellas to use for shade on sunny days, except you've made it so that they only open when it's raining.

Cadence contracts are deployed to the account of the deployer. As a result, the contract is in the deployer's storage, and the contract itself has read and write access to the storage of the account that they are deployed to by using the built-in [`self.account`](/docs/language/contracts) field. This is an [account reference](/docs/language/accounts/) (`&Account`), authorized and entitled to access and manage all aspects of the account, such as account storage, capabilities, keys, and contracts.

You can access any of the account functions with `self.account` by updating the `init` function to create and publish a [capability](/docs/language/capabilities) allowing public access to the NFT:

`_10

let capability = self

_10

.account

_10

.capabilities

_10

.storage

_10

.issue<&NFT>(/storage/BasicNFTPath)

_10

_10

self

_10

.account

_10

.capabilities

_10

.publish(capability, at: /public/BasicNFTPath)`

danger

The capability you are creating gives everyone full access to all properties of the resource. It does **not** allow other users or developers to move or destroy the resource and is thus harmless.

However, if the resource contained functions to mutate data within the token, this capability would **allow anyone to call it and mutate the data!**

You might be tempted to add this code to `mintNFT` so that you can reuse it for anyone who wants to mint the NFT and automatically create the related capability.

The code will work, but it will **not** function the way you're probably expecting it to. In the context of being called from a function inside a contract, `self.account` refers to the account of the contract deployer, not the caller of the function. That's you!

Adding `self.account.save` or `self.account.publish` to `mintNFT` allows anyone to attempt to mint and publish capabilities to **your** account, so don't do it!

danger

Passing a [fully authorized account reference](/docs/anti-patterns#avoid-using-fully-authorized-account-references-as-a-function-parameter) as a function parameter is a dangerous anti-pattern.

### Deploying and testing[​](#deploying-and-testing "Direct link to Deploying and testing")

Deploy the contract and check the storage for account `0x06`.

You'll be able to find your NFT in the storage for `0x06`:

`_40

"value": {

_40

"value": {

_40

"id": "A.0000000000000006.BasicNFT.NFT",

_40

"fields": [

_40

{

_40

"value": {

_40

"value": "41781441855488",

_40

"type": "UInt64"

_40

},

_40

"name": "uuid"

_40

},

_40

{

_40

"value": {

_40

"value": "1",

_40

"type": "UInt64"

_40

},

_40

"name": "id"

_40

},

_40

{

_40

"value": {

_40

"value": [

_40

{

_40

"key": {

_40

"value": "description",

_40

"type": "String"

_40

},

_40

"value": {

_40

"value": "First one for me!",

_40

"type": "String"

_40

}

_40

}

_40

],

_40

"type": "Dictionary"

_40

},

_40

"name": "metadata"

_40

}

_40

]

_40

},

_40

"type": "Resource"

_40

}`

## Getting the number of an NFT owned by a user[​](#getting-the-number-of-an-nft-owned-by-a-user "Direct link to Getting the number of an NFT owned by a user")

We can see the NFT from the storage view for each account, but it's much more useful to write a script or transaction that can do that for any account. You can follow a similar technique as the last tutorial and create a script to use the capability.

Add a script called `GetNFTNumber` that returns the id number of the NFT owned by an address. It should accept the `Address` of the account you wish to check as an argument.

Try to do this on your own. You should end up with something similar to:

`_12

import BasicNFT from 0x06

_12

_12

access(all) fun main(address: Address): UInt64 {

_12

let account = getAccount(address)

_12

_12

let nftReference = account

_12

.capabilities

_12

.borrow<&BasicNFT.NFT>(/public/BasicNFTPath)

_12

?? panic("Could not borrow a reference\n")

_12

_12

return nftReference.id

_12

}`

## Minting with a transaction[​](#minting-with-a-transaction "Direct link to Minting with a transaction")

You usually don't want a contract with just one NFT given to the account holder. One strategy is to allow anyone who wants to mint an NFT. To do this, you can simply create a transaction that calls the `mintNFT` function you added to your contract, and adds the capability for others to view the NFT:

1. Create a transaction called `MintNFT.cdc` that mints an NFT for the caller with the `description` they provide. You'll need entitlements to borrow values, save values, and issue and publish capabilities.
2. Verify that the NFT isn't already stored in the location used by the contract:

   MintNFT.cdc

   `_15

   import BasicNFT from 0x06

   _15

   _15

   transaction {

   _15

   prepare(account: auth(

   _15

   BorrowValue,

   _15

   SaveValue,

   _15

   IssueStorageCapabilityController,

   _15

   PublishCapability

   _15

   ) &Account) {

   _15

   if account.storage.borrow<&BasicNFT.NFT>(from: /storage/BasicNFTPath) != nil {

   _15

   panic("This user has a token already!")

   _15

   }

   _15

   // TODO

   _15

   }

   _15

   }`
3. Use the `mintNFT` function to create an NFT, and then save that NFT in the user's account storage:

   `_10

   account.storage

   _10

   .save(<-BasicNFT.mintNFT(description: "Hi there!"), to: /storage/BasicNFTPath)`
4. Create and publish a capability to access the NFT:

   `_10

   let capability = account

   _10

   .capabilities

   _10

   .storage

   _10

   .issue<&BasicNFT.NFT>(/storage/BasicNFTPath)

   _10

   _10

   account

   _10

   .capabilities

   _10

   .publish(capability, at: /public/BasicNFTPath)`
5. Call the `MintNFT` transaction from account `0x06`.
   * It will fail because you minted an NFT with `0x06` when you deployed the contract.
6. Call `MintNFT` from account `0x07`. Then, `Execute` the `GetNFTNumber` script for account `0x07`.

You'll see the NFT number `2` returned in the log.

## Performing a basic transfer[​](#performing-a-basic-transfer "Direct link to Performing a basic transfer")

Users, independently or with the help of other developers, have the **inherent ability to delete or transfer any resources in their accounts**, including those created by your contracts. To perform a basic transfer:

1. Open the `Basic Transfer` transaction. We've stubbed out the beginnings of a transfer transaction for you. Note that we're preparing account references for not one, but **two** accounts: the sender and the recipient.

   Basic

   `_10

   import BasicNFT from 0x06

   _10

   _10

   transaction {

   _10

   prepare(

   _10

   signer1: auth(LoadValue) &Account,

   _10

   signer2: auth(SaveValue) &Account

   _10

   ) {

   _10

   // TODO

   _10

   }

   _10

   }`

   * While a transaction is open, you can select one or more accounts to sign a transaction. This is because, in Flow, multiple accounts can sign the same transaction, giving access to their private storage.
2. Write a transaction to execute the transfer. You'll need to `load()` the NFT from `signer1`'s storage and `save()` it into `signer2`'s storage:

   `_14

   import BasicNFT from 0x06

   _14

   _14

   transaction {

   _14

   prepare(

   _14

   signer1: auth(LoadValue) &Account,

   _14

   signer2: auth(SaveValue) &Account

   _14

   ) {

   _14

   let nft <- signer1.storage.load<@BasicNFT.NFT>(from: /storage/BasicNFTPath)

   _14

   ?? panic("Could not load NFT from the first signer's storage")

   _14

   _14

   // WARNING: Incomplete code, see below

   _14

   signer2.storage.save(<-nft, to: /storage/BasicNFTPath)

   _14

   }

   _14

   }`
3. Select both account `0x06` and account `0x08` as the signers. Make sure account `0x06` is the first signer.
4. Click the `Send` button to send the transaction.
5. Verify the NFT is in account storage for account `0x08`.
6. Run the `GetNFTNumber` script to check account `0x08` to see if a user has an NFT.
   * **You'll get an error here.** The reason is that you haven't created or published the capability on account `0x08` to access and return the id number of the NFT owned by that account. You can do this as a part of your transaction, but remember that it isn't required. Another dev, or sophisticated user, could do the transfer **without** publishing a capability.
7. On your own, refactor your transaction to publish a capability in the new owner's account.
   * You're also not making sure that the recipient doesn't already have an NFT in the storage location, so go ahead and add that check as well.

You should end up with something similar to:

`_29

import BasicNFT from 0x06

_29

_29

transaction {

_29

prepare(

_29

signer1: auth(LoadValue) &Account,

_29

signer2: auth(

_29

SaveValue,

_29

IssueStorageCapabilityController,

_29

PublishCapability) &Account

_29

) {

_29

let nft <- signer1.storage.load<@BasicNFT.NFT>(from: /storage/BasicNFTPath)

_29

?? panic("Could not load NFT from the first signer's storage")

_29

_29

if signer2.storage.check<&BasicNFT.NFT>(from: /storage/BasicNFTPath) {

_29

panic("The recipient already has an NFT")

_29

}

_29

_29

signer2.storage.save(<-nft, to: /storage/BasicNFTPath)

_29

_29

let capability = signer2

_29

.capabilities

_29

.storage

_29

.issue<&BasicNFT.NFT>(/storage/BasicNFTPath)

_29

_29

signer2

_29

.capabilities

_29

.publish(capability, at: /public/BasicNFTPath)

_29

}

_29

}`

### Capabilities referencing moved objects[​](#capabilities-referencing-moved-objects "Direct link to Capabilities referencing moved objects")

What about the capability you published for account `0x06` to access the NFT? What happens to that?

Run `GetNFTNumber` for account `0x06` to find out.

**You'll get an error** here as well, but this is expected. Capabilities that reference an object in storage return `nil` if that storage path is empty.

danger

The capability itself is not deleted. If you move an object of the same type back to the storage location reference by the capability, the capability **will** function again.

## Reviewing Basic NFTs[​](#reviewing-basic-nfts "Direct link to Reviewing Basic NFTs")

In this tutorial, you learned how to create a basic NFT with minimal functionality. Your NFT can be held, viewed, and transferred, though it does **not** adhere to the official standard, doesn't allow anyone to own more than one, and is missing other features.

Now that you have completed the tutorial, you should be able to:

* Deploy a basic NFT contract and type definitions.
* Create an NFT object and store it in a user's account storage.
* Write a transaction to mint an NFT and create a capability so others can view it.
* Transfer an NFT from one account to another.
* Use a script to see if an NFT is stored in an account.

In the next tutorial, you'll learn how to make more complete NFTs that allow each user to possess many NFTs from your collection.

## Reference Solution[​](#reference-solution "Direct link to Reference Solution")

warning

You are **not** saving time by skipping the reference implementation. You'll learn much faster by doing the tutorials as presented!

Reference solutions are functional, but may not be optimal.

* [Reference Solution](https://play.flow.com/4a74242f-bf77-4efd-9742-31a2b7580b8e)

---

**Tags:**

* [reference](/docs/tags/reference)
* [NFT](/docs/tags/nft)
* [Non-Fungible Token](/docs/tags/non-fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/05-non-fungible-tokens-1.md)

[Previous

Capabilities](/docs/tutorial/capabilities)[Next

Intermediate NFTs](/docs/tutorial/non-fungible-tokens-2)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [NFTs on Cadence](#nfts-on-cadence)
* [The simplest possible NFT](#the-simplest-possible-nft)
  + [Adding basic metadata](#adding-basic-metadata)
  + [Creating the NFT](#creating-the-nft)
* [Adding an NFT to your account](#adding-an-nft-to-your-account)
  + [NFT capability](#nft-capability)
  + [Deploying and testing](#deploying-and-testing)
* [Getting the number of an NFT owned by a user](#getting-the-number-of-an-nft-owned-by-a-user)
* [Minting with a transaction](#minting-with-a-transaction)
* [Performing a basic transfer](#performing-a-basic-transfer)
  + [Capabilities referencing moved objects](#capabilities-referencing-moved-objects)
* [Reviewing Basic NFTs](#reviewing-basic-nfts)
* [Reference Solution](#reference-solution)