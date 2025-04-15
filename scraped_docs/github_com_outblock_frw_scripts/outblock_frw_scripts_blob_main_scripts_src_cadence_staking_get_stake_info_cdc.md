# Source: https://github.com/Outblock/FRW-scripts/blob/main/scripts/src/cadence/staking/get_stake_info.cdc

```

import FlowStakingCollection from 0xFlowStakingCollection
import FlowIDTableStaking from 0xFlowIDTableStaking
import LockedTokens from 0xLockedTokens

access(all) struct StakeInfo {
    access(all) let id: String
    access(all) let role: UInt8
    access(all) let networkingAddress: String
    access(all) let networkingKey: String
    access(all) let stakingKey: String
    access(all) let tokensStaked: UFix64
    access(all) let totalTokensStaked: UFix64
    access(all) let tokensCommitted: UFix64
    access(all) let tokensUnstaking: UFix64
    access(all) let tokensUnstaked: UFix64
    access(all) let tokensRewarded: UFix64

    access(all) let delegatorsCnt: Int
    access(all) let delegatorIDCounter: UInt32
    access(all) let tokensRequestedToUnstake: UFix64
    access(all) let initialWeight: UInt64

    // Projected Values
    access(all) let nodeID: String
    access(all) let unstakableTokens: UFix64
    access(all) let tokensDelegated: UFix64
    access(all) let restakableUnstakedTokens: UFix64

    access(all) let machineAccountAddress: Address?
    access(all) let machineAccountBalance: UFix64?

    init(nodeInfo: FlowIDTableStaking.NodeInfo, machineAccountInfo: FlowStakingCollection.MachineAccountInfo?) {
        self.id = nodeInfo.id
        self.role = nodeInfo.role
        self.networkingAddress = nodeInfo.networkingAddress
        self.networkingKey = nodeInfo.networkingKey
        self.stakingKey = nodeInfo.stakingKey
        self.tokensStaked = nodeInfo.tokensStaked
        self.totalTokensStaked = nodeInfo.totalStakedWithDelegators()
        self.tokensCommitted = nodeInfo.tokensCommitted
        self.tokensUnstaking = nodeInfo.tokensUnstaking
        self.tokensUnstaked = nodeInfo.tokensUnstaked
        self.tokensRewarded = nodeInfo.tokensRewarded

        self.delegatorsCnt = nodeInfo.delegators.length 
        self.delegatorIDCounter = nodeInfo.delegatorIDCounter
        self.tokensRequestedToUnstake = nodeInfo.tokensRequestedToUnstake
        self.initialWeight = nodeInfo.initialWeight

        // Projected Values
        self.nodeID = nodeInfo.id
        self.unstakableTokens = self.tokensStaked + self.tokensCommitted
        let nodeStakedBalanceWithDelegators = nodeInfo.totalStakedWithDelegators()
        self.tokensDelegated = nodeStakedBalanceWithDelegators - nodeInfo.tokensStaked
        self.restakableUnstakedTokens = self.tokensUnstaked + self.tokensRequestedToUnstake

        if let _machineAccountInfo = machineAccountInfo {
            let _machineAccountAddress = _machineAccountInfo.getAddress()

            let machineAccount = getAccount(_machineAccountAddress)

            self.machineAccountAddress = _machineAccountAddress
            self.machineAccountBalance = machineAccount.balance
        } else {
            self.machineAccountAddress = nil
            self.machineAccountBalance = nil
        }
    }
}

access(all) fun main(account: Address): {String: StakeInfo}? {
    let doesAccountHaveStakingCollection = FlowStakingCollection.doesAccountHaveStakingCollection(address: account)
    if (!doesAccountHaveStakingCollection) {
        return nil
    }

    let formattedNodeInfo: {String: StakeInfo} = {}
    let allNodeInfo: [FlowIDTableStaking.NodeInfo] = FlowStakingCollection.getAllNodeInfo(address: account)
    let machineAccounts: {String: FlowStakingCollection.MachineAccountInfo} = FlowStakingCollection.getMachineAccounts(address: account)

    for nodeInfo in allNodeInfo {
        formattedNodeInfo[nodeInfo.id] = StakeInfo(nodeInfo: nodeInfo, machineAccountInfo: machineAccounts[nodeInfo.id])
    }

    return formattedNodeInfo
}

```