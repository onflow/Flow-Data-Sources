# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/transactions/bridge/admin/blocklist/block_evm_address.cdc

```
import "EVM"

import "FlowEVMBridgeConfig"

/// Blocks the given EVM contract address from onboarding.
///
/// @param evmContractHex: The EVM contract address to block from onboarding
///
transaction(evmContractHex: String) {

    let evmBlocklist: auth(FlowEVMBridgeConfig.Blocklist) &FlowEVMBridgeConfig.EVMBlocklist
    let evmAddress: EVM.EVMAddress

    prepare(signer: auth(BorrowValue) &Account) {
        self.evmBlocklist = signer.storage.borrow<auth(FlowEVMBridgeConfig.Blocklist) &FlowEVMBridgeConfig.EVMBlocklist>(
                from: /storage/evmBlocklist
            ) ?? panic("Could not borrow FlowEVMBridgeConfig Admin reference")
        self.evmAddress = EVM.addressFromString(evmContractHex)
    }

    execute {
        self.evmBlocklist.block(self.evmAddress)
    }

    post {
        FlowEVMBridgeConfig.isEVMAddressBlocked(self.evmAddress): "EVM address was not blocked"
    }
}

```