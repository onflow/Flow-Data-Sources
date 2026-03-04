# Source: https://github.com/blocto/revv-contracts/blob/master/transactions/teleport/cleanTeleportCustodyAdmin.cdc

```
import "TeleportCustody"

transaction {
  prepare(admin: auth(LoadValue) &Account) {
    destroy <- admin.storage.load<@AnyResource>(from: TeleportCustody.AdminStoragePath)
  }
}

```