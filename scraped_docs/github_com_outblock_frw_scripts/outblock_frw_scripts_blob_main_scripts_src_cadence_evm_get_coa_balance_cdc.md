# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/evm/get_coa_balance.cdc

```
import EVM from 0xEVM

access(all)
fun main(address: Address): UFix64 {
     let account = getAuthAccount<auth(Storage) &Account>(address)

    let coa = account.storage.borrow<&EVM.CadenceOwnedAccount>(
        from: /storage/evm
    ) ?? panic("Could not borrow reference to the COA!")
    
    return coa.balance().inFLOW()
}

```