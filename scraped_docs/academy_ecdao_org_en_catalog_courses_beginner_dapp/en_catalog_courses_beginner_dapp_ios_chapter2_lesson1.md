# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter2/lesson1





















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

# Chapter 2 Lesson 1 - Creating our Mobile (iOS) DApp

> Developing apps for iOS requires using a Mac, if you donât have access to Mac the easiest way to get is started is by renting access to a Mac using services like [macincloud](https://checkout.macincloud.com)

In this lesson, we are going to actually jump into some code and start our Mobile (iOS) DApp development. We will be using Swift and SwiftUI to create our first DApp.

## IMPORTANT NOTE

Chapter 2 will focus on front-end development, specifically the semantics of Swift and SwiftUI. If you are already comfortable with these languages, you still need to complete Chapter 2 because you will be setting up for other chapters. However it will be very quick for you, and you can skim through the lesson. That is totally okay.

## What is Swift and SwiftUI?

> You can skip this section if you already know the basic of Swift/SwiftUI and frontend development

iOS apps are developed using Appleâs native programming languages Swift and SwiftUI, with the application âlogicâ or functionality being declared in Swift and the user interface being defined in SwiftUI. With SwiftUI, we can define our user interface using a declarative syntax, making it easy to understand and maintain.

Before we get started, letâs cover the difference between âfrontendâ and âbackendâ development

### Frontend iOS Development

When you visit a website or open a mobile app, you are presented with content on the screen. As a user, three primary aspects immediately catch your attention:

1. **What is being displayed**: This refers to the actual content visible on the screen, such as text, images, buttons, and other elements.
2. **How it looks (Styling)**: Styling encompasses the visual appearance of the content, including colors, fonts, layout, and overall design aesthetics.
3. **What happens when you interact (Interactivity)**: This aspect pertains to the behavior of the app or website when you interact with it, such as clicking on buttons, scrolling through content, or triggering animations.

Collectively, these elements are integral to what we call âfrontendâ development. Frontend development focuses on crafting the user experience and interface that users interact with directly. For instance, when you use Instagram, activities like scrolling through your feed, viewing posts, searching for content, and liking posts by tapping the heart button are all part of the front-end components. Itâs the front end that allows you to engage with the appâs features and explore its functionalities, making it a crucial aspect of the overall user experience.

### Backend iOS Development

In contrast to frontend development, there is a vital aspect known as âbackendâ development. And donât worry, itâs not as hard as Jacob makes it sound in his web-focused lessons! Backend development is responsible for handling operations that occur outside of your mobile device. While frontend development deals with what you see and interact with on your phone, the backend typically operates on a remote system running elsewhere. In the context of traditional Web2 applications like Instagram, backend development involves various essential tasks, including:

1. **Fetching Complicated Information**: The backend is responsible for retrieving and processing complex data from various sources, such as databases or external APIs. This information may require extensive computations or multiple data sources to provide the desired results.
2. **Storing Data in a Database**: When you interact with an app, like making a post on Instagram, the backend handles the storage of that postâs information in a database. The database serves as a centralized repository for all the appâs data, making it accessible and persistent.
3. **Handling Complex Procedures**: Certain operations, like performing extensive calculations or executing resource-intensive tasks, are better suited for backend processing. This avoids overburdening the front end, ensuring a smoother user experience.

For instance, when you tap on a userâs profile in the Instagram app, the backend springs into action. It gathers all the necessary data related to that user, such as their posts, followers, and other information, and then delivers it to the front end. The front end then displays this data to you, allowing you to view the userâs profile.

Similarly, when you create a post on Instagram, the front end sends the postâs details, like the description and image, to the backend. The backend then handles the process of saving this post in a database, ensuring that your post is securely stored and accessible to other users.

In summary, backend development plays a crucial role in managing the complex, behind-the-scenes operations of a mobile app, making it an indispensable component of the overall app development process.

### Back to our mobile development journey!

Now that we have gotten some basics out of the way, we can start building our Mobile DApp, as you may have guessed the app will be our âfrontendâ and we will be using the Flow Blockchain as our âbackendâ.

## Setting Up the Environment

Before we dive into the rest of the tutorial, letâs make sure we have the necessary tools installed to develop our iOS app. If you need any help, please reach out in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

1. Xcode: Install Xcode from the Mac App Store. Xcode is the integrated development environment (IDE) for macOS that includes all the tools needed for iOS app development.
2. Git: If you donât already have Git installed, you can follow the instructions on this website: <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>. You can confirm that Git is installed by running git âversion in the Terminal.

## Creating Our DApp Project

> Note I am using Xcode Version 15 Beta, your Xcode version might look slightly different as Apple releases new updates.

1. Open Xcode, and from the welcome screen, select âCreate a new Xcode projectâ![](https://i.imgur.com/7IutQqM.png)
2. Choose âAppâ under the Multiplatform section, this way our app will work on both iOS and iPadOS.![](https://i.imgur.com/GA18lwP.png)
3. On the next screen, enter `EmeraldDApp` for the product name, leave the default value for the rest of the options, and then click Next.![](https://i.imgur.com/DftpgpA.png)
4. Select a location to save your project and be sure to check the `Create Git repository on my Mac` box so we can save this project to our GitHub repository later.![](https://i.imgur.com/gSX1cMr.png)
5. The last thing we need to do is remove the Mac destination as the FCL-Swift SDK doesnât support it yet. Click on the top `EmeraldDApp` in your project structure on the left. Select `Mac` in the Supported Destinations list, then click the minus button to remove it.![](https://i.imgur.com/GNdCEPT.png)

## Understanding the Project Structure

Your project in Xcode should have the following structure:

> Note that Xcode hides the file extension of the files unless you are renaming them or viewing them in the Finder.

* EmeraldDApp
  + EmeraldDApp
    - EmeraldDAppApp.swift
    - ContentView.swift
    - Assets.xcassets
    - EmeraldDApp.entitlements
  + Preview Content
    - Preview Assets.xcassets

1. EmeraldDAppApp.swift is the main entry point for the project and defines the initial view to be displayed as well as hosting the appâs life cycle. If you click on the file to open it you can see it contains a `WindowGroup` that loads the `ContentView`. Donât worry too much about how this works for now, the key thing to note is that when the application launches it will display our `ContentView`.
2. ContentView.swift contains the initial view to be displayed in the application.
3. Assets.xcassets is where we will place our image assets to be displayed inside our views.
4. The remainder of the files are used by the Xcode compiler to build the application and are not relevant to the course.

## Viewing Our DApp Preview

Before we even jump into coding our DApp, letâs explore how Xcode allows us to preview our DApp as it is developed. Previews are a powerful feature that allows developers to visualize and interact with SwiftUI views in real-time without running the entire app on a simulator or device. Previews provide a live preview of the user interface, enabling developers to see how their SwiftUI code will look and behave across various device sizes and orientations instantly. This streamlined workflow makes it easier for beginners and experienced developers alike to iterate and refine their user interfaces quickly, saving time and enhancing the development process.

As we develop our DApp, the changes you make to your SwiftUI views will be updated in real-time in the `Canvas` on the right side of the screen. If for any reason you donât see the Canvas interface, or you would like to hide it to save screen space you can enable/disable it by clicking the `Editor` menu and selecting `Canvas`.

![](https://i.imgur.com/KflRwZS.png)
![](https://i.imgur.com/sQJsyhz.png)
## Running Our DApp On The Simulator

Xcode includes simulators for all currently supported Apple devices including iPhone, iPad, Apple Watch, and Apple TV. Simulators are useful for testing your application on various devices however, it is always recommended to test on a physical device before deploying an application to the App Store. The simulator is a full-fledged virtual environment that mimics an Apple device, allowing developers to test their apps, while Xcode previews provide a lightweight, real-time preview of SwiftUI user interfaces directly within the Xcode editor.

To launch the simulator simply select a device from the drop-down list, then press the âplayâ button.

![](https://i.imgur.com/16Sc44o.png)

Once the simulator loads, it will automatically install and launch our DApp. Hopefully, it will look something like this:

![](https://i.imgur.com/T1ask9Rl.png)
## Storing Our iOS DApp On GitHub

As we wrap up this section, letâs talk about GitHub, an indispensable tool for developers like us. GitHub provides a centralized platform to store and manage our code, allowing easy tracking of our projectâs progress. Whether youâre working on personal projects or collaborating with a team, GitHub streamlines code sharing and version control.

> If you donât have a GitHub account yet, [you can sign up here](https://github.com/).

Letâs take the code weâve developed for our iOS app and add it to our own GitHub repository. In other words, we will âpushâ our code to GitHub, ensuring it is safely stored and accessible.

### Create A New Repository

In Git, a repository is like a container for our project.

1. Go to <https://github.com/new> and name your project âbeginner-emerald-dappâ
2. Set the repository visibility to âpublic.â
3. Click âCreate repository.â

You will now be taken to a page with no files inside of it. It should look like this:

![](/courses/beginner-dapp/empty-github.png)
### Pushing to Our Repository

Letâs now add (or âpushâ) our iOS app code to GitHub. Open up a terminal on your computer and make sure youâre in the base directory of your project.

> Run the following lines of code:

bash
```
		
			git add .
git commit -m "Initial commit: Adding my iOS app code"
git branch -M main
git remote add origin [THE URL OF YOUR GITHUB REPOSITORY]
git push -u origin main
		 
	
```

Replace [THE URL OF YOUR GITHUB REPOSITORY] with the actual URL of your newly created GitHub repository.

If this is your first time pushing to GitHub, it may prompt you to log in. After completing the push, you can visit your GitHub repository to verify that all your code is there, securely stored and ready for future development!

![](https://i.imgur.com/UZPdhw3.png)
### Making Changes

Now, what if we make changes to our code? How do we put it on GitHub?

When you make a change in your code and save the file, you can push it to GitHub by running:

bash
```
		
			git add .
git commit -m "you can put any message about the code changes here"
git push origin main
		 
	
```
## Conclusion

All we wanted you to do today was create the Xcode project and run the application on the simulator. If you could successfully do that, woo! You will have no problem with the Quest.

In tomorrowâs content, we will explain what all the code is actually doing, and make some changes.

## Quests

For your quest today, you have one task:

1. What is the difference between front-end and back-end? Can you provide a real-life example? Note: You canât use the example in this chapter.
2. What is the difference between the Preview and running the application on the Simulator?
3. Take a screenshot of the application running on the Simulator and upload it to your quest submissions.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter2/lesson1.md)


[Exploring the Flow Blockchain & Cadence](/en/catalog/courses/beginner-dapp-ios/chapter1/lesson2)
[Learning Frontend Code](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson2)

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



