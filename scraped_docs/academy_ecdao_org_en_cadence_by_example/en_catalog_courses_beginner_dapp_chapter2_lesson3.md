# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter2/lesson3





















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

# Chapter 2 Lesson 3 - Adding Javascript Code

> If you have already worked with React.js or Javascript code before, you may find this a bit boring. But itâll be really quick for you.

Sup sup! In this chapter, we will be teaching you what Javascript code is and what it does. Then we will add some to our project.

> Also, before moving on, make sure to complete all previous quests. They are necessary to continuing at this point.

## What is Javascript?

When we talked about HTML & CSS, we concluded that HTML is the *what*, and CSS is the *styling*. Well, adding Javascript will allow us to *do things* on the site.

For example, when you go to an NFT marketplace and click a âbuyâ button, and it does something. Or when you load up Instagram and the application somehow fetches all your posts and likes from some database, that is Javascript.

Woohoo, we love you Jacob! This sounds like so much fun. I know, it is. Letâs dive into it.

## Adding Some Javascript

Letâs add some Javascript to our application, and maybe it will make more sense.

> Open up your `./pages/index.js` file. Under the `<p>` tag you added in the Quests of lesson 2, add this line of code: `<button>Hello</button>`

The surrounding code should now look something like this:

javascript
```
		
			<main className={styles.main}>
	<h1 className={styles.title}>
		Welcome to my{' '}
		<a href="https://academy.ecdao.org" target="_blank">
			Emerald DApp!
		</a>
	</h1>
	<p>This is a DApp created by Jacob Tucker.</p>

	<button>Hello</button>
</main>
		 
	
```

---

> Go back to your browser at http://localhost:3000 and see that there is now a button under to the text in the middle of the page. It should look like:

![](/courses/beginner-dapp/begin-lesson3.png)

---

Cool! Now letâs make that button do something.

> Go back to your code and right before your `return` keyword, add this piece of code:

javascript
```
		
			function printHello() {
	console.log('Hello there! Jacob is soooooo much cooler than me.');
}
		 
	
```
> Then, change your `<button>` to be this:

html
```
		
			<button onClick="{printHello}">Hello</button>
		 
	
```

What we just did is add a function called `printHello` that will perform some task when it is called. In this case, the âsomethingâ is a `console.log` that prints something to the console.

Then, we added an `onClick` âhandlerâ to our button that will call the `printHello` function when we click the button on the screen.

Your entire file should now look like this:

javascript
```
		
			import Head from 'next/head';
import styles from '../styles/Home.module.css';

export default function Home() {
	function printHello() {
		console.log('Hello there! Jacob is soooooo much cooler than me.');
	}

	return (
		<div>
			<Head>
				<title>Emerald DApp</title>
				<meta name="description" content="Created by Emerald Academy" />
				<link rel="icon" href="https://i.imgur.com/hvNtbgD.png" />
			</Head>

			<main className={styles.main}>
				<h1 className={styles.title}>
					Welcome to my{' '}
					<a href="https://academy.ecdao.org" target="_blank">
						Emerald DApp!
					</a>
				</h1>
				<p>This is a DApp created by Jacob Tucker.</p>

				<button onClick={printHello}>Hello</button>
			</main>
		</div>
	);
}
		 
	
```

---

## Developer Console

The Developer Console is something we can use to actually see our `console.log`s from our code. In order to open the Developer Console:

1. Go back to your browser
2. Right click the screen
3. Click âinspectâ
4. Go to the âConsoleâ tab
5. Click the âHelloâ button on the main screen

You will see something like this:

![](/courses/beginner-dapp/developer-console.png)

When you click the button, you will see messages popping up in the âdeveloper consoleâ now. Usually, developers use the developer console to print error messages or debug their code when they donât know what is wrong. Or in this case, we used it just to make sure things were working.

## Conclusion

Thatâs all for today!

Tomorrow, we will finish the base skeleton of our DApp.

## Quests

Today, we will split the Quests into two different parts.

1. In this part, we will be adding another button and changing up some styling.

* Wrap the `<button>` tag we added inside of a `<div>`. Add a `className` called `styles.flex` to that `<div>`. Make sure the `<button>` is inside of it.
* Then, add another `<button>` inside the `<div>` tag and put âGoodbyeâ inside of it.
* In `./styles/Home.module.css`, add a new style for the âflexâ class, and inside of it, add one line: `display: flex`.
* Your page should now look like this:

![](/courses/beginner-dapp/lesson3-quest1.png)

Here is the box model for what your code should look like:

![](/courses/beginner-dapp/box-model-quest1.png)

2. Now weâre going to add an action to your new button.

* To your second button, add an `onClick` handler and call a function named `printGoodbye`.
* Define a new function called `printGoodbye` under the `printHello` function
* Make it `console.log` âGoodbyeâ

To submit your quests, take a picture of both the screen and the console logs in the developer console.


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter2/lesson3.md)


[Learning Frontend Code](/en/catalog/courses/beginner-dapp/chapter2/lesson2)
[Finishing the Skeleton](/en/catalog/courses/beginner-dapp/chapter2/lesson4)

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



