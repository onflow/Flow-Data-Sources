# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/get_account_min_flow.cdc

```
access(all) fun main(address: Address): UFix64 {
  let account = getAccount(address)
  return account.balance - account.availableBalance
}
```