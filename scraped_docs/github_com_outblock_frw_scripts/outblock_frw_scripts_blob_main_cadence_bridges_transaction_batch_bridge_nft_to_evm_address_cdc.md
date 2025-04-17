# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/transaction/batch_bridge_nft_to_evm_address.cdc

```
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import NonFungibleToken from 0xNonFungibleToken

import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import FungibleTokenMetadataViews from 0xFungibleToken

import ScopedFTProviders from 0xFlowEVMBridge

import EVM from 0xEVM

import FlowEVMBridgeUtils from 0xFlowEVMBridge
import FlowEVMBridge from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge


transaction(nftIdentifier: String, ids: [UInt64], recipient: String) {
  let nft: @{NonFungibleToken.NFT}
  let requiresOnboarding: Bool
  let scopedProvider: @ScopedFTProviders.ScopedFTProvider
  let collection: auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}

  prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {        
    /* --- Construct the NFT type --- */
    //
    // Construct the NFT type from the provided identifier
    let nftType = CompositeType(nftIdentifier)
      ?? panic("Could not construct NFT type from identifier: ".concat(nftIdentifier))
    // Parse the NFT identifier into its components
    let nftContractAddress = FlowEVMBridgeUtils.getContractAddress(fromType: nftType)
      ?? panic("Could not get contract address from identifier: ".concat(nftIdentifier))
    let nftContractName = FlowEVMBridgeUtils.getContractName(fromType: nftType)
      ?? panic("Could not get contract name from identifier: ".concat(nftIdentifier))

    /* --- Retrieve the NFT --- */
    //
    // Borrow a reference to the NFT collection, configuring if necessary
    let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)
      ?? panic("Could not borrow ViewResolver from NFT contract")
    let collectionData = viewResolver.resolveContractView(
      resourceType: nil,
      viewType: Type<MetadataViews.NFTCollectionData>()
    ) as! MetadataViews.NFTCollectionData? ?? panic("Could not resolve NFTCollectionData view")
    self.collection = signer.storage.borrow<auth(NonFungibleToken.Withdraw) &{NonFungibleToken.Collection}>(
      from: collectionData.storagePath
    ) ?? panic("Could not access signer's NFT Collection")

    // Withdraw the requested NFT & calculate the approximate bridge fee based on NFT storage usage
    let currentStorageUsage = signer.storage.used
    self.nft <- self.collection.withdraw(withdrawID: ids[0])
    let withdrawnStorageUsage = signer.storage.used
    var approxFee = FlowEVMBridgeUtils.calculateBridgeFee(bytes: 400_000) + (FlowEVMBridgeConfig.baseFee * UFix64(ids.length))

    // Determine if the NFT requires onboarding - this impacts the fee required
    self.requiresOnboarding = FlowEVMBridge.typeRequiresOnboarding(self.nft.getType())
      ?? panic("Bridge does not support this asset type")
    if self.requiresOnboarding {
      approxFee = approxFee + FlowEVMBridgeConfig.onboardFee
    }

    /* --- Configure a ScopedFTProvider --- */
    //
    // Issue and store bridge-dedicated Provider Capability in storage if necessary
    if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {
      let providerCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(
        /storage/flowTokenVault
      )
      signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)
    }
    // Copy the stored Provider capability and create a ScopedFTProvider
    let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(
      from: FlowEVMBridgeConfig.providerCapabilityStoragePath
    ) ?? panic("Invalid Provider Capability found in storage.")
    let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)
    self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
      provider: providerCapCopy,
      filters: [ providerFilter ],
      expiration: getCurrentBlock().timestamp + 1.0
    )
  }

  pre {
    self.nft.getType().identifier == nftIdentifier:
      "Attempting to send invalid nft type - requested: ".concat(nftIdentifier)
      .concat(", sending: ").concat(self.nft.getType().identifier)
  }

  execute {
    if self.requiresOnboarding {
      // Onboard the NFT to the bridge
      FlowEVMBridge.onboardByType(
        self.nft.getType(),
        feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
      )
    }
    // Execute the bridge transaction
    let recipientEVMAddress = EVM.addressFromString(recipient)
    FlowEVMBridge.bridgeNFTToEVM(
      token: <-self.nft,
      to: recipientEVMAddress,
      feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
    )
    var idx = 0

    for id in ids {
      if idx == 0 {
        idx = idx + 1
        continue
      }

      FlowEVMBridge.bridgeNFTToEVM(
        token: <- self.collection.withdraw(withdrawID: id),
        to: recipientEVMAddress,
        feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
      )
    }
   
    // Destroy the ScopedFTProvider
    destroy self.scopedProvider
  }
}
```