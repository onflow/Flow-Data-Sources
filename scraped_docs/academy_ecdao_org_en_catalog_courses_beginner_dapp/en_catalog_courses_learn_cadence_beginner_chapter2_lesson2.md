# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter2/lesson2

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

# Chapter 2 Lesson 2 - Resources

Uh oh. Weâre on the most important topic in all of Cadence: Resources. Seriously, this is the most important thing youâll learn from me. Letâs get into it!

## Pokemon

Iâm going to be using [Pokemon](https://sg.portal-pokemon.com/about/) in the lesson today.

If you donât know what that is (we canât be friends if you donât), itâs basically a video game where you catch & collect little creatures and make them your friends. You can fight with them as well and level them up to make them stronger.

Weâre going to be making our own Pokemon and leveling them up for fun to demonstrate resources!

![](https://i.imgur.com/BMy7XNT.png)

## Resources

What is a resource? Itâs always helpful to look at code, so letâs do that first:

cadence

```
		
			access(all) resource Pokemon {
    access(all) let name: String

    init() {
        self.name = "Pikachu"
    }
}
		 
	
```

Doesnât this look very similar to a Struct? In code, they do actually look pretty similar. Here, the resource `Pokemon` is a container that stores a name, which is a `String` type. But there are many, many differences behind the scenes.

### Resources vs. Structs

In Cadence, structs are merely containers of data. You can copy them, overwrite them, and create them whenever you want. All of these things are completely false for resources. Here are some important facts that define resources:

1. They cannot be copied
2. They cannot be lost (or overwritten)
3. They cannot be created whenever you want
4. You must be extremely explicit about how you handle a resource (for example, moving them)

Letâs look at some code below to figure out resources:

cadence

```
		
			access(all) contract Game {

    // PokemonDetails
    // Description: Holds all of the static details
    // of the Pokemon. Useful as an easy container.
    access(all) struct PokemonDetails {
        access(all) let name: String
        access(all) let dateCreated: UFix64
        // fire, water, electric...
        access(all) let type: String

        init(name: String, dateCreated: UFix64, type: String) {
            self.name = name
            self.dateCreated = dateCreated
            self.type = type
        }
    }

    // Pokemon
    // Description: The actual Pokemon asset that will
    // get stored by the user and upgraded over time.
    access(all) resource Pokemon {
        access(all) let details: PokemonDetails
        access(all) var xp: Int

        init(name: String, type: String) {
            // gets the timestamp of the current block (in unix seconds)
            let currentTime: UFix64 = getCurrentBlock().timestamp
            self.details = PokemonDetails(
                name: name, 
                dateCreated: currentTime,
                type: type
            )
            self.xp = 0
        }
    }

    // createPokemon
    // Description: Creates a new Pokemon using a name and type and returns
    // it back to the caller.
    // Returns: A new pokemon resource.
    access(all) fun createPokemon(name: String, type: String): @Pokemon {
        let newPokemon <- create Pokemon(name: name, type: type)
        return <- newPokemon
    }
}
		 
	
```

Couple of important things to note:

* Resources in Cadence use the `@` symbol in front of their type to say, âthis is a resource.â For example: `@Pokemon`.
* You can only make a new resource with the `create` keyword. The `create` keyword can only ever be used inside the contract. This means you, as the developer, can control when they are made. This is not true for structs, since structs can be created outside the contract in structs and transactions.
* To move resources around you must use the `<-` âmoveâ operator. In Cadence, you cannot simply use the `=` to put a resource somewhere. You MUST use the `<-` âmove operatorâ to explicity âmoveâ the resource around.
* You use the `destroy` keyword to destroy a resource (we will see this later)

**In short, structs should merely be used as containers of data, while resources are more secure digital assets or objects.** You will soon see why this is the case as we continue with this example throughout the course.

## Creating a new Pokemon

Now that we have a super cool smart contract, we should write a transaction to actually create a new Pokemon!

Make sure to deploy the Game contract to your local emulator before running this transaction.

cadence

```
		
			import Game from "./Game.cdc"

transaction(name: String, type: String) {
    prepare(signer: &Account) {

    }

    execute {
        let newPokemon <- Game.createPokemon(name: name, type: type)
        log(newPokemon.details)
        destroy newPokemon // destroys the resource
    }
}
		 
	
```

Come up with your own name for a pokemon and a type (water, fire, electric, or whatever you want!) and run the transaction in your terminal. You should see that it logs the pokemons details.

## Conclusion

Hey, you made it! In todayâs lesson, you learned what resources are and how they differ from structs. We created a new Pokemon resource inside of a transaction and destroyed it as well.

That wasnât so bad right? I think youâre all gonna do just fine. Letâs end things there for today, and tomorrow, Iâll make it impossible for you. Just kiddinâ ;)

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter2/lesson2.md)

[Basic Structs](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson1)
[Contract State](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson3)



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