# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/scripts/get_version_boundaries.cdc

```
import "NodeVersionBeacon"

/// Returns the versionBoundaries page for the given page and perPage.
access(all) fun main(page: Int, perPage: Int): NodeVersionBeacon.VersionBoundaryPage {
    return NodeVersionBeacon.getVersionBoundariesPage(page: page, perPage: perPage)
}
```