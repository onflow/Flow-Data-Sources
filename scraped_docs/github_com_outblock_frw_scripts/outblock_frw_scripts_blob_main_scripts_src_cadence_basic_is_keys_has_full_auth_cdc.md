# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/basic/is_keys_has_full_auth.cdc

```

access(all) fun main(address: Address, publicKeys: [String]): Bool {
  let account = getAccount(address)
  var weight: UFix64 = 0.0
  fun accountFn(accountKey: AccountKey): Bool {
    let key = String.encodeHex(accountKey.publicKey.publicKey)
    if publicKeys.contains(key) && !accountKey.isRevoked {
      weight = weight + accountKey.weight 
    }
    return false
  }
  account.keys.forEach(accountFn)

  return weight >= UFix64(1000)
}

```