# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/has_float_collection_setup_batch.cdc

```
import "FLOAT"
import "NonFungibleToken"

access(all) fun main(users: [Address]): Result {
  let addressesNotSetup: [Address] = []
  for user in users {
    let setupCorrectly: Bool = getAccount(user).capabilities.borrow<&FLOAT.Collection>(FLOAT.FLOATCollectionPublicPath) != nil
    if !setupCorrectly {
      addressesNotSetup.append(user)
    }
  }
  return Result(addressesNotSetup.length == 0, addressesNotSetup)
}

access(all) struct Result {
  access(all) let allPass: Bool
  access(all) let addressesNotSetup: [Address]

  init(_ ap: Bool, _ ans: [Address]) {
    self.allPass = ap
    self.addressesNotSetup = ans
  }
}
```