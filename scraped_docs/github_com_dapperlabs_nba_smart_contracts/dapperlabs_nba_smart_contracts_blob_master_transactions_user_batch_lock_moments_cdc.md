# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/user/batch_lock_moments.cdc

```
import TopShot from 0xTOPSHOTADDRESS
import TopShotMarketV3 from 0xMARKETV3ADDRESS
import NonFungibleToken from 0xNFTADDRESS

// This transaction locks a list of TopShot NFTs rendering them unable to be withdrawn, sold, or transferred

// Parameters
//
// ids: array of TopShot moment Flow IDs
// duration: number of seconds that the moment will be locked for

transaction(ids: [UInt64], duration: UFix64) {
    prepare(acct: auth(BorrowValue) &Account) {
        if let saleRef = acct.storage.borrow<auth(TopShotMarketV3.Cancel) &TopShotMarketV3.SaleCollection>(from: TopShotMarketV3.marketStoragePath) {
            for id in ids {
                saleRef.cancelSale(tokenID: id)
            }
        }

        let collectionRef = acct.storage.borrow<auth(NonFungibleToken.Update) &TopShot.Collection>(from: /storage/MomentCollection)
            ?? panic("Could not borrow from MomentCollection in storage")

        collectionRef.batchLock(ids: ids, duration: duration)
    }
}

```