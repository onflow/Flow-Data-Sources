# Source: https://github.com/emerald-dao/emerald-id/blob/main/flow/cadence/scripts/check_emeraldid.cdc

```
import EmeraldID from "../EmeraldID.cdc"

pub fun main(user: Address): UInt64? {
  let info = getAccount(user).getCapability(EmeraldID.InfoPublicPath)
              .borrow<&EmeraldID.Info{EmeraldID.InfoPublic}>()
  return info?.uuid
}
```