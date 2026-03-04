# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/scripts/hw_v2_get_live_series.cdc

```
import "HWGaragePMV2"

access(all) fun main(): AnyStruct {
    return {
        "getEnabledSeries":HWGaragePMV2.getEnabledSeries(),
        "getEnabledPackSeries": HWGaragePMV2.getEnabledPackSeries(),
        "getEnabledCardSeries": HWGaragePMV2.getEnabledCardSeries(),
        "getEnabledTokenSeries": HWGaragePMV2.getEnabledTokenSeries()
        }
}

```