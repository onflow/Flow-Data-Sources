# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter2/lesson2





















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

# Chapter 2 Lesson 2 - Learning SwiftUI

> If you have already worked with SwiftUI before, you may find this a bit boring. But itâll be really quick for you.

Hello there! In this lesson, we will be giving you an introduction to SwiftUI, Appleâs declarative user interface framework for building iOS, macOS, watchOS, and tvOS applications. This will help you understand the frontend code in our DApp.

## What Is SwiftUI?

SwiftUI is a user interface toolkit provided by Apple for building user interfaces across their platforms. Itâs a declarative way of describing the user interface and its behavior. SwiftUI is based on Swift, the programming language developed by Apple.

Views in SwiftUI define what is being displayed on your screen. In our example from the previous lessonâ¦

![](https://i.imgur.com/KflRwZS.png)

The âHello Worldâ text, and the âglobeâ image, along with their position, layout, and size on the screen are all thanks to SwiftUI.

Letâs start defining our DApps view, and then explain what all of it is actually doing.

## Remove Boilerplate Code

Letâs remove some boilerplate code (code that is there at the start that just takes up space). We will explain what everything is afterward.

> Open up your `ContentView` file in Xcode and replace everything in the file with this code:

swift
```
		
			import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            HStack {
                Text("Welcome to")
                    .font(.title)

                Text("Emerald DApp!")
                    .font(.title)
                    .foregroundStyle(Color.green)
            }
            .padding()

            Image("emerald_logo")
                .resizable()
                .frame(width: 200, height: 200)
                .padding()

            Spacer()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

		 
	
```
> Before we dive into the code, notice that in the preview window on the right, no image is displayed. This is because the Image view is looking for an image named `emerald_logo` in the `Assets` folder, lets add that now.

1. Click the link to download the image: [Download Image](https://cdn.discordapp.com/attachments/1122027331570110504/1122027809632686150/ea-logo.png) - Hint: You might need to right-click on the image and select âSave Imae Asâ depending on the browser you are using.
2. Once Downloaded selected the `Assets` folder in Xcode to simply drag and drop the downloaded image into your project.![](https://i.imgur.com/alDU945.gif)

If we go back to our `ContentView` file you should now see the image loading in the preview on the right.

![](https://i.imgur.com/GTy1Y0q.png)
## Understanding What We Just Did

> If you already understand all of that, skip this section.

Now, letâs break down the code:

* **Import SwiftUI**: The code begins with importing the SwiftUI framework, which allows us to use SwiftUI components.
* **ContentView**: A struct is defined with the name `ContentView`, which conforms to the `View` protocol. This means we are creating a view in SwiftUI.
* `var body: some View { ... }`: The `body` property represents the content of the view. It uses a closure that returns a `View`.
* **VStack**: A `VStack` is used to arrange the views vertically in a column. All views inside the `VStack` will be stacked on top of each other.
* **HStack**: Inside the `VStack`, thereâs an `HStack` used to arrange views horizontally in a row. It contains two `Text` views:
  + The first `Text` view displays âWelcome toâ. The `.font(.title)` modifier sets the font size to `.title`, which is a system-defined font size for titles.
  + The second `Text` view displays âEmerald DApp!â. The `.font(.title)` modifier also sets the font size to `.title`. Additionally, the `.foregroundStyle(Color.green)` modifier applies a green color to the text using the `Color` SwiftUI type.
* **Padding**: The `.padding()` modifier is applied to the `HStack`, which adds some padding around the horizontal stack of texts.
* **Image View**: Below the `HStack`, thereâs an `Image` view with the name âemerald\_logoâ. The `Image` initializer takes the name of an image asset in the projectâs asset catalog. The `.resizable()` modifier makes the image resizable to adapt to the frameâs size. The `.frame(width: 200, height: 200)` modifier sets the width and height of the image to 200 points. The `.padding()` modifier adds some padding around the image.
* **Spacer**: The `Spacer()` view is used to create flexible space that expands to fill the available space in a view. Being used at the bottom of `VStack` like this pushes the other views to the top of the screen.

## Learn More

Because this is not necessarily a course on Swift/SwiftUI, if youâd like to learn more about it, please check out these resources:

* <https://www.codecademy.com/catalog/language/swift>

> If you have any other resources that have helped you, and you want us to list them, please let me know!

## Quests

1. Change the color of âEmerald DAppâ to whatever color you want
2. Change the font size of the title
3. Change the `Image` view to an image of your choice.

---

Take a screenshot of your changes (both the code and the result) and upload it to your quests


![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter2/lesson2.md)


[Creating our Mobile (iOS) DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson1)
[Adding Interactivity To Our DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson3)

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



