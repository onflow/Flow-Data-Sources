# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_card_totalSupply.cdc

```
import "BBxBarbieCard"

access(all) fun main(): UInt64 {
    return BBxBarbieCard.getTotalSupply()
}

```