# Source: https://academy.ecdao.org/en/catalog/tutorials/todo-app

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Catalog](/en/catalog)
ToDo App in Cadence

# ToDo App in Cadence

Tutorial

Beginner

5 mins

# ToDo App in Cadence

The goto example for learning any language is a todo app. Hereâs one for Cadence â the smart contract programming language â for the Flow blockchain.

Letâs create a simple todo app that will allow us to add new todo items to the chain and mark them as completed.

## What are resources?

Each todo item will be a resource. Resources are how unique digital assets are represented in Cadence. They can be created, destroyed, and passed around between accounts. They can also stored in contracts.

## Creating a resource

To declare a resource, we first need to specify what data is contained within it, along with an âinitâ function which sets its initial values. Weâll also add a âmarkCompletedâ function that will allow someone to denote the todo item as completed.

![](https://pbs.twimg.com/media/F2o-fKZbkAA6ghT?format=jpg&name=large)

## Storing our todos

Next, weâll need a public variable that will hold all of our todo items. Weâll use a dictionary for this. The key will be the id of the todo item and the value will be the todo item itself.

![](https://pbs.twimg.com/media/F2o-iCsaUAIJ_lT?format=jpg&name=medium)

## Adding a new todo item

Now we need a way for someone to add a new todo item to the list. Weâll create a public function on the contracted called âaddItemâ that will take a string as an argument and create a new todo item with that text.

![](https://pbs.twimg.com/media/F2o-j6ubgAIIQCW?format=jpg&name=large)

## Completing a todo item

Finally, weâll create a public function called âcompleteItemâ that will take the id of a todo item and mark it as completed.

![](https://pbs.twimg.com/media/F2o-l4maUAAoDXF?format=jpg&name=medium)

## Cadence code

If you want to see the whole contract, check it out interactively on the Flow playground here: <https://play.flow.com/9cdfa00a-9a11-4e71-b31e-9b9aa76fad5f>

![User avatar](https://pbs.twimg.com/profile_images/1640120827135021056/0paOJYnu_400x400.jpg)

Author

[Chase Fleming](https://twitter.com/chasefleming)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/tutorials/todo-app/en/readme.md)



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