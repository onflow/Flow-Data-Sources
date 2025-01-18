# Source: https://academy.ecdao.org/en/catalog/courses/niftory/chapter1/lesson3





















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

# Chapter 1 Lesson 3 - The API and building your first app

Youâve already gotten your API keys in the last lesson so now youâre ready to build your very first app on Niftoryâs APIs!

## Sample App

First things first, letâs [clone the Niftory samples workspace](https://github.com/Niftory/niftory-samples). Here, youâll see a few different projects. The one weâll focus on for today is [basic app sdk](https://github.com/Niftory/niftory-samples/tree/test/basic-app-sdk). Note that thereâs another [basic app sample](https://github.com/Niftory/niftory-samples/tree/test/basic-app) that uses the regular graphql API but using the SDK is usually going to be more suitable when creating a client application.

Once youâve gotten the workspace set up, navigate to the basic-app-sdk directory

null
```
		
			cd basic-app-sdk
		 
	
```

Then open up the readme file and follow the instructions. Itâs pretty straightforward, but just so we have it in this lesson as well it consists of:

1. Install dependencies. Nodejs, Yarn and NPM if you havenât already.
2. Create a .env file with the API key and secret that we have from the last lesson
3. Run the app with `yarn dev`.

For a more detailed walkthrough, check out the sample apps [readme](https://github.com/Niftory/niftory-samples/blob/test/basic-app-sdk/README.md).

With the app running, you should see the collection that you created in the last lesson. Pat yourself on the back! This is your first collection *and* your first DApp.

## Niftory Data Model

Okay, now that weâve seen some running code, letâs take a step back and look at the data model

![drawing](https://3595744636-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F1itXKRjyFqqWGYkUXFnP%2Fuploads%2FFUraB6Gkodf53YiwvDTq%2FNiftoryDataModel2.png?alt=media&token=d506b1fd-29d9-49c0-85c4-036477640308)
> The data model

An `AppUser` doesnât need to worry about `NFTModel` and `NFTSet` concepts. Those are for your App to manage and represents the digital collection you want your users to see.

There are two main sections of the Data model which intersect at the NFT.

1. *User*. An `AppUser` has a `Wallet`. The `Wallet` stores NFTs. Pretty simple.
2. *NFT*. The `NFT` is the atomic store of value. It is minted from `NFTModel` which is simply a template. The `NFTSet` is meant simply for you to organize various NFTModels. For example, if you were to develop a pet-rearing game, the NFT would be Mr. Ruffles - the bowler hat wearing Burmese. The NFTModel would be âCatsâ and the NFTSet would be Pets. Perhaps if you started an NFT line of in-game pet houses, that would be a different NFTSet.

## Conclusion

Almost done! We have one bonus lesson centered around authentication types but, youâre well on your way. You now know what Niftory is, why youâd use it and how youâd incorporate it into your projects.

## Quests

1. Pull down the code, create the `.env` file and get the app up and running!

![User avatar](https://i.imgur.com/bymjTdC.png)

Author

[Team Niftory](https://twitter.com/niftory)


[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/niftory/en/chapter1/lesson3.md)


[Admin Portal](/en/catalog/courses/niftory/chapter1/lesson2)
[Authentication](/en/catalog/courses/niftory/chapter1/lesson4)

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



