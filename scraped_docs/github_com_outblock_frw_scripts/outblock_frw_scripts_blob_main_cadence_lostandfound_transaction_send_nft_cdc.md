# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/lostAndFound/transaction/send_nft.cdc

```

import FlowToken from 0xFlowToken
import NonFungibleToken from 0xNonFungibleToken
import FungibleToken from 0xFungibleToken
import LostAndFound from 0xLostAndFound
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import FungibleTokenMetadataViews from 0xFungibleToken
import FlowEVMBridgeUtils from 0xFlowEVMBridge


transaction(nftIdentifier: String, recipient: Address, id: UInt64, memo: String) {
  let nft: @{NonFungibleToken.NFT}
  let flowProvider: Capability<auth(FungibleToken.Withdraw) &FlowToken.Vault>
  let flowReceiver: Capability<&FlowToken.Vault>
  let receiverCap: Capability<&{NonFungibleToken.CollectionPublic}>

  prepare(acct: auth(Storage, Capabilities) &Account) {
    let nftType = CompositeType(nftIdentifier)
      ?? panic("Could not construct NFT type from identifier: ".concat(nftIdentifier))
    let nftContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: nftType)
      ?? panic("Could not get contract address from identifier: ".concat(nftIdentifier))
    let nftContractName = FlowEVMBridgeUtils.getContractName(fromType: nftType)
      ?? panic("Could not get contract name from identifier: ".concat(nftIdentifier))

    let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)
      ?? panic("Could not borrow ViewResolver from NFT contract")
    let collectionData = viewResolver.resolveContractView(
        resourceType: nil,
        viewType: Type<MetadataViews.NFTCollectionData>()
      ) as! MetadataViews.NFTCollectionData? ?? panic("Could not resolve NFTCollectionData view")
    
    let collection = acct.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(
        from: collectionData.storagePath
      ) ?? panic("Could not access signer's FungibleToken Vault")

    self.nft <- collection.withdraw(withdrawID: id)

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
    self.receiverCap = getAccount(recipient).capabilities.get<&{NonFungibleToken.CollectionPublic}>(collectionData.publicPath)!
  }

  execute {
    let display = self.nft.resolveView(Type<MetadataViews.Display>()) as! MetadataViews.Display?

    let depositEstimate <- LostAndFound.estimateDeposit(redeemer: recipient, item: <-self.nft, memo: memo, display: display)
    let storageFee <- self.flowProvider.borrow()!.withdraw(amount: depositEstimate.storageFee)
    let item <- depositEstimate.withdraw()

    LostAndFound.trySendResource(
      item: <-item,
      cap: self.receiverCap,
      memo: memo,
      display: display,
      storagePayment: &storageFee as auth(FungibleToken.Withdraw) &{FungibleToken.Vault},
      flowTokenRepayment: self.flowReceiver
    )

    self.flowReceiver.borrow()!.deposit(from: <-storageFee)
    destroy depositEstimate
  }
}
```