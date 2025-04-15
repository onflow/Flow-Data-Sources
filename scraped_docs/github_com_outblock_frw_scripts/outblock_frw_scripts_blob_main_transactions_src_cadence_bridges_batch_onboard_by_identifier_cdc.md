# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/bridges/batch_onboard_by_identifier.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken

import ScopedFTProviders from 0xFlowEVMBridge

import EVM from 0xEVM

import FlowEVMBridge from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge

/// This transaction onboards the asset type to the bridge, configuring the bridge to move assets between environments
/// NOTE: This must be done before bridging a Cadence-native asset to EVM
///
/// @param types: The Cadence types of the bridgeable asset to onboard to the bridge
///
transaction(identifiers: [String]) {

    let scopedProvider: @ScopedFTProviders.ScopedFTProvider
    
    prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {

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
        // Set a withdrawal limit for the provider
        let providerLimit = FlowEVMBridgeConfig.onboardFee * UFix64(types.length)
        let providerFilter = ScopedFTProviders.AllowanceFilter(providerLimit)
        // Create ScopedFTProvider to expire just after this transaction
        self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
                provider: providerCapCopy,
                filters: [ providerFilter ],
                expiration: getCurrentBlock().timestamp + 1.0
            )
    }

    execute {
        for identifiers in identifiers { 
            let type = CompositeType(identifier) ?? panic("Invalid type identifier")
            // Continue on if the type does not require onboarding
            if FlowEVMBridge.typeRequiresOnboarding(type) != true {
                continue
            }
            // Onboard the asset Type
            FlowEVMBridge.onboardByType(
                type,
                feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
            )
        }
        destroy self.scopedProvider
    }
}

```