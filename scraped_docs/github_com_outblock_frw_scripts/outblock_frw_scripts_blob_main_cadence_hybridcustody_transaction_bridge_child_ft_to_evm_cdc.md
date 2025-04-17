# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/hybridCustody/transaction/bridge_child_ft_to_evm.cdc

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

import HybridCustody from 0xHybridCustody
import CapabilityFilter from 0xCapabilityFilter


transaction(vaultIdentifier: String, child: Address, amount: UFix64) {

  // The Vault resource that holds the tokens that are being transferred
  let paymentVault: @{FungibleToken.Vault}
  let coa: auth(EVM.Bridge) &EVM.CadenceOwnedAccount
  let scopedProvider: @ScopedFTProviders.ScopedFTProvider

  prepare(signer: auth(Storage, CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {
    /* --- Reference the signer's CadenceOwnedAccount --- */
    //
    // Borrow a reference to the signer's COA
    self.coa = signer.storage.borrow<auth(EVM.Bridge) &EVM.CadenceOwnedAccount>(from: /storage/evm)
      ?? panic("Could not borrow COA from provided gateway address")

    /* --- Retrieve the funds --- */
    //
    // Borrow a reference to the FungibleToken Vault
    let vaultType = CompositeType(vaultIdentifier)
      ?? panic("Could not construct Vault type from identifier: ".concat(vaultIdentifier))
    // Parse the Vault identifier into its components
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
    let vault = signer.storage.borrow<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(
      from: vaultData.storagePath
    ) ?? panic("Could not access signer's FungibleToken Vault")

    // signer is the parent account
    // get the manager resource and borrow childAccount
    let m = signer.storage.borrow<auth(HybridCustody.Manage) &HybridCustody.Manager>(from: HybridCustody.ManagerStoragePath)
      ?? panic("manager does not exist")
    let childAcct = m.borrowAccount(addr: child) ?? panic("child account not found")
    
    //get Ft cap from child account
    let capType = Type<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>()
    let controllerID = childAcct.getControllerIDForType(type: capType, forPath: vaultData.storagePath)
      ?? panic("no controller found for capType")
    
    let cap = childAcct.getCapability(controllerID: controllerID, type: capType) ?? panic("no cap found")
    let providerCap = cap as! Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>
    assert(providerCap.check(), message: "invalid provider capability")
    
    // Get a reference to the child's stored vault
    let vaultRef = providerCap.borrow()!

    // Withdraw tokens from the signer's stored vault
    vault.deposit(from: <- vaultRef.withdraw(amount: amount))
    // Withdraw the requested balance & calculate the approximate bridge fee based on storage usage
    let currentStorageUsage = signer.storage.used
    self.paymentVault <- vault.withdraw(amount: amount)
    let withdrawnStorageUsage = signer.storage.used
    // Approximate the bridge fee based on the difference in storage usage with some buffer
    let approxFee = FlowEVMBridgeUtils.calculateBridgeFee(
      bytes: 400_000
    )

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
    let providerCapCopy = signer.storage.copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(from: FlowEVMBridgeConfig.providerCapabilityStoragePath)
      ?? panic("Invalid Provider Capability found in storage.")
    let providerFilter = ScopedFTProviders.AllowanceFilter(approxFee)
    self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
      provider: providerCapCopy,
      filters: [ providerFilter ],
      expiration: getCurrentBlock().timestamp + 1.0
    )
  }

  execute {
    self.coa.depositTokens(
      vault: <-self.paymentVault,
      feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
    )
    // Destroy the ScopedFTProvider
    destroy self.scopedProvider
  }
}

```