# Source: https://cadence-lang.org/docs/tutorial/resources-compose




10. Composable Resources | Cadence




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
* 10. Composable Resources
On this page
# 10. Composable Resources

In this tutorial, we're going to walk through how resources can own other resources by creating, deploying, and moving composable NFTs.

---


Action

This tutorial just includes example code. It does not have an associated playground project.
You are still welcome to copy this code and paste it to the playground to test it out though!

Resources owning other resources is a powerful feature in the world of blockchain and smart contracts.

**Before proceeding with this tutorial**, we recommend following the instructions in [Getting Started](/docs/tutorial/first-steps),
[Hello, World!](/docs/tutorial/hello-world),
and [Resources](/docs/tutorial/resources) to learn about the Playground and Cadence.

## Resources Owning Resources[​](#resources-owning-resources "Direct link to Resources Owning Resources")

---

The NFT collections talked about in [Non-Fungible Tokens](/docs/tutorial/non-fungible-tokens-1) are examples of resources that own other resources.
We have a resource, the NFT collection, that has ownership of the NFT resources that are stored within it.
The owner and anyone with a reference can move these resources around,
but they still belong to the collection while they are in it and the code defined in the collection has ultimate control over the resources.

When the collection is moved or destroyed, all of the NFTs inside of it are moved or destroyed with it.

If the owner of the collection transferred the whole collection resource to another user's account,
all of the tokens will move to the other user's account with it. The tokens don't stay in the original owner's account.
This is like handing someone your wallet instead of just a dollar bill. It isn't a common action, but certainly is possible.

References cannot be created for resources that are stored in other resources.
The owning resource has control over it and therefore controls the type of access that external calls have on the stored resource.

## Resources Owning Resources: An Example[​](#resources-owning-resources-an-example "Direct link to Resources Owning Resources: An Example")

---

The NFT collection is a simple example of how resources can own other resources, but innovative and more powerful versions can be made.

An important feature of CryptoKitties (and other applications on the Ethereum blockchain) is that any developer can make new experiences around the existing application.
Even though the original contract didn't include specific support for CryptoKitty accessories (like hats), an independent developer was still able to make hats that Kitties from the original contract could use.

Here is a basic example of how we can replicate this feature in Cadence:

KittyVerse.cdc `_79// KittyVerse.cdc_79//_79// The KittyVerse contract defines two types of NFTs._79// One is a KittyHat, which represents a special hat, and_79// the second is the Kitty resource, which can own Kitty Hats._79//_79// You can put the hats on the cats and then call a hat function_79// that tips the hat and prints a fun message._79//_79// This is a simple example of how Cadence supports_79// extensibility for smart contracts, but the language will soon_79// support even more powerful versions of this._79//_79_79access(all) contract KittyVerse {_79_79 // KittyHat is a special resource type that represents a hat_79 access(all) resource KittyHat {_79_79 access(all) let id: Int_79 _79 access(all) let name: String_79_79 init(id: Int, name: String) {_79 self.id = id_79 self.name = name_79 }_79_79 // An example of a function someone might put in their hat resource_79 access(all) fun tipHat(): String {_79 if self.name == "Cowboy Hat" {_79 return "Howdy Y'all"_79 } else if self.name == "Top Hat" {_79 return "Greetings, fellow aristocats!"_79 }_79_79 return "Hello"_79 }_79 }_79_79 // Create a new hat_79 access(all) fun createHat(id: Int, name: String): @KittyHat {_79 return <-create KittyHat(id: id, name: name)_79 }_79_79 access(all) resource Kitty {_79_79 access(all) let id: Int_79_79 // place where the Kitty hats are stored_79 access(all) var items: @{String: KittyHat}_79_79 init(newID: Int) {_79 self.id = newID_79 self.items <- {}_79 }_79_79 access(all) fun getKittyItems(): @{String: KittyHat} {_79 var other: @{String:KittyHat} <- {}_79 self.items <-> other_79 return <- other_79 }_79_79 access(all) fun setKittyItems(items: @{String: KittyHat}) {_79 var other <- items_79 self.items <-> other_79 destroy other_79 }_79_79 access(all) fun removeKittyItem(key: String): @KittyHat? {_79 var removed <- self.items.remove(key: key)_79 return <- removed_79 }_79 }_79_79 access(all) fun createKitty(): @Kitty {_79 return <-create Kitty(newID: 1)_79 }_79}`

