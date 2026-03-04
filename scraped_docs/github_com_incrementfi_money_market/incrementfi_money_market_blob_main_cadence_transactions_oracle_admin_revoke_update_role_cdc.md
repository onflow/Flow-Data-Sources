# Source: https://github.com/IncrementFi/Money-Market/blob/main/cadence/transactions/Oracle/admin_revoke_update_role.cdc

```
// Admin needs to keep track of updaterCapability paths.

/// TODO: figure out how to cancel issued capabilities. Asked in Flow-Discord already.
/// TODO: Probably can use `view fun getController(byCapabilityID: UInt64): &AccountCapabilityController?`
/// TODO:      https://cadence-lang.org/docs/1.0/language/accounts/capabilities
transaction() {
    prepare(adminAccount: &Account) {
        // Note!: Admin needs to keep track of updaterCapability paths.
        // let updaterCapPath: CapabilityPath = /private/oracleUpdater_001
        // adminAccount.unlink(updaterCapPath)
    }
}
```