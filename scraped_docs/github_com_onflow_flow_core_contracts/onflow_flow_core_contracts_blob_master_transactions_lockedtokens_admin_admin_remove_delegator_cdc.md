# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/lockedTokens/admin/admin_remove_delegator.cdc

```
import "FlowIDTableStaking"
import "LockedTokens"

transaction {

    prepare(signer: auth(BorrowValue) &Account) {

        let managerRef = signer.storage.borrow<auth(LockedTokens.UnlockTokens) &LockedTokens.LockedTokenManager>(from: LockedTokens.LockedTokenManagerStoragePath)
            ?? panic("Could not borrow a reference to the locked token manager")

        let delegator <- managerRef.removeDelegator()!

        destroy delegator

    }
}

```