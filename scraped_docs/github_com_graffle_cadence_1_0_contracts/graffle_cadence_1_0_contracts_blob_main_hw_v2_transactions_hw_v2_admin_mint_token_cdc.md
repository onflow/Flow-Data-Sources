# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_admin_mint_token.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "MetadataViews"
import "FlowToken"

import "HWGaragePMV2"
import "HWGarageTokenV2"

transaction(
    address: Address
    , airdropSeriesID: UInt64

    // fields from above will now be included in metadata
    , metadatas: [{String: String}]
    ) {

    let manager: &HWGaragePMV2.Manager

    let recipientCollectionRef: &{NonFungibleToken.Receiver}

    prepare(acct: auth(BorrowValue) &Account) {

        let collectionData: MetadataViews.NFTCollectionData = HWGarageTokenV2.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
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
            let airdropToken <- self.manager.airdropRedeemable(
                airdropSeriesID: airdropSeriesID
                , address: address
                , tokenMintID: metadata["mint"] ?? "N/A"
                , originalCardSerial: metadata["originalCardSerial"] ?? "N/A"
                , tokenSerial: metadata["tokenSerial"] ?? "N/A"
                , seriesName: metadata["seriesName"] ?? "N/A"
                , carName: metadata["originalCarName"] ?? "N/A"
                , tokenImageHash: metadata["thumbnailCID"] ?? "N/A"
                , tokenReleaseDate: metadata["tokenReleaseDate"] ?? "N/A"
                , tokenExpireDate: metadata["tokenExpireDate"] ?? "N/A"
                , card_ID: metadata["card_ID"] ?? "N/A"
                , template_ID: metadata["template_ID"] ?? "N/A"
                , metadata: metadata
                )

            getAccount(address)
            .capabilities.get<&{NonFungibleToken.Receiver}>(HWGarageTokenV2.CollectionPublicPath)
            .borrow()!
            .deposit(
                token: <-airdropToken
            )
        }
    }
}
 
```