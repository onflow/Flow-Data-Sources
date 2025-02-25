# Source: https://academy.ecdao.org/en/quickstarts/1-non-fungible-token-ios

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Non Fungible Token (NFT)

# Non Fungible Token (NFT)

Quickstart

SwiftUI

Mint NFTs and transfer them to another account on Flow Testnet.

## ð© Quickstart 1: Non-Fungible Token

ð« Deploy your own NFT contract to learn the basics of the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Swift iOS/iPadOS app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a Mobile DApp that lets users create an empty collection, mint some pre-loaded NFTs, and transfer them to another account on Flow testnet.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¹ Video Walkthrough

Coming Soon!â¦hopefully..

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

> in a terminal window, clone the project repo, install the dependencies, and open the project in Xcode:

sh

```
		
			git clone https://github.com/boiseitguru/1-non-fungible-token-ios.git
cd 1-non-fungible-token-ios
npm install
open NonFungible\ Token.xcodeproj
		 
	
```

> Next we need to copy or rename `flow.json.example` to `flow.json`.

sh

```
		
			mv flow.json.example flow.json
		 
	
```

> in a second terminal window, start your ð·â local emulator:

bash

```
		
			cd 1-non-fungible-token-ios
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash

```
		
			cd 1-non-fungible-token-ios
