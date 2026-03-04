# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/blackhole/get-blackholes.cdc

```
import "BlackHole"

access(all)
fun main(): [Address] {
    return BlackHole.getRegisteredBlackHoles()
}

```