# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/staker/withdraw_rewarded_tokens_locked.cdc

```
import "LockedTokens"
import "FungibleToken"

transaction(amount: UFix64) {

    let holderRef: auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder

    prepare(account: auth(BorrowValue) &Account) {
        self.holderRef = account.storage.borrow<auth(LockedTokens.TokenOperations, FungibleToken.Withdraw) &LockedTokens.TokenHolder>(from: LockedTokens.TokenHolderStoragePath)
            ?? panic("Could not borrow reference to TokenHolder")
    }

    execute {
        let stakerProxy = self.holderRef.borrowStaker()

        stakerProxy.withdrawRewardedTokens(amount: amount)
    }
}

```