# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/swap/freeze.cdc

```
import BltUsdtSwapPair from "../../contracts/flow/swap/BltUsdtSwapPair.cdc"

transaction() {
  prepare(swapPairAdmin: AuthAccount) {

    let adminRef = swapPairAdmin.borrow<&BltUsdtSwapPair.Admin>(from: /storage/bltUsdtPairAdmin)
        ?? panic("Could not borrow a reference to Admin")

    adminRef.freeze()
  }
}

```