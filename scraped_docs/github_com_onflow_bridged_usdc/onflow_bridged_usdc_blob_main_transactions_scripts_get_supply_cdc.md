# Source: https://github.com/onflow/bridged-usdc/blob/main/transactions/scripts/get_supply.cdc

```
// This script reads the total supply field
// of the USDCFlow smart contract

import USDCFlow from "USDCFlow"

access(all) fun main(): UFix64 {
    return USDCFlow.totalSupply
}
```