# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/marketV3/scripts/get_sale_len.cdc

```
import Market from 0xMARKETADDRESS
import TopShotMarketV3 from 0xMARKETV3ADDRESS

access(all) fun main(sellerAddress: Address): Int {
    let acct = getAccount(sellerAddress)
    let collectionRef = acct.capabilities.borrow<&TopShotMarketV3.SaleCollection>(TopShotMarketV3.marketPublicPath)
        ?? panic("Could not borrow capability from public collection")
    
    return collectionRef.getIDs().length
}
```