# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/shardedCollection/batch_from_sharded.cdc

```
import NonFungibleToken from 0xNFTADDRESS
import TopShot from 0xTOPSHOTADDRESS
import TopShotShardedCollection from 0xSHARDEDADDRESS

// This transaction deposits a number of NFTs to a recipient

// Parameters
//
// recipient: the Flow address who will receive the NFTs
// momentIDs: an array of moment IDs of NFTs that recipient will receive

transaction(recipient: Address, momentIDs: [UInt64]) {

    let transferTokens: @{NonFungibleToken.Collection}
    
    prepare(acct: auth(BorrowValue) &Account) {
        
        self.transferTokens <- acct.storage.borrow<auth(NonFungibleToken.Withdraw) &TopShotShardedCollection.ShardedCollection>(from: /storage/ShardedMomentCollection)!.batchWithdraw(ids: momentIDs)
    }

    execute {

        // get the recipient's public account object
        let recipient = getAccount(recipient)

        // get the Collection reference for the receiver
        let receiverRef = recipient.capabilities.borrow<&{TopShot.MomentCollectionPublic}>(/public/MomentCollection)!

        // deposit the NFT in the receivers collection
        receiverRef.batchDeposit(tokens: <-self.transferTokens)
    }
}
```