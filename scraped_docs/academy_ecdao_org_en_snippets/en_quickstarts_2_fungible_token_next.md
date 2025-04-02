# Source: https://academy.ecdao.org/en/quickstarts/2-fungible-token-next

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Fungible Token

# Fungible Token

Quickstart

Next.js

React.js

Create your own fungible token and transfer them to another account on Flow Testnet.

## ð© Quickstart 2: Fungible Token

ð« Deploy a FungibleToken contract to learn the basics of the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Next.js app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that lets users create their own fungible token and transfer them to another account on Flow testnet.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¹ Video Walkthrough

Want a video walkthrough? Check out Jacob Tuckerâs walkthrough here:

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/2-fungible-token.git
		 
	
```

> in a terminal window, ð± install the dependencies start your frontend:

sh

```
		
			cd 2-fungible-token
npm install
npm run dev
		 
	
```

> in a second terminal window, start your ð·â local emulator:

bash

```
		
			cd 2-fungible-token
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash

```
		
			cd 2-fungible-token
flow project deploy
flow dev-wallet
		 
	
```

> You can `flow project deploy --update` to deploy a new contract any time.

ð± Open http://localhost:3000 to see the app

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð Checkpoint 2: Reading Your Balance

> When you log in, click the little spinner next to your balance in the top right. Notice that you get an error:

![error when getting balance](https://i.imgur.com/IIXjt8h.png)

The reason for this is because we havenât set up a vault in the userâs account. On Flow, you need a vault in your account to be able to store specific tokens. Letâs set that up that now.

> Click the `Setup Vault` button:

![setup vault for user account](https://i.imgur.com/4XEwntp.png)

This will set up the userâs account so it can receive tokens.

> Try refreshing the balance again. You will see a balance of 0.0. So letâs mint some tokens!

## âï¸ Checkpoint 3: Minting Fungible Tokens

> In a terminal, run `npm run mint 0xf8d6e0586b0a20c7 30.0`.

![mint fungible tokens](https://i.imgur.com/hTEzmqe.png)

This will mint 30 tokens to their address (`0xf8d6e0586b0a20c7`).

> Go back to your application and refresh the balance again. Notice that you have a balance of 30.0 now! Woooohoooo.

## ð Checkpoint 4: Setup Second User Vault

We want to transfer tokens to another account, but the problem is we donât have another account (that is set up properly) to transfer tokens to!

> Log out of the current account and login to another account. Refresh the balance again. You will see an error appear:

![error when getting tokens](https://i.imgur.com/hmS1eYZ.png)

Again, this is because we havenât set up the userâs account. We will do this again by clicking the `Setup Vault` button:

![setup vault for user account](https://i.imgur.com/4XEwntp.png)

This will set up the userâs account so it can receive tokens.

> Try refreshing the balance again. You will see a balance of 0.0. So letâs transfer some from the other account!

## ð¾ Checkpoint 5: Transfer Tokens

> ð Log out of your account and go back to the Service Account. In the main box, put `0x179b6b1cb6755e31` as the recipient and `10.0` as the amount, then click `Transfer Tokens`:

![transfer tokens](https://i.imgur.com/guxcLRz.png)

This will transfer tokens to the `0x179b6b1cb6755e31` account. Log in to that account, refresh the balance, and you will see you have 10.0 tokens now!

## ð¾ Checkpoint 6: Deploy it to testnet!

ð Ready to deploy to a public testnet?!?

> ð Generate a **deployer address** by typing `flow keys generate --network=testnet` into a terminal. Make sure to save your public key and private key somewhere, you will need them soon.

![generate key pair](https://i.imgur.com/jU9sRiL.png)
> ð Create your **deployer account** by going to <https://testnet-faucet.onflow.org/>, pasting in your public key from above, and clicking `CREATE ACCOUNT`:

![configure testnet account on the website](https://i.imgur.com/OitvEoO.png)
> After it finishes, click `COPY ADDRESS` and make sure to save that address somewhere. You will need it!

> â½ï¸ Add your new testnet account to your `flow.json` by modifying the following lines of code. Paste your address you copied above to where it says âYOUR GENERATED ADDRESSâ, and paste your private key where it says âYOUR PRIVATE KEYâ.

json

```
		
			{
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

> ð Deploy your ExampleToken smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/iTqfXeg.png)
> Lastly, configure your .env file to point to Flow TestNet so we can interact with your new contract.

In your .env file, change the following:

1. `NEXT_PUBLIC_CONTRACT_ADDRESS` to your generated testnet address
2. `NEXT_PUBLIC_STANDARD_ADDRESS` to `0x9a0766d93b6608b7`
3. `PRIVATE_KEY` to your private key
4. `NEXT_PUBLIC_ACCESS_NODE` to `https://rest-testnet.onflow.org`
5. `NEXT_PUBLIC_WALLET` to `https://fcl-discovery.onflow.org/testnet/authn`

You can now terminate all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Letâs try out our DApp on testnet:

1. Run `npm run dev` to start your application in a terminal.
2. On http://localhost:3000/, click âconnectâ and log in to your Blocto or Lilico wallet, making sure to copy the address you log in with.
3. Click âSetup Vaultâ to give yourself a vault and the ability to store tokens
4. In a terminal, run `npm run mint [THE ADDRESS OF THE ACCOUNT YOU'RE LOGGED IN TO] [AMOUNT OF TOKENS]`
5. In your terminal, you should see a printed âTransaction Idâ. If you go to [Testnet Flowdiver](https://testnet.flowdiver.io) and paste in that Transaction Id, you should see information about that minting transaction.
6. Refresh the balance once again, and you should see tokens minted to your account :)

## ð Make Edits!

ð You can also check out your smart contract `ExampleToken.cdc` in `flow/cadence/ExampleToken.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `index.js` in `pages/index.js`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/3-nft-minting-next).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/2-fungible-token/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/2-fungible-token-next/en/readme.md)



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