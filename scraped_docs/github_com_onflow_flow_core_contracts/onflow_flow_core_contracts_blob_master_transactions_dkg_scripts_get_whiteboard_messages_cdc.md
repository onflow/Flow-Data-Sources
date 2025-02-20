# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_whiteboard_messages.cdc

```
import "FlowDKG"

access(all) fun main(): [FlowDKG.Message] {
    return FlowDKG.getWhiteBoardMessages() 
}
```