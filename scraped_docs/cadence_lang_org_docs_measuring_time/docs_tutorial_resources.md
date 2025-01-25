# Source: https://cadence-lang.org/docs/tutorial/resources




Resources and the Move (<-) Operator | Cadence




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
* Resources and the Move (<-) Operator
On this page
# Resources and the Move (<-) Operator

This tutorial will build on your understanding of accounts and how to interact with them by introducing [resources](/docs/language/resources). Resources are a special type found in Cadence that are used for any virtual items, properties, or any other sort of data that are **owned** by an account. They can **only exist in one place at a time**, which means they can be moved or borrowed, but they **cannot be copied**.

Working with resources requires you to take a few more steps to complete some tasks, but this level of explicit control makes it nearly impossible to accidentally duplicate, break, or burn an asset.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this tutorial, you'll be able to:

* Instantiate a `resource` in a smart contract with the `create` keyword
* Save, move, and load resources using the [Account Storage API](/docs/language/accounts/storage) and the [move operator](/docs/language/operators#move-operator--) (`<-`)
* Use [`borrow`](/docs/language/accounts/storage#accessing-objects) to access and use a function in a resource
* Use the `prepare` phase of a transaction to load resources from account storage
* Set and use variables in both the `prepare` and `execute` phase
* Use the [nil-coalescing operator (`??`)](/docs/language/operators#nil-coalescing-operator-) to `panic` if a resource is not found

## Resources[​](#resources "Direct link to Resources")

[Resources](/docs/language/resources) are one of the most important and unique features in Cadence. They're a composite type, like a struct or a class in other languages, but with some special rules designed to avoid many of the traditional dangers in smart contract development. The short version is that resources can only exist in one location at a time - they cannot be copied, duplicated, or have multiple references.

Here is an example definition of a resource:

 `_10access(all) resource Money {_10 access(all) let balance: Int_10_10 init() {_10 self.balance = 0_10 }_10}`

See, it looks just like a regular `struct` definition! The difference is in the behavior.

Resources are useful when you want to model **direct ownership** of an asset or an object. By **direct ownership**, we mean the ability to own an **actual object** in **your storage** that represents your asset, instead of just a password or certificate that allows you to access it somewhere else.

Traditional structs or classes from other conventional programming languages
are not an ideal way to represent direct ownership because they can be **copied**. This means a coding error can easily result in creating multiple copies of the same asset, which breaks the scarcity requirements needed for these assets to have real value.

We have to consider loss and theft at the scale of a house, a car, a bank account, or a horse. It's worth a little bit of extra code to avoid accidentally duplicating ownership of one of these properties!

Resources solve this problem by making creation, destruction, and movement of assets explicit.

## Implementing a Contract with Resources[​](#implementing-a-contract-with-resources "Direct link to Implementing a Contract with Resources")

Action

Open the starter code for this tutorial in the Flow Playground:

[<https://play.flow.com/b999f656-5c3e-49fa-96f2-5b0a4032f4f1>](https://play.flow.com/b999f656-5c3e-49fa-96f2-5b0a4032f4f1)

`HelloWorldResource.cdc` contains the following code:


HelloWorldResource.cdc `_10access(all) contract HelloResource {_10 // TODO_10}`
### Defining a Resource[​](#defining-a-resource "Direct link to Defining a Resource")

Similar to other languages, Cadence can declare type definitions within deployed contracts. A type definition is simply a description of how a particular set of data is organized. It **is not** a copy or instance of that data on its own.

Any account can import these definitions to interact with objects of those types.

The key difference between a `resource` and a `struct` or `class` is the access scope for resources:

* Each instance of a resource can only exist in exactly one location and cannot be copied.
  + Here, location refers to account storage, a temporary variable in a function, a storage field in a contract, etc.
* Resources must be explicitly moved from one location to another when accessed.
* Resources also cannot go out of scope at the end of function execution. They must be explicitly stored somewhere or explicitly destroyed.
* A resource can only be created in the scope that it is defined in.
  + This prevents anyone from being able to create arbitrary amounts of resource objects that others have defined.

These characteristics make it impossible to accidentally lose a resource from a coding mistake.

Action

Add a `resource` called `HelloAsset` that contains a function to return a string containing "Hello Resources!":

::

HelloResource.cdc `_10access(all) contract HelloResource {_10 access(all) resource HelloAsset {_10 // A transaction can call this function to get the "Hello Resources!"_10 // message from the resource._10 access(all) view fun hello(): String {_10 return "Hello Resources!"_10 }_10 }_10}`

A few notes on this function:

* `access(all)` makes the function publicly accessible
* `view` indicates that the function does not modify state
* The function return type is a `String`
* The function is **not** present on the contract itself and cannot be called by interacting with the contract

warning

If you're used to Solidity, you'll want to take note that the `view` keyword in Cadence is used in the same cases as both `view` and `pure` in Solidity.

### Creating a Resource[​](#creating-a-resource "Direct link to Creating a Resource")

Next, you'll create a resource with the `create` keyword and the [move operator](/docs/language/operators#move-operator--) (`<-`).

You use the `create` keyword used to initialize a resource. Resources can only be created by the contract that defines them and **must** be created before they can be used.

The move operator `<-` is used to move a resource - you cannot use the assignment operator `=`. When you initialize them or assign then to a new variable, you use the move operator `<-` to **literally move** the resource from one location to another. The old variable or location that was holding it will no longer be valid after the move.

If you create a resource called `first_resource`:

 `_10// Note the `@` symbol to specify that it is a resource_10var first_resource: @AnyResource <- create AnyResource()`

Then move it:

 `_10var second_resource <- first_resource`

The name `first_resource` is **no longer valid or usable**:

 `_10// Bad code, will generate an error_10var third_resource <- first_resource`
Action

Add a function called `createHelloAsset` that creates and returns a `HelloAsset` resource.


HelloWorldResource.cdc `_10access(all) fun createHelloAsset(): @HelloAsset {_10 return <-create HelloAsset()_10}`

Unlike the `hello()` function, this function **does** exist on the contract and can be called directly. Doing so creates an instance of the `HelloAsset` resource, **moves** it through the `return` of the function to the location calling the function - the same as you'd expect for other languages.

Remember, when resources are referenced, the `@` symbol is placed at the beginning. In the function above, the return type is a resource of the `HelloAsset` type.

Action

Deploy this code to account `0x06` by using the `Deploy` button.

## Create Hello Transaction[​](#create-hello-transaction "Direct link to Create Hello Transaction")

Now, we're going to create a transaction that calls the `createHelloAsset()` function and saves a `HelloAsset` resource to the account's storage.

Action

Open the transaction named `Create Hello`.

`Create Hello` should contain the following code:

create\_hello.cdc `_10import HelloWorldResource from 0x06_10_10transaction {_10 // TODO_10}`

We've already imported the `HelloWorldResource` contract for you and stubbed out a `transaction`. Unlike the transaction in Hello World, you will need to modify the user's account, which means you will need to use the `prepare` phase to access and modify the account that is going to get an instance of the resource.

### Prepare Phase[​](#prepare-phase "Direct link to Prepare Phase")

Action

Create a `prepare` phase with the `SaveValue` authorization [entitlement](/docs/language/access-control#entitlements) to the user's account, `create` a new instance of the `HelloAsset`, and save the new resource in the user's account.

First, inside the `transaction`, stub out the `prepare` phase with the authorization [entitlement](/docs/language/access-control#entitlements):


 `_10prepare(acct: auth(SaveValue) &Account) {_10 // TODO_10}`
Action

Next, use the `createHelloAsset` function in `HelloWorldResource` to `create` an instance of the resource and *move* it into a constant:


 `_10let newHello <- HelloWorldResource.createHelloAsset()`
### Storage Paths[​](#storage-paths "Direct link to Storage Paths")

In Cadence Accounts, objects are stored in [paths](/docs/language/accounts/paths). Paths represent a file system for your account, where an object can be stored at any user-defined path. Often, contracts will specify for the user where objects from that contract should be stored. This enables any code to know how to access these objects in a standard way.

Paths start with the character `/`, followed by the domain, the path separator `/`, and finally the identifier. The identifier must start with a letter and can only be followed by letters, numbers, or the underscore `_`. For example, the path `/storage/test` has the domain `storage` and the identifier `test`.

There are two valid domains: `storage` and `public`.

Paths in the storage domain have type `StoragePath`, and paths in the public domain have the type `PublicPath`. Both `StoragePath` and `PublicPath` are subtypes of `Path`.

Paths are not strings and do not have quotes around them.

Action

Use the account reference with the `SaveValue` authorization [entitlement](/docs/language/access-control#entitlements) to move the new resource into storage located in `/storage/HelloAssetTutorial`.


 `_10acct.storage.save(<-newHello, to: /storage/HelloAssetTutorial)`

The first parameter in `save` is the object that is being stored, and the `to` parameter is the path that the object is being stored at. The path must be a storage path, so only the domain `/storage/` is allowed in the `to` parameter.

If there is already an object stored under the given path, the program aborts.

Remember, the Cadence type system ensures that a resource can never be accidentally lost. When moving a resource to a field, into an array, into a dictionary, or into storage, there is the possibility that the location already contains a resource.

Cadence forces the developer to explicitly handle the case of an existing resource so that it is not accidentally lost through an overwrite.

It is also very important when choosing the name of your paths to pick an identifier that is very specific and unique to your project.

Currently, account storage paths are global, so there is a chance that projects could use the same storage paths, **which could cause path conflicts**! This could be a headache for you, so choose unique path names to avoid this problem.

### Execute Phase[​](#execute-phase "Direct link to Execute Phase")

Action

Use the `execute` phase to `log` a message that the resource was successfully saved:


 `_10execute {_10 log("Saved Hello Resource to account.")_10}`

You should have something similar to:

 `_12import HelloResource from 0x06_12_12transaction {_12 prepare(acct: auth(SaveValue) &Account) {_12 let newHello <- HelloResource.createHelloAsset()_12 acct.storage.save(<-newHello, to: /storage/HelloAssetTutorial)_12 }_12_12 execute {_12 log("Saved Hello Resource to account.")_12 }_12}`

This is our first transaction using the `prepare` phase!

The `prepare` phase is the only place that has access to the signing account, via [account references (`&Account`)](/docs/language/accounts/).

Account references have access to many different methods that are used to interact with an account, such as to `save` a resource to the account's storage.

By not allowing the execute phase to access account storage and using entitlements, we can statically verify which assets and areas/paths of the signers' account a given transaction can modify.

Browser wallets and applications that submit transactions for users can use this to show what a transaction could alter, giving users information about transactions that wallets will be executing for them, and confidence that they aren't getting fed a malicious or dangerous transaction from an app or wallet.

Action

Select account `0x06` as the only signer. Click the `Send` button to submit
the transaction.

You'll see in the log:

 `_10"Saved Hello Resource to account."`
Action

`Send` the transaction again from account `0x06`

You'll now get an error, because there's already a resource in `/storage/HelloAssetTutorial`:

 `_10execution error code 1: [Error Code: 1101] error caused by: 1 error occurred:_10 * transaction execute failed: [Error Code: 1101] cadence runtime error: Execution failed:_10error: failed to save object: path /storage/HelloAssetTutorial in account 0x0000000000000009 already stores an object_10 --> 805f4e247a920635abf91969b95a63964dcba086bc364aedc552087334024656:19:8_10 |_1019 | acct.storage.save(<-newHello, to: /storage/HelloAssetTutorial)_10 | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
Action

Try removing the line of code that saves `newHello` to storage.

You'll get an error for `newHello` that says `loss of resource`. This means that you are not handling the resource properly. Remember that if you ever see this error in any of your programs, it means there is a resource somewhere that is not being explicitly stored or destroyed.

**Add the line back before you forget!**

### Reviewing Storage[​](#reviewing-storage "Direct link to Reviewing Storage")

Now that you have executed the transaction, account `0x06` will have the newly created `HelloWorld.HelloAsset` resource stored in its storage. You can verify this by clicking on account `0x06` on the bottom left. This will open a view of the different contracts and objects in the account.

You'll see the resource you created in Account Storage:

 `_49{_49 "value": [_49 {_49 "key": {_49 "value": "value",_49 "type": "String"_49 },_49 "value": {_49 "value": {_49 "id": "A.0000000000000006.HelloResource.HelloAsset",_49 "fields": [_49 {_49 "value": {_49 "value": "269380348805120",_49 "type": "UInt64"_49 },_49 "name": "uuid"_49 }_49 ]_49 },_49 "type": "Resource"_49 }_49 },_49 {_49 "key": {_49 "value": "type",_49 "type": "String"_49 },_49 "value": {_49 "value": "A.0000000000000006.HelloResource.HelloAsset",_49 "type": "String"_49 }_49 },_49 {_49 "key": {_49 "value": "path",_49 "type": "String"_49 },_49 "value": {_49 "value": {_49 "domain": "storage",_49 "identifier": "HelloAssetTutorial"_49 },_49 "type": "Path"_49 }_49 }_49 ],_49 "type": "Dictionary"_49}`

You'll also see `FlowToken` objects, and the `HelloResource` Contract.

Action

Run the transaction from account `0x07` and compare the differences between the accounts.

### Checking for Existing Storage[​](#checking-for-existing-storage "Direct link to Checking for Existing Storage")

In real applications, you need to check the location path you are storing in to make sure both cases are handled properly.

Action

First, update the authorization [entitlement](/docs/language/access-control#entitlements) in the prepare phase to include `BorrowValue`:


 `_10prepare(acct: auth(BorrowValue, SaveValue) &Account) {_10 // Existing code..._10}`
Action

Next, add a `transaction`-level variable to store a result `String`:

Similar to a class-level variable in other languages, these go at the top, inside the `transaction` scope, but not inside anything else. They are accessible in both the `prepare` and `execute` statements of a transaction.

 `_10import HelloResource from 0x06_10_10transaction {_10 var result: String_10 // Other code..._10}`

You'll get an error: `missing initialization of field` result`in type`Transaction`. not initialized`

In transactions, variables at the `transaction` level must be initialized in the `prepare` phase.

Action

Initialize the `result` message and create a constant for the storage path.


 `_10self.result = "Saved Hello Resource to account."_10let storagePath = /storage/HelloAssetTutorial`
warning

In Cadence, storage paths are a type. They are **not** `Strings` and are not enclosed by quotes.

One way to check whether or not a storage path has an object in it is to use the built-in [`storage.check`](/docs/language/accounts/storage#accountstorage) function with the type and path. If the result is `true`, then there is an object in account storage that matches the type requested. If it's `false`, there is not.

 `_10_10A response of `false` does **not** mean the location is empty. If you ask for an apple and the location contains an orange, this function will return `false`._10_10This is not likely to occur because projects are encouraged to create storage and public paths that are very unique, but is theoretically possible if projects don't follow this best practice or if there is a malicious app that tries to store things in other projects' paths.`

Depending on the needs of your app, you'll use this pattern to decide what to do in each case. For this example, we'll simply use it to change the log message if the storage is in use or create and save the `HelloAsset` if it is not.

Action

Refactor your prepare statement to check and see if the storage path is in use. If it is, update the `result` message. Otherwise, create and save a `HelloAsset`:


 `_10if !acct.storage.check<&HelloWorldResource.HelloAsset>(from: storagePath) {_10 self.result = "Unable to save, resource already present."_10} else {_10 let newHello <- HelloWorldResource.createHelloAsset()_10 acct.storage.save(<-newHello, to: storagePath)_10}`

When you [`check`] a resource, you must put the type of the resource to be borrowed inside the `<>` after the call to `borrow`, before the parentheses. The `from` parameter is the storage path to the object you are borrowing.

Action

Finally, update the `log` in execute to use `self.result` instead of the hardcoded string:


 `_10execute {_10 log(self.result)_10}`
Action

`Send` the transaction again, both with accounts that have and have not yet created and stored an instance of `HelloAsset`.

Now you'll see an appropriate log whether or not a new resource was created and saved.

## Load Hello Transaction[​](#load-hello-transaction "Direct link to Load Hello Transaction")

Now we're going to use a transaction to call the `hello()` method from the `HelloAsset` resource.

Action

Open the transaction named `Load Hello`.

It's empty!

Action

On your own, stub out a transaction that imports `HelloWorldResource` and passes in an account [reference](/docs/language/references) with the `BorrowValue` authorization entitlement.

You should end up with something like this:

load\_hello.cdc `_10import HelloWorldResource from 0x06_10_10transaction {_10_10 prepare(acct: auth(BorrowValue) &Account) {_10 // TODO_10 }_10}`

You just learned how to [`borrow`](/docs/language/accounts/storage#accessing-objects) a [reference](/docs/language/references) to a resource. You could use an `if` statement to handle the possibility that the resource isn't there, but if you want to simply terminate execution, a common practice is to combine a `panic` statement with the [nil-coalescing operator (`??`)](/docs/language/operators#nil-coalescing-operator-).

This operator executes the statement on the left side. If that is `nil`, the right side is evaluated and returned. In this case, the return is irrelevant, because we're going to cause a `panic` and terminate execution.

Action

Create a variable with a [reference](/docs/language/references) to the `HelloAsset` resource stored in the user's account. Panic if this resource is not found.


 `_10let helloAsset = acct.storage.borrow<&HelloWorldResource.HelloAsset>(from: /storage/HelloAssetTutorial)_10 ?? panic("The signer does not have the HelloAsset resource stored at /storage/HelloAssetTutorial. Run the `Create Hello` Transaction to store the resource")`
Action

Finally, `log` the return from a call to the `hello()` function.


warning

Borrowing a [reference](/docs/language/references) does **not** allow you to move or destroy a resource, but it **does allow** you to mutate data inside that resource via one of the resource's functions.

Your transaction should be similar to:

 `_10import HelloWorldResource from 0x06_10_10transaction {_10 prepare(acct: auth(BorrowValue, LoadValue, SaveValue) &Account) {_10 let helloAsset = acct.storage.borrow<&HelloWorldResource.HelloAsset>(from: /storage/HelloAssetTutorial)_10 ?? panic("The signer does not have the HelloAsset resource stored at /storage/HelloAssetTutorial. Run the `Create Hello` Transaction again to store the resource")_10_10 log(helloAsset.hello())_10 }_10}`

In Cadence, we have the resources to leave very detailed error messages. Check out the error messages in the [Non-Fungible Token Contract] and [Generic NFT Transfer transaction] in the Flow NFT GitHub repo for examples of production error messages.

Action

Test your transaction with several accounts to evaluate all possible cases.

## Reviewing the Resource Contract[​](#reviewing-the-resource-contract "Direct link to Reviewing the Resource Contract")

In this tutorial you learned how to `create` [resources](/docs/language/resources) in Cadence. You implemented a smart contract that is accessible in all scopes. The smart contract has a resource declared that implemented a function called `hello()`, that returns the string `"Hello, World!"`. It also declares a function that can create a resource.

Next, you implemented a transaction to create the resource and save it in the account calling it.

Finally, you used a transaction to [borrow](/docs/language/accounts/storage#accessing-objects) a [reference](/docs/language/references) to the `HelloAsset` resource from account storage and call the `hello` method

Now that you have completed the tutorial, you can:

* Instantiate a `resource` in a smart contract with the `create` keyword
* Save, move, and load resources using the [Account Storage API](/docs/language/accounts/storage) and the [move operator](/docs/language/operators#move-operator--) (`<-`)
* Use [`borrow`](/docs/language/accounts/storage#accessing-objects) to access and use a function in a resource
* Use the `prepare` phase of a transaction to load resources from account storage
* Set and use variables in both the `prepare` and `execute` phase
* Use the [nil-coalescing operator (`??`)](/docs/language/operators#nil-coalescing-operator-) to `panic` if a resource is not found

[Non-Fungible Token Contract]: <https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc#L115-L121>)
[Generic NFT Transfer transaction]: <https://github.com/onflow/flow-nft/blob/master/transactions/generic_transfer_with_address_and_type.cdc#L46-L50>

**Tags:**

* [reference](/docs/tags/reference)
* [cadence](/docs/tags/cadence)
* [tutorial](/docs/tags/tutorial)
[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/03-resources.md)[PreviousHello World](/docs/tutorial/hello-world)[NextCapabilities](/docs/tutorial/capabilities)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Resources](#resources)
* [Implementing a Contract with Resources](#implementing-a-contract-with-resources)
  + [Defining a Resource](#defining-a-resource)
  + [Creating a Resource](#creating-a-resource)
* [Create Hello Transaction](#create-hello-transaction)
  + [Prepare Phase](#prepare-phase)
  + [Storage Paths](#storage-paths)
  + [Execute Phase](#execute-phase)
  + [Reviewing Storage](#reviewing-storage)
  + [Checking for Existing Storage](#checking-for-existing-storage)
* [Load Hello Transaction](#load-hello-transaction)
* [Reviewing the Resource Contract](#reviewing-the-resource-contract)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

