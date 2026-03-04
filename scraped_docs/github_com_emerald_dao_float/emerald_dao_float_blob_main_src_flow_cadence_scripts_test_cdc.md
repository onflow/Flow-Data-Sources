# Source: https://github.com/emerald-dao/float/blob/main/src/flow/cadence/scripts/test.cdc

```

access(all) fun main(): [UInt8] {
  let thing = "02374732ab0".decodeHex()
  return thing
}
```