# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/collection/send_nft.cdc

```
import NonFungibleToken from 0xNonFungibleToken
import <NFT> from <NFTAddress>

// This transaction is for transferring and NFT from
// one account to another

transaction(recipientAddr: Address, withdrawID: UInt64) {

    prepare(signer: auth(Storage, BorrowValue) &Account) {
        // get the recipients public account object
        let recipient = getAccount(recipientAddr)

        // borrow a reference to the signer's NFT collection
        let collectionRef = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(from: <CollectionStoragePath>)
            ?? panic("Could not borrow a reference to the owner's collection")

        // borrow a public reference to the receivers collection
        let depositRef = recipient
            .capabilities
            .borrow<&{NonFungibleToken.Collection}>(<CollectionPublicPath>)
            ?? panic("Could not borrow a reference to the receiver's collection")

        // withdraw the NFT from the owner's collection
        let nft <- collectionRef.withdraw(withdrawID: withdrawID)

        // Deposit the NFT in the recipient's collection
        depositRef.deposit(token: <-nft)

    }
}
```