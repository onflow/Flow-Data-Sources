# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/fastbreak/scripts/get_fast_break.cdc

```
import FastBreakV1 from 0xFASTBREAKADDRESS

access(all) fun main(id: String): FastBreakV1.FastBreakGame? {

    return FastBreakV1.getFastBreakGame(id: id)
}
```