# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_private_paths.cdc

```
access(all)fun main(address: Address): [PrivatePath] {
  let account = getAuthAccount(address)
  let cleandPaths: [PrivatePath] = []
  for path in account.privatePaths {
    cleandPaths.append(path)
  }
  return cleandPaths
}
```