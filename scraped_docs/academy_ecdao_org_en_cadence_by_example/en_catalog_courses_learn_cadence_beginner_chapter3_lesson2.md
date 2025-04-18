# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter3/lesson2

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/learn-cadence-beginner)

1. Cadence Basic Concepts

[1.1 Our First Smart Contract](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson1)[1.2 Transactions and Scripts](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson2)[1.3 Types](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson3)

2. Structs, Resources, and Contract State

[2.1 Basic Structs](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson1)[2.2 Resources](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson2)[2.3 Contract State](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson3)

3. References, Account Storage, and Access Modifiers

[3.1 References](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson1)[3.2 Account Storage](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson2)[3.3 Access Modifiers](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson3)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/learn-cadence-beginner)
Learn Cadence Beginner

# Chapter 3 Lesson 2 - Account Storage

So far, we have been storing all of our data inside the smart contract. Today, we will learn how we can store a Pokemon directly in our own account and catch it just like the real show!

![](https://i.imgur.com/QnB7MW0.png)

## Accounts on Flow

In Cadence, users can store & own their data. This is *very different* from other languages like Solidity on Ethereum, where your NFT gets stored in the smart contract. In Cadence, if I own an NFT, it gets stored in my account.

You can manage your account (like storing and deleting things) in a transaction. Every time a user sends a transaction, they âsignâ it. All that means is you clicked a button (or provided a private key) saying âhey, I want to approve this transaction.â When you sign it, the transaction takes in your `&Account` - a type that lets you manage it based on the âentitlementsâ granted. More on this below.

## Account Storage

You can think of account storage as a container inside your account that stores all your data that lives at different storage paths. Think of it like your own computer where you store files (âdataâ) in different folders (âstorage pathsâ).

In order to store data somewhere, you must save it to a certain storage path. Letâs see an example using our `Game` contract from the last lesson:

cadence

```
		
			import Game from "./Game.cdc"

transaction(name: String, type: String) {
  prepare(signer: &Account) {
    // create a new pokemon resource
    let newPokemon: @Game.Pokemon <- Game.createPokemon(name: name, type: type)
    // attempt to store it in your account
    signer.storage.save(<- newPokemon, to: /storage/MyPokemon)
  }

  execute {}
}
		 
	
```

This transaction looks perfect, and in fact it almost isâ¦ but if you try to run it, it will fail! This is because in order to perform certain actions on your `&Account` (like `save`), you need certain âentitlementsâ that unlock different actions. We will learn a few built-in entitlements for managing accounts below.

We will learn a lot about entitlements in the intermediate course. For now, we will learn just a few built-in entitlements that are used for managing accounts.

### Save and Load Functions

Letâs see how to properly save and remove data from our account.

cadence

```
		
			import Game from "./Game.cdc"

transaction(name: String, type: String) {
  // notice the `SaveValue` entitlement - this allows
  // us to call the `save` function
  prepare(signer: auth(SaveValue) &Account) {
    // create a new pokemon
    let newPokemon: @Game.Pokemon <- Game.createPokemon(name: name, type: type)
    // saves `newPokemon` to my account storage at this path:
    // /storage/MyPokemon
    signer.storage.save(<- newPokemon, to: /storage/MyPokemon)
  }

  execute {}
}
		 
	
```

In the example above, I saved `newPokemon` (note the `<-` syntax since itâs a resource) to the path `/storage/MyPokemon`. Notice also that we had to provide the `SaveValue` entitlement on the `&Account` type to enable saving to the account.

Now anytime we want to access the new pokemon, we can go to that path. Letâs do that below.

cadence

```
		
			import Game from "./Game.cdc"

transaction() {
  // notice the `LoadValue` entitlement - this allows
  // us to call the `load` function
  prepare(signer: auth(LoadValue) &Account) {
    // takes `myPokemon` out of my account storage
    let myPokemon: @Game.Pokemon? <- signer.storage.load<@Game.Pokemon>(from: /storage/MyPokemon)
                        ?? panic("A Pokemon does not live here.")
    // destroys it
    destroy myPokemon
  }

  execute {}
}
		 
	
```

In the example above, we use the `.load()` function to take data OUT of our account storage.

Youâll notice that we have to do this weird thing: `<@Game.Pokemon>`. What is that? Well, when youâre interacting with account storage, you have to specify the type youâre looking at. Cadence has no idea that a `@Game.Pokemon` is stored at that storage path. But as the coder, we know that is whatâs stored there, so we have to put `<@Game.Pokemon>` to say âwe expect a `@Game.Pokemon` to come out of that storage path.â

One more important thing is that when you `load` data from storage, it returns an optional. `myPokemon` actually has type `@Game.Pokemon?`. The reason for this is because Cadence has no idea that you are telling the truth and something actually lives there, or that itâs even the right type. So if you were wrong, it will return `nil`.

### Borrow Function

Previously, we saved and loaded from our account. But what if we just want to look at something in an account and donât want to move it out of storage to read it? Thatâs where references and the `.borrow()` function comes in.

cadence

```
		
			import Game from "./Game.cdc"

transaction() {
  // notice the `BorrowValue` entitlement - this allows
  // us to call the `load` function
  prepare(signer: auth(BorrowValue) &Account) {
    let myPokemonRef = signer.storage.borrow<&Game.Pokemon>(from: /storage/MyPokemon)
                          ?? panic("A Pokemon does not live here.")
    log(myPokemonRef.xp)
  }

  execute {}
}
		 
	
```

You can see that we used the `.borrow()` function to get a reference to the resource in our storage, not the resource itself. That is why the type we use is `<&Game.Pokemon>` instead of `<@Game.Pokemon>`.

## Reading this Data in a Script

You may be wonderingâ¦ if we are storing our Pokemon in our account storage, and we need an authorized reference (like `auth(BorrowValue) &Account`) to access this dataâ¦ how will we get this inside of a script?!

It turns out itâs very easy. Scripts allow you to get authorized references to accounts using the `getAuthAccount` function:

cadence

```
		
			access(all) fun main(address: Address) {
  // `getAuthAccount` is a built-in function to Cadence
  //
  // `Storage` is an entitlement that enables save,
  // load, and borrow all in one.
  let authAccount = getAuthAccount<auth(Storage) &Account>(address)
}
		 
	
```

Using this function, we can easily get data about our Pokemon inside of our account:

cadence

```
		
			import Game from "./Game.cdc"

access(all) fun main(address: Address): PokemonResult {
  let authAccount = getAuthAccount<auth(Storage) &Account>(address)
  let myPokemonRef = authAccount.storage.borrow<&Game.Pokemon>(from: /storage/MyPokemon)
                    ?? panic("A Pokemon does not live here.")
    
  return PokemonResult(myPokemonRef.details, myPokemonRef.xp)
}

access(all) struct PokemonResult {
  access(all) let details: &Game.PokemonDetails
  access(all) let xp: Int

  init(_ details: &Game.PokemonDetails, _ xp: Int) {
    self.details = details
    self.xp = xp
  }
}
		 
	
```

In this script, we:

1. Used the `authAccount` to borrow a reference to our Pokemon
2. Defined our own `PokemonResult` struct inside of the script to better organize our result data
3. Returned a `PokemonResult`

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter3/lesson2.md)

[References](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson1)
[Access Modifiers](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson3)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)