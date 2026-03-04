# Source: https://github.com/fixes-world/token-list/blob/main/cadence/transactions/migration/register-all-onboarded-nfts.cdc

```
import "NFTList"
import "FlowEVMBridgeConfig"
import "EVMTokenList"

transaction {
    prepare(signer: &Account) {
        let registry = NFTList.borrowRegistry()
        let entries = registry.getAllNFTEntries()
        for tokenType in entries {
            if let evmAddr = FlowEVMBridgeConfig.getEVMAddressAssociated(with: tokenType) {
                EVMTokenList.ensureEVMAssetRegistered(evmAddr.toString(), feeProvider: nil)
            }
        }
    }
}

```