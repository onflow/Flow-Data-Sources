# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/register-evm-asset.cdc

```
import "FungibleToken"
import "FlowToken"

import "ScopedFTProviders"
import "EVM"
import "FlowEVMBridgeConfig"

import "TokenList"
import "NFTList"
import "EVMTokenList"

transaction(
    contractAddressHex: String,
) {
    let scopedProvider: @ScopedFTProviders.ScopedFTProvider

    prepare(signer: auth(CopyValue, BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {
        /* --- Configure a ScopedFTProvider - Start -- */

        // Issue and store bridge-dedicated Provider Capability in storage if necessary
        if signer.storage.type(at: FlowEVMBridgeConfig.providerCapabilityStoragePath) == nil {
            let providerCap = signer.capabilities
                .storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>(/storage/flowTokenVault)
            signer.storage.save(providerCap, to: FlowEVMBridgeConfig.providerCapabilityStoragePath)
        }
        // Copy the stored Provider capability and create a ScopedFTProvider
        let providerCapCopy = signer.storage
            .copy<Capability<auth(FungibleToken.Withdraw) &{FungibleToken.Provider}>>(
                from: FlowEVMBridgeConfig.providerCapabilityStoragePath
            ) ?? panic("Invalid Provider Capability found in storage.")
        let providerFilter = ScopedFTProviders.AllowanceFilter(FlowEVMBridgeConfig.onboardFee)
        self.scopedProvider <- ScopedFTProviders.createScopedFTProvider(
            provider: providerCapCopy,
            filters: [ providerFilter ],
            expiration: getCurrentBlock().timestamp + 1.0
        )
        /* --- Configure a ScopedFTProvider - End -- */
    }

    execute {
        // Onboard the EVM contract
        EVMTokenList.ensureEVMAssetRegistered(
            contractAddressHex,
            feeProvider: &self.scopedProvider as auth(FungibleToken.Withdraw) &{FungibleToken.Provider}
        )
        destroy self.scopedProvider
    }
}

```