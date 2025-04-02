# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter3/lesson1

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

# Chapter 3 Lesson 1 - References

Hey there Flow people. Today, weâll be talking about references, another important part of the Cadence programming language.

## What is a Reference?

In simplest terms, a reference is a way for you to interact with a piece of data without actually having to have that piece of data. Right off the bat, you can imagine how helpful this will be for resources. Imagine a world where you donât have to move a resource 1,000 times just to look at or update its fields. Ahh, that world does exist! References are here to save us.

## Pokemon Contract

Letâs take a look at our contract from Chapter 2:

cadence

```
		
			access(all) contract Game {

    access(all) var totalPokemonCreated: Int
    access(all) let storedPokemon: @{UInt64: Pokemon}

    access(all) struct PokemonDetails {
        access(all) let id: UInt64
        access(all) let name: String
        access(all) let dateCreated: UFix64
        access(all) let type: String

        init(id: UInt64, name: String, dateCreated: UFix64, type: String) {
            self.id = id
            self.name = name
            self.dateCreated = dateCreated
            self.type = type
        }
    }

    access(all) resource Pokemon {
        access(all) let details: PokemonDetails
        access(all) var xp: Int

        init(name: String, type: String) {
            let currentTime: UFix64 = getCurrentBlock().timestamp
            self.details = PokemonDetails(
                id: self.uuid,
                name: name,
                dateCreated: currentTime,
                type: type
            )
            self.xp = 0

            Game.totalPokemonCreated = Game.totalPokemonCreated + 1
        }
    }

    access(all) fun createPokemon(name: String, type: String): @Pokemon {
        let newPokemon <- create Pokemon(name: name, type: type)
        return <- newPokemon
    }

    access(all) fun storePokemon(pokemon: @Pokemon) {
        self.storedPokemon[pokemon.details.id] <-! pokemon
    }

    access(all) fun getIDs(): [UInt64] {
        return self.storedPokemon.keys
    }

    access(all) fun getPokemonDetails(id: UInt64): PokemonDetails? {
        return self.storedPokemon[id]?.details
    }

    init() {
        self.totalPokemonCreated = 0
        self.storedPokemon <- {}
    }
}
		 
	
```

### Add Battling

To spice things up, lets add a `levelUp` function to our `Pokemon` resource that adds some `xp`:

cadence

```
		
			access(all) resource Pokemon {
    access(all) let details: PokemonDetails
    access(all) var xp: Int

    access(all) fun levelUp() {
        self.xp = self.xp + 1
    }

    init(name: String, type: String) {
        let currentTime: UFix64 = getCurrentBlock().timestamp
        self.details = PokemonDetails(
            id: self.uuid,
            name: name,
            dateCreated: currentTime,
            type: type
        )
        self.xp = 0

        Game.totalPokemonCreated = Game.totalPokemonCreated + 1
    }
}
		 
	
```

To make things fun, we should also add a function that makes two Pokemon battle. It will level up whoever the winner is, based on a random number:

cadence

```
		
			access(all) fun battle(pokemonId1: UInt64, pokemonId2: UInt64) {
    // equals either 1 or 2
    let randomNumber: UInt64 = self.getRandom(min: 1, max: 2)
    // if the random number is 1, use `pokemonId1`. Otherwise use `pokemonId2`
    let winnerPokemonId = randomNumber == 1 ? pokemonId1 : pokemonId2

    // move the Pokemon resource out of `storedPokemon`
    let pokemon <- self.storedPokemon.remove(key: winnerPokemonId)
                    ?? panic("Pokemon does not exist.")
    // level it up
    pokemon.levelUp()
    // move the resource back into the dictionary
    self.storedPokemon[winnerPokemonId] <-! pokemon
}

// gets a number [min, max]
access(all) fun getRandom(min: UInt64, max: UInt64): UInt64 {
    // revertibleRandom is a built-in random function to Cadence!
    let randomNumber: UInt64 = revertibleRandom<UInt64>()
    return (randomNumber % (max + 1 - min)) + min
}
		 
	
```

You can see that in order to level up the winner of `battle`, we had to move the Pokemon resource out of storage first, level it up, and then move it back in.

### References in Cadence

Instead, letâs just use references to keep the Pokemon in `storedPokemon`, but be able to call `levelUp` anyway!

cadence

