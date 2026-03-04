# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_card_totalSupply.cdc

```
import "HWGarageCardV2"

access(all) fun main(): UInt64 {
    return HWGarageCardV2.getTotalSupply()
}

```