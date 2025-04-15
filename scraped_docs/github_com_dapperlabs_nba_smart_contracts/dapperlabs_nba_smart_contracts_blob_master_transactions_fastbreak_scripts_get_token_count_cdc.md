# Source: https://github.com/dapperlabs/nba-smart-contracts/blob/master/transactions/fastbreak/scripts/get_token_count.cdc

```
import FastBreakV1 from 0xFASTBREAKADDRESS

access(all) fun main(): UInt64 {

    return FastBreakV1.totalSupply
}
```