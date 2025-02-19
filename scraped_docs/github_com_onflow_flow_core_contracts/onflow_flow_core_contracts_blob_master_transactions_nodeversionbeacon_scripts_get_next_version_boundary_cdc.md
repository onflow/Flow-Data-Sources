# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_next_version_boundary.cdc

```
import "NodeVersionBeacon"

/// Retrieves the next version boundary or nil
/// if there is no upcoming version boundary defined
access(all) fun main(): NodeVersionBeacon.VersionBoundary? {
    return NodeVersionBeacon.getNextVersionBoundary()
}

```