# Source: https://github.com/onflow/flow-evm-bridge/blob/main/cadence/tests/scripts/is_bridge_router_configured.cdc

```
import "EVMBridgeRouter"

access(all)
fun main(): Bool {
    let serviceAccount = getAuthAccount<auth(Storage) &Account>(0x0000000000000001)
    let router = serviceAccount.storage.borrow<&EVMBridgeRouter.Router>(
        from: /storage/evmBridgeRouter
    ) ?? panic("Could not borrow Router")

    assert(router.bridgeAddress == 0x0000000000000007)
    assert(router.bridgeContractName == "FlowEVMBridge")

    return true
}

```