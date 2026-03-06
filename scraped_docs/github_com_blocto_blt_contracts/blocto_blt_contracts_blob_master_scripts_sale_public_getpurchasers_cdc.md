# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/sale/public/getPurchasers.cdc

```
import BloctoTokenPublicSale from "../../../contracts/flow/sale/BloctoTokenPublicSale.cdc"

pub fun main(): [Address] {
    return BloctoTokenPublicSale.getPurchasers()
}

```