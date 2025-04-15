# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/fastbreak/scripts/get_fast_break_stats.cdc

```
import FastBreakV1 from 0xFASTBREAKADDRESS

access(all) fun main(fastBreakGameID: String): [FastBreakV1.FastBreakStat] {

    return FastBreakV1.getFastBreakGameStats(id: fastBreakGameID)
}
```