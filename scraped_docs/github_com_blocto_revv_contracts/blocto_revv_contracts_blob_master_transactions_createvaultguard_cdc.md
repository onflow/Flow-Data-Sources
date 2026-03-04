# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/createVaultGuard.cdc

```
import REVVVaultAccess from "../contracts/flow/REVVVaultAccess.cdc"

transaction(maxAmount: UFix64) {
    prepare(acct: AuthAccount) {
        let adminRef = acct.borrow<&REVVVaultAccess.Admin>(from: REVVVaultAccess.AdminStoragePath)!

        let guardStoragePath: StoragePath = /storage/revvVaultGuard_01  // new path for every guard
        let guardPrivatePath: PrivatePath = /private/revvVaultGuard_01 // new path for every gaurd
        let vaultProxyAddress: Address = 0x01cf0e2f2f715450
        REVVVaultAccess.createVaultGuard(adminRef: adminRef, vaultProxyAddress: vaultProxyAddress, maxAmount: maxAmount, guardStoragePath: guardStoragePath, guardPrivatePath: guardPrivatePath)
    }
    execute {

    }
}
```