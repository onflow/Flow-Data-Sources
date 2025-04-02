# Source: https://academy.ecdao.org/en/quickstarts/2-fungible-token-svelte

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Fungible Token

# Fungible Token

Quickstart

SvelteKit

Create your own fungible token and transfer them to another account on Flow Testnet.

## ð© Quickstart 2: Fungible Token

ð« Deploy a FungibleToken contract to learn the basics of the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template SvelteKit app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that lets users create their own fungible token and transfer them to another account on Flow Testnet.

ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/en/download)
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) - you know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/2-fungible-token-svelte.git
		 
	
```

First, rename the `.env.example` file to `.env`

Then, in a terminal window, install the dependencies and start your frontend:

sh

```
		
			cd 2-fungible-token-svelte
npm install
npm run dev
		 
	
```

In a second terminal window, start your local emulator:

bash

```
		
			cd 2-fungible-token-svelte
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

In a third terminal window, deploy your contract and start your local wallet:

bash

```
		
			cd 2-fungible-token-svelte
flow project deploy
flow dev-wallet
		 
	
```

You can `flow project deploy --update` to deploy a new contract or update your existing `ExampleToken` contract any time.

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

Click the âConnectâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð³ï¸ Checkpoint 2: Set up your Vault

After logging in to the account with address `0xf8d6e0586b0a20c7`, click the `Setup Vault` button.

This will store an empty token Vault inside of your accountâs storage so you have the ability to receive tokens.

## âï¸ Checkpoint 3: Minting Tokens

Now that we have set up your account, we can mint some tokens to it.

In a terminal, run `npm run mint 0xf8d6e0586b0a20c7 10`

This will mint 10 tokens to the supplied address (`0xf8d6e0586b0a20c7`).

## ð Checkpoint 4: See Your Tokens

Go back to your application and click `Get Balance`. Notice that your vault appears below! Wooooohooooo.

## ð Checkpoint 5: Setup Another User

Log out of the current account and connect to another account. Set up another token Vault.

## ð¾ Checkpoint 6: Transfer Tokens

Log out of your account and go back to the first account that has the tokens. After clicking âGet Balanceâ again, go to your vault below, copy and paste the address of the 2nd account you set up (ex. `0x045a1763c93006ca`), input an amount to transfer, and click `Transfer`.

This will transfer tokens to the 2nd account. Log in to that account, click `Get Balance`, and you will see it has tokens now!

## ð Checkpoint 7: Create a Testnet Account

Create a new account by opening up a terminal in the same directory as your project and typing `flow accounts create`.

* Name: `testnet-account`
* Network: `Testnet`

Open up your flow.json file and you should see under the âaccountsâ object that it automatically configured a testnet-account for you.

> â ï¸ Make sure `testnet-account.pkey` is inside your .gitignore. You never want to commit private keys to git!

## ð¾ Checkpoint 8: Deploy to Testnet!

We will now deploy our contracts to the account we just created.

In your flow.json file, under the âdeploymentsâ object, add the following:

json

```
		
			"testnet": {
  "testnet-account": [
    "ExampleToken"
  ]
}
		 
	
```

Then, under the âcontractsâ object, find the âExampleTokenâ object and add a new testnet alias. The address you put should be the same one that was added to your flow.json automatically under the âtestnet-accountâ object:

json

```
		
			"ExampleToken": {
  "source": "./src/lib/flow/cadence/contracts/ExampleToken.cdc",
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
		"ExampleToken": {
			"source": "./src/lib/flow/cadence/contracts/ExampleToken.cdc",
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
				"ExampleToken"
			]
		},
		"testnet": {
			"testnet-account": [
				"ExampleToken"
			]
		}
	}
}
		 
	
```

ð Deploy your ExampleToken smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/iTqfXeg.png)

In your .env file, change the following:

1. `PUBLIC_FLOW_NETWORK=testnet`
2. `PRIVATE_KEY` to the private key of the testnet account you created. It should be in the `testnet-account.pkey` file. **You must remove the `0x` from the beginning of the private key for it to work.**

You can now stop all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Run `npm run dev` to start your application in a terminal, and have a blast with your DApp!

## ð Make Edits!

ð You can also check out your smart contract `ExampleToken.cdc` in `flow/cadence/ExampleToken.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `+page.svelte` in `src/routes/+page.svelte`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/3-nft-minting-next).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/2-fungible-token/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/2-fungible-token-svelte/en/readme.md)



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