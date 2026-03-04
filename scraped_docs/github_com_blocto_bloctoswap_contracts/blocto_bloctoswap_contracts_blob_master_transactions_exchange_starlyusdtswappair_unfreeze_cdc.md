# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/transactions/exchange/StarlyUsdtSwapPair/unfreeze.cdc

```
import "StarlyUsdtSwapPair"

transaction {
  prepare(signer: auth(BorrowValue) &Account) {
    let adminRef = signer.storage.borrow<&StarlyUsdtSwapPair.Admin>(from: /storage/StarlyUsdtSwapAdmin)
      ?? panic("Could not borrow a reference to the admin resource")

    adminRef.unfreeze()
  }
}

```