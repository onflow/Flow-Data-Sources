# Source: https://github.com/fixes-world/token-list/blob/main/cadence/scripts/get-ft-or-nft-contract-by-evm.cdc

```
import "EVM"
import "FlowEVMBridge"
import "FlowEVMBridgeConfig"
import "FlowEVMBridgeUtils"

import "EVMTokenList"

access(all)
fun main(
    evmContractAddress: String,
): EVMAssetStatus? {
    if evmContractAddress.length != 42 && evmContractAddress.length != 40 {
        return nil
    }
    let addrNo0x = evmContractAddress.slice(from: 0, upTo: 2) == "0x"
            ? evmContractAddress.slice(from: 2, upTo: evmContractAddress.length)
            : evmContractAddress
    let acct = EVM.addressFromString(addrNo0x)

    let isRequires = FlowEVMBridge.evmAddressRequiresOnboarding(acct)
    if isRequires == nil {
        return nil
    }

    let isNFT = FlowEVMBridgeUtils.isERC721(evmContractAddress: acct)

    var bridgedAddress: Address? = nil
    var bridgedContractName: String? = nil
    if let type = FlowEVMBridgeConfig.getTypeAssociated(with: acct) {
        bridgedAddress = FlowEVMBridgeUtils.getContractAddress(fromType: type)
        bridgedContractName = FlowEVMBridgeUtils.getContractName(fromType: type)
    }

    return EVMAssetStatus(
        address: acct,
        isNFT: isNFT,
        isRegistered: EVMTokenList.isEVMAddressRegistered(acct.toString()),
        isBridged: isRequires == false,
        bridgedAddress: bridgedAddress,
        bridgedContractName: bridgedContractName
    )
}

access(all) struct EVMAssetStatus {
    access(all)
    let evmAddress: String
    access(all)
    let isNFT: Bool
    access(all)
    let isRegistered: Bool
    access(all)
    let isBridged: Bool
    access(all)
    let bridgedAddress: Address?
    access(all)
    let bridgedContractName: String?

    init(
        address: EVM.EVMAddress,
        isNFT: Bool,
        isRegistered: Bool,
        isBridged: Bool,
        bridgedAddress: Address?,
        bridgedContractName: String?
    ) {
        self.evmAddress = address.toString()
        self.isNFT = isNFT
        self.isRegistered = isRegistered
        self.isBridged = isBridged
        self.bridgedAddress = bridgedAddress
        self.bridgedContractName = bridgedContractName
    }
}

```