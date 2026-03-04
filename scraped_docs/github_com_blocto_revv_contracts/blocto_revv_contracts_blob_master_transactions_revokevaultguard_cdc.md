# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/revokeVaultGuard.cdc

```
import REVVVaultAccess from "../contracts/flow/REVVVaultAccess.cdc"

transaction(vaultProxyAddress: Address) {
    var adminRef: &REVVVaultAccess.Admin
    prepare(acct: AuthAccount) {
        self.adminRef = acct.borrow<&REVVVaultAccess.Admin>(from: REVVVaultAccess.AdminStoragePath)!
    }
    execute {
        REVVVaultAccess.revokeVaultGuard(adminRef: self.adminRef, vaultProxyAddress: vaultProxyAddress)
    }
}
```