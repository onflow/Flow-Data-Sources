# Source: https://cadence-lang.org/docs/tutorial/resources




3. Resource Contract Tutorial | Cadence




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
* 3. Resource Contract Tutorial
On this page
# 3. Resource Contract Tutorial

## Overview[​](#overview "Direct link to Overview")

tip

Open the starter code for this tutorial in the Flow Playground:   


[<https://play.flow.com/ddf0177e-81c8-4512-ac2e-28036b1a3f89>](https://play.flow.com/ddf0177e-81c8-4512-ac2e-28036b1a3f89)

The tutorial will ask you to take various actions to interact with this code.


Action

Instructions that require you to take action are always included in a callout
box like this one. These highlighted actions are all that you need to do to
get your code running, but reading the rest is necessary to understand the
language's design.

This tutorial builds on the previous `Hello World` tutorial.
Before beginning this tutorial, you should understand :

* [Accounts](/docs/language/accounts)
* [Transactions](/docs/language/transactions)
* Signers
* [Field types](/docs/language/composite-types)

This tutorial will build on your understanding of accounts and how to interact with them by introducing [resources](/docs/language/resources).

Resources are one of Cadence's most important features.

In Cadence, resources are a composite type like a struct or a class in other languages,
but with some special rules.

Here is an example definition of a resource:

 `_10access(all) resource Money {_10_10 access(all) let balance: Int_10_10 init() {_10 self.balance = 0_10 }_10}`

See, it looks just like a regular `struct` definition! The difference is in the behavior.

Resources are useful when you want to model **direct ownership** of an asset or an object.
By **direct ownership**, we mean the ability to own an *actual object* that represents your asset,
instead of just a password or certificate that allows you to access it.
Traditional structs or classes from other conventional programming languages
are not an ideal way to represent direct ownership because they can be *copied*.
This means a coding error can easily result in creating multiple copies of the same asset,
which breaks the scarcity requirements needed for these assets to have real value.
We have to consider loss and theft at the scale of a house, a car, or a bank account with millions of dollars, or a horse.
Resources, in turn, solve this problem by making creation, destruction, and movement of assets explicit.

In this tutorial, you will:

1. Deploy a contract that declares a resource
2. Save the resource into the account storage
3. Interact with the resource we created using a transaction

## Implementing a Contract with Resources[​](#implementing-a-contract-with-resources "Direct link to Implementing a Contract with Resources")

---

To interact with resources, you'll learn a few important concepts:

* Using the `create` keyword
* The move operator `<-`
* The [Account Storage API](/docs/language/accounts/storage)

Let's start by looking at how to create a resource with the `create` keyword and the move operator `<-`.

You use the `create` keyword used to initialize a resource.
Resources can only be created by the contract that defines them and
**must** be created before they can be used.

The move operator `<-` is used to move a resource into a variable.
You cannot use the assignment operator `=` with resources,
so when you initialize them or assign then to a new variable,
you will need to use the move operator `<-`. This indicates that the resource is literally
being *moved* from one place to another. The old variable or location that was holding
it will no longer be valid after the move. This is one of the ways that Cadence ensures
that any given resource only exists in one place at a time.

Action

Open the Account `0x06` tab with file named `HelloWorldResource.cdc`.   

`HelloWorldResource.cdc` should contain the following code:


HelloWorldResource.cdc `_18access(all) contract HelloWorld {_18_18 // Declare a resource that only includes one function._18 access(all) resource HelloAsset {_18_18 // A transaction can call this function to get the "Hello, World!"_18 // message from the resource._18 access(all) view fun hello(): String {_18 return "Hello, World!"_18 }_18 }_18_18 // We're going to use the built-in create function to create a new instance_18 // of the HelloAsset resource_18 access(all) fun createHelloAsset(): @HelloAsset {_18 return <-create HelloAsset()_18 }_18}`
Action

Deploy this code to account `0x06` using the `Deploy` button.

We start by declaring a new `HelloWorld` contract in account `0x06`, inside this new `HelloWorld` contract we:

1. Declare the resource `HelloAsset` with public scope `access(all)`
2. Declare the resource function `hello()` inside `HelloAsset` with public scope `access(all)`
3. Declare the contract function `createHelloAsset()` which `create`s a `HelloAsset` resource
4. The `createHelloAsset()` function uses the move operator (`<-`) to return the resource

This is another example of what we can do with a contract.
Cadence can declare type definitions within deployed contracts.
A type definition is simply a description of how a particular set of data is organized.
It **is not** a copy or instance of that data on its own.
Any account can import these definitions to interact with objects of those types.

This contract that we just deployed declares a definition
for the `HelloAsset` resource and a function to create the resource.

Let's walk through this contract in more detail, starting with the resource.
Resources are one of the most important things that Cadence introduces to the smart contract design experience:

 `_10access(all)_10resource HelloAsset {_10 access(all)_10 view fun hello(): String {_10 return "Hello, World!"_10 }_10}`
### Resources[​](#resources "Direct link to Resources")

The key difference between a `resource` and a `struct` or `class` is the access scope for resources:

* Each instance of a resource can only exist in exactly one location and cannot be copied.
  Here, location refers to account storage, a temporary variable in a function, a storage field in a contract, etc.
* Resources must be explicitly moved from one location to another when accessed.
* Resources also cannot go out of scope at the end of function execution.
  They must be explicitly stored somewhere or explicitly destroyed.

These characteristics make it impossible to accidentally lose a resource from a coding mistake.

**A resource can only be created in the scope that it is defined in.**

This prevents anyone from being able to create arbitrary amounts of resource objects that others have defined.

### The Move Operator (`<-`)[​](#the-move-operator-- "Direct link to the-move-operator--")

In this example, we declared a function that can create `HelloAsset` resources:

 `_10access(all)_10fun createHelloAsset(): @HelloAsset {_10 return <-create HelloAsset()_10}`

The `@` symbol specifies that it is a resource of the type `HelloAsset`, which we defined in the contract.
This function uses the move operator to create a resource of type `HelloAsset` and return it.
To create a new resource object, we use the `create` keyword

Here we use the `<-` symbol. [This is the move operator](/docs/language/resources#the-move-operator--).
The move operator `<-` replaces the assignment operator `=` in assignments that involve resources.
To make the assignment of resources explicit, the move operator `<-` must be used when:

* the resource is the initial value of a constant or variable,
* the resource is moved to a different variable in an assignment,
* the resource is moved to a function as an argument
* the resource is returned from a function.

When a resource is moved, the old location is invalidated, and the object moves into the context of the new location.

So if I have a resource in the variable `first_resource`, like so:

 `_10// Note the `@` symbol to specify that it is a resource_10var first_resource: @AnyResource <- create AnyResource()`

and I want to assign it to a new variable, `second_resource`,
after I do the assignment, `first_resource` is invalid because the underlying resource has been moved to the new variable.

 `_10var second_resource <- first_resource_10// first_resource is now invalid. Nothing can be done with it`

Regular assignments of resources are not allowed because assignments only copy the value.
Resources can only exist in one location at a time, so movement must be explicitly shown in the code by using the move operator `<-`.

### Create Hello Transaction[​](#create-hello-transaction "Direct link to Create Hello Transaction")

Now we're going to use a transaction to that calls the `createHelloAsset()` function
and saves a `HelloAsset` resource to the account's storage.

Action

Open the transaction named `Create Hello`.

`Create Hello` should contain the following code:


create\_hello.cdc `_26/// create_hello.cdc_26/// This transaction calls the createHelloAsset() function from the contract_26/// to create a resource, then saves the resource_26/// in the signer's account storage using the "save" method._26import HelloWorld from 0x06_26_26transaction {_26_26 /// `auth(SaveValue) &Account` signifies an account object_26 /// that has the `SaveValue` authorization entitlement, which means_26 /// that this transaction can't do anything with the &Account object_26 /// besides saving values to storage._26 /// You will learn more about entitlements later_26 prepare(acct: auth(SaveValue) &Account) {_26 // Here we create a resource and move it to the variable newHello,_26 // then we save it in the signer's account storage_26 let newHello <- HelloWorld.createHelloAsset()_26_26 acct.storage.save(<-newHello, to: /storage/HelloAssetTutorial)_26 }_26_26 // In execute, we log a string to confirm that the transaction executed successfully._26 execute {_26 log("Saved Hello Resource to account.")_26 }_26}`

Here's what this transaction does:

1. Import the `HelloWorld` definitions from account `0x06`
2. Uses the `createHelloAsset()` function to create a resource and move it to `newHello`
3. `save` the created resource in the account storage of the account
   that signed the transaction at the path `/storage/HelloAssetTutorial`
4. `log` the text `Saved Hello Resource to account.` to the console.

This is our first transaction using the `prepare` phase!
The `prepare` phase is the only place that has access to the signing account,
via [account references (`&Account`)](/docs/language/accounts/).
Account references have access to many different methods that are used
to interact with and account, e.g., the account's storage.
In this case, the transaction uses `auth(SaveValue) &Account`.
This means that it is an account object that has the `SaveValue` authorization entitlement,
which means that this transaction can't do anything with the `&Account` object
besides saving values to storage.
We'll cover entitlements in more detail in a later tutorial.
You can go to [the entitlements documentation](/docs/language/access-control#entitlements) to learn more about them though.

You can also see the documentation for all of the possible account entitlements
in the [account section of the language reference](/docs/language/accounts/#performing-write-operations).
In this tutorial, we'll be using account functions to save to and load from account storage (`/storage/`).

Accounts store objects at [paths](/docs/language/accounts/paths).
Paths basically represent a file system for your account, where an object can be stored
at any user-defined path. Often, contracts will specify for the user where objects
from that contract should be stored. This enables any code to know
how to access these objects in a standard way.

By not allowing the execute phase to access account storage and using entitlements,
we can statically verify which assets and areas/paths of the signers' account a given transaction can modify.
Browser wallets and applications that submit transactions for users can use this to show what a transaction could alter,
giving users information about transactions that wallets will be executing for them,
and confidence that they aren't getting fed a malicious or dangerous transaction from an app or wallet.

Let's go over the transaction in more detail.
To create a `HelloAsset` resource, we accessed the function `createHelloAsset()` from our contract, and moved the
resource it created to the variable `newHello`.

 `_10let newHello <- HelloWorld.createHelloAsset()`

Next, we save the resource to the account storage.
We use the [account storage API](/docs/language/accounts/storage) to interact with the account storage in Flow.
To save the resource, we'll be using the
[`save()`](/docs/language/accounts/storage)
method from the account storage API to store the resource in the account at the path `/storage/HelloAssetTutorial`.

 `_10acct.storage.save(<-newHello, to: /storage/HelloAssetTutorial)`

The first parameter to `save` is the object that is being stored,
and the `to` parameter is the path that the object is being stored at.
The path must be a storage path, so only the domain `/storage/` is allowed in the `to` parameter.

If there is already an object stored under the given path, the program aborts.
Remember, the Cadence type system ensures that a resource can never be accidentally lost.
When moving a resource to a field, into an array, into a dictionary, or into storage,
there is the possibility that the location already contains a resource.
Cadence forces the developer to handle the case of an existing resource so that it is not accidentally lost through an overwrite.

It is also very important when choosing the name of your paths to pick an identifier
that is very specific and unique to your project.
Currently, account storage paths are global, so there is a chance that projects could use the same storage paths,
**which could cause path conflicts**!
This could be a headache for you, so choose unique path names to avoid this problem.

Finally, in the execute phase we log the phrase `"Saved Hello Resource to account."` to the console.

 `_10log("Saved Hello Resource to account.")`
Action

Select account `0x06` as the only signer. Click the `Send` button to submit
the transaction.

You should see something like this:

 `_10"Saved Hello Resource to account."`
Action

You can also try removing the line of code that saves `newHello` to storage.

You should see an error for `newHello` that says `loss of resource`.
This means that you are not handling the resource properly.
If you ever see this error in any of your programs,
it means there is a resource somewhere that is not being explicitly stored or destroyed, meaning the program is invalid.

Add the line back to make the transaction check properly.

In this case, this is the first time we have saved anything with the selected account,
so we know that the storage spot at `/storage/HelloAssetTutorial` is empty.
In real applications, we would likely perform necessary checks and actions with the location path we are storing in
to make sure we don't abort a transaction because of an accidental overwrite.

Now that you have executed the transaction, account `0x06` should have the newly created `HelloWorld.HelloAsset`
resource stored in its storage. You can verify this by clicking on account `0x06` on the bottom left.
This should open a view of the different contracts and objects in the account.
You should see this entry for the `HelloWorld` contract and the `HelloAsset` resource:

 `_34Deployed Contracts:_34[_34 {_34 "contract": "HelloWorld",_34 "height": 6_34 }_34]_34Account Storage:_34{_34 "Private": null,_34 "Public": {},_34 "Storage": {_34 "HelloAssetTutorial": {_34 "Fields": [_34 39_34 ],_34 "ResourceType": {_34 "Fields": [_34 {_34 "Identifier": "uuid",_34 "Type": {}_34 }_34 ],_34 "Initializers": null,_34 "Location": {_34 "Address": "0x0000000000000005",_34 "Name": "HelloWorld",_34 "Type": "AddressLocation"_34 },_34 "QualifiedIdentifier": "HelloWorld.HelloAsset"_34 }_34 }_34 }_34}`

You'll also see `FlowToken` objects. Every account is automatically initialized
with the ability to use FlowToken assets. You don't have to worry about those for now.

### Load Hello Transaction[​](#load-hello-transaction "Direct link to Load Hello Transaction")

Now we're going to use a transaction to call the `hello()` method from the `HelloAsset` resource.

Action

Open the transaction named `Load Hello`.

`Load Hello` should contain the following code:


load\_hello.cdc `_25import HelloWorld from 0x06_25_25// This transaction calls the "hello" method on the HelloAsset object_25// that is stored in the account's storage by removing that object_25// from storage, calling the method, and then saving it back to the same storage path_25_25transaction {_25_25 /// In this prepare block, we have to load a value from storage_25 /// in addition to saving it, so we also need the `LoadValue` entitlement_25 /// which additionally allows loading values from storage_25 prepare(acct: auth(LoadValue, SaveValue) &Account) {_25_25 // Load the resource from storage, specifying the type to load it as_25 // and the path where it is stored_25 let helloResource <- acct.storage.load<@HelloWorld.HelloAsset>(from: /storage/HelloAssetTutorial)_25 ?? panic("The signer does not have the HelloAsset resource stored at /storage/HelloAssetTutorial. Run the `Create Hello` Transaction again to store the resource")_25_25 // log the hello world message_25 log(helloResource.hello())_25_25 // Put the resource back in storage at the same spot_25 acct.storage.save(<-helloResource, to: /storage/HelloAssetTutorial)_25 }_25}`

Here's what this transaction does:

1. Import the `HelloWorld` definitions from account `0x06`
2. Moves the `HelloAsset` object from storage to `helloResource` with the move operator
   and the `load` function from the [account storage API](/docs/language/accounts/storage)
3. Calls the `hello()` function of the `HelloAsset` resource stored in `helloResource` and logs the result
4. Saves the resource in the account that we originally moved it from at the path `/storage/HelloAssetTutorial`

We're going to be using the `prepare` phase again to load the resource
using the [reference to the account](/docs/language/accounts/) that is passed in.

Let's go over the transaction in more detail.

#### Loads the `HelloAsset` resource from storage[​](#loads-the-helloasset-resource-from-storage "Direct link to loads-the-helloasset-resource-from-storage")

To remove an object from storage, we use the `load` method from the [account storage API](/docs/language/accounts/storage)

 `_10let helloResource <- acct.storage.load<@HelloWorld.HelloAsset>(from: /storage/HelloAssetTutorial)`

If there is an object of the specified type at the path,
the function returns that object and the account storage will no longer contain an object under the given path.

The type parameter for the object type to load is contained in `<>`.
In this case, we're basically saying that we expect to load a `@HelloWorld.HelloAsset` resource object from this path.
A type argument for the parameter must be provided explicitly.
(Note the `@` symbol to specify that it is a resource)

The path `from` must be a storage path, so only the domain `/storage/` is allowed.

If no object of the specified type is stored under the given path, the function returns nothing, or `nil`.
(This is an [Optional](/docs/language/values-and-types#optionals),

Optionals are values that are able to represent either the presence or the absence of a value.
Optionals have two cases: either there is a value of the specified type, or there is nothing (`nil`).
An optional type is declared using the `?` suffix.

 `_10let newResource: HelloAsset? // could either have a value of type `HelloAsset`_10 // or it could have a value of `nil`, which represents nothing`

Optionals allow developers to account for `nil` cases more gracefully.
Here, we explicitly have to account for the possibility that the `helloResource` object we got with `load` is `nil`
(because `load` will return `nil` if there is nothing there to load).

We use the nil-coalescing operator (`??`) to "unwrap" the optional.
This basically means that we are handling the case where the `load` method returns `nil`.
If it returns `nil`, the block of code after `??` executes.
Here, we `panic`, which will abort execution of the transaction
with an error message.

Refer to [Optionals In Cadence](/docs/language/values-and-types#optionals) to learn more about optionals and how they are used.

It is **extremely important** for developers to always provide detailed error messages
so that if something goes wrong in the code, it is obvious to a user and/or developer
what needs to be fixed.

Error messages should contain these if possible:

* Contract name and function name if coming from a contract.
* Description of the literal error that is happening.
* Description of what high-level reason might be causing the error.
* Any metadata or variable values that might are relevant to the error.
* Suggestion for fixing it if possible.

As you can see in our error message, we describe exactly what is wrong,
that the resource is not stored at the correct storage path (which we mention).
Then we suggest a solution to remedy the error, that being to run the "Create Hello"
transaction to store the resource.

Check out the error messages in the [contracts](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L115-L121)
and [transactions](https://github.com/onflow/flow-nft/blob/master/transactions/generic_transfer_with_address_and_type.cdc#L46-L50)
in the Flow NFT GitHub repo for examples of thorough and helpful error messages.

#### Calls the `hello()` function[​](#calls-the-hello-function "Direct link to calls-the-hello-function")

Next, we call the `hello()` function and log the output.

 `_10log(helloResource.hello())`
#### Saves the resource back in the signer's account[​](#saves-the-resource-back-in-the-signers-account "Direct link to Saves the resource back in the signer's account")

Next, we use `save` again to put the object back in storage in the same spot:

 `_10acct.storage.save(<-helloResource, to: /storage/HelloAssetTutorial)`
Action

Select account `0x06` as the only signer. Click the `Send` button to submit
the transaction.

You should see something like this:

 `_10"Hello, World!"`
## Reviewing the Resource Contract[​](#reviewing-the-resource-contract "Direct link to Reviewing the Resource Contract")

This tutorial covered an introduction to resources in Cadence,
using the account storage API and interacting with resources using transactions.

You implemented a smart contract that is accessible in all scopes.
The smart contract had a resource declared that implemented a function called `hello()`
that returns the string `"Hello, World!"`
and declared a function that can create a resource.

Next, you deployed this contract in an account and implemented a transaction to create the resource in the smart contract
and save it in the account `0x06` by using it as the signer for this transaction.

Finally, you used a transaction to move the `HelloAsset` resource from account storage, call the `hello` method,
and return it to the account storage.

Now that you have completed the tutorial, you have the basic knowledge to write a simple Cadence program that can:

* Implement a resource in a smart contract
* Save, move, and load resources using the account storage API and the move operator `<-`
* Use the `prepare` phase of a transaction to load resources from account storage

Feel free to modify the smart contract to create different resources,
experiment with the available [account storage API](/docs/language/accounts/storage),
and write new transactions that execute different functions from your smart contract.
Have a look at the [resource reference page](/docs/language/resources)
to find out more about what you can do with resources.

**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/03-resources.md)[Previous2. Hello World](/docs/tutorial/hello-world)[Next4. Capability Tutorial](/docs/tutorial/capabilities)
###### Rate this page

😞😐😊

* [Overview](#overview)
* [Implementing a Contract with Resources](#implementing-a-contract-with-resources)
  + [Resources](#resources)
  + [The Move Operator (`<-`)](#the-move-operator--)
  + [Create Hello Transaction](#create-hello-transaction)
  + [Load Hello Transaction](#load-hello-transaction)
* [Reviewing the Resource Contract](#reviewing-the-resource-contract)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

