# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/remove_last_phase.cdc

```
import "FlowtyDrops"
import "FlowtyPricers"

transaction(dropID: UInt64, start: UInt64?, end: UInt64?) {
    prepare(acct: auth(BorrowValue) &Account) {
        let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
            ?? panic("container not found")
        let drop = container.borrowDrop(id: dropID) ?? panic("drop not found")
        let firstPhase = drop.borrowPhase(index: 0)

        let phases = drop.borrowAllPhases()
        destroy drop.removePhase(index: phases.length - 1)
    }
}
```