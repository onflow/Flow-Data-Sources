# Source: https://cadence-lang.org/docs/tutorial/marketplace-compose




8. Marketplace | Cadence




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
* 8. Marketplace
On this page
# 8. Marketplace

In this tutorial, we're going to create a marketplace that uses both the fungible
and non-fungible token (NFTs) contracts that we have learned about in previous tutorials.
This is only for educational purposes and is not meant to be used in production
See a production-ready marketplace in the [NFT storefront repo.](https://github.com/onflow/nft-storefront)
This contract is already deployed to testnet and mainnet and can be used by anyone for any generic NFT sale!

---


Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/7355d51c-066b-46be-adab-a3da6c28b645>](https://play.flow.com/7355d51c-066b-46be-adab-a3da6c28b645)

The tutorial will be asking you to take various actions to interact with this code.
[The marketplace setup guide](/docs/tutorial/marketplace-setup) shows you how to get the playground set up to do this tutorial.


Action

Instructions that require you to take action are always included in a callout box like this one.
These highlighted actions are all that you need to do to get your code running,
but reading the rest is necessary to understand the language's design.

Marketplaces are a popular application of blockchain technology and smart contracts.
When there are NFTs in existence, users usually want to be able to buy and sell them with their fungible tokens.

Now that there is an example for both fungible and non-fungible tokens,
we can build a marketplace that uses both. This is referred to as **composability**:
the ability for developers to leverage shared resources, such as code or userbases,
and use them as building blocks for new applications.

Flow is designed to enable composability because of the way that interfaces, resources and capabilities are designed.

* [Interfaces](/docs/language/interfaces) allow projects to support any generic type as long as it supports a standard set of functionality specified by an interface.
* [Resources](/docs/language/resources) can be passed around and owned by accounts, contracts or even other resources, unlocking different use cases depending on where the resource is stored.
* [Capabilities](/docs/language/capabilities) allow exposing user-defined sets of functionality through special objects that enforce strict security with Cadence's type system.

The combination of these allows developers to do more with less, re-using known safe code and design patterns
to create new, powerful, and unique interactions!

Action

At some point before or after this tutorial, you should definitely check out the formal documentation
linked above about interfaces, resources, and capabilities. It will help complete your understanding
of these complex, but powerful features.

To create a marketplace, we need to integrate the functionality of both fungible
and non-fungible tokens into a single contract that gives users control over their money and assets.
To accomplish this, we're going to take you through these steps to create a composable smart contract and get comfortable with the marketplace:

1. Ensure that your fungible token and non-fungible token contracts are deployed and set up correctly.
2. Deploy the marketplace type declarations to account `0x08`.
3. Create a marketplace object and store it in your account storage, putting an NFT up for sale and publishing a public capability for your sale.
4. Use a different account to purchase the NFT from the sale.
5. Run a script to verify that the NFT was purchased.

**Before proceeding with this tutorial**, you need to complete the [Fungible Tokens](/docs/tutorial/fungible-tokens)
and [Non-Fungible Token](/docs/tutorial/non-fungible-tokens-1) tutorials
to understand the building blocks of this smart contract.

## Marketplace Design[​](#marketplace-design "Direct link to Marketplace Design")

---

One way to implement a marketplace is to have a central smart contract that users deposit their NFTs and their price into,
and have anyone come by and be able to buy the token for that price.
This approach is reasonable, but it centralizes the process and takes away options from the owners.
We want users to be able to maintain ownership of the NFTs that they are trying to sell while they are trying to sell them.

Instead of taking this centralized approach, each user can list a sale from within their own account.

Then, users could either provide a link to their sale to an application that can list it centrally on a website,
or to a central sale aggregator smart contract if they want the entire transaction to stay on-chain.
This way, the owner of the token keeps custody of their token while it is on sale.

Action

Before we start, we need to confirm the state of your accounts.

If you haven't already, please perform the steps in the [marketplace setup guide](/docs/tutorial/marketplace-setup)
to ensure that the Fungible Token and Non-Fungible Token contracts are deployed to account 6 and 2 and own some tokens.

Your accounts should look like this:


![](https://storage.googleapis.com/flow-resources/documentation-assets/cadence-tuts/accounts-nft-storage.png)
Action

You can run the `1. Check Setup` script to ensure that your accounts are correctly set up:


CheckSetupScript.cdc `_87// CheckSetupScript.cdc_87_87import ExampleToken from 0x06_87import ExampleNFT from 0x07_87_87/// Allows the script to return the ownership info_87/// of all the accounts_87access(all) struct OwnerInfo {_87 access(all) let acct6Balance: UFix64_87 access(all) let acct7Balance: UFix64_87_87 access(all) let acct6IDs: [UInt64]_87 access(all) let acct7IDs: [UInt64]_87_87 init(balance1: UFix64, balance2: UFix64, acct6IDs: [UInt64], acct7IDs: [UInt64]) {_87 self.acct6Balance = balance1_87 self.acct7Balance = balance2_87 self.acct6IDs = acct6IDs_87 self.acct7IDs = acct7IDs_87 }_87}_87_87// This script checks that the accounts are set up correctly for the marketplace tutorial._87//_87// Account 0x06: Vault Balance = 40, NFT.id = 1_87// Account 0x07: Vault Balance = 20, No NFTs_87access(all) fun main(): OwnerInfo {_87 // Get the accounts' public account objects_87 let acct6 = getAccount(0x06)_87 let acct7 = getAccount(0x07)_87_87 // Get references to the account's receivers_87 // by getting their public capability_87 // and borrowing a reference from the capability_87 let acct6ReceiverRef = acct6.capabilities.get<&{ExampleToken.Balance}>_87 (/public/CadenceFungibleTokenTutorialReceiver)_87 .borrow()_87 ?? panic("Could not borrow a balance reference to "_87 .concat("0x06's ExampleToken.Vault")_87 .concat(". Make sure 0x06 has set up its account ")_87 .concat("with an ExampleToken Vault and valid capability."))_87_87 let acct7ReceiverRef = acct7.capabilities.get<&{ExampleToken.Balance}>_87 (/public/CadenceFungibleTokenTutorialReceiver)_87 .borrow()_87 ?? panic("Could not borrow a balance reference to "_87 .concat("0x07's ExampleToken.Vault")_87 .concat(". Make sure 0x07 has set up its account ")_87 .concat("with an ExampleToken Vault and valid capability."))_87_87 let returnArray: [UFix64] = []_87_87 // verify that the balances are correct_87 if acct6ReceiverRef.balance != 40.0 || acct7ReceiverRef.balance != 20.0 {_87 panic("Wrong balances!")_87 }_87_87 // Find the public Receiver capability for their Collections_87 let acct6Capability = acct6.capabilities.get<&{ExampleNFT.NFTReceiver}>(ExampleNFT.CollectionPublicPath)_87 let acct7Capability = acct7.capabilities.get<&{ExampleNFT.NFTReceiver}>(ExampleNFT.CollectionPublicPath)_87_87 // borrow references from the capabilities_87 let nft1Ref = acct6Capability.borrow()_87 ?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"_87 .concat(" from the path ")_87 .concat(ExampleNFT.CollectionPublicPath.toString())_87 .concat(". Make sure account 0x06 has set up its account ")_87 .concat("with an ExampleNFT Collection."))_87_87 let nft2Ref = acct7Capability.borrow()_87 ?? panic("Could not borrow a collection reference to 0x07's ExampleNFT.Collection"_87 .concat(" from the path ")_87 .concat(ExampleNFT.CollectionPublicPath.toString())_87 .concat(". Make sure account 0x07 has set up its account ")_87 .concat("with an ExampleNFT Collection."))_87_87 // verify that the collections are correct_87 if nft1Ref.getIDs()[0] != 1 || nft2Ref.getIDs().length != 0 {_87 panic("Wrong Collections!")_87 }_87_87 // Return the struct that shows the account ownership info_87 return OwnerInfo(balance1: acct6ReceiverRef.balance,_87 balance2: acct7ReceiverRef.balance,_87 acct6IDs: nft1Ref.getIDs(),_87 acct7IDs: nft2Ref.getIDs())_87}`

You should see something similar to this output if your accounts are set up correctly.
They are in the same state that they would have been in if you followed
the [Fungible Tokens](/docs/tutorial/fungible-tokens)
and [Non-Fungible Tokens](/docs/tutorial/non-fungible-tokens-1) tutorials in succession:

 `_10"Account 6 Balance"_1040.00000000_10"Account 7 Balance"_1020.00000000_10"Account 6 NFTs"_10[1]_10"Account 7 NFTs"_10[]`

Now that your accounts are in the correct state, we can build a marketplace that enables the sale of NFT's between accounts.

## Setting up an NFT **Marketplace**[​](#setting-up-an-nft-marketplace "Direct link to setting-up-an-nft-marketplace")

---

Every user who wants to sell an NFT will store an instance of a `@SaleCollection` resource in their account storage.

Time to deploy the marketplace contract:

Action

1. Switch to the ExampleMarketplace contract (Contract 3).
2. With `ExampleMarketplace.cdc` open, select account `0x08` from the deployment modal in the bottom right and deploy.

`ExampleMarketplace.cdc` should contain the following contract definition:

ExampleMarketplace.cdc `_175import ExampleToken from 0x06_175import ExampleNFT from 0x07_175_175// ExampleMarketplace.cdc_175//_175// The ExampleMarketplace contract is a very basic sample implementation of an NFT ExampleMarketplace on Flow._175//_175// This contract allows users to put their NFTs up for sale. Other users_175// can purchase these NFTs with fungible tokens._175//_175// Learn more about marketplaces in this tutorial: https://developers.flow.com/cadence/tutorial/marketplace-compose_175//_175// This contract is a learning tool and is not meant to be used in production._175// See the NFTStorefront contract for a generic marketplace smart contract that_175// is used by many different projects on the Flow blockchain:_175//_175// https://github.com/onflow/nft-storefront_175_175access(all) contract ExampleMarketplace {_175_175 // Event that is emitted when a new NFT is put up for sale_175 access(all) event ForSale(id: UInt64, price: UFix64, owner: Address?)_175_175 // Event that is emitted when the price of an NFT changes_175 access(all) event PriceChanged(id: UInt64, newPrice: UFix64, owner: Address?)_175_175 // Event that is emitted when a token is purchased_175 access(all) event TokenPurchased(id: UInt64, price: UFix64, seller: Address?, buyer: Address?)_175_175 // Event that is emitted when a seller withdraws their NFT from the sale_175 access(all) event SaleCanceled(id: UInt64, seller: Address?)_175_175 access(all) entitlement Owner_175_175 // SaleCollection_175 //_175 // NFT Collection object that allows a user to put their NFT up for sale_175 // where others can send fungible tokens to purchase it_175 //_175 access(all) resource SaleCollection {_175_175 /// A capability for the owner's collection_175 access(self) var ownerCollection: Capability<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>_175_175 // Dictionary of the prices for each NFT by ID_175 access(self) var prices: {UInt64: UFix64}_175_175 // The fungible token vault of the owner of this sale._175 // When someone buys a token, this resource can deposit_175 // tokens into their account._175 access(account) let ownerVault: Capability<&{ExampleToken.Receiver}>_175_175 init (ownerCollection: Capability<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>,_175 ownerVault: Capability<&{ExampleToken.Receiver}>) {_175_175 pre {_175 // Check that the owner's collection capability is correct_175 ownerCollection.check():_175 "ExampleMarketplace.SaleCollection.init: "_175 .concat("Owner's NFT Collection Capability is invalid! ")_175 .concat("Make sure the owner has set up an `ExampleNFT.Collection` ")_175 .concat("in their account and provided a valid capability")_175_175 // Check that the fungible token vault capability is correct_175 ownerVault.check():_175 "ExampleMarketplace.SaleCollection.init: "_175 .concat("Owner's Receiver Capability is invalid! ")_175 .concat("Make sure the owner has set up an `ExampleToken.Vault` ")_175 .concat("in their account and provided a valid capability")_175 }_175 self.ownerCollection = ownerCollection_175 self.ownerVault = ownerVault_175 self.prices = {}_175 }_175_175 // cancelSale gives the owner the opportunity to cancel a sale in the collection_175 access(Owner) fun cancelSale(tokenID: UInt64) {_175 // remove the price_175 self.prices.remove(key: tokenID)_175 self.prices[tokenID] = nil_175_175 // Nothing needs to be done with the actual token because it is already in the owner's collection_175 }_175_175 // listForSale lists an NFT for sale in this collection_175 access(Owner) fun listForSale(tokenID: UInt64, price: UFix64) {_175 pre {_175 self.ownerCollection.borrow()!.idExists(id: tokenID):_175 "ExampleMarketplace.SaleCollection.listForSale: "_175 .concat("Cannot list token ID ").concat(tokenID.toString())_175 .concat(" . This NFT ID is not owned by the seller.")_175 .concat("Make sure an ID exists in the sellers NFT Collection")_175 .concat(" before trying to list it for sale")_175 }_175 // store the price in the price array_175 self.prices[tokenID] = price_175_175 emit ForSale(id: tokenID, price: price, owner: self.owner?.address)_175 }_175_175 // changePrice changes the price of a token that is currently for sale_175 access(Owner) fun changePrice(tokenID: UInt64, newPrice: UFix64) {_175 self.prices[tokenID] = newPrice_175_175 emit PriceChanged(id: tokenID, newPrice: newPrice, owner: self.owner?.address)_175 }_175_175 // purchase lets a user send tokens to purchase an NFT that is for sale_175 access(all) fun purchase(tokenID: UInt64,_175 recipient: Capability<&ExampleNFT.Collection>, buyTokens: @ExampleToken.Vault) {_175 pre {_175 self.prices[tokenID] != nil:_175 "ExampleMarketplace.SaleCollection.purchase: "_175 .concat("Cannot purchase NFT with ID ")_175 .concat(tokenID.toString())_175 .concat(" There is not an NFT with this ID available for sale! ")_175 .concat("Make sure the ID to purchase is correct.")_175 buyTokens.balance >= (self.prices[tokenID] ?? 0.0):_175 "ExampleMarketplace.SaleCollection.purchase: "_175 .concat(" Cannot purchase NFT with ID ")_175 .concat(tokenID.toString())_175 .concat(" The amount provided to purchase (")_175 .concat(buyTokens.balance.toString())_175 .concat(") is less than the price of the NFT (")_175 .concat(self.prices[tokenID]!.toString())_175 .concat("). Make sure the ID to purchase is correct and ")_175 .concat("the correct amount of tokens have been used to purchase.")_175 recipient.borrow != nil:_175 "ExampleMarketplace.SaleCollection.purchase: "_175 .concat(" Cannot purchase NFT with ID ")_175 .concat(tokenID.toString())_175 .concat(". The buyer's NFT Collection Capability is invalid.")_175 }_175_175 // get the value out of the optional_175 let price = self.prices[tokenID]!_175_175 self.prices[tokenID] = nil_175_175 let vaultRef = self.ownerVault.borrow()_175 ?? panic("Could not borrow reference to owner token vault")_175_175 // deposit the purchasing tokens into the owners vault_175 vaultRef.deposit(from: <-buyTokens)_175_175 // borrow a reference to the object that the receiver capability links to_175 // We can force-cast the result here because it has already been checked in the pre-conditions_175 let receiverReference = recipient.borrow()!_175_175 // deposit the NFT into the buyers collection_175 receiverReference.deposit(token: <-self.ownerCollection.borrow()!.withdraw(withdrawID: tokenID))_175_175 emit TokenPurchased(id: tokenID, price: price, seller: self.owner?.address, buyer: receiverReference.owner?.address)_175 }_175_175 // idPrice returns the price of a specific token in the sale_175 access(all) view fun idPrice(tokenID: UInt64): UFix64? {_175 return self.prices[tokenID]_175 }_175_175 // getIDs returns an array of token IDs that are for sale_175 access(all) view fun getIDs(): [UInt64] {_175 return self.prices.keys_175 }_175 }_175_175 // createCollection returns a new collection resource to the caller_175 access(all) fun createSaleCollection(_175 ownerCollection: Capability<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>,_175 ownerVault: Capability<&{ExampleToken.Receiver}>_175 ): @SaleCollection_175 {_175 return <- create SaleCollection(ownerCollection: ownerCollection, ownerVault: ownerVault)_175 }_175}`

This marketplace contract has resources that function similarly to the NFT `Collection`
that was explained in [Non-Fungible Tokens](/docs/tutorial/non-fungible-tokens-1), with a few differences and additions:

* This marketplace contract has methods to add and remove NFTs, but instead of storing the NFT resource object in the sale collection,
  the user provides a capability to their main collection that allows the listed NFT to be withdrawn and transferred when it is purchased.
  When a user wants to put their NFT up for sale, they do so by providing the ID and the price to the `listForSale()` function.
  Then, another user can call the `purchase()` function, sending their `ExampleToken.Vault` that contains the currency they are using to make the purchase.
  The buyer also includes a capability to their NFT `ExampleNFT.Collection` so that the purchased token
  can be immediately deposited into their collection when the purchase is made.
* This marketplace contract stores a capability: `access(all) let ownerVault: Capability<&{FungibleToken.Receiver}>`.
  The owner of the sale saves a capability to their Fungible Token `Receiver` within the sale.
  This allows the sale resource to be able to immediately deposit the currency that was used to buy the NFT
  into the owners `Vault` when a purchase is made.
* This marketplace contract includes events. Cadence supports defining events within contracts
  that can be emitted when important actions happen. External apps can monitor these events to know the state of the smart contract.

 `_11 // Event that is emitted when a new NFT is put up for sale_11 access(all) event ForSale(id: UInt64, price: UFix64, owner: Address?)_11_11 // Event that is emitted when the price of an NFT changes_11 access(all) event PriceChanged(id: UInt64, newPrice: UFix64, owner: Address?)_11_11 // Event that is emitted when a token is purchased_11 access(all) event TokenPurchased(id: UInt64, price: UFix64, seller: Address?, buyer: Address?)_11_11 // Event that is emitted when a seller withdraws their NFT from the sale_11 access(all) event SaleCanceled(id: UInt64, seller: Address?)`

This contract has a few new features and concepts that are important to cover:

### Events[​](#events "Direct link to Events")

[Events](/docs/language/events) are special values that can be emitted during the execution of a program.
They usually contain information to indicate that some important action has happened in a smart contract,
such as an NFT transfer, a permission change, or many other different things.
Off-chain applications can monitor events using a Flow SDK to know what is happening on-chain without having to query a smart contract directly.

Many applications want to maintain an off-chain record of what is happening on-chain so they can have faster performance
when getting information about their users' accounts or generating analytics.

Events are declared by indicating [the access level](/docs/language/access-control), `event`,
and the name and parameters of the event, like a function declaration:

 `_10access(all) event ForSale(id: UInt64, price: UFix64, owner: Address?)`

Events cannot modify state at all; they indicate when important actions happen in the smart contract.

Events are emitted with the `emit` keyword followed by the invocation of the event as if it were a function call.

 `_10emit ForSale(id: tokenID, price: price, owner: self.owner?.address)`

External applications can monitor the blockchain to take action when certain events are emitted.

### Resource-Owned Capabilities[​](#resource-owned-capabilities "Direct link to Resource-Owned Capabilities")

We have covered capabilities in previous [tutorials](/docs/tutorial/capabilities),
but only the basics. Capabilities can be used for so much more!

As you hopefully understand, [capabilites](/docs/language/capabilities)
are links to private objects in account storage that specify and expose
a subset of the resource they are linked to.

To create a capability, a user typically uses [the `account.capabilities.storage.issue`](/docs/language/accounts)
method to create a link to a resource in their private storage, specifying a type to link the capability as:

 `_10let cap = acct.capabilities.storage.issue<&ExampleNFT.Collection>(ExampleNFT.CollectionStoragePath)`

After that, the owner can publish the capability to a public path in their account:

 `_10acct.capabilities.publish(cap, at: ExampleNFT.CollectionPublicPath)`

Then, users can get that capability from [the public path](/docs/language/accounts/paths),
borrow it, and access the functionality that the owner specified.

 `_16// Get the account object for address 0x06_16let publicAccount = getAccount(0x06)_16_16// Retrieve a Vault Receiver Capability from the account's public storage_16let acct6Capability = acct.capabilities.get<&{ExampleToken.Receiver}>(_16 ExampleToken.VaultPublicPath_16 )_16_16// Borrow a reference_16let acct6ReceiverRef = acct6Capability.borrow()_16 ?? panic("Account 0x06's Receiver Capability is invalid! ")_16 .concat("Make sure the owner has set up an `ExampleToken.Vault` ")_16 .concat("in their account and provided a valid capability")_16_16// Deposit tokens_16acct6ReceiverRef.deposit(from: <-tokens)`

With the marketplace contract, we are utilizing a new feature of capabilities.
Capabilities can be stored anywhere! Lots of functionality is contained within resources,
and developers will sometimes want to be able to access some of the functionality of resources from within different resources or contracts.

We store two different capabilities in the marketplace sale collection:

 `_10/// A capability for the owner's collection_10access(self) var ownerCollection: Capability<auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>_10_10// The fungible token vault of the owner of this sale._10// When someone buys a token, this resource can deposit_10// tokens into their account._10access(account) let ownerVault: Capability<&{ExampleToken.Receiver}>`

If an object like a contract or resource owns a capability, they can borrow a reference to that capability at any time
to access that functionality without having to get it from the owner's account every time.

This is especially important if the owner wants to expose some functionality that is only intended for one person,
meaning that the link for the capability is not stored in a public path.
We do that in this example, because the sale collection stores a capability
that can access the withdraw functionality
of the `ExampleNFT.Collection` with the `ExampleNFT.Withdraw` entitlement.
It needs this because it withdraws the specified NFT in the `purchase()` method to send to the buyer.

It is important to remember that control of a capability does not equal ownership of the underlying resource.
You can use the capability to access that resource's functionality, but you can't use it to fake ownership.
You need the actual resource (identified by the prefixed `@` symbol) to prove ownership.

Additionally, these capabilities can be stored anywhere, but if a user decides that they no longer want the capability
to be used, they can revoke it by getting the controller for the capability
from their account with the `getControllers` method and delete the capability with `delete`.
Here is an example that deletes all the controllers for a specified storage path:

 `_18let controllers = self.account.capabilities.storage.getControllers(forPath: storagePath)_18for controller in controllers {_18 controller.delete()_18}_18After this, any capabilities that use that storage path are rendered invalid._18_18One last piece to consider about capabilities is the decision about_18when to use them instead of storing the resource directly._18This tutorial used to have the `SaleCollection` directly store the NFTs that were for sale, like so:_18_18```cadence_18access(all) resource SaleCollection {_18_18 /// Dictionary of NFT objects for sale_18 /// Maps ID to NFT resource object_18 /// Not recommended_18 access(self) var forSale: @{UInt64: ExampleNFT.NFT}_18}`

This is a logical way to do it, and illustrates another important concept in Cadence, that resources can own other resources!
Check out the [Kitty Hats tutorial](/docs/tutorial/resources-compose) for a little more exploration of this concept.

In this case however, nesting resources doesn't make sense. If a user decides to store their for-sale NFTs in a separate place from their main collection,
then those NFTs are not available to be shown to any app or smart contract that queries the main collection,
so it is as if the owner doesn't actually own the NFT!

In cases like this, we usually recommend using a capability to the main collection so that the main collection can remain unchanged and fully usable by
other smart contracts and apps. This also means that if a for-sale NFT gets transferred by some means other than a purchase, then you need a way to get
rid of the stale listing. That is out of the scope of this tutorial though.

Enough explaining! Lets execute some code!

## Using the Marketplace[​](#using-the-marketplace "Direct link to Using the Marketplace")

At this point, we should have an `ExampleToken.Vault` and an `Example.NFT.Collection` in both accounts' storage.
Account `0x06` should have an NFT in their collection and the `ExampleMarketplace` contract should be deployed to `0x08`.

You can create a `SaleCollection` and list account `0x06`'s token for sale by following these steps:

Action

1. Open Transaction 4, `Create Sale`
2. Select account `0x06` as the only signer and click the `Send` button to submit the transaction.

Transaction4.cdc `_37// CreateSale.cdc_37_37import ExampleToken from 0x06_37import ExampleNFT from 0x07_37import ExampleMarketplace from 0x08_37_37// This transaction creates a new Sale Collection object,_37// lists an NFT for sale, puts it in account storage,_37// and creates a public capability to the sale so that others can buy the token._37transaction {_37_37 prepare(acct: auth(SaveValue, StorageCapabilities) &Account) {_37_37 // Borrow a reference to the stored Vault_37 let receiver = acct.capabilities.get<&{ExampleToken.Receiver}>(ExampleToken.VaultPublicPath)_37_37 // Create an entitled capability to the NFT Collection_37 let collectionCapability = acct.capabilities.storage.issue_37 <auth(ExampleNFT.Withdraw) &ExampleNFT.Collection>_37 (ExampleNFT.CollectionStoragePath)_37_37 // Create a new Sale object,_37 // initializing it with the reference to the owner's vault_37 let sale <- ExampleMarketplace.createSaleCollection(ownerCollection: collectionCapability, ownerVault: receiver)_37_37 // List the token for sale by moving it into the sale object_37 sale.listForSale(tokenID: 1, price: 10.0)_37_37 // Store the sale object in the account storage_37 acct.storage.save(<-sale, to: /storage/NFTSale)_37_37 // Create a public capability to the sale so that others can call its methods_37 acct.capabilities.storage.issue<&ExampleMarketplace.SaleCollection>(/public/NFTSale, target: /storage/NFTSale)_37_37 log("Sale Created for account 6. Selling NFT 1 for 10 tokens")_37 }_37}`

This transaction:

1. Gets a `Receiver` capability on the owners `Vault`.
2. Creates a private entitled `ExampleNFT.Collection` Capability from the owner.
3. Creates the `SaleCollection`, which stores their `Vault` and `ExampleNFT.Collection` capabilities.
4. Lists the token with `ID = 1` for sale and sets its price as 10.0.
5. Stores the `SaleCollection` in their account storage and links a public capability that allows others to purchase any NFTs for sale.

Let's run a script to ensure that the sale was created correctly.

1. Open Script 2: `GetSaleIDs.cdc`
2. Click the `Execute` button to print the ID and price of the NFT that account `0x06` has for sale.

GetSaleIDs.cdc `_23// GetSaleIDs.cdc_23_23import ExampleToken from 0x06_23import ExampleNFT from 0x07_23import ExampleMarketplace from 0x08_23_23// This script returns the NFTs that account 0x06 has for sale._23access(all)_23fun main(): [UInt64] {_23 // Get the public account object for account 0x06_23 let account1 = getAccount(0x06)_23_23 // Find the public Sale reference to their Collection_23 let acct6saleRef = account1.capabilities.get<&ExampleMarketplace.SaleCollection>(/public/NFTSale)>_23 .borrow()_23 ?? panic("Could not borrow a reference to the SaleCollection capability for account 0x06 ")_23 .concat("at path /public/NFTSale. ")_23 .concat("Make sure the owner has set up the SaleCollection ")_23 .concat("in their account with the Create Sale transaction")_23_23 // Return the NFT IDs that are for sale_23 return acct6saleRef.getIDs()_23}`

This script should complete and print something like this:

 `_10[1]`
## Purchasing an NFT[​](#purchasing-an-nft "Direct link to Purchasing an NFT")

---

The buyer can now purchase the seller's NFT by using the transaction in `Transaction2.cdc`:

Action

1. Open Transaction 5: `PurchaseSale.cdc` file
2. Select account `0x07` as the only signer and click the `Send` button

PurchaseSale.cdc `_50// PurchaseSale.cdc_50_50import ExampleToken from 0x06_50import ExampleNFT from 0x07_50import ExampleMarketplace from 0x08_50_50// This transaction uses the signers Vault tokens to purchase an NFT_50// from the Sale collection of account 0x06._50transaction {_50_50 // Capability to the buyer's NFT collection where they_50 // will store the bought NFT_50 let collectionCapability: Capability<&ExampleNFT.Collection>_50_50 // Vault that will hold the tokens that will be used to_50 // but the NFT_50 let temporaryVault: @ExampleToken.Vault_50_50 prepare(acct: auth(BorrowValue) &Account) {_50_50 // get the references to the buyer's fungible token Vault and NFT Collection Receiver_50 self.collectionCapability = acct.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_50_50 let vaultRef = acct.storage.borrow<&ExampleToken.Vault>(from: /storage/CadenceFungibleTokenTutorialVault)_50 ?? panic("Could not borrow a reference to "_50 .concat("0x07's ExampleToken.Vault")_50 .concat(". Make sure 0x07 has set up its account ")_50 .concat("with an ExampleToken Vault and valid capability."))_50_50 // withdraw tokens from the buyers Vault_50 self.temporaryVault <- vaultRef.withdraw(amount: 10.0)_50 }_50_50 execute {_50 // get the read-only account storage of the seller_50 let seller = getAccount(0x06)_50_50 // get the reference to the seller's sale_50 let saleRef = seller.capabilities.get<&ExampleMarketplace.SaleCollection>(/public/NFTSale)_50 .borrow()_50 ?? panic("Could not borrow a reference to "_50 .concat("0x06's ExampleMarketplace.SaleCollection")_50 .concat(". Make sure 0x06 has set up its account ")_50 .concat("with an ExampleMarketplace SaleCollection and valid capability."))_50_50 // purchase the NFT the seller is selling, giving them the capability_50 // to your NFT collection and giving them the tokens to buy it_50 saleRef.purchase(tokenID: 1, recipient: self.collectionCapability, buyTokens: <-self.temporaryVault)_50 }_50}`

This transaction:

1. Gets the capability to the buyer's NFT receiver
2. Get a reference to their token vault and withdraws the sale purchase amount
3. Gets the public account object for account `0x06`
4. Gets the reference to the seller's public sale
5. Calls the `purchase` function, passing in the tokens and the `Collection` reference. Then `purchase` deposits the bought NFT directly into the buyer's collection.

## Verifying the NFT Was Purchased Correctly[​](#verifying-the-nft-was-purchased-correctly "Direct link to Verifying the NFT Was Purchased Correctly")

---

You can run now run a script to verify that the NFT was purchased correctly because:

* account `0x06` has 50 tokens and does not have any NFTs for sale or in their collection and account
* account `0x07` has 10 tokens and an NFT with id=1

To run a script that verifies the NFT was purchased correctly, follow these steps:

Action

1. Open Script 3: `VerifyAfterPurchase.cdc`
2. Click the `Execute` button

`VerifyAfterPurchase.cdc` should contain the following code:

Script3.cdc `_86// VerifyAfterPurchase_86import ExampleToken from 0x06_86import ExampleNFT from 0x07_86_86/// Allows the script to return the ownership info_86/// of all the accounts_86access(all) struct OwnerInfo {_86 access(all) let acct6Balance: UFix64_86 access(all) let acct7Balance: UFix64_86_86 access(all) let acct6IDs: [UInt64]_86 access(all) let acct7IDs: [UInt64]_86_86 init(balance1: UFix64, balance2: UFix64, acct6IDs: [UInt64], acct7IDs: [UInt64]) {_86 self.acct6Balance = balance1_86 self.acct7Balance = balance2_86 self.acct6IDs = acct6IDs_86 self.acct7IDs = acct7IDs_86 }_86}_86_86// This script checks that the accounts are in the correct state after purchasing a listing._86//_86// Account 0x06: Vault Balance = 50, No NFTs_86// Account 0x07: Vault Balance = 10, NFT.id = 1_86access(all) fun main(): OwnerInfo {_86 // Get the accounts' public account objects_86 let acct6 = getAccount(0x06)_86 let acct7 = getAccount(0x07)_86_86 // Get references to the account's receivers_86 // by getting their public capability_86 // and borrowing a reference from the capability_86 let acct6ReceiverRef = acct6.capabilities.get<&{ExampleToken.Balance}>_86 (/public/CadenceFungibleTokenTutorialReceiver)_86 .borrow()_86 ?? panic("Could not borrow a balance reference to "_86 .concat("0x06's ExampleToken.Vault")_86 .concat(". Make sure 0x06 has set up its account ")_86 .concat("with an ExampleToken Vault and valid capability."))_86_86 let acct7ReceiverRef = acct7.capabilities.get<&{ExampleToken.Balance}>_86 (/public/CadenceFungibleTokenTutorialReceiver)_86 .borrow()_86 ?? panic("Could not borrow a balance reference to "_86 .concat("0x07's ExampleToken.Vault")_86 .concat(". Make sure 0x07 has set up its account ")_86 .concat("with an ExampleToken Vault and valid capability."))_86_86 let returnArray: [UFix64] = []_86_86 // verify that the balances are correct_86 if acct6ReceiverRef.balance != 50.0 || acct7ReceiverRef.balance != 10.0 {_86 panic("Wrong balances! Account 6 Balance should be 50 and Account 7 balance should be 10.")_86 }_86_86 // Find the public Receiver capability for their Collections_86 let acct6Capability = acct6.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_86 let acct7Capability = acct7.capabilities.get<&ExampleNFT.Collection>(ExampleNFT.CollectionPublicPath)_86_86 // borrow references from the capabilities_86 let nft1Ref = acct6Capability.borrow()_86 ?? panic("Could not borrow a collection reference to 0x06's ExampleNFT.Collection"_86 .concat(" from the path ")_86 .concat(ExampleNFT.CollectionPublicPath.toString())_86 .concat(". Make sure account 0x06 has set up its account ")_86 .concat("with an ExampleNFT Collection."))_86_86 let nft2Ref = acct7Capability.borrow()_86 ?? panic("Could not borrow a collection reference to 0x07's ExampleNFT.Collection"_86 .concat(" from the path ")_86 .concat(ExampleNFT.CollectionPublicPath.toString())_86 .concat(". Make sure account 0x07 has set up its account ")_86 .concat("with an ExampleNFT Collection."))_86_86 // verify that the collections are correct_86 if nft2Ref.getIDs()[0] != 1 || nft1Ref.getIDs().length != 0 {_86 panic("Wrong Collections! Account 6 should own zero NFTs and account 7 should own one.")_86 }_86_86 // Return the struct that shows the account ownership info_86 return OwnerInfo(balance1: acct6ReceiverRef.balance,_86 balance2: acct7ReceiverRef.balance,_86 acct6IDs: nft1Ref.getIDs(),_86 acct7IDs: nft2Ref.getIDs())_86}`

If you did everything correctly, the transaction should succeed and it should print something similar to this:

 `_10"account 6 Vault Balance"_1050_10"account 7 Vault Balance"_1010_10"account 6 NFTs"_10[]_10"account 7 NFTs"_10[1]`

Congratulations, you have successfully implemented a simple marketplace in Cadence and used it to allow one account to buy an NFT from another!

## Scaling the Marketplace[​](#scaling-the-marketplace "Direct link to Scaling the Marketplace")

---

A user can hold a sale in their account with these resources and transactions.
Support for a central marketplace where users can discover sales is relatively easy to implement and can build on what we already have.
If we wanted to build a central marketplace on-chain, we could use a contract that looks something like this:

CentralMarketplace.cdc `_25// Marketplace would be the central contract where people can post their sale_25// references so that anyone can access them_25access(all) contract Marketplace {_25 // Data structure to store active sales_25 access(all) var tokensForSale: {Address: Capability<&SaleCollection>)}_25_25 // listSaleCollection lists a users sale reference in the array_25 // and returns the index of the sale so that users can know_25 // how to remove it from the marketplace_25 access(all) fun listSaleCollection(collection: Capability<&SaleCollection>) {_25 let saleRef = collection.borrow()_25 ?? panic("Could not borrow a reference to the SaleCollection capability ")_25 .concat("Make sure the owner has set up the SaleCollection ")_25 .concat("in their account and provided a valid capability")_25_25 self.tokensForSale[saleRef.owner!.address] = collection_25 }_25_25 // removeSaleCollection removes a user's sale from the array_25 // of sale references_25 access(all) fun removeSaleCollection(owner: Address) {_25 self.tokensForSale[owner] = nil_25 }_25_25}`

This contract isn't meant to be a working or production-ready contract, but it could be extended to make a complete central marketplace by having:

* Sellers list a capability to their `SaleCollection` in this contract
* Other functions that buyers could call to get info about all the different sales and to make purchases.

A central marketplace in an off-chain application is easier to implement because:

* The app could host the marketplace and a user would simply log in to the app and give the app its account address.
* The app could read the user's public storage and find their sale reference.
* With the sale reference, the app could get all the information they need about how to display the sales on their website.
* Any buyer could discover the sale in the app and login with their account, which gives the app access to their public references.
* When the buyer wants to buy a specific NFT, the app would automatically generate the proper transaction to purchase the NFT from the seller.

## Creating a **Marketplace for Any Generic NFT**[​](#creating-a-marketplace-for-any-generic-nft "Direct link to creating-a-marketplace-for-any-generic-nft")

---

The previous examples show how a simple marketplace could be created for a specific class of NFTs.
However, users will want to have a marketplace where they can buy and sell any NFT they want, regardless of its type.
There are a few good examples of generic marketplaces on Flow right now.

* The Flow team has created a completely decentralized example of a generic marketplace in the [NFT storefront repo.](https://github.com/onflow/nft-storefront)
  This contract is already deployed to testnet and mainnet and can be used by anyone for any generic NFT sale!

## Composable Resources on Flow[​](#composable-resources-on-flow "Direct link to Composable Resources on Flow")

---

Now that you have an understanding of how composable smart contracts and the marketplace work on Flow, you're ready to play with composable resources!
Check out the [Kitty Hats tutorial!](/docs/tutorial/resources-compose)

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/08-marketplace-compose.md)[Previous7. Marketplace Setup](/docs/tutorial/marketplace-setup)[Next9. Voting Contract](/docs/tutorial/voting)
###### Rate this page

😞😐😊

* [Marketplace Design](#marketplace-design)
* [Setting up an NFT **Marketplace**](#setting-up-an-nft-marketplace)
  + [Events](#events)
  + [Resource-Owned Capabilities](#resource-owned-capabilities)
* [Using the Marketplace](#using-the-marketplace)
* [Purchasing an NFT](#purchasing-an-nft)
* [Verifying the NFT Was Purchased Correctly](#verifying-the-nft-was-purchased-correctly)
* [Scaling the Marketplace](#scaling-the-marketplace)
* [Creating a **Marketplace for Any Generic NFT**](#creating-a-marketplace-for-any-generic-nft)
* [Composable Resources on Flow](#composable-resources-on-flow)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

