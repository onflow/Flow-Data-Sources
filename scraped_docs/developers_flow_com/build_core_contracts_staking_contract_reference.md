# Source: https://developers.flow.com/build/core-contracts/staking-contract-reference




Flow Staking Contract Reference | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
* [Core Smart Contracts](/build/core-contracts)
  + [Fungible Token](/build/core-contracts/fungible-token)
  + [Flow Token](/build/core-contracts/flow-token)
  + [Service Account](/build/core-contracts/service-account)
  + [Flow Fees](/build/core-contracts/flow-fees)
  + [Staking Table](/build/core-contracts/staking-contract-reference)
  + [Epoch Contracts](/build/core-contracts/epoch-contract-reference)
  + [Non-Fungible Token](/build/core-contracts/non-fungible-token)
  + [NFT Metadata](/build/core-contracts/nft-metadata)
  + [NFT Storefront](/build/core-contracts/nft-storefront)
  + [Staking Collection](/build/core-contracts/staking-collection)
  + [Account Linking](/build/core-contracts/hybrid-custody)
  + [EVM](/build/core-contracts/evm)
  + [Burner](/build/core-contracts/burner)
* [Explore More](/build/explore-more)


* [Core Smart Contracts](/build/core-contracts)
* Staking Table
On this page
# Flow Staking Contract Reference

## Contract[​](#contract "Direct link to Contract")

The `FlowIDTableStaking` contract is the central table that manages staked nodes, delegation and rewards.

Source: [FlowIDTableStaking.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x9eca2b38b18b5dfe` |
| Mainnet | `0x8624b52f9ddcd04a` |

## Transactions and Scripts[​](#transactions-and-scripts "Direct link to Transactions and Scripts")

Transactions for the staking contract are in the `flow-core-contracts` repo.
Developers and users are advised to use [the staking collection transactions](/networks/staking/staking-collection)
to stake tokens instead of the basic transactions that are used for tests.

### Getting Staking Info with Scripts[​](#getting-staking-info-with-scripts "Direct link to Getting Staking Info with Scripts")

These scripts are read-only and get info about the current state of the staking contract.

| ID | Name | Source |
| --- | --- | --- |
| **`SC.01`** | Get Delegation Cut Percentage | [idTableStaking/get\_cut\_percentage.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_cut_percentage.cdc) |
| **`SC.02`** | Get Minimum Stake Requirements | [idTableStaking/get\_stake\_requirements.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_stake_requirements.cdc) |
| **`SC.03`** | Get Total Weekly Reward Payout | [idTableStaking/get\_weekly\_payout.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_weekly_payout.cdc) |
| **`SC.04`** | Get Current Staked Node Table | [idTableStaking/get\_current\_table.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_current_table.cdc) |
| **`SC.05`** | Get Proposed Staked Node Table | [idTableStaking/get\_proposed\_table.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_proposed_table.cdc) |
| **`SC.06`** | Get Total Flow Staked | [idTableStaking/get\_total\_staked.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_total_staked.cdc) |
| **`SC.07`** | Get Total Flow Staked by Node Type | [idTableStaking/get\_total\_staked\_by\_type.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_total_staked_by_type.cdc) |
| **`SC.08`** | Get All Info about a single NodeID | [idTableStaking/get\_node\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_info.cdc) |
| **`SC.09`** | Get a node's total Commitment (delegators) | [idTableStaking/get\_node\_total\_commitment.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_total_commitment.cdc) |
| **`SC.10`** | Get All Info about a single Delegator | [idTableStaking/delegation/get\_delegator\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/get_delegator_info.cdc) |
| **`SC.11`** | Get a node's total Commitment | [idTableStaking/get\_node\_total\_commitment\_without\_delegators.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_total_commitment_without_delegators.cdc) |

### Delegator Transactions[​](#delegator-transactions "Direct link to Delegator Transactions")

Documentation for delegating with tokens is described in the staking documentation
for [the staking collection](/networks/staking/staking-collection)

## Events[​](#events "Direct link to Events")

The `FlowIDTableStaking` contract emits an event whenever an important action occurs.
See the [staking events Documentation](/networks/staking/staking-scripts-events) for more information about each event.

 `_44 /// Epoch_44 access(all) event NewEpoch(_44 totalStaked: UFix64,_44 totalRewardPayout: UFix64,_44 newEpochCounter: UInt64_44 )_44 access(all) event EpochTotalRewardsPaid(_44 total: UFix64,_44 fromFees: UFix64,_44 minted: UFix64,_44 feesBurned: UFix64,_44 epochCounterForRewards: UInt64_44 )_44_44 /// Node_44 access(all) event NewNodeCreated(nodeID: String, role: UInt8, amountCommitted: UFix64)_44 access(all) event TokensCommitted(nodeID: String, amount: UFix64)_44 access(all) event TokensStaked(nodeID: String, amount: UFix64)_44 access(all) event NodeTokensRequestedToUnstake(nodeID: String, amount: UFix64)_44 access(all) event TokensUnstaking(nodeID: String, amount: UFix64)_44 access(all) event TokensUnstaked(nodeID: String, amount: UFix64)_44 access(all) event NodeRemovedAndRefunded(nodeID: String, amount: UFix64)_44 access(all) event RewardsPaid(nodeID: String, amount: UFix64, epochCounter: UInt64)_44 access(all) event UnstakedTokensWithdrawn(nodeID: String, amount: UFix64)_44 access(all) event RewardTokensWithdrawn(nodeID: String, amount: UFix64)_44 access(all) event NetworkingAddressUpdated(nodeID: String, newAddress: String)_44 access(all) event NodeWeightChanged(nodeID: String, newWeight: UInt64)_44_44 /// Delegator_44 access(all) event NewDelegatorCreated(nodeID: String, delegatorID: UInt32)_44 access(all) event DelegatorTokensCommitted(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorTokensStaked(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorTokensRequestedToUnstake(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorTokensUnstaking(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorTokensUnstaked(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorRewardsPaid(nodeID: String, delegatorID: UInt32, amount: UFix64, epochCounter: UInt64)_44 access(all) event DelegatorUnstakedTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)_44 access(all) event DelegatorRewardTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)_44_44 /// Contract Fields_44 access(all) event NewDelegatorCutPercentage(newCutPercentage: UFix64)_44 access(all) event NewWeeklyPayout(newPayout: UFix64)_44 access(all) event NewStakingMinimums(newMinimums: {UInt8: UFix64})_44 access(all) event NewDelegatorStakingMinimum(newMinimum: UFix64)`[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/06-staking-contract-reference.md)Last updated on **Jan 14, 2025** by **Giovanni Sanchez**[PreviousFlow Fees](/build/core-contracts/flow-fees)[NextEpoch Contracts](/build/core-contracts/epoch-contract-reference)
###### Rate this page

😞😐😊

* [Contract](#contract)
* [Transactions and Scripts](#transactions-and-scripts)
  + [Getting Staking Info with Scripts](#getting-staking-info-with-scripts)
  + [Delegator Transactions](#delegator-transactions)
* [Events](#events)
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

