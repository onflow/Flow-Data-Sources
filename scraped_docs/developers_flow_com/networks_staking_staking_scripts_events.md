# Source: https://developers.flow.com/networks/staking/staking-scripts-events

Query Staking Info with Scripts or Events | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)

  + [Epoch and Staking Terminology](/networks/staking/epoch-terminology)
  + [Epoch and Reward Schedule](/networks/staking/schedule)
  + [Epoch Preparation Protocol](/networks/staking/epoch-preparation)
  + [Stake Slashing](/networks/staking/stake-slashing)
  + [Epoch Scripts and Events](/networks/staking/epoch-scripts-events)
  + [Staking Technical Overview](/networks/staking/technical-overview)
  + [Staking Scripts and Events](/networks/staking/staking-scripts-events)
  + [How to Query Staking rewards](/networks/staking/staking-rewards)
  + [QC and DKG](/networks/staking/qc-dkg)
  + [QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)
  + [Machine Account](/networks/staking/machine-account)
  + [FAQs](/networks/staking/faq)
  + [Technical Staking Options](/networks/staking/staking-options)
  + [Staking Collection Guide](/networks/staking/staking-collection)
  + [Basic Staking Guide (Deprecated)](/networks/staking/staking-guide)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Staking and Epochs](/networks/staking)
* Staking Scripts and Events

On this page

# Introduction

The staking contract stores a lot of different state, and the state is constantly changing.
As an external party, there are two ways to keep track of these state changes.
You can either use Cadence scripts to query the state of the contract at any given time,
or you can monitor events that are emitted by the staking contract to be notified of any important occurances.

# Query Information with Scripts

## Get the list of proposed nodes for the next epoch:[​](#get-the-list-of-proposed-nodes-for-the-next-epoch "Direct link to Get the list of proposed nodes for the next epoch:")

`FlowIDTableStaking.getProposedNodeIDs()`: Returns an array of node IDs for proposed nodes.
Proposed nodes are nodes that have enough staked and committed for the next epoch
to be above the minimum requirement and have been selected to participate in the next epoch.
This means that new access nodes that have not been selected with the random slot selection algorithm
will not be included in this list.

