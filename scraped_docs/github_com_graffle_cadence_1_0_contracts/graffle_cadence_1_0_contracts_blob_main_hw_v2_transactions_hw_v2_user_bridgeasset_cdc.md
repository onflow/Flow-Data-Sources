# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_user_bridgeAsset.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"

import "HWGarageCard"
import "HWGaragePack"

import "HWGarageTokenV2"
import "HWGarageCardV2"
import "HWGaragePackV2"
import "HWGaragePMV2"

transaction(
    waxWallet: String
    , assetIds: [String]
    ) {

        let flowWallet: Address

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        // Setup V1
        // Setup Pack Collection

        let packCollectionDataV1: MetadataViews.NFTCollectionData = HWGaragePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&HWGaragePack.Collection>(from: packCollectionDataV1.storagePath) == nil {
            // create a new empty packCollection for HWGaragePack
            let packCollection: @{NonFungibleToken.Collection} <- HWGaragePack.createEmptyCollection(nftType: Type<@HWGaragePack.NFT>())

            // save HWGaragePack packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionDataV1.storagePath)

            // create a public capability for the HWGaragePack packCollection
            acct.capabilities.unpublish(packCollectionDataV1.publicPath) // remove any current pubCap 
            let packCollectionCap: Capability<&HWGaragePack.Collection> = acct.capabilities.storage.issue<&HWGaragePack.Collection>(packCollectionDataV1.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionDataV1.publicPath)

        }

        // Setup Card Collection

        let cardCollectionDataV1: MetadataViews.NFTCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&HWGarageCard.Collection>(from: cardCollectionDataV1.storagePath) == nil {
            // create a new empty cardCollection for HWGarageCard
            let cardCollection: @{NonFungibleToken.Collection} <- HWGarageCard.createEmptyCollection(nftType: Type<@HWGarageCard.NFT>())

            // save HWGarageCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionDataV1.storagePath)

            // create a public capability for the HWGarageCard cardCollection
            acct.capabilities.unpublish(cardCollectionDataV1.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&HWGarageCard.Collection> = acct.capabilities.storage.issue<&HWGarageCard.Collection>(cardCollectionDataV1.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionDataV1.publicPath)
        }

        // setup V2
        // Setup Token Collection

        let tokenCollectionDataV2: MetadataViews.NFTCollectionData = HWGarageTokenV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if tokenCollection exists
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



        // Setup Card Collection

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



        // Setup Pack Collection

        let packCollectionDataV2: MetadataViews.NFTCollectionData = HWGaragePackV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&HWGaragePackV2.Collection>(from: packCollectionDataV2.storagePath) == nil {
            // create a new empty packCollection for HWGaragePackV2
            let packCollection: @{NonFungibleToken.Collection} <- HWGaragePackV2.createEmptyCollection(nftType: Type<@HWGaragePackV2.NFT>())

            // save HWGaragePackV2 packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionDataV2.storagePath)

            // create a public capability for the HWGaragePackV2 packCollection
            acct.capabilities.unpublish(packCollectionDataV2.publicPath) // remove any current pubCap 
            let packCollectionCap = acct.capabilities.storage.issue<&HWGaragePackV2.Collection>(packCollectionDataV2.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionDataV2.publicPath)
        }

        
        self.flowWallet = acct.address
    }
    execute {
        // call public function to start migration to Flow
        HWGaragePMV2.migrateAsset(
            waxWallet: waxWallet
            , assetIds: assetIds
            , flowWallet: self.flowWallet
            )
        
    }
}
 
```