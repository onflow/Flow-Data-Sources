# Source: https://academy.ecdao.org/en/quickstarts/3-nft-minting-next

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
NFT Minting

# NFT Minting

Quickstart

Next.js

React.js

A Next.js DApp that lets an admin create an NFT Collection and display available NFTs for purchase on a minting site. Users will be able to see their purchased NFTs as well.

## ð© Quickstart 3: NFT Minting

ð« Setup your own NFT collection and minting site while learning the basics of the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Next.js app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that lets an admin create an NFT Collection and display available NFTs for purchase on a minting site. Users will be able to see their purchased NFTs as well.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/3-nft-minting.git
		 
	
```

> in a terminal window, ð± install the dependencies start your frontend:

sh

```
		
			cd 3-nft-minting
npm install
npm run dev
		 
	
```

> in a second terminal window, start your ð·â local emulator:

bash

```
		
			cd 3-nft-minting
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash

```
		
			cd 3-nft-minting
flow project deploy
flow dev-wallet
		 
	
```

> You can `flow project deploy --update` to deploy a new contract any time.

ð± Open http://localhost:3000 to see the app

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âConnectâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## âï¸ Checkpoint 2: Minting some NFTâs

Before we allow users to purchase NFTs, we have to mint them first!

> In a terminal, run `npm run mint`

![mint NFTs transaction](https://i.imgur.com/zhxWHyY.png)

This will mint 3 NFTs and store them in the contract. They will be ready for purchasing.

> Go back to your application and refresh the page. You will now see some NFTs available for purchase!

![NFTs now appear on the frontend](https://i.imgur.com/s5uAUMW.png)

## ð Checkpoint 3: Purchase NFTs

Now that there are NFTs available for purchase, we can go ahead and buy some NFTs.

> Make sure you log in to the Service Account, since that account already has a lot of Flow Tokens to buy with.

> Click Purchase on any of the available NFTs.

![purchase nft tx](https://i.imgur.com/rOsj53Y.png)

If you click approve, you will see that the NFT successfully gets taken off the market and put under the âPurchased NFTsâ category:

![nft is now purchased](https://i.imgur.com/aMv2KOI.png)

## ð¾ Checkpoint 4: Fund an Account

Before we try to purchase with another account, we have to make sure they have enough Flow Tokens to buy with.

> Log out if you are already logged in, click âConnectâ, and click âManageâ next to Account A:

![manage button](https://i.imgur.com/7qb3yVZ.png)
> Click âFundâ a few times, and then press âSaveâ

![fund account](https://i.imgur.com/9Elc5W5.png)

Now you will have enough Flow to purchase with Account A. Try to buy an NFT!

After buying an NFT, you should notice the balance of the account decrease.

## ð¾ Checkpoint 5: Deploy it to testnet!

ð Ready to deploy to a public testnet?!?

> ð Generate a **deployer address** by typing `flow keys generate --network=testnet` into a terminal. Make sure to save your public key and private key somewhere, you will need them soon.

![generate key pair](https://i.imgur.com/Rf0f1ox.png)
> ð Create your **deployer account** by going to <https://testnet-faucet.onflow.org/>, pasting in your public key from above, and clicking `CREATE ACCOUNT`:

![configure testnet account on the website](https://i.imgur.com/mkNCf1o.png)
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
      "NonFungibleToken",
		  "MetadataViews",
		  "ExampleNFT"
	  ]
  },
  "testnet": {
    "testnet-account": [
      "ExampleNFT"
    ]
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
> Lastly, configure your .env file to point to Flow TestNet so we can interact with your new contract.

In your .env file, change the following:

1. `NEXT_PUBLIC_CONTRACT_ADDRESS` to your generated testnet address
2. `NEXT_PUBLIC_NFT_STANDARD_ADDRESS` to `0x631e88ae7f1d7c20`
3. `NEXT_PUBLIC_TOKEN_STANDARD_ADDRESS` to `0x9a0766d93b6608b7`
4. `NEXT_PUBLIC_FLOW_TOKEN_ADDRESS` to `0x7e60df042a9c0868`
5. `PRIVATE_KEY` to your private key
6. `NEXT_PUBLIC_ACCESS_NODE` to `https://rest-testnet.onflow.org`
7. `NEXT_PUBLIC_WALLET` to `https://fcl-discovery.onflow.org/testnet/authn`

You can now terminate all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Letâs try out our DApp on testnet:

1. Run `npm run dev` to start your application in a terminal.
2. On `http://localhost:3000/`, click âconnectâ and log in to your Blocto or Lilico wallet, making sure to copy the address you log in with.

![logging into discovery](https://i.imgur.com/dvYO2aU.png)

3. In a terminal, run `npm run mint`
4. In your terminal, you should see a printed âTransaction Idâ. If you go to [Testnet Flowdiver](https://testnet.flowdiver.io) and paste in that Transaction Id, you should see information about that minting transaction.
5. You should now see all the NFTs available for purchase!

\*Note: If you want to fund a testnet account with Flow Tokens to test your application, you can use the [Testnet Faucet](https://testnet-faucet.onflow.org/fund-account)

## ð Make Edits!

ð You can also check out your smart contract `ExampleNFT.cdc` in `flow/cadence/ExampleNFT.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `index.js` in `pages/index.js`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/4-voting-next).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/3-nft-minting/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/3-nft-minting-next/en/readme.md)



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