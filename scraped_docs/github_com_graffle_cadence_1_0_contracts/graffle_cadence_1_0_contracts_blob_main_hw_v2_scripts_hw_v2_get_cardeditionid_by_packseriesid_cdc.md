# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_cardEditionId_by_packSeriesId.cdc

```
import "HWGaragePMV2"

access(all) fun main(): AnyStruct {
    return HWGaragePMV2.getCardEditionIdByPackSeriesId()
}

```