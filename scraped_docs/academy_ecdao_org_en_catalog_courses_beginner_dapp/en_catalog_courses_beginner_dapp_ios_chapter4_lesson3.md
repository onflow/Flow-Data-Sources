# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter4/lesson3





















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

# Chapter 4 Lesson 3 - Running a Script

Today we are going to learn how to run a script on the Blockchain to read our `greeting` variable from our smart contract.

## Quick Overview of Scripts

If you remember back from Chapter 1, a script will allow us to *read* information from our smart contracts. In addition, scripts donât have any gas fees making them completely free.

We will utilize a script to read our `greeting` variable from our smart contract, which we deployed in Chapter 3 Lesson 3.

## Executing a Script using FCL

In our `ContentView` file, letâs add a function to execute a script on Flow using FCL.

> Under the `body` closure, make a new function called `getGreeting()`:

javascript
```
		
			func getGreeting() async {}
		 
	
```

Notice we added the word `async` between the parentheses and closure of the function, this is how you define an asynchronous function in Swift. This is needed since our function will be executing a script on the blockchain, then âwaitingâ for the results.

Inside your function, letâs actually execute a script using FCL by doing two things:

1. Importing `FCL` at the top of the file so we can call the `fcl.query` function:

javascript
```
		
			import FCL
		 
	
```

2. Adding this code inside the `getGreeting` function:

swift
```
		
			func getGreeting() async {
	do {
		let result = try await fcl.query(script: """
			import HelloWorld from 0xDeployer

			pub fun main(): String {
				return HelloWorld.greeting
			}
		""").decode(String.self)

		print(result)
	} catch {
		print(error)
	}
}
		 
	
```

Okay so most of this should be semi-familiar to you at this point, however, there are a few new things going on here that we need to go over:

1. `do { ... } catch { ... }`: If you recall from lesson 1, functions can âthrowâ errors, previously we gracefully ignored the error using `try?`, by using `do { ... } catch { ... }` we can actually âcatchâ the error so we can implement so form of error handing. You âdoâ the code that can throw errors in the `do` block, then âcatchâ any errors that occur in the `catch` block.
2. `let result = try await fcl.query(...).decode(...)`: Notice there is not a `?` following `try` this time, this passes any error to the `error` variable inside the `catch` block. Next, we wait for the results of `fcl.query(...).decode(...)` and assign the value to the `result` variable.
3. `script: """ ... """`: Swift allows you to create multi-line strings by using triple quotes instead of single quotes.

> Most of that is probably self explanatory but what is going on with the trailing `.decode(...)`?

Swift has an amazing library known as âCombineâ, one of its many features is allowing developers to easily define methods and structs so that data can be mutated into usable objects without having to go through the (often) lengthy decoding process manually each time. In fact, these features were so useful Apple decide to include much of Combineâs functionality directly in the main library shortly after its release.

The response object that is returned from `fcl.query()` has this `decode()` function defined in its code, which takes the value of the response object and âdecodesâ it into a `Codable` object. In this case, the response is a simple string so we just use the predefined value `String.self`.

The script that we provide to `fcl.query()` is the same script we created in Chapter 3 to read the `greeting` variable from our `HelloWorld` contract with one minor change. Since we need to find the contract itself on the blockchain, Iâve changed the import to use an âAddress Replacementâ variable called `0xDeployer`. If you recall from lesson 1 we already defined a configuration key for this variable on our `FlowManager` service. Letâs update the value of our `testAccount` variable now.

swift
```
		
			...

class FlowManager: NSObject, ObservableObject {
    static let shared = FlowManager()

    let testAccount = "YOUR TEST ACCOUNT" // UPDATE THIS WITH YOUR TEST ACCOUNT FROM CHAPTER 3

    func setup() { ... }
}
		 
	
```

Nice! Now letâs figure out how to call that function in our code so we can see if itâs working!

## Seeing our Greeting

We could make a button and call this function every time we click the button, but thatâs boring and we already know how to do that. Instead, letâs call this function every time our `ContentView` is displayed on the screen.

In lesson 1, we covered how to create a `Task` to call asynchronous functions, today we are going to expand on that using the `.task {}` SwiftUI modifier allowing us to start asynchronous work as soon as the view is shown. In the `ContentView` file add the following to the `greetingDisplay` `Text` view.

swift
```
		
			Text(greetingDisplay)
	...
	.task {
		await getGreeting()
	}
		 
	
```

If you run your app on the simulator, after signing in, you should see the value of `HelloWorld.greeting` displayed in the console. Now letâs update our `getGreeting()` function to actually update `greetingDisplay` when it is called.

swift
```
		
			func getGreeting() async {
	do {
		let result = try await fcl.query(script: """
			import HelloWorld from 0xDeployer

			pub fun main(): String {
				return HelloWorld.greeting
			}
		""").decode(String.self)

		await MainActor.run {
			greetingDisplay = result
		}
	} catch {
		print(error)
	}
}
		 
	
```

In the above code, notice how we assign the value of `result` to `greetingDisplay` inside this `await MainActor.run { ... }` function? Since async functions run in the background, we need to use this function to update any values that are defined on the main thread. Since all SwiftUI views are on the main thread, we use it here to avoid unpredictable behavior in our app such as locking up or crashing.

Now when you run your app on the simulator, you should see the value of `result` in the `greetingDisplay` `Text` view displayed on the screen.

## Conclusion

We did it! We are successfully reading from the blockchain. Here is what your `ContentView` page should look like at this point:

swift
```
		
			import SwiftUI
import FCL

struct ContentView: View {
    @Binding var loggedIn: Bool
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
                .task {
                    await getGreeting()
                }

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
                inputText = ""
            })

            Spacer()

            ButtonView(title: "Sign Out: \(fcl.currentUser?.address.hex ?? "")") {
                Task {
                    try? await fcl.unauthenticate()
                }
            }
        }
    }

    func getGreeting() async {
        do {
            let result = try await fcl.query(script: """
                import HelloWorld from 0xDeployer

                pub fun main(): String {
                  return HelloWorld.greeting
                }
            """).decode(String.self)

            await MainActor.run {
                greetingDisplay = result
            }
        } catch {
            print(error)
        }
    }
}
		 
	
```
## Quests

You have a lot of tools under your belt now, in fact much more than you think you do. Letâs see what youâre capable ofâ¦

1. Jacob deployed a contract called `SimpleTest` to an account with an address of `0x6c0d53c676256e8c`. I want you to make a button that, when clicked, executes a script to read the `number` variable from that contract. If youâre curious, you can see the contract here: <https://flow-view-source.com/testnet/account/0x6c0d53c676256e8c/contract/SimpleTest>

Submit all the code you used to call the script and the result of the script.

2. Then, I want you to remove the button, and make the script execute every time the app launches.

Submit all the code you used to do this.


![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter4/lesson3.md)


[Integrating WalletConnect and Lilco Wallet](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson2)
[Passing in Arguments to a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson4)

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



