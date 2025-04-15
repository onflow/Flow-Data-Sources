# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/evm/check_coa_link.cdc

```
import EVM from 0xEVM

/// Returns whether a COA is stored and its public capability is published
///
/// @param flowAddress: The Flow address to check for a COA
///
/// @return Bool: Whether a COA is stored and its public capability is published, nil if no COA is stored
///
access(all) fun main(flowAddress: Address): Bool? {
    // Borrow the COA to check if one is stored
    if let address: EVM.EVMAddress = getAuthAccount<auth(BorrowValue) &Account>(flowAddress)
        .storage.borrow<&EVM.CadenceOwnedAccount>(from: /storage/evm)?.address() {
        // COA found - check if the public capability is published
        return getAccount(flowAddress).capabilities.borrow<&EVM.CadenceOwnedAccount>(/public/evm) != nil
    }
    // No COA found - return nil
    return nil
}
```