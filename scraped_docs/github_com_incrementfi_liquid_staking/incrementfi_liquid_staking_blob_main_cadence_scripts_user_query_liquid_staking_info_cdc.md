# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/user/query_liquid_staking_info.cdc

```
import stFlowToken from "../../contracts/stFlowToken.cdc"
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

access(all) fun main(): {String: AnyStruct} {
    let currentSnapshot = DelegatorManager.borrowCurrentQuoteEpochSnapshot()
    
    return {
        "stFlow total supply": stFlowToken.totalSupply,
        "Unprocessed unstake request": DelegatorManager.requestedToUnstake,
        "Protocol fees": DelegatorManager.getProtocolFeeBalance(),
        "Unstaked vault": DelegatorManager.getTotalUnstakedVaultBalance(),
        "snapshot": currentSnapshot
    }
}
```