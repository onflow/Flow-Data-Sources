# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_array_addr.cdc

```
import SwapFactory from "../../contracts/SwapFactory.cdc"

access(all) fun main(from: UInt64, to: UInt64): [Address] {
    return SwapFactory.getSlicedPairs(from: from, to: to)
}

```