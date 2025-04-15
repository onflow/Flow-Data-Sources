# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/transactions/bridge/admin/deploy_bridge_accessor.cdc

```
transaction(name: String, code: String, evmAddress: Address) {
  prepare(signer: auth(AddContract) &Account) {
    signer.contracts.add(name: name, code: code.utf8, publishToEVMAccount: evmAddress)
  }
}

```