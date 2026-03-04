# Source: https://github.com/flovatar/flovatar/blob/main/legacy/scripts/get_community_dust.cdc

```
import FlovatarInbox from "../contracts/FlovatarInbox.cdc"

pub fun main() : UFix64 {

    return FlovatarInbox.getCommunityDustBalance()
}
```