# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter3/lesson2

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

# Chapter 3 Lesson 2 - Transactions and Scripts

Hey there you crazy Cadence people! We are BACK for another lesson of content, and in this lesson, we will be going more in-depth on transactions and scripts. If you havenât already, make sure you read the introductory part to transactions and scripts in Chapter 1 Lesson 1.

## Transactions & Scripts

Transactions and scripts are both essential to any blockchain application. Without them, we wouldnât be able to interact with the blockchain at all. On Flow, they are even more special because *they are both separate from the contract.* If you have coded on Ethereum before, you know that transactions are just functions you call inside the contract itself (if you donât know that, thatâs okay!). However, on Flow, transactions and scripts act as a sort of âmiddlemanâ between the person interacting with the blockchain and the smart contracts. It looks something like this:

![drawing](/courses/beginner-dapp/sctsworkflow.png)

## Transactions vs. Scripts

Now, what is the difference between transactions and scripts? Well, the biggest difference is that transactions **modify the data** on the blockchain, and scripts **view the data** on the blockchain. Here is a helpful diagram to understand the differences:

![drawing](/courses/beginner-dapp/transactionvscript.png)

As you can see, scripts also do not cost any money (phew!). Transactions on the other hand cost âgas,â which is a form of payment needed to change the data on the blockchain.

## Scripts

During the last lesson, we actually implemented our first script on the Flow playground. Letâs revisit that example:

