# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/scripts/subeditions/get_nft_subedition.cdc

```
import TopShot from 0xTOPSHOTADDRESS

access(all) fun main(nftID: UInt64): UInt32 {

    let subedition = TopShot.getMomentsSubedition(nftID: nftID)
                ?? panic("Could not find the specified moment")
    return subedition
}
```