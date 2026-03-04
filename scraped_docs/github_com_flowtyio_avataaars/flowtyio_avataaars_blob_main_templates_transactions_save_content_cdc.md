# Source: https://github.com/Flowtyio/avataaars/blob/main/templates/transactions/save_content.cdc

```
import Components from {{.contractAddress}}

transaction(section: String, name: String, content: [String]) {
    prepare(acct: AuthAccount) {
        let admin = acct.borrow<&Components.Admin>(from: Components.AdminPath)
            ?? panic("admin not found")
        admin.registerContent(component: section, name: name, content: content)
    }
}
```