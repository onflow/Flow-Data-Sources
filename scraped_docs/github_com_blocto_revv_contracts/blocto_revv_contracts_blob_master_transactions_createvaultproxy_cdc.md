# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/createVaultProxy.cdc

```
import REVVVaultAccess from "../contracts/flow/REVVVaultAccess.cdc"

transaction {
    prepare(acct: AuthAccount) {
        let vaultProxy <- REVVVaultAccess.createVaultProxy()
        acct.save(<- vaultProxy, to: REVVVaultAccess.VaultProxyStoragePath)
        acct.link<&REVVVaultAccess.VaultProxy{REVVVaultAccess.VaultProxyPublic}>(REVVVaultAccess.VaultProxyPublicPath, target: REVVVaultAccess.VaultProxyStoragePath)
    }
}
```