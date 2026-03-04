# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Oracle/admin_grant_update_role.cdc

```
import SimpleOracle from "../../contracts/SimpleOracle.cdc"

transaction(updater: Address) {
    let updaterCapability: Capability<&{SimpleOracle.DataUpdater}>

    prepare(adminAccount: auth(Capabilities) &Account) {
        self.updaterCapability = adminAccount.capabilities.storage.issue<&{SimpleOracle.DataUpdater}>(SimpleOracle.OracleStoragePath)
    }

    execute {
        let capabilityReceiver = getAccount(updater).capabilities.borrow<&{SimpleOracle.OracleUpdateProxyPublic}>(SimpleOracle.UpdaterPublicPath)
            ?? panic("Could not borrow reference to updater")

        capabilityReceiver.setUpdaterCapability(cap: self.updaterCapability)
    }
}
```