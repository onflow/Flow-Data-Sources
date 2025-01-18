# Source: https://cadence-lang.org/docs/tutorial/non-fungible-tokens-2




5.2 Non-Fungible Token Tutorial Part 2 | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
  + [1. First Steps](/docs/tutorial/first-steps)
  + [2. Hello World](/docs/tutorial/hello-world)
  + [3. Resource Contract Tutorial](/docs/tutorial/resources)
  + [4. Capability Tutorial](/docs/tutorial/capabilities)
  + [5.1 Non-Fungible Token Tutorial Part 1](/docs/tutorial/non-fungible-tokens-1)
  + [5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)
  + [6. Fungible Token Tutorial](/docs/tutorial/fungible-tokens)
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
* [Guide for Solidity Developers](/docs/solidity-to-cadence)
* [Contract Upgrades with Incompatible Changes](/docs/contract-upgrades)
* [JSON-Cadence format](/docs/json-cadence-spec)
* [Measuring Time](/docs/measuring-time)
* [Testing](/docs/testing-framework)


* Tutorial
* 5.2 Non-Fungible Token Tutorial Part 2
On this page
# 5.2 Non-Fungible Token Tutorial Part 2

In this tutorial, we're going to learn about
a full implementation for **Non-Fungible Tokens (NFTs)**.

---


