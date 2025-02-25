# Source: https://academy.ecdao.org/en/quickstarts/5-multisign-next

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Multisign

# Multisign

Quickstart

Next.js

React.js

A Next.js DApp that allows anyone to deposit $FLOW to a DAO Treasury, of which admins must multisign actions to withdraw that $FLOW from the Treasury.

## ð© Quickstart 5: Multisign

ð« Deploy a Multisign contract to learn the basics of multisigning withdraws and deposits to a DAO Treasury on the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Next.js app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that allows anyone to deposit $FLOW to a DAO Treasury, of which admins must multisign actions to withdraw that $FLOW from the Treasury.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/5-multisign.git
		 
	
```

> in a terminal window, ð± install the dependencies start your frontend:

sh

```
		
			cd 5-multisign
npm install
npm run dev
		 
	
```

> in a second terminal window, start your ð·â local emulator:

bash

```
		
			cd 5-multisign
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash

```
		
			cd 5-multisign
flow project deploy
flow dev-wallet
		 
	
```

> You can `flow project deploy --update` to deploy a new contract any time.

ð± Open http://localhost:3000 to see the app

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð Checkpoint 2: Deposit $FLOW

After logging in to your DApp, you will see a Treasury that current has 0 $FLOW inside of it. You will notice at the top that you currently have a large balance of $FLOW, so letâs give our treasury some!

> Click the âDepositâ button. Input 100 for the amount, and write any description you wish.

![deposit](https://i.imgur.com/YC9IqZt.png)
> Click âDepositâ again and you will notice a transaction popup appear:

![deposit transaction popup](https://i.imgur.com/GiDWROX.png)

After clicking Approve, you will notice the balance in the Treasury get updated. In addition, a history of the deposit is placed under the âTransaction Historyâ section.

> Click on the deposit underneath âTransaction Historyâ. It will show you the details of that transaction:

![deposit history](https://i.imgur.com/E4bh4E5.png)

## ðª Checkpoint 3: Withdraw $FLOW

Now that we have deposited $FLOW to the treasury, letâs test out making a withdraw.

> On the main page, click the âWithdrawâ button. Input 10 for the amount, `0xf8d6e0586b0a20c7` for the beneficiary, and write any description you wish.

![withdraw](https://i.imgur.com/0ZWjZoA.png)
> Click âRequest Withdrawâ and you will notice a transaction popup appear.

After clicking Approve, you will notice that the balance in the Treasury *does not* get updated. This is because Admins of the treasury must all sign the request in order for it to go through. However, a âPendingâ history is shown:

![pending](https://i.imgur.com/13YPTA5.png)

## ð Checkpoint 4: Sign Withdraw Request

You can view all the Admins of the treasury on the main page. Initially, only the `0xf8d6e0586b0a20c7` account is an Admin, so if they sign a request, it will go through.

> From the main page, click âView Admin Dashboardâ.

You will see all the pending withdraw requests that you must vote on.

> Click on the request and you will be taken to a page describing the request:

![pending info](https://i.imgur.com/1q5b9RW.png)
> Sign the transaction by clicking the âSign Requestâ button. Approve the transaction.

After signing the transaction, you will notice âPendingâ switches to âCompleteâ in the top left. This is because all of the admins have approved the withdraw request.

In addition, the $FLOW token was withdrawn from the treasury and deposited to the beneficiary (`0xf8d6e0586b0a20c7`).

If you return back to the main page, you will notice there is now history marking the completed withdraw.

## ð Checkpoint 5: Add a New Admin

Letâs test out adding a new Admin to the Treasury. Once we do so, the new admin will also have to sign withdraw requests in order for them to go through.

If you log out of your account and log in with Account A, you will notice you cannot view the Admin Dashboard. This is because you are not yet an Admin of the Treasury! Letâs change that.

> Log back in to the Service Account and return back to your Admin Dashboard. Click âAdd Adminâ and add `0x179b6b1cb6755e31` as a new Admin.

> Next, repeat Checkpoint #3 and #4 to create & sign a withdraw request.

After doing that, you will notice that when we sign the new withdraw request from the Service Account, the request didnât go through! This is because we must also sign it from Account A.

> Log in to Account A, visit the Admin dashboard, and sign the new withdraw request.

Now it has officially gone through!

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
      "Multisign"
    ]
  },
  "testnet": {
    "testnet-account": [
      "Multisign"
    ]
  }
}
		 
	
```

> ð Deploy your Multisign smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/h2CId5N.png)
> Lastly, configure your .env file to point to Flow TestNet so we can interact with your new contract.

In your .env file, change the following:

1. `NEXT_PUBLIC_CONTRACT_ADDRESS` to your generated testnet address
2. `NEXT_PUBLIC_STANDARD_ADDRESS` to `0x9a0766d93b6608b7`
3. `NEXT_PUBLIC_FLOW_TOKEN_ADDRESS` to `0x7e60df042a9c0868`
4. `PRIVATE_KEY` to your private key
5. `NEXT_PUBLIC_ACCESS_NODE` to `https://rest-testnet.onflow.org`
6. `NEXT_PUBLIC_WALLET` to `https://fcl-discovery.onflow.org/testnet/authn`

You can now terminate all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Letâs try out our application on testnet:

1. Run `npm run dev` to start your application in a terminal.
2. On http://localhost:3000/, click âconnectâ and log in to your Blocto or Lilico wallet, making sure to copy the address you log in with.
3. Fund your testnet account by pasting your address into <https://testnet-faucet.onflow.org/fund-account>
4. Deposit $FLOW into the treasury.
5. Make a new withdraw request.
6. By default, the Admin of the treasury is the account you deployed your contract to. However, we do not have this account in a wallet like Lilico or Blocto, so we will have some trouble signing the withdraw request. To fix that, we created a command for you to sign proposals from your terminal:

* In your terminal, type `npm run sign [THE PROPOSAL ID]` (you can get the `proposalId` by clicking on the request and seeing its number)
* You should see a printed âTransaction Idâ. If you go to [Testnet Flowdiver](https://testnet.flowdiver.io) and paste in that Transaction Id, you should see information about that minting transaction.

## ð Make Edits!

ð You can also check out your multisign smart contract `Multisign.cdc` in `flow/cadence/Multisign.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `index.js` in `pages/index.js`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/6-groups-next).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/5-multisign/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/5-multisign-next/en/readme.md)



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