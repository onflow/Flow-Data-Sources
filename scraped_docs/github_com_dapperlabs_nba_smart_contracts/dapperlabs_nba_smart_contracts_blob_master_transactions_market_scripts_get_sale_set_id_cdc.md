# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/market/scripts/get_sale_set_id.cdc

```
import Market from 0xMARKETADDRESS

// This script gets the setID of a moment in an account's sale collection
// by looking up its unique ID

// Parameters:
//
// sellerAddress: The Flow Address of the account whose sale collection needs to be read
// momentID: The unique ID for the moment whose data needs to be read

// Returns: UInt32
// The setID of moment with specified ID

access(all) fun main(sellerAddress: Address, momentID: UInt64): UInt32 {

    let saleRef =  getAccount(sellerAddress).capabilities.borrow<&Market.SaleCollection>(/public/topshotSaleCollection)
        ?? panic("Could not get public sale reference")

    let token = saleRef.borrowMoment(id: momentID)
        ?? panic("Could not borrow a reference to the specified moment")

    let data = token.data

    return data.setID
}
```