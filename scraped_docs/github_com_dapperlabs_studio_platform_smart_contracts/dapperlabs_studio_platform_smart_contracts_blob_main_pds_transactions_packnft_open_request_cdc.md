# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/packNFT/open_request.cdc

```
import PackNFT from "PackNFT"
import IPackNFT from "IPackNFT"
import NonFungibleToken from "NonFungibleToken"

transaction(revealID: UInt64) {
    prepare(owner: auth(BorrowValue) &Account) {
        let collectionRef = owner.storage.borrow<auth(NonFungibleToken.Update) &PackNFT.Collection>(from: PackNFT.CollectionStoragePath)
            ?? panic("could not borrow authorized collection")
        collectionRef.emitOpenRequestEvent(id: revealID)
    }
}

```