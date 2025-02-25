# Source: https://academy.ecdao.org/en/catalog/courses/niftory/chapter1/lesson2

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Course Overview](/en/catalog/courses/niftory)

1. Niftory Concepts

[1.1 Why Niftory?](/en/catalog/courses/niftory/chapter1/lesson1)[1.2 Admin Portal](/en/catalog/courses/niftory/chapter1/lesson2)[1.3 Basic Niftory App](/en/catalog/courses/niftory/chapter1/lesson3)[1.4 Authentication](/en/catalog/courses/niftory/chapter1/lesson4)

Course Overview

[Catalog](/en/catalog)
[Course](/en/catalog/courses/niftory)
Niftory

# Chapter 1 Lesson 2 - The Admin Portal

The first of the two tools that make up Niftory. The admin portal is the source of tremendous power and has functionality thatâs meant for all the different types of people that may go into making an NFT project come to life. Or it could be just for one person wearing multiple hats.

The Niftory admin dashboard is designed to let you easily switch between different operations during the launch of your NFT collection. Okay, so check this out - each of the boxes below are labeled 1 through 4. Letâs go through them one by one.

![drawing](/courses/niftory/niftory-welcome.png)

1. **Collection**. This view is primarily for your designers and artists who need to manage the assets being collected as an NFT. In Collections view, youâll see all of this content. **Sets** are primarily a way to organize your NFT Collection. **Collectibles** are templates for the NFTs that are being made. These Sets and Collectibles are created and minted on the blockchain.
2. **Manage**. Manage your app and organization settings. Developers can find useful information (like API key and client secret here).
3. **Dashboard**. For people more interested in the business side of thing, the dashboards give you full visibility into your users, sales, and anything else you might want to know.
4. **Listings**. Once the collection is ready, share it with the word through the listings page.

We will mostly focus on the **App Settings** view for the remainder of this tutorial but that should give you a good overview of everything the admin panel can do.

## Deploying a contract

Now, weâre going to deploy a contract in under 30s. Ready? LFG!

1. Head on over to [Niftory](https://www.niftory.com/) and hit the big âGet My API Keyâ button.
2. Youâll be prompted to create an account with Niftory.
3. Once youâve created an account, youâll have to name your organization. Donât worry about this part being perfect, you can always change this later.

![drawing](/courses/niftory/niftory-org-name.png)

4. Once youâve create an organization, you will be prompted to name the app. Again, this can be changed later.

![drawing](/courses/niftory/niftory-app-name.png)

5. Now, you will get dropped into the admin panel into a first-run user flow. This part is actually fairly important because you are naming the app for the final time (no takebacks). If you get the naming wrong, or you need to start over, you *can* always create a new contract.

![drawing](/courses/niftory/niftory-contract-name.png)

6. Hit âDeployâ to finalize the contract name and write it to the blockchain.

![drawing](/courses/niftory/niftory-deploy.png)

And voila! Youâve just deployed your first Flow contract.

## Mainnet vs. Testnet

Here, itâs probably good to direct you to another excellent course here on Emerald DAO. The full course is [here](https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter1/lesson1#mainnet-vs-testnet), but hereâs a tiny excerpt that should give you enough of an idea to get going:

TestNet:

> TestNet is an environment where developers test their applications before releasing it to the public. This is a perfect space to figure out whatâs wrong with your application before actually releasing it to the public to use.

MainNet:

> MainNet is an environment where everything is real. When you release your application to the public, you put it on MainNet. On MainNet, everything is live, so things cost real money, there are risks, and you must make sure everything is working correctly.

In Niftory, you can switch from TestNet to MainNet with a toggle. This is a particularly powerful toggle because as weâve discussed, once things are deployed to MainNet, people are spending *real* money.

![drawing](/courses/niftory/niftory-admin.png)

## Creating a collection

Youâre now ready to create your very first collection of NFTs! Weâre not going to need to code at all during this stage. Simply navigate to the âCollectionâ page of the Niftory admin panel, and follow these steps. Donât worry too much about filling in all the non-required text fields because you should do this *all* on testnet:

1. Create a set.
2. Create a collectible in the set. Remember, this is just the template of the NFT and not an NFT itself.
3. List the NFT. Niftory will handle the first mint for the collectible specified. Once the NFTs have been minted, they should be ready to transfer to customers. Alternatively, thereâs an API that you could trigger to allow users to kickoff the mint themselves.

## Conclusion

That about wraps things up for today! In the next lesson, we will walk through the current Niftory sample so you can use it as a template to get started on your own DApp.

## Quests

1. Go on ahead and [get your API keys](https://docs.niftory.com/home/get-your-api-keys). Donât worry, itâs free! If you followed the steps in the lesson, you should already have the API key, have deployed your contract *and* have your first collection ready to go.

![User avatar](https://i.imgur.com/bymjTdC.png)

Author

[Team Niftory](https://twitter.com/niftory)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/niftory/en/chapter1/lesson2.md)

[Why Niftory?](/en/catalog/courses/niftory/chapter1/lesson1)
[Basic Niftory App](/en/catalog/courses/niftory/chapter1/lesson3)



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