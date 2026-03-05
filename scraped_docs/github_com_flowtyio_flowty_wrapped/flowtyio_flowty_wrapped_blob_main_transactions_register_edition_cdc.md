# Source: https://github.com/Flowtyio/flowty-wrapped/blob/main/transactions/register_edition.cdc

```
import "FlowtyWrapped"
import "WrappedEditions"
import "FlowtyRaffles"
import "FlowtyRaffleSource"

// flow transactions send ./transactions/register_edition.cdc false 1703035065 1705195052 "https://storage.googleapis.com/flowty-wrapped-2023-testnet/" QmcvXz8zZ8hZwgH95zVQ8ZEJUZ92oR9MVjCFVYePyCuvxB -n testnet --signer wrapped-testnet
transaction(removeAfterReveal: Bool, start: UInt64?, end: UInt64?, baseImageUrl: String, baseHtmlUrl: String) {
    prepare(acct: auth(Storage) &Account) {
        let raffleManager = acct.storage.borrow<auth(FlowtyRaffles.Manage) &FlowtyRaffles.Manager>(from: FlowtyRaffles.ManagerStoragePath)!

        // make a raffle source which is based on addresses
        let source <- FlowtyRaffleSource.createRaffleSource(entryType: Type<Address>(), removeAfterReveal: removeAfterReveal)

        // fill out raffle details. All we really care about is the start and end here
        let details = FlowtyRaffles.Details(start: start, end: end, display: nil, externalURL: nil, commitBlocksAhead: 0)

        // make the raffle, get its id to pass on to the edition
        let raffleID = raffleManager.createRaffle(source: <- source, details: details, revealers: [])

        // create and register the edition
        let admin = acct.storage.borrow<auth(FlowtyWrapped.Owner) &FlowtyWrapped.Admin>(from: FlowtyWrapped.AdminStoragePath)!
        let edition = WrappedEditions.Edition2023(raffleID: raffleID, baseImageUrl: baseImageUrl, baseHtmlUrl: baseHtmlUrl)
        admin.registerEdition(edition)
    }
}
```