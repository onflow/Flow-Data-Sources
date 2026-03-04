# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_pack_totalSupply.cdc

```
import "HWGaragePackV2"

access(all) fun main(): UInt64 {
    return HWGaragePackV2.getTotalSupply()
}

```