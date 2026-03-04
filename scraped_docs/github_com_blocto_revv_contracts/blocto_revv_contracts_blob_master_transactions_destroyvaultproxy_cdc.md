# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/destroyVaultProxy.cdc

```
import REVVVaultAccess from "../contracts/flow/REVVVaultAccess.cdc"

transaction {
    prepare(acct: AuthAccount) {
        acct.unlink(REVVVaultAccess.VaultProxyPublicPath)
        let vaultProxy <- acct.load<@AnyResource>(from: REVVVaultAccess.VaultProxyStoragePath)  
        destroy vaultProxy
    }
}
```