# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter4/lesson5

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

# Chapter 4 Lesson 5 - Sending a Transaction

Hi! Today, we will learn how to send a transaction using FCL so we can change our greeting in our DApp.

## Quick Overview of Transactions

If you remember back from Chapter 1, a transaction will allow us to *change* information inside our smart contracts. In addition, transactions cost **gas** and require someone to **sign** the transaction and send it to the blockchain.

We will utilize a transaction to change our `greeting` variable inside our smart contract, which we deployed in Chapter 4 Lesson 3.

## Overview of What We Have So Far

Before we add the final pieces of functionality to our DApp, letâs take a look at what we have accomplished so far:

![](https://i.imgur.com/9UimLMll.gif)

This is our application. It:

1. Lets us sign in with our wallet
2. Automatically gets the greeting from the contract every time the app loads and displays it in a `TextField`.
3. Allows us to click a âChange Greetingâ button that should run a transaction, using the input we type into the box as the `newGreeting`

We must complete step 3 in order to complete our DApp.

Here is *something similar* to what your `ContentView` file should be right now, after completing the quests from the previous few lessons:

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

## Sending Transactions Using FCL

> Lets implement a `changeGreeting` function that sends a transaction to change our greeting using FCL.

Here is a snippet of a transaction:

swift

```
		
			func changeGreeting() async {
	do {
		let txId = try await fcl.mutate(
			cadence: "",
			args: []
		)
	} catch {
		print(error)
	}
}
		 
	
```

As you can see is this *almost* the same thing as executing a script, except that we are using `fcl.muate()` instead of `fcl.query()`.

> `fcl.mutate()` takes several more optional parameters, we wonât be using any of them in this course, but Iâve included an general overview of them below.

1. `gasLimit`: the gas limit of the transaction. This has a default value of 1000.
2. `proposer`: this is the *proposer* of a transaction (the person sending it to the blockchain).
3. `authorizors`: this is a list of *authorizors* of the transaction. Essentially, these are people that are saying âI am signing this transactionâ and thus grant the transaction access to their account (for example, sending an NFT, paying someone, etc). If you go through our [Beginner Cadence Course](https://academy.ecdao.org/en/catalog/courses/beginner-cadence), you will learn much more about what this means.
4. `payers`: this is a list of *payers* for the transaction. Like we mentioned, transactions cost gas. Although transactions on Flow cost basically nothing (in fact theyâre free since wallets usually cover the cost), you still need to provide someone to pay.

Parameters 2-4 all default to the current user.

> Quick side note: transactions on Flow are very unique in that they have 3 roles: a payer, proposer, and authorizor. If you want to learn more about it, go here: <https://docs.onflow.org/concepts/transaction-signing/#signer-roles>

> Letâs finsih up our DApp to see how this works in practice.

swift

```
		
			func changeGreeting() async {
	do {
		let txId = try await fcl.mutate(
			cadence: """
				import HelloWorld from 0xDeployer

				transaction(myNewGreeting: String) {

					prepare(signer: AuthAccount) {}

					execute {
					HelloWorld.changeGreeting(newGreeting: myNewGreeting)
					}
				}
			""",
			args: [
				.string(inputText)
			]
		)

		print(txId.hex)
	} catch {
		print(error)
	}
}
		 
	
```

Okay, so what did we just do?

1. We filled in our Cadence script.
2. We added an argument because our transaction takes in 1 argument: `myNewGreeting: String`. We learned how to pass in arguments in the last lesson. The value we pass in is our `inputText` variable.

> Run your DApp in the simulator and try clicking the âChange Greetingâ button now after typing something into the `TextField`. You should be able to run a transaction!

![](https://i.imgur.com/A5jsLokl.png)

If you wait for a couple minutes and sign out then back in, you will hopefully see your updated greeting displaying on the screen ;)

Letâs learn a little more about whatâs actually happening and how we can make this smootherâ¦

## What is the `transactionId`?

You may be wondering what the `transactionId` is that is being returned from your function. Well, thatâs a unique hash you can use to search for your transaction.

After you click âApproveâ on the Blocto transaction belowâ¦

![](https://i.imgur.com/A5jsLokl.png)

â¦a bunch of letters and numbers should appear in the console. This is because we `print` the `txId` in our `changeGreeting` function.

![](https://i.imgur.com/fdHvOAC.png)

A txId or âtransaction idâ can help you find information about your transaction. More specifically, you can do this on Flowdiver!

> Copy + paste that transactionId, go to <https://testnet.flowdiver.io/>, and paste it into the search bar. You should be able to discover your transaction!

![](https://i.imgur.com/IHZBBGV.png)

## Updating the Displayed Greeting After Transaction

Now that we are changing the greeting, we want to make sure our frontend reflects this change.

> Inside of `changeGreeting`, after the `print`, add these lines:

swift

```
		
			_ = try await txId.onceSealed()

await getGreeting()
		 
	
```

What this will do is take the `txId` we got from our transaction, then wait for the transaction to be completed or âsealedâ before calling the `getGreeting()` function.

## Conclusion

CONGRADULATIONS! You have officially made a Mobile DApp that sends transactions and scripts! While this is a simple Hello World example we covered many concepts across two different programming languagues, honestly geat job!!.

This also concludes the course! If you want to check out other courses, please see our main webpage: <https://academy.ecdao.org/>

## Quests

1. Clear the `TextField` once the transaction has been submitted.
2. Add two more `txId.once...` statements to our changeGreeting function, updating the `greetingDisplay` varable to show the end user when the transaction is âpendingâ, âexecutedâ, and âsealedâ.

Sumbmit a link to your Github repo with your completed Emerald DApp iOS App!!

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Quests](#quests)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter4/lesson5.md)

[Passing in Arguments to a Script](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson4)



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