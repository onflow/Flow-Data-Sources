# Source: https://academy.ecdao.org/en/quickstarts/4-voting-next



















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Voting

# Voting


Quickstart

Next.js
React.js

A Next.js DApp that spins up an open DAO that lets community members create proposals and vote within it based on token holdings that govern the DAO.



## ð© Quickstart 4: Voting

ð« Deploy a Voting contract to learn the basics of voting inside of a DAO on the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Next.js app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that spins up an open DAO that lets community members create proposals and vote within it based on token holdings that govern the DAO.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

sh
```
		
			git clone https://github.com/emerald-dao/4-voting.git
		 
	
```
> in a terminal window, ð± install the dependencies start your frontend:

sh
```
		
			cd 4-voting
npm install
npm run dev
		 
	
```
> in a second terminal window, start your ð·â local emulator:

bash
```
		
			cd 4-voting
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash
```
		
			cd 4-voting
flow project deploy
flow dev-wallet
		 
	
```
> You can `flow project deploy --update` to deploy a new contract any time.

ð± Open http://localhost:3000 to see the app

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð Checkpoint 2: Name & Describe Your DAO

After logging in to our DApp, you will see that there is no name or description for our DAO:

![empty](https://i.imgur.com/YxDuWN5.png)
> Open up `./pages/index.js` and scroll down until you see `{"<Example DAO>"}` and `{"<Replace this with a description of your DAO>"}`. Replace these lines with a name & description of your DAO.

You will now see that being changed on your frontend:

![name & describe dao](https://i.imgur.com/nRHh0Mr.png)
## ðª Checkpoint 3: Join the DAO

Now that we have given our DAO a name & description, letâs join the DAO!

> Click the âJoin this DAOâ button and you will see a transaction model pop up:

![join dao tx](https://i.imgur.com/pvRoZPb.png)

If you click âApproveâ, you will be granted access to the DAOâs main dashboard.

Under the hood, you just set up your own token vault for the token that is governing this DAO.

> To see the smart contract for this token, you can go to `./flow/cadence/ExampleToken.cdc`

> To see how this transaction was run, check out the `joinDAO` function inside of `./pages/index.js`

## ð Checkpoint 4: Create a Proposal

After joining the DAO, you will be brought to the main dashboard of your DAO. You can see there are no active proposals, so letâs make one!

> Press the âSubmit Proposalâ button on the right side

To create a proposal, you must fill in:

* The name of the proposal
* The image of the proposal
* A start & end date
* A description of the proposal

![filling in proposal fields](https://i.imgur.com/HMfsBPQ.png)
> Click âSubmit Proposalâ to run a transaction that will create the new proposal on-chain

![run submit proposal tx](https://i.imgur.com/Fg8Qmuz.png)

A popup will appear to create your new proposal. This is a transaction that will change data on the blockchain. Specifically, it is creating a new `Proposal` resource and storing it in your DAOs collection of proposals.

> To see how this transaction was run, check out the `submitProposal` function inside of `./pages/submit.js`

> For more on Cadence & Resources, you can look at the contract code in `./flow/cadence/Vote.cdc` or check out our [Beginner Cadence Course](https://github.com/emerald-dao/beginner-cadence-course)

After clicking âApproveâ, you will be taken back to the main dashboard. You should now see a vote in play:

![a vote is now in play](https://i.imgur.com/PQXUtbb.png)
## ð Checkpoint 5: Viewing a Proposal

Now that a proposal has been created, lets click on it and see what it looks like:

![active proposal](https://i.imgur.com/R78d772.png)

You should see:

* Name
* Description
* Image
* Vote counts
* Who voted for what option
* Start & end date
* Who submitted the proposal

In order to actually vote however, we must own some tokens inside the DAO!

## ð¸ Checkpoint 6: Obtaining Tokens

In order to obtain some tokens, letâs actually mint some to our account.

> In a new terminal window, run `npm run mint 0xf8d6e0586b0a20c7 30.0`

This will mint 30.0 tokens to the account with address 0xf8d6e0586b0a20c7.

If you go back to your application and refresh the page (making sure you are logged in with account 0xf8d6e0586b0a20c7), you will notice your balance update at the top:

![balance update](https://i.imgur.com/zH4fgxP.png)
> To see how this command minted tokens to our account, check out `./actions/mint_tokens.js`

## ð¤ Checkpoint 7: Voting

You can click to vote a certain way by clicking one of either âForâ, âAgainstâ, or âAbstainâ.

> Click one of the voting options and see the transaction popup appear:

![tx to vote](https://i.imgur.com/AOjf5wx.png)

If you click approve, you should see the vote tally change, and your address get added to the list of voters below. Remember, you canât vote again!

## ð Checkpoint 8: Vote with a Different Account

Letâs try to submit a vote from another account!

1. At the top, click âLogoutâ and log in with a different account than before.
2. Join the DAO
3. Mint tokens to the new account using the same command as in Checkpoint 6, making sure to change the address to the new account.
4. Click on the same proposal and vote once again.
5. Watch the tally change!

## ð¾ Checkpoint 9: Deploy it to testnet!

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
      "ExampleToken",
      "Vote"
    ]
  },
  "testnet": {
    "testnet-account": [
      "ExampleToken",
      "Vote"
    ]
  }
}
		 
	
```
> ð Deploy your Vote smart contract:

sh
```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/nsASuV3.png)
> Lastly, configure your .env file to point to Flow TestNet so we can interact with your new contract.

In your .env file, change the following:

1. `NEXT_PUBLIC_CONTRACT_ADDRESS` to your generated testnet address
2. `NEXT_PUBLIC_STANDARD_ADDRESS` to `0x9a0766d93b6608b7`
3. `PRIVATE_KEY` to your private key
4. `NEXT_PUBLIC_ACCESS_NODE` to `https://rest-testnet.onflow.org`
5. `NEXT_PUBLIC_WALLET` to `https://fcl-discovery.onflow.org/testnet/authn`

You can now terminate all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Letâs try out our application on testnet:

1. Run `npm run dev` to start your application in a terminal.
2. On http://localhost:3000/, click âconnectâ and log in to your Blocto or Lilico wallet, making sure to copy the address you log in with.
3. Join the DAO and run the transaction. Wait ~30 seconds and then refresh the page. You should now be in the DAO.
4. Create a new proposal, same as before.
5. To obtain tokens, run `npm run mint [THE ADDRESS YOU COPIED IN STEP 2] [AMOUNT OF TOKENS]` like we did in Checkpoint 6.
6. In your terminal, you should see a printed âTransaction Idâ. If you go to [Testnet Flowdiver](https://testnet.flowdiver.io) and paste in that Transaction Id, you should see information about that minting transaction.
7. Attempt to vote in your proposal.

## ð Make Edits!

ð You can also check out your token smart contract `ExampleToken.cdc` in `flow/cadence/ExampleToken.cdc`, or your voting/DAO smart contract `Vote.cdc` in `flow/cadence/Vote.cdc`

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `index.js` in `pages/index.js`.

## âï¸ Side Quests

> ð Head to your next challenge [here](https://academy.ecdao.org/en/quickstarts/5-multisign-next).

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).


![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)


[Fork Quickstart](https://github.com/emerald-dao/4-voting/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/4-voting-next/en/readme.md)


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



