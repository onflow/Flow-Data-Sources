# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/get_nodes_info.cdc

```
import FlowStakingCollection from 0xFlowStakingCollection
import FlowIDTableStaking from 0xFlowIDTableStaking

access(all) struct SummaryStakeDelegateInfo {
  access(all) var nodeCount: UInt64
  access(all) var delegateCount: UInt64

  access(all) var totalTokensStaked: UFix64
  access(all) var totalTokensCommitted: UFix64
  access(all) var totalTokensUnstaking: UFix64
  access(all) var totalTokensUnstaked: UFix64
  access(all) var totalTokensRewarded: UFix64
  access(all) var totalTokensRequestedToUnstake: UFix64

  access(all) var stakeTokensStaked: UFix64
  access(all) var stakeTokensCommitted: UFix64
  access(all) var stakeTokensUnstaking: UFix64
  access(all) var stakeTokensUnstaked: UFix64
  access(all) var stakeTokensRewarded: UFix64
  access(all) var stakeTokensRequestedToUnstake: UFix64

  access(all) var delegateTokensStaked: UFix64
  access(all) var delegateTokensCommitted: UFix64
  access(all) var delegateTokensUnstaking: UFix64
  access(all) var delegateTokensUnstaked: UFix64
  access(all) var delegateTokensRewarded: UFix64
  access(all) var delegateTokensRequestedToUnstake: UFix64

  init(allNodeInfo: [FlowIDTableStaking.NodeInfo], allDelegateInfo: [FlowIDTableStaking.DelegatorInfo]) {
    self.nodeCount = UInt64(0)
    self.delegateCount = UInt64(0)

    self.totalTokensStaked = UFix64(0)
    self.totalTokensCommitted = UFix64(0)
    self.totalTokensUnstaking = UFix64(0)
    self.totalTokensUnstaked = UFix64(0)
    self.totalTokensRewarded = UFix64(0)
    self.totalTokensRequestedToUnstake = UFix64(0)

    self.stakeTokensStaked = UFix64(0)
    self.stakeTokensCommitted = UFix64(0)
    self.stakeTokensUnstaking = UFix64(0)
    self.stakeTokensUnstaked = UFix64(0)
    self.stakeTokensRewarded = UFix64(0)
    self.stakeTokensRequestedToUnstake = UFix64(0)

    self.delegateTokensStaked = UFix64(0)
    self.delegateTokensCommitted = UFix64(0)
    self.delegateTokensUnstaking = UFix64(0)
    self.delegateTokensUnstaked = UFix64(0)
    self.delegateTokensRewarded = UFix64(0)
    self.delegateTokensRequestedToUnstake = UFix64(0)

    for nodeInfo in allNodeInfo {
      self.nodeCount = self.nodeCount + 1

      self.totalTokensStaked = self.totalTokensStaked + nodeInfo.tokensStaked
      self.totalTokensCommitted = self.totalTokensCommitted + nodeInfo.tokensCommitted
      self.totalTokensUnstaking = self.totalTokensUnstaking + nodeInfo.tokensUnstaking
      self.totalTokensUnstaked = self.totalTokensUnstaked + nodeInfo.tokensUnstaked
      self.totalTokensRewarded = self.totalTokensRewarded + nodeInfo.tokensRewarded
      self.totalTokensRequestedToUnstake = self.totalTokensRequestedToUnstake + nodeInfo.tokensRequestedToUnstake

      self.stakeTokensStaked = self.stakeTokensStaked + nodeInfo.tokensStaked
      self.stakeTokensCommitted = self.stakeTokensCommitted + nodeInfo.tokensCommitted
      self.stakeTokensUnstaking = self.stakeTokensUnstaking + nodeInfo.tokensUnstaking
      self.stakeTokensUnstaked = self.stakeTokensUnstaked + nodeInfo.tokensUnstaked
      self.stakeTokensRewarded = self.stakeTokensRewarded + nodeInfo.tokensRewarded
      self.stakeTokensRequestedToUnstake = self.stakeTokensRequestedToUnstake + nodeInfo.tokensRequestedToUnstake
    }

    for delegateInfo in allDelegateInfo {
      self.delegateCount = self.delegateCount + 1

      self.totalTokensStaked = self.totalTokensStaked + delegateInfo.tokensStaked
      self.totalTokensCommitted = self.totalTokensCommitted + delegateInfo.tokensCommitted
      self.totalTokensUnstaking = self.totalTokensUnstaking + delegateInfo.tokensUnstaking
      self.totalTokensUnstaked = self.totalTokensUnstaked + delegateInfo.tokensUnstaked
      self.totalTokensRewarded = self.totalTokensRewarded + delegateInfo.tokensRewarded
      self.totalTokensRequestedToUnstake = self.totalTokensRequestedToUnstake + delegateInfo.tokensRequestedToUnstake

      self.delegateTokensStaked = self.delegateTokensStaked + delegateInfo.tokensStaked
      self.delegateTokensCommitted = self.delegateTokensCommitted + delegateInfo.tokensCommitted
      self.delegateTokensUnstaking = self.delegateTokensUnstaking + delegateInfo.tokensUnstaking
      self.delegateTokensUnstaked = self.delegateTokensUnstaked + delegateInfo.tokensUnstaked
      self.delegateTokensRewarded = self.delegateTokensRewarded + delegateInfo.tokensRewarded
      self.delegateTokensRequestedToUnstake = self.delegateTokensRequestedToUnstake + delegateInfo.tokensRequestedToUnstake
    }
  }
}

access(all) fun main(account: Address): SummaryStakeDelegateInfo? {
  let doesAccountHaveStakingCollection = FlowStakingCollection.doesAccountHaveStakingCollection(address: account)
  if (!doesAccountHaveStakingCollection) {
    return nil
  }

  let allNodeInfo: [FlowIDTableStaking.NodeInfo] = FlowStakingCollection.getAllNodeInfo(address: account)
  let allDelegateInfo: [FlowIDTableStaking.DelegatorInfo] = FlowStakingCollection.getAllDelegatorInfo(address: account)

  return SummaryStakeDelegateInfo(allNodeInfo: allNodeInfo, allDelegateInfo: allDelegateInfo)
}

```