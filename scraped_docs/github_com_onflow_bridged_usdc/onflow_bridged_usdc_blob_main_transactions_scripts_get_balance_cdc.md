# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/scripts/get_balance.cdc

```
// This script reads the balance field
// of an account's USDCFlow Balance

import FungibleToken from "FungibleToken"
import USDCFlow from "USDCFlow"

access(all) fun main(address: Address): UFix64 {
    let account = getAccount(address)
    let vaultRef = account.capabilities.get<&USDCFlow.Vault>
        (USDCFlow.VaultPublicPath)
        .borrow()
        ?? panic("Could not borrow a USDCFlow.Vault reference to the USDCFlow Vault in account"
                .concat(address.toString())
                .concat(". at the path ").concat(USDCFlow.VaultPublicPath.toString())
                .concat(". Make sure the account address is correct and that ")
                .concat("the account being queried has initialized with ")
                .concat("a USDCFlow Vault and valid capability."))

    return vaultRef.balance
}

```