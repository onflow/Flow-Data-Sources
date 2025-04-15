# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/transactions/bridge/onboarding/batch_onboard_by_evm_address.cdc

```
import "FungibleToken"
import "FlowToken"

import "ScopedFTProviders"

import "EVM"

import "FlowEVMBridge"
import "FlowEVMBridgeConfig"

/// This transaction onboards ERC20/ERC721 assets to the bridge, configuring the bridge to move assets between
/// environments
/// NOTE: This must be done before bridging a Cadence-native NFT to EVM
///
/// @param addressesAsHex: Array of EVM contract addresses defining the 
///     bridgeable asset to be onboarded
///
transaction(addressesAsHex: [String]) {

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
        let providerLimit = FlowEVMBridgeConfig.onboardFee * UFix64(addressesAsHex.length)
        let providerFilter = ScopedFTProviders.AllowanceFilter(providerLimit)
        // Create ScopedFTProvider to expire just after this transaction
        self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
                provider: providerCapCopy,
                filters: [ providerFilter ],
                expiration: getCurrentBlock().timestamp + 1.0
            )
    }

    execute {
        // Iterate over provided array
        for addressHex in addressesAsHex {
            // Convert hex string to EVMAddress
            let address = EVM.addressFromString(addressHex)
            // Continue if the hex is not a valid EVM address or if the address is already onboarded
            if address == nil || FlowEVMBridge.evmAddressRequiresOnboarding(address!) != true {
                continue
            }

            FlowEVMBridge.onboardByEVMAddress(
                address!,
                feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
            )
        }
        destroy self.scopedProvider
    }
}

```