# Source: https://github.com/austinkline/managed-account/blob/main/transactions/setup_manager.cdc

```
import "ManagedAccount"

transaction(voters: {Address: UFix64}) {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        if acct.storage.type(at: ManagedAccount.ManagerStoragePath) == nil {
            let cap = acct.capabilities.account.issue<auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account>() 
            let manager <- ManagedAccount.createManager(acct: cap, voters: voters)
            acct.storage.save(<-manager, to: ManagedAccount.ManagerStoragePath)

            acct.capabilities.publish(
                acct.capabilities.storage.issue<&ManagedAccount.Manager>(ManagedAccount.ManagerStoragePath),
                at: ManagedAccount.ManagerPublicPath
            )
        }
    }
}
```