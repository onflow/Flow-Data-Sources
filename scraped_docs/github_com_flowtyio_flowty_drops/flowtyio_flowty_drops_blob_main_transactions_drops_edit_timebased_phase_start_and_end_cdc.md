# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/edit_timebased_phase_start_and_end.cdc

```
import "FlowtyDrops"
import "FlowtyActiveCheckers"

transaction(dropID: UInt64, phaseIndex: Int, start: UInt64?, end: UInt64?) {
    prepare(acct: auth(BorrowValue) &Account) {
        let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
            ?? panic("container not found")
        let drop = container.borrowDrop(id: dropID) ?? panic("drop not found")
        let phase = drop.borrowPhase(index: phaseIndex)

        let tmp = phase.borrowActiveCheckerAuth()
        let s = tmp as! auth(Mutate) &FlowtyActiveCheckers.TimestampChecker

        s.setStart(start: start)
        s.setEnd(end: end)
    }
}
```