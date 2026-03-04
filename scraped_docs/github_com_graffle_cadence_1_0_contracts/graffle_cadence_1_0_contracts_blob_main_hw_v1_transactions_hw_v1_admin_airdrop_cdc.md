# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_admin_airdrop.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGaragePack"
import "HWGaragePM"
import "MetadataViews"

transaction(
    airdropSeriesID: UInt64
    , address: Address
    , tokenMintID: UInt64
    , originalCardSerial: String
    , tokenSerial: String // aka NFT Serial
    , seriesName: String
    , carName: String
    , tokenImageHash: String
    , tokenReleaseDate: String
    , tokenExpireDate: String
    , cardID: UInt64
    , templateID: String
    ) {
    
    let manager: &HWGaragePM.Manager

    let recipientCollectionRef: &{NonFungibleToken.Receiver}

    prepare(acct: auth(BorrowValue) &Account) {

        let collectionData = HWGaragePack.resolveContractView(resourceType: nil, viewType: Type<MetadataViews.NFTCollectionData>()) as! MetadataViews.NFTCollectionData?
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
        let redeemable: @{NonFungibleToken.NFT} <- self.manager.airdropRedeemable(
            airdropSeriesID: airdropSeriesID
            , address: address
            , tokenMintID: tokenMintID
            , originalCardSerial: originalCardSerial
            , tokenSerial: tokenSerial
            , seriesName: seriesName
            , carName: carName
            , tokenImageHash: tokenImageHash
            , tokenReleaseDate: tokenReleaseDate
            , tokenExpireDate: tokenExpireDate
            , cardID: cardID
            , templateID: templateID
            )

        let updateAirdropMetadata = HWGaragePack.getEditionMetadata(redeemable.id)
        updateAirdropMetadata["tokenSerial"] = tokenSerial
        updateAirdropMetadata["name"] = seriesName.concat(" #").concat(redeemable.id.toString())
        updateAirdropMetadata["originalCardSerial"] = originalCardSerial
        updateAirdropMetadata["carName"] = carName // Name
        updateAirdropMetadata["tokenReleaseDate"] = tokenReleaseDate
        updateAirdropMetadata["tokenExpireDate"] = tokenExpireDate
        updateAirdropMetadata["cardID"] = cardID.toString()
        updateAirdropMetadata["templateID"] = templateID
        updateAirdropMetadata["thumbnailCID"] = tokenImageHash
        self.manager.updatePackEditionMetadata(editionNumber: redeemable.id, metadata: updateAirdropMetadata)
        getAccount(address).capabilities.get<&{NonFungibleToken.Receiver}>(HWGaragePack.CollectionPublicPath).borrow()!.deposit(token: <- redeemable)
    }
}
 
```