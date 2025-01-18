# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_config_metadata.cdc

```
import FlowEpoch from "FlowEpoch"

access(all) fun main(): FlowEpoch.Config {
    return FlowEpoch.getConfigMetadata()
}

```