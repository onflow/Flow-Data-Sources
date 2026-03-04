# Source: https://github.com/austinkline/managed-account/blob/main/transactions/vote.cdc

```
import "ManagedAccount"

transaction(managerAddress: Address, proposalId: UInt64, approved: Bool) {
    let voter: auth(ManagedAccount.Vote) &ManagedAccount.Voter

    prepare(acct: auth(Storage) &Account) {
        if acct.storage.type(at: ManagedAccount.VoterStoragePath) == nil {
            let voter <- ManagedAccount.createVoter()
            acct.storage.save(<-voter, to: ManagedAccount.VoterStoragePath)
        }

        self.voter = acct.storage.borrow<auth(ManagedAccount.Vote) &ManagedAccount.Voter>(from: ManagedAccount.VoterStoragePath)
            ?? panic("voter not found in storage path")
    }

    execute {
        let managerCap = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
        let manager = managerCap.borrow() ?? panic("manager not found")

        self.voter.vote(manager: manager, proposalId: proposalId, approved: approved)
    }
}
```