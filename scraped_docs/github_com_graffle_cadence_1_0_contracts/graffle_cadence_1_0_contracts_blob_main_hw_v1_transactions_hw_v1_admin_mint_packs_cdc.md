# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_admin_mint_packs.cdc

```
import "NonFungibleToken"
import "FungibleToken"
import "FlowToken"
import "HWGaragePack"
import "HWGaragePM"
import "MetadataViews"

transaction(address: Address, packID: UInt64, packHash: String) {
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
        let pack: @{NonFungibleToken.NFT} <- self.manager.mintSequentialHWGaragePack(packID: packID, address: address, packHash: packHash)

        let updatePackMetadata: {String: String} = HWGaragePack.getEditionMetadata(pack.id)
        updatePackMetadata["packHash"] = packHash
        updatePackMetadata["seriesNumber"] = "4"
        updatePackMetadata["seriesName"] = "Series 4"
        updatePackMetadata["totalItemCount"] = "7"
        updatePackMetadata["thumbnailCID"] = "QmPcs6V5RfLrCzUm8zfU62UGQWNArKE44xYYof8iA5bRm7"
        updatePackMetadata["thumbnailPath"] = "" // TBD
        self.manager.updatePackEditionMetadata(editionNumber: pack.id, metadata: updatePackMetadata)

        getAccount(address).capabilities.get<&{NonFungibleToken.Receiver}>(HWGaragePack.CollectionPublicPath).borrow()!.deposit(token: <- pack)
    }
}
 
```