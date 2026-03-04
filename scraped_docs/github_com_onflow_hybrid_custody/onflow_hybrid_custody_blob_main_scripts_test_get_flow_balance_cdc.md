# Source: https://github.com/onflow/hybrid-custody/blob/main/scripts/test/get_flow_balance.cdc

```
access(all) fun main(address: Address): UFix64 {
    return getAccount(address).balance
}
```