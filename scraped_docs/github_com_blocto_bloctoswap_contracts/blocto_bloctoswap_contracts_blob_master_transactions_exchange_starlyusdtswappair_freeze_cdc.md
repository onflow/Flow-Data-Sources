# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/transactions/exchange/StarlyUsdtSwapPair/freeze.cdc

```
import StarlyUsdtSwapPair from "../../../contracts/exchange/StarlyUsdtSwapPair.cdc"

transaction {
  // The Admin reference
  let adminRef: &StarlyUsdtSwapPair.Admin

  prepare(signer: AuthAccount) {
    self.adminRef = signer.borrow<&StarlyUsdtSwapPair.Admin>(from: /storage/StarlyUsdtSwapAdmin)
      ?? panic("Could not borrow a reference to Admin")
  }

  execute {
    self.adminRef.freeze()
  }
}

```