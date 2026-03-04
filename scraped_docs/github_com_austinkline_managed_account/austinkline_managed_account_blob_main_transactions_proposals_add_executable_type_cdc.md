# Source: https://github.com/austinkline/managed-account/blob/main/transactions/proposals/add_executable_type.cdc

```
import "ManagedAccount"

transaction(managerAddress: Address, executableTypeIdentifier: String, approved: Bool) {
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

        let executableType = CompositeType(executableTypeIdentifier) ?? panic("invalid executable type")
        let executable <- ManagedAccount.createChangeApprovedTypeExecutable(executableType: executableType, approved: approved)

        let title = "Change executable type approval for type ".concat(executableTypeIdentifier).concat(" to ").concat(approved ? "true": "false")
        let description = "Alters the approval of the proposed executable type."
            .concat("If approved is set to true, this will allow the executable to be used by this manager in future proposals.")
            .concat("If approved is set to false, current proposals of the given executable type will not be permitted, ")
            .concat("and future proposals with this executable type will not be able to be added")
        self.voter.proposeExecutable(manager: manager, executable: <-executable, title: title, description: description)
    }
}
```