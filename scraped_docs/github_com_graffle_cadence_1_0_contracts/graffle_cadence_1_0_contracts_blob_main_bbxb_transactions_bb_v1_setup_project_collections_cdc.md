# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_setup_project_collections.cdc

```
import "NonFungibleToken"
import "MetadataViews"
import "FungibleToken"
import "FlowToken"
import "BBxBarbieToken"
import "BBxBarbieCard"
import "BBxBarbiePack"


transaction() {

    prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
        // Setup Token Collection

        let tokenCollectionData: MetadataViews.NFTCollectionData = BBxBarbieToken.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if tokenCollection exists
        if acct.storage.borrow<&BBxBarbieToken.Collection>(from: tokenCollectionData.storagePath) == nil {
            // create a new empty tokenCollection for BBxBarbieToken
            let tokenCollection: @{NonFungibleToken.Collection} <- BBxBarbieToken.createEmptyCollection(nftType: Type<@BBxBarbieToken.NFT>())

            // save BBxBarbieToken tokenCollection to the account
            acct.storage.save(<-tokenCollection, to: tokenCollectionData.storagePath)

            // create a public capability for the BBxBarbieToken tokenCollection
            acct.capabilities.unpublish(tokenCollectionData.publicPath) // remove any current pubCap 
            let tokenCollectionCap: Capability<&BBxBarbieToken.Collection> = acct.capabilities.storage.issue<&BBxBarbieToken.Collection>(tokenCollectionData.storagePath)
            acct.capabilities.publish(tokenCollectionCap, at: tokenCollectionData.publicPath)
        }



        // Setup Card Collection

        let cardCollectionData: MetadataViews.NFTCollectionData = BBxBarbieCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if cardCollection exists
        if acct.storage.borrow<&BBxBarbieCard.Collection>(from: cardCollectionData.storagePath) == nil {
            // create a new empty cardCollection for BBxBarbieCard
            let cardCollection: @{NonFungibleToken.Collection} <- BBxBarbieCard.createEmptyCollection(nftType: Type<@BBxBarbieCard.NFT>())

            // save BBxBarbieCard cardCollection to the account
            acct.storage.save(<-cardCollection, to: cardCollectionData.storagePath)

            // create a public capability for the BBxBarbieCard cardCollection
            acct.capabilities.unpublish(cardCollectionData.publicPath) // remove any current pubCap 
            let cardCollectionCap: Capability<&BBxBarbieCard.Collection> = acct.capabilities.storage.issue<&BBxBarbieCard.Collection>(cardCollectionData.storagePath)
            acct.capabilities.publish(cardCollectionCap, at: cardCollectionData.publicPath)
        }



        // Setup Pack Collection

        let packCollectionData: MetadataViews.NFTCollectionData = BBxBarbiePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")

        // exit if packCollection exists
        if acct.storage.borrow<&BBxBarbiePack.Collection>(from: packCollectionData.storagePath) == nil {
            // create a new empty packCollection for BBxBarbiePack
            let packCollection: @{NonFungibleToken.Collection} <- BBxBarbiePack.createEmptyCollection(nftType: Type<@BBxBarbiePack.NFT>())

            // save BBxBarbiePack packCollection to the account
            acct.storage.save(<-packCollection, to: packCollectionData.storagePath)

            // create a public capability for the BBxBarbiePack packCollection
            acct.capabilities.unpublish(packCollectionData.publicPath) // remove any current pubCap 
            let packCollectionCap: Capability<&BBxBarbiePack.Collection> = acct.capabilities.storage.issue<&BBxBarbiePack.Collection>(packCollectionData.storagePath)
            acct.capabilities.publish(packCollectionCap, at: packCollectionData.publicPath)
        }

    }
    execute {
    }
}
 
```