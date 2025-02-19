# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_machine_accounts.cdc

```
import "FlowStakingCollection"

/// Gets all the machine account addresses for nodes
/// in the account's staking collection

access(all) fun main(account: Address): {String: FlowStakingCollection.MachineAccountInfo} {
    return FlowStakingCollection.getMachineAccounts(address: account)
}

```