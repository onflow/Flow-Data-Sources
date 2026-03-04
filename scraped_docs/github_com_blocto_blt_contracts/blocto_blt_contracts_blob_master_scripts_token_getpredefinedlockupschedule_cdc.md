# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/token/getPredefinedLockupSchedule.cdc

```
import BloctoPass from "../../contracts/flow/token/BloctoPass.cdc"

pub fun main(id: Int): {UFix64: UFix64} {
    return BloctoPass.getPredefinedLockupSchedule(id: id)
}

```