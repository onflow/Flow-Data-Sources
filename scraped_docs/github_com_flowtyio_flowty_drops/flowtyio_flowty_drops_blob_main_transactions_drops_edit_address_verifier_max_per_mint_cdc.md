# Source: https://github.com/Flowtyio/flowty-drops/blob/main/transactions/drops/edit_address_verifier_max_per_mint.cdc

```
import "FlowtyDrops"
import "FlowtyAddressVerifiers"

transaction(dropID: UInt64, phaseIndex: Int, maxPerMint: Int) {
    prepare(acct: auth(BorrowValue) &Account) {
        let container = acct.storage.borrow<auth(FlowtyDrops.Owner) &FlowtyDrops.Container>(from: FlowtyDrops.ContainerStoragePath)
            ?? panic("container not found")
        let drop = container.borrowDrop(id: dropID) ?? panic("drop not found")
        let phase = drop.borrowPhase(index: phaseIndex)
        let v = phase.borrowAddressVerifierAuth() as! auth(Mutate) &FlowtyAddressVerifiers.AllowAll
        v.setMaxPerMint(maxPerMint)
    }
}
```