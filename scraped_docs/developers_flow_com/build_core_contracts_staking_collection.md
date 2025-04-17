# Source: https://developers.flow.com/build/core-contracts/staking-collection

Flow Staking Collection Contract Reference | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
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
  + [VM Bridge](/build/core-contracts/bridge)
* [Explore More](/build/explore-more)

* [Core Smart Contracts](/build/core-contracts)
* Staking Collection

On this page

# Contract

The `FlowStakingCollection` contract is a contract that manages a resource containing a user's stake and delegation objects.

The `FlowStakingCollection` allows a user to manage multiple active nodes or delegators
and interact with node or delegator objects stored in either their optional locked account
or in the StakingCollection itself (stored in the main account).
If a user has locked tokens, StakingCollection allows a user to interact with their locked tokens
to perform staking actions for any of their nodes or delegators.

The staking collection also manages creating a node's machine accounts if they have any collector or consensus nodes.
It also allows them to deposit and withdraw tokens from any of their machine accounts through the staking collection.

See the [Staking Collection Docs](/networks/staking/staking-collection) for more information on the design of the staking collection contract.

Source: [FlowStakingCollection.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowStakingCollection.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x95e019a17d0e23d7` |
| Mainnet | `0x8d0e87b65159ae63` |

## Transactions[​](#transactions "Direct link to Transactions")

Use the following transactions to interact with the StakingCollection.

\_Note: The StakingCollection differentiates between stake and delegation requests through
passing an optional DelegatorID argument. For example, if you wish to Stake New Tokens for an active node,
pass `nil` as the optional DelegatorID argument to the Stake New Tokens transaction.
The same applies for all the other staking operation transactions.

| ID | Name | Source |
| --- | --- | --- |
| **`SCO.01`** | Setup Staking Collection | [stakingCollection/setup\_staking\_collection.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/setup_staking_collection.cdc) |
| **`SCO.02`** | Register Delegator | [stakingCollection/register\_delegator.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/register_delegator.cdc) |
| **`SCO.03`** | Register Node | [stakingCollection/register\_node.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/register_node.cdc) |
| **`SCO.04`** | Create Machine Account | [stakingCollection/create\_machine\_account.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/create_machine_account.cdc) |
| **`SCO.05`** | Request Unstaking | [stakingCollection/request\_unstaking.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/request_unstaking.cdc) |
| **`SCO.06`** | Stake New Tokens | [stakingCollection/stake\_new\_tokens.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/stake_new_tokens.cdc) |
| **`SCO.07`** | Stake Rewarded Tokens | [stakingCollection/stake\_rewarded\_tokens.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/stake_rewarded_tokens.cdc) |
| **`SCO.08`** | Stake Unstaked Tokens | [stakingCollection/stake\_unstaked\_tokens.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/stake_unstaked_tokens.cdc) |
| **`SCO.09`** | Unstake All | [stakingCollection/unstake\_all.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/unstake_all.cdc) |
| **`SCO.10`** | Withdraw Rewarded Tokens | [stakingCollection/withdraw\_rewarded\_tokens.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/withdraw_rewarded_tokens.cdc) |
| **`SCO.11`** | Withdraw Unstaked Tokens | [stakingCollection/withdraw\_unstaked\_tokens.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/withdraw_unstaked_tokens.cdc) |
| **`SCO.12`** | Close Stake | [stakingCollection/close\_stake.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/close_stake.cdc) |
| **`SCO.13`** | Transfer Node | [stakingCollection/transfer\_node.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/transfer_node.cdc) |
| **`SCO.14`** | Transfer Delegator | [stakingCollection/transfer\_delegator.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/transfer_delegator.cdc) |
| **`SCO.15`** | Withdraw From Machine Account | [stakingCollection/withdraw\_from\_machine\_account.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/withdraw_from_machine_account.cdc) |
| **`SCO.22`** | Update Networking Address | [stakingCollection/update\_networking\_address.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/update_networking_address.cdc) |

## Scripts[​](#scripts "Direct link to Scripts")

| ID | Name | Source |
| --- | --- | --- |
| **`SCO.16`** | Get All Delegator Info | [stakingCollection/scripts/get\_all\_delegator\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_all_delegator_info.cdc) |
| **`SCO.15`** | Get All Node Info | [stakingCollection/scripts/get\_all\_node\_info.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_all_node_info.cdc) |
| **`SCO.22`** | Get Delegator Ids | [stakingCollection/scripts/get\_delegator\_ids.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_delegator_ids.cdc) |
| **`SCO.17`** | Get Node Ids | [stakingCollection/scripts/get\_node\_ids.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_node_ids.cdc) |
| **`SCO.18`** | Get Does Stake Exist | [stakingCollection/scripts/get\_does\_stake\_exist.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_does_stake_exist.cdc) |
| **`SCO.19`** | Get Locked Tokens Used | [stakingCollection/scripts/get\_locked\_tokens\_used.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_locked_tokens_used.cdc) |
| **`SCO.20`** | Get Unlocked Tokens Used | [stakingCollection/scripts/get\_unlocked\_tokens\_used.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_unlocked_tokens_used.cdc) |
| **`SCO.21`** | Get Machine Accounts | [stakingCollection/scripts/get\_machine\_accounts.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/stakingCollection/scripts/get_machine_accounts.cdc) |

## Setup Transaction[​](#setup-transaction "Direct link to Setup Transaction")

To setup the Staking Collection for an account, use the `SC.01` transaction.

The setup process finds any node or delegator records already stored in the main account's storage,
as well as any in the associated locked account if an associated locked account exists.
It connects these node and delegator records with the new Staking Collection, allowing them
to be interacted with using the Staking Collection API.

## Events[​](#events "Direct link to Events")

The `StakingCollection` contract emits an event whenever an important action occurs.

`_10

access(all) event NodeAddedToStakingCollection(nodeID: String, role: UInt8, amountCommitted: UFix64, address: Address?)

_10

access(all) event DelegatorAddedToStakingCollection(nodeID: String, delegatorID: UInt32, amountCommitted: UFix64, address: Address?)

_10

_10

access(all) event NodeRemovedFromStakingCollection(nodeID: String, role: UInt8, address: Address?)

_10

access(all) event DelegatorRemovedFromStakingCollection(nodeID: String, delegatorID: UInt32, address: Address?)

_10

_10

access(all) event MachineAccountCreated(nodeID: String, role: UInt8, address: Address)`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/11-staking-collection.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

NFT Storefront](/build/core-contracts/nft-storefront)[Next

Account Linking](/build/core-contracts/hybrid-custody)

###### Rate this page

😞😐😊

* [Transactions](#transactions)
* [Scripts](#scripts)
* [Setup Transaction](#setup-transaction)
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
* [Flowscan Mainnet](https://flowscan.io/)
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