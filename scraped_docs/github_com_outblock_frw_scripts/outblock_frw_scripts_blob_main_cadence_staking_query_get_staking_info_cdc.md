# Source: https://github.com/Outblock/FRW-scripts/blob/main/cadence/staking/query/get_staking_info.cdc

```
import LockedTokens from 0xLockedTokens
import FlowIDTableStaking from 0xFlowIDTableStaking
import FlowEpoch from 0xFlowEpoch

access(all)struct EpochInfo {
  access(all)let currentEpochCounter: UInt64
  access(all)let currentEpochPhase: UInt8

  init(
      currentEpochCounter: UInt64,
      currentEpochPhase: UInt8
  ) {
      self.currentEpochCounter = currentEpochCounter
      self.currentEpochPhase = currentEpochPhase
  }
}

access(all)struct Result {
  access(all)let stakingInfo: StakingInfo?

  init(stakingInfo: StakingInfo?) {
    self.stakingInfo = stakingInfo
  }
}

access(all)struct StakingInfo {
  access(all)let epochInfo: EpochInfo
  access(all)let lockedAddress: Address   
  access(all)let lockedBalance: UFix64
  access(all)let unlockLimit: UFix64
  access(all)let nodeInfo: NodeInfo?
  access(all)let delegatorNodeInfo: NodeInfo?
  access(all)let delegatorInfo: DelegatorInfo?

  init(
    epochInfo: EpochInfo,
    lockedAddress: Address,
    lockedBalance: UFix64,
    unlockLimit: UFix64,
    nodeInfo: NodeInfo?,
    delegatorNodeInfo: NodeInfo?,
    delegatorInfo: DelegatorInfo?,
  ) {
    self.epochInfo = epochInfo
    self.lockedAddress = lockedAddress
    self.lockedBalance = lockedBalance
    self.unlockLimit = unlockLimit
    self.nodeInfo = nodeInfo
    self.delegatorNodeInfo = delegatorNodeInfo
    self.delegatorInfo = delegatorInfo
  }
}

access(all)struct NodeInfo {
  access(all)let id: String
  access(all)let networkingAddress: String
  access(all)let role: UInt8
  access(all)let tokensStaked: UFix64
  access(all)let tokensCommitted: UFix64
  access(all)let tokensUnstaking: UFix64
  access(all)let tokensUnstaked: UFix64
  access(all)let tokensRewarded: UFix64
  
  access(all)let delegatorIDCounter: UInt32
  access(all)let tokensRequestedToUnstake: UFix64
  access(all)let initialWeight: UInt64

  init(nodeID: String) {
    let nodeInfo = FlowIDTableStaking.NodeInfo(nodeID: nodeID) 

    self.id = nodeInfo.id
    self.networkingAddress = nodeInfo.networkingAddress
    self.role = nodeInfo.role
    self.tokensStaked = nodeInfo.tokensStaked
    self.tokensCommitted = nodeInfo.tokensCommitted
    self.tokensUnstaking = nodeInfo.tokensUnstaking
    self.tokensUnstaked = nodeInfo.tokensUnstaked
    self.tokensRewarded = nodeInfo.tokensRewarded
    self.delegatorIDCounter = nodeInfo.delegatorIDCounter
    self.tokensRequestedToUnstake = nodeInfo.tokensRequestedToUnstake
    self.initialWeight = nodeInfo.initialWeight
  }
}

access(all)struct DelegatorInfo {
  access(all)let id: UInt32
  access(all)let nodeID: String
  access(all)let tokensCommitted: UFix64
  access(all)let tokensStaked: UFix64
  access(all)let tokensUnstaking: UFix64
  access(all)let tokensRewarded: UFix64
  access(all)let tokensUnstaked: UFix64
  access(all)let tokensRequestedToUnstake: UFix64

  init(nodeID: String, delegatorID: UInt32) {
    let delegatorInfo = FlowIDTableStaking.DelegatorInfo(nodeID: nodeID, delegatorID: delegatorID)

    self.id = delegatorInfo.id
    self.nodeID = delegatorInfo.nodeID
    self.tokensCommitted = delegatorInfo.tokensCommitted
    self.tokensStaked = delegatorInfo.tokensStaked
    self.tokensUnstaking = delegatorInfo.tokensUnstaking
    self.tokensRewarded = delegatorInfo.tokensRewarded
    self.tokensUnstaked = delegatorInfo.tokensUnstaked
    self.tokensRequestedToUnstake = delegatorInfo.tokensRequestedToUnstake
  }
}

access(all)fun main(address: Address): Result {
  let tokenHolderRef = 
      getAuthAccount(address)
          .borrow<&LockedTokens.TokenHolder>(from: LockedTokens.TokenHolderStoragePath)

  var stakingInfo: StakingInfo? = nil
  if let tokenHolder = tokenHolderRef {
    let lockedAddress = tokenHolder.getLockedAccountAddress()       
    let lockedBalance = tokenHolder.getLockedAccountBalance()
    let unlockLimit = tokenHolder.getUnlockLimit()
    
    var nodeInfo: NodeInfo? = nil
    if let nodeID = tokenHolder.getNodeID() {
      nodeInfo = NodeInfo(nodeID: nodeID)
    }

    var delegatorNodeInfo: NodeInfo? = nil
    var delegatorInfo: DelegatorInfo? = nil
    if let delegatorNodeID = tokenHolder.getDelegatorNodeID() {
      if let delegatorID = tokenHolder.getDelegatorID() {
        delegatorNodeInfo = NodeInfo(nodeID: delegatorNodeID)
        delegatorInfo = DelegatorInfo(nodeID: delegatorNodeID, delegatorID: delegatorID)
      } 
    } 

    let epochInfo: EpochInfo = EpochInfo(
      currentEpochCounter: FlowEpoch.currentEpochCounter,
      currentEpochPhase: FlowEpoch.currentEpochPhase.rawValue
    )

    stakingInfo = StakingInfo(
      epochInfo: epochInfo,
      lockedAddress: lockedAddress,
      lockedBalance: lockedBalance,
      unlockLimit: unlockLimit,
      nodeInfo: nodeInfo,
      delegatorNodeInfo: delegatorNodeInfo,
      delegatorInfo: delegatorInfo 
    )
  }

  return Result(stakingInfo: stakingInfo)
}
```