You can use the **Get Proposed Table**([SC.05](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script for retrieving this info.

This script requires no arguments.

## Get the list of all nodes that are currently staked:[​](#get-the-list-of-all-nodes-that-are-currently-staked "Direct link to Get the list of all nodes that are currently staked:")

`FlowIDTableStaking.getStakedNodeIDs()` and ``FlowIDTableStaking.getParticipantNodeList()`:
Returns an array of nodeIDs that are currently staked.
Staked nodes are nodes that are staked and participating in the current epoch.

You can use the **Get Current Table**([SC.04](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script for retrieving this info.

This script requires no arguments.

## Get the list of all Candidate Nodes[​](#get-the-list-of-all-candidate-nodes "Direct link to Get the list of all Candidate Nodes")

`getCandidateNodeList(): {UInt8: {String: Bool}}`:
Returns a dictionary of nodes that are candidates to stake in the next epoch
but are not staked in the current epoch.

You can use the [**Get Candidate Node List**](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L1762) script for retrieving this info.

This script requires no arguments.

## Get all of the info associated with a single node staker:[​](#get-all-of-the-info-associated-with-a-single-node-staker "Direct link to Get all of the info associated with a single node staker:")

`FlowIDTableStaking.NodeInfo(nodeID: String)`: Returns a `NodeInfo` struct with all of the metadata
associated with the specified node ID. You can see the `NodeInfo` definition in the [FlowIDTableStaking
smart contract.](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L254)

You can use the **Get Node Info**([SC.08](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script
with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID of the node to search for. |

You can also query the info from an address that uses the staking collection by using the **Get Node Info From Address**([SCO.15](/build/core-contracts/staking-collection#scripts)) script
with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Address` | The address of the account that manages the nodes. |

## Get the total committed balance of a node (with delegators):[​](#get-the-total-committed-balance-of-a-node-with-delegators "Direct link to Get the total committed balance of a node (with delegators):")

`FlowIDTableStaking.NodeInfo(_ nodeID: String).totalCommittedWithDelegators()`: Returns the total committed balance for a node,
which is their total tokens staked + committed, plus all of the staked + committed tokens of all their delegators.

You can use the **Get Node Total Commitment**([SC.09](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script
with the following argument:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID of the node to search for. |

## Get the total committed balance of a node (without delegators):[​](#get-the-total-committed-balance-of-a-node-without-delegators "Direct link to Get the total committed balance of a node (without delegators):")

`FlowIDTableStaking.NodeInfo(_ nodeID: String).totalCommittedWithoutDelegators()`: Returns the total committed balance for a node,
which is their total tokens staked + committed, plus all of the staked + committed tokens of all their delegators.

You can use the **Get Only Node Total Commitment**([SC.11](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script
with the following argument:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID of the node to search for. |

## Get all the info associated with a single delegator:[​](#get-all-the-info-associated-with-a-single-delegator "Direct link to Get all the info associated with a single delegator:")

`FlowIDTableStaking.DelegatorInfo(nodeID: String, delegatorID: UInt32)`: Returns a `DelegatorInfo` struct with all of the metadata
associated with the specified node ID and delegator ID. You can see the `DelegatorInfo` definition in the [FlowIDTableStaking
smart contract.](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L375)

You can use the **Get Delegator Info**([SC.10](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts))
script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID that the delegator delegates to. |
| **delegatorID** | `String` | The ID of the delegator to search for. |

You can also query the info from an address by using the **Get Delegator Info From Address**([SCO.16](/build/core-contracts/staking-collection#scripts)) script
with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Address` | The address of the account that manages the delegator. |

## Get the delegation cut percentage:[​](#get-the-delegation-cut-percentage "Direct link to Get the delegation cut percentage:")

`FlowIDTableStaking.getRewardCutPercentage(): UFix64`: Returns a `UFix64` number for the cut of delegator rewards that each node operator takes.

You can use the **Get Cut Percentage**([SC.01](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script to retrieve this info.

This script requires no arguments.

## Get the minimum stake requirements:[​](#get-the-minimum-stake-requirements "Direct link to Get the minimum stake requirements:")

`FlowIDTableStaking.getMinimumStakeRequirements(): {UInt8: UFix64}`: Returns a mapping
for the stake requirements for each node type.

You can use the **Get stake requirements**([SC.02](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script to retrieve this info.

This script requires no arguments.

## Get the total weekly reward payout:[​](#get-the-total-weekly-reward-payout "Direct link to Get the total weekly reward payout:")

`FlowIDTableStaking.getEpochTokenPayout(): UFix64`: Returns a `UFix64` value for the total number of FLOW paid out each epoch (week).

You can use the **Get weekly payout**([SC.03](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script to retrieve this info.

This script requires no arguments.

## Get the total FLOW staked:[​](#get-the-total-flow-staked "Direct link to Get the total FLOW staked:")

You can use the **Get total FLOW staked**([SC.06](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script to retrieve this info.

This script requires no arguments.

## Get the total FLOW staked by all the nodes of a single node role:[​](#get-the-total-flow-staked-by-all-the-nodes-of-a-single-node-role "Direct link to Get the total FLOW staked by all the nodes of a single node role:")

You can use the **Get total FLOW staked by node type**([SC.07](/build/core-contracts/staking-contract-reference#getting-staking-info-with-scripts)) script
with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeType** | `UInt8` | The type of node to search for. |

# Staking Events

Staking events can be queried using the Go or JavaScript SDKs to extract useful notifications and information about the
state of the staking process.

## Global Staking and Epoch Events[​](#global-staking-and-epoch-events "Direct link to Global Staking and Epoch Events")

### NewEpoch[​](#newepoch "Direct link to NewEpoch")

`_10

access(all) event NewEpoch(totalStaked: UFix64, totalRewardPayout: UFix64, newEpochCounter: UInt64)`

| Field | Type | Description |
| --- | --- | --- |
| totalStaked | UFix64 | The total number of tokens staked for the new Epoch |
| totalRewardPayout | UFix64 | The total number of tokens that will be paid as rewards for this epoch |
| newEpochCounter | UInt64 | The epoch counter for this new epoch |

Emitted by `FlowIDTableStaking.Admin.moveTokens()` when the tokens are moved between pools, which signals a new epoch.

### NewWeeklyPayout[​](#newweeklypayout "Direct link to NewWeeklyPayout")

`_10

access(all) event NewWeeklyPayout(newPayout: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| newPayout | UFix64 | The new number of tokens that will be paid at the end of the epoch |

Emitted by `FlowIDTableStaking.Admin.setEpochTokenPayout()` when the Admin changes the total tokens paid at the end of the epoch.

After this event the `epochTokenPayout` is equal to the new value.

## Node Events[​](#node-events "Direct link to Node Events")

These are events that concern the operation of a node.

### NewNodeCreated[​](#newnodecreated "Direct link to NewNodeCreated")

`_10

access(all) event NewNodeCreated(nodeID: String, role: UInt8, amountCommitted: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. Usually the hash of the node's public key. |
| role | UInt8 | The node's role type. From 1 to 5 inclusive. |
| amountCommitted | UFix64 | The amount of FLOW tokens staked to register the node. This is determined by the `role`. |

Emitted by `FlowIDTableStaking.NodeRecord.init()` when a new node is successfully created.

After this event is emitted for your node, you can begin to perform staking transactions using it.

### NodeRemovedAndRefunded[​](#noderemovedandrefunded "Direct link to NodeRemovedAndRefunded")

`_10

access(all) event NodeRemovedAndRefunded(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of FLOW tokens returned to the node. |

Emitted by `FlowIDTableStaking.Admin.endStakingAuction()` if the node is being removed from the next epoch
due to a failure to meet the minimum requirements of committed tokens for the next epoch.

After this event, the refunded FLOW tokens will be part of the node's `tokensUnstaked` balance.

## Token Events[​](#token-events "Direct link to Token Events")

These are events that concern the direct usage of FLOW tokens - staking or unstaking locked tokens, withdrawing rewards, etc.

Events emitted when using delegation are described in the next section.

### TokensCommitted[​](#tokenscommitted "Direct link to TokensCommitted")

`_10

access(all) event TokensCommitted(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of additional FLOW tokens committed to the node. |

Emitted whenever additional tokens are staked on the node for the following epoch. Specifically:

1. By `FlowIDTableStaking.NodeStaker.stakeNewTokens()` when new tokens (tokens that have not previously been staked) are added to the system
   to stake on the node during the next epoch.
2. By `FlowIDTableStaking.NodeStaker.stakeUnstakedTokens()` when unstaked tokens (tokens that were previously staked and then unstaked)
   are staked again with the node for the next epoch.
3. By `FlowIDTableStaking.NodeStaker.stakeRewardedTokens()` when reward tokens (tokens paid in return for previous staking)
   are staked with the node for the next epoch.

After this event, the FLOW tokens will be part of the node's `tokensCommitted` balance.

### TokensStaked[​](#tokensstaked "Direct link to TokensStaked")

`_10

access(all) event TokensStaked(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of FLOW tokens staked to the node. |

Emitted by `FlowIDTableStaking.Admin.moveTokens()` at the end of an epoch if committed tokens are being added to the node's tokensStaked balance.

After this event, the tokens will be part of the node's staked balance.

### TokensUnstaking[​](#tokensunstaking "Direct link to TokensUnstaking")

`_10

access(all) event TokensUnstaking(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of FLOW tokens unstaked from the node. |

Emitted by `FlowIDTableStaking.Admin.moveTokens()` at the end of an epoch if
a node operator's staked tokens are being unstaked in response to a request from the node operator.
After this event, the tokens will be a part of the node operator's `tokensUnstaking` balance, where they are held for a whole epoch "unstaking period" with no rewards.

### TokensUnstaked[​](#tokensunstaked "Direct link to TokensUnstaked")

`_10

access(all) event TokensUnstaked(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of FLOW tokens unstaked from the node. |

Emitted by `FlowIDTableStaking.NodeStaker.requestUnstaking()` and `FlowIDTableStaking.Admin.moveTokens()`
when tokens are deposited into the `tokensUnstaked` pool:

### RewardsPaid[​](#rewardspaid "Direct link to RewardsPaid")

`_10

access(all) event RewardsPaid(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of FLOW tokens paid to the node this epoch as a reward. |

Emitted by `FlowIDTableStaking.Admin.payRewards()` at the end of the epoch to pay rewards to node operators based on the tokens that they have staked.

After this event, the reward tokens will be part of the node's tokensRewarded balance.

The Delegator rewards are paid at the same time, see `DelegatorRewardsPaid` below.

### UnstakedTokensWithdrawn[​](#unstakedtokenswithdrawn "Direct link to UnstakedTokensWithdrawn")

`_10

access(all) event UnstakedTokensWithdrawn(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of unstaked FLOW tokens that the node operator is withdrawing. |

Emitted by `FlowIDTableStaking.NodeStaker.withdrawUnstakedTokens()` when the node operator calls that function to withdraw part or all of their
unstaked tokens balance.

After this event, the FLOW tokens will be withdrawn to a newly created `FungibleToken.Vault` which the caller can deposit to the vault of their choice.

### RewardTokensWithdrawn[​](#rewardtokenswithdrawn "Direct link to RewardTokensWithdrawn")

`_10

access(all) event RewardTokensWithdrawn(nodeID: String, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| amount | UFix64 | The amount of rewarded FLOW tokens that the node operator is withdrawing. |

Emitted by `FlowIDTableStaking.NodeStaker.withdrawRewardedTokens()` when the node operator calls that function to withdraw part or all of their
reward tokens balance.

After this event, the FLOW tokens will be withdrawn to a newly created `FungibleToken.Vault` which the caller can deposit to the vault of their choice.

## Delegator Events[​](#delegator-events "Direct link to Delegator Events")

These are events that concern FLOW token delegation.

### NewDelegatorCreated[​](#newdelegatorcreated "Direct link to NewDelegatorCreated")

`_10

access(all) event NewDelegatorCreated(nodeID: String, delegatorID: UInt32)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UFix64 | The ID for the new delegator. Unique within the node but not globally. |

Emitted by `FlowIDTableStaking.Admin.registerNewDelegator()` when the node operator registers a new delegator for the node.

Note that the delegatorID is unique within the node but is not globally unique.

After this event, the new delegator is registered with the node.

### DelegatorTokensCommitted[​](#delegatortokenscommitted "Direct link to DelegatorTokensCommitted")

`_10

access(all) event DelegatorTokensCommitted(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UInt32 | The ID for the delegator. |
| amount | UFix64 | The amount of additional FLOW tokens committed to the node. |

Emitted whenever additional tokens are committed for a delegator for the following epoch. Specifically:

1. By `FlowIDTableStaking.NodeDelegator.delegateNewTokens()` when new tokens (tokens that have not previously been staked) are added to the system
   to stake with the delegator during the next epoch.
2. By `FlowIDTableStaking.NodeDelegator.delegateUnstakedTokens()` when unstaked tokens (tokens that were previously staked and then unstaked)
   are staked again with the delegator for the next epoch.
3. By `FlowIDTableStaking.NodeDelegator.delegateRewardedTokens()` when reward tokens (tokens paid in return for previous staking)
   are staked with the delegator for the next epoch.

After this event, the FLOW tokens will be part of the delegator's `tokensCommitted` balance.

### DelegatorTokensStaked[​](#delegatortokensstaked "Direct link to DelegatorTokensStaked")

`_10

access(all) event DelegatorTokensStaked(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UInt32 | The ID for the delegator. |
| amount | UFix64 | The amount of FLOW tokens staked to the node. |

Emitted by `FlowIDTableStaking.Admin.moveTokens()` at the end of an epoch if committed tokens are being added to the delegator's tokensStaked balance.

After this event, the tokens will be part of the delegator's staked balance.

### DelegatorTokensUnstaking[​](#delegatortokensunstaking "Direct link to DelegatorTokensUnstaking")

`_10

access(all) event DelegatorTokensUnstaking(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UInt32 | The ID for the delegator. |
| amount | UFix64 | The amount of FLOW tokens unstaked from the node. |

Emitted by `FlowIDTableStaking.Admin.moveTokens()` at the end of an epoch if
a delegator's staked tokens are being unstaked in response to a request from the delegator.
After this event, the tokens will be a part of the delegator's `tokensUnstaking` balance, where they are held for a whole epoch "unstaking period" with no rewards.

### DelegatorTokensUnstaked[​](#delegatortokensunstaked "Direct link to DelegatorTokensUnstaked")

`_10

access(all) event DelegatorTokensUnstaked(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UInt32 | The ID for the delegator. |
| amount | UFix64 | The amount of FLOW tokens unstaked from the node. |

Emitted by `FlowIDTableStaking.NodeDelegator.requestUnstaking()` and `FlowIDTableStaking.Admin.moveTokens()`
when tokens are deposited into the delegator's `tokensUnstaked` pool:

### DelegatorRewardsPaid[​](#delegatorrewardspaid "Direct link to DelegatorRewardsPaid")

`_10

access(all) event DelegatorRewardsPaid(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UFix64 | The ID for the delegator. Unique within the node but not globally. |
| amount | UFix64 | The amount of rewarded FLOW tokens that the delegator is paid. |

Emitted by `FlowIDTableStaking.Admin.payRewards()` at the end of an epoch when rewards are being paid.

After this event is emitted, the reward tokens will be part of the delegator's tokensRewarded balance.

The Node rewards are paid at the same time, see `RewardsPaid` above.

### DelegatorUnstakedTokensWithdrawn[​](#delegatorunstakedtokenswithdrawn "Direct link to DelegatorUnstakedTokensWithdrawn")

`_10

access(all) event DelegatorUnstakedTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UFix64 | The ID for the delegator. Unique within the node but not globally. |
| amount | UFix64 | The amount of unstaked FLOW tokens that the delegator is withdrawing. |

Emitted by `FlowIDTableStaking.NodeDelegator.withdrawUnstakedTokens()` when the delegator calls that function to withdraw part or all of their
unstaked tokens balance.

After this event, the FLOW tokens will be withdrawn to a newly created `FungibleToken.Vault` which the caller can deposit to the vault of their choice.

### DelegatorRewardTokensWithdrawn[​](#delegatorrewardtokenswithdrawn "Direct link to DelegatorRewardTokensWithdrawn")

`_10

access(all) event DelegatorRewardTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| nodeID | String | The unique ID string for the node. 32 bytes. The same value emitted in the `NewNodeCreated` event for the node. |
| delegatorID | UFix64 | The ID for the delegator. Unique within the node but not globally. |
| amount | UFix64 | The amount of rewarded FLOW tokens that the delegator is withdrawing. |

Emitted by `FlowIDTableStaking.NodeDelegator.withdrawRewardedTokens()` when the delegator calls that function to withdraw part or all of their
unstaked tokens balance.

After this event, the FLOW tokens will be withdrawn to a newly created `FungibleToken.Vault` which the caller can deposit to the vault of their choice.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/07-staking-scripts-events.md)

Last updated on **Mar 13, 2025** by **j pimmel**

[Previous

Staking Technical Overview](/networks/staking/technical-overview)[Next

How to Query Staking rewards](/networks/staking/staking-rewards)

###### Rate this page

😞😐😊

* [Get the list of proposed nodes for the next epoch:](#get-the-list-of-proposed-nodes-for-the-next-epoch)
* [Get the list of all nodes that are currently staked:](#get-the-list-of-all-nodes-that-are-currently-staked)
* [Get the list of all Candidate Nodes](#get-the-list-of-all-candidate-nodes)
* [Get all of the info associated with a single node staker:](#get-all-of-the-info-associated-with-a-single-node-staker)
* [Get the total committed balance of a node (with delegators):](#get-the-total-committed-balance-of-a-node-with-delegators)
* [Get the total committed balance of a node (without delegators):](#get-the-total-committed-balance-of-a-node-without-delegators)
* [Get all the info associated with a single delegator:](#get-all-the-info-associated-with-a-single-delegator)
* [Get the delegation cut percentage:](#get-the-delegation-cut-percentage)
* [Get the minimum stake requirements:](#get-the-minimum-stake-requirements)
* [Get the total weekly reward payout:](#get-the-total-weekly-reward-payout)
* [Get the total FLOW staked:](#get-the-total-flow-staked)
* [Get the total FLOW staked by all the nodes of a single node role:](#get-the-total-flow-staked-by-all-the-nodes-of-a-single-node-role)
* [Global Staking and Epoch Events](#global-staking-and-epoch-events)
  + [NewEpoch](#newepoch)
  + [NewWeeklyPayout](#newweeklypayout)
* [Node Events](#node-events)
  + [NewNodeCreated](#newnodecreated)
  + [NodeRemovedAndRefunded](#noderemovedandrefunded)
* [Token Events](#token-events)
  + [TokensCommitted](#tokenscommitted)
  + [TokensStaked](#tokensstaked)
  + [TokensUnstaking](#tokensunstaking)
  + [TokensUnstaked](#tokensunstaked)
  + [RewardsPaid](#rewardspaid)
  + [UnstakedTokensWithdrawn](#unstakedtokenswithdrawn)
  + [RewardTokensWithdrawn](#rewardtokenswithdrawn)
* [Delegator Events](#delegator-events)
  + [NewDelegatorCreated](#newdelegatorcreated)
  + [DelegatorTokensCommitted](#delegatortokenscommitted)
  + [DelegatorTokensStaked](#delegatortokensstaked)
  + [DelegatorTokensUnstaking](#delegatortokensunstaking)
  + [DelegatorTokensUnstaked](#delegatortokensunstaked)
  + [DelegatorRewardsPaid](#delegatorrewardspaid)
  + [DelegatorUnstakedTokensWithdrawn](#delegatorunstakedtokenswithdrawn)
  + [DelegatorRewardTokensWithdrawn](#delegatorrewardtokenswithdrawn)

Documentation

* [Getting Started](/build/getting-started/contract-interaction)
* [SDK's & Tools](/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/guides/mobile/overview)
* [FCL](/tools/clients/fcl-js)
* [Testing](/build/smart-contracts/testing)
* [CLI](/tools/flow-cli)
* [Emulator](/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.onflow.org/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://open-cadence.onflow.org)
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.onflow.org/)
* [Flowscan Mainnet](https://flowdscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.onflow.org/)
* [OnFlow](https://onflow.org/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.