flow project deploy
flow dev-wallet
		 
	
```

> You can `flow project deploy --update` to deploy a new contract any time.

ð± Once the emulator and dev-wallet have been started, use Xcode to run your app on the iOS simulator. (ð§¨ FCL-Swift does not currently support using the dev-wallet on a physical iOS device.)

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a pop up asking you to connect a wallet. Select `Dev Wallet` then wait for the authentication page to load. Notice a window appears with one or more accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

![launch-screen](https://i.imgur.com/jUo8QDQl.png)
![login-page](https://i.imgur.com/830cfF1l.png)
![wallet-select](https://i.imgur.com/TWJi16hl.png)
![account-select](https://i.imgur.com/bbS1hknl.png)

---

## ð Checkpoint 2: See your NFTs

> After logging in to the account with address `0xf8d6e0586b0a20c7`, click the `Get NFTs` button. Notice that you get an error:

![get-nfts](https://i.imgur.com/FiSkeq1l.png)
![initial-error](https://i.imgur.com/9jUuQJHl.png)

The reason for this is because we havenât set up the userâs account to be able to receive NFTs. On Flow, accounts needs to have a collection in their account to store specific NFTs. Letâs set that up that now.

> Click the `Setup Collection` button, then approve the transaction:

![setup-account](https://i.imgur.com/FiSkeq1l.png)
![approve-transaction](https://i.imgur.com/iGrohdpl.png)

This will set up the userâs account so it can receive NFTs.

> Try clicking `Get NFTs`. You will see no NFTs appear. So letâs mint some NFTs!

---

## âï¸ Checkpoint 3: Minting the NFTâs

Now that we have set up the userâs account, we can mint some NFTs to it.

> In a terminal, run `npm run mint 0xf8d6e0586b0a20c7`

![mint NFTs transaction](https://i.imgur.com/N2Twynw.png)

This will mint 3 NFTs to the supplied address (`0xf8d6e0586b0a20c7`).

> Go back to your application and click `Get NFTs` again. Notice that a paged TabView with 3 NFTs appear! Woooohoooo.

![education-nft](https://i.imgur.com/Rl5rONZl.png)
![governance-nft](https://i.imgur.com/HlZRR6hl.png)
![building-nft](https://i.imgur.com/Q3QnZNFl.png)

---

## ð Checkpoint 4: Setup empty user Collection

> Log out of the current account and begin the login process again, however, this time we will be creating a new account using the dev-wallet. After the account selection screen loads press the green â+â button next to the words âCreate new Accountâ, give the account a name, then click âCREATEâ. You can now select the newly created account to login with:

![account-select](https://i.imgur.com/bbS1hknl.png)
![create-account](https://i.imgur.com/fb4hh6Vl.png)
![account-created](https://i.imgur.com/5FilEbml.png)

> Click `Get NFTs` again. You will see an error appear:

![get-nfts](https://i.imgur.com/FiSkeq1l.png)
![second-error](https://i.imgur.com/9jUuQJHl.png)

Again, this is because we havenât set up the userâs account. We will do this again by clicking the `Setup Collection` button and approving the transaction:

![setup-account](https://i.imgur.com/FiSkeq1l.png)
![approve-transaction](https://i.imgur.com/detzsD4l.png)

This will set up the userâs account so it can receive NFTs.

> Try clicking `Get NFTs`. You will see no NFTs appear. So letâs transfer some from the other account!

---

## ð¾ Checkpoint 5: Transfer an NFT

> ð Log out of your account and go back to the Service Account. In one of the NFT boxes, copy and paste `0x179b6b1cb6755e31` and click `Transfer`:

![transfer-nft](https://i.imgur.com/yMJRfQnl.png)
![approve-transaction](https://i.imgur.com/V3ptnErl.png)

This will transfer an NFT to the `0x179b6b1cb6755e31` account.

Log in to that account, click `Get NFTs`, and you will see it has an NFT now!

![received-nft](https://i.imgur.com/cnwV3Erl.png)

---

## ð¾ Checkpoint 6: Deploy it to testnet!

ð Ready to deploy to a public testnet?!?

> ð Generate a **deployer address** by typing `flow keys generate --network=testnet` into a terminal. Make sure to save your public key and private key somewhere, you will need them soon.

![generate key pair](https://i.imgur.com/Rf0f1ox.png)
> ð Create your **deployer account** by going to <https://testnet-faucet.onflow.org/>, pasting in your public key from above, and clicking `CREATE ACCOUNT`:

![configure testnet account on the website](https://i.imgur.com/mkNCf1o.png)
> After it finishes, click `COPY ADDRESS` and make sure to save that address somewhere. You will need it!

> â½ï¸ Add your new testnet account to your `flow.json` by modifying the following lines of code. Paste your address you copied above to where it says âYOUR GENERATED ADDRESSâ, and paste your private key where it says âYOUR PRIVATE KEYâ.

json

```
		
			{
	"emulators": {
		"default": {
			"port": 3569,
			"serviceAccount": "emulator-account"
		}
	},
	"contracts": {
		"NonFungibleToken": {
			"source": "./cadence/utility/NonFungibleToken.cdc",
			"aliases": {
				"testnet": "0x631e88ae7f1d7c20"
			}
		},
		"FungibleToken": {
			"source": "./cadence/utility/FungibleToken.cdc",
			"aliases": {
				"emulator": "0xee82856bf20e2aa6",
				"testnet": "0x9a0766d93b6608b7"
			}
		},
		"MetadataViews": {
			"source": "./cadence/utility/MetadataViews.cdc",
			"aliases": {
				"testnet": "0x631e88ae7f1d7c20"
			}
		},
		"ExampleNFT": "./cadence/ExampleNFT.cdc"
	},
	"networks": {
		"emulator": "127.0.0.1:3569",
		"mainnet": "access.mainnet.nodes.onflow.org:9000",
		"testnet": "access.devnet.nodes.onflow.org:9000"
	},
	"accounts": {
		"emulator-account": {
			"address": "f8d6e0586b0a20c7",
			"key": "cdb3410ae829f5e2a29f71f53efbce66bde1187948d6317de6918d5003576ca7"
		}
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
	},
	"deployments": {
		"emulator": {
			"emulator-account": ["NonFungibleToken", "MetadataViews", "ExampleNFT"]
		}
	},
	"testnet": {
		"testnet-account": ["ExampleNFT"]
	}
}
		 
	
```

Notice that we do not want to re-deploy NonFungibleToken or MetadataViews. That is because they are already deploy and live on Flow testnet!

> ð Deploy your ExampleNFT smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/9rfZNhr.png)

ð± Open `NonFungible Token.xcodeproj` in Xcode and update line 13 of `Hello World > Flow > FlowManager.swift with the newly created Testnet account so we can interact with your new contract.

swift

```
		
			import UIKit

let testAccount = "YOUR TESTNET ACCOUNT"

class FlowManager: ObservableObject {
  ...
}
		 
	
```

You will also need to change the first to lines of the `setup()` function inside FlowManager to switch over to the Flow testnet, as shown below. WalletConnect has been configured for this project allowing you to use the wallet of your choice on testnet. For details on how to setup Lilico Wallet for development use on testnet, check out our course [Setting Up Lilico Wallet For Development](https://academy.ecdao.org/en/catalog/courses/setting-up-lilico-wallet-for-development)

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

## ð Make Edits!

ð You can also check out your smart contract `ExampleNFT.cdc` in `flow/cadence/ExampleNFT.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð The app is written in SwiftUI, and implements a âNo View Modelâ design. With the exception of the FlowManager service and a few UI helpers in the Misc directory, the design and direct functions can all be modified in the Views directory.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/2-fungible-token-svelte).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)

[Fork Quickstart](https://github.com/boiseitguru/1-non-fungible-token-ios/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/1-non-fungible-token-ios/en/readme.md)



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