# Source: https://github.com/emerald-dao/emerald-id/blob/main/flow/cadence/transactions/create_emeraldid.cdc

```
import EmeraldIdentityLilico from "../EmeraldIdentityLilico.cdc"

transaction(discordID: String) {
    prepare(admin: auth(Storage) &Account, user: &Account) {
        let administrator = admin.storage.borrow<&EmeraldIdentityLilico.Administrator>(from: EmeraldIdentityLilico.AdministratorStoragePath)
                                    ?? panic("Could not borrow the administrator")
        administrator.createEmeraldID(account: user.address, discordID: discordID)
    }

    execute {
        log("Created EmeraldID")
    }
}
```