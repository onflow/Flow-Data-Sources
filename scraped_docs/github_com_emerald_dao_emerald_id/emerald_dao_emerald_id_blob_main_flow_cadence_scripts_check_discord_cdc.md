# Source: https://github.com/emerald-dao/emerald-id/blob/main/flow/cadence/scripts/check_discord.cdc

```
import EmeraldIdentity from "../EmeraldIdentity.cdc"

pub fun main(user: Address): String? {
  return EmeraldIdentity.getDiscordFromAccount(account: user)
}
```