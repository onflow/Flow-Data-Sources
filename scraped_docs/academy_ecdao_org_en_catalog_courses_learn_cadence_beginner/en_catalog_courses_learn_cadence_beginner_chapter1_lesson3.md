# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter1/lesson3





















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

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

# Chapter 1 Lesson 3 - Types

Whatsup! Today, we will be learning some of the most important types that you will use in nearly every contract you write.

## Types

To start playing around with types, letâs create a new file called `test.cdc`. Weâre not going to write any smart contracts today :)

In Cadence, the code you write can often infer what type something is. For example, if you write:

cadence
```
		
			var jacob = "isCool"
		 
	
```

Cadence will automatically realize you have initialized a String. However, if we want to be more explicit about our types, we can include the type in the declaration, like so:

cadence
```
		
			var jacob: String = "isCool"
		 
	
```

Itâs often helpful to include the type of something so we can reason about where we went wrong in our programs. Cadence will also tell you straight up that youâve made a mistake if you intended a variable to be of different type. For example, try typing:

cadence
```
		
			var jacob: String = 3
		 
	
```

Cadence will say âHey! These types donât match.â Or something like that. But the point is we can include types to help us understand where we went wrong.

## Common Types

cadence
```
		
			var number: Int = 2
var address: Address = 0x01
var text: String = "Hey!"
		 
	
```
## Arrays

An array is a list of elements. Letâs look at a very basic array in Cadence:

cadence
```
		
			var people: [String] = ["Jacob", "Alice", "Damian"]
		 
	
```

This is a list of Strings. We declare an array type like so: `[Type]`. Letâs do another example. If we wanted a list of addresses, well, itâs very similar:

cadence
```
		
			var addresses: [Address] = [0x1, 0x2, 0x3]
		 
	
```

We can also index into arrays to see what the elements are. This is exactly like Javascript or similar languages.

cadence
```
		
			var addresses: [Address] = [0x1, 0x2, 0x3]
log(addresses[0]) // 0x1
log(addresses[1]) // 0x2
log(addresses[2]) // 0x3
		 
	
```
### Helpful Array Functions that I Use All the Time

The things we looked at above are all fixed arrays. We can also do some cool things with arrays, and Iâll list some of them here.

**append(\_ element: Type)**

(note the argument label `element` has a `_`  in front of it, which means it is implicit, so you donât have to put the argument label when you call the function. So instead of `.append(element: value)`, you can just do `.append(value)`)

Adds an element to the end of the array.

ex.

cadence
```
		
			var people: [String] = ["Jacob", "Alice", "Damian"]
people.append("Ochako Unaraka") // anyone watch My Hero Academia? :D
log(people) // ["Jacob", "Alice", "Damian", "Ochako Unaraka"]
		 
	
```

**contains(*element*: Type): Bool**

Checks to see if an array contains an element.

ex.

cadence
```
		
			var people: [String] = ["Jacob", "Alice", "Damian"]
log(people.contains("Jacob")) // true
log(people.contains("Poop")) // false
		 
	
```

**remove(at: Int)**

Removes an element at the given index (index starts from 0, meaning the first element has index 0)

ex.

cadence
```
		
			var people: [String] = ["Jacob", "Alice", "Damian"]
people.remove(at: 1)
log(people) // ["Jacob", "Damian"]
		 
	
```

**length**

Returns the length of the array.

ex.

cadence
```
		
			var people: [String] = ["Jacob", "Alice", "Damian"]
log(people.length) // 3
		 
	
```
## Dictionaries

Nice! Thatâs arrays for ya. Time for dictionaries. Well, what is this thing?! A dictionary is something that maps a `key` to a `value`. Letâs look at a simple example below.

cadence
```
		
			var names: {String: String} = {"Jacob": "Tucker", "Bob": "Vance", "Ochako": "Unaraka"} // anyone watch The Office?
		 
	
```

In the above example, we mapped `String`s to `String`s. More specifically, we mapped someoneâs first name to their last name. We did this with the dictionary type, which is `{Type: Type}`. We can use this dictionary to get peoplesâ last names like so:

cadence
```
		
			var names: {String: String} = {"Jacob": "Tucker", "Bob": "Vance", "Ochako": "Unaraka"}
log(names["Jacob"]) // "Tucker"
log(names["Bob"]) // "Vance"
log(names["Ochako"]) // "Unaraka"
		 
	
```

Letâs look at an example of mapping `String`s to `Int`s. Weâll map someoneâs name to their favourite number.

cadence
```
		
			var favouriteNums: {String: Int} = {"Jacob": 13, "Bob": 0, "Ochako": 1000100103}
log(favouriteNums["Jacob"]) // 13
		 
	
```

This is cool. But thereâs more. We will get into why dictionaries are more complicated in the Dictionaries and Optionals section at the bottom. For now, letâs look at some helpful functions.

### Helpful Dictionary Functions that I Use All the Time

**insert(key: Type, \_ value: Type)**

(note the `value` argument label is implicit, but the `key` is not)

ex.

