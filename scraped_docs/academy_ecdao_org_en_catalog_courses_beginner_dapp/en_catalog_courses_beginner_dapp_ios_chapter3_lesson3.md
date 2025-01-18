# Source: https://academy.ecdao.org/en/catalog/courses/beginner-dapp-ios/chapter3/lesson3





















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

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

# Chapter 3 Lesson 3 - Bringing Cadence to our DApp & Deploying our Contract

Todayâs lesson will be very short (WOOOHOOOO! We donât have to read Jacobâs annoying lesson for too long!). We are going to bring our Cadence code into our DApp.

## Installing the Cadence VSCode Extension

Xcode is specific to development for Apple systems, particularly Swift. Unfortunately, it doesnât support working with Cadence, Open your project folder in VSCode for these next steps.

Now that weâre no longer on the playground, we want to be able to have errors show up in our VSCode when weâre coding Cadence. Thereâs an extension to do that!

> Open VSCode. On the left side of VSCode, thereâs an icon that looks like 4 squares. Click that and search âCadenceâ.

> Click on the following extension and press âInstallâ:

![](https://i.imgur.com/SG5vHHo.png)
## Installing the Flow CLI & flow.json

The Flow CLI will allow us to run transactions & scripts from the terminal, and allow us to do other Flow stuff like creating `flow.json` (coming soonâ¦)

> Install the [Flow CLI](https://docs.onflow.org/flow-cli/install/). You can do that by:

**Mac**

* Pasting `sh -ci "$(curl -fsSL https://storage.googleapis.com/flow-cli/install.sh)"` into a terminal

You can confirm the Flow CLI is installed by going to a terminal and typing `flow version`. If a version appears, youâre good to go.

## Cadence Folder

Inside our Emerald DApp, letâs make a new folder called `cadence`.

Inside the `cadence` folder, letâs make a `contracts` folder, a `transactions` folder, and a `scripts` folder.

Inside the `contracts` folder, add a new file called `HelloWorld.cdc`. In that file, put our contract code from yesterday:

cadence
```
		
			pub contract HelloWorld {

    pub var greeting: String

    pub fun changeGreeting(newGreeting: String) {
        self.greeting = newGreeting
    }

    init() {
        self.greeting = "Hello, World!"
    }
}
		 
	
```

---

Inside the transactions folder, make a new file called `changeGreeting.cdc` and put our transaction code from yesterday:

cadence
```
		
			import HelloWorld from 0x01 // THIS IS NO LONGER CORRECT

transaction(myNewGreeting: String) {

  prepare(signer: AuthAccount) {}

  execute {
    HelloWorld.changeGreeting(newGreeting: myNewGreeting)
  }
}
		 
	
```

Notice that the import is now wrong. We arenât importing from `0x01` anymore, that was just a playground thing. In this case, we are importing from a local contract that exists in our project. So change it to:

cadence
```
		
			import HelloWorld from "../contracts/HelloWorld.cdc"
		 
	
```

---

Inside the scripts folder, add a new file called `readGreeting.cdc` and put in our script code from yesterday:

cadence
```
		
			import HelloWorld from "../contracts/HelloWorld.cdc"

pub fun main(): String {
    return HelloWorld.greeting
}
		 
	
```

Your project directory should now look like this:

![](https://i.imgur.com/rgYpVEY.png)

---

### flow.json

> Now that we have our contract in our project directory, go to your terminal and `cd` into the base project directory.

> Type `flow init`

This will create a `flow.json` file inside your project. This is needed to deploy contracts and to give us compile errors inside our Cadence code.

## Deploying our Greeting Contract to TestNet

Sweet! Now letâs deploy our contract to TestNet so that we can start interacting with it.

## Configuring `flow.json`

> Inside of your `flow.json` file, make the âcontractsâ object look like this:

json
```
		
			"contracts": {
  "HelloWorld": "./cadence/contracts/HelloWorld.cdc"
},
		 
	
```

This will allow your `flow.json` to know where your contracts live.

## Creating an Account

> ð Generate a **deployer address** by typing `flow keys generate --network=testnet` into a terminal. Make sure to save your public key and private key somewhere, you will need them soon.

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

![deploy contract to testnet](https://i.imgur.com/m1zMisW.png)
## Interacting with our Contract

Now that we deployed our contract to testnet, we can interact with it in our terminal using the Flow CLI.

### Informing flow.json of our Deployed Contract

Before we run a script using the Flow CLI in our terminal, we have to tell our `flow.json` where our contract lives on testnet. This is because right now, the import path (`"../contracts/HelloWorld.cdc"`) is meaningless inside our script file.

Now that we have deployed our contract to testnet, we can configure our `flow.json` to recognize that the contract exists at that address.

Inside your `flow.jsonâ, change the âcontractsâ object to look like this:

json
```
		
			"contracts": {
  "HelloWorld": {
    "source": "./cadence/contracts/HelloWorld.cdc",
    "aliases": {
      "testnet": "YOUR CONTRACT ADDRESS"
    }
  }
}
		 
	
```

Now, when you run your script, it will automatically replace the local import path to the deployed contract address.

### Reading our Greeting

To run our `readGreeting.cdc` script from the terminal, go to your project directory and type:

bash
```
		
			flow scripts execute ./flow/cadence/scripts/readGreeting.cdc --network=testnet
		 
	
```

If it works properly, you will see this:

![](https://i.imgur.com/TPDJsdO.png)

Boom! It returned âHello, World!â, which is exactly what our `greeting` variable is in the contract. YAY!!

### Changing our Greeting

To run our `changeGreeting.cdc` transaction from the terminal, go to your project directory and type:

bash
```
		
			flow transactions send ./flow/cadence/transactions/changeGreeting.cdc "Goodbye, Loser" --network=testnet --signer=testnet-account
		 
	
```

If it works properly, you will see this:

![](https://i.imgur.com/1JXgEav.png)

That means the transaction is sealed (completed) and worked! If you run the script to read the greeting again, hopefully, you will see:

![](https://i.imgur.com/K7nAYC5.png)

NICE!!! We successfully changed our `greeting` in our contract. This is so cool.

## Conclusion

That was a lot today, but how cool is this?! We deployed our own contract to Flow Testnet, ran a script to read our `greeting`, and then ran a transaction to change it. You are all doing amazing!

## Quests

1. Create a new smart contract in Cadence that has at least the following two things:

* A variable to hold a value (like a number or a piece of text)
* A function to change that variable

After, deploy that contract to the same testnet account you generated today.

2. Send a screenshot of you reading the variable from your new contract using the Flow CLI
3. Send a screenshot of you changing the variable from your new contract using the Flow CLI
4. Send a screenshot of you reading your changed variable from your new contract using the Flow CLI
5. Go to <https://flow-view-source.com/testnet/>. Where it says âAccountâ, paste in the Flow address you generated and click âGoâ. On the left-hand side, you should see your âHelloWorldâ contract and your new contract. Isnât it so cool to see them live on Testnet? Then, send the URL to the page.

* EXAMPLE: <https://flow-view-source.com/testnet/account/0x90250c4359cebac7/>

![User avatar](https://avatars.githubusercontent.com/u/3641594?s=400&u=044fd05bc61270527c4da99212f143595d6fa4a1&v=4)

Author

[BoiseITGuru](https://twitter.com/boise_it_guru)




[Quests](#quests)
[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/courses/beginner-dapp-ios/en/chapter3/lesson3.md)


[Transactions and Scripts](/en/catalog/courses/beginner-dapp-ios/chapter3/lesson2)
[Connecting the Blockchain](/en/catalog/courses/beginner-dapp-ios/chapter4/lesson1)

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



