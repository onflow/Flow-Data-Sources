# Source: https://github.com/blocto/bloctoswap-contracts/blob/master/scripts/exchange/BltUsdtSwapPair/getPoolAmounts.cdc

```
import BltUsdtSwapPair from "../../../contracts/exchange/BltUsdtSwapPair.cdc"

pub fun main(): BltUsdtSwapPair.PoolAmounts {
  return BltUsdtSwapPair.getPoolAmounts()
}

```