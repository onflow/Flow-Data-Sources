# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/get_contract_by_name.cdc

```
access(all) fun main(address: Address, contractName: String): String? {
  let account = getAccount(address)
  let deployedContract = account.contracts.get(name: contractName)

  return String.fromUTF8(deployedContract?.code!)
}
```