# Source: https://github.com/austinkline/managed-account/blob/main/transactions/setup_voter.cdc

```
import "ManagedAccount"

transaction {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        if acct.storage.type(at: ManagedAccount.VoterStoragePath) == nil {
            let voter <- ManagedAccount.createVoter()
            acct.storage.save(<-voter, to: ManagedAccount.VoterStoragePath)
        }
    }
}
```