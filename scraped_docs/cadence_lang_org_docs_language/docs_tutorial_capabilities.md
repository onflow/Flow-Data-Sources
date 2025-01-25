# Source: https://cadence-lang.org/docs/tutorial/capabilities




Capabilities | Cadence




[Skip to main content](#__docusaurus_skipToContent_fallback)[![Cadence](/img/logo.svg)![Cadence](/img/logo.svg)](/)[Learn](/learn)[Solidity Guide](/docs/solidity-to-cadence)[Playground](https://play.flow.com/)[Community](/community)[Security](https://flow.com/flow-responsible-disclosure/)[Documentation](/docs/)[1.0](/docs/)Search

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
* Capabilities
On this page
# Capabilities

This tutorial will build on your understanding of [accounts](/docs/language/accounts/) and [resources](/docs/language/resources). You'll learn how to interact with resources using [capabilities](/docs/language/capabilities) and [entitlements](/docs/language/access-control#entitlements).

Reminder

In Cadence, resources are a composite type like a struct or a class, but with some **special rules**:

* Each instance of a resource can only exist in exactly one location and cannot be copied.
* Resources must be explicitly moved from one location to another when accessed.
* Resources also cannot go out of scope at the end of function execution, they must be explicitly stored somewhere or destroyed.
## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Interact with [resources](/docs/language/resources) created using transactions.
* Write transactions to create [capabilities](/docs/language/capabilities) to extend resource access scope from the owner to anyone (`public`).
* Write and execute a script that interacts with the resource through the capability.

## Use-Cases for Capabilities and Entitlements[​](#use-cases-for-capabilities-and-entitlements "Direct link to Use-Cases for Capabilities and Entitlements")

Let's look at why you would want to use capabilities and entitlements to expand access to resources in a real-world context. A real user's account and stored objects will contain functions and fields that need varying levels of access scope and privacy.

If you're working on an app that allows users to exchange tokens, you'll want different features available in different use cases. While you definitely want to make a feature like withdrawing tokens from an account only accessible by the owner of the tokens, your app should allow anybody to deposit tokens.

Capabilities and entitlements are what allows for this detailed control of access to owned assets. They allow a user to indicate which of the functionality of their account and owned objects should be accessible to themselves, their trusted friends, and the public.

For example, a user might want to allow a friend of theirs to use some of their money to spend, in this case, they could create an entitled capability that gives the friend access to only this part of their account, instead of having to hand over full control.

Another example is when a user authenticates a trading app for the first time, the trading app could ask the user for a capability object that allows the app to access the trading functionality of a user's account so that the app doesn't need to ask the user for a signature every time it wants to do a trade. The user can choose to empower the app, and that app alone, for this functionality and this functionality alone.

## Accessing Resources with Capabilities[​](#accessing-resources-with-capabilities "Direct link to Accessing Resources with Capabilities")

As a smart contract developer, you need explicit permission from the owner of an account to access its [storage](/docs/language/accounts/storage). Capabilities allow an account owner to grant access to specific fields and functions on objects stored in their account.

First, you'll write a transaction in which you'll issue a new capability using the `issue` function. This capability creates a link to the user's `HelloAsset` resource object. It then publishes that link to the account's public space, so others can access it.

Next, you'll write a script that anyone can use that link to borrow a [reference](/docs/language/references) to the underlying object and call the `hello()` function.

## Creating Capabilities and References to Stored Resources[​](#creating-capabilities-and-references-to-stored-resources "Direct link to Creating Capabilities and References to Stored Resources")

Action

Continue working with your code from the previous tutorial. Alternately, open a fresh copy here:

[<https://play.flow.com/64287da4-50c4-4580-8b9f-5792b78d77c3>](https://play.flow.com/64287da4-50c4-4580-8b9f-5792b78d77c3)
Action

If you started with a fresh playground, be sure to deploy the `HelloWorld` contract with account `0x06` and call the `Create Hello` transaction, also with `0x06`.

### Prepare the Account Capabilities[​](#prepare-the-account-capabilities "Direct link to Prepare the Account Capabilities")

Action

Create a new transaction called `Create Link`.

Import `HelloWorld` and stub out a `transaction` with a `prepare` phase.


tip

Cadence allows for static analysis of imported contracts. You'll get errors in the transactions and scripts that import `HelloWorld` from `0x06` if you haven't deployed that contract.


create\_link.cdc `_10import HelloWorld from 0x06_10_10transaction {_10 prepare() {_10 // TODO_10 }_10}`
Action

Next, pass an `&Account` reference into `prepare` with the capabilities needed to give the `transaction` the ability to create and publish a capability.


create\_link.cdc `_10import HelloWorld from 0x06_10_10transaction {_10 prepare(account: auth(_10 IssueStorageCapabilityController,_10 PublishCapability_10 ) &Account) {_10 // TODO_10 }_10}`

The [`IssueStorageCapabilityController`](/docs/language/accounts/capabilities#accountstoragecapabilities-and-accountaccountcapabilities) allows the transaction to [issue](/docs/language/accounts/capabilities#issuing-capabilities) a new capability, which includes storing that capability to the user's account. [`PublishCapability`](/docs/language/accounts/capabilities#accountcapabilities) allows the transaction to [publish](/docs/language/accounts/capabilities#publishing-capabilities) a capability and make it available to other users - in this case, we'll make it public.

### Capability Based Access Control[​](#capability-based-access-control "Direct link to Capability Based Access Control")

[Capabilities](/docs/language/capabilities) allow the owners of objects to specify what functionality of their private objects is available to others. Think of it kind of like an account's API, if you're familiar with the concept.

The account owner has private objects stored in their storage, like their collectibles or their money, but they might still want others to be able to see what collectibles they have in their account, or they want to allow anyone to access the deposit functionality for a certain asset.

Since these objects are stored in private storage by default, the owner has to authorize something to open up access to these while still retaining full control.

We create capabilities to accomplish this, and the account owner must sign a transaction to [issue](/docs/language/accounts/capabilities#issuing-capabilities) and [publish](/docs/language/accounts/capabilities#publishing-capabilities) them.

Every capability has a `borrow` method, which creates a reference to the object that the capability is linked to. This reference is used to read fields or call methods on the object they reference, **as if the owner of the reference had the actual object**.

It is important to remember that someone else who has access to a capability cannot move or destroy the object that the capability is linked to! They can only access fields that the owner has explicitly declared in the type specification and authorization-level of the [issue](/docs/language/accounts/capabilities#issuing-capabilities) method.

### Issue the Capability[​](#issue-the-capability "Direct link to Issue the Capability")

Capabilities are created with the [issue](/docs/language/accounts/capabilities#issuing-capabilities) function and can be stored in variables or constants.

Action

Issue a capability to allow access to the instance of the `HelloAsset` [resource](/docs/language/resources) the `Create Hello` transaction saved in `/storage/HelloAssetTutorial`.


 `_10let capability = account_10 .capabilities_10 .storage_10 .issue<&HelloWorld.HelloAsset>(/storage/HelloAssetTutorial)`
danger

In our example capability, we had the user sign a transaction that gave public access to **everything** found in the `HelloAsset` resource!

When you're writing real transactions, follow the principle of giving minimal access. While the capability cannot move or destroy an object, it might be able to mutate data inside of it in a way that the owner does not desire.

For example, if you added a function to allow the owner of the resource to change the greeting message, this code would open that function up to anyone and everyone!


 `_10let capability = account_10 .capabilities_10 .storage_10 .issue<&HelloWorld.HelloAsset>(/storage/HelloAssetTutorial)`

The capability says that whoever borrows a reference from this capability has access to the fields and methods that are specified by the type and entitlements in `<>`. The specified type has to be a subtype of the type of the object being linked to, meaning that it cannot contain any fields or functions that the linked object doesn't have.

A reference is referred to by the `&` symbol. Here, the capability references the `HelloAsset` object, so we specify `<&HelloWorld.HelloAsset>` as the type, which gives access to **everything** in the `HelloAsset` object.

The argument to the `issue` function is the path to the object in storage that is to be linked to. When a capability is issued, a [capability controller](/docs/language/accounts/capabilities#accountcapabilities) is created for it in `account.capabilities`. This controller allows the creator of the capability to have fine-grained control over the capability.

Capabilities usually link to objects in the `/storage/` domain,
but can also be created for `Account` objects. Account capabilities will not be covered in this tutorial.

### Publish the Capability[​](#publish-the-capability "Direct link to Publish the Capability")

Now that your transaction has created the capability with the [issue](/docs/language/accounts/capabilities#issuing-capabilities) function and saved it in a constant, you can use the [publish](/docs/language/accounts/capabilities#publishing-capabilities) function to store the capability in a place where it can be used by anyone.

Action

Use [publish](/docs/language/accounts/capabilities#publishing-capabilities) function to publish the `capability` at `/public/HelloAssetTutorial`.


 `_10account.capabilities.publish(capability, at: /public/HelloAssetTutorial)`

You should end up with a transaction similar to:

Create `_17import HelloWorld from 0x06_17_17transaction {_17 prepare(account: auth(_17 IssueStorageCapabilityController,_17 PublishCapability_17 ) &Account) {_17 let capability = account_17 .capabilities_17 .storage_17 .issue<&HelloWorld.HelloAsset>(/storage/HelloAssetTutorial)_17_17 account_17 .capabilities_17 .publish(capability, at: /public/HelloAssetTutorial)_17 }_17}`
### Execute the Transaction to Publish the Capability[​](#execute-the-transaction-to-publish-the-capability "Direct link to Execute the Transaction to Publish the Capability")

Action

Ensure account `0x06` is still selected as a transaction signer.

Click the `Send` button to send the transaction. Then, send it a second time.


warning

This implementation will work the first time and fail the second. The object cannot be saved because something is already at the path.

As you learned in the [resources tutorial](/docs/tutorial/resources), Cadence prevents you from writing code that might accidentally overwrite an object in storage, thus mutating or even destroying a piece of your users' digital property.

action

On your own, refactor your `Create Link` transaction to elegantly handle a scenario where an object is already stored at `/public/HelloAssetTutorial`

## Using the Capability in a Script[​](#using-the-capability-in-a-script "Direct link to Using the Capability in a Script")

Now that you've published the capability with `public` `access`, anyone who wants to can write transactions or scripts that make use of it.

Action

Create a script called `GetGreeting`. Import `HelloWorld` and give it public `access`.


GetGreeting.cdc `_10import HelloWorld from 0x06_10_10access(all) fun main(): String {_10 // TODO_10}`

You'll need a reference to the public account object for the `0x06` account to be able to access public capabilities within it.

Action

Use `getAccount` to get a reference to account `0x06`. Hardcode it for now.


 `_10let helloAccount = getAccount(0x06)`
warning

Addresses are **not** strings and thus do **not** have quotes around them.


Action

Next, `borrow` the public capability your `Create Link` transaction saved in `/public/HelloAssetTutoral`.

Your script should return `return helloReference.hello()`.

You've already borrowed something before. Try to implement this on your own. **Hint:** this time you're borrowing a `capability` from the account, **not** something from `storage`. Don't forget to handle the case where the object can't be found!

You should end up with a script similar to:

GetGreeting.cdc `_12import HelloWorld from 0x06_12_12access(all) fun main(): String {_12 let helloAccount = getAccount(0x06)_12_12 let helloReference = helloAccount_12 .capabilities_12 .borrow<&HelloWorld.HelloAsset>(/public/HelloAssetTutorial)_12 ?? panic("Could not borrow a reference to the HelloAsset capability")_12_12 return helloReference.hello()_12}`
Action

`Execute` your script.

You'll see `"Hello, World!"` logged to the console.

Note that scripts don't need any authorization and can only access public information. You've enabled the user to make this capability public through the transaction you wrote and they signed.

At the end of the script execution, the `helloReference` value is lost, but that is ok because while it references a resource, it isn't the actual resource itself. It's ok to lose it.

## Deleting Capabilities[​](#deleting-capabilities "Direct link to Deleting Capabilities")

danger

While most apps will need to depend on users storing resource that allow the user to interact with the app, avoid constructing your app logic such that it depends on something in a user's storage for important metadata. They own their storage and can delete anything in it at any time without asking anyone.

For example, if you stored the amount of debt for tokens you'd lent a user as a standalone resource in their account, they could simply delete the storage and erase the debt. Instead, store that metadata in your smart contract.

The owner of an object can effectively [revoke capabilities](/docs/language/accounts/capabilities#revoking-capabilities) they have created by using the `delete` method on the Capability Controller that was created for the capability when it was issued.

Additionally, if the referenced object in storage is moved, capabilities that have been created from that storage path are invalidated.

## Reviewing Capabilities[​](#reviewing-capabilities "Direct link to Reviewing Capabilities")

This tutorial expanded on the idea of resources in Cadence by expanding access scope to a resource using capabilities and covering more account storage API use-cases.

You deployed a smart contract with a resource, then created a capability to grant access to that resource. With the capability, you used the `borrow` method in a script to create a reference to the capability. You then used the reference to call the resource's `hello()` function. This is important because scripts cannot access account storage without using capabilities.

Now that you have completed the tutorial, you should be able to:

* Interact with [resources](/docs/language/resources) created using transactions.
* Write transactions to create [capabilities](/docs/language/capabilities) to extend resource access scope from the owner to anyone (`public`).
* Write and execute a script that interacts with the resource through the capability.

You're on the right track to building more complex applications with Cadence. Now is a great time to check out the [Cadence Best Practices document](/docs/design-patterns), [Anti-patterns document](/docs/anti-patterns), and the first NFT tutorial!

**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/04-capabilities.md)[PreviousResources and the Move (<-) Operator](/docs/tutorial/resources)[NextBasic NFT](/docs/tutorial/non-fungible-tokens-1)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Use-Cases for Capabilities and Entitlements](#use-cases-for-capabilities-and-entitlements)
* [Accessing Resources with Capabilities](#accessing-resources-with-capabilities)
* [Creating Capabilities and References to Stored Resources](#creating-capabilities-and-references-to-stored-resources)
  + [Prepare the Account Capabilities](#prepare-the-account-capabilities)
  + [Capability Based Access Control](#capability-based-access-control)
  + [Issue the Capability](#issue-the-capability)
  + [Publish the Capability](#publish-the-capability)
  + [Execute the Transaction to Publish the Capability](#execute-the-transaction-to-publish-the-capability)
* [Using the Capability in a Script](#using-the-capability-in-a-script)
* [Deleting Capabilities](#deleting-capabilities)
* [Reviewing Capabilities](#reviewing-capabilities)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

