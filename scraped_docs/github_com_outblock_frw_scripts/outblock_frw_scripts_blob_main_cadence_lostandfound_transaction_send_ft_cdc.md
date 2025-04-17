# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/transaction/send_ft.cdc

```

import FlowToken from 0xFlowToken
import FungibleToken from 0xFungibleToken
import LostAndFound from 0xLostAndFound
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import FungibleTokenMetadataViews from 0xFungibleToken
import FlowEVMBridgeUtils from 0xFlowEVMBridge


transaction(vaultIdentifier: String, recipient: Address, amount: UFix64, memo: String) {
  let sentVault: @{FungibleToken.Vault}
  let flowProvider: Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault>
  let flowReceiver: Capability<&FlowToken.Vault>
  let receiverCap: Capability<&{FungibleToken.Receiver}>
  let display: MetadataViews.Display?

  prepare(acct: auth(Storage, Capabilities) &Account) {
    let vaultType = CompositeType(vaultIdentifier)
      ?? panic("Could not construct Vault type from identifier: ".concat(vaultIdentifier))
    let tokenContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: vaultType)
      ?? panic("Could not get contract address from identifier: ".concat(vaultIdentifier))
    let tokenContractName = FlowEVMBridgeUtils.getContractName(fromType: vaultType)
      ?? panic("Could not get contract name from identifier: ".concat(vaultIdentifier))
    
    let viewResolver = getAccount(tokenContractAddress).contracts.borrow<&{ViewResolver}>(name: tokenContractName)
      ?? panic("Could not borrow ViewResolver from FungibleToken contract")
    let vaultData = viewResolver.resolveContractView(
        resourceType: nil,
        viewType: Type<FungibleTokenMetadataViews.FTVaultData>()
      ) as! FungibleTokenMetadataViews.FTVaultData? ?? panic("Could not resolve FTVaultData view")

    let vaultDisplay = viewResolver.resolveContractView(
        resourceType: nil,
        viewType: Type<FungibleTokenMetadataViews.FTDisplay>()
      ) as! FungibleTokenMetadataViews.FTDisplay? ?? panic("Could not resolve FTVaultData view")

    self.display = MetadataViews.Display(
      name: vaultDisplay.name,
      description: vaultDisplay.description,
      thumbnail: vaultDisplay.logos.items[0].file
    )

    let vault = acct.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(
        from: vaultData.storagePath
      ) ?? panic("Could not access signer's FungibleToken Vault")

    self.sentVault <- vault.withdraw(amount: amount)

    var provider: Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault>? = nil
    acct.capabilities.storage.forEachController(forPath: /storage/flowTokenVault, fun(c: &StorageCapabilityController): Bool {
      if c.borrowType == Type<auth(FungibleToken.Withdraw) &FlowToken.Vault>() {
        provider = c.capability as! Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault>
      }
      return true
    })

    if provider == nil {
      provider = acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &FlowToken.Vault>(/storage/flowTokenVault)
    }
    self.flowProvider = provider!
    self.flowReceiver = acct.capabilities.get<&FlowToken.Vault>(/public/flowTokenReceiver)!
    self.receiverCap = getAccount(recipient).capabilities.get<&{FungibleToken.Receiver}>(vaultData.receiverPath)!
  }

  execute {
    let depositEstimate <- LostAndFound.estimateDeposit(redeemer: recipient, item: <-self.sentVault, memo: memo, display: self.display)
    let storageFee <- self.flowProvider.borrow()!.withdraw(amount: depositEstimate.storageFee)
    let item <- depositEstimate.withdraw()

    LostAndFound.trySendResource(
      item: <-item,
      cap: self.receiverCap,
      memo: memo,
      display: self.display,
      storagePayment: &storageFee as auth(FungibleToken.Withdraw) &{FungibleToken.Vault},
      flowTokenRepayment: self.flowReceiver
    )

    self.flowReceiver.borrow()!.deposit(from: <-storageFee)
    destroy depositEstimate
  }
}
```