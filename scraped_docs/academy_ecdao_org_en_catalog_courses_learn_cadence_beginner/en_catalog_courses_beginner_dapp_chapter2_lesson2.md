# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp/chapter2/lesson2

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

# Chapter 2 Lesson 2 - Learning Frontend Code

> If you have already worked with frontend code before, you may find this a bit boring. But itâll be really quick for you.

Hiiiiii! In this chapter, we will be giving you an introduction to HTML & CSS code. This will help you understand all of the code behind your running application.

## What are HTML & CSS?

HTML & CSS are languages used for frontend code.

**HTML is *what* is being displayed on your screen**. From our example yesterdayâ¦

![](/courses/beginner-dapp/base-nextjs.png)

The âWelcome to Next.js!â, the âGet startedâ¦â, and the 4 boxes with all of their text, that is the *what* is being displayed. That is thanks to HTML.

On the other hand, **CSS is the *styling* of the application**. Using the same example, it is what makes the âWelcome to Next.js!â bigger than the rest, âNext.jsâ blue, the boxes appear in a grid format, etc.

Now, we will change up the application to make it simpler, and then explain what all of it is actually doing.

## Remove Boilerplate Code

Letâs remove some boilerplate code (code that is there at the start that just takes up space). We will explain what everything is afterwards.

> Open up your `./pages/index.js` file and replace everything in the file with this code:

javascript

```
		
			import Head from 'next/head';
import styles from '../styles/Home.module.css';

export default function Home() {
	return (
		<div className={styles.container}>
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
			</main>
		</div>
	);
}
		 
	
```

> Then, open up your `./styles/Home.module.css` file and replace everything with this code:

css

```
		
			.main {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
}

.title {
	font-size: 50px;
}

.title a {
	color: #35e8c5;
	text-decoration: none;
}
		 
	
```

> Navigate back to http://localhost:3000/ and look at the changes. God Jacob, you are so talented. Our DApp looks SICK! I know, I know. Iâm the best.

It should look something like this:

![](/courses/beginner-dapp/base-emerald-dapp.png)

## Understanding What We Just Did

> If you already understand all of that, skip this section.

Letâs understand what the heck we just did. First, letâs start in the `./pages/index.js` fileâ¦

javascript

```
		
			import Head from 'next/head';
import styles from '../styles/Home.module.css';
		 
	
```

* Importing something called `Head` and `styles`.
* âImportingâ just means we are bringing in some code to this file so we can use it somewhere.
* `from` means where that code is coming from. In this case, `next/head` is a built in location we can use, so donât worry about it. On the other hand, you can actually find the place `styles` is coming from: `./styles/Home.module.css`. We wrote that ourselves!
* We will see why we need these things soon.

---

javascript

```
		
			export default function Home() {}
		 
	
```

* This creates something called a `Component` that is named âHomeâ.
* A component is a chunk of code that will get ârenderedâ (or put on the screen) if we return something from it
* All of the following code is stuff that lives inside of the Home component

---

javascript

```
		
			return <div></div>;
		 
	
```

* Returns something from the component with the `return` keyword.
* The `return` keyword takes all of the code inside of it and renders it on the screen.
* In this case, weâre returning a `<div>` block, which is basically just a container for other code.
* When you return something from a component, you can only return 1 HTML tag. An HMTL tag is things like `<div>`, `<p>`, `<h1>`. They signal that they hold something inside of them, but are for different things. For example, `<h1>` is for a title, whereas `<p>` is for text, and `<img>` is for an image. If you want to see a list of tags, see [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element).

---

javascript

```
		
			<Head>
	<title>Emerald DApp</title>
	<meta name="description" content="Created by Emerald Academy" />
	<link rel="icon" href="https://i.imgur.com/hvNtbgD.png" />
</Head>
		 
	
```

* Notice why we imported `Head`. We use it here (`Head` is a built-in thing provided by Next.js).
* This changes the information in the browser tab. It looks like this:

![](/courses/beginner-dapp/emerald-dapp-tab.png)


---

javascript

```
		
			<main className={styles.main}>
	<h1 className={styles.title}>
		Welcome to my{' '}
		<a href="https://academy.ecdao.org" target="_blank">
			Emerald DApp!
		</a>
	</h1>
</main>
		 
	
```

* Created another container of code using the `<main>` tag.
* The `<main>` tag has something called a `className` (we will go over this later).
* Inside the `<main>` tag is an `<h1>` tag that has some text in it.
* Inside the `<h1>` tag is an `<a>` tag that links to the Emerald Academy site.
* This piece of code is what youâre seeing on the main page:

![](/courses/beginner-dapp/emerald-dapp-home.png)

If it helps, you can think about this using the âbox modelâ:

![](/courses/beginner-dapp/box-model.png)

Notice also that when you hover over âEmerald DAppâ, your cursor turns into a pointer. If you click it, it actually takes you to the Emerald Academy site. This is because itâs an `<a>` tag in code, which is used for links!

---

Now that we have gone through all of our code, you should at least understand why the things on the screen are appearing there.

## Understanding the Styling

Now letâs walk through the styling, or in other words, the CSS code. CSS is what gives our application code some spice and makes it look the way it does.

Go to `./styles/Home.module.css` and letâs break up the code just like we did before:

css

```
		
			.main {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
}
		 
	
```

* This means that whatever has a `className` of âmainâ should have the styling inside the `{}`
* `height: 100vh` means that this âboxâ takes up the whole height of the screen. `vh` is a measurement of the screenâs dimensions, so `100vh` means the whole screen.
* `display: flex`, `justify-content: center`, and `align-items: center` put the text in the middle of the screen.

---

css

```
		
			.title {
	font-size: 50px;
}
		 
	
```

* This means that whatever has a `className` of âtitleâ should have a `font-size` of `50px`.

---

css

```
		
			.title a {
	color: #35e8c5;
	text-decoration: none;
}
		 
	
```

* This means that any `<a>` tag inside of a tag with a `className` of âtitleâ should be a certain color.
* `text-decoration: none` just means it has no underline when we click the link.

---

PHEW! We are done. Wow, that was a lot. And maybe boring? I donât know. I hope youâre still alive.

## Learn More

Because this is not necessarily a course on frontend development, if youâd like to learn more about HTML and CSS code, please check out these resources:

* <https://www.codecademy.com/catalog/language/html-css>

> If you have any other resources that have helped you, and you want us to list them, please let me know!

## Quests

1. Change the color of âEmerald DAppâ to whatever color you want
2. Change the font size of the title
3. Change the âEmerald DAppâ link to a different link (this means messing with the `<a>` tag)
4. There are two parts.

4a. Inside of your `<main>` tag, add a `<p>` tag and put whatever text you want in it.

4b. Go to the `.main` class and add this line: `flex-direction: column`. Watch what it does!

The box model for Quest #4 looks like this:

![](/courses/beginner-dapp/quest-box-model.png)


---

Take a screenshot of your changes (both the code and the result) and upload it to your quests

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp/en/chapter2/lesson2.md)

[Creating our DApp](/en/catalog/courses/beginner-dapp/chapter2/lesson1)
[Adding Javascript Code](/en/catalog/courses/beginner-dapp/chapter2/lesson3)



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