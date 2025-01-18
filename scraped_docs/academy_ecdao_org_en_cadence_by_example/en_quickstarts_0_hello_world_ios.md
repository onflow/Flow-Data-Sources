# Source: https://academy.ecdao.org/en/quickstarts/0-hello-world-ios



















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Hello World

# Hello World


Quickstart

SwiftUI

Change and read a greeting field on Flow Testnet.



## ð© Quickstart 0: Hello World

ð« Deploy a simple HelloWorld contract to learn the basics of the Flow blockchain and Cadence. Youâll use:

* The Flow CLI & local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Swift iOS/iPadOS app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a Mobile DApp that lets users read and change a greeting field on Flow testnet. (ð§¨ WalletConnect has not been configured so `DapperSC` and `Lilico` wallets will crash the application)

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

---

## Video Walkthrough

Coming Soon!â¦hopefully..

---

## ð¦ Checkpoint 0: Install && Deploy

Required:

* [Git](https://git-scm.com/downloads)
* [Xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

> First open a terminal ð± and clone this repository. After switching to the project directory open the project in Xcode.

sh
```
		
			git clone https://github.com/BoiseITGuru/0-hello-world-ios.git
cd 0-hello-world-ios
open Hello\ World.xcodeproj/
		 
	
```
> Next we need to copy or rename `flow.json.example` to `flow.json`.

sh
```
		
			mv flow.json.example flow.json
		 
	
```
> in a second terminal window, start your ð·â local emulator:

bash
```
		
			cd 0-hello-world
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash
```
		
			cd 0-hello-world
flow project deploy
flow dev-wallet
		 
	
```
> You can `flow project deploy --update` to deploy a new contract any time.

> Once the emulator and dev-wallet have been started, use Xcode to run your app on the iOS simulator. (ð§¨ FCL-Swift does not currently support using the dev-wallet on a physical iOS device.)

---

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a pop up asking you to connect a wallet. Select `Dev Wallet` then wait for the authentication page to load. Notice a window appears with one or more accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

![launch-screen](https://i.imgur.com/jUo8QDQl.png)
![login-page](https://i.imgur.com/HyGr40al.png)
![wallet-select](https://i.imgur.com/M3olOljl.png)
![account-select](https://i.imgur.com/iDDul6Il.png)

---

## ð Checkpoint 2: Reading the Greeting

> ð Press the `Get Greeting` button to see your greeting:

![no-greeting](https://i.imgur.com/mGDpcdfl.png)
![get-greeting](https://i.imgur.com/G6Tubj4l.png)

---

## âï¸ Checkpoint 3: Changing the Greeting

> âï¸ Change the greeting! Type a new greeting into the input and press the `Change Greeting` button or the `Send` button on the keyboard. You should see a transaction pop up:

![change-greeting](https://i.imgur.com/RRoAOgMl.png)
> ð Click âAPPROVEâ and then click the `Get Greeting` button to see your new greeting:

![transaction-approval](https://i.imgur.com/5ntNrS3l.png)
![new-greeting](https://i.imgur.com/19YnQH1l.png)

---

## ð¾ Checkpoint 4: Deploy it to testnet!?

> Now ð Generate a **deployer address** by typing `flow keys generate --network=testnet` into a terminal. Make sure to save your public key and private key somewhere, you will need them soon.

![generate key pair](https://i.imgur.com/HbF4C73.png)
> ð Create your **deployer account** by going to <https://testnet-faucet.onflow.org/>, pasting in your public key from above, and clicking `CREATE ACCOUNT`:

![configure testnet account on the website](https://i.imgur.com/73OjT3K.png)
> After it finishes, click `COPY ADDRESS` and make sure to save that address somewhere. You will need it!

> â½ï¸ Add your new testnet account to your `flow.json` by modifying the following lines of code. Paste your address you copied above to where it says âYOUR GENERATED ADDRESSâ, and paste your private key where it says âYOUR PRIVATE KEYâ.

json
```
		
			"accounts": {
  "emulator-account": {
    "address": "f8d6e0586b0a20c7",
    "key": "5112883de06b9576af62b9aafa7ead685fb7fb46c495039b1a83649d61bff97c"
  },
  "testnet-account": {
    "address": "YOUR GENERATED ADDRESS",
    "key": {
      "type": "hex",
      "index": 0,
      "signatureAlgorithm": "ECDSA_P256",
      "hashAlgorithm": "SHA3_256",
      "privateKey": "YOUR PRIVATE KEY"
    }
  }
},
"deployments": {
  "emulator": {
    "emulator-account": [
      "HelloWorld"
    ]
  },
  "testnet": {
    "testnet-account": [
      "HelloWorld"
    ]
  }
}
		 
	
```
> ð Deploy your HelloWorld smart contract:

sh
```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/GBFs2Uz.png)
> You can use `flow project deploy --update` to deploy a new contract any time.

ð± Open `Hello World.xcodeproj` in Xcode and update line 13 of `Hello World > Flow > FlowManager.swift with the newly created Testnet account so we can interact with your new contract.

swift
```
		
			import UIKit

let testAccount = "YOUR TESTNET ACCOUNT"

class FlowManager: ObservableObject {
  ...
}
		 
	
```

You will also need to change the first to lines of the `setup()` function inside FlowManager to switch over to the Flow testnet, as shown below. REMINDER: ð§¨ WalletConnect has not been configured so `DapperSC` and `Lilico` wallets will crash the application.

swift
```
		
			class FlowManager: ObservableObject {
  ...
  func setup() {
      let defaultProvider: FCL.Provider = .blocto
      let defaultNetwork: Flow.ChainID = .testnet
      ...
  }
  ...
}
		 
	
```

Lastly, run the app in the simulator or on your iOS/iPadOS Device.

---

## ð Make Edits

ð You can also check out your smart contract `HelloWorld.cdc` in `cadence/HelloWorld.cdc`.

ð¼ Take a quick look at how your contract gets deployed in `flow.json`.

ð The app is written in SwiftUI, and implements a âNo View Modelâ design. With the exception of the FlowManager service and a few UI helpers in the Misc directory, the design and direct functions can all be modified in the Views directory.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/1-non-fungible-token-ios).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).


![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)




[Fork Quickstart](https://github.com/boiseitguru/0-hello-world-ios/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/0-hello-world-ios/en/readme.md)


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



