# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/blackhole/samples/vanish-flow-token.cdc

```
import "FlowToken"
import "FungibleToken"
import "BlackHole"

transaction(
    amount: UFix64
) {
    let flowVaultRef: auth(FungibleToken.Withdraw) &FlowToken.Vault

    prepare(acct: auth(BorrowValue) &Account) {
        self.flowVaultRef = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
            ?? panic("Could not borrow a reference to the Flow Vault!")
    }

    execute {
        log("Before withdrawal:".concat(self.flowVaultRef.balance.toString()))
        BlackHole.vanish(<- self.flowVaultRef.withdraw(amount: amount))
        log("After withdrawal:".concat(self.flowVaultRef.balance.toString()))
    }
}

```