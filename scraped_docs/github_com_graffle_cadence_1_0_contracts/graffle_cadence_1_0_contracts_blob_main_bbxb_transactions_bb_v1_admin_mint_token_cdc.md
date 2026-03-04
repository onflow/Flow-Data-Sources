# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/transactions/bb_v1_admin_mint_token.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "MetadataViews"
import "FlowToken"

import "BBxBarbiePM"
import "BBxBarbieToken"

transaction(
    address: Address
    , packSeriesID: UInt64
    , metadatas: [{String: String}]
    ) {
    let manager: &BBxBarbiePM.Manager

    let recipientCollectionRef: &{NonFungibleToken.Receiver}

    prepare(acct: auth(BorrowValue) &Account) {

        let collectionData: MetadataViews.NFTCollectionData = BBxBarbieToken.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
            ?? panic("ViewResolver does not resolve NFTCollectionData view")
        
        // borrow a reference to the manager resource
        self.manager = acct.storage.borrow<&BBxBarbiePM.Manager>(from: BBxBarbiePM.ManagerStoragePath)
            ?? panic("This account does not have a manager resource.")
        
        // Borrow the recipient's public NFT collection reference
        self.recipientCollectionRef = getAccount(address).capabilities.borrow<&{NonFungibleToken.Receiver}>(
                collectionData.publicPath
            ) ?? panic("Could not get receiver reference to the NFT Collection")
    }

    execute {
        assert(metadatas.length > 0, message: "No quantity provided.")

        for metadata in metadatas {

            let token <- self.manager.mintSequentialBBxBarbieToken(
            address: address
            , packSeriesID: packSeriesID
            , metadata: metadata
            )
            getAccount(address)
            .capabilities.get<&{NonFungibleToken.Receiver}>(BBxBarbieToken.CollectionPublicPath)
            .borrow()!
            .deposit(
                token: <-token
            )
    }
        }

}
 
```