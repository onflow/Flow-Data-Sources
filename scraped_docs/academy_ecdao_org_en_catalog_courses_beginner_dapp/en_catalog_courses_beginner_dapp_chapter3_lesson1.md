# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter3/lesson1

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

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

# Chapter 3 Lesson 1 - Our First Smart Contract

Hello beautiful people! Welcome to the glorious Chapter 3, in which we will start diving into actual Blockchain stuff. Before we do some blockchain stuff in our DApp, itâs important to give a brief (2 lesson long) introduction to Cadence.

Today, we will be learning the very basics of Cadence code by implementing our first Smart Contract. That is, how to declare a variable, how to write a function, etc.

## Our First Smart Contract

*Before going on, make sure youâve read Chapter 1, Lesson 1. That lesson covers everything you need to know about Smart Contracts up to this point.*

In order to start making our first Smart Contract, we need to figure out a place to actually put it! To do that, launch a browser of your choice (I would recommend Google Chrome), go to the Flow playground by pasting in this URL: <https://play.onflow.org.> After you do that, do the following

1. On the left hand side, click the â0x01â tab.
2. Delete everything in that page.

It should look like this:

![drawing](/courses/beginner-dapp/blanksc.png)

What we have done is clicked on the `Account` with address `0x01` and deleted the contract in its account. This brings up an important topic.

### Whatâs an address?

An address is something that looks like `0x` and then a bunch of random numbers and letters. Hereâs an example address on Flow: `0xe5a8b7f23e8b548f`. On the Flow playground, youâll see much shorter addresses like `0x01`. Thatâs just to make things simpler.

But what actually IS an address? Well, you can think of them as a user. When I want to do something on the blockchain, I need to have an account. Every account has an address associated with it. So when you see something like `0xe5a8b7f23e8b548f`, thatâs really just a personâs account that they use to store data, send transactions, etc.

### Where do smart contracts live?

Smart Contracts are deployed accounts. As we mentioned above, accounts are owned by a user, and every account has an address associated with it that always begins with `0x`.

In this case, since we are on the Flow playground, it has automatically given us 5 accounts, namely `0x01`, `0x02`, and so on. Thus, Smart Contracts live at an address. So when we deploy a contract named âHello Worldâ to account `0x01`, that is how we identify it. If we wanted to interact with it, we would have to know both the name of the contract and the address.

Weâll see this more in-depth when we import stuff later on.

### Back to our exampleâ¦

In this case, we will be deploying our Smart Contract to account `0x01`. This means account `0x01` is the **owner** of this Smart Contract. In the real world, you would deploy your Smart Contract to **your** account, but because this is a fake-simulation world, we can choose any account we want, so we chose `0x01`.

> Letâs make our contract now. In the empty space, type the following:

cadence

```
		
			pub contract HelloWorld {

    init() {

    }
}
		 
	
```

The `pub contract [contract name]` part will ALWAYS be what you type when you create a new contract. You can fill in `contract name` with whatever youâd like to call your contract.

The `init()` function is a function that every single contract MUST have. It is called when the Contract is initially deployed, which in the real world, only ever happens 1 time. So, we can initialize some stuff in it when we want to.

