# Source: https://github.com/Graffle/cadence-1.0-contracts/blob/main/hw_v2/transactions/hw_v2_add_proposal_keys.cdc

```
transaction(numProposers: UInt16) {  
  prepare(acc: auth(Keys) &Account) {
    let key: AccountKey  = acc.keys.get(keyIndex: 0)!
    var count: UInt16 = 0
    while count < numProposers {
        acc.keys.add(
            publicKey: key.publicKey,
            hashAlgorithm: key.hashAlgorithm,
            weight: 0.0
        )
        count = count + 1
    }
  }
}
```