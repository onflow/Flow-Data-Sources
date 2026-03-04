# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/scripts/exchange/FlowUsdtSwapPair/getPoolAmounts.cdc

```
import FlowSwapPair from "../../../contracts/exchange/FlowSwapPair.cdc"

pub fun main(): FlowSwapPair.PoolAmounts {
  return FlowSwapPair.getPoolAmounts()
}

```