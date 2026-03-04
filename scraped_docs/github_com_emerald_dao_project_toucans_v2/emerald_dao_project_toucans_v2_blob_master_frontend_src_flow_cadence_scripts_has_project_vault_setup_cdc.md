# Source: https://github.com/emerald-dao/project-toucans-v2/blob/master/frontend/src/flow/cadence/scripts/has_project_vault_setup.cdc

```
import ExampleToken from "../ExampleToken.cdc"

access(all) fun main(user: Address): Bool {
  let authAccount = getAuthAccount<auth(Storage, Capabilities) &Account>(user)
  return authAccount.storage.borrow<&ExampleToken.Vault>(from: ExampleToken.VaultStoragePath) != nil
}
```