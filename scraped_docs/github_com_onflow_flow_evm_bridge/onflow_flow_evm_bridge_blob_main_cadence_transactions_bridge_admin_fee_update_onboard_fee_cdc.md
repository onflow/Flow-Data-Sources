# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/transactions/bridge/admin/fee/update_onboard_fee.cdc

```
import "FlowEVMBridgeConfig"

/// Sets the onboarding fee charged to onboard an asset to the bridge.
///
/// @param newFee: The fee paid to onboard an asset.
///
/// @emits FlowEVMBridgeConfig.BridgeFeeUpdated(old: FlowEVMBridgeConfig.onboardFee, new: newFee, isOnboarding: true)
///
transaction(newFee: UFix64) {

    let admin: auth(FlowEVMBridgeConfig.Fee) &FlowEVMBridgeConfig.Admin

    prepare(signer: auth(BorrowValue) &Account) {
        self.admin = signer.storage.borrow<auth(FlowEVMBridgeConfig.Fee) &FlowEVMBridgeConfig.Admin>(
                from: FlowEVMBridgeConfig.adminStoragePath
            ) ?? panic("Could not borrow FlowEVMBridgeConfig Admin reference")
    }

    execute {
        self.admin.updateOnboardingFee(newFee)
    }

    post {
        FlowEVMBridgeConfig.onboardFee == newFee: "Fee was not set correctly"
    }
}

```