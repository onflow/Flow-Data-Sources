# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingProxy/remove_staking_proxy.cdc

```
import "StakingProxy"

transaction(nodeID: String) {

    prepare(account: auth(BorrowValue) &Account) {
        let proxyHolder = account.storage.borrow<auth(StakingProxy.NodeOperator) &StakingProxy.NodeStakerProxyHolder>(from: StakingProxy.NodeOperatorCapabilityStoragePath)
            ?? panic("Could not borrow reference to staking proxy holder")

        proxyHolder.removeStakingProxy(nodeID: nodeID)
    }
}

```