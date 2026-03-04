# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/scripts/get_COA_flow.cdc

```
import "EVM"

access(all)
fun main(address: Address): UFix64 {
     let account = getAuthAccount<auth(Storage) &Account>(address)

    let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(
        from: /storage/evm
    ) ?? panic("Could not borrow reference to the COA!")
    
    return coa.balance().inFLOW()
}

```