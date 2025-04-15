# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/evm/fund_coa.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM

transaction(amount: UFix64) {
    let sentVault: @FlowToken.Vault
    let auth: auth(Storage) &Account
    let coa: &EVM.CadenceOwnedAccount

    prepare(signer: auth(Storage) &Account) {
        let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(
            from: /storage/flowTokenVault
        ) ?? panic("Could not borrow reference to the owner's Vault!")


        let coa = signer.storage.borrow<&EVM.CadenceOwnedAccount>(
            from: /storage/evm
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