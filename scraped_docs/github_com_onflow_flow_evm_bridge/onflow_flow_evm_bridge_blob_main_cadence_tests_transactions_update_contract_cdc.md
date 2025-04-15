# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/transactions/update_contract.cdc

```
transaction(name: String, codeHex: String) {
    prepare(signer: auth(UpdateContract) &Account) {
        signer.contracts.update(name: name, code: codeHex.decodeHex())
    }
}
```