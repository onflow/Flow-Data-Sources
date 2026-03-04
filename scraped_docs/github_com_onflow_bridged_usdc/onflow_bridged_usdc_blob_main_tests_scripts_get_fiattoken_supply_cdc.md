# Source: https://github.com/onflow/bridged-usdc/blob/main/tests/scripts/get_fiattoken_supply.cdc

```
// This script reads the total supply field
// of the FiatToken smart contract

import FiatToken from "FiatToken"

access(all) fun main(): UFix64 {
    return FiatToken.totalSupply
}

```