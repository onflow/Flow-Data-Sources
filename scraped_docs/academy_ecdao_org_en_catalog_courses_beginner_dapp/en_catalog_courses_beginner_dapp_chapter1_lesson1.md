# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter1/lesson1





















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

# Chapter 1 Lesson 1 - Learning Blockchain Concepts

Hello! Yes, it is me. Your favourite developer of all time, Jacob. You are currently viewing the first lesson of the entire course. Letâs start this journey together.

Letâs start off our first lesson by going over what seems to be complicated terms that you will need to understand for the journey ahead.

## What the heck is a Blockchain?

![drawing](/courses/beginner-dapp/blockchain.png)

*If you already understand what the Blockchain is or you simply donât care (thatâs fair!), you can skip this section.*

When learning about the Blockchain, you may find some complicated articles. Itâs easy to get completely lost in the sauce and feel like you want to give up. So, Iâm going to explain the Blockchain in a very easy way that may have some innacuracies/left out information but is meant to help you get started. **Specifically, I will help you understand the Blockchain from the perspective of someone who is looking to code Smart Contracts or make some Decentralized Applications (both of which we will do!).**

In one sentence: the Blockchain is an open, decentralized, shared database that allows anyone to store stuff publically.

Okay, woah. What does that mean?

1. **OPEN**: Anyone can interact with it. There are no restrictions.
2. **DECENTRALIZED**: Nobody owns it. There is no central authority dictating stuff.
3. **DATABASE**: You can store information on it.
4. **PUBLIC**: Anyone can view the data on it.

Because of these things, we can interact with the Blockchain however we please. Often times, we may want to set up ârulebooksâ that determine how people can interact with specific parts of the Blockchain so that it has some functionality - specifically our own applications that we will define. This is done with Smart Contracts.

Itâs also important to note that there are many different Blockchains out there. For example, Ethereum is probably the most popular Blockchain. In this course, we will be learning about the wonderful Flow Blockchain, because thatâs where my expertise lies ;)

## Smart Contracts? Ooo, that sounds cool.

![drawing](/courses/beginner-dapp/smart contract.png)

Why yes, yes it is. Smart Contracts are very cool. Smart Contracts are programs, or ârulebooksâ that developers make. Developers create them because it allows us to specify some functionality that users can interact with. For example, if I want to make an application that allows users to store their favourite fruit on the Blockchain, I need to make a Smart Contract that:

1. Has a function that anyone can call
2. Takes in a parameter (the personâs favourite fruit)
3. Stores that parameter in some data
4. Sends the updated data to the Blockchain (happens automatically)

If I created this Smart Contract and âdeployedâ it to the Blockchain (deployed means we put the contract onto the Blockchain so people can interact with it), then anyone could put their favourite fruit on the Blockchain, and it would live there forever and ever! Unless we also had a function to remove that data.

So, why do we use Smart Contracts?

1. **Speed, efficiency and accuracy**: Smart Contracts are fast, and there is no middleman. There is also no paperwork. If I want to update the data on the Blockchain by using a Smart Contract that allows me to call some function, I can just do it. I donât have to get approval from my parents or my bank.
2. **Trust and transparency**: The Blockchain, and thus Smart Contracts, are extremely secure if we make them that way. It is near impossible to hack or alter the state of the Blockchain, and while thatâs due to other reasons, it is largely because of Smart Contracts. If a Smart Contract doesnât let me do something, I simply canât do it. Thereâs no way around it.

What are some downsides?

1. **Hard to get right**: While Smart Contracts are cool, they are NOT smart. They require sophisticated levels of expertise from the developerâs side to make sure they have no security problems, they are cheap, and they do what we want them to do. We will learn all of this later.
2. **Can be malicious if the developer is mean**: If a developer wants to make a Smart Contract that steals your money, and then tricks you into calling a function that does that, your money will be stolen. In the world of the Blockchain, you must make sure you interact with Smart Contracts that you know are secure.
3. **Cannot undo something**: You canât just undo something. Unless you have a function that allows you to.

## Transactions & Scripts

![drawing](/courses/beginner-dapp/transaction.jpeg)

*âOkay, so we have a Smart Contract. How do I actually interact with it? You keep saying call a function, but what does that mean!?â*

**A transaction is a glorified, paid function call.** Thatâs pretty much the simplest I can put it. Whatâs important to know is that a transaction CHANGES the data on the Blockchain, and usually is the ONLY way we can change the data on the Blockchain. Transactions can cost different amounts of money depending on which Blockchain you are on. On Ethereum, to store your favourite fruit on the Blockchain, it could cost dang near 100$. On Flow, itâs fractions of a cent.

On the other hand, a script is used to VIEW data on the Blockchain, they do not change it. Scripts do not cost any money, thatâd be ridiculous.

Here is the normal workflow:

1. A developer âdeploysâ a Smart Contract to the Blockchain
2. A user runs a âtransactionâ that takes in some payment (to pay for gas fees, execution, etc) that calls some functions in the Smart Contract
3. **The Smart Contract changes its data in some way**

## âMainNetâ vs. âTestNetâ

![drawing](/courses/beginner-dapp/tvm.PNG)

You may have heard these terms come up, but what do they actually mean?

**TestNet** is an environment where developers test their applications before releasing it to the public. This is a perfect space to figure out whatâs wrong with your application before actually releasing it to the public to use. Here are a few additional notes:

* Everything is fake
* No actual money involved
* Transactions cost fake money
* A good way for developers to test their smart contracts and applications BEFORE releasing to the public
* If something bad happens, no one cares.

**MainNet** is an environment where everything is real. When you release your application to the public, you put it on MainNet. On MainNet, everything is live, so things cost real money, there are risks, and you must make sure everything is working correctly. Here are a few additional notes:

* Everything is real
* Money is involved
* Transactions cost real money
* When your application is fully ready, you put it on MainNet for users to interact with.
* If something bad happens, thatâs really bad.

## Decentralized Applications (DApps)

![drawing](/courses/beginner-dapp/dapps.jpeg)

Oh no, this sounds complicated. Nope! Itâs not. DApps are literally just normal applications (Javascript, Python, etc) that ALSO have Smart Contracts involved. Thatâs it.

For example, Instagram is an application that is not a âDAppâ because it doesnât involve any blockchain code. However, after Flowâs recent announcement of NFT integration into Instagram, we can officially call Instagram a DApp. Examples of other DApps includes [FLOAT](https://floats.city/).

Also, we will be building a DApp throughout this course :)

## Why do I care about all this?

Well, because thatâs what this course is all about, knucklehead! In this course, we will be making our own Smart Contracts, specifically on the Flow Blockchain. In addition, we will be making Decentralized Applications that *use* those Smart Contracts.

## Conclusion

Jacob is the best. No, no. Thatâs not the conclusion. The conclusion is that although all of this stuff sounds very complicated, it really isnât. And if you still donât understand ANY of this, thatâs totally okay. Sometimes itâs better to jump into some examples to make things make more sense. Weâll be doing that in the upcoming lessons.

## Quests

You are free to answer these questions in your own language of choice. And no, I donât mean computer programming language, haha.

1. Explain what the Blockchain is in your own words. You can read this to help you, but you donât have to: <https://www.investopedia.com/terms/b/blockchain.asp>
2. Explain what a Smart Contract is. You can read this to help you, but you donât have to: <https://www.ibm.com/topics/smart-contracts>
3. Explain the difference between a script and a transaction.
4. What is the difference between Testnet and Mainnet? When would you develop on each?

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter1/lesson1.md)


[The Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp/chapter1/lesson2)

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



