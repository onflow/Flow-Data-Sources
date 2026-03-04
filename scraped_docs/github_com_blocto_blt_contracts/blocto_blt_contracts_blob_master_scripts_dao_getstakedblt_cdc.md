# Source: https://github.com/blocto/blt-contracts/blob/master/scripts/dao/getStakedBLT.cdc

```
import BloctoDAO from "../../contracts/flow/dao/BloctoDAO.cdc"

pub fun main(address: Address): UFix64 {
  return BloctoDAO.getStakedBLT(address: address)
}
```