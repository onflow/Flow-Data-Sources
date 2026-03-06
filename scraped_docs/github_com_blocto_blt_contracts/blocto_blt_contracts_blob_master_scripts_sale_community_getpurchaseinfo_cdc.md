# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/sale/community/getPurchaseInfo.cdc

```
import BloctoTokenSale from "../../../contracts/flow/sale/BloctoTokenSale.cdc"

pub fun main(address: Address): BloctoTokenSale.PurchaseInfo? {
    return BloctoTokenSale.getPurchase(address: address)
}

```