# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/get_stable_swap_pool_info.cdc

```
import ToucansUtils from "../ToucansUtils.cdc"

access(all) fun main(amountIn: UFix64, tokenInKey: String): UFix64 {
    return ToucansUtils.getEstimatedOut(amountIn: amountIn, tokenInKey: tokenInKey)
}
```