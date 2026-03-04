# Source: https://github.com/Flowtyio/lost-and-found/blob/main/transactions/depositor/destroy.cdc

```
import "LostAndFound"

transaction {
    prepare(acct: auth(Storage, Capabilities) &Account) {
        let depositor <- acct.storage.load<@AnyResource>(from: LostAndFound.DepositorStoragePath)
        destroy depositor

        acct.capabilities.unpublish(LostAndFound.DepositorPublicPath)
    }
}

```