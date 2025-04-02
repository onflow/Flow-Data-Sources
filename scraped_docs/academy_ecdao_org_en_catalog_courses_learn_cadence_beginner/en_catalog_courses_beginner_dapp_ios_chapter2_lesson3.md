# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter2/lesson3

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

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

# Chapter 2 Lesson 3 - Adding Interactivity To Our DApp

> Before we proceed, ensure that you have completed all the previous tasks as they are essential for continuing at this point.

## Adding A Button

Open up your `ContentView` file in Xcode and add the code below between the `Image` and `Spacer()` views to add a button to our DApp.

swift

```
		
			Button {
	print("Hello There! Isn't SwiftUI super simple to use?")
} label: {
	Text("Hello")
		.font(.title2)
}
	.frame(maxWidth: .infinity, maxHeight: 40)
	.background(Color.green)
	.cornerRadius(15)
	.buttonStyle(PlainButtonStyle())
		 
	
```

This SwiftUI code creates a button with the label âHelloâ and sets the font size to .title2. The button is then styled with a green background and rounded corners. When the button is tapped, it will print the message âHello There! Isnât SwiftUI super simple to use?â to the console.

Here is a breakdown of the code:

1. **Button**: This creates a button view in SwiftUI. It takes two closures: the first closure contains the action to be performed when the button is tapped, and the second closure contains the content of the button (i.e., the label). In this case, the buttonâs action is to print the given message when tapped.
2. **print(âHello There! Isnât SwiftUI super simple to use?â)**: This line is the action closure for the button. It prints the message âHello There! Isnât SwiftUI super simple to use?â to the console when the button is tapped.
3. **label**: This is a label closure that provides the content for the button. It contains a Text view with the text âHelloâ and sets the font to .title2, which is a predefined text style in SwiftUI.
4. **.frame(maxWidth: .infinity, maxHeight: 40)**: This modifier sets the frame size of the buttonâs content. The buttonâs width will be set to the maximum available width, and the height will be limited to 40 points.
5. **.background(Color.green)**: This modifier sets the background color of the button to green.
6. **.cornerRadius(15)**: This modifier adds rounded corners to the button, with a corner radius of 15 points. This gives the button a visually appealing appearance.
7. **.buttonStyle(PlainButtonStyle())**: This modifier applies a button style to the button. In this case, `PlainButtonStyle()` is used, which is a simple and unstyled button.

---

> Now that we have added the button your Preview should look like this:

