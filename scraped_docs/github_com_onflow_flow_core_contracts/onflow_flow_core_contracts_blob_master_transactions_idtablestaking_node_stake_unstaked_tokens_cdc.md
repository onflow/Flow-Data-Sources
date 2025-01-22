# Source: https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/node/stake_unstaked_tokens.cdc

```
import FlowIDTableStaking from "FlowIDTableStaking"


transaction(amount: UFix64) {

    // Local variable for a reference to the node object
    let stakerRef: auth(FlowIDTableStaking.NodeOperator) &FlowIDTableStaking.NodeStaker

    prepare(acct: auth(BorrowValue) &Account) {
        // borrow a reference to the node object
        self.stakerRef = acct.storage.borrow<auth(FlowIDTableStaking.NodeOperator) &FlowIDTableStaking.NodeStaker>(from: /storage/flowStaker)
            ?? panic("Could not borrow reference to staking admin")
    }

    execute {
        self.stakerRef.stakeUnstakedTokens(amount: amount)
    }
}

```