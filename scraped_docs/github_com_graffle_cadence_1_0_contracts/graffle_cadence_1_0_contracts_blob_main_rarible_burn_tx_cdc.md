# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/rarible/burn-tx.cdc

```
import NonFungibleToken from "NonFungibleToken"
import HWGarageCard from "HWGarageCard"

// Burn HWGarageCard on signer account by tokenId
//
transaction(tokenId: UInt64) {
    prepare(account: auth(BorrowValue) &Account) {
        let card: @HWGarageCard.NFT <-account.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Provider}>(from: HWGarageCard.CollectionStoragePath)!.withdraw(withdrawID: tokenId) as! @HWGarageCard.NFT
        
        destroy card
    }
}

```