# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_current_node_version_as_string.cdc

```
import NodeVersionBeacon from "NodeVersionBeacon"

/// Gets the current version defined in the versionTable
/// as a String.
access(all) fun main(): String {
    let boundary = NodeVersionBeacon.getCurrentVersionBoundary()
    return boundary.version.toString()
}

```