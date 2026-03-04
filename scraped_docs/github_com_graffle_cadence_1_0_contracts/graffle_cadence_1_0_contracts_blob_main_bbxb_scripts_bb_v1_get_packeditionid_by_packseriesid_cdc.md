# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/bbxb/scripts/bb_v1_get_packEditionId_by_packSeriesId.cdc

```
import "BBxBarbiePM"

access(all) fun main(): AnyStruct {
    return BBxBarbiePM.getPackEditionIdByPackSeriesId()

}

```