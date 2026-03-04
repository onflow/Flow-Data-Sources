# Source: https://github.com/blocto/revv-contracts/blob/master/scripts/getREVVTokenBalance.cdc

```
import "FungibleToken"
import "REVV"

access(all)
fun main(address: Address): UFix64 {
    let balanceRef = getAccount(address).capabilities.borrow<&{FungibleToken.Balance}>(REVV.RevvBalancePublicPath) 
        ?? panic("Could not borrow balance public reference")
    return balanceRef.balance
}

```