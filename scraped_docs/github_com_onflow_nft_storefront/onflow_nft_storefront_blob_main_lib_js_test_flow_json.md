# Source: https://github.com/onflow/nft-storefront/blob/main/lib/js/test/flow.json

```
{
	"emulators": {
	  "default": {
		"port": 3569,
		"serviceAccount": "emulator-account"
	  }
	},
	"contracts": {
	  "NFTStorefront": "./contracts/NFTStorefront.cdc",
	  "NFTStorefrontV2": "./contracts/NFTStorefrontV2.cdc",
	  "FungibleToken": "./contracts/utility/FungibleToken.cdc",
	  "NonFungibleToken": "./contracts/utility/NonFungibleToken.cdc",
	  "MetadataViews": "./contracts/utility/MetadataViews.cdc",
	  "FlowToken": {
		"aliases": {
		  "emulator": "0x0ae53cb6e3f42a79"
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
		"address": "0xf8d6e0586b0a20c7",
		"key": "ca102a35963666f3b517a903b747da4eece5e0553523cb8e59a851e162c85db2"
	  }
	},
	"deployments": {
	  "emulator": {
		"emulator-account": [
		  "NonFungibleToken","NFTStorefront", "NFTStorefrontV2", "MetadataViews", "FungibleToken"
		]
	  }
	}
  }
  
```