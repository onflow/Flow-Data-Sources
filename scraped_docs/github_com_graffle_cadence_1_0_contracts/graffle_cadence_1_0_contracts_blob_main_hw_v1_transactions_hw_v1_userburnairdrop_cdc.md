# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v1/transactions/hw_v1_userBurnAirdrop.cdc

```
import NonFungibleToken from "../contracts/utility/NonFungibleToken.cdc"
import MetadataViews from "../contracts/utility/MetadataViews.cdc"
import HWGaragePack from "../contracts/HWGaragePack.cdc"
import HWGaragePM from "../contracts/HWGaragePM.cdc"

transaction(
    owner: Address
    , tokenSerial: String
    , tokenEditionID: UInt64
    ) {
    
    prepare(acct: auth(BorrowValue) &Account) {
        let airdropInstance <- acct.storage.borrow<auth(NonFungibleToken.Withdraw)&{NonFungibleToken.Provider}>(from: HWGaragePack.CollectionStoragePath)!.withdraw(withdrawID: tokenEditionID) as! @HWGaragePack.NFT
        
        HWGaragePM.burnAirdrop(
            walletAddress: owner
            , tokenSerial: tokenSerial
            , airdropToken: <-airdropInstance
            )
    }

    execute {        
    }
}
 
```