tip

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/63d827b3-0b49-48d5-91ba-4b222c23e217>](https://play.flow.com/63d827b3-0b49-48d5-91ba-4b222c23e217)

The tutorial will ask you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout box like this one.
These highlighted actions are all that you need to do to get your code running,
but reading the rest is necessary to understand the language's design.

## Storing Multiple NFTs in a Collection[​](#storing-multiple-nfts-in-a-collection "Direct link to Storing Multiple NFTs in a Collection")

In the [last tutorial](/docs/tutorial/non-fungible-tokens-1),
we created a simple `NFT` resource, stored in at a storage path,
then used a multi-sig transaction to transfer it from one account to another.

It should hopefully be clear that the setup and operations that we used
in the previous tutorial are not very scalable. Users need a way
to manage all of their NFTs from a single place.

There are some different ways we could accomplish this.

* We could store all of our NFTs in an array or dictionary, like so.

 `_11// Define a dictionary to store the NFTs in_11let myNFTs: @{Int: BasicNFT.NFT} = {}_11_11// Create a new NFT_11let newNFT <- BasicNFT.createNFT(id: 1)_11_11// Save the new NFT to the dictionary_11myNFTs[newNFT.id] <- newNFT_11_11// Save the NFT to a new storage path_11account.storage.save(<-myNFTs, to: /storage/basicNFTDictionary)`
## Dictionaries[​](#dictionaries "Direct link to Dictionaries")

This example uses a [**Dictionary**: a mutable, unordered collection of key-value associations](/docs/language/values-and-types#dictionaries).

 `_10// Keys are `Int`_10// Values are `NFT`_10access(all) let myNFTs: @{Int: NFT}`

In a dictionary, all keys must have the same type, and all values must have the same type.
In this case, we are mapping integer (`Int`) IDs to `NFT` resource objects
so that there is one `NFT` for each `Int` that exists in the dictionary.

Dictionary definitions don't usually have the `@` symbol in the type specification,
but because the `myNFTs` mapping stores resources, the whole field also has to become a resource type,
which is why the field has the `@` symbol indicating that it is a resource type.

This means that all the rules that apply to resources apply to this type.

Using a dictionary to store our NFTs would solve the problem
of having to use different storage paths for each NFT, but it doesn't solve all the problems.
These types are relatively opaque and don't have much useful functionality on their own.

Instead, we can use a powerful feature of Cadence, resources owning other resources!
We'll define a new `Collection` resource as our NFT storage place
to enable more-sophisticated ways to interact with our NFTs.

The next contract we look at is called `ExampleNFT`, it's stored in Contract 1 in account `0x06`.

This contract expands on the `BasicNFT` we looked at by adding:

1. An `idCount` contract field that tracks unique NFT ids.
2. An `NFTReceiver` interface that specifies three public functions for the collection.
3. Declares a resource called `Collection` that acts as a place to intuitively store and manage
   your NFTs. It implements the `NFTReceiver` interface
4. The `Collection` will declare fields and functions to interact with it,
   including `ownedNFTs`, `init()`, `withdraw()`, and other important functions
5. Next, the contract declares functions that create a new NFT (`mintNFT()`)
   and an empty collection (`createEmptyCollection()`)
6. Finally, the contract declares an initializer that initializes the path fields,
   creates an empty collection as well as a reference to it,
   and saves a minter resource to account storage.

This contract introduces a few new concepts, we'll look at the new contract, then break down all the new
concepts this contract introduces.

Action

Open the `ExampleNFT` contract.

Deploy the contract by clicking the Deploy button in the bottom right of the editor.

`ExampleNFT.cdc` should contain the code below.
It contains what was already in `BasicNFT.cdc` plus additional resource declarations in the contract body.


ExampleNFT.cdc `_118/// ExampleNFT.cdc_118///_118/// This is a complete version of the ExampleNFT contract_118/// that includes withdraw and deposit functionalities, as well as a_118/// collection resource that can be used to bundle NFTs together._118///_118/// Learn more about non-fungible tokens in this tutorial: https://developers.flow.com/cadence/tutorial/non-fungible-tokens-1_118_118access(all) contract ExampleNFT {_118_118 // Declare Path constants so paths do not have to be hardcoded_118 // in transactions and scripts_118_118 access(all) let CollectionStoragePath: StoragePath_118 access(all) let CollectionPublicPath: PublicPath_118 access(all) let MinterStoragePath: StoragePath_118_118 // Tracks the unique IDs of the NFTs_118 access(all) var idCount: UInt64_118_118 // Declare the NFT resource type_118 access(all) resource NFT {_118 // The unique ID that differentiates each NFT_118 access(all) let id: UInt64_118_118 // Initialize both fields in the initializer_118 init(initID: UInt64) {_118 self.id = initID_118 }_118 }_118_118 access(all) entitlement Withdraw_118_118 // The definition of the Collection resource that_118 // holds the NFTs that a user owns_118 access(all) resource Collection {_118 // dictionary of NFT conforming tokens_118 // NFT is a resource type with an `UInt64` ID field_118 access(all) var ownedNFTs: @{UInt64: NFT}_118_118 // Initialize the NFTs field to an empty collection_118 init () {_118 self.ownedNFTs <- {}_118 }_118_118 // withdraw_118 //_118 // Function that removes an NFT from the collection_118 // and moves it to the calling context_118 access(Withdraw) fun withdraw(withdrawID: UInt64): @NFT {_118 // If the NFT isn't found, the transaction panics and reverts_118 let token <- self.ownedNFTs.remove(key: withdrawID)_118 ?? panic("Could not withdraw an ExampleNFT.NFT with id="_118 .concat(withdrawID.toString())_118 .concat("Verify that the collection owns the NFT ")_118 .concat("with the specified ID first before withdrawing it."))_118_118 return <-token_118 }_118_118 // deposit_118 //_118 // Function that takes a NFT as an argument and_118 // adds it to the collections dictionary_118 access(all) fun deposit(token: @NFT) {_118 // add the new token to the dictionary with a force assignment_118 // if there is already a value at that key, it will fail and revert_118 self.ownedNFTs[token.id] <-! token_118 }_118_118 // idExists checks to see if a NFT_118 // with the given ID exists in the collection_118 access(all) view fun idExists(id: UInt64): Bool {_118 return self.ownedNFTs[id] != nil_118 }_118_118 // getIDs returns an array of the IDs that are in the collection_118 access(all) view fun getIDs(): [UInt64] {_118 return self.ownedNFTs.keys_118 }_118 }_118_118 // creates a new empty Collection resource and returns it_118 access(all) fun createEmptyCollection(): @Collection {_118 return <- create Collection()_118 }_118_118 // mintNFT_118 //_118 // Function that mints a new NFT with a new ID_118 // and returns it to the caller_118 access(all) fun mintNFT(): @NFT {_118_118 // create a new NFT_118 var newNFT <- create NFT(initID: self.idCount)_118_118 // change the id so that each ID is unique_118 self.idCount = self.idCount + 1_118_118 return <-newNFT_118 }_118_118 init() {_118 self.CollectionStoragePath = /storage/nftTutorialCollection_118 self.CollectionPublicPath = /public/nftTutorialCollection_118 self.MinterStoragePath = /storage/nftTutorialMinter_118_118 // initialize the ID count to one_118 self.idCount = 1_118_118 // store an empty NFT Collection in account storage_118 self.account.storage.save(<-self.createEmptyCollection(), to: self.CollectionStoragePath)_118_118 // publish a capability to the Collection in storage_118 let cap = self.account.capabilities.storage.issue<&Collection>(self.CollectionStoragePath)_118 self.account.capabilities.publish(cap, at: self.CollectionPublicPath)_118 }_118}`

This smart contract more closely resembles a contract
that a project would actually use in production, but still does not use the official NFT standard,
so it should not be used in any production code.

Any user who owns one or more `ExampleNFT` should have an instance
of this `@ExampleNFT.Collection` resource stored in their account.
This collection stores all of their NFTs in a dictionary that maps integer IDs to `@NFT`s.

Each collection has a `deposit` and `withdraw` function.
These functions allow users to follow the pattern of moving tokens in and out of
their collections through a standard set of functions.

When a user wants to store NFTs in their account,
they will create an empty `Collection` by calling the `createEmptyCollection()` function in the `ExampleNFT` smart contract.
This returns an empty `Collection` object that they can store in their account storage.

There are a few new features that we use in this example, so let's walk through them.

## The Resource Dictionary[​](#the-resource-dictionary "Direct link to The Resource Dictionary")

We discussed above that when a dictionary stores a resource, it also becomes a resource!

This means that the collection has to have special rules for how to handle its own resource.
You wouldn't want it getting lost by accident!

As we learned in the resource tutorial, you can destroy any resource
by explicitly invoking the `destroy` command.

When the NFT `Collection` resource is destroyed with the `destroy` command,
all the resources stored in the dictionary are also `destroy`ed.

When the `Collection` resource is created, the initializer is run
and must explicitly initialize all member variables.
This helps prevent issues in some smart contracts where uninitialized fields can cause bugs.
The initializer can never run again after this.
Here, we initialize the dictionary as a resource type with an empty dictionary.

 `_10init () {_10 self.ownedNFTs <- {}_10}`

Another feature for dictionaries is the ability to get an array
of the keys of the dictionary using the built-in `keys` function.

 `_10// getIDs returns an array of the IDs that are in the collection_10access(all) view fun getIDs(): [UInt64] {_10 return self.ownedNFTs.keys_10}`

This can be used to iterate through the dictionary or just to see a list of what is stored.
As you can see, [a variable length array type](/docs/language/values-and-types#arrays)
is declared by enclosing the member type within square brackets (`[UInt64]`).

## Resources Owning Resources[​](#resources-owning-resources "Direct link to Resources Owning Resources")

This NFT Collection example in `ExampleNFT.cdc` illustrates an important feature: resources can own other resources.

In the example, a user can transfer one NFT to another user.
Additionally, since the `Collection` explicitly owns the NFTs in it,
the owner could transfer all of the NFTs at once by just transferring the single collection.

This is an important feature because it enables numerous additional use cases.
In addition to allowing easy batch transfers,
this means that if a unique NFT wants to own another unique NFT,
like a CryptoKitty owning a hat accessory,
the Kitty literally stores the hat in its own fields and effectively owns it.
The hat belongs to the CryptoKitty that it is stored in,
and the hat can be transferred separately or along with the CryptoKitty that owns it.

This also brings up an interesting wrinkle in Cadence in regards to ownership.
In other ledger-based languages, ownership is indicated by account addresses.
Cadence is a fully object-oriented language, so ownership is indicated by where
an object is stored, not just an entry on a ledger.

Resources can own other resources, which means that with some interesting logic,
a resource can have more control over the resources it owns than the actual
person whose account it is stored in!

You'll encounter more fascinating implications of ownership and interoperability
like this as you get deeper into Cadence.

Now, back to the tutorial!

## Restricting Access to the NFT Collection[​](#restricting-access-to-the-nft-collection "Direct link to Restricting Access to the NFT Collection")

In the NFT Collection, we will publish a capability to allow anyone
to access important functionality for our `Collection`, like `deposit()` and `getIDs()`.

This is where an important layer of access control comes in.
Cadence utilizes [capability security](/docs/language/capabilities),
which means that for any given object, a user is allowed to access a field or method of that object if they either:

* Are the owner of the object
* Have a valid reference to that field or method (note that references can only be created from capabilities, and capabilities can only be created by the owner of the object)

When a user stores their NFT `Collection` in their account storage,
it is by default not available for other users to access
because it requires access to the authorized account object (`auth(Storage) &Account`)
which is only accessible by a transaction that the owner authorizes and signs.

To give external accounts access to the `access(all)` fields and functions,
the owner creates a link to the object in storage.

This link creates a capability. From there, the owner can then do whatever they want with that capability:
they could pass it as a parameter to a function for one-time-use,
or they could put in the `/public/` domain of their account so that anyone can access it.

The creation and publishing of the capability is seen
in the `ExampleNFT.cdc` contract initializer.

 `_10// publish a capability to the Collection in storage_10let cap = self.account.capabilities.storage.issue<&Collection>(self.CollectionStoragePath)_10self.account.capabilities.publish(cap, at: self.CollectionPublicPath)`

The `issue` function specifies that the capability is typed as `&Collection`.
Then the link is published to `/public/` which is accessible by anyone.
The link targets the `/storage/NFTCollection` (through the `self.CollectionStoragePath` contract field) that we created earlier.

Now the user has an NFT collection in their account `/storage/`,
along with a capability for it that others can use to see what NFTs they own and to send an NFT to them.

Let's confirm this is true by running a script!

## Run a Script[​](#run-a-script "Direct link to Run a Script")

---

Scripts in Cadence are simple transactions that run without any account permissions and only read information from the blockchain.

Action

Open the script file named `Print 0x06 NFTs`.
`Print 0x06 NFTs` should contain the following code:


 `_20import ExampleNFT from 0x06_20_20// Print the NFTs owned by account 0x06._20access(all) fun main(): [UInt64] {_20 // Get the public account object for account 0x06_20 let nftOwner = getAccount(0x06)_20_20 // Find the public Receiver capability for their Collection and borrow it_20 let receiverRef = nftOwner.capabilities_20 .borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_20 ?? panic("Could not borrow a receiver reference to 0x06's ExampleNFT.Collection"_20 .concat(" from the path ")_20 .concat(ExampleNFT.CollectionPublicPath.toString())_20 .concat(". Make sure account 0x06 has set up its account ")_20 .concat("with an ExampleNFT Collection."))_20_20 // Log the NFTs that they own as an array of IDs_20 log("Account 1 NFTs")_20 return receiverRef.getIDs()_20}`
Action

Execute `Print 0x06 NFTs` by clicking the Execute button in the top right of the editor box.

This script returns a list of the NFTs that account `0x06` owns.

Because account `0x06` currently doesn't own any in its collection, it will just print an empty array:

 `_10"Account 1 NFTs"_10Result > []`

If the script cannot be executed, it probably means that the NFT collection hasn't been stored correctly in account `0x06`.
If you run into issues, make sure that you deployed the contract in account `0x06` and that you followed the previous steps correctly.

## Using Entitlements[​](#using-entitlements "Direct link to Using Entitlements")

We do not want everyone in the network to be able to call our `withdraw` function though.
In Cadence, any reference can be freely up-casted or down-casted to any subtype or supertype
that the reference conforms to. This means that if I had a reference of the type
`&ExampleNFT.Collection`, this would expose all the `access(all)` functions on the `Collection`.

This is a powerful feature that is very useful, but developers need to understand that
this means that if there is any privileged functionality on a resource that has a
public capability, then this functionality cannot be `access(all)`.
It needs to use [Entitlements](/docs/language/access-control#entitlements).

Entitlements enable authors to restrict the scope of access
at a granular level with the option to group restrictions
under similarly name entitlements. Owners of resources can then
use these entitlements to grant access to the subset of actions
enabled by the authorized reference.

As you can see in our NFT contract, we've added an entitlement:

 `_10access(all) entitlement Withdraw`

We also added this entitlement to the `withdraw()` method:

 `_10access(Withdraw) fun withdraw(withdrawID: UInt64): @NFT {`

A function with entitled access means that that function is callable by someone
with a concrete object of the containing type as if it were `access(all)`,
but it is not callable from a regular reference to that object.
So if I borrowed a public reference to the `Collection` above of the type `&ExampleNFT.Collection`,
I could call every function and access every field on it except the `withdraw()` function.

 `_10// Get the public capability and borrow a reference from it_10let collectionRef = recipient.capabilities_10 .borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_10 ?? panic("Could not borrow a reference to the ExampleNFT.Collection")_10_10// Try to withdraw an NFT from their collection_10// ERROR: The reference is not entitled, so this call is not possible and will FAIL_10let stolenNFT <- collectionRef.withdraw(withdrawID: 1)`

In order to access an **entitled field or function** through a reference,
the reference needs to also be **entitled**. This means that when
the reference or capability is created, the owner of that object
has to explicitly specify that is has that entitlement.

The owner of an object is the only one who can create an entitled capability or reference.
In the above example, if you wanted to make your withdraw function publicly accessible,
you would issue the capability as an entitled capability
by specifying all the entitlements in the capability's type specification
using the `auth` keyword:

 `_10// publish an entitled capability to the Collection in storage_10// This capability is issued with the `auth(ExampleNFT.Withdraw)` entitlement_10// This gives access to the withdraw function_10let cap = self.account.capabilities.storage.issue<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>(self.CollectionStoragePath)_10self.account.capabilities.publish(cap, at: self.CollectionPublicPath)`

Now, anyone could borrow that capability as the entitled version it was issued as:

 `_10// Get the public entitled capability and borrow a reference from it_10let entitledCollectionRef = recipient.capabilities_10 .borrow<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_10 ?? panic("Could not borrow a reference to the ExampleNFT.Collection")_10_10// Try to withdraw an NFT from their collection_10// This will succeed because the reference is entitled_10let stolenNFT <- entitledCollectionRef.withdraw(withdrawID: 1)`

Obviously, you would not want to create a public entitled reference like this
because you don't want anyone accessing your withdraw function.
Entitlements are primarily meant for sharing private capabilities with small subsets
of trusted users or smart contracts and should never be used for public capabilities.

The most important thing to remember is, if you don't want everyone in the network
to be able to access a function on a resource, you should default
put an entitlement on that function. Better to be safe than sorry.

## Mint and Distribute Tokens[​](#mint-and-distribute-tokens "Direct link to Mint and Distribute Tokens")

---

One way to create NFTs is by having an admin mint new tokens and send them to a user.
For the purpose of learning, we are simply implementing minting as a public function here.
Normally, most would implement restricted minting by having an NFT Minter resource.
This would restrict minting, because the owner of this resource is the only one that can mint tokens.

You can see an example of this in the [Marketplace tutorial](/docs/tutorial/marketplace-compose).

Action

Open the file named `Mint NFT`.
Select account `0x06` as the only signer and send the transaction.

This transaction deposits the minted NFT into the account owner's NFT collection:


mint\_nft.cdc `_31import ExampleNFT from 0x06_31_31// This transaction allows the Minter account to mint an NFT_31// and deposit it into its own collection._31_31transaction {_31_31 // The reference to the collection that will be receiving the NFT_31 let receiverRef: &ExampleNFT.Collection_31_31 prepare(acct: auth(BorrowValue) &Account) {_31 // Get the owner's collection capability and borrow a reference_31 self.receiverRef = acct.capabilities_31 .borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_31 ?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"_31 .concat(" from the path ")_31 .concat(ExampleNFT.CollectionPublicPath.toString())_31 .concat(". Make sure account 0x06 has set up its account ")_31 .concat("with an ExampleNFT Collection."))_31 }_31_31 execute {_31 // Use the minter reference to mint an NFT, which deposits_31 // the NFT into the collection that is sent as a parameter._31 let newNFT <- ExampleNFT.mintNFT()_31_31 self.receiverRef.deposit(token: <-newNFT)_31_31 log("NFT Minted and deposited to Account 0x06's Collection")_31 }_31}`
Action

Reopen `Print 0x06 NFTs` and execute the script.
This prints a list of the NFTs that account `0x06` owns.


print\_06\_nfts.cdc `_22import ExampleNFT from 0x06_22_22// Print the NFTs owned by account 0x06._22access(all) fun main(): [UInt64] {_22 // Get the public account object for account 0x06_22 let nftOwner = getAccount(0x06)_22_22 // Find the public Receiver capability for their Collection_22 let capability = nftOwner.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_22_22 // borrow a reference from the capability_22 let receiverRef = capability.borrow()_22 ?? panic("Could not borrow a receiver reference to 0x06's ExampleNFT.Collection"_22 .concat(" from the path ")_22 .concat(ExampleNFT.CollectionPublicPath.toString())_22 .concat(". Make sure account 0x06 has set up its account ")_22 .concat("with an ExampleNFT Collection."))_22_22 // Log the NFTs that they own as an array of IDs_22 log("Account 0x06 NFTs")_22 return receiverRef.getIDs()_22}`

You should see that account `0x06` owns the NFT with `id = 1`

 `_10"Account 0x06 NFTs"_10[1]`
## Transferring an NFT[​](#transferring-an-nft "Direct link to Transferring an NFT")

Before we are able to transfer an NFT to another account, we need to set up that account
with an NFTCollection of their own so they are able to receive NFTs.

Action

Open the file named `Setup Account` and submit the transaction, using account `0x07` as the only signer.


SetupAccount.cdc `_23import ExampleNFT from 0x06_23_23// This transaction configures a user's account_23// to use the NFT contract by creating a new empty collection,_23// storing it in their account storage, and publishing a capability_23transaction {_23 prepare(acct: auth(SaveValue, Capabilities) &Account) {_23_23 // Create a new empty collection_23 let collection <- ExampleNFT.createEmptyCollection()_23_23 // store the empty NFT Collection in account storage_23 acct.storage.save(<-collection, to: ExampleNFT.CollectionStoragePath)_23_23 log("Collection created for account 0x07")_23_23 // create a public capability for the Collection_23 let cap = acct.capabilities.storage.issue<&ExampleNFT.Collection>(ExampleNFT.CollectionStoragePath)_23 acct.capabilities.publish(cap, at: ExampleNFT.CollectionPublicPath)_23_23 log("Capability created")_23 }_23}`

Account `0x07` should now have an empty `Collection` resource stored in its account storage.
It has also created and stored a capability to the collection in its `/public/` domain.

Action

Open the file named `Transfer`, select account `0x06` as the only signer, and send the transaction.

This transaction transfers a token from account `0x06` to account `0x07`.


transfer\_nft.cdc `_46import ExampleNFT from 0x06_46_46// This transaction transfers an NFT from one user's collection_46// to another user's collection._46transaction {_46_46 // The field that will hold the NFT as it is being_46 // transferred to the other account_46 let transferToken: @ExampleNFT.NFT_46_46 prepare(acct: auth(BorrowValue) &Account) {_46_46 // Borrow a reference from the stored collection_46 let collectionRef = acct.storage_46 .borrow<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>(from: ExampleNFT.CollectionStoragePath)_46 ?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"_46 .concat(" from the path ")_46 .concat(ExampleNFT.CollectionPublicPath.toString())_46 .concat(". Make sure account 0x06 has set up its account ")_46 .concat("with an ExampleNFT Collection."))_46_46 // Call the withdraw function on the sender's Collection_46 // to move the NFT out of the collection_46 self.transferToken <- collectionRef.withdraw(withdrawID: 1)_46 }_46_46 execute {_46 // Get the recipient's public account object_46 let recipient = getAccount(0x07)_46_46 // Get the Collection reference for the receiver_46 // getting the public capability and borrowing a reference from it_46 let receiverRef = recipient.capabilities_46 .borrow<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_46 ?? panic("Could not borrow a collection reference to 0x07's ExampleNFT.Collection"_46 .concat(" from the path ")_46 .concat(ExampleNFT.CollectionPublicPath.toString())_46 .concat(". Make sure account 0x07 has set up its account ")_46 .concat("with an ExampleNFT Collection."))_46_46 // Deposit the NFT in the receivers collection_46 receiverRef.deposit(token: <-self.transferToken)_46_46 log("NFT ID 1 transferred from account 0x06 to account 0x07")_46 }_46}`

See, with the use of Collections and capabilities, now the only account
that needs to sign a transaction to transfer a token is the one who is sending the token.

Now we can check both accounts' collections to make sure that account `0x07` owns the token and account `0x06` has nothing.

Action

Execute the script `Print all NFTs` to see the tokens in each account:


print\_all\_owned\_nfts.cdc `_35import ExampleNFT from 0x06_35_35// Print the NFTs owned by accounts 0x06 and 0x07._35access(all) fun main() {_35_35 // Get both public account objects_35 let account6 = getAccount(0x06)_35 let account7 = getAccount(0x07)_35_35 // Find the public Receiver capability for their Collections_35 let acct6Capability = account6.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_35 let acct7Capability = account7.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_35_35 // borrow references from the capabilities_35 let receiver6Ref = acct6Capability.borrow()_35 ?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"_35 .concat(" from the path ")_35 .concat(ExampleNFT.CollectionPublicPath.toString())_35 .concat(". Make sure account 0x06 has set up its account ")_35 .concat("with an ExampleNFT Collection."))_35_35 let receiver7Ref = acct7Capability.borrow()_35 ?? panic("Could not borrow a collection reference to 0x07's ExampleNFT.Collection"_35 .concat(" from the path ")_35 .concat(ExampleNFT.CollectionPublicPath.toString())_35 .concat(". Make sure account 0x07 has set up its account ")_35 .concat("with an ExampleNFT Collection."))_35_35 // Print both collections as arrays of IDs_35 log("Account 0x06 NFTs")_35 log(receiver6Ref.getIDs())_35_35 log("Account 0x07 NFTs")_35 log(receiver7Ref.getIDs())_35}`

You should see something like this in the output:

 `_10"Account 0x06 NFTs"_10[]_10"Account 0x07 NFTs"_10[1]`

Account `0x07` has one NFT with ID=1 and account `0x06` has none.
This shows that the NFT was transferred from account `0x06` to account `0x07`.

![](https://storage.googleapis.com/flow-resources/documentation-assets/cadence-tuts/accounts-nft-storage.png)

Congratulations, you now have a working NFT!

## Putting It All Together[​](#putting-it-all-together "Direct link to Putting It All Together")

---

This was only a basic example how a NFT might work on Flow.
Please refer to the [Flow NFT Standard repo](https://github.com/onflow/flow-nft)
and the [NFT Developer Guide](https://developers.flow.com/build/guides/nft)
for information about the official Flow NFT standard and how to implement
a real version of an NFT smart contract.

## Fungible Tokens[​](#fungible-tokens "Direct link to Fungible Tokens")

---

Now that you have a working NFT, you will probably want to be able to trade it. For that you are going to need to
understand how fungible tokens work on Flow, so go ahead and move to the next tutorial!

**Tags:**

* [reference](/docs/tags/reference)
* [NFT](/docs/tags/nft)
* [Non-Fungible Token](/docs/tags/non-fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/05-non-fungible-tokens-2.md)[Previous5.1 Non-Fungible Token Tutorial Part 1](/docs/tutorial/non-fungible-tokens-1)[Next6. Fungible Token Tutorial](/docs/tutorial/fungible-tokens)
###### Rate this page

😞😐😊

* [Storing Multiple NFTs in a Collection](#storing-multiple-nfts-in-a-collection)
* [Dictionaries](#dictionaries)
* [The Resource Dictionary](#the-resource-dictionary)
* [Resources Owning Resources](#resources-owning-resources)
* [Restricting Access to the NFT Collection](#restricting-access-to-the-nft-collection)
* [Run a Script](#run-a-script)
* [Using Entitlements](#using-entitlements)
* [Mint and Distribute Tokens](#mint-and-distribute-tokens)
* [Transferring an NFT](#transferring-an-nft)
* [Putting It All Together](#putting-it-all-together)
* [Fungible Tokens](#fungible-tokens)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