Okay, boom! This is your first Smart Contract, although it doesnât do anything ;( Letâs make it store a `greeting` variable so we can store some data in this contract.

Modify your contract code so it looks like this:

cadence

```
		
			pub contract HelloWorld {

    pub var greeting: String

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

In Cadence, when you declare a variable, you follow this format:

`[access modifier] [var/let] [variable name]: [type]`

Using our example aboveâ¦

* Our access modifier is `pub`, which means anyone can read this variable. In the future, we will see lots of other access modifiers, but lets stick with `pub` for the next few lessons just to make life easy.
* `let` means that this variable is a constant. If youâve coded in other programming languages, a constant means that once we make this variable equal to something, we **cannot change it**. On the other hand, `var` means we can change it.
* Our variable name is `greeting`
* The type of our variable is a `String`. This means we can put stuff like âHelloâ, âJacob is the bestâ, âI love Jacobâ, stuff like that.

Next, we put `self.greeting = "Hello, World!"` inside the `init()` function. Remember, the `init()` function is called when the contract is deployed, which only happens once. `self` is a keyword that means âthe variable that is one layer above.â In this case, `self.greeting` is referring to the `greeting` variable we declared right above it, and we set it equal to âHello, World!â

> To deploy this contract, click the green âDeployâ button.

Your page should look like this:

![drawing](/courses/beginner-dapp/helloworld.png)
> NOTE: If youâre getting errors, try first refreshing the page.

Awesome!!! Youâve deployed your first Smart Contract. Note that this is not the real blockchain, it a simulated one that only applies to you.

## Reading our Greeting

Letâs make sure that our `greeting` variable actually got set to âHello, World!â. Remember, we can view data from the Blockchain using a script.

> On the left hand side, under âScript Templatesâ, click on the tab that says âScriptâ and delete everything inside of it.

> Next, write the following code:

cadence

```
		
			import HelloWorld from 0x01

pub fun main(): String {
    return HelloWorld.greeting
}
		 
	
```

This Script will return the value of greeting, which is âHello, World!â In order to do that, letâs see what we did:

1. First, we imported our Smart Contract by doing `import HelloWorld from 0x01`. In Cadence, you import a contract by doing `import [contract name] from [address of that contract]`. Because we deployed HelloWorld to `0x01`, we wrote the above.
2. Next, we wrote a function. In Cadence, you write a function by doing `[access modifier] fun [function name](): [return type] { ... }`. In this case, we used `pub` for our access modifier (more on that later), named our function `main`, and said we will be returning a `String` type, which remember, is the type of `greeting`.
3. We then accessed the `greeting` variable from the contract using `HelloWorld.greeting`.

> If you click âExecuteâ on the right side, you will see in the terminal it prints, âHello, World!â like below:

![drawing](/courses/beginner-dapp/hwscript.png)

If yours looks like that, you have executed your first script!

## Concept Check

Okay, so we just wrote some code. That was fast. But how does all of this relate back to what I was saying in Chapter 1, Lesson 1?

Remember I said Smart Contracts are both programs and rulebooks. They allow us to do certain things, nothing more and nothing less. In this example, our Smart Contract let us initialize `greeting` and read `greeting`. Notice that it does NOT let us change `greeting` to be something else. If we had wanted to add that functionality, we wouldâve had to do it ahead of time, before we deployed it. This is why itâs so crucial that as a developer of a Smart Contract, you implement all the functionality you want a user to have before you deploy the contract. Because after you deploy, thereâs nothing you can do. (Of course, on the Flow playground, we can deploy the contract again. But in the real world you cannot do this.)

## Conclusion

Today, we learned how to deploy our first contract, declare a variable, write a function, and execute a script. Wow! Thatâs a lot. But it wasnât too bad, right?

## Quests

For todays quest, please load up a new Flow playground by going to <https://play.onflow.org> just like we did in this lesson. You will use that for writing your code.

1. Deploy a contract to account `0x03` called âJacobTuckerâ. Inside that contract, declare a **constant** variable named `is`, and make it have type `String`. Initialize it to âthe bestâ when your contract gets deployed.
2. Check that your variable `is` actually equals âthe bestâ by executing a script to read that variable. Include a screenshot of the output.

Itâs so awesome that I get to make these quests. I love this.

Anyways, please remember to store your answers in some way so I can review them if you submit them to me. Good luck!

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Video lesson](#)
[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter3/lesson1.md)

[Finishing the Skeleton](/en/catalog/courses/beginner-dapp/chapter2/lesson4)
[Transactions and Scripts](/en/catalog/courses/beginner-dapp/chapter3/lesson2)



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