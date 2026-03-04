# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/transactions/exchange/FlowUsdtSwapPair/unfreeze.cdc

```
import "FlowSwapPair"

transaction {
  prepare(signer: auth(BorrowValue) &Account) {
    let adminRef = signer.storage.borrow<&FlowSwapPair.Admin>(from: /storage/flowSwapPairAdmin)
      ?? panic("Could not borrow a reference to the admin resource")

    adminRef.unfreeze()
  }
}

```