cadence
```
		
			var favouriteNums: {String: Int} = {"Jacob": 13, "Bob": 0, "Ochako": 1000100103}
favouriteNums.insert(key: "Justin Bieber", 1)
log(favouriteNums) // {"Jacob": 13, "Bob": 0, "Ochako": 1000100103, "Justin Bieber": 1}
		 
	
```

**remove(key: Type): Type?**

Removes the `key` and the value associated with it, and returns that value.

ex.

cadence
```
		
			var favouriteNums: {String: Int} = {"Jacob": 13, "Bob": 0, "Ochako": 1000100103}
let removedNumber = favouriteNums.remove(key: "Jacob")
log(favouriteNums) // {"Bob": 0, "Ochako": 1000100103}
log(removedNumber) // 13
		 
	
```

**keys: [Type]**

Returns an array of all the keys in the dictionary.

ex.

cadence
```
		
			var favouriteNums: {String: Int} = {"Jacob": 13, "Bob": 0, "Ochako": 1000100103}
log(favouriteNums.keys) // ["Jacob", "Bob", "Ochako"]
		 
	
```

**values: [Type]**

Returns an array of all the values in the dictionary.

ex.

cadence
```
		
			var favouriteNums: {String: Int} = {"Jacob": 13, "Bob": 0, "Ochako": 1000100103}
log(favouriteNums.values) // [13, 0, 1000100103]
		 
	
```
## Optionals

Okay, so now weâre on optionals. Crap. Optionals are SO important, but can be tricky. You will probably encounter optionals in everything you do in Cadence. Most of the time, it will be because of dictionaries.

An `optional type` in Cadence is represented with a `?`. It means: âIt is either the type itâs saying, or `nil`â. Letâs take a look:

cadence
```
		
			var name: String? = "Jacob"
		 
	
```

Notice the `?` after the `String`. That means: âthe variable `name` is either a `String`, or it is `nil`.â Obviously, we know itâs a `String` because itâs equal to âJacobâ. But we can also have something like this:

cadence
```
		
			var name: String? = nil
		 
	
```

This wonât have any compile errors, because itâs correct. A `String?` type can be `nil`.

Not too bad right? Man, Iâm the best teacher ever. Youâre all so lucky to have me here.

### Force-Unwrap Operator

This gets us into the force-unwrap operator, `!`. This operator âunwrapsâ an optional type by saying: âIf this thing is nil, PANIC! If itâs not nil, weâre fine, but get rid of the optional type.â Well what the heck does THIS mean!? Letâs look:

cadence
```
		
			var name1: String? = "Jacob"
var unwrappedName1: String = name1! // Notice it removes the optional type

var name2: String? = nil
var unwrappedName2: String = name2! // PANICS! The entire program will abort because it found a problem. It tried to unwrap a nil, which isn't allowed
		 
	
```
## Optionals and Dictionaries

Alright so this is where we will combine everything we know to talk about Optionals and Dictionaries. Before, when I explained dictionaries, I left out a key (no pun intended) piece of information: When you access elements of a dictionary, it returns the value as an **optional**.

Letâs make a new script that looks like this:

cadence
```
		
			access(all) fun main(): Int {
    let thing: {String: Int} = {"Hi": 1, "Bonjour": 2, "Hola": 3}
    return thing["Bonjour"] // ERROR: "Mismatched types. expected `Int`, got `Int?`"
}
		 
	
```

This will give us an ERROR! The error says: âMismatched types. expected `Int`, got `Int?`â. Well, we know what `Int?` means now! It means it is an optional, so it may be `Int` or it may be `nil`. In order to fix this error, we have to use the force-unwrap operator `!` like so:

cadence
```
		
			access(all) fun main(): Int {
    let thing: {String: Int} = {"Hi": 1, "Bonjour": 2, "Hola": 3}
    return thing["Bonjour"]! // we added the force-unwrap operator
}
		 
	
```

Now, there are no errors :D

### Returning Optionals vs. Unwrapping

You may be asking, âis there ever a case where I want to return an optional instead of force-unwrapping the optional? The answer is yes. In fact, most times, it is preferred to return an optional instead of unwrapping. For example, looking at this code:

cadence
```
		
			access(all) fun main(): Int {
    let thing: {String: Int} = {"Hi": 1, "Bonjour": 2, "Hola": 3}
    return thing["Bonjour"]! // we are force-unwrapping the optional
}
		 
	
```

â¦ this will `panic` and abort the program if there is no value at the âBonjourâ key. Instead, we can write the code like this:

cadence
```
		
			access(all) fun main(): Int? { // notice the return value is an optional type
    let thing: {String: Int} = {"Hi": 1, "Bonjour": 2, "Hola": 3}
    return thing["Bonjour"] // we leave the optional
}
		 
	
```

This way, the client/caller can handle the case where the return value is `nil`, instead of having to worry about errors in the program. This same logic applies for other functions in your Cadence code as well.

## Conclusion

In todayâs lesson, we learned the basic types in Cadence. We will be using all of these throughout the next 2 chapters, so you will get quite familiar with them. Great work!


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter1/lesson3.md)


[Transactions and Scripts](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson2)
[Basic Structs](/en/catalog/courses/learn-cadence-beginner/chapter2/lesson1)

[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow


##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)
##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)
##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)
[Join the community](https://discord.gg/emerald-city-906264258189332541)



