# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/hybrid-custody/has_owned_accounts.cdc

```
import "HybridCustody"

/// Returns whether the given Address has a HybridCustod.Manager with owned accounts or not
///
access(all) fun main(parent: Address): Bool {
    let acct = getAuthAccount<auth(Storage) &Account>(parent)
    if let manager = acct.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath) {
        return manager.getOwnedAddresses().length > 0
    }
    return false
}

```