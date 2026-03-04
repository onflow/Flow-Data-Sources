# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/scripts/Oracle/check_updater_setup.cdc

```
import SimpleOracle from "../../contracts/SimpleOracle.cdc"

/// Checks whether an updater account has been properly setup or not.
access(all) fun main(updater: Address): Bool {
    let updateCapability = getAccount(updater)
        .capabilities.borrow<&{SimpleOracle.OracleUpdateProxyPublic}>(SimpleOracle.UpdaterPublicPath)
    if (updateCapability != nil && updateCapability!.isUpdaterCapabilityGranted()) {
        return true
    } else {
        return false
    }
}
```