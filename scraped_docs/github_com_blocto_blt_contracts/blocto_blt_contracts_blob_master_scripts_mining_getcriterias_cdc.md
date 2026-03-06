# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/mining/getCriterias.cdc

```
import BloctoTokenMining from "../../contracts/flow/mining/BloctoTokenMining.cdc"

pub fun main(): {String: BloctoTokenMining.Criterion} {
    return BloctoTokenMining.getCriteria()
}

```