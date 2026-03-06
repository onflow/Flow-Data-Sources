# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/sale/community/getPurchasers.cdc

```
import BloctoTokenSale from "../../../contracts/flow/sale/BloctoTokenSale.cdc"

pub fun main(): [Address] {
    return BloctoTokenSale.getPurchasers()
}

```