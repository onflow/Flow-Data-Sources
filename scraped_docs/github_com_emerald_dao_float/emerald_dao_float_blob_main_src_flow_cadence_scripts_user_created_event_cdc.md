# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/user_created_event.cdc

```
import "FLOAT"

access(all) fun main(user: Address, eventId: UInt64): Bool {
  let authAccount = getAuthAccount<auth(Storage) &Account>(user)
  if let floatEventCollection = authAccount.storage.borrow<&FLOAT.FLOATEvents>(from: FLOAT.FLOATEventsStoragePath) {
    return floatEventCollection.getIDs().contains(eventId)
  }

  return false
}
```