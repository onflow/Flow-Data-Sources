# Source: https://academy.ecdao.org/en/quickstarts/6-groups-next

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Quickstart](/en/quickstarts)
Groups

# Groups

Quickstart

Next.js

React.js

A Next.js DApp that allows users to create Groups, join & leave them, discover Groups, and chat inside of them.

## ð© Quickstart 5: Groups

ð« Deploy a subcommunities contract to learn the basics of voting inside of a DAO on the Flow blockchain and Cadence. Youâll use:

* The local Flow emulator to deploy smart contracts.
* The local Flow dev wallet to log into test accounts.
* A template Next.js app with sample scripts and transactions to interact with your contract.

ð The final deliverable is a DApp that allows users to create Groups, join & leave them, discover Groups, and chat inside of them.

ð¬ Meet other builders working on this challenge and get help in the [Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

## ð¦ Checkpoint 0: Install

Required:

* [Git](https://git-scm.com/downloads)
* [Node](https://nodejs.org/dist/latest-v16.x/) (ð§¨ Use Node v16 or a previous version as v17 may cause errors ð§¨). You know you have installed it if you type `node -v` in your terminal and it prints a version.
* [Flow CLI](https://docs.onflow.org/flow-cli/install/) (ð§¨ Make sure to install the correct link for your system ð§¨). You know you have installed it if you type `flow version` in your terminal and it prints a version.

sh

```
		
			git clone https://github.com/emerald-dao/6-groups.git
		 
	
```

> in a terminal window, ð± install the dependencies start your frontend:

sh

```
		
			cd 6-groups
npm install
npm run dev
		 
	
```

> in a second terminal window, start your ð·â local emulator:

bash

```
		
			cd 6-groups
flow emulator start -v
		 
	
```

*Note: the `-v` flag means to print transaction and script output to your local emulator*

> in a third terminal window, ð¾ deploy your contract and ð¸ start your local wallet:

bash

```
		
			cd 6-groups
flow project deploy
flow dev-wallet
		 
	
```

> You can `flow project deploy --update` to deploy a new contract any time.

ð± Open http://localhost:3000 to see the app

## ð Checkpoint 1: Wallets

Weâll be using **the local Flow dev wallet**.

> Click the âLog Inâ button and notice a window appears with different accounts to select, each with their own Flow Token balance. Select the first account to log in to it.

## ð Checkpoint 2: Viewing a Group

After logging in to our DApp, you will notice that there is already a community up and running: Emerald City!

![emerald city group](https://i.imgur.com/gWlGUwh.png)
> Click on Emerald City

You will be taken to a page that shows all the details of Emerald City:

![group page](https://i.imgur.com/BIuoZPm.png)

Because you are logged in to the Service Account, and that account is the owner of this group, you are in the community already. Letâs try to log into a different account and join this community.

## ðª Checkpoint 3: Joining a Group

Letâs join the Emerald City group from a different account!

> At the top, click âLogoutâ and log back in with Account A

Account A does not belong to this group, so we cannot do thing like see the groupâs forum.

> To join, click the âJoin Communityâ button and you will see a transaction model pop up:

![join group](https://i.imgur.com/rFUkEKX.png)

If you click âApproveâ, you will notice that your address is now added to the members list. Woohoo! We successfully joined the group. If you wanted to, you could also leave the group.

## ð Checkpoint 4: Type a Message

Now that we joined the group, we can start to use the forum!

> Type a message into the community forum and click âSubmitâ. You will notice a transaction popup, click Approve.

![join group](https://i.imgur.com/OKkFToc.png)

Your message has been added to the community forum, stored completely on-chain!

## ð Checkpoint 5: Creating a Group

To create a group, head back to the main page and click âCreate Groupâ. Once you are there, you must fill in:

* An image for your group
* The name of your group
* A description for your group

You will be able to preview your new group on the right-hand side:

![preview group](https://i.imgur.com/yvZCW6P.png)
> Click âCreate Groupâ to run a transaction that will create the new group on-chain

A popup will appear to create your new proposal. This is a transaction that will change data on the blockchain. Specifically, it is creating a new `Group` resource and storing it in your collection of Groups that you have created.

> To see how this transaction was run, check out the `createGroup` function inside of `./pages/create.js`

> For more on Cadence & Resources, you can look at the contract code in `./flow/cadence/Groups.cdc` or check out our [Beginner Cadence Course](https://github.com/emerald-dao/beginner-cadence-course)

After clicking âApproveâ, you will be taken back to the main dashboard. You should now see your group:

![see your new group]()

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
      "Groups"
    ]
  },
  "testnet": {
    "testnet-account": [
      "Groups"
    ]
  }
}
		 
	
```

> ð Deploy your Vote smart contract:

sh

```
		
			flow project deploy --network=testnet
		 
	
```

![deploy contract to testnet](https://i.imgur.com/s899jKs.png)
> Lastly, configure your .env file to point to Flow TestNet so we can interact with your new contract.

In your .env file, change the following:

1. `NEXT_PUBLIC_CONTRACT_ADDRESS` to your generated testnet address
2. `NEXT_PUBLIC_ACCESS_NODE` to `https://rest-testnet.onflow.org`
3. `NEXT_PUBLIC_WALLET` to `https://fcl-discovery.onflow.org/testnet/authn`

You can now terminate all your terminals since we no longer need to run our own local blockchain or wallet. Everything lives on testnet!

Letâs try out our application on testnet:

1. Run `npm run dev` to start your application in a terminal.
2. On http://localhost:3000/, click âconnectâ and log in to your Blocto or Lilico wallet.
3. Join the Emerald City group by running the associated transaction. Wait ~30 seconds and then refresh the page. You should now be in the group.
4. Create a new group, same as before.
5. Chat in any group of your wish.

## Storing Image Assets

You may be wondering: How are you storing images? Where do they go?

Thanks to our amazing supporters at [Filecoin](https://filecoin.io/), we decided to use [NFT.Storage](https://nft.storage/) to store our image assets on IPFS. NFT.Storage allows you to upload an image, and in return it gives you whatâs called a âCIDâ, or a long list of random numbers and letters. You can use this to fetch your image from a URL and properly display it.

This is also especially useful when we think about storage costs. We would never want to store images directly in our smart contract because that would be expensive (having to store hundreds of Megabytes, or potentially Gigabytes). Instead, we store the CID, which is just a small string and much cheaper.

This is how simple it is to store images on IPFS in your code:

1. `npm install nft.storage`
2. Go to [NFT.Storage](https://nft.storage/) > Login > API Keys > + New Key > Actions > Copy
3. Paste your key in your `.env` file
4. Added the following code in our `/pages/create.js` file:

jsx

```
		
			import { NFTStorage } from 'nft.storage';

const [preview, setPreview] = useState('');
const [ipfsCid, setIpfsCid] = useState('');

const NFT_STORAGE_TOKEN = process.env.NEXT_PUBLIC_NFTSTORAGE_KEY;
const client = new NFTStorage({ token: NFT_STORAGE_TOKEN });

async function uploadToIPFS(file) {
	let prev = URL.createObjectURL(file);
	setPreview(prev);
	const cid = await client.storeBlob(file);
	setIpfsCid(cid);
}
		 
	
```

5. Store the IPFS CID in your smart contract code. Inside `/flow/cadence/Groups.cdc`, check out the `image` variable under the `GroupInfo` struct. That stores the IPFS CID.

## ð Make Edits!

ð You can also check out your groups smart contract `Groups.cdc` in `flow/cadence/Groups.cdc`.

ð¼ Take a quick look at how your contract get deployed in `flow.json`.

ð If you want to make frontend edits, open `index.js` in `pages/index.js`.

## âï¸ Side Quests

> ð More challenges coming soonâ¦

> ð¬ Meet other builders working on this challenge and get help in the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541)!

> ð Problems, questions, comments on the stack? Post them to the [ð Emerald City Discord](https://discord.gg/emerald-city-906264258189332541).

![User avatar](https://avatars.githubusercontent.com/u/100654804?v=4)

Author

[Emerald City](https://twitter.com/emerald_dao)

[Fork Quickstart](https://github.com/emerald-dao/6-groups/fork)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/quickstarts/6-groups-next/en/readme.md)



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