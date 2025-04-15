# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_machine_account_address.cdc

```
import "FlowStakingCollection"

/// Gets the machine account address for a specific node
/// in an account's staking collection

access(all) fun main(account: Address, nodeID: String): Address? {
    let machineAccounts = FlowStakingCollection.getMachineAccounts(address: account)

    if let accountInfo = machineAccounts[nodeID] {
        return accountInfo.getAddress()
    } else {
        return nil
    }
}

```