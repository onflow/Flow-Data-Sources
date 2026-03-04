# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Query/query_vault_balance.cdc

```
import FungibleToken from "../../contracts/tokens/FungibleToken.cdc"

access(all) fun main(userAddr: Address, vaultPath: PublicPath): UFix64 {
    let vaultBalCap = getAccount(userAddr).capabilities.get<&{FungibleToken.Balance}>(vaultPath)
    if vaultBalCap.check() == false || vaultBalCap.borrow() == nil {
        return 0.0
    }
    return vaultBalCap.borrow()!.balance
}
```