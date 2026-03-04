# Source: https://github.com/dapperlabs/studio-platform-smart-contracts/blob/main/pds/transactions/keys/revoke-key.cdc

```
transaction(idx: Int) {
    prepare(signer: AuthAccount) {
      let keyA = signer.keys.revoke(keyIndex: idx)
    }
}

```