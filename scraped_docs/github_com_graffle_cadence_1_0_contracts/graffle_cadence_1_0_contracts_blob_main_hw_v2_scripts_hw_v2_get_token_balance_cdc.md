# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_token_balance.cdc

```
import "FlowToken"
import "FungibleToken"

access(all) fun main(account: Address): {String: UFix64} {
    let flowCap: PublicPath = /public/flowTokenBalance
    let flowVaultBalance: UFix64 = getAccount(account)
        .capabilities.borrow<&{FungibleToken.Balance}>(flowCap)?.balance
        ?? panic("Could not borrow Balance reference to FLOW Vault")

    let vaultStatus: {String: UFix64} = {}
    
    vaultStatus.insert(key: "FLOW", flowVaultBalance)

    return vaultStatus
}
```