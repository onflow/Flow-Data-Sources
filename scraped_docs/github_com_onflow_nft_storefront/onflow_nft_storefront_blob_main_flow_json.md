# Source: https://github.com/onflow/nft-storefront/blob/main/flow.json

```
{
	"contracts": {
		"Burner": {
			"source": "./contracts/utility/Burner.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "f233dcee88fe0abe",
				"previewnet": "b6763b4399a888c8",
				"testing": "0000000000000001",
				"testnet": "9a0766d93b6608b7"
			}
		},
		"CapabilityDelegator": {
			"source": "./contracts/hybrid-custody/CapabilityDelegator.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"CapabilityFactory": {
			"source": "./contracts/hybrid-custody/CapabilityFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"CapabilityFilter": {
			"source": "./contracts/hybrid-custody/CapabilityFilter.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"ExampleNFT": {
			"source": "./contracts/utility/ExampleNFT.cdc",
			"aliases": {
				"testing": "0000000000000008"
			}
		},
		"ExampleToken": {
			"source": "./contracts/utility/ExampleToken.cdc",
			"aliases": {
				"testing": "0000000000000009"
			}
		},
		"FTAllFactory": {
			"source": "./contracts/hybrid-custody/factories/FTAllFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"FTBalanceFactory": {
			"source": "./contracts/hybrid-custody/factories/FTBalanceFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"FTProviderFactory": {
			"source": "./contracts/hybrid-custody/factories/FTProviderFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"FTReceiverBalanceFactory": {
			"source": "./contracts/hybrid-custody/factories/FTReceiverBalanceFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"FTReceiverFactory": {
			"source": "./contracts/hybrid-custody/factories/FTReceiverFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"FungibleToken": {
			"source": "./contracts/utility/FungibleToken.cdc",
			"aliases": {
				"emulator": "ee82856bf20e2aa6",
				"mainnet": "f233dcee88fe0abe",
				"previewnet": "a0225e7000ac82a9",
				"testing": "0000000000000002",
				"testnet": "9a0766d93b6608b7"
			}
		},
		"FungibleTokenMetadataViews": {
			"source": "./contracts/utility/FungibleTokenMetadataViews.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "f233dcee88fe0abe",
				"previewnet": "a0225e7000ac82a9",
				"testing": "0000000000000002",
				"testnet": "9a0766d93b6608b7"
			}
		},
		"HybridCustody": {
			"source": "./contracts/hybrid-custody/HybridCustody.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"MaliciousStorefrontV1": {
			"source": "./contracts/utility/test/MaliciousStorefrontV1.cdc",
			"aliases": {
				"testing": "0000000000000007"
			}
		},
		"MaliciousStorefrontV2": {
			"source": "./contracts/utility/test/MaliciousStorefrontV2.cdc",
			"aliases": {
				"testing": "0000000000000007"
			}
		},
		"MetadataViews": {
			"source": "./contracts/utility/MetadataViews.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testing": "0000000000000001",
				"testnet": "631e88ae7f1d7c20"
			}
		},
		"NFTCatalog": {
			"source": "./contracts/utility/NFTCatalog.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "49a7cda3a1eecc29",
				"testnet": "324c34e1c517e4db"
			}
		},
		"NFTCollectionPublicFactory": {
			"source": "./contracts/hybrid-custody/factories/NFTCollectionPublicFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"NFTProviderAndCollectionFactory": {
			"source": "./contracts/hybrid-custody/factories/NFTProviderAndCollectionFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "d8a7e05a7ac670c0",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"NFTProviderFactory": {
			"source": "./contracts/hybrid-custody/factories/NFTProviderFactory.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"testnet": "294e44e1ec6993c6"
			}
		},
		"NFTStorefront": {
			"source": "./contracts/NFTStorefront.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testing": "0000000000000006",
				"testnet": "94b06cfca1d8a476"
			}
		},
		"NFTStorefrontV2": {
			"source": "./contracts/NFTStorefrontV2.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testing": "0000000000000007",
				"testnet": "2d55b98eb200daef"
			}
		},
		"NonFungibleToken": {
			"source": "./contracts/utility/NonFungibleToken.cdc",
			"aliases": {
				"emulator": "f8d6e0586b0a20c7",
				"mainnet": "1d7e57aa55817448",
				"testing": "0000000000000001",
				"testnet": "631e88ae7f1d7c20"
			}
		},
		"ViewResolver": {
			"source": "./contracts/utility/ViewResolver.cdc",
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
		"previewnet": "access.previewnet.nodes.onflow.org:9000",
		"testing": "127.0.0.1:3569",
		"testnet": "access.devnet.nodes.onflow.org:9000"
	},
	"accounts": {
		"emulator-account": {
			"address": "f8d6e0586b0a20c7",
			"key": "ca102a35963666f3b517a903b747da4eece5e0553523cb8e59a851e162c85db2"
		},
		"mainnet-storefront": {
			"address": "4eb8a10cb9f87357",
			"key": {
				"type": "google-kms",
				"index": 1,
				"hashAlgorithm": "SHA2_256",
				"resourceID": "projects/dl-flow-admin/locations/global/keyRings/flow-nft-storefront/cryptoKeys/flow-nft-storefront/cryptoKeyVersions/1"
			}
		},
		"testnet-storefront": {
			"address": "94b06cfca1d8a476",
			"key": {
				"type": "file",
				"location": "./storefront-testnet.pkey"
			}
		}
	},
	"deployments": {
		"emulator": {
			"emulator-account": [
				"FungibleTokenMetadataViews",
				"ExampleNFT",
				"ExampleToken",
				"NFTStorefront",
				"NFTStorefrontV2"
			]
		},
		"mainnet": {
			"mainnet-storefront": [
				"NFTStorefrontV2",
				"NFTStorefront"
			]
		},
		"testnet": {
			"testnet-storefront": [
				"NFTStorefront"
			]
		}
	}
}
```