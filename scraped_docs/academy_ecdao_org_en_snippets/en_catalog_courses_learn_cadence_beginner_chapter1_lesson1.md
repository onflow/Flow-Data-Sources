# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter1/lesson1

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

# Chapter 1 Lesson 1 - Our First Smart Contract

Hello and welcome to the first lesson of the Learn Cadence (Beginner) course. Jacob here ð. Letâs just dive right into this because introductions are so boring.

## Video

If you enjoy learning in video format, this video covers everything in this lesson.

It is also very helpful if you have never coded before. It will walk you through setting up everything you need to start your coding career.

How to write smart contracts for people who have never coded before.

## Quick Note

Cadence is a smart contract language.

Put simply, smart contracts are:

* programs that you **deploy** (put) onto this weird thing called the âblockchainâ
* they contain data and functions to modify that data
* you can execute **transactions** to call the functions that modify data or make something happen. Transactions are executed when some sort of account signs it (*so smart contracts require someone/something to send a transaction for anything to happen*)
* you can execute **scripts** to read data on the blockchain

## Our First Smart Contract

In order to start making our first smart contract, we need to figure out a place to actually put it!

### Install Flow CLI

First install the Cadence Flow CLI by going to [this link](https://forum.flow.com/t/update-on-cadence-1-0/5197/8) and scrolling to the most recent post. Then, copy the command based on what system (Mac/Linux/Windows) youâre running and paste it in your terminal.

After you do that, type `flow version` in your terminal and make sure a version appears.

### Install VSCode

Next, you will need a code editor so you can start writing code. I highly recommend installing [Visual Studio Code](https://code.visualstudio.com/Download). Once you install VSCode, create a folder on your computer and open it up in VSCode. On the left side, click the âExtensionsâ button and search âCadenceâ. Install the one that looks like this:

![vscode cadence extension](https://i.imgur.com/BthLlAu.png)

### Setting Up our Project

Open your project in VSCode by launching the app, going to File > Open > the folder that you want to work in.

In your terminal, navigate to that folder and type `flow init`. You should see this creates a `flow.json` file in your project.

Lastly, create a new file called `HelloWorld.cdc` in your project folder.

Soon, we will be âdeployingâ a contract we make in this file to an address. But what is an address?

### Whatâs an Address?

An address is something that looks like `0xe5a8b7f23e8b548f`.

An address represents an account. Accounts are used to store data (your NFTs, tokens, etc), send transactions, and more. Wallets like Blocto, Metamask (a common wallet on Ethereum), and Dapper create accounts for you and provide a simple interface for you to interact with your account and do things with it.

### Where do Smart Contracts Live?

Smart contracts are deployed to accounts. More specifically, an account will sign a transaction to deploy a contract to itself.

When you want to interact with a contract, you would have to know both the name of the contract and the address where it lives. Weâll see this more in-depth when we import stuff later on.

### Back to our Example

Letâs make our contract now. In our `HelloWorld.cdc` file, type the following:

cadence

```
		
			access(all) contract HelloWorld {

    init() {

    }
}
		 
	
```

Boom, we wrote our first contract. Thatâ¦ has nothing in it.

The `init()` function is a function that every single contract **must** have. It is run when the contract is initially deployed, which only ever happens 1 time. So we can initialize some stuff in it when we want to. Weâll see this later on.

## Adding Data to our Contract

Letâs make our contract store a `greeting` variable.

Modify your contract code so it looks like this:

cadence

```
		
			access(all) contract HelloWorld {

    access(all) let greeting: String

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

The greeting variable:

* has a `access(all)` access modifier, which means anyone can read this variable.
* has `let`, which means itâs a constant (cannot be changed)
* is a `String` type, so it contains some sort of text (in this case âHello Worldâ)

In the `init` function we put `self.greeting = "Hello, World!"`. Remember, the `init()` function is called when the contract is deployed, which only happens once. *Note that we must set a value for `greeting`, and really any variable, in the `init` function or else there will be an error.*

`self.greeting` is referring to the `greeting` variable we declared right above it, and we set it equal to âHello, World!â.

## Deploying our Contract

To deploy this contract, change your `flow.json` to the following code:

json

```
		
			{
	"networks": {
		"emulator": "127.0.0.1:3569",
		"mainnet": "access.mainnet.nodes.onflow.org:9000",
		"testing": "127.0.0.1:3569",
		"testnet": "access.devnet.nodes.onflow.org:9000"
	},
	"contracts": {
		"HelloWorld": "./HelloWorld.cdc"
	},
	"accounts": {
		"emulator-account": {
			"address": "f8d6e0586b0a20c7",
			"key": "d1cee73eb866a5f8293943abb7dcbc210d5d9a3c0337042dcb3d9ec1cb90f534"
		}
	},
	"deployments": {
		"emulator": {
			"emulator-account": ["HelloWorld"]
		}
	}
}
		 
	
```

Then, go to your terminal and:

1. in one terminal, run `flow emulator start -v`. This runs a local version of the Flow blockchain on our computer, otherwise known as an âemulatorâ.
2. in a separate terminal (making sure you navigate to your project directory again), run `flow project deploy`. This will deploy your contract to the emulator, specifically to the âemulator-accountâ that is automatically created for you and has address `0xf8d6e0586b0a20c7`.

## Reading our Greeting

Letâs make sure that our `greeting` variable actually got set to âHello, World!â.

Create another file called `read_greeting.cdc`. Next, write the following code:

cadence

```
		
			import HelloWorld from "./HelloWorld.cdc"

access(all) fun main(): String {
    return HelloWorld.greeting
}
		 
	
```

Then, go to your terminal and run:

bash

```
		
			flow scripts execute ./read_greeting.cdc
		 
	
```

Make sure it returns âHello, World!â.

Soâ¦ what did we just do?! Well, we just executed a **script**. Scripts are used to **read** data from our smart contracts. This script does the following:

1. We imported our smart contract by doing `import HelloWorld from "./HelloWorld.cdc"`. In Cadence, you import a contract by doing `import [contract name] from [address of that contract]`. In this case, our `flow.json` file knows the address of our contract.
2. Next, we wrote a function called âmainâ that returns a `String`. Scripts always have a function named âmainâ.
3. We then accessed the `greeting` variable from the contract using `HelloWorld.greeting`.

## Conclusion

Today, we learned how to deploy our first contract, declare a variable, write a function, and execute a script. Wow! Thatâs a lot. But it wasnât too bad, right?

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Video lesson](#)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter1/lesson1.md)

[Transactions and Scripts](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson2)



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