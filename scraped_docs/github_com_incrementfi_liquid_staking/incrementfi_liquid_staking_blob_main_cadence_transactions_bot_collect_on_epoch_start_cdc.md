# Source: https://github.com/IncrementFi/Liquid-Staking/blob/main/cadence/transactions/bot/collect_on_epoch_start.cdc

```
import DelegatorManager from "../../contracts/DelegatorManager.cdc"

transaction(start: Int, end: Int, ifAdvanceEpoch: Bool) {
    prepare(botAcct: &Account) {
        log("---------> bot: update")
        DelegatorManager.collectDelegatorsOnEpochStart(startIndex: start, endIndex: end, ifAdvanceEpoch: ifAdvanceEpoch)
    }
}
```