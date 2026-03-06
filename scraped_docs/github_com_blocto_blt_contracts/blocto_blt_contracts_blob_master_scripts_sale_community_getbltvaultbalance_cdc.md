# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/sale/community/getBLTVaultBalance.cdc

```
import BloctoTokenSale from "../../../contracts/flow/sale/BloctoTokenSale.cdc"

pub fun main(): UFix64 {
    return BloctoTokenSale.getBltVaultBalance()
}

```