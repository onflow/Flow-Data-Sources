# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/scripts/create_empty_usdc_vault.cdc

```
import "USDCFlow"

access(all)
fun main() {
    let v <- USDCFlow.createEmptyVault(vaultType: Type<@USDCFlow.Vault>())
    log("Vault creation successful")
    destroy v
}

```