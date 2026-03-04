# Source: https://github.com/Noah-Overflow/Cadence-Arch-example/blob/main/transactions/fund_COA.cdc

```

import "FungibleToken"
import "FlowToken"
import "EVM"

transaction(amount: UFix64, pathId: Int) {
    let sentVault: @FlowToken.Vault
    let auth: auth(Storage) &Account
    let coa: &EVM.CadenceOwnedAccount

    prepare(signer: auth(Storage) &Account) {
        // COA should be at "EVM_${pathId}"
        // this setting is done to avoid collition, but is only a simple example
        let coaPath = StoragePath(identifier: signer.address.toString().concat("EVM_").concat(pathId.toString()))!
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(
            from: /storage/flowTokenVault
        ) ?? panic("Could not borrow reference to the owner's Vault!")


        let coa = signer.storage.borrow<&EVM.CadenceOwnedAccount>(
            from: coaPath
        ) ?? panic("Could not borrow reference to the COA!")

        self.sentVault <- vaultRef.withdraw(amount: amount) as! @FlowToken.Vault
        self.auth = signer
        self.coa = coa
    }

    execute {
        self.coa.deposit(from: <-self.sentVault)
    }
}


```