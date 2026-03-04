# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/withdrawFromVaultProxy.cdc

```
import REVV from "../contracts/flow/REVV.cdc"
import REVVVaultAccess from "../contracts/flow/REVVVaultAccess.cdc"

transaction(amount: UFix64) {
    let vaultProxyRef: &REVVVaultAccess.VaultProxy
    let ownedRevvVaultRef: &REVV.Vault 
    prepare(acct: AuthAccount) {
        self.vaultProxyRef = acct.borrow<&REVVVaultAccess.VaultProxy>(from: REVVVaultAccess.VaultProxyStoragePath)!
        self.ownedRevvVaultRef = acct.borrow<&REVV.Vault>(from: REVV.RevvVaultStoragePath)!
    }
    execute {
        let tempVault <- self.vaultProxyRef.withdraw(amount: amount)
        self.ownedRevvVaultRef.deposit(from: <- tempVault)
    }
}
```