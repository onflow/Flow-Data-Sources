# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/transactions/add_contract.cdc

```
transaction(name: String, codeHex: String, arg0: AnyStruct, arg1: AnyStruct) {
    prepare(signer: auth(AddContract) &Account) {
        signer.contracts.add(name: name, code: codeHex.decodeHex(), arg0, arg1)
    }
}
```