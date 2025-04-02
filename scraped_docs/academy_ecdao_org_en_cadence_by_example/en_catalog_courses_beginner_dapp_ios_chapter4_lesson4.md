# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter4/lesson4

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/beginner-dapp-ios)

1. Basic Concepts

[1.1 Understanding Blockchain Concepts](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson1)[1.2 Exploring the Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson2)

2. Learning Swift (iOS) Development

[2.1 Creating our Mobile (iOS) DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson1)[2.2 Learning Frontend Code](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson2)[2.3 Adding Interactivity To Our DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson3)[2.4 Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson4)

3. Cadence Development

[3.1 Our First Smart Contract](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson1)[3.2 Transactions and Scripts](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson2)[3.3 Bringing Cadence to our DApp & Deploying our Contract](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson3)

4. Learn FCL

[4.1 Connecting the Blockchain](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson1)[4.2 Integrating WalletConnect and Lilco Wallet](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson2)[4.3 Running a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson3)[4.4 Passing in Arguments to a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson4)[4.5 Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson5)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/beginner-dapp-ios)
Beginner Dapp Ios

# Chapter 4 Lesson 4 - Passing in Arguments to a Script

In the last lesson, we learned how to execute a script with FCL. Today, weâre going to learn how to pass arguments to the script.

## Important Note

1. None of todayâs material will involve changing our Emerald DApp. This is a standalone lesson to help you understand arguments.
2. **Take Notes** - All of what you learn today is **the exact same for transactions**. We will be using transactions tomorrow ;)

## Quick Overview of Yesterday

Yesterday, we made executed a script using FCL like this:

swift

```
		
			func getGreeting() async {
    do {
        let result = try await fcl.query(script: """
            import HelloWorld from 0xDeployer

            pub fun main(): String {
              return HelloWorld.greeting
            }
        """).decode(String.self)

        await MainActor.run {
            greetingDisplay = result
        }
    } catch {
        print(error)
    }
}
		 
	
```

But when typing in `fcl.query` in might have noticed Xcodeâs code completion showing an `arg` parameter.

![](https://i.imgur.com/ybGdnlS.png)

Why didnât we use that one? Well, our Cadence code didnât take any arguments. If you look at the Cadence codeâ¦

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

swift

```
		
			let result2 = try await fcl.query(script: """
    pub fun main(a: Int, b: Int): Int {
      // Example:
      // a = 2
      // b = 3
      // result = 5
      return a + b
    }
""", args: [.int(2), .int(3)])
		 
	
```

Now, there are a few things we should talk about to help you understand:

1. The args parameter accepts an array of Cadence values, so naturally, all args go inside the `[]`.
2. To create a new argument type a `.` then select the proper type from the code completion drop down.
3. Place the value of the argument inside the parathesis.

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

Hopefully, this helps you understand the different types of arguments you can pass in :)

## Conclusion

Thatâs it! Not so bad, right?

## Quests

I only have one quest for you today, and itâs almost exactly what we reviewed already :)

1. Write a function that executes a script with all the Cadence types that we reviewed today. Call the script when the page refreshes. Return something random from the Cadence script, and print it to prove to your script actually worked.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter4/lesson4.md)

[Running a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson3)
[Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson5)



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