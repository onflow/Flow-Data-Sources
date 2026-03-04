# Source: https://github.com/Flowtyio/flow-raffle/blob/main/transactions/create_raffle_source.cdc

```
import "FlowtyRaffleSource"

transaction(type: Type, path: StoragePath) {
    prepare(acct: auth(Capabilities, Storage) &Account) {
        let source <- FlowtyRaffleSource.createRaffleSource(entryType: type, removeAfterReveal: false)
        let t = source.getEntryType()
        assert(t == type)

        acct.storage.save(<-source, to: path)
    }
}
```