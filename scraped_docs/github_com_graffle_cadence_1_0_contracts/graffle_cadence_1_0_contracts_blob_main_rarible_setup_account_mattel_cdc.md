# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/setup-account-mattel.cdc

```
import NonFungibleToken from "NonFungibleToken"
import MetadataViews from "MetadataViews"
import FungibleToken from "FungibleToken"
// import USDCFlow from "USDCFlow"
import HWGarageCard from "HWGarageCard"
import HWGaragePack from "HWGaragePack"
import HWGarageCardV2 from "HWGarageCardV2"
import HWGaragePackV2 from "HWGaragePackV2"
import HWGarageTokenV2 from "HWGarageTokenV2"
import BBxBarbiePack from "BBxBarbiePack"
import BBxBarbieCard from "BBxBarbieCard"
import BBxBarbieToken from "BBxBarbieToken"
import NFTStorefrontV2 from "NFTStorefrontV2"

transaction() {
		prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {

			// ******
			// IMPORTANT UNCOMMENT WHEN USDCFLOW IS READY FOR CRESCENDO
			// ******
			// if signer.storage.borrow<&USDCFlow.Vault>(from: /storage/usdcFlowVault) == nil {
			// 		// Create a new flowToken Vault and put it in storage
			// 		signer.storage.save(<-USDCFlow.createEmptyVault(), to: /storage/usdcFlowVault)

			// 		// Create a public capability to the Vault that only exposes
			// 		// the deposit function through the Receiver interface
			// 		let vaultCap = signer.capabilities.storage.issue<&USDCFlow.Vault>(
			// 				/storage/usdcFlowVault
			// 		)

			// 		signer.capabilities.publish(
			// 				vaultCap,
			// 				at: /public/usdcFlowReceiver
			// 		)

			// 		// Create a public capability to the Vault that only exposes
			// 		// the balance field through the Balance interface
			// 		let balanceCap = signer.capabilities.storage.issue<&USDCFlow.Vault>(
			// 				/storage/usdcFlowVault
			// 		)

			// 		signer.capabilities.publish(
			// 				balanceCap,
			// 				at: /public/usdcFlowMetadata
			// 		)
			// }

			// HWGaragePack
			let packCollectionData: MetadataViews.NFTCollectionData = HWGaragePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if packCollection exists
			if acct.storage.borrow<&HWGaragePack.Collection>(from: packCollectionData.storagePath) == nil {
					// create a new empty packCollection for HWGaragePack
					let packCollection: @{NonFungibleToken.Collection} <- HWGaragePack.createEmptyCollection(nftType: Type<@HWGaragePack.NFT>())

					// save HWGaragePack packCollection to the account
					acct.storage.save(<-packCollection, to: packCollectionData.storagePath)

					// create a public capability for the HWGaragePack packCollection
					acct.capabilities.unpublish(packCollectionData.publicPath) // remove any current pubCap 
					let packCollectionCap: Capability<&HWGaragePack.Collection> = acct.capabilities.storage.issue<&HWGaragePack.Collection>(packCollectionData.storagePath)
					acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)
			}

			// HWGarageCard
			let cardCollectionData: MetadataViews.NFTCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if cardCollection exists
			if acct.storage.borrow<&HWGarageCard.Collection>(from: cardCollectionData.storagePath) == nil {
					// create a new empty cardCollection for HWGarageCard
					let cardCollection: @{NonFungibleToken.Collection} <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

					// save HWGarageCard cardCollection to the account
					acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

					// create a public capability for the HWGarageCard cardCollection
					acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
					let cardCollectionCap: Capability<&HWGarageCard.Collection> = acct.capabilities.storage.issue<&HWGarageCard.Collection>(cardCollectionData.storagePath)
					acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
			}

			// HWGarageTokenV2
			let tokenCollectionDataV2: MetadataViews.NFTCollectionData = HWGarageTokenV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			if acct.storage.borrow<&HWGarageTokenV2.Collection>(from: tokenCollectionDataV2.storagePath) == nil {
					// create a new empty tokenCollection for HWGarageTokenV2
					let tokenCollection: @{NonFungibleToken.Collection} <- HWGarageTokenV2.createEmptyCollection(nftType: Type<@HWGarageTokenV2.NFT>())

					// save HWGarageTokenV2 tokenCollection to the account
					acct.storage.save(<-tokenCollection, to: tokenCollectionDataV2.storagePath)

					// create a public capability for the HWGarageTokenV2 tokenCollection
					acct.capabilities.unpublish(tokenCollectionDataV2.publicPath) // remove any current pubCap 
					let tokenCollectionCap = acct.capabilities.storage.issue<&HWGarageTokenV2.Collection>(tokenCollectionDataV2.storagePath)
					acct.capabilities.publish(tokenCollectionCap, at: tokenCollectionDataV2.publicPath)
			}

			// HWGarageCardV2
			let cardCollectionDataV2: MetadataViews.NFTCollectionData = HWGarageCardV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if cardCollection exists
			if acct.storage.borrow<&HWGarageCardV2.Collection>(from: cardCollectionDataV2.storagePath) == nil {
					// create a new empty cardCollection for HWGarageCardV2
					let cardCollection: @{NonFungibleToken.Collection} <- HWGarageCardV2.createEmptyCollection(nftType: Type<@HWGarageCardV2.NFT>())

					// save HWGarageCardV2 cardCollection to the account
					acct.storage.save(<-cardCollection, to: cardCollectionDataV2.storagePath)

					// create a public capability for the HWGarageCardV2 cardCollection
					acct.capabilities.unpublish(cardCollectionDataV2.publicPath) // remove any current pubCap 
					let cardCollectionCap = acct.capabilities.storage.issue<&HWGarageCardV2.Collection>(cardCollectionDataV2.storagePath)
					acct.capabilities.publish(cardCollectionCap, at: cardCollectionDataV2.publicPath)
			}

			// HWGaragePackV2
			let garagePackCollectionDataV2: MetadataViews.NFTCollectionData = HWGaragePackV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if packCollection exists
			if acct.storage.borrow<&HWGaragePackV2.Collection>(from: garagePackCollectionDataV2.storagePath) == nil {
					// create a new empty packCollection for HWGaragePackV2
					let packCollection: @{NonFungibleToken.Collection} <- HWGaragePackV2.createEmptyCollection(nftType: Type<@HWGaragePackV2.NFT>())

					// save HWGaragePackV2 packCollection to the account
					acct.storage.save(<-packCollection, to: garagePackCollectionDataV2.storagePath)

					// create a public capability for the HWGaragePackV2 packCollection
					acct.capabilities.unpublish(garagePackCollectionDataV2.publicPath) // remove any current pubCap 
					let packCollectionCap = acct.capabilities.storage.issue<&HWGaragePackV2.Collection>(garagePackCollectionDataV2.storagePath)
					acct.capabilities.publish(packCollectionCap, at: garagePackCollectionDataV2.publicPath)
			}

		// Setup Token Collection

			let barbieTokenCollectionData: MetadataViews.NFTCollectionData = BBxBarbieToken.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if tokenCollection exists
			if acct.storage.borrow<&BBxBarbieToken.Collection>(from: barbieTokenCollectionData.storagePath) == nil {
					// create a new empty tokenCollection for BBxBarbieToken
					let tokenCollection: @{NonFungibleToken.Collection} <- BBxBarbieToken.createEmptyCollection(nftType: Type<@BBxBarbieToken.NFT>())

					// save BBxBarbieToken tokenCollection to the account
					acct.storage.save(<-tokenCollection, to: barbieTokenCollectionData.storagePath)

					// create a public capability for the BBxBarbieToken tokenCollection
					acct.capabilities.unpublish(barbieTokenCollectionData.publicPath) // remove any current pubCap 
					let tokenCollectionCap: Capability<&BBxBarbieToken.Collection> = acct.capabilities.storage.issue<&BBxBarbieToken.Collection>(barbieTokenCollectionData.storagePath)
					acct.capabilities.publish(tokenCollectionCap, at: barbieTokenCollectionData.publicPath)
			}



			// Setup Card Collection

			let barbieCardCollectionData: MetadataViews.NFTCollectionData = BBxBarbieCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if cardCollection exists
			if acct.storage.borrow<&BBxBarbieCard.Collection>(from: barbieCardCollectionData.storagePath) == nil {
					// create a new empty cardCollection for BBxBarbieCard
					let cardCollection: @{NonFungibleToken.Collection} <- BBxBarbieCard.createEmptyCollection(nftType: Type<@BBxBarbieCard.NFT>())

					// save BBxBarbieCard cardCollection to the account
					acct.storage.save(<-cardCollection, to: barbieCardCollectionData.storagePath)

					// create a public capability for the BBxBarbieCard cardCollection
					acct.capabilities.unpublish(barbieCardCollectionData.publicPath) // remove any current pubCap 
					let cardCollectionCap: Capability<&BBxBarbieCard.Collection> = acct.capabilities.storage.issue<&BBxBarbieCard.Collection>(barbieCardCollectionData.storagePath)
					acct.capabilities.publish(cardCollectionCap, at: barbieCardCollectionData.publicPath)
			}
			// Setup Pack Collection

			let barbiePackCollectionData: MetadataViews.NFTCollectionData = BBxBarbiePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
					?? panic("ViewResolver does not resolve NFTCollectionData view")

			// exit if packCollection exists
			if acct.storage.borrow<&BBxBarbiePack.Collection>(from: barbiePackCollectionData.storagePath) == nil {
					// create a new empty packCollection for BBxBarbiePack
					let packCollection: @{NonFungibleToken.Collection} <- BBxBarbiePack.createEmptyCollection(nftType: Type<@BBxBarbiePack.NFT>())

					// save BBxBarbiePack packCollection to the account
					acct.storage.save(<-packCollection, to: barbiePackCollectionData.storagePath)

					// create a public capability for the BBxBarbiePack packCollection
					acct.capabilities.unpublish(barbiePackCollectionData.publicPath) // remove any current pubCap 
					let packCollectionCap: Capability<&BBxBarbiePack.Collection> = acct.capabilities.storage.issue<&BBxBarbiePack.Collection>(barbiePackCollectionData.storagePath)
					acct.capabilities.publish(packCollectionCap, at: barbiePackCollectionData.publicPath)
			}

			if acct.storage.borrow<&NFTStorefrontV2.Storefront>(from: NFTStorefrontV2.StorefrontStoragePath) == nil {
				// Create a new empty Storefront
				let storefront: @NFTStorefrontV2.Storefront <- NFTStorefrontV2.createStorefront()
				
				// save it to the account
				acct.storage.save(<-storefront, to: NFTStorefrontV2.StorefrontStoragePath)

				// create a public capability for the Storefront
				let storefrontPublicCap: Capability<&{NFTStorefrontV2.StorefrontPublic}> = acct.capabilities.storage.issue<&{NFTStorefrontV2.StorefrontPublic}>(
								NFTStorefrontV2.StorefrontStoragePath
						)
				acct.capabilities.publish(storefrontPublicCap, at: NFTStorefrontV2.StorefrontPublicPath)
      }
		}
		execute {
		}
}


```