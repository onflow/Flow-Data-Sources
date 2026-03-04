# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_balance.cdc

```
import FungibleToken from "../../contracts/standard/FungibleToken.cdc"

access(all) fun main(userAddr: Address): [UFix64] {
    
    let flowBalance = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(/public/flowTokenBalance)!.balance
    //let stFlowBalance = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(/public/stFlowTokenBalance)!.balance
    //let usdcBalance = getAccount(userAddr).capabilities.borrow<&{FungibleToken.Balance}>(/public/USDCVaultBalance)!.balance
    return [flowBalance]
}
```