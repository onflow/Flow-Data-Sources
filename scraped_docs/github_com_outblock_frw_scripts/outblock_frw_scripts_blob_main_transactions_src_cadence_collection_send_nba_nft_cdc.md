# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/collection/send_nba_nft.cdc

```
import NonFungibleToken from 0xNonFungibleToken

import <NFT> from <NFTAddress>

transaction(recipientAddr: Address, withdrawID: UInt64) {
    prepare(signer: auth(Storage, BorrowValue) &Account) {
        // get the recipients public account object
        let recipient = getAccount(recipientAddr)
        // borrow a reference to the signer''s NFT collection
        let collectionRef = signer.storage
        .borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(from: /storage/MomentCollection)
        ?? panic("Could not borrow a reference to the owner''s collection")
        let senderRef = signer
        .capabilities
        .borrow<&{NonFungibleToken.CollectionPublic}>(/public/MomentCollection)
        // borrow a public reference to the receivers collection
        let recipientRef = recipient
        .capabilities
        .borrow<&{TopShot.MomentCollectionPublic}>(/public/MomentCollection) ?? panic("Unable to borrow receiver reference")
        
        // withdraw the NFT from the owner''s collection
        let nft <- collectionRef.withdraw(withdrawID: withdrawID)
        // Deposit the NFT in the recipient''s collection
        recipientRef!.deposit(token: <-nft)
    }
}
```