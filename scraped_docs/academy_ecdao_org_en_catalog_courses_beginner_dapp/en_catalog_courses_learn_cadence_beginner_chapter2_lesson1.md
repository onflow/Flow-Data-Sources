# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter2/lesson1

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

# Chapter 2 Lesson 1 - Basic Structs

Hello peoples. Today is your lesson to learn Structs! The good news is structs are pretty simple to learn, so today wonât be too long. Woooohoooo! Letâs get into it.

## Structs

What are structs? Structs are containers of other types. Letâs look at an example:

cadence

```
		
			access(all) struct ArtPiece {
    access(all) let id: Int
    access(all) let name: String
    access(all) let artLink: String
    access(all) let hoursWorkedOn: Int

    // `init()` gets called when this Struct is created...
    // You have to provide 4 arguments when creating this Struct.
    init(id: Int, name: String, artLink: String, hoursWorkedOn: Int) {
        self.name = name
        self.artLink = artLink
        self.description = description
        self.hoursWorkedOn = hoursWorkedOn
    }
}
		 
	
```

Okay, thereâs a lot going on there. What happened? Basically, we defined a new Type named `ArtPiece`. It is a Struct. As you can see, it contains 4 pieces of data:

1. an âidâ (`id`)
2. a name (`name`)
3. a link to the art (`artLink`)
4. the amount of hours it took to make (`hoursWorkedOn`)

It is really helpful to make a Struct when we want information to be gathered together in a container.

Notice that Structs have the `init()` function that gets called when the Struct gets created, much like the `init()` function that gets called when the contract is deployed.

## Real Example

Letâs start off by actually deploying a new smart contract.

Create a new file called `Art.cdc` and add it to your `flow.json` file by making a new entry under the âcontractsâ object just like you did for `HelloWorld` earlier in the course. Then, paste the following code in your new `Art.cdc` file:

cadence

```
		
			access(all) contract Art {

    // this will act as an 'id' for
    // new art pieces
    access(all) var totalArtPieces: Int
    access(all) var artPieces: {Int: ArtPiece}

    access(all) struct ArtPiece {
        access(all) let id: Int
        access(all) let name: String
        access(all) let artLink: String
        access(all) let hoursWorkedOn: Int

        init(id: Int, name: String, artLink: String, hoursWorkedOn: Int) {
            self.id = id
            self.name = name
            self.artLink = artLink
            self.hoursWorkedOn = hoursWorkedOn
        }
    }

    access(all) fun uploadArt(name: String, artLink: String, hoursWorkedOn: Int) {
        let id: Int = Art.totalArtPieces
        let newArtPiece = ArtPiece(id: id, name: name, artLink: artLink, hoursWorkedOn: hoursWorkedOn)
        // store the new art piece, mapped to its `id`
        self.artPieces[id] = newArtPiece
        // increment the amount of art pieces by one
        Art.totalArtPieces = Art.totalArtPieces + 1
    }

    init() {
        self.totalArtPieces = 0
        self.artPieces = {}
    }
}
		 
	
```

I threw a lot at you here. But you actually know all of it now! We can break it down:

1. We defined a new contract named `Art`
2. We defined a dictionary named `artPieces` that maps an âidâ to an `ArtPiece` struct with that âidâ
3. We defined a new Struct called `ArtPiece` that contains 4 fields
4. We defined a new function named `uploadArt` that takes in 4 arguments and creates & stores a new `ArtPiece` with them. It then creates a new mapping from `id` -> the `ArtPiece` associated with that âidâ

If you can understand these things, youâve made significant progress. If youâre struggling with this a bit, no worries! I would maybe review some of the concepts from the past few lessons.

Make sure to also add the Art contract to your `flow.json` file and deploy it just like we did for HelloWorld in the previous chapter.

### Upload Art

Now that weâve defined a new Struct, letâs see why it can be helpful.

Letâs create a new transaction and copy and paste this boilerplate transaction code:

cadence

```
		
			import Art from "./Art.cdc"

transaction() {

    prepare(signer: &Account) {}

    execute {
        log("We're done.")
    }
}
		 
	
```

Cool! Now, we want to add a new art piece to the `artPieces` dictionary in the `Art` contract. How can we do this? Well, letâs call the `uploadArt` function with all the arguments we need like so:

cadence

```
		
			Art.uploadArt(name: name, artLink: artLink, hoursWorkedOn: hoursWorkedOn)
		 
	
```

But wait, we need to get these arguments from somewhere first! We can do that by providing them to the transaction as arguments, like so:

cadence

```
		
			import Art from "./Art.cdc"

transaction(name: String, artLink: String, hoursWorkedOn: Int) {

    prepare(signer: &Account) {}

    execute {
        Art.uploadArt(name: name, artLink: artLink, hoursWorkedOn: hoursWorkedOn)
        log("We're done.")
    }
}
		 
	
```

Bam! Letâs run this transaction with some test data by pasting the following into our terminal:

bash

```
		
			flow transactions send ./upload_art.cdc "Jacob" "https://i.imgur.com/mdDB58Z.png" 10
		 
	
```

### Read our Art Piece

To read our new Art Piece, letâs create a script and copy and paste the boilerplate script code:

cadence

```
		
			import Art from "./Art.cdc"

access(all) fun main() {

}
		 
	
```

Now, letâs try to read our stored art piece. Our goal is to go into the dictionary that stores all of the art pieces and return a specific one back. We can do this by providing the `id` of the art piece we want since we mapped `id` -> `ArtPiece` in our `artPieces` dictionary. We can then return the `ArtPiece` type we get from that dictionary, like so:

cadence

```
		
			import Art from "./Art.cdc"

access(all) fun main(id: Int): Art.ArtPiece? {
    return Art.artPieces[id]
}
		 
	
```

But wait! How do we know which `id` to provide?

Letâs create another script to fetch all of the ids of the art pieces stored in the contract:

cadence

```
		
			import Art from "./Art.cdc"

access(all) fun main(): [Int] {
    return Art.artPieces.keys
}
		 
	
```

When you run this script, you will get back a list of ids (depending on how many you made) that are stored in the `artPieces` dictionary. Pick one id and run the following script that fetches a specific art piece, providing the id to it:

cadence

```
		
			import Art from "./Art.cdc"

access(all) fun main(id: Int): Art.ArtPiece? {
    return Art.artPieces[id]
}
		 
	
```

Note the return type here: `Art.ArtPiece?`. Types are always based on the contract they are defined in. And, itâs an optional because we are accessing a dictionary.

Boom! Thatâs it. Now, whoever called this script can have all the art information they need. Sweet, Structs are awesome!

## Conclusion

In todayâs lesson, we learned how to make our own type by creating a struct. Structs are really useful for gathering data into one object.

Thatâs all! See you tomorrow folks ;)

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter2/lesson1.md)

[Types](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson3)
[Resources](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson2)



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