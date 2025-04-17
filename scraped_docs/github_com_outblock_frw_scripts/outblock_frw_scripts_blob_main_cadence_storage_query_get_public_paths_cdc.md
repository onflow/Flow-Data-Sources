# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/storage/query/get_public_paths.cdc

```
pub fun main(address: Address): [PublicPath] {
  let account = getAuthAccount(address)
  let cleandPaths: [PublicPath] = []
  for path in account.publicPaths {
    cleandPaths.append(path)
  }
  return cleandPaths
}
```