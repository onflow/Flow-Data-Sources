# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Oracle/admin_create_oracle_resource.cdc

```
import LendingInterfaces from "../../contracts/LendingInterfaces.cdc"
import SimpleOracle from "../../contracts/SimpleOracle.cdc"

// Note: Only run once.
//       Any subsequent runs will discard existing Oracle resource and create & link a new one.
transaction() {
    prepare(adminAccount: auth(Storage, Capabilities) &Account) {
        let adminRef = adminAccount.storage.borrow<&SimpleOracle.Admin>(from: SimpleOracle.OracleAdminStoragePath)
            ?? panic("Could not borrow reference to Oracle Admin")

        // Discard any existing contents
        destroy <-adminAccount.storage.load<@AnyResource>(from: SimpleOracle.OracleStoragePath)
        // Create and store a new Oracle resource
        adminAccount.storage.save(<-adminRef.createOracleResource(), to: SimpleOracle.OracleStoragePath)

        // Create a public capability to Oracle resource that only exposes {OraclePublic} interface to public.
        adminAccount.capabilities.unpublish(SimpleOracle.OraclePublicPath)
        adminAccount.capabilities.publish(
            adminAccount.capabilities.storage.issue<&{LendingInterfaces.OraclePublic}>(SimpleOracle.OracleStoragePath),
            at: SimpleOracle.OraclePublicPath
        )
    }
}
```