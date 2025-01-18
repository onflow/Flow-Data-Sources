# Source: https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1




5.1 Non-Fungible Token Tutorial Part 1 | Cadence




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
* 5.1 Non-Fungible Token Tutorial Part 1
On this page
# 5.1 Non-Fungible Token Tutorial Part 1

In this tutorial, we're going to deploy, store, and transfer **Non-Fungible Tokens (NFTs)**.

---


tip

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/dde1e2a4-aae6-4eda-86fd-f0b0b3f53f7e>](https://play.flow.com/dde1e2a4-aae6-4eda-86fd-f0b0b3f53f7e)

The tutorial will ask you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout box like this one.
These highlighted actions are all that you need to do to get your code running,
but reading the rest is necessary to understand the language's design.

The NFT is an integral part of blockchain technology.
An NFT is a digital asset that represents ownership of a unique asset.
NFTs are also indivisible, you can't trade part of an NFT.
Possible examples of NFTs include:
CryptoKitties, Top Shot Moments, tickets to a really fun concert, or a horse.

Instead of being represented in a central ledger, like in most smart contract languages,
Cadence represents each NFT as a [resource object](/docs/language/resources)
that users store in their accounts.

This allows NFTs to benefit from the resource ownership rules
that are enforced by the [type system](/docs/language/values-and-types) -
resources can only have a single owner, they cannot be duplicated,
and they cannot be lost due to accidental or malicious programming errors.
These protections ensure that owners know that their NFT is safe and can represent an asset that has real value.

NFTs in a real-world context make it possible to trade assets and
prove who the owner of an asset is.
On Flow, NFTs are interoperable -
so the NFTs in an account can be used in different smart contracts and app contexts.
All NFTs on Flow implement the [Flow NFT Standard](https://github.com/onflow/flow-nft)
which defines a basic set of properties for NFTs on Flow.
This tutorial, will teach you a basic method of creating NFTs
to illustrate important language concepts, but will not use the NFT Standard
for the sake of simplicity and learning.

After completing the NFT tutorials, readers should visit
[the NFT Guide](https://developers.flow.com/build/guides/nft) and
[the NFT standard GitHub repository](https://github.com/onflow/flow-nft)
to learn how full, production-ready NFTs are created.

To get you comfortable using NFTs, this tutorial will teach you to:

1. Deploy a basic NFT contract and type definitions.
2. Create an NFT object and store it in your account storage.
3. Create an NFT collection object to store multiple NFTs in your account.
4. Create an `NFTMinter` and use it to mint an NFT.
5. Create capabilities to your collection that others can use to send you tokens.
6. Set up another account the same way.
7. Transfer an NFT from one account to another.
8. Use a script to see what NFTs are stored in each account's collection.

warning

It is important to remember that while this tutorial implements a working
non-fungible token, it has been simplified for educational purposes and is not
what any project should use in production. See the
[Flow Fungible Token standard](https://github.com/onflow/flow-nft)
for the standard interface and example implementation.

**Before proceeding with this tutorial**, we highly recommend
following the instructions in [Getting Started](/docs/tutorial/first-steps),
[Hello, World!](/docs/tutorial/hello-world),
[Resources](/docs/tutorial/resources),
and [Capabilities](/docs/tutorial/capabilities)
to learn how to use the Playground tools and to learn the fundamentals of Cadence.
This tutorial will build on the concepts introduced in those tutorials.

## Non-Fungible Tokens on the Flow Emulator[​](#non-fungible-tokens-on-the-flow-emulator "Direct link to Non-Fungible Tokens on the Flow Emulator")

---

In Cadence, each NFT is represented by a resource with an integer ID:

 `_11// The most basic representation of an NFT_11access(all) resource NFT {_11 // The unique ID that differentiates each NFT_11 access(all)_11 let id: UInt64_11_11 // Initialize both fields in the initializer_11 init(initID: UInt64) {_11 self.id = initID_11 }_11}`

Resources are a perfect type to represent NFTs
because resources have important ownership rules that are enforced by the type system.
They can only have one owner, cannot be copied, and cannot be accidentally or maliciously lost or duplicated.
These protections ensure that owners know that their NFT is safe and can represent an asset that has real value.
For more information about resources, see the [resources tutorial](/docs/tutorial/resources)

An NFT is also usually represented by some sort of metadata like a name or a picture.
Historically, most of this metadata has been stored off-chain,
and the on-chain token only contains a URL or something similar that points to the off-chain metadata.
In Flow, this is possible, but the goal is to make it possible for all the metadata associated with a token to be stored on-chain.
This is out of the scope of this tutorial though.
This paradigm has been defined by the Flow community and the details are contained in
[the NFT metadata guide](https://developers.flow.com/build/advanced-concepts/metadata-views).

When users on Flow want to transact with each other,
they can do so peer-to-peer and without having to interact with a central NFT contract
by calling resource-defined methods in both users' accounts.

## Adding an NFT Your Account[​](#adding-an-nft-your-account "Direct link to Adding an NFT Your Account")

We'll start by looking at a basic NFT contract that adds an NFT to an account.
The contract will:

1. Create a smart contract with the NFT resource type.
2. Declare an ID field, a metadata field and an initializer in the NFT resource.
3. Create an initializer for the contract that saves an NFT to an account.

This contract relies on the [account storage API](/docs/language/accounts/storage)
to save NFTs in the account.

Action

First, you'll need to follow this link to open a playground session
with the Non-Fungible Token contracts, transactions, and scripts pre-loaded:

[<https://play.flow.com/dde1e2a4-aae6-4eda-86fd-f0b0b3f53f7e>](https://play.flow.com/dde1e2a4-aae6-4eda-86fd-f0b0b3f53f7e)
Action

Open Account `0x06` to see `BasicNFT.cdc`.
`BasicNFT.cdc` should contain the following code:


BasicNFT.cdc `_27access(all) contract BasicNFT {_27_27 // Declare the NFT resource type_27 access(all) resource NFT {_27 // The unique ID that differentiates each NFT_27 access(all) let id: UInt64_27_27 // String mapping to hold metadata_27 access(all) var metadata: {String: String}_27_27 // Initialize both fields in the initializer_27 init(initID: UInt64) {_27 self.id = initID_27 self.metadata = {}_27 }_27 }_27_27 // Function to create a new NFT_27 access(all) fun createNFT(id: UInt64): @NFT {_27 return <-create NFT(initID: id)_27 }_27_27 // Create a single new NFT and save it to account storage_27 init() {_27 self.account.storage.save(<-create NFT(initID: 1), to: /storage/BasicNFTPath)_27 }_27}`

In the above contract, the NFT is a resource with an integer ID and a field for metadata.

Each NFT resource should have a unique ID, so they cannot be combined or duplicated
unless the smart contract allows it.

Another unique feature of this design is that each NFT can contain its own metadata.
In this example, we use a simple `String`-to-`String` mapping, but you could imagine a [much more rich
version](https://github.com/onflow/flow-nft#nft-metadata)
that can allow the storage of complex file formats and other such data.

An NFT could even own other NFTs! This functionality is shown in a later tutorial.

### Initializers[​](#initializers "Direct link to Initializers")

 `_10init() {_10// ...`

All composite types like contracts, resources,
and structs can have an optional initializer that only runs when the object is initially created.
Cadence requires that all fields in a composite type must be explicitly initialized,
so if the object has any fields, this function has to be used to initialize them.

Contracts also have read and write access to the storage of the account that they are deployed to
by using the built-in [`self.account`](/docs/language/contracts) field.
This is an [account reference](/docs/language/accounts/) (`&Account`),
authorized and entitled to access and manage all aspects of the account,
such as account storage, capabilities, keys, and contracts.

In the contract's initializer, we create a new NFT object and move it into the account storage.

 `_10// put it in storage_10self.account.storage.save(<-create NFT(initID: 1), to: /storage/BasicNFTPath)`

Here we access the storage object of the account that the contract is deployed to and call its `save` method.
We also create the NFT in the same line and pass it as the first argument to `save`.
We save it to the `/storage/` domain, where objects are meant to be stored.

Action

Deploy `BasicNFT` by clicking the Deploy button in the top right of the editor.

You should now have an NFT in your account. Let's run a transaction to check.

Action

Open the `NFT Exists` transaction, select account `0x06` as the only signer, and send the transaction.

`NFT Exists` should look like this:


NFTExists.cdc `_13import BasicNFT from 0x06_13_13// This transaction checks if an NFT exists in the storage of the given account_13// by trying to borrow from it. If the borrow succeeds (returns a non-nil value), the token exists!_13transaction {_13 prepare(acct: auth(BorrowValue) &Account) {_13 if acct.storage.borrow<&BasicNFT.NFT>(from: /storage/BasicNFTPath) != nil {_13 log("The token exists!")_13 } else {_13 log("No token found!")_13 }_13 }_13}`

Here, we are trying to directly borrow a reference from the NFT in storage.
If the object exists, the borrow will succeed and the reference optional will not be `nil`,
but if the borrow fails, the optional will be `nil`.

You should see something that says `"The token exists!"`.

Great work! You have your first NFT in your account. Let's move it to another account!

## Performing a Basic Transfer[​](#performing-a-basic-transfer "Direct link to Performing a Basic Transfer")

With these powerful assets in your account, you'll probably want to
move them around to other accounts. There are many ways to transfer objects in Cadence,
but we'll show the simplest one first.

This will also be an opportunity for you to try to write some of your own code!

Action

Open the `Basic Transfer` transaction.

`Basic Transfer` should look like this:


 `_16import BasicNFT from 0x06_16_16/// Basic transaction for two accounts to authorize_16/// to transfer an NFT_16_16transaction {_16 prepare(_16 signer1: auth(LoadValue) &Account,_16 signer2: auth(SaveValue) &Account_16 ) {_16_16 // Fill in code here to load the NFT from signer1_16 // and save it into signer2's storage_16_16 }_16}`

We've provided you with a blank transaction with two signers.

While a transaction is open, you can select one or more accounts to sign a transaction.
This is because, in Flow, multiple accounts can sign the same transaction,
giving access to their private storage. If multiple accounts are selected as signers,
this needs to be reflected in the signature of the transaction to show multiple signers,
as is shown in the "Basic Transfer" transaction.

All you need to do is `load()` the NFT from `signer1`'s storage and `save()` it
into `signer2`'s storage. You have used both of these operations before,
so this hopefully shouldn't be too hard to figure out.
Feel free to go back to earlier tutorials to see examples of these account methods.

You can also scroll down a bit to see the correct code:

---


---


---


---


---


---


---


---


---

Here is the correct code to load the NFT from one account and save it to another account.

 `_20import BasicNFT from 0x06_20_20/// Basic transaction for two accounts to authorize_20/// to transfer an NFT_20_20transaction {_20 prepare(_20 signer1: auth(LoadValue) &Account,_20 signer2: auth(SaveValue) &Account_20 ) {_20_20 // Load the NFT from signer1's account_20 let nft <- signer1.storage.load<@BasicNFT.NFT>(from: /storage/BasicNFTPath)_20 ?? panic("Could not load NFT from the first signer's storage")_20_20 // Save the NFT to signer2's account_20 signer2.storage.save(<-nft, to: /storage/BasicNFTPath)_20_20 }_20}`
Action

Select both Account `0x06` and Account `0x07` as the signers.
Make sure account `0x06` is the first signer.  

Click the "Send" button to send the transaction.

Now, the NFT should be stored in the storage of Account `0x07`!
You should be able to run the "NFT Exists" transaction again with `0x07` as the signer
to confirm that it is in their account.

## Enhancing the NFT Experience[​](#enhancing-the-nft-experience "Direct link to Enhancing the NFT Experience")

Hopefully by now, you have an idea of how NFTs can be represented by resources in Cadence.
You might have noticed by now that if we required users
to remember different paths for each NFT and to use a multisig transaction for transfers,
we would not have a very friendly developer and user experience.

This is where the true utility of Cadence is shown.
Continue on to the [next tutorial](/docs/tutorial/non-fungible-tokens-2)
to find out how we can use capabilities and resources owning other resources
to enhance the ease of use and safety of our NFTs.

---

**Tags:**

* [reference](/docs/tags/reference)
* [NFT](/docs/tags/nft)
* [Non-Fungible Token](/docs/tags/non-fungible-token)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/05-non-fungible-tokens-1.md)[Previous4. Capability Tutorial](/docs/tutorial/capabilities)[Next5.2 Non-Fungible Token Tutorial Part 2](/docs/tutorial/non-fungible-tokens-2)
###### Rate this page

😞😐😊

* [Non-Fungible Tokens on the Flow Emulator](#non-fungible-tokens-on-the-flow-emulator)
* [Adding an NFT Your Account](#adding-an-nft-your-account)
  + [Initializers](#initializers)
* [Performing a Basic Transfer](#performing-a-basic-transfer)
* [Enhancing the NFT Experience](#enhancing-the-nft-experience)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

