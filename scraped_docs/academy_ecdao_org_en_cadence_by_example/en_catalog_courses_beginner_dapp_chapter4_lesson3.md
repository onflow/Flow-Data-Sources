# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter4/lesson3

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/beginner-dapp)

1. Basic Concepts

[1.1 Learning Blockchain Concepts](/en/catalog/courses/beginner-dapp/chapter1/lesson1)[1.2 The Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp/chapter1/lesson2)

2. Learning Web Development

[2.1 Creating our DApp](/en/catalog/courses/beginner-dapp/chapter2/lesson1)[2.2 Learning Frontend Code](/en/catalog/courses/beginner-dapp/chapter2/lesson2)[2.3 Adding Javascript Code](/en/catalog/courses/beginner-dapp/chapter2/lesson3)[2.4 Finishing the Skeleton](/en/catalog/courses/beginner-dapp/chapter2/lesson4)

3. Cadence Development

[3.1 Our First Smart Contract](/en/catalog/courses/beginner-dapp/chapter3/lesson1)[3.2 Transactions and Scripts](/en/catalog/courses/beginner-dapp/chapter3/lesson2)[3.3 Bringing Cadence to our DApp & Deploying our Contract](/en/catalog/courses/beginner-dapp/chapter3/lesson3)

4. Learn FCL

[4.1 Connecting the Blockchain](/en/catalog/courses/beginner-dapp/chapter4/lesson1)[4.2 Running a Script](/en/catalog/courses/beginner-dapp/chapter4/lesson2)[4.3 Passing in Arguments to a Script](/en/catalog/courses/beginner-dapp/chapter4/lesson3)[4.4 Finishing the Skeleton](/en/catalog/courses/beginner-dapp/chapter4/lesson4)

5. Finish & Deploy

[5.1 Finishing our DApp](/en/catalog/courses/beginner-dapp/chapter5/lesson1)[5.2 Deploying our DApp](/en/catalog/courses/beginner-dapp/chapter5/lesson2)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/beginner-dapp)
Beginner Dapp

# Chapter 4 Lesson 3 - Passing in Arguments to a Script

Yesterday we learned how to execute a script with FCL. Today, weâre going to learn how to pass in arguments to the script.

## Important Note

1. None of todayâs material will involve changing our Emerald DApp. This is a standalone lesson to help you understand arguments.
2. All of what you learn today is **the exact same for transactions**. We will be using transactions tomorrow ;)

## Quick Overview of Yesterday

Yesterday, we made executed a script using FCL like this:

javascript

```
		
			async function executeScript() {
	const response = await fcl.query({
		cadence: `
    import HelloWorld from 0x90250c4359cebac7 // THIS WAS MY ADDRESS, USE YOURS

    pub fun main(): String {
        return HelloWorld.greeting
    }
    `,
		args: (arg, t) => [] // ARGUMENTS GO IN HERE
	});

	console.log('Response from our script: ' + response);
}
		 
	
```

But one missing piece was the `args` property. Why didnât we put anything there? Well, our Cadence code didnât take any arguments. If you look at the Cadence codeâ¦

cadence

```
		
			pub fun main(): String
		 
	
```

â¦youâll see it doesnât take any arguments. But what if we had a Cadence script like this?

cadence

```
		
			pub fun main(a: Int, b: Int): Int {
  // Example:
  // a = 2
  // b = 3
  // result = 5
  return a + b
}
		 
	
```

Or something like this?

cadence

```
		
			pub fun main(greeting: String, person: String): String {
  // Example:
  // greeting = "Hello"
  // person = "Jacob"
  // result = "Hello, Jacob!"
  return greeting.concat(", ").concat(person).concat("!")
}
		 
	
```

Now we need to pass in arguments.

## Passing in Arguments Using FCL

Here is an example of passing in arguments, and then we will explainâ¦

javascript

```
		
			async function executeScript() {
	const response = await fcl.query({
		cadence: `
    pub fun main(a: Int, b: Int): Int {
      // Example:
      // a = 2
      // b = 3
      // result = 5
      return a + b
    }
    `,
		args: (arg, t) => [arg('2', t.Int), arg('3', t.Int)]
	});
}
		 
	
```

Now, thereâs a few things we should talk about to help you understand:

1. All the arguments go inside the `[]`.
2. You create a new argument with the `arg` keyword
3. You put the value of the argument first (ex. `"2"`)
4. You put the Cadence type of the value 2nd using `t` (ex. `t.Int`)

You may be wondering, why are our Integers represented as strings? The answer is, I have no idea. The FCL team just wanted it like that.

### Different Types

Letâs look at another example using tons of different types:

javascript

```
		
			async function executeScript() {
	const response = await fcl.query({
		cadence: `
    pub fun main(
      a: Int, 
      b: String, 
      c: UFix64, 
      d: Address, 
      e: Bool,
      f: String?,
      g: [Int],
      h: {String: Address}
    ) {
      // Example:
      // a = 2
      // b = "Jacob is so cool"
      // c = 5.0
      // d = 0x6c0d53c676256e8c
      // e = true
      // f = nil
      // g = [1, 2, 3]
      // h = {"FLOAT": 0x2d4c3caffbeab845, "EmeraldID": 0x39e42c67cc851cfb}

      // something happens here... but it doesn't matter
    }
    `,
		args: (arg, t) => [
			arg('2', t.Int),
			arg('Jacob is so cool', t.String),
			arg('5.0', t.UFix64),
			arg('0x6c0d53c676256e8c', t.Address),
			arg(true, t.Bool),
			arg(null, t.Optional(t.String)),
			arg([1, 2, 3], t.Array(t.Int)),
			arg(
				[
					{ key: 'FLOAT', value: '0x2d4c3caffbeab845' },
					{ key: 'EmeraldID', value: '0x39e42c67cc851cfb' }
				],
				t.Dictionary({ key: t.String, value: t.Address })
			)
		]
	});
}
		 
	
```

Hopefully this helps you understand the different types of arguments you can pass in :)

## Conclusion

Thatâs it! Not so bad, right?

## Quests

I only have one quest for you today, and itâs almost exactly what we reviewed already :)

1. Write a function that executes a script with all the Cadence types that we reviewed today. Call the script when the page refreshes. Return something random from the Cadence script, and console log it to prove to me your script actually worked.

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Video lesson](#)
[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter4/lesson3.md)

[Running a Script](/en/catalog/courses/beginner-dapp/chapter4/lesson2)
[Finishing the Skeleton](/en/catalog/courses/beginner-dapp/chapter4/lesson4)



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