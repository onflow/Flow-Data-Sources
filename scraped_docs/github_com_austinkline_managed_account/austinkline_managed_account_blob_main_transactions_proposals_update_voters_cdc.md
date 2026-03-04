# Source: https://github.com/austinkline/managed-account/blob/main/transactions/proposals/update_voters.cdc

```
import "ManagedAccount"

transaction(managerAddress: Address, voters: {Address: UFix64}) {
    let voter: auth(ManagedAccount.Propose) &ManagedAccount.Voter

    prepare(acct: auth(Storage) &Account) {
        if acct.storage.type(at: ManagedAccount.VoterStoragePath) == nil {
            let voter <- ManagedAccount.createVoter()
            acct.storage.save(<-voter, to: ManagedAccount.VoterStoragePath)
        }

        self.voter = acct.storage.borrow<auth(ManagedAccount.Propose) &ManagedAccount.Voter>(from: ManagedAccount.VoterStoragePath)
            ?? panic("voter not found in storage path")
    }

    execute {
        let cap = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
        let manager = cap.borrow() ?? panic("manager not found")

        let executable <- ManagedAccount.createChangeVotersExecutable(voters: voters)

        let title = "Update approved Voters"
        let description = "Merges the current set of voters on this manager with a new one. Any voter with an entry of 0.0 will be removed if it is already present"

        self.voter.proposeExecutable(manager: manager, executable: <-executable, title: title, description: description)
    }
}
```