# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/scripts/resolve_bridged_token_views.cdc

```
import "FungibleToken"
import "FungibleTokenMetadataViews"

access(all)
fun main(address: Address, vaultPathIdentifier: String): Bool {
    let path = StoragePath(identifier: vaultPathIdentifier) ?? panic("Malformed StoragePath identifier")
    if let vault = getAuthAccount<auth(BorrowValue) &Account>(address).storage.borrow<&{FungibleToken.Vault}>(
            from: path
        ) {
        let ftdisplay = vault.resolveView(Type<FungibleTokenMetadataViews.FTDisplay>()) ?? panic("FTDisplay was not resolved")
        return true
    }
    return false
}

```