# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter2/lesson4

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

# Chapter 2 Lesson 4 - Finishing the Skeleton

In this lesson, we will finalize the base skeleton of our Mobile DApp so that we can focus purely on the blockchain-related tasks in Chapter 3.

## Adding A Sign-In View

What is a mobile app without a sign-in view? Letâs go ahead and create one:

1. Right-click on the `EmeraldDApp` folder in Xcode, then click new file.
2. On The new file screen, ensure âSwiftUIâ is selected then click `Next`.
3. Letâs name the file `SignInView` and click `Create`.
4. Our project view is starting to look a little crowded, letâs create a `Group` to hold our views. Holding down the command key to the left of the keyboard, select both the `ContentView` and `SignInView` before right-clicking then selecting âNew Group from Selectionâ. We will name the group `Views`

![](https://i.imgur.com/I1UI3qR.gif)

Replace the boilerplate code with the below:

swift

```
		
			import SwiftUI

struct SignInView: View {
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
                .aspectRatio(contentMode: .fit)
                .padding(.bottom, 100)

            Button {
                // TODO: Sign in logic
            } label: {
                Text("Sign In")
                    .font(.title2)
            }
                .frame(maxWidth: .infinity, maxHeight: 40)
                .background(Color.green)
                .cornerRadius(15)
                .buttonStyle(PlainButtonStyle())


        }
        .padding(.horizontal, 10)
    }
}

struct SignInView_Previews: PreviewProvider {
    static var previews: some View {
        SignInView()
    }
}
		 
	
```

Assuming you completed all of the above steps, it should look like this:

![](https://i.imgur.com/n2gvsoV.png)

## Keeping Our Code DRY

This looks great, but you may notice we had to rewrite the exact same code for the button as we have in our `ContentView`â¦ Ok so we replicated more code than just the button, but we will make further changes to our `ContentView` removing the other code later in this lesson.

DRY coding stands for âDonât Repeat Yourself.â Itâs a principle in software development that encourages developers to avoid duplicating code in a program. Instead of writing the same code multiple times, we strive to create reusable and modular components, functions, or classes. This helps make our code more efficient, easier to maintain and reduces the risk of introducing bugs. By following DRY principles, we can save time and effort in the long run, leading to more reliable and maintainable software.

Using the same steps as we used for creating the `SignInView`, create a new SwiftUI file named `ButtonView` inside of the Views directory. Replace the boilerplate code with the following:

swift

```
		
			import SwiftUI

struct ButtonView: View {
    var title: String
    var action: () -> Void

    var body: some View {
        Button {
            action()
        } label: {
            Text(title)
                .font(.title2)
        }
            .frame(maxWidth: .infinity, maxHeight: 40)
            .background(Color.green)
            .cornerRadius(15)
            .buttonStyle(PlainButtonStyle())
    }
}

struct ButtonView_Previews: PreviewProvider {
    static var previews: some View {
        ButtonView(title: "Button View", action: {})
    }
}
		 
	
```

This SwiftUI code defines a custom ButtonView that takes a title string and an action closure. The view displays a button with the provided title, and when the button is tapped, the specified action is executed. The button has a green background, rounded corners, and a fixed height. The font size of the title text is set to .title2. The ButtonView also includes a preview provider to display a live preview, since we have two variables that have not been initiated we must provide values for them in the preview view.

Now letâs update the Button in our `ContentView` and `SignInView` files, replace the `Button` views with the below.

`SignInView`:

swift

```
		
			ButtonView(title: "Sign In", action: {
	// TODO: Sign in logic
})
		 
	
```

`ContentView`:

swift

```
		
			ButtonView(title: "Hello", action: {
	print(inputText)
})
		 
	
```

## Creating A View Router

Now that our main views are set up, we need to create a view router to programmatically navigate between them. Create another new SwiftUI file in our Views directory called `RouterView`, and replace the boilerplate with the following code:

swift

```
		
			import SwiftUI

struct RouterView: View {
    @State var loggedIn: Bool = false

    var body: some View {
        ZStack {
            Group {
                if !loggedIn {
                    SignInView()
                } else {
                    ContentView()
                }
            }
            .padding(.horizontal, 10)
        }
    }
}

struct RouterView_Previews: PreviewProvider {
    static var previews: some View {
        RouterView()
    }
}
		 
	
```

Letâs review the code that is new to this example:

1. `ZStack {...}`: This creates a `ZStack` (z-index stack) container. In SwiftUI, a `ZStack` allows views to be stacked on top of each other, and the order of the views determines their visibility.
2. `Group {...}`: This creates a `Group` container. In SwiftUI, a `Group` is used to group views together. It is useful for conditionally showing different views based on conditions or applying the same modifiers to multiple views.
3. `if !loggedIn {...} else {...}`: This is a conditional statement that checks whether `loggedIn` is false, the â!â is a shorthand for âif falseâ. If `loggedIn` is false, it displays the `SignInView()`; otherwise, it displays the `ContentView()`.

Here is what it looks like in Xcode:

![](https://i.imgur.com/mKHqOFQ.png)

As you can see, while the above code works, there is now too much horizontal padding. Remember from our earlier lesson that modifiers are applied in hierarchical order, this also applies to modifiers used across views. To fix this we need to remove the horizontal padding from our VStacks in `SignInView` and `ContentView`. Once completed you can check to ensure everything looks good by changing the value of `loggedIn` from `false` to `true` and watching the preview update.

![](https://i.imgur.com/5hEPCo4.gif)

### Linking It All Together

Great work! Now we have a view router that can switch between the `SignInView` and `ContentView` based on the `loggedIn` status in our DApp. But how do we update this variable from our other views?

One option is to use another property wrapper called `@Binding`. Just like the `$` we added to our TextField variable in a previous lesson, the `@Binding` property wrapper binds a variable across views so either view can read or write to the contents of a variable. To see how this works letâs add a new variable to our `SignInView`, add the following just above the `body`

swift

```
		
			@Binding var loggedIn: Bool
		 
	
```

We also need to update our `ButtonView` action to update the variable.

swift

```
		
			ButtonView(title: "Sign In", action: {
	loggedIn = true
})
		 
	
```

> Note: Passing a binding value to a struct in the preview content can be difficult. The easiest way to to avoid erros is to change the view listed in the preview to our `RouterView` like so:

swift

```
		
			struct SignInView_Previews: PreviewProvider {
    static var previews: some View {
        RouterView()
    }
}
		 
	
```

We also need to update the `SignInView` initialization inside our `RouterView` so that it includes the loggedIn variable.

swift

```
		
			...
Group {
	if !loggedIn {
		SignInView(loggedIn: $loggedIn)
	} else {
		ContentView()
	}
}
...
		 
	
```

> Fun Fact: We can actually test this directly within preview without needing to run the simulator. Go ahead and press the âSign Inâ button in the preview and see what happensâ¦

![](https://i.imgur.com/3xsqQme.gif)

To reset the view, simply open another file and then go back to our `SignInView` file as shown above.

The last thing we need to do is update our `EmeraldDAppApp` file to load the `RouterView` directly:

swift

```
		
			struct EmeraldDAppApp: App {
    var body: some Scene {
        WindowGroup {
            RouterView()
        }
    }
}
		 
	
```

## Making It Less Ugly

Our DApp Skeleton is really starting to come together!! The only problem is that it is kind of ugly! Letâs start making it look nice by changing the colors and refactoring the `ContentView`

### Creating Custom Colors

Xcode makes it super simple for us to create custom colors that can be applied to views:

1. Open our `Assets` file in Xcode, then right-click in the blank space below the `emerald_logo` file.
2. Select `New Color Set`, and name the color `defaultBackgroundColor`.
3. If necessary, press the button in the upper right corner of Xcode to show the attribute settings.
4. Click the `Appearances` dropdown and select `None`.
5. You may need to click on the white `Universal` image, then update the `Hex` value under Color to `#011E30`

![](https://i.imgur.com/CYPh7XV.gif)

Now create three more custom colors:

1. `defaultTextColor` with a Hex value of `#1E3A8A`
2. `defaultAccentColor` with a Hex value of `#38E8C6`
3. `secondaryAccentColor` with a Hex value of `#00344B`

While we can access these colors by passing the name as a parameter to the `Color` view, that is prone to errors and is frankly a pain the a\*\*. The good news is we can add something called an `extension` to make our custom colors work the same way as the system colors.

Create a new SwiftUI file called `Colors` and replace the boilerplate with the following code:

swift

```
		
			import SwiftUI

extension Color {
    static let defaultBackgroundColor = Color("defaultBackgroundColor")
    static let defaultTextColor = Color("defaultTextColor")
    static let defaultAccentColor = Color("defaultAccentColor")
    static let secondaryAccentColor = Color("secondaryAccentColor")
}
		 
	
```

Now we can access our custom colors using the âdotâ notation `Color`.defaultTextColor` and Xcode will prefill the values for us!!

### App Wide Background Color

Rather than adding a background color to each view, we can use our `ZStack` in the `RouterView` to apply the background to the entire app. Add the following code above the `Group` view:

swift

```
		
			...
ZStack {
	Color.defaultBackgroundColor
		.ignoresSafeArea()

    ...
}
		 
	
```

### Refactoring `ContentView`

The DApp we are building is one where you can change a âGreetingâ value inside our contract, and then display it to the public. Letâs refactor our code in `ContentView` to provide a display for this data. Replace the code in `ContentView` with the following code:

swift

```
		
			import SwiftUI

struct ContentView: View {
    @State var greetingDisplay = ""
    @State var inputText = ""

    var body: some View {
        VStack {
            HStack(spacing: 6) {
                Image("emerald_logo")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .frame(width: 40)
                Text("Emerald DApp")
                    .font(.title)
                    .foregroundStyle(Color.defaultAccentColor)
            }

            Text(greetingDisplay)
                .font(.title)
                .frame(maxWidth: .infinity, maxHeight: 200)
                .foregroundStyle(Color.white)
                .background(Color.secondaryAccentColor)
                .cornerRadius(15)
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color.defaultAccentColor, lineWidth: 3)
                )
                .padding(.bottom, 20)

            TextField("Change Greeting", text: $inputText)
                .foregroundStyle(Color.white)
                .frame(maxWidth: .infinity, maxHeight: 50)
                .background(Color.secondaryAccentColor)
                .cornerRadius(15)
                .padding(3)
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color.defaultAccentColor, lineWidth: 3)
                )
                .padding(.bottom, 4)

            ButtonView(title: "Change Greeting", action: {
                print(inputText)
            })

            Spacer()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        RouterView()
    }
}
		 
	
```

Letâs go ahead and run things in the simulator now to ensure everything is working!

![](https://i.imgur.com/GQOPEkh.gif)

Wow! Things are starting to look much better! There is still more work to be done but you will complete most of that in your Quests

## Conclusion

That is all we have for Chapter 2. In this Chapter, we learned about Swift and SwiftuI. These are the foundational elements weâll need to actually start learning about integrating Blockchain code into our DApps.

If you struggled with Chapter 2, I would recommend checking out introductory SwiftUI courses. They will help you understand all of this foundational stuff.

In Chapter 3, we will start exploring some blockchain code.

## Quests

1. Update the background color of your `ButtonView` to use the `defaultAccentColor`.
2. Update the `Text` of your `ButtonView` to âdefaultTextColorâ.
3. Update the âWelcome toâ text in your `SignInView` to white.
4. Update the âEmerald DApp!â text in your `SignInView` to use the `defaultAccentColor`.
5. Add another `ButtonView` to the bottom of your `ContentView`, the action should set the `loggedIn` variable in your `RouterView` to `false`.

To upload your quests, show us your code for the modified files.

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter2/lesson4.md)

[Adding Interactivity To Our DApp](/en/catalog/courses/beginner-dapp-ios/chapter2/lesson3)
[Our First Smart Contract](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson1)



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