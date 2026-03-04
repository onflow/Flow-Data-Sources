# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/scripts/get_coa_balance.cdc

```
import "EVM"

access(all)
fun main(address: Address, pathId: Int): UFix64 {
    // COA should be at "EVM_${pathId}"
    // this setting is done to avoid collition, but is only a simple example
    let coaPath = StoragePath(identifier: address.toString().concat("EVM_").concat(pathId.toString()))!
    // Borrow a reference to the COA from the storage location we saved it to
    let coa = getAuthAccount<auth(Storage) &Account>(address).storage.borrow<&EVM.CadenceOwnedAccount>(
        from: coaPath
    ) ?? panic("Could not borrow reference to the COA located at storage slot: ".concat(coaPath.toString()))
    // Get the current balance of this COA
    return coa.balance().inFLOW()
}

```