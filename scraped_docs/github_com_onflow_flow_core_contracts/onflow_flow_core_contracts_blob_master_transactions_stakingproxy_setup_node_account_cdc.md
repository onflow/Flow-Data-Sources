# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingProxy/setup_node_account.cdc

```
import "StakingProxy"

transaction() {

    prepare(nodeOperator: auth(SaveValue, Capabilities) &Account) {
        let proxyHolder <- StakingProxy.createProxyHolder()

        nodeOperator.storage.save(<-proxyHolder, to: StakingProxy.NodeOperatorCapabilityStoragePath)

        let nodeOperatorCap = nodeOperator.capabilities.storage.issue<&StakingProxy.NodeStakerProxyHolder>(
            StakingProxy.NodeOperatorCapabilityStoragePath
        )

        nodeOperator.capabilities.publish(
            nodeOperatorCap,
            at: StakingProxy.NodeOperatorCapabilityPublicPath
        )
    }
}

```