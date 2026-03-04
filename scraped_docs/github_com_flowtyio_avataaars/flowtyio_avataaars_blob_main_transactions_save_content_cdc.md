# Source: https://github.com/Flowtyio/avataaars/blob/main/transactions/save_content.cdc

```
import "Avataaars"

transaction(section: String, name: String, content: [String]) {
    prepare(acct: AuthAccount) {
        let storagePath = StoragePath(identifier: section.concat("_").concat(name))!
        acct.save(content, to: storagePath)
    }
}
```