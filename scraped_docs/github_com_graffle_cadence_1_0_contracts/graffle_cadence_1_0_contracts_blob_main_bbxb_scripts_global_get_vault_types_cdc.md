# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/global_get_vault_types.cdc

```
import "FungibleToken"
import "FungibleTokenSwitchboard"

/// This script reads the stored vault capabilities from a switchboard on the passed account
///
access(all) fun main(account: Address): {Type: Address} {

    // Get a reference to the switchboard conforming to SwitchboardPublic
    let switchboardRef = getAccount(account).capabilities.borrow<&{FungibleTokenSwitchboard.SwitchboardPublic}>(
            FungibleTokenSwitchboard.PublicPath
        ) ?? panic("Could not borrow reference to switchboard")

    // Return the result of `getVaultTypesWithAddress()`
    return switchboardRef.getVaultTypesWithAddress()

}
```