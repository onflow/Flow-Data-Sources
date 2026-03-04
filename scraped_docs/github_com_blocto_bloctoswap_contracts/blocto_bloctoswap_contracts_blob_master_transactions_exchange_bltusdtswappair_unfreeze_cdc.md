# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/transactions/exchange/BltUsdtSwapPair/unfreeze.cdc

```
import "BltUsdtSwapPair"

transaction {
  prepare(signer: auth(BorrowValue) &Account) {
    let adminRef = signer.storage.borrow<&BltUsdtSwapPair.Admin>(from: /storage/bltUsdtPairAdmin)
      ?? panic("Could not borrow a reference to the admin resource")

    adminRef.unfreeze()
  }
}

```