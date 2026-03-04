# Source: https://github.com/austinkline/managed-account/blob/main/transactions/proposals/update_contracts.cdc

```
import "ManagedAccount"
import "ContractUpdateExecutable"

transaction(managerAddress: Address, names: [String], code: [String], isUpdate: [Bool]) {
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
        let mutations: [ContractUpdateExecutable.ContractMutation] = []
        var idx = 0
        while idx < names.length {
            let m = ContractUpdateExecutable.ContractMutation(name: names[idx], content: code[idx], isUpdate: isUpdate[idx])
            mutations.append(m)

            idx = idx + 1
        }
        

        let cap = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
        let manager = cap.borrow() ?? panic("manager not found")
    
        let executable <- ContractUpdateExecutable.createContractUpdateExecutable(mutations: mutations)
        
        let title = "Update contract definitions"
        let description = "Updates contract definitions according to the mutations provided."
            .concat(" The mutations will be performed in the order they are encoded.")
        self.voter.proposeExecutable(manager: manager, executable: <- executable, title: title, description: description)
    }
}
```