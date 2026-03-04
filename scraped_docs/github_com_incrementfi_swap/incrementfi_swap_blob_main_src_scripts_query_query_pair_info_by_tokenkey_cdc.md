# Source: https://github.com/IncrementFi/Swap/blob/main/src/scripts/query/query_pair_info_by_tokenkey.cdc

```
import SwapFactory from "../../contracts/SwapFactory.cdc"
import StableSwapFactory from "../../contracts/StableSwapFactory.cdc"

access(all) fun main(token0Key: String ,token1Key: String, stableMode: Bool): AnyStruct? {
    if stableMode {
        return StableSwapFactory.getPairInfo(token0Key: token0Key, token1Key: token1Key)
    } else {
        return SwapFactory.getPairInfo(token0Key: token0Key, token1Key: token1Key)
    }
}
```