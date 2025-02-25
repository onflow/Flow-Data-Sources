# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter1/lesson1

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

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

# Chapter 1 Lesson 1 - Understanding Blockchain Concepts

Welcome to the first lesson of this comprehensive course on building iOS Mobile DApps for the Flow Blockchain. I am BoiseITGuru, your instructor for this journey. In this lesson, we start with exploring the fundamental concepts of blockchain technology.

## What is a Blockchain?

![drawing](https://i.imgur.com/lnSYcQm.png)

If you already have a good grasp of blockchain technology, feel free to skip this section. Otherwise, letâs delve into the basics.

A Blockchain is an open, decentralized, and shared database that enables public storage of information. Its key features are:

1. **Open**: Anyone can interact with the blockchain without restrictions.
2. **Decentralized**: It operates without a central authority, making it free from centralized control.
3. **Database**: Information can be stored securely on the blockchain.
4. **Public**: Data on the blockchain is accessible to anyone.

The blockchain allows various interactions, and we will primarily focus on coding smart contracts and building decentralized applications (DApps) using this technology. Itâs essential to note that there are multiple blockchains available, and for this course, we will be focusing on the Flow Blockchain.

## Smart Contracts - Powerful Code on the Blockchain

![drawing](https://i.imgur.com/e0pKRQf.png)

Smart contracts are programs or ârulebooksâ designed by developers to define specific functionalities for users to interact with. For instance, you could create a smart contract that allows users to store their favorite fruit on the blockchain, and this data would be permanently stored unless explicitly removed.

Benefits of smart contracts include:

1. **Speed, Efficiency, and Accuracy**: Smart contracts are fast and remove the need for intermediaries, reducing paperwork and approval processes.
2. **Trust and Transparency**: Smart contracts enhance security and transparency, ensuring that actions permitted by the contract are the only ones possible.

However, there are some downsides to consider:

1. **Complexity**: Developing smart contracts requires expertise to ensure security, cost-effectiveness, and desired functionality.
2. **Security Concerns**: A poorly designed smart contract can be exploited maliciously, resulting in loss of funds or data.
3. **Immutable**: Once a smart contract is deployed, its actions cannot be undone unless specific functions are built for that purpose.

## Transactions & Scripts - Interacting with Smart Contracts

![drawing](https://i.imgur.com/XU8iOHj.png)

A transaction is essentially a paid function call that changes data on the blockchain. It is the primary method for altering blockchain data. Transactions involve costs, known as gas fees, which can vary depending on the blockchain. For instance, Flowâs gas fees are extremely low compared to other blockchains like Ethereum.

In contrast, scripts are used to view data on the blockchain without altering it. They are free and do not incur any costs.

The standard workflow for interacting with a smart contract is:

1. Deploying a smart contract to the blockchain.
2. Executing a transaction with the required payment of gas fees to call functions within the smart contract.
3. The smart contract updates its data according to the executed function.

## âMainNetâ vs. âTestNetâ Environments

![drawing](https://i.imgur.com/IsKWP5M.png)

When developing blockchain applications, developers often use two different environments:

**TestNet** is a testing environment where developers can experiment and identify issues before deploying their applications to the public. It offers the following advantages:

* Simulated environment with fake data and no actual money involved.
* Transactions and interactions cost simulated or fake money.
* Safer space for testing smart contracts and applications.

**MainNet** is the live environment where real transactions and interactions take place. Applications are deployed on MainNet for public use. Key aspects of MainNet include:

* Real transactions with actual money involved.
* High risk, so applications must be thoroughly tested before deployment.
* Provides the actual user experience.

## Decentralized Applications (DApps) - Empowering Traditional Apps

![drawing](https://i.imgur.com/Q9KopWa.jpg)

DApps are regular applications (ie. Swift, Kotlin, Javascript) that incorporate a blockchain and smart contracts. The inclusion of blockchain technology gives users transparency and trust in the application they are using. For example, a social media app like Instagram traditionally is not a âDAppâ because the core application does not involve any blockchain code. However, they could technically be classified as a DApp due to Flowâs recent announcement of NFT integration into the platform.

Throughout this course, we will build a DApp that utilizes smart contracts on the Flow Blockchain.

## Conclusion

Blockchain technology and smart contracts may sound complex, but with practical examples, they become clearer. In the upcoming lessons, we will explore real-world use cases and hands-on coding to help solidify your understanding.

## Quests

Feel free to answer the following questions in your preferred language:

1. Explain the concept of blockchain in your own words. You may refer to external sources for assistance.
2. Define a smart contract in your own words. You can use external resources for guidance.
3. Differentiate between a script and a transaction on the blockchain.
4. Describe the differences between TestNet and MainNet environments and when to use each for development.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter1/lesson1.md)

[Exploring the Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson2)



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