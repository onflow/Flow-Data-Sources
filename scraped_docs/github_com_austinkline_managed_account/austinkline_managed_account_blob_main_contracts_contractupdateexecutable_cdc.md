# Source: https://github.com/austinkline/managed-account/blob/main/contracts/ContractUpdateExecutable.cdc

```
import "ManagedAccount"

access(all) contract ContractUpdateExecutable {
    // Defines an executable that can be used to propose changes to an account's deployed contracts.
    // Mutations are executed in order, and must explicitly flag whether it is an update or not.
    access(all) resource Executable: ManagedAccount.Executable {
        access(all) let mutations: [ContractMutation]
        // What is the next mutation that should be run?
        access(all) var nextIndex: Int

        access(contract) fun run(acct: auth(Storage, Contracts, Keys, Inbox, Capabilities) &Account): Bool {
            self.mutations[self.nextIndex].apply(acct: acct)
            self.nextIndex = self.nextIndex + 1
            return self.nextIndex >= self.mutations.length
        }

        access(all) view fun describe(): AnyStruct {
            let data: {String: AnyStruct} = {}
            return data
        }

        init(mutations: [ContractMutation]) {
            self.mutations = mutations

            self.nextIndex = 0
        }
    }

    access(all) struct ContractMutation {
        access(all) let name: String
        access(all) let content: String
        access(all) let isUpdate: Bool

        access(all) fun apply(acct: auth(Contracts) &Account) {
            if self.isUpdate {
                acct.contracts.update(name: self.name, code: self.content.utf8)
            } else {
                acct.contracts.add(name: self.name, code: self.content.utf8)
            }
        }

        init(name: String, content: String, isUpdate: Bool) {
            self.name = name
            self.content = content
            self.isUpdate = isUpdate
        }
    }

    access(all) fun createContractUpdateExecutable(mutations: [ContractMutation]): @Executable {
        return <- create Executable(mutations: mutations)
    }
}
```