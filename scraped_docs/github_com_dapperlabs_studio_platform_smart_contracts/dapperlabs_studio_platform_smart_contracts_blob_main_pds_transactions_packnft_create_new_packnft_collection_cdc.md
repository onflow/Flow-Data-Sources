# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/packNFT/create_new_packNFT_collection.cdc

```
import PackNFT from "PackNFT"
import NonFungibleToken from "NonFungibleToken"

transaction() {
    prepare (issuer: auth(Storage, Capabilities) &Account) {

        // Check if account already have a PackIssuer resource, if so destroy it
        if issuer.storage.borrow<&PackNFT.Collection>(from: PackNFT.CollectionStoragePath) == nil {
            let collection <- PackNFT.createEmptyCollection(nftType: Type<@PackNFT.NFT>())

            issuer.storage.save(<- collection, to: PackNFT.CollectionStoragePath);
            issuer.capabilities.publish(
                issuer.capabilities.storage.issue<&PackNFT.Collection>(PackNFT.CollectionStoragePath),
                at: PackNFT.CollectionPublicPath
            ) 
        }
    } 
}
 

```