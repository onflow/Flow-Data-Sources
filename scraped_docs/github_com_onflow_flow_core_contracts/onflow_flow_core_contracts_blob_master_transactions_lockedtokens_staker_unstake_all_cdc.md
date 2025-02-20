# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/staker/unstake_all.cdc

```
import "LockedTokens"
import "FungibleToken"

transaction() {

    let holderRef: auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder

    prepare(account: auth(BorrowValue) &Account) {
        self.holderRef = account.storage.borrow<auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder>(from: LockedTokens.TokenHolderStoragePath)
            ?? panic("Could not borrow reference to TokenHolder")
    }

    execute {
        let stakerProxy = self.holderRef.borrowStaker()

        stakerProxy.unstakeAll()
    }
}

```