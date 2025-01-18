# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingProxy/remove_node_info.cdc

```
import StakingProxy from "StakingProxy"

transaction(nodeID: String) {

    prepare(account: auth(BorrowValue) &Account) {
        let proxyHolder = account.storage.borrow<&StakingProxy.NodeStakerProxyHolder>(from: StakingProxy.NodeOperatorCapabilityStoragePath)

        proxyHolder.removeNodeInfo(nodeID: nodeID)
    }
}

```