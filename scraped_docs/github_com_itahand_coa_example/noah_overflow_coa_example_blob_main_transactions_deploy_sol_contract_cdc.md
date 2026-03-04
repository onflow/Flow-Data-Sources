# Source: https://github.com/Noah-Overflow/COA-Example/blob/main/transactions/deploy_sol_contract.cdc

```
import "EVM"

transaction(code: String, pathId: Int) {
    let coa: auth(EVM.Deploy) &EVM.CadenceOwnedAccount
    

    prepare(signer: auth(Storage) &Account) {
        // COA should be at "EVM_${pathId}"
        // this setting is done to avoid collition, but is only a simple example
        let coaPath = StoragePath(identifier: signer.address.toString().concat("EVM_").concat(pathId.toString()))!
        self.coa = signer.storage.borrow<auth(EVM.Deploy) &EVM.CadenceOwnedAccount>(
        from: coaPath) ?? panic("Could not borrow reference to the COA!")

    }

    execute {
      self.coa.deploy(code: code.decodeHex(),  gasLimit: 15000000, value: EVM.Balance(attoflow: 0))
    }
}
```