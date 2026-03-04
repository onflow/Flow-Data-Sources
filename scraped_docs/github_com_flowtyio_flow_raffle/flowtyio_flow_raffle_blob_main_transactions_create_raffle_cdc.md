# Source: https://github.com/Flowtyio/flow-raffle/blob/main/transactions/create_raffle.cdc

```
import "FlowtyRaffles"
import "FlowtyRaffleSource"
import "MetadataViews"

transaction(type: Type, start: UInt64?, end: UInt64?, name: String, description: String, thumbnail: String, externalURL: String, commitBlocksAhead: UInt64, revealers: [Address]?) {
    prepare(acct: auth(Capabilities, Storage) &Account) {
        let source <- FlowtyRaffleSource.createRaffleSource(entryType: type, removeAfterReveal: false)

        if acct.storage.borrow<&AnyResource>(from: FlowtyRaffles.ManagerStoragePath) == nil {
            acct.storage.save(<-FlowtyRaffles.createManager(), to: FlowtyRaffles.ManagerStoragePath)
            acct.capabilities.publish(
                acct.capabilities.storage.issue<&FlowtyRaffles.Manager>(FlowtyRaffles.ManagerStoragePath),
                at: FlowtyRaffles.ManagerPublicPath
            )
        }

        let manager = acct.storage.borrow<auth(FlowtyRaffles.Manage) &FlowtyRaffles.Manager>(from: FlowtyRaffles.ManagerStoragePath)
            ?? panic("raffles manager not found")

        let display = MetadataViews.Display(
            name: name,
            description: description,
            thumbnail: MetadataViews.HTTPFile(url: thumbnail)
        )
        let details = FlowtyRaffles.Details(start: start, end: end, display: display, externalURL: MetadataViews.ExternalURL(externalURL), commitBlocksAhead: commitBlocksAhead)
        let id = manager.createRaffle(source: <-source, details: details, revealers: revealers)

        // make sure you can borrow the raffle back
        manager.borrowRafflePublic(id: id) ?? panic("raffle not found")
    }
}
```