# Source: https://academy.ecdao.org/en/catalog/tutorials/deploy-contract-flow-cli

Emerald Academy





[![Emerald DAO Logo](/ea-logo.png)
Emerald Academy](/en/)


[* Catalog](/en/catalog)[* Cadence by Example](/en/cadence-by-example)[* Code Snippets](/en/snippets)[* Quickstarts](/en/quickstarts)[* Arcade](https://arcade.ecdao.org)

Connect



[Catalog](/en/catalog)
Deploy a Contract w/ the Flow CLI

# Deploy a Contract w/ the Flow CLI

Tutorial

Beginner

5 minutes

This tutorial will help you deploy a smart contract on Flow testnet/mainnet using the Flow CLI.

Follow along in a video format.

## 1. Install the Flow CLI

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

## 2. Create a flow.json File

In your terminal, go to whatever folder your project is. Type `flow init`. This will create a flow.json file in your project.

## 3. Create an Account

In your terminal, type `flow accounts create` and follow the process. When itâs complete, it will add all the necessary information to your flow.json file.

## 4. Configure your flow.json

Now we need to configure your flow.json to be able to find and deploy your contract.

First, add your contract to the âcontractsâ object. The key should be the name of your contract, and the value should be the file destination of your contract in your project.

json

```
		
			{
	"contracts": {
		"ExampleContract": "./src/flow/cadence/ExampleContract.cdc"
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
		"mainnet-account": {
			"address": "3d64e203dbb5eafb",
			"key": {
				"type": "file",
				"location": "mainnet-account.pkey"
			}
		}
	},
	"deployments": {}
}
		 
	
```

Next, add all the contract dependencies that your `ExampleContract` uses. For example, if it imports `NonFungibleToken`, you have to add it and all its âaliasesâ to your flow.json. Aliases are where the contract is already deployed on testnet/mainnet.

json

```
		
			{
	"contracts": {
		"ExampleContract": "./src/flow/cadence/ExampleContract.cdc",
        "NonFungibleToken": {
			"source": "./src/flow/cadence/NonFungibleToken.cdc",
			"aliases": {
                "testnet": "0x631e88ae7f1d7c20",
				"mainnet": "0x1d7e57aa55817448"
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
		"mainnet-account": {
			"address": "3d64e203dbb5eafb",
			"key": {
				"type": "file",
				"location": "mainnet-account.pkey"
			}
		}
	},
	"deployments": {}
}
		 
	
```

Next, add your contract to the âdeploymentsâ object:

json

```
		
			{
	"contracts": {
		"ExampleContract": "./src/flow/cadence/ExampleContract.cdc",
        "NonFungibleToken": {
			"source": "./src/flow/cadence/utility/NonFungibleToken.cdc",
			"aliases": {
                "testnet": "0x631e88ae7f1d7c20",
				"mainnet": "0x1d7e57aa55817448"
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
		"mainnet-account": {
			"address": "3d64e203dbb5eafb",
			"key": {
				"type": "file",
				"location": "mainnet-account.pkey"
			}
		}
	},
	"deployments": {
        "mainnet": {
            "mainnet-account": [
                "ExampleContract"
            ]
        }
    }
}
		 
	
```

## 5. Deploy

Lastly, run one of the following commands in your terminal:

* Testnet: `flow project deploy --network=testnet`
* Mainnet: `flow project deploy --network=mainnet`

## 6. Done!

To make sure your contract was actually deployed, you can use [Contract Browser](https://contractbrowser.com/) to search for your contract.

Till next time ~ Jacob Tucker

![User avatar](/avatars/jacob.jpeg)

Author

[Jacob Tucker](https://twitter.com/jacobmtucker)

[Video lesson](#)

[Edit Content](https://github.com/emerald-dao/emerald-academy-v2/tree/main/src/lib/content/tutorials/deploy-contract-flow-cli/en/readme.md)



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