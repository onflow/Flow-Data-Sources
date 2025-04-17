# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/bridges/transaction/bridge_nft_from_evm_to_flow.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken
import MetadataViews from 0xMetadataViews
import ViewResolver from 0xMetadataViews
import NonFungibleToken from 0xNonFungibleToken
import ScopedFTProviders from 0xFlowEVMBridge

import EVM from 0xEVM

import FlowEVMBridgeUtils from 0xFlowEVMBridge
import FlowEVMBridge from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge


transaction(nftContractAddress: Address, nftContractName: String, id: UInt256, receiver: Address) {

  let nftType: Type
  let collection: &{NonFungibleToken.Collection}
  let scopedProvider: @ScopedFTProviders.ScopedFTProvider
  let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount
  
  prepare(signer: auth(BorrowValue, CopyValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {
    /* --- Reference the signer's CadenceOwnedAccount --- */
    //
    // Borrow a reference to the signer's COA
    self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)
      ?? panic("Could not borrow COA from provided gateway address")

    // Get the ERC721 contract address for the given NFT type
    self.nftType = FlowEVMBridgeUtils.buildCompositeType(
      address: nftContractAddress,
      contractName: nftContractName,
      resourceName: "NFT"
    ) ?? panic("Could not construct NFT type")

    /* --- Reference the signer's NFT Collection --- */
    //
    // Borrow a reference to the NFT collection, configuring if necessary
    let viewResolver = getAccount(nftContractAddress).contracts.borrow<&{ViewResolver}>(name: nftContractName)
      ?? panic("Could not borrow ViewResolver from NFT contract")
    let collectionData = viewResolver.resolveContractView(
      resourceType: self.nftType,
      viewType: Type<MetadataViews.NFTCollectionData>()
    ) as! MetadataViews.NFTCollectionData? ?? panic("Could not resolve NFTCollectionData view")
    if signer.storage.borrow<&{NonFungibleToken.Collection}>(from: collectionData.storagePath) == nil {
      signer.storage.save(<-collectionData.createEmptyCollection(), to: collectionData.storagePath)
      signer.capabilities.unpublish(collectionData.publicPath)
      let collectionCap = signer.capabilities.storage.issue<&{NonFungibleToken.Collection}>(collectionData.storagePath)
      signer.capabilities.publish(collectionCap, at: collectionData.publicPath)
    }

    let receiverAcct = getAccount(receiver)
    self.collection = receiverAcct.capabilities.borrow<&{NonFungibleToken.Collection}>(collectionData.publicPath)
      ?? panic("Could not borrow collection capabilities from public path")

    /* --- Configure a ScopedFTProvider --- */
    //
    // Calculate the bridge fee - bridging from EVM consumes no storage, so flat fee
    let approxFee = FlowEVMBridgeUtils.calculateBridgeFee(bytes: 400_000)
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

  execute {
    // Execute the bridge
    let nft: @{NonFungibleToken.NFT} <- self.coa.withdrawNFT(
      type: self.nftType,
      id: id,
      feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
    )
    // Deposit the bridged NFT into the signer's collection
    self.collection.deposit(token: <-nft)
    // Destroy the ScopedFTProvider
    destroy self.scopedProvider
  }
}

```