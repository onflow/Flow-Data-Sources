# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/admin/mint_moment_with_subedition.cdc

```
import TopShot from 0xTOPSHOTADDRESS

// This transaction is what an admin would use to mint a single new moment
// and deposit it in a user's collection

// Parameters:
//
// setID: the ID of a set containing the target play
// playID: the ID of a play from which a new moment is minted
// subeditionID: the ID of play's subedition
// recipientAddr: the Flow address of the account receiving the newly minted moment

transaction(setID: UInt32, playID: UInt32, subeditionID: UInt32, recipientAddr: Address) {
    // local variable for the admin reference
    let adminRef: &TopShot.Admin

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the Admin resource in storage
        self.adminRef = acct.storage.borrow<&TopShot.Admin>(from: /storage/TopShotAdmin)!
    }

    execute {
        // Borrow a reference to the specified set
        let setRef = self.adminRef.borrowSet(setID: setID)

        // Mint a new NFT with Subedition
        let moment1 <- setRef.mintMomentWithSubedition(playID: playID, subeditionID: subeditionID)

        // get the public account object for the recipient
        let recipient = getAccount(recipientAddr)

        // get the Collection reference for the receiver
        let receiverRef = recipient.capabilities.borrow<&{TopShot.MomentCollectionPublic}>(/public/MomentCollection)
            ?? panic("Cannot borrow a reference to the recipient's moment collection")

        // deposit the NFT in the receivers collection
        receiverRef.deposit(token: <-moment1)
    }
}
```