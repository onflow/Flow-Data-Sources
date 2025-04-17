# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/basic/query/get_contract_names.cdc

```
access(all) fun main(address: Address): &[String] {
  let account = getAccount(address)
  return account.contracts.names
}
```