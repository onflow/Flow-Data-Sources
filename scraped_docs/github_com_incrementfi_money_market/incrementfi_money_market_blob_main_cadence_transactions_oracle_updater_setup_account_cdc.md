# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Oracle/updater_setup_account.cdc

```
import SimpleOracle from "../../contracts/SimpleOracle.cdc"

// Note: Essentially only need to run once.
transaction() {
    prepare(updater: auth(Storage, Capabilities) &Account) {
        destroy <-updater.storage.load<@AnyResource>(from: SimpleOracle.UpdaterStoragePath)
        updater.storage.save(<-SimpleOracle.createUpdateProxy(), to: SimpleOracle.UpdaterStoragePath)
        // Create public capability to OracleUpdateProxy resource that the exposed interface can only be invoked
        // by Oracle resource admin, which is ensured by the type system.
        updater.capabilities.unpublish(SimpleOracle.UpdaterPublicPath)
        updater.capabilities.publish(
            updater.capabilities.storage.issue<&{SimpleOracle.OracleUpdateProxyPublic}>(SimpleOracle.UpdaterStoragePath),
            at: SimpleOracle.UpdaterPublicPath
        )
    }
}
```