![](https://i.imgur.com/FM6IGOL.png)


---

Cool! Now letâs run our DApp in the simulator to see what happens when you press the button.

In Xcode, press the play button to build and run the application on the simulator. Keep in mind that this may take a few minutes to launch the simulator depending on how powerful of a Mac you are using.

When you launch an application in the simulator an output âconsoleâ pops up at the bottom of your Xcode project, this allows you to see any outputs or errors from the running application. Go ahead and click the âHelloâ button on the simulator and watch what gets printed to the console. It should look something like this:

> Note: I am using a beta version of Xcode that prints addtional information about how the simulator is responding to events/actions, you may not see any of the text highlighted in yellow.

![](https://i.imgur.com/eLrVFch.png)

Usually, developers use the console to print error messages or debug their code when they donât know what is wrong. In this case, we used it just to make sure things were working.

## Adding A Text Field

Now that we have a working button, letâs add a text field so the user can enter a prompt for the button to print instead of the statically defined text we currently have. To add a text field we first need to add a variable that will hold the input text. To do this add the below code just above the `body` of our `ContentView`:

swift

```
		
			@State var inputText = ""
		 
	
```

Overall this is fairly self-explanatory, we create a `var` or variable named `inputText` and initialize it with an empty string. However, notice the `@State` before the variable declaration. SwiftUI provides various âProperty Wrappersâ such as `@State` that enhance the functionality of our code, in particular, the `@Stateâ property wrapper allows SwiftUI to track and update the value of a variable as it changes. It is often used for storing and managing the state of user interface elements since any time its value changes the view is updated to reflect the new value.

Now letâs add the text field itself, place the below code just above the button we created earlier:

swift

```
		
			TextField("Change Greeting", text: $inputText)
	.frame(maxWidth: .infinity, maxHeight: 50)
	.cornerRadius(15)
	.padding(3)
	.overlay(
		RoundedRectangle(cornerRadius: 15)
			.stroke(Color.black, lineWidth: 3)
	)
	.padding(.bottom, 4)
		 
	
```

This SwiftUI code creates a customized TextField with the placeholder text âChange Greeting.â The text field has a black border with rounded corners, and padding around the content. The height of the text field is limited to 50 points. When the user types into the text field, the value will be bound to the inputText variable.

Here is a breakdown of the code:

1. **TextField(âChange Greetingâ, text: $inputText)**: This creates a `TextField` view in SwiftUI. It displays a text input field where the user can type text. The first parameter is a placeholder text that will be displayed inside the text field when there is no user input. The second parameter, text, is a âbindingâ to the `inputText` property we discussed in the previous breakdown. Notice the â$â in front of it, this is what creates the âbindingâ and allows the text field to read and write the value of the inputText variable.
2. **.frame(maxWidth: .infinity, maxHeight: 50)**: This modifier sets the frame size of the `TextField`. The width will be set to the maximum available width, and the height will be limited to 50 points.
3. **.cornerRadius(15)**: This modifier adds rounded corners to the `TextField`, with a corner radius of 15 points. This gives the text field a visually appealing appearance.
4. **.padding(3)**: This adds padding around the TextFieldâs content. The text fieldâs content will be indented by 3 points from all sides.
5. **.overlay(RoundedRectangle(cornerRadius: 15).stroke(Color.black, lineWidth: 3))**: This modifier adds an overlay to the `TextField`. It creates a `RoundedRectangle` with a corner radius of 15 points and adds a black stroke (border) with a line width of 3 points around the `TextField`. This creates a border around the text field.
6. **.padding(.bottom, 4)**: This adds additional padding at the bottom of the TextField. The content below the TextField will be pushed down by 4 points.

Notice that we have added the `.padding`(â¦)`modifier twice. It is important to note that the order of the modifiers is extremely important in SwiftUI as they are applied in the same order by the system when displaying the view itself. In the above`TextField` the first padding modifier is adding a small amount of padding around the text that is inputted and the border created by the overlay modifier. Whereas the second padding modifier creates padding between the entire generated view and the content below it.

## Updating Our Buttonâs Action

Now we can make a quick change to the action of our button so it prints the inputted text instead of the static text value. To do this all we need to do is replace the text inside the `print(...)` function with the variable we created like so:

swift

```
		
			Button {
	print(inputText)
} label: {
	Text("Hello")
		.font(.title2)
}
	.frame(maxWidth: .infinity, maxHeight: 40)
	.background(Color.green)
	.cornerRadius(15)
	.buttonStyle(PlainButtonStyle())
		 
	
```

Since the `print(...)` function only reads from the `inputText` variable there is no need to use â$â in front of it to create a binding with the variable.

The complete code should look like this:

swift

```
		
			import SwiftUI

struct ContentView: View {
    @State var inputText = ""

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

            TextField("Change Greeting", text: $inputText)
                .frame(maxWidth: .infinity, maxHeight: 50)
                .cornerRadius(15)
                .padding(3)
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color.black, lineWidth: 3)
                )
                .padding(.bottom, 4)

            Button {
                print(inputText)
            } label: {
                Text("Hello")
                    .font(.title2)
            }
                .frame(maxWidth: .infinity, maxHeight: 40)
                .background(Color.green)
                .cornerRadius(15)
                .buttonStyle(PlainButtonStyle())

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

Now press the play button again to run the updated code in the simulator. Note this time you are prompted to replace the previous build of the application, go ahead and select `Replace` on the prompt.

![](https://i.imgur.com/Tqvg13U.png)

Once the application is launched on the simulator click into the `TextField` to type some text, then press the âHelloâ `Button` to print it to the console. If everything is working correctly it should look like the below:

![](https://i.imgur.com/6GrWxvh.gif)

## Conclusion

Thatâs all for today!

Tomorrow, we will finish the base skeleton of our DApp.

## Quests

Today, we are making the Quests a little more challenging. We have covered all the concepts needed in todayâs lesson however, I didnât cover exactly how to complete them below. Donât worry a thorough review of the code breakdowns should give you everything you need to figure it out, and if you have any questions or problems feel free to reach out in Discord!

1. Currently, our view spans the entire width of the screen, see if you can add a modifier to the `VStack` that creates âhorizontalâ padding, giving the entire view some padding around the left and right edges.
2. Add some code to the button action that assigns an empty string to the `inputText` variable after it prints the user input.

To submit your quests, take a picture of both the screen and the console logs in the developer console.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter2/lesson3.md)

[Learning Frontend Code](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson2)
[Finishing the Skeleton](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson4)



[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

Built by Emerald City DAO.  
[Join us](https://discord.gg/emerald-city-906264258189332541) on our mission to build the future #onFlow

##### Pages

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)


##### Emerald City Tools

[* Emerald Academy](https://academy.ecdao.org/)[* Touchstone](https://touchstone.city/)[* FLOAT](https://floats.city/)[* Emerald Bot](https://bot.ecdao.org/)[* Link](https://link.ecdao.org/)[* Run](https://run.ecdao.org/)


##### 33 Labs Tools

[* Drizzle](https://drizzle33.app/)[* Flowview](https://flowview.app/)[* Bayou](https://bayou33.app/)

[Join the community](https://discord.gg/emerald-city-906264258189332541)