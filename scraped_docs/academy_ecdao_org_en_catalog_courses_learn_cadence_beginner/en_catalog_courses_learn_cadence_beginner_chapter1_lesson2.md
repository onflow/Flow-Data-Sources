# Source: https://academy.ecdao.org/en/catalog/courses/learn-cadence-beginner/chapter1/lesson2





















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

# Chapter 1 Lesson 2 - Transactions and Scripts

Hey there you crazy Cadence people! We are back for another lesson of content, and in this lesson, we will be going more in-depth on transactions and scripts.

## Transactions & Scripts

Transactions and scripts are both essential to any blockchain application. Without them, we wouldnât be able to interact with the blockchain at all. On Flow, they are even more special because *they are both separate from the contract.*

### Differences with Ethereum/Solidity

If you have coded in Solidity before, you know that transactions are just functions you call inside the contract itself. However, in Cadence transactions and scripts act as a sort of âmiddlemanâ between the account interacting with the blockchain and the smart contracts. It looks something like this:

![transactions and script picture](/courses/beginner-cadence/sctsworkflow.png)
## Transactions vs. Scripts

The biggest difference between the two is that transactions **modify the data** on the blockchain and scripts **view the data** on the blockchain. Here is a helpful diagram to understand the differences:

![difference between transactions and scripts](/courses/beginner-cadence/transactionvscript.png)

As you can see, scripts do not cost any money. Transactions on the other hand cost gas (money), which is a form of payment needed to change the data on the blockchain. It is **super** cheap on Flow though.

## Scripts

During the last lesson, we actually implemented our first contract, transaction, and script on a local emulator. Letâs revisit that example:

Load up your project and redeploy your contract:

cadence
```
		
			access(all) contract HelloWorld {

    access(all) let greeting: String

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

Re-run your script as well:

cadence
```
		
			import HelloWorld from "./HelloWorld.cdc"

access(all) fun main(): String {
    return HelloWorld.greeting
}
		 
	
```

You should see âHello, World!â in your terminal. Great! What you just did is run a script. Notice there was no payment needed and we **viewed** the data in our smart contract.

## Transactions

Now letâs do an example of a transaction. Create another file called `change_greeting.cdc`.

Okay cool. Now we want to modify the data on the blockchain. In order to do that, letâs set up our transaction. We can do that by pasting this code:

cadence
```
		
			transaction() {
    prepare(signer: &Account) {

    }

    execute {

    }
}
		 
	
```

Boom! This is an empty transaction that doesnât do anything.

There are 2 stages of a transaction in which we write code: `prepare` and `execute`. You will learn more on this later. For now, just know that `prepare` is where we deal with user accounts and `execute` is where we do everything else. So weâll stick with `execute` until we cover accounts.

### Changing our Greeting

Alright, so we want to change our `greeting` field to be something other than âHello, World!â But thereâs a problem: we never added a way to modify our data in the smart contract! So we have to add a function in the contract to do that.

Go back to your contract and add the following function:

cadence
```
		
			access(all) fun changeGreeting(newGreeting: String) {
  self.greeting = newGreeting
}
		 
	
```

We just added a new function that:

* takes in a `newGreeting` parameter. It is a `String` type
* sets our `greeting` variable equal to `newGreeting`
* does not return anything, hence the missing return type

But wait! Thereâs an error in the contract. It says âcannot assign to constant member: `greeting`.â Why is it saying that? Remember, we made our greeting be `let`. `let` means itâs a constant, so if we want to change our `greeting`, we must change it to `var`. Your code should now look like this:

cadence
```
		
			access(all) contract HelloWorld {

    access(all) var greeting: String

    access(all) fun changeGreeting(newGreeting: String) {
        self.greeting = newGreeting
    }

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

Make sure to deploy your contract again by stopping your emulator, restarting it, and deploying. OR you can simply run a command to update your contract: `flow project deploy --update`.

### Sending Our Transaction

Go back to your `change_greeting.cdc` file and add the following code:

cadence
```
		
			import HelloWorld from "./HelloWorld.cdc"

transaction(myNewGreeting: String) {

  prepare(signer: &Account) {}

  execute {
    HelloWorld.changeGreeting(newGreeting: myNewGreeting)
    log("We're done!")
  }
}
		 
	
```

We use the `log` function to print things to our emulator. This is really helpful for testing our code. This will do nothing on real, public networks like testnet and mainnet.

You can see that this transaction is expecting an input from you. Specifically, you must provide the transaction with a new greeting, which will get provided to the `myNewGreeting` variable.

To provide an argument to a transaction, you simply add it to the end of the command.

So in your terminal, run this transaction like so:

bash
```
		
			flow transactions send ./change_greeting.cdc "Hey there, Jacob!"
		 
	
```

To make sure this transaction actually ran, go to the terminal that is running your emulator (where all log output will be) and make sure you see âWeâre done!â printed in the console.

Lastly, if you rerun your script, you should now see âHey there, Jacob!â printed in the console. Boom, you just successfully implemented your first transaction.

Try to change the greeting to something else by running the same command, but changing the text at the end.

## Conclusion

Today we learned how to send a transaction in Cadence. This is for modifying data.

We also learned how to execute a script in Cadence. This is for reading data.


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/learn-cadence-beginner/en/chapter1/lesson2.md)


[Our First Smart Contract](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson1)
[Types](/en/catalog/courses/learn-cadence-beginner/chapter1/lesson3)

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



