# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/flowToken/scripts/get_supply.cdc

```
// This script reads the total supply field
// of the FlowToken smart contract

import "FlowToken"

access(all) fun main(): UFix64 {

    let supply = FlowToken.totalSupply

    return supply
}
```