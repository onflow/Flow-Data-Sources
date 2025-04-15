# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/get_account_info.cdc

```
access(all) struct Result {
  access(all) let address: Address
  access(all) let balance: UFix64
  access(all) let availableBalance: UFix64
  access(all) let storageUsed: UInt64
  access(all) let storageCapacity: UInt64
  access(all) let storageFlow: UFix64

  init(
    address: Address,
    balance: UFix64,
    availableBalance: UFix64,
    storageUsed: UInt64,
    storageCapacity: UInt64,
    storageFlow: UFix64,
  ) {
    self.address = address
    self.balance = balance
    self.availableBalance = availableBalance
    self.storageUsed = storageUsed
    self.storageCapacity = storageCapacity
    self.storageFlow = storageFlow
  }
}

access(all) fun main(address: Address): Result {
  let account = getAccount(address)
  return Result(
    address: account.address,
    balance: account.balance,
    availableBalance: account.availableBalance,
    storageUsed: account.storage.used,
    storageCapacity: account.storage.capacity,
    storageFlow: account.balance - account.availableBalance
  )
}
```