```
		
			access(all) fun battle(pokemonId1: UInt64, pokemonId2: UInt64) {
    let randomNumber: UInt64 = self.getRandom(min: 1, max: 2)
    let winnerPokemonId = randomNumber == 1 ? pokemonId1 : pokemonId2

    // get a reference to the Pokemon
    let pokemonRef: &Pokemon = (&self.storedPokemon[winnerPokemonId] as &Pokemon?)
                    ?? panic("Pokemon does not exist.")
    // level it up
    pokemonRef.levelUp()
}

// gets a number [min, max]
access(all) fun getRandom(min: UInt64, max: UInt64): UInt64 {
    // revertibleRandom is a built-in random function to Cadence!
    let randomNumber: UInt64 = revertibleRandom<UInt64>()
    return (randomNumber % (max + 1 - min)) + min
}
		 
	
```

Notice that if we had forgotten the `as &Pokemon?`, Cadence would yell at us and say âexpected casting expression.â This is because in Cadence, **you have to type cast when getting a reference**. Type casting is when you tell Cadence what type youâre getting the reference as. Itâs saying âget this optional reference that is a &Pokemon reference.â

### Running a Transaction to Test our Contract

Our final contract should look like this:

cadence

```
		
			access(all) contract Game {

    access(all) var totalPokemonCreated: Int
    access(all) let storedPokemon: @{UInt64: Pokemon}

    access(all) struct PokemonDetails {
        access(all) let id: UInt64
        access(all) let name: String
        access(all) let dateCreated: UFix64
        access(all) let type: String

        init(id: UInt64, name: String, dateCreated: UFix64, type: String) {
            self.id = id
            self.name = name
            self.dateCreated = dateCreated
            self.type = type
        }
    }

    access(all) resource Pokemon {
        access(all) let details: PokemonDetails
        access(all) var xp: Int

        access(all) fun levelUp() {
            self.xp = self.xp + 1
        }

        init(name: String, type: String) {
            let currentTime: UFix64 = getCurrentBlock().timestamp
            self.details = PokemonDetails(
                id: self.uuid,
                name: name,
                dateCreated: currentTime,
                type: type
            )
            self.xp = 0

            Game.totalPokemonCreated = Game.totalPokemonCreated + 1
        }
    }

    access(all) fun createPokemon(name: String, type: String): @Pokemon {
        let newPokemon <- create Pokemon(name: name, type: type)
        return <- newPokemon
    }

    access(all) fun storePokemon(pokemon: @Pokemon) {
        self.storedPokemon[pokemon.details.id] <-! pokemon
    }

    access(all) fun getIDs(): [UInt64] {
        return self.storedPokemon.keys
    }

    access(all) fun getPokemonDetails(id: UInt64): PokemonDetails? {
        return self.storedPokemon[id]?.details
    }

    access(all) fun battle(pokemonId1: UInt64, pokemonId2: UInt64) {
        let randomNumber: UInt64 = self.getRandom(min: 1, max: 2)
        let winnerPokemonId = randomNumber == 1 ? pokemonId1 : pokemonId2

        let pokemonRef: &Pokemon = (&self.storedPokemon[winnerPokemonId] as &Pokemon?)
                        ?? panic("Pokemon does not exist.")
        pokemonRef.levelUp()
    }

    access(all) fun getRandom(min: UInt64, max: UInt64): UInt64 {
        let randomNumber: UInt64 = revertibleRandom<UInt64>()
        return (randomNumber % (max + 1 - min)) + min
    }

    init() {
        self.totalPokemonCreated = 0
        self.storedPokemon <- {}
    }
}
		 
	
```

This is the transaction we would use to actually make two Pokemon battle:

cadence

```
		
			import Game from "./Game.cdc"

transaction(pokemonId1: UInt64, pokemonId2: UInt64) {
    prepare(signer: &Account) {}

    execute {
        Game.battle(pokemonId1: pokemonId1, pokemonId2: pokemonId2)
    }
}
		 
	
```

Isnât that so simple? Easy peasy.

## Conclusion

References arenât so bad right? The main two points are:

1. You can use references to get information without moving resources around.
2. You MUST âtype castâ a reference when getting it, or youâll receive an error.

References are not going to go away, though. They will be very important when we talk about account storage in the next chapter.

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter3/lesson1.md)

[Contract State](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson3)
[Account Storage](/en/catalog/courses/learn-cadence-beginner/chapter3/lesson2)



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