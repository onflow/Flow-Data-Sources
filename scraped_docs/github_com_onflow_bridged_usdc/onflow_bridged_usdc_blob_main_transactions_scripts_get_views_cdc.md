# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/scripts/get_views.cdc

```
// This script checks the supported views from USDCFlow
// are the expected ones. This is merely used in testing.

import "MetadataViews"
import "USDCFlow"
import "FungibleTokenMetadataViews"

access(all) fun main(address: Address): [Type] {
    let account = getAccount(address)

    let vaultRef = account.capabilities.get<&USDCFlow.Vault>(USDCFlow.VaultPublicPath)
        .borrow()
        ?? panic("Could not borrow a USDCFlow.Vault reference to the USDCFlow Vault in account"
                .concat(address.toString())
                .concat(". at the path ").concat(USDCFlow.VaultPublicPath.toString())
                .concat(". Make sure the account address is correct and that ")
                .concat("the account being queried has initialized with ")
                .concat("a USDCFlow Vault and valid capability."))

    return vaultRef.getViews()
}

```