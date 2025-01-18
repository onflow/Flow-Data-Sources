# Source: https://academy.ecdao.org/en/catalog/tutorials/send-txs-scripts-flix




















Emerald Academy


[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)

[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Flownaut](https://flownaut.ecdao.org)[* Arcade](https://arcade.ecdao.org)

Connect



[Catalog](/en/catalog)
Send Transactions and Scripts using FLIX

# Send Transactions and Scripts using FLIX


Tutorial

Beginner

20 minutes



This tutorial will help you use FLIX - a way to send transactions & scripts from a frontend without having to know Cadence.

## What is FLIX?

FLIX allows Cadence developers to turn their transactions & scripts, which are written in Cadence, into JSON âtemplatesâ. These templates can then be âconsumedâ by frontend app developers who do not know Cadence, but instead can simply generate Javascript or Typescript files with those pre-made templates to automatically set up calling transactions & scripts in their app.

# Creating FLIX Templates from Cadence Files

If you are a Cadence developer who would like to actually create FLIX templates for others to use, this section is for you. If you are **not** a Cadence developer and would simply like to use FLIX on your frontend - skip this section.

If you would like to view a completed version of this section, go [here](https://github.com/onflow/hello-world-flix).

## Install the Flow CLI

Open up a terminal on your computer. Paste and run the command based on your system:

* Mac:

bash
```
		
			sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
		 
	
```

* Linux:

bash
```
		
			sh -ci "$(curl -fsSL https://raw.githubusercontent.com/onflow/flow-cli/master/install.sh)"
		 
	
```

* Windows:

bash
```
		
			iex "& { $(irm 'https://raw.githubusercontent.com/onflow/flow-cli/master/install.ps1') }"
		 
	
```

To make sure it worked, type `flow version`. If you see a version, it worked.

## Setup flow.json File

In your terminal, go to the main directory of your project. Type `flow init`. This will create a flow.json file in your project.

Next, inside your flow.json file, add a âcontractsâ object that looks something like this:

json
```
		
			"contracts": {
	"HelloWorld": {
		"source": "./HelloWorld.cdc",
		"aliases": {
			"testnet": "0x01",
			"mainnet": "0x02"
		}
	}
}
		 
	
```

Make sure to replace the addresses of where your contract is with actual testnet/mainnet addresses under âaliasesâ.

## Creating Templates

Now we can actually create a template from our Cadence code.

To do that, run the following command in your terminal from the main directory:

bash
```
		
			flow flix generate ./cadence/scripts/ReadHelloWorld.cdc --save ./cadence/templates/ReadHelloWorld.template.json      
		 
	
```

Make sure to replace the first file path with the actual location of your script/tx Cadence code, and the second file path with where you want your template to be saved.

## Testing Your Template

You can actually run your script/tx template using the Flow CLI.

To do that, run the following command in your terminal from the main directory:

bash
```
		
			flow flix execute ./cadence/templates/ReadHelloWorld.template.json --network testnet
		 
	
```

You should see a valid result in your terminal.

# Consuming FLIX Templates on a Frontend

This section will teach you how to actually consume pre-made FLIX templates to automatically create tx/script functions you can call from your app.

If you would like to view a completed version of this section, go [here](https://github.com/onflow/hello-world-web).

## Creating a Package File

A package file is simply an auto-generated file in Javascript or Typescript that includes a function to call a script or transaction.

To create one, run the following command in your terminal from the main directory:

bash
```
		
			flow flix package https://raw.githubusercontent.com/onflow/hello-world-flix/main/cadence/templates/ReadHelloWorld.template.json --lang ts --save ./app/cadence/readHelloWorld.ts
		 
	
```

The first link in that command is a link to the template file. The last file path is where we want to save our package file.

If you go to your `readHelloWorld.ts` file, you should see it looks something like this:

typescript
```
		
			/**
    This binding file was auto generated based on FLIX template v1.1.0. 
    Changes to this file might get overwritten.
    Note fcl version 1.9.0 or higher is required to use templates. 
**/

import * as fcl from "@onflow/fcl"
const flixTemplate = "https://raw.githubusercontent.com/onflow/hello-world-flix/main/cadence/templates/ReadHelloWorld.template.json"


/**
* getGreeting: Call HelloWorld contract to get greeting
* @returns {Promise<string>} - 
*/
export async function getGreeting(): Promise<string> {
  const info = await fcl.query({
    cadence: "",
    // @ts-ignore, fcl needs to be updated to support templates urls along with template as an object
    template: flixTemplate,
    
  });

  return info
}
		 
	
```

Perfect! We now have a function we can call to read our greeting from the `HelloWorld` contract on Flow testnet.

# Conlusion

Thanks so much to Tom Haile for not only creating FLIX, but helping me learn about it! This is all thanks to him.

Till next time ~ Jacob Tucker


![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)




[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/tutorials/send-txs-scripts-flix/en/readme.md)


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



