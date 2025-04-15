# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/staking/withdraw_locked.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import LockedTokens from 0xLockedTokens

transaction(amount: UFix64) {

    let holderRef: auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder
    let vaultRef: auth(FungibleToken.Withdraw) &FlowToken.Vault

    prepare(acct: auth(BorrowValue) &Account) {
        self.holderRef = acct.storage.borrow<auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder>(from: LockedTokens.TokenHolderStoragePath)
            ?? panic("The primary user account does not have an associated locked account")

        self.vaultRef = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)
            ?? panic("Could not borrow flow token vault ref")
    }

    execute {
        self.vaultRef.deposit(from: <-self.holderRef.withdraw(amount: amount))
    }
}
```