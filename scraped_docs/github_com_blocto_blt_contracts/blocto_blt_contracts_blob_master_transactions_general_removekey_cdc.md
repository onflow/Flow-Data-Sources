# Source: https://github.com/blocto/blt-contracts/blob/master/transactions/general/removeKey.cdc

```
transaction(keyIndex: Int) {
  prepare(signer: AuthAccount) {
    // revoke old recovery key
		signer.keys.revoke(keyIndex: keyIndex)
  }
}

```