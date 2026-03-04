# Source: https://github.com/blocto/revv-contracts/blob/master/scripts/getFlowLogoURL.cdc

```
import "FlowToken"

access(all)
fun main(): String {
    return FlowToken.getLogoURI()
}
```