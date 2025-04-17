# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/transaction/transfer_flow_to_evm_address.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM

transaction(recipientEVMAddressHex: String, amount: UFix64, gasLimit: UInt64) {
  let coa: auth(EVM.Withdraw, EVM.Call) &EVM.CadenceOwnedAccount
  let recipientEVMAddress: EVM.EVMAddress
  var sentVault: @FlowToken.Vault

  prepare(signer: auth(BorrowValue, SaveValue) &Account) {
    if signer.storage.type(at: /storage/evm) == nil {
      signer.storage.save(<-EVM.createCadenceOwnedAccount(), to: /storage/evm)
    }
    self.coa = signer.storage.borrow<auth(EVM.Withdraw, EVM.Call) &EVM.CadenceOwnedAccount>(from: /storage/evm)
      ?? panic("Could not borrow reference to the signer's bridged account")

    let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(
      from: /storage/flowTokenVault
    ) ?? panic("Could not borrow reference to the owner's Vault!")
    self.sentVault <- vaultRef.withdraw(amount: amount) as! @FlowToken.Vault

    self.recipientEVMAddress = EVM.addressFromString(recipientEVMAddressHex)
  }

  execute {
    self.coa.deposit(from: <-self.sentVault)
    
    let valueBalance = EVM.Balance(attoflow: 0)
    valueBalance.setFLOW(flow: amount)
    let txResult = self.coa.call(
      to: self.recipientEVMAddress,
      data: [],
      gasLimit: gasLimit,
      value: valueBalance
    )
    assert(
      txResult.status == EVM.Status.failed || txResult.status == EVM.Status.successful,
      message: "evm_error=".concat(txResult.errorMessage).concat("\n")
    )
  }
}
```