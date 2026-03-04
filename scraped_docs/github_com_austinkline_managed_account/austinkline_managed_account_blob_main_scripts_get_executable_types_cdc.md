# Source: https://github.com/austinkline/managed-account/blob/main/scripts/get_executable_types.cdc

```
import "ManagedAccount"

access(all) fun main(managerAddress: Address): [String] {
    let manager = getAccount(managerAddress).capabilities.get<&ManagedAccount.Manager>(ManagedAccount.ManagerPublicPath)
        .borrow() ?? panic("manager not found")
    let approvedTypes: [String] = []

    let approved = manager.getApprovedExecutableTypes()
    for type in approved.keys {
        if approved[type] == true {
            approvedTypes.append(type.identifier)
        }
    }

    return approvedTypes
}
```