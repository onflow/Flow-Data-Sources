# Source: https://github.com/austinkline/managed-account/blob/main/transactions/run.cdc

```
import "ManagedAccount"

transaction(managerAddress: Address, proposalId: UInt64) {
    prepare(acct: &Account) {}

    execute {
        let manager = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
            .borrow() ?? panic("failed to borrow manager for address: ".concat(managerAddress.toString()))
        manager.run(proposalId: proposalId)
    }
}
```