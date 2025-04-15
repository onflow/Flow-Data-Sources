# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/evm/withdraw_coa.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM

transaction(amount: UFix64, address: Address) {
    let sentVault: @FlowToken.Vault

    prepare(signer: auth(Storage, EVM.Withdraw) &Account) {
        let coa = signer.storage.borrow<auth(EVM.Withdraw) &EVM.CadenceOwnedAccount>(
            from: /storage/evm
        ) ?? panic("Could not borrow reference to the COA!")
        let withdrawBalance = EVM.Balance(attoflow: 0)
        withdrawBalance.setFLOW(flow: amount)
        self.sentVault <- coa.withdraw(balance: withdrawBalance) as! @FlowToken.Vault
    }

    execute {
        let account = getAccount(address)
        let receiver = account.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
        receiver.deposit(from: <-self.sentVault)
    }
}

```