> Load up the flow playground (<https://play.onflow.org>), copy this contract into the `0x01` account, and click âDeployâ:

cadence

```
		
			pub contract HelloWorld {

    pub var greeting: String

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

> Then, go to the Script tab on the left hand side and bring back our script from yesterday:

cadence

```
		
			import HelloWorld from 0x01

pub fun main(): String {
    return HelloWorld.greeting
}
		 
	
```

> If you click âExecute,â you should see âHello, World!â in the console.

Great! What you just did is run a script. Notice there was no payment needed and we **viewed** the data in our smart contract.

## Transactions

Now, letâs do an example of a transaction.

> On the left hand side, under âTransaction Templates,â click on the âTransactionâ tab. Go ahead and delete everything in that tab so it looks like this:

![drawing](/courses/beginner-dapp/emptytx.PNG)

Okay, cool. Now, we want to modify the data on the blockchain. In order to do that, letâs set up our transaction.

> We can do that by putting this code into the page:

cadence

```
		
			transaction() {
    prepare(signer: AuthAccount) {}

    execute {}
}
		 
	
```

Boom! This is an empty transaction that doesnât do anything. In order to explain what `prepare` and `execute`, we need to take a quick break and talk about accounts on Flow.

### Accounts on Flow

On Flow, accounts can store their own data. What does this mean? Well, if I own an NFT (NonFungibleToken) on Flow, that NFT gets stored in my account. This is *very different* than other blockchains like Ethereum. On Ethereum, your NFT gets stored in the smart contract. On Flow, we actually allow accounts to store their own data themselves, which is super cool. But how do we access the data in their account? We can do that with the `AuthAccount` type. Every time a user (like you and me) sends a transaction, you have to pay for the transaction, and then you âsignâ it. All that means is you clicked a button saying âhey, I want to approve this transaction.â When you sign it, the transaction takes in your `AuthAccount` and can access the data in your account.

You can see this being done in the `prepare` portion of the transaction, and thatâs the whole point of the `prepare` phase: to access the information/data in your account. On the other hand, the `execute` phase canât do that. But it can call functions and do stuff to change the data on the blockchain. NOTE: In reality, you never *actually* need the `execute` phase. You could technically do everything in the `prepare` phase, but the code is less clear that way. Itâs better to separate the logic.

### Back to our Example

Alright, so we want to change our `greeting` field to be something other than âHello, World!â But thereâs a problem. We never added a way to modify our data in the smart contract! So we have to add a function in the contract to do that.

> Go back to account `0x01` and add this function inside the contract:

cadence

```
		
			pub fun changeGreeting(newGreeting: String) {
    self.greeting = newGreeting
}
		 
	
```

What does this mean? Remember from previous lessons what we said about functions. You set them up like so:
`[access modifier] fun [function name](parameter1: Type, parameter2: Type, ...): [return type] {}`

In order to keep things simple, we are using `pub` as our access modifier. `pub` means we can call this function from anywhere (in our contract or in a transaction). We also take in a `newGreeting` parameter that is a string, and we set our greeting equal to our new greeting.

But wait! Thereâs an error in the contract. It says âcannot assign to constant member: `greeting`.â Why is it saying that? Remember, we made our greeting be `let`. `let` means itâs a constant, so if we want to change our `greeting`, we must change it to `var`. Make sure to hit âDeployâ again. Your code should now look like this:

cadence

```
		
			pub contract HelloWorld {

    pub var greeting: String

    pub fun changeGreeting(newGreeting: String) {
        self.greeting = newGreeting
    }

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

Now that weâve set up our contract, letâs go back to our transaction.

> First, letâs make sure to `import` our HelloWorld contract, like so: `import HelloWorld from 0x01`.

Then, we must decide: where do we want to call `changeGreeting`? In the `prepare` phase, or the `execute` phase? The answer is the `execute` phase because we are not accessing any data in the account. We are just changing some data in the smart contract.

> We can do that by adding this line in the `execute` phase:

cadence

```
		
			HelloWorld.changeGreeting(newGreeting: myNewGreeting)
		 
	
```

When you call a function in Cadence, you pass in parameters by doing `(argumentLabel: value`), where `argumentLabel` is the name of the argument and `value` is the actual value. You will notice we get an error that `myNewGreeting` isnât defined, which makes sense, because we arenât getting it from anywhere.

> So letâs add a parameter called `myNewGreeting` to our transaction so we can pass in a value for a new greeting. We can do that like so:

cadence

```
		
			import HelloWorld from 0x01

transaction(myNewGreeting: String) {

  prepare(signer: AuthAccount) {}

  execute {
    HelloWorld.changeGreeting(newGreeting: myNewGreeting)
  }
}
		 
	
```

Now, on the right side, youâll see a prompt pop up. We can type in our new greeting into the little box! Letâs type âGoodbye, World!â:

![drawing](/courses/beginner-dapp/txgoodbye.PNG)

Notice also that we can âsignâ this transaction from any account. Since it doesnât really matter (we arenât accessing data in an account), feel free to choose any account you wish.

> After you click âSendâ, go back to your Script and click âExecuteâ. You should now see âGoodbye, World!â printed in the console.

Boom, you just successfully implemented your first transaction.

That wraps things up for today.

## Conclusion

We just spent 2 lessons on Cadence. This is all the Cadence we will cover in this course.

If you want to learn more about Cadence, you should definitely check out our [Beginner Cadence Course](https://github.com/emerald-dao/beginner-cadence-course). It is structured the same way as this one, and in fact, all of Chapter 1 and Chapter 3 Lessons 1-2 were taken directly from that course!

## Quests

Please answer in the language of your choice.

1. Explain why we wouldnât call `changeGreeting` in a script.
2. What does the `AuthAccount` mean in the `prepare` phase of the transaction?
3. What is the difference between the `prepare` phase and the `execute` phase in the transaction?
4. This is the hardest quest so far, so if it takes you some time, do not worry! I can help you in the Discord if you have questions.

* Add two new things inside your contract:

  + A variable named `myNumber` that has type `Int` (set it to 0 when the contract is deployed)
  + A function named `updateMyNumber` that takes in a new number named `newNumber` as a parameter that has type `Int` and updates `myNumber` to be `newNumber`
* Add a script that reads `myNumber` from the contract
* Add a transaction that takes in a parameter named `myNewNumber` and passes it into the `updateMyNumber` function. Verify that your number changed by running the script again.

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Video lesson](#)
[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter3/lesson2.md)

[Our First Smart Contract](/en/catalog/courses/beginner-dapp/chapter3/lesson1)
[Bringing Cadence to our DApp & Deploying our Contract](/en/catalog/courses/beginner-dapp/chapter3/lesson3)



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