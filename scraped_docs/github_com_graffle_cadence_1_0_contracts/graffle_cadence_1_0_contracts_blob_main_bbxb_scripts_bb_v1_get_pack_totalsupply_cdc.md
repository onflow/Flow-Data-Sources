# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_pack_totalSupply.cdc

```
import "BBxBarbiePack"

access(all) fun main(): UInt64 {
    return BBxBarbiePack.getTotalSupply()
}

```