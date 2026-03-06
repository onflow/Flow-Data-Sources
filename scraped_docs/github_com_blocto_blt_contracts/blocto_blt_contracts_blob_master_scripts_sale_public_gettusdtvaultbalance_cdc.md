# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/sale/public/gettUSDTVaultBalance.cdc

```
import BloctoTokenPublicSale from "../../../contracts/flow/sale/BloctoTokenPublicSale.cdc"

pub fun main(): UFix64 {
    return BloctoTokenPublicSale.getTusdtVaultBalance()
}

```