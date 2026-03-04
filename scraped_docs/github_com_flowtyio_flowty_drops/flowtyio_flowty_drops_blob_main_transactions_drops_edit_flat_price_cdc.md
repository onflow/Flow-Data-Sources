# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/edit_flat_price.cdc

```
import "FlowtyDrops"
import "FlowtyPricers"

transaction(dropID: UInt64, phaseIndex: Int, price: UFix64) {
    prepare(acct: auth(BorrowValue) &Account) {
        let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
            ?? panic("container not found")
        let drop = container.borrowDrop(id: dropID) ?? panic("drop not found")
        let phase = drop.borrowPhase(index: phaseIndex)
        let pricer = phase.borrowPricerAuth() as! auth(Mutate) &FlowtyPricers.FlatPrice
        pricer.setPrice(price: price)
    }   
}
```