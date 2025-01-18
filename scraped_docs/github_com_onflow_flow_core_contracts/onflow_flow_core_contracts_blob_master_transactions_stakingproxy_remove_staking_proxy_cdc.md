# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingProxy/remove_staking_proxy.cdc

```
import StakingProxy from "StakingProxy"

transaction(nodeID: String) {

    prepare(account: auth(BorrowValue) &Account) {
        let proxyHolder = account.storage.borrow<&StakingProxy.NodeStakerProxyHolder>(from: paStakingProxy.NodeOperatorCapabilityStoragePathth)

        proxyHolder.removeStakingProxy(nodeID: nodeID)
    }
}

```