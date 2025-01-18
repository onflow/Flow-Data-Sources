# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/accounts/revoke_key.cdc

```
transaction(keyIndex: Int) {
	prepare(signer: auth(RevokeKey) &Account) {
		if let key = signer.keys.get(keyIndex: keyIndex) {
			signer.keys.revoke(keyIndex: keyIndex)
		} else {
            panic("Cannot revoke key: No key with the index "
                  .concat(keyIndex.toString())
                  .concat(" exists on the authorizer's account."))
		}
	}
}
```