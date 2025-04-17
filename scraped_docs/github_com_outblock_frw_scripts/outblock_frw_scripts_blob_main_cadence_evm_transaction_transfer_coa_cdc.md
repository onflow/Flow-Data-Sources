# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/transaction/transfer_coa.cdc

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

    self.sentVault <- coa.withdraw(balance: EVM.Balance(attoflow: UInt(amount) * 100000000000000000)) as! @FlowToken.Vault
  }

  execute {
    let account = getAccount(address)
    let receiver = account.capabilities.borrow<&{FungibleToken.Receiver}>(/public/flowTokenReceiver)!
    receiver.deposit(from: <-self.sentVault)
  }
}

```