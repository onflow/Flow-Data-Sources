# Source: https://developers.flow.com/build/cadence/core-contracts/staking-contract-reference

Flow Staking Contract Reference | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              + [Core Smart Contracts](/build/cadence/core-contracts)

                - [Fungible Token](/build/cadence/core-contracts/fungible-token)- [Flow Token](/build/cadence/core-contracts/flow-token)- [Service Account](/build/cadence/core-contracts/service-account)- [Flow Fees](/build/cadence/core-contracts/flow-fees)- [Staking Table](/build/cadence/core-contracts/staking-contract-reference)- [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)- [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)- [NFT Metadata](/build/cadence/core-contracts/nft-metadata)- [NFT Storefront](/build/cadence/core-contracts/nft-storefront)- [Staking Collection](/build/cadence/core-contracts/staking-collection)- [Account Linking](/build/cadence/core-contracts/hybrid-custody)- [EVM](/build/cadence/core-contracts/evm)- [Burner](/build/cadence/core-contracts/burner)- [VM Bridge](/build/cadence/core-contracts/bridge)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* [Core Smart Contracts](/build/cadence/core-contracts)* Staking Table

On this page

# Flow Staking Contract Reference

The `FlowIDTableStaking` contract is the central table that manages staked nodes, delegation and rewards.

Source: [FlowIDTableStaking.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Contract Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Emulator `0xf8d6e0586b0a20c7`| Cadence Testing Framework `0x0000000000000001`| Testnet `0x9eca2b38b18b5dfe`| Mainnet `0x8624b52f9ddcd04a` | | | | | | | | | |

## Transactions and scripts[​](#transactions-and-scripts "Direct link to Transactions and scripts")

Transactions for the staking contract are in the `flow-core-contracts` repo. Developers and users are advised to use [the staking collection transactions](/protocol/staking/staking-collection) to stake tokens instead of the basic transactions that are used for tests.

### Getting staking info with scripts[​](#getting-staking-info-with-scripts "Direct link to Getting staking info with scripts")

These scripts are read-only and get info about the current state of the staking contract.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID Name Source|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **`SC.01`** Get Delegation Cut Percentage [idTableStaking/get\_cut\_percentage.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_cut_percentage.cdc)| **`SC.02`** Get Minimum Stake Requirements [idTableStaking/get\_stake\_requirements.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_stake_requirements.cdc)| **`SC.03`** Get Total Weekly Reward Payout [idTableStaking/get\_weekly\_payout.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_weekly_payout.cdc)| **`SC.04`** Get Current Staked Node Table [idTableStaking/get\_current\_table.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_current_table.cdc)| **`SC.05`** Get Proposed Staked Node Table [idTableStaking/get\_proposed\_table.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_proposed_table.cdc)| **`SC.06`** Get Total Flow Staked [idTableStaking/get\_total\_staked.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_total_staked.cdc)| **`SC.07`** Get Total Flow Staked by Node Type [idTableStaking/get\_total\_staked\_by\_type.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_total_staked_by_type.cdc)| **`SC.08`** Get All Info about a single NodeID [idTableStaking/get\_node\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_info.cdc)| **`SC.09`** Get a node's total Commitment (delegators) [idTableStaking/get\_node\_total\_commitment.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_total_commitment.cdc)| **`SC.10`** Get All Info about a single Delegator [idTableStaking/delegation/get\_delegator\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/delegation/get_delegator_info.cdc)| **`SC.11`** Get a node's total Commitment [idTableStaking/get\_node\_total\_commitment\_without\_delegators.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/idTableStaking/scripts/get_node_total_commitment_without_delegators.cdc) | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

### Delegator transactions[​](#delegator-transactions "Direct link to Delegator transactions")

Documentation for token delegation is described in the staking documentation
for [the staking collection](/protocol/staking/staking-collection).

## Events[​](#events "Direct link to Events")

The `FlowIDTableStaking` contract emits an event whenever an important action occurs.
See the [staking events Documentation](/protocol/staking/staking-scripts-events)for more information about each event.

`_44

/// Epoch

_44

access(all) event NewEpoch(

_44

totalStaked: UFix64,

_44

totalRewardPayout: UFix64,

_44

newEpochCounter: UInt64

_44

)

_44

access(all) event EpochTotalRewardsPaid(

_44

total: UFix64,

_44

fromFees: UFix64,

_44

minted: UFix64,

_44

feesBurned: UFix64,

_44

epochCounterForRewards: UInt64

_44

)

_44

_44

/// Node

_44

access(all) event NewNodeCreated(nodeID: String, role: UInt8, amountCommitted: UFix64)

_44

access(all) event TokensCommitted(nodeID: String, amount: UFix64)

_44

access(all) event TokensStaked(nodeID: String, amount: UFix64)

_44

access(all) event NodeTokensRequestedToUnstake(nodeID: String, amount: UFix64)

_44

access(all) event TokensUnstaking(nodeID: String, amount: UFix64)

_44

access(all) event TokensUnstaked(nodeID: String, amount: UFix64)

_44

access(all) event NodeRemovedAndRefunded(nodeID: String, amount: UFix64)

_44

access(all) event RewardsPaid(nodeID: String, amount: UFix64, epochCounter: UInt64)

_44

access(all) event UnstakedTokensWithdrawn(nodeID: String, amount: UFix64)

_44

access(all) event RewardTokensWithdrawn(nodeID: String, amount: UFix64)

_44

access(all) event NetworkingAddressUpdated(nodeID: String, newAddress: String)

_44

access(all) event NodeWeightChanged(nodeID: String, newWeight: UInt64)

_44

_44

/// Delegator

_44

access(all) event NewDelegatorCreated(nodeID: String, delegatorID: UInt32)

_44

access(all) event DelegatorTokensCommitted(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorTokensStaked(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorTokensRequestedToUnstake(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorTokensUnstaking(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorTokensUnstaked(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorRewardsPaid(nodeID: String, delegatorID: UInt32, amount: UFix64, epochCounter: UInt64)

_44

access(all) event DelegatorUnstakedTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

access(all) event DelegatorRewardTokensWithdrawn(nodeID: String, delegatorID: UInt32, amount: UFix64)

_44

_44

/// Contract Fields

_44

access(all) event NewDelegatorCutPercentage(newCutPercentage: UFix64)

_44

access(all) event NewWeeklyPayout(newPayout: UFix64)

_44

access(all) event NewStakingMinimums(newMinimums: {UInt8: UFix64})

_44

access(all) event NewDelegatorStakingMinimum(newMinimum: UFix64)`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/06-staking-contract-reference.md)

