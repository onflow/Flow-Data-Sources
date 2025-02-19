# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_current_node_version.cdc

```
import "NodeVersionBeacon"

/// Gets the current version defined in the contract's versionTable
access(all) fun main(): NodeVersionBeacon.Semver {
    return NodeVersionBeacon.getCurrentVersionBoundary().version
}

```