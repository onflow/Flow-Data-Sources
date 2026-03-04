# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_admin_mint_card.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "MetadataViews"
import "FlowToken"

import "HWGaragePMV2"
import "HWGarageCardV2"

transaction(
    address: Address
    , packHash: String
    , packSeriesID: UInt64
    , packID: UInt64 // aka packEditionID
    , metadatas: [{String: String}]
    ) {
    let manager: &HWGaragePMV2.Manager
    let recipientCollectionRef: &{NonFungibleToken.Receiver}

    prepare(acct: auth(BorrowValue) &Account) {

        let collectionData: MetadataViews.NFTCollectionData = HWGarageCardV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow a reference to the manager resource
        self.manager = acct.storage.borrow<&HWGaragePMV2.Manager>(from: HWGaragePMV2.ManagerStoragePath)
            ?? panic("This account does not have a manager resource.")
        
        // Borrow the recipient's public NFT collection reference
        self.recipientCollectionRef = getAccount(address).capabilities.borrow<&{NonFungibleToken.Receiver}>(
                collectionData.publicPath
            ) ?? panic("Could not get receiver reference to the NFT Collection")
    }

    execute {
        assert(metadatas.length > 0, message: "No quantity provided.")
        
        
        for metadata in metadatas {
            
            let redeemable: String = metadata["Redeemable"] ?? metadata["redeemable"] ?? "N/A"
 
            let token <- self.manager.mintSequentialHWGarageCardV2(
            address: address
            , packHash: packHash
            , packSeriesID: packSeriesID
            , packEditionID: packID
            , redeemable: redeemable
            , metadata: metadata
            )

            getAccount(address)
            .capabilities.get<&{NonFungibleToken.Receiver}>(HWGarageCardV2.CollectionPublicPath)
            .borrow()!
            .deposit(
                token: <-token
            )
    }
        }
                

}
 
```