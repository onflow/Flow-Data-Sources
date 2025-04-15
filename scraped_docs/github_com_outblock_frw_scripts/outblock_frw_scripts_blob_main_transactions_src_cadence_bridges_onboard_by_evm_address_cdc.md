# Source: https://github.com/Outblock/FRW-scripts/blob/main/transactions/src/cadence/bridges/onboard_by_evm_address.cdc

```
import FungibleToken from 0xFungibleToken
import FlowToken from 0xFlowToken

import ScopedFTProviders from 0xFlowEVMBridge

import EVM from 0xEVM

import EVMUtils from 0xFlowEVMBridge
import FlowEVMBridge from 0xFlowEVMBridge
import FlowEVMBridgeConfig from 0xFlowEVMBridge

/// This transaction onboards the NFT type to the bridge, configuring the bridge to move NFTs between environments
/// NOTE: This must be done before bridging a Cadence-native NFT to EVM
///
/// @param contractAddressHex: The EVM address of the contract (as hex string without 0x prefix) defining the 
///     bridgeable asset to be onboarded
///
transaction(contractAddressHex: String) {

    let contractAddress: EVM.EVMAddress
    let scopedProvider: @ScopedFTProviders.ScopedFTProvider
    
    prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {
        /* --- Construct EVMAddress from hex string (no leading `"0x"`) --- */
        //
        self.contractAddress = EVMUtils.getEVMAddressFromHexString(address: contractAddressHex)
            ?? panic("Invalid EVM address string provided")

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
        let providerFilter = ScopedFTProviders.AllowanceFilter(FlowEVMBridgeConfig.onboardFee)
        self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
                provider: providerCapCopy,
                filters: [ providerFilter ],
                expiration: getCurrentBlock().timestamp + 1.0
            )
    }

    execute {
        // Onboard the EVM contract
        FlowEVMBridge.onboardByEVMAddress(
            self.contractAddress,
            feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
        )
        destroy self.scopedProvider
    }
}

```