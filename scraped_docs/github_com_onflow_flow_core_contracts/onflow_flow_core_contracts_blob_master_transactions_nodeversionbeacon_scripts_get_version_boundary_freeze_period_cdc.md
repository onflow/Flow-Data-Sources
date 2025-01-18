# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_version_boundary_freeze_period.cdc

```
import NodeVersionBeacon from "NodeVersionBeacon"

/// Returns the versionBoundaryFreezePeriod which defines the minimum number of blocks
/// that must pass between updating a version and its defined block height
/// boundary
access(all) fun main(): UInt64 {
    return NodeVersionBeacon.getVersionBoundaryFreezePeriod()
}
```