These definitions show how a Kitty resource could own hats.

The hats are stored in a variable in the Kitty resource.

 `_10 // place where the Kitty hats are stored_10 access(all) var items: @{String: KittyHat}`

A Kitty owner can take the hats off the Kitty and transfer them individually. Or the owner can transfer a Kitty that owns a hat, and the hat will go along with the Kitty.

Here is a transaction to create a `Kitty` and a `KittyHat`, store the hat in the Kitty, then store it in your account storage.

create\_kitty.cdc `_30import KittyVerse from 0x06_30_30// This transaction creates a new kitty, creates two new hats and_30// puts the hats on the cat. Then it stores the kitty in account storage._30transaction {_30 prepare(acct: auth(SaveValue) &Account) {_30_30 // Create the Kitty object_30 let kitty <- KittyVerse.createKitty()_30_30 // Create the KittyHat objects_30 let hat1 <- KittyVerse.createHat(id: 1, name: "Cowboy Hat")_30 let hat2 <- KittyVerse.createHat(id: 2, name: "Top Hat")_30_30 let kittyItems <- kitty.getKittyItems()_30_30 // Put the hat on the cat!_30 let oldCowboyHat <- kittyItems["Cowboy Hat"] <- hat1_30 destroy oldCowboyHat_30 let oldTopHat <- kittyItems["Top Hat"] <- hat2_30 destroy oldTopHat_30_30 kitty.setKittyItems(items: <-kittyItems)_30_30 log("The cat has the hats")_30_30 // Store the Kitty in storage_30 acct.storage.save(<-kitty, to: /storage/kitty)_30 }_30}`

Now we can run a transaction to move the Kitty along with its hat, remove the cowboy hat from the Kitty, then make the Kitty tip its hat.

tip\_hat.cdc `_27import KittyVerse from 0x06_27_27// This transaction moves a kitty out of storage, takes the cowboy hat off of the kitty,_27// calls its tip hat function, and then moves it back into storage._27transaction {_27 prepare(acct: auth(Storage) &Account) {_27_27 // Move the Kitty out of storage, which also moves its hat along with it_27 let kitty <- acct.storage.load<@KittyVerse.Kitty>(from: /storage/kitty)_27 ?? panic("Kitty doesn't exist!")_27_27 // Take the cowboy hat off the Kitty_27 let cowboyHat <- kitty.removeKittyItem(key: "Cowboy Hat")_27 ?? panic("cowboy hat doesn't exist!")_27_27 // Tip the cowboy hat_27 log(cowboyHat.tipHat())_27 destroy cowboyHat_27_27 // Tip the top hat that is on the Kitty_27 log(kitty.items["Top Hat"]?.tipHat())_27_27 // Move the Kitty to storage, which_27 // also moves its hat along with it._27 acct.storage.save(<-kitty, to: /storage/kitty)_27 }_27}`

If you were to run this transaction, you should see something like this output:

 `_10> "Howdy Y'all"_10> "Greetings, fellow aristocats!"`

Whenever the Kitty is moved, its hats are implicitly moved along with it. This is because the hats are owned by the Kitty.

## The Future is Meow! Extensibility is coming![​](#the-future-is-meow-extensibility-is-coming "Direct link to The Future is Meow! Extensibility is coming!")

---

The above is a simple example of composable resources.
We had to explicitly say that a Kitty could own a Hat in this example,
but Cadence now supports more powerful ways of achieving resource extensibility
where developers can declare types that separate resources can own
even if the owning resource never specified the ownership possibility in the first place.

This feature is called [Attachments](https://cadence-lang.org/docs/language/attachments)
and you should check out the documentation to learn about this powerful feature!

Practice what you're learned in the Flow Playground!

[Edit this page](https://github.com/onflow/cadence-lang.org/tree/main/docs/tutorial/10-resources-compose.md)[Previous9. Voting Contract](/docs/tutorial/voting)[NextLanguage Reference](/docs/language/)
###### Rate this page

😞😐😊

* [Resources Owning Resources](#resources-owning-resources)
* [Resources Owning Resources: An Example](#resources-owning-resources-an-example)
* [The Future is Meow! Extensibility is coming!](#the-future-is-meow-extensibility-is-coming)
Got suggestions for this site? 

* [It's open-source!](https://github.com/onflow/cadence-lang.org)
The source code of this site is licensed under the Apache License, Version 2.0.
Content is licensed under the Creative Commons Attribution 4.0 International License.