Last updated on **Dec 3, 2025** by **cshannon1218**

[Previous

Flow Fees](/build/cadence/core-contracts/flow-fees)[Next

Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)

###### Rate this page

😞😐😊

Copy as Markdown

* [Transactions and scripts](#transactions-and-scripts)
  + [Getting staking info with scripts](#getting-staking-info-with-scripts)+ [Delegator transactions](#delegator-transactions)* [Events](#events)

Flow

* [Build with AI](/blockchain-development-tutorials/use-AI-to-build-on-flow)* [Why Flow](/blockchain-development-tutorials/flow-101)* [Tools](/build/tools)* [Faucet](/ecosystem/faucets)* [Builder Toolkit](/ecosystem/developer-support-hub)

Cadence

* [Quickstart](/blockchain-development-tutorials/cadence/getting-started)* [Build with Forte](/blockchain-development-tutorials/forte)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* [React SDK](/build/tools/react-sdk)* [Language Reference](https://cadence-lang.org/)

Solidity (EVM)

* [Quickstart](/build/evm/quickstart)* [Native VRF](/blockchain-development-tutorials/native-vrf)* [Batched Transactions](/blockchain-development-tutorials/cross-vm-apps)* [Network Information](/build/evm/networks)

Community & Support

* [Dev Office Hours](https://calendar.google.com/calendar/u/0/embed?src=c_47978f5cd9da636cadc6b8473102b5092c1a865dd010558393ecb7f9fd0c9ad0@group.calendar.google.com)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Discord](https://discord.gg/flow)* [GitHub](https://github.com/onflow)* [Careers](https://flow.com/careers)

Network & Resources

* [Network Status](https://status.flow.com/)* [Block Explorer](https://flowscan.io/)* [Flow Port](https://port.flow.com/)* [Flow Website](https://flow.com/)* [Flow Blog](https://flow.com/blog)

Copyright © 2026 Flow Foundation. All Rights Reserved.