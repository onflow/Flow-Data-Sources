# Source: https://cadence-lang.org/docs/design-patterns




Cadence Design Patterns | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

* [Introduction](/docs/)
* [Why Use Cadence?](/docs/why)
* [Tutorial](/docs/tutorial/first-steps)
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


* Design Patterns
On this page

This is a selection of software design patterns developed by core Flow developers
while writing Cadence code for deployment to Flow Mainnet.

Many of these design patters apply to most other programming languages, but some are specific to Cadence.

[Design patterns](https://en.wikipedia.org/wiki/Software_design_pattern) are building blocks for software development.
They may provide a solution to a problem that you encounter when writing smart contracts in Cadence.
If they do not clearly fit, these patterns may not be the right solution for a given situation or problem.
They are not meant to be rules to be followed strictly, especially where a better solution presents itself.

# General

These are general patterns to follow when writing smart contracts.

## Use named value fields for constants instead of hard-coding[​](#use-named-value-fields-for-constants-instead-of-hard-coding "Direct link to Use named value fields for constants instead of hard-coding")

### Problem[​](#problem "Direct link to Problem")

Your contracts, resources, and scripts all have to refer to the same value.
A number, a string, a storage path, etc.
Entering these values manually in transactions and scripts is a potential source of error.
See [Wikipedia's page on magic numbers](https://en.wikipedia.org/wiki/Magic_number_(programming))

### Solution[​](#solution "Direct link to Solution")

Add a public (`access(all)`), constant (`let`) field, e.g. a `Path` , to the contract responsible for the value,
and set it in the contract's initializer.
Refer to that value via this public field rather than specifying it manually.

Example Snippet:

 `_32_32// BAD Practice: Do not hard code storage paths_32access(all)_32contract NamedFields {_32_32 access(all)_32 resource Test {}_32_32 init() {_32 // BAD: Hard-coded storage path_32 self.account.storage.save(<-create Test(), to: /storage/testStorage)_32 }_32}_32_32// GOOD practice: Instead, use a field_32//_32access(all)_32contract NamedFields {_32_32 access(all)_32 resource Test {}_32_32 // GOOD: field storage path_32 access(all)_32 let testStoragePath: StoragePath_32_32 init() {_32 // assign and access the field here and in transactions_32 self.testStoragePath = /storage/testStorage_32 self.account.storage.save(<-create Test(), to: self.TestStoragePath)_32 }_32}`

[Example Code](https://github.com/onflow/flow-core-contracts/blob/71ea0dfe843da873d52c6a983e7c8f44a4677b26/contracts/LockedTokens.cdc#L779)

## Script-Accessible public field/function[​](#script-accessible-public-fieldfunction "Direct link to Script-Accessible public field/function")

Data availability is important in a blockchain environment.
It is useful to publicize information about your smart contract and the assets it controls
so other smart contracts and apps can easily query it.

### Problem[​](#problem-1 "Direct link to Problem")

Your contract, resource, or struct has a field or resource that will need to be read and used on or off-chain, often in bulk.

### Solution[​](#solution-1 "Direct link to Solution")

Make sure that the field can be accessed from a script.
This saves the time and fees required to read a property using a transaction.
Making the field or function `access(all)` and exposing it via a `/public/` capability will allow this.

Be careful not to expose any data or functionality that should be kept private when doing so.

Example:

 `_10// BAD: Field is private, so it cannot be read by the public_10access(self)_10let totalSupply: UFix64_10_10// GOOD: Field is public, so it can be read and used by anyone_10access(all)_10let totalSupply: UFix64`
## Script-Accessible report[​](#script-accessible-report "Direct link to Script-Accessible report")

### Problem[​](#problem-2 "Direct link to Problem")

Your contract has a resource that you wish to access fields of.
Resources are often stored in private places and are hard to access.
Additionally, scripts cannot return resources to the external context,
so a struct must be used to hold the data.

### Solution[​](#solution-2 "Direct link to Solution")

Return a reference to a resource if the data from a single resource is all that is needed.
Otherwise, declare a struct to hold the data that you wish to return from the script.
Write a function that fills out the fields of this struct with the data
from the resource that you wish to access.
Then call this on the resource that you wish to access the fields of in a script,
and return the struct from the script.

See [Script-Accessible public field/function](#script-accessible-public-fieldfunction), above, for how best to expose this capability.

### Example[​](#example "Direct link to Example")

 `_79access(all)_79contract AContract {_79_79 access(all)_79 let BResourceStoragePath: StoragePath_79_79 access(all)_79 let BResourcePublicPath: PublicPath_79_79 init() {_79 self.BResourceStoragePath = /storage/BResource_79 self.BResourcePublicPath = /public/BResource_79 }_79_79 // Resource definition_79 access(all)_79 resource BResource {_79_79 access(all)_79 var c: UInt64_79_79 access(all)_79 var d: String_79_79_79 // Generate a struct with the same fields_79 // to return when a script wants to see the fields of the resource_79 // without having to return the actual resource_79 access(all)_79 fun generateReport(): BReportStruct {_79 return BReportStruct(c: self.c, d: self.d)_79 }_79_79 init(c: UInt64, d: String) {_79 self.c = c_79 self.d = d_79 }_79 }_79_79 // Define a struct with the same fields as the resource_79 access(all)_79 struct BReportStruct {_79_79 access(all)_79 var c: UInt64_79_79 access(all)_79 var d: String_79_79 init(c: UInt64, d: String) {_79 self.c = c_79 self.d = d_79 }_79_79 }_79}_79..._79// Transaction_79import AContract from 0xAContract_79_79transaction {_79 prepare(acct: auth(IssueStorageCapabilityController, PublishCapability) &Account) {_79 //..._79 let cap = acct.capabilities.storage.issue<&AContract.BResource>(AContract.BResourceStoragePath)_79 acct.capabilities.publish(cap, at: AContract.BResourcePublicPath)_79 }_79}_79// Script_79import AContract from 0xAContract_79_79// Return the struct with a script_79access(all)_79fun main(account: Address): AContract.BReportStruct {_79 // borrow the resource_79 let b = getAccount(account).capabilities_79 .borrow<&AContract.BResource>(AContract.BResourcePublicPath)_79 // return the struct_79 return b.generateReport()_79}`
## Init singleton[​](#init-singleton "Direct link to Init singleton")

### Problem[​](#problem-3 "Direct link to Problem")

An admin resource must be created and delivered to a specified account.
There should not be a function to do this, as that would allow anyone to create an admin resource.

### Solution[​](#solution-3 "Direct link to Solution")

Create any one-off resources in the contract's initializer
and deliver them to an address or `&Account` specified as an argument.

See how this is done in the LockedTokens contract initializer:

[LockedTokens.cdc](https://github.com/onflow/flow-core-contracts/blob/71ea0dfe843da873d52c6a983e7c8f44a4677b26/contracts/LockedTokens.cdc#L765-L780)

and in the transaction that is used to deploy it:

[admin\_deploy\_contract.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/admin/admin_deploy_contract.cdc)

## Use descriptive names for fields, paths, functions and variables[​](#use-descriptive-names-for-fields-paths-functions-and-variables "Direct link to Use descriptive names for fields, paths, functions and variables")

### Problem[​](#problem-4 "Direct link to Problem")

Smart contracts often are vitally important pieces of a project and often have many other
smart contracts and applications that rely on them.
Therefore, they need to be clearly written and easy to understand.

### Solution[​](#solution-4 "Direct link to Solution")

All fields, functions, types, variables, etc., need to have names that clearly describe what they are used for.

`account` / `accounts` is better than `array` / `element`.

`providerAccount` / `tokenRecipientAccount` is better than `acct1` / `acct2`.

`/storage/bestPracticesDocsCollectionPath` is better than `/storage/collection`

### Example[​](#example-1 "Direct link to Example")

 `_37// BAD: Unclear naming_37//_37access(all)_37contract Tax {_37_37 // Do not use abbreviations unless absolutely necessary_37 access(all)_37 var pcnt: UFix64_37_37 // Not clear what the function is calculating or what the parameter should be_37 access(all)_37 fun calculate(num: UFix64): UFix64 {_37 // What total is this referring to?_37 let total = num + (num * self.pcnt)_37_37 return total_37 }_37}_37_37// GOOD: Clear naming_37//_37access(all)_37contract TaxUtilities {_37_37 // Clearly states what the field is for_37 access(all)_37 var taxPercentage: UFix64_37_37 // Clearly states that this function calculates the_37 // total cost after tax_37 access(all)_37 fun calculateTotalCostPlusTax(preTaxCost: UFix64): UFix64 {_37 let postTaxCost = preTaxCost + (preTaxCost * self.taxPercentage)_37_37 return postTaxCost_37 }_37}`
## Plural names for arrays and maps are preferable[​](#plural-names-for-arrays-and-maps-are-preferable "Direct link to Plural names for arrays and maps are preferable")

For example, use `accounts` rather than `account` for an array of accounts.

This signals that the field or variable is not scalar.
It also makes it easier to use the singular form for a variable name during iteration.

## Use transaction post-conditions when applicable[​](#use-transaction-post-conditions-when-applicable "Direct link to Use transaction post-conditions when applicable")

### Problem[​](#problem-5 "Direct link to Problem")

Transactions can contain any amount of valid Cadence code and access many contracts and accounts.
The power of resources and capabilities means that there may be some behaviors of programs that are not expected.

### Solution[​](#solution-5 "Direct link to Solution")

It is usually safe to include post-conditions in transactions to verify the intended outcome.

### Example[​](#example-2 "Direct link to Example")

This could be used when purchasing an NFT to verify that the NFT was deposited in your account's collection.

 `_22// Pseudo-code_22_22transaction {_22_22 access(all)_22 let buyerCollectionRef: &NonFungibleToken.Collection_22_22 prepare(acct: auth(BorrowValue) &Account) {_22_22 // Get tokens to buy and a collection to deposit the bought NFT to_22 let temporaryVault <- vaultRef.withdraw(amount: 10.0)_22 let self.buyerCollectionRef = acct.storage.borrow(from: /storage/Collection)_22_22 // purchase, supplying the buyers collection reference_22 saleRef.purchase(tokenID: 1, recipient: self.buyerCollectionRef, buyTokens: <-temporaryVault)_22_22 }_22 post {_22 // verify that the buyer now owns the NFT_22 self.buyerCollectionRef.idExists(1) == true: "Bought NFT ID was not deposited into the buyers collection"_22 }_22}`
## Avoid unnecessary load and save storage operations, prefer in-place mutations[​](#avoid-unnecessary-load-and-save-storage-operations-prefer-in-place-mutations "Direct link to Avoid unnecessary load and save storage operations, prefer in-place mutations")

### Problem[​](#problem-6 "Direct link to Problem")

When modifying data in account storage, `load()` and `save()` are costly operations:
All data is unnecessarily moved out of the account, then moved back into the account.
This can quickly cause your transaction to reach its limits.

This also applies to nested, stored in fields, arrays, and dictionaries:
Moving objects out of containers and moving them back into the container,
just to modify the object, is just as costly.

For example, a collection contains a dictionary of NFTs.
There is no need to move the whole dictionary out of the field,
update the dictionary on the stack (e.g., adding or removing an NFT),
and then move the whole dictionary back to the field:
the dictionary can be updated in-place, which is easier and more efficient.
The same goes for a more complex data structure like a dictionary of nested resources:
Each resource can be updated in-place by taking a reference to the nested object instead of loading and saving.

### Solution[​](#solution-6 "Direct link to Solution")

For making modifications to values in storage or accessing stored objects,
`borrow()` should always be used to access them instead of `load` or `save` unless absolutely necessary.
`borrow()` returns a reference to the object at the storage path instead of having to load the entire object.
This reference can be assigned to or can be used to access fields or call methods on stored objects.

Fields and value in containers, such as in arrays and dictionaries,
can be borrowed using a reference expression (`&v as &T`).

### Example[​](#example-3 "Direct link to Example")

 `_36// BAD: Loads and stores a resource to use it_36//_36transaction {_36_36 prepare(acct: auth(LoadValue, SaveValue) &Account) {_36_36 // Removes the vault from storage, a costly operation_36 let vault <- acct.storage.load<@ExampleToken.Vault>(from: /storage/exampleToken)_36_36 // Withdraws tokens_36 let burnVault <- vault.withdraw(amount: 10)_36_36 destroy burnVault_36_36 // Saves the used vault back to storage, another costly operation_36 acct.storage.save(to: /storage/exampleToken)_36_36 }_36}_36_36// GOOD: Uses borrow instead to avoid costly operations_36//_36transaction {_36_36 prepare(acct: auth(BorrowValue) &Account) {_36_36 // Borrows a reference to the stored vault, much less costly operation_36 let vault <- acct.storage.borrow<&ExampleToken.Vault>(from: /storage/exampleToken)_36_36 let burnVault <- vault.withdraw(amount: 10)_36_36 destroy burnVault_36_36 // No `save` required because we only used a reference_36 }_36}`
# Capabilities

## Capability bootstrapping[​](#capability-bootstrapping "Direct link to Capability bootstrapping")

### Problem[​](#problem-7 "Direct link to Problem")

An account must be given a [capability](/docs/language/capabilities) to an object stored in another account.
To create (issue) the capability, the transaction must be signed by a key which has access to the target account.

To transfer / deliver the capability to the other account, the transaction also needs write access to that one.
It is not as easy to produce a single transaction which is authorized by two accounts
as it is to produce a typical transaction which is authorized by one account.

This prevents a single transaction from fetching the capability
from one account and delivering it to the other.

### Solution[​](#solution-7 "Direct link to Solution")

The solution to the bootstrapping problem in Cadence is provided by the
[Inbox API](/docs/language/accounts/inbox).

Account A (which we will call the provider) creates the capability they wish to send to account B
(which we will call the recipient),
and stores this capability on their account in a place where the recipient can access it
using the `Inbox.publish` function on their account.
They choose a name for the capability that the recipient can later use to identify it,
and specify the recipient's address when calling `publish`.
This call to `publish` will emit an `InboxValuePublished` event
that the recipient can listen for off-chain to know that the Capability is ready for them to claim.

The recipient then later can use the `Inbox.claim` function to securely claim the capability
from the provider's account.
They must provide the name and type with which the capability was published,
as well as the address of the provider's account
(all of this information is available in the `InboxValuePublished` event emitted on `publish`).
This will remove the capability from the provider's account and emit an `InboxValueClaimed` event
that the provider can listen for off-chain.

One important caveat to this is that the published capability is stored on the provider's account
until the recipient claims it,
so the provider can also use the `Inbox.unpublish` function to remove the capability from their account
if they no longer wish to pay for storage for it.
This also requires the name and type which the capability was published,
and emits an `InboxValueUnpublished` event that the recipient can listen for off-chain.

It is also important to note that the recipient becomes the owner of the capability object
once they have claimed it, and can thus store it or copy it anywhere they have access to.
This means providers should only publish capabilities to recipients they trust to use them properly,
or limit the type with which the capability is authorized
in order to only give recipients access to the functionality
that the provider is willing to allow them to copy.

 `_20import "BasicNFT"_20_20transaction(receiver: Address, name: String) {_20_20 prepare(signer: auth(IssueStorageCapabilityController, PublishInboxCapability) &Account) {_20_20 // Issue a capability controller for the storage path_20 let capability = signer.capabilities.storage.issue<&BasicNFT.Minter>(BasicNFT.minterPath)_20_20 // Set the name as tag so it is easy for us to remember its purpose_20 let controller = signer.capabilities.storage.getController(byCapabilityID: capability.id)_20 ?? panic("Cannot get the storage capability controller with ID "_20 .concat(capabilityID.toString())_20 .concat(" from the signer's account! Make sure the ID belongs to a capability that the owner controls and that it is a storage capability.")_20 controller.setTag(name)_20_20 // Publish the capability, so it can be later claimed by the receiver_20 signer.inbox.publish(capability, name: name, recipient: receiver)_20 }_20}`
 `_17import "BasicNFT"_17_17transaction(provider: Address, name: String) {_17_17 prepare(signer: auth(ClaimInboxCapability, SaveValue) &Account) {_17_17 // Claim the capability from our inbox_17 let capability = signer.inbox.claim<&BasicNFT.Minter>(name, provider: provider)_17 ?? panic("Cannot claim the storage capability controller with name "_17 .concat(name).concat(" from the provider account (").concat(provider.toString())_17 .concat("! Make sure the provider address is correct and that they have published "_17 .concat(" a capability with the desired name.")_17_17 // Save the capability to our storage so we can later retrieve and use it_17 signer.storage.save(capability, to: BasicNFT.minterPath)_17 }_17}`
## Check for existing capability before publishing new one[​](#check-for-existing-capability-before-publishing-new-one "Direct link to Check for existing capability before publishing new one")

### Problem[​](#problem-8 "Direct link to Problem")

When publishing a capability, a capability might be already be published at the specified path.

### Solution[​](#solution-8 "Direct link to Solution")

Check if a capability is already published at the given path.

### Example[​](#example-4 "Direct link to Example")

 `_13transaction {_13 prepare(signer: auth(Capabilities) &Account) {_13 let capability = signer.capabilities.storage_13 .issue<&ExampleToken.Vault>(/storage/exampleTokenVault)_13_13 let publicPath = /public/exampleTokenReceiver_13_13 if signer.capabilities.exits(publicPath) {_13 signer.capabilities.unpublish(publicPath)_13 }_13 signer.capabilities.publish(capability, at: publicPath)_13 }_13}`
## Capability Revocation[​](#capability-revocation "Direct link to Capability Revocation")

### Problem[​](#problem-9 "Direct link to Problem")

A capability provided by one account to a second account must able to be revoked
by the first account without the co-operation of the second.

### Solution[​](#solution-9 "Direct link to Solution")

If the capability is a storage capability:

 `_10transaction(capabilityID: UInt64) {_10 prepare(signer: auth(StorageCapabilities) &Account) {_10 let controller = signer.capabilities.storage_10 .getController(byCapabilityID: capabilityID)_10 ?? panic("Cannot get the storage capability controller with ID "_10 .concat(capabilityID.toString())_10 .concat(" from the signer's account! Make sure the ID belongs to a capability that the owner controls and that it is a storage capability.")_10 controller.delete()_10 }_10}`

If the capability is an account capability:

 `_10transaction(capabilityID: UInt64) {_10 prepare(signer: auth(AccountCapabilities) &Account) {_10 let controller = signer.capabilities.account_10 .getController(byCapabilityID: capabilityID)_10 ?? panic("Cannot get the account capability controller with ID "_10 .concat(capabilityID.toString())_10 .concat(" from the signer's account! Make sure the ID belongs to a capability that the owner controls and that it is an account capability.")_10 controller.delete()_10 }_10}`[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/design-patterns.md)[PreviousCore Contracts Guide](/docs/cadence-migration-guide/core-contracts-guide)[NextAnti-Patterns](/docs/anti-patterns)
###### Rate this page

😞😐😊

* [Use named value fields for constants instead of hard-coding](#use-named-value-fields-for-constants-instead-of-hard-coding)
  + [Problem](#problem)
  + [Solution](#solution)
* [Script-Accessible public field/function](#script-accessible-public-fieldfunction)
  + [Problem](#problem-1)
  + [Solution](#solution-1)
* [Script-Accessible report](#script-accessible-report)
  + [Problem](#problem-2)
  + [Solution](#solution-2)
  + [Example](#example)
* [Init singleton](#init-singleton)
  + [Problem](#problem-3)
  + [Solution](#solution-3)
* [Use descriptive names for fields, paths, functions and variables](#use-descriptive-names-for-fields-paths-functions-and-variables)
  + [Problem](#problem-4)
  + [Solution](#solution-4)
  + [Example](#example-1)
* [Plural names for arrays and maps are preferable](#plural-names-for-arrays-and-maps-are-preferable)
* [Use transaction post-conditions when applicable](#use-transaction-post-conditions-when-applicable)
  + [Problem](#problem-5)
  + [Solution](#solution-5)
  + [Example](#example-2)
* [Avoid unnecessary load and save storage operations, prefer in-place mutations](#avoid-unnecessary-load-and-save-storage-operations-prefer-in-place-mutations)
  + [Problem](#problem-6)
  + [Solution](#solution-6)
  + [Example](#example-3)
* [Capability bootstrapping](#capability-bootstrapping)
  + [Problem](#problem-7)
  + [Solution](#solution-7)
* [Check for existing capability before publishing new one](#check-for-existing-capability-before-publishing-new-one)
  + [Problem](#problem-8)
  + [Solution](#solution-8)
  + [Example](#example-4)
* [Capability Revocation](#capability-revocation)
  + [Problem](#problem-9)
  + [Solution](#solution-9)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

