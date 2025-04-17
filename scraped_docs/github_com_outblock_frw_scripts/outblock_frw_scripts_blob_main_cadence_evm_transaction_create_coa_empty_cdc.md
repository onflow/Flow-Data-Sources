# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/evm/transaction/create_coa_empty.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import EVM from 0xEVM


transaction() {
  let auth: auth(IssueStorageCapabilityController, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account

  prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
    let vaultRef = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(
      from: /storage/flowTokenVault
    ) ?? panic("Could not borrow reference to the owner's Vault!")
    self.auth = signer
  }

  execute {
    let coa <- EVM.createCadenceOwnedAccount()
    let storagePath = StoragePath(identifier: "evm")!
    let publicPath = PublicPath(identifier: "evm")!
    self.auth.storage.save<@EVM.CadenceOwnedAccount>(<-coa, to: storagePath)
    let addressableCap = self.auth.capabilities.storage.issue<&EVM.CadenceOwnedAccount>(storagePath)
    self.auth.capabilities.unpublish(publicPath)
    self.auth.capabilities.publish(addressableCap, at: publicPath)
  }
}
```