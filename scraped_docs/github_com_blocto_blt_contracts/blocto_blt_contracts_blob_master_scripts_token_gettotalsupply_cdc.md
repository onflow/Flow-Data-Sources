# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/token/getTotalSupply.cdc

```
import "BloctoToken"

access(all)
fun main(): UFix64 {
    return BloctoToken.totalSupply
}

```