# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/market/scripts/get_sale_percentage.cdc

```
import Market from 0xMARKETADDRESS

// This script gets the percentage cut that beneficiary will take
// of moments in an account's sale collection

// Parameters:
//
// sellerAddress: The Flow Address of the account whose sale collection needs to be read

// Returns: UFix64
// The percentage cut of an account's sale collection

access(all) fun main(sellerAddress: Address): UFix64 {

    let acct = getAccount(sellerAddress)

    let collectionRef = acct.capabilities.borrow<&Market.SaleCollection>(/public/topshotSaleCollection)
        ?? panic("Could not borrow capability from public collection")
    
    return collectionRef.cutPercentage
}
```