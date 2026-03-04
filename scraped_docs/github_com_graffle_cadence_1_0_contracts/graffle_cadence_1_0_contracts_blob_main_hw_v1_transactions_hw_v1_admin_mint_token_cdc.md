# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_admin_mint_token.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGarageCard"
import "HWGaragePM"
import "MetadataViews"

transaction(address: Address, packID: UInt64, metadatas: [{String: String}], packHash: String) {
    let manager: &HWGaragePM.Manager
    let recipientCollectionRef: &{NonFungibleToken.Receiver}
    prepare(acct: auth(BorrowValue) &Account) {

        let collectionData: MetadataViews.NFTCollectionData = HWGarageCard.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow a reference to the manager resource
        self.manager = acct.storage.borrow<&HWGaragePM.Manager>(from: HWGaragePM.ManagerStoragePath)
            ?? panic("This account does not have a manager resource.")
        
        // Borrow the recipient's public NFT collection reference
        self.recipientCollectionRef = getAccount(address).capabilities.borrow<&{NonFungibleToken.Receiver}>(
                collectionData.publicPath
            ) ?? panic("Could not get receiver reference to the NFT Collection")
    }

    execute {
        assert(metadatas.length > 0, message: "No quantity provided.")
        for metadata in metadatas {
            let token <- self.manager.mintSequentialHWGarageCard(packID: packID)

            let updatedMetadata: {String: String} = HWGarageCard.getEditionMetadata(UInt64(token.id))
            for key in metadata.keys {
                updatedMetadata[key] = metadata[key]
            }
            self.manager.updateHWGarageCardEditionMetadata(editionNumber: UInt64(token.id), metadata: metadata, packHash: packHash, address: address)
        
            getAccount(address).capabilities.get<&{NonFungibleToken.Receiver}>(HWGarageCard.CollectionPublicPath).borrow()!.deposit(token: <-token)
        }
    }
}
 
```