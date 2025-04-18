# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/nodeVersionBeacon/admin/set_version_boundary.cdc

```
import "NodeVersionBeacon"

/// Transaction that allows NodeVersionAdmin to add a new version to the
/// version table defining a version boundary at the targetBlockHeight

transaction(
  newMajor: UInt8,
  newMinor: UInt8,
  newPatch: UInt8,
  newPreRelease: String,
  blockHeight: UInt64
) {

  let NodeVersionBeaconAdminRef: &NodeVersionBeacon.Admin
  let newVersionBoundary: NodeVersionBeacon.VersionBoundary

  prepare(acct: auth(BorrowValue) &Account) {
    // Create the new version from the passed parameters
    let newVersion = NodeVersionBeacon.Semver(
      major: newMajor, minor: newMinor, patch: newPatch, preRelease: newPreRelease
    )

    self.newVersionBoundary = NodeVersionBeacon.VersionBoundary(blockHeight: blockHeight, version: newVersion)

    // Borrow a reference to the NodeVersionAdmin resource
    self.NodeVersionBeaconAdminRef = acct.storage.borrow<&NodeVersionBeacon.Admin>
      (from: NodeVersionBeacon.AdminStoragePath)
      ?? panic("Couldn't borrow NodeVersionBeacon.Admin Resource")
  }

  execute {
    // Add the new version to the version table
    self.NodeVersionBeaconAdminRef.setVersionBoundary(versionBoundary: self.newVersionBoundary)
  }

  post {
    NodeVersionBeacon.getVersionBoundary(effectiveAtBlockHeight: blockHeight).version
        .strictEqualTo(self.newVersionBoundary.version) : "New version was not added to the versionTable"
  }
}

```