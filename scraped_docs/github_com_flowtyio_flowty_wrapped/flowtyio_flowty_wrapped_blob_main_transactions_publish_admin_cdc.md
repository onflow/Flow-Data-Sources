# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/publish_admin.cdc

```
import "FlowtyWrapped"

transaction(receiver: Address) {
    prepare(acct: auth(Capabilities, Inbox) &Account) {
        let identifier = "FlowtyWrapped_Admin_".concat(receiver.toString())
        let p = PrivatePath(identifier: identifier)!
        let cap = acct.capabilities.storage.issue<&FlowtyWrapped.Admin>(FlowtyWrapped.AdminStoragePath)
        acct.inbox.publish(cap, name: "flowty-wrapped-minter", recipient: receiver)
    }
}
```