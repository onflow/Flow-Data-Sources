# Source: https://academy.ecdao.org/en/quickstarts/0-hello-world-svelte

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Hello World

# Hello World

Quickstart

SvelteKit

Change and read a greeting field on Flow Testnet.

## ð© Quickstart 0: Hello World

ð« Deploy a simple HelloWorld contract to learn the basics of the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template SvelteKit app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that lets users read and change a greeting field on Flow Testnet.

ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¹ Video Walkthrough

Want a video walkthrough? Check out Jacob Tuckerâs walkthrough here:

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/en/download)
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) - you know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/0-hello-world-svelte.git
		 
	
```

First, rename the `.env.example` file to `.env`

Then, in a terminal window, install the dependencies and start your frontend:

sh

```
		
			cd 0-hello-world-svelte
npm install
npm run dev
		 
	
```

In a second terminal window, start your local emulator:

bash

```
		
			cd 0-hello-world-svelte
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

In a third terminal window, deploy your contract and start your local wallet:

bash

```
		
			cd 0-hello-world-svelte
flow project deploy
flow dev-wallet
		 
	
```

You can run `flow project deploy --update` to deploy a new contract or update your existing `HelloWorld` contract any time.

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

Click the âConnectâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð Checkpoint 2: Reading the Greeting

Click the `Get greeting` button to see your greeting:

![get greeting](https://i.imgur.com/scGk30z.png)

## âï¸ Checkpoint 3: Changing the Greeting

Change the greeting! Type a new greeting into the input.

![changing the greeting](https://i.imgur.com/7MnrBGO.png)

Then, click the `Change greeting` button. You should see a transaction pop up:

![transaction popup](https://i.imgur.com/PMPzs15.png)

Click âAPPROVEâ and then click the `Get greeting` button again. You should now see your new greeting.

## ð Checkpoint 4: Create a Testnet Account

Create a new account by opening up a terminal in the same directory as your project and typing `flow accounts create`.

* Name: `testnet-account`
* Network: `Testnet`

Open up your flow.json file and you should see under the âaccountsâ object that it automatically configured a testnet-account for you.

> â ï¸ Make sure `testnet-account.pkey` is inside your .gitignore. You never want to commit private keys to git!

## ð¾ Checkpoint 5: Deploy to Testnet!

We will now deploy our contracts to the account we just created.

In your flow.json file, under the âdeploymentsâ object, add the following:

json

```
		
			"testnet": {
  "testnet-account": [
    "HelloWorld"
  ]
}
		 
	
```

Then, under the âcontractsâ object, find the âHelloWorldâ object and add a new testnet alias. The address you put should be the same one that was added to your flow.json automatically under the âtestnet-accountâ object:

json

```
		
			"HelloWorld": {
  "source": "./src/lib/flow/cadence/contracts/HelloWorld.cdc",
  "aliases": {
    "emulator": "f8d6e0586b0a20c7",
    "testnet": "5f4ea4877f5afeab"
  }
}
		 
	
```

Your final flow.json should look something like this:

json

```
		
			{
	"contracts": {
		"FIND": {
			"source": "./src/flow/cadence/contracts/utility/FIND.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testnet": "631e88ae7f1d7c20"
			}
		},
		"FlowToken": {
			"source": "./src/flow/cadence/contracts/utility/FlowToken.cdc",
			"aliases": {
				"emulator": "0ae53cb6e3f42a79",
				"mainnet": "1654653399040a61",
				"testnet": "7e60df042a9c0868"
			}
		},
		"FungibleToken": {
			"source": "./src/flow/cadence/contracts/utility/FungibleToken.cdc",
			"aliases": {
				"emulator": "ee82856bf20e2aa6",
				"mainnet": "f233dcee88fe0abe",
				"testnet": "9a0766d93b6608b7"
			}
		},
		"HelloWorld": {
			"source": "./src/lib/flow/cadence/contracts/HelloWorld.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"testnet": "5f4ea4877f5afeab"
			}
		},
		"MetadataViews": {
			"source": "./src/flow/cadence/contracts/utility/MetadataViews.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testnet": "631e88ae7f1d7c20"
			}
		},
		"NonFungibleToken": {
			"source": "./src/flow/cadence/contracts/utility/NonFungibleToken.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testnet": "631e88ae7f1d7c20"
			}
		}
	},
	"networks": {
		"emulator": "127.0.0.1:3569",
		"mainnet": "access.mainnet.nodes.onflow.org:9000",
		"testnet": "access.devnet.nodes.onflow.org:9000"
	},
	"accounts": {
		"emulator-account": {
			"address": "f8d6e0586b0a20c7",
			"key": "fc49a771829ff480841164af13b18a68cd697b6e79c80af7f8470a9e651dfac5"
		},
		"testnet-account": {
			"address": "5f4ea4877f5afeab",
			"key": {
				"type": "file",
				"location": "testnet-account.pkey"
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
}
		 
	
```

ð Deploy your HelloWorld smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/GBFs2Uz.png)

In your .env file, change the following:

1. `PUBLIC_FLOW_NETWORK=testnet`

You can now stop all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Run `npm run dev` to start your application in a terminal, and have a blast with your DApp!

## ð Make Edits!

ð You can check out your smart contract `HelloWorld.cdc`, transactions and scripts in `src/lib/flow/cadence`.

ð¼ Look at how FCL runs your transactions or scripts in `src/lib/flow/actions`.

ð If you want to make frontend edits, open `+page.svelte` in `src/routes/+page.svelte`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/1-non-fungible-token-svelte).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/0-hello-world-svelte/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/0-hello-world-svelte/en/readme.md)



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