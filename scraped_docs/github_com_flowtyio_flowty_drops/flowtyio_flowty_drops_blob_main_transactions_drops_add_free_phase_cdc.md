# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/add_free_phase.cdc

```
import "FlowtyDrops"
import "FlowtyPricers"
import "FlowtyActiveCheckers"
import "FlowtyAddressVerifiers"

import "MetadataViews"

transaction(dropID: UInt64, start: UInt64?, end: UInt64?, displayURL: String) {
    prepare(acct: auth(BorrowValue) &Account) {
        let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
            ?? panic("container not found")
        let drop = container.borrowDrop(id: dropID) ?? panic("drop not found")
        let firstPhase = drop.borrowPhase(index: 0)

        let checker = FlowtyActiveCheckers.TimestampChecker(start: start, end: end)

        var display: MetadataViews.Display? = nil
        if let tmpDisplay = firstPhase.details.display {
            display = MetadataViews.Display(
                name: tmpDisplay.name,
                description: tmpDisplay.description,
                thumbnail: MetadataViews.HTTPFile(url: displayURL)
            )
        }

        let verifier = FlowtyAddressVerifiers.AllowAll(maxPerMint: 1000)

        let details = FlowtyDrops.PhaseDetails(activeChecker: checker, display: display, pricer: FlowtyPricers.Free(), addressVerifier: verifier)
        let phase <- FlowtyDrops.createPhase(details: details)

        drop.addPhase(<- phase)
    }
}
```