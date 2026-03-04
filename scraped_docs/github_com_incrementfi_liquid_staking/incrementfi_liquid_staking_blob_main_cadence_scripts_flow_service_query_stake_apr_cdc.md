# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/scripts/flow-service/query_stake_apr.cdc

```
import FlowIDTableStaking from "../../contracts/standard/mainnet/FlowIDTableStaking.cdc"

access(all) fun main(): [AnyStruct] {
    var totalStaked = FlowIDTableStaking.getTotalStaked()
    var totalPayed = FlowIDTableStaking.getEpochTokenPayout()
    totalStaked = 718993681.55853413
    totalPayed = 1288436.00000000
    // apr return totalPay/totalStaked*100.0/7.0*365.0 * 0.92
    return [totalStaked, totalPayed, (totalPayed/totalStaked*2514.6*0.92)]
    //return [totalStaked, totalPayed]
}
```