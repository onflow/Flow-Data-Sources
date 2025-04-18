# Source: https://developers.flow.com/networks/staking/technical-overview

Staking Technical Overview | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* Staking Technical Overview

On this page

warning

If you haven't read the Introduction, please read that first. That document
provides a non-technical overview of staking on Flow for all users and is a
necessary prerequisite to this document.

warning

This document assumes you have some technical knowledge about the Flow
blockchain and programming environment.

# Staking

This document describes the functionality of the
[core identity table and staking smart contract](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc).
It gives an overview of the process of epochs, staking as a node, and delegation. It is an important prerequisite
to understand before proceeding with any other technical integration or interaction with the Flow Protocol,
but does not provide step-by-step instructions for how to perform specific actions. See the
[Staking Collection Docs for instructions](/networks/staking/staking-collection)

This document also describes how to read public staking data from the contract.
Anyone can read public data from the staking smart contract with these instructions.

The transactions described in this document are contained in the
[`flow-core-contracts/transactions/idTableStaking/`](https://github.com/onflow/flow-core-contracts/tree/master/transactions/idTableStaking)
directory. You can see the text of all the transactions used to interact with the smart contract there.

## Smart Contract Summary[​](#smart-contract-summary "Direct link to Smart Contract Summary")

The Flow staking smart contract manages a record of stakers who have staked tokens for the network.
Users who want to stake can register with the staking contract at any time during the staking auction,
and their tokens will be locked for staking until they request to unstake them.

You should already understand from reading the [epoch documentation](/networks/staking/epoch-preparation)
that an epoch lasts roughly a week. The `FlowIDTableStaking` contract focuses on the identity table
and staking part of the epoch schedule.

Epoch Schedule from the perspective of the `FlowIDTableStaking` contract:

1. **Start of Epoch:** Generic metadata about the current epoch is updated and shared
   and the staking auction is enabled.
2. **Staking Auction:** Stakers can perform any action they want to manage their stake, like
   initially registering, staking new tokens, unstaking tokens, or withdrawing rewards.
   This phase takes up the vast majority of time in the epoch.
3. **End Staking Auction:** Stakers cannot perform any more staking actions
   until the start of the next epoch/staking auction.
4. **Remove Insufficiently Staked Nodes:** All node operators who don't meet the minimum
   or are not operating their node properly will be removed.
5. **Randomly Assign Nodes to New Slots:** Each node type has a configurable
   number of nodes that can operate during any given epoch.
   The contract will randomly select nodes from the list of newly staked and approved nodes
   to add them to the ID table. Once all the slots have been filled, the remaining nodes are refunded
   and can apply again for the next epoch if there are slots available.
6. **Rewards Calculation:** Calculate rewards for all the node operators staked in the current epoch.
7. **Move tokens between pools.** (See the token pools section for the order of movements)
8. **End Epoch:** Set the reward payout for the upcoming epoch and go to the top of this list.
9. **Rewards Payout:** Pay rewards to all the node operators staked
   from the previous epoch using the calculation from earlier in the epoch.

The `FlowIDTableStaking` contract manages the identity table, and all of these phases.
Control of these phases is controlled by the `FlowIDTableStaking.Admin` resource
object stored in the Flow Epoch account storage.
The `FlowEpoch` smart contract uses this resource to autonomously manage the functioning of the network. It is decentralized and managed by the node software, smart contracts,
and democratically by all the stakers in the network.

## Staking as a Node Operator[​](#staking-as-a-node-operator "Direct link to Staking as a Node Operator")

For a node to stake, node operators first need to generate their staking key,
staking key proof-of-possesion, networking address, and networking key.

The [node operation guide](/networks/node-ops)
describes how to run a node and generate node information.

To generate a node ID, simply hash the staking key.

Node operators need to determine the role of node they will be running
(Collection, Consensus, Execution, Verification, or Access).

warning

NOTE: Access Nodes are eligible to stake and have a staking minimum of 100 FLOW,
but will not receive rewards for their stake.
Please register as a different node type if you would like to receive rewards.

Once the info has been determined:

* Node role: `UInt8` (1 = Collection, 2 = Consensus, 3 = Execution, 4 = Verification, 5 = Access)
* Node ID: 32 byte `String` (64 hex characters)
* Networking Address: `String` (Length must be less than 510 characters and be a properly formatted IP address or hostname)
* Networking Key: 64 byte `String` (128 hex characters, must be a valid ECDSA-P256 Key)
* Staking Key: 96 byte `String` (192 hex characters, must be a valid BLS key)
* Staking Key Proof of Possesion: (48 byte (96 hex characters) string)

The node operator is ready to register their node.

warning

NOTE: The staking smart contract validates that the strings for the keys are
valid public keys. The staking admin and node software also checks the keys
and networking address to make sure they are valid and if they are not, the
registered node will not be eligible to stake.

To register a node, the node operator calls the
[`addNodeRecord` function](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L1552)
on the staking contract, providing all the node info and the tokens that they want to immediately stake, if any.

This registers the node in the Flow node identity table
and commits the specified tokens to stake during the next epoch.
This also returns a special node operator object that is stored in the node operator's account.
This object is used for staking, unstaking, and withdrawing rewards.

Consensus and Collection nodes also need to create a separate machine account
for use in the DKG and QC processes, respectively. This machine account creation
is handled automatically by the staking collection smart contract.
More information is in the [machine account documentation](/networks/staking/machine-account#creation).

warning

The register node transaction only needs to be submitted once per node. A node
does not need to register every epoch. A registration cannot be used to manage
multiple nodes. Multiple nodes need to be registered separately (with the
Staking Collection).

warning

Once a node operator has registered their node and its metadata, the metadata
cannot be modified. The only exception is the networking address, which can me
modified with the Update Networking Address transaction. If a node operator
wants to update any of their other metadata such as ID, keys, or role, they
need to unstake, withdraw their tokens, and register a completely new node.

Once node operators have registered and have the special node object, they will be able
to perform any of the valid staking options with it, assuming that they have
the required amount of tokens to perform each operation.

When the staking auction ends, if a node operator has committed less than the minimum stake required,
[or if their node information is invalid and they haven't been approved by the network,](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L788)
their committed tokens are moved to their unstaked pool, which they can withdraw from at any time.

Nodes who did have enough tokens committed and are approved will have their
[committed tokens moved to the staked state](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L923-L927)
at the end of the epoch if they are selected as a node operator
by the random node slot filling algorithm.
There is a configurable cap on the number of nodes of each type,
so if the number of selected nodes equals the cap, than newly registered nodes
will not be added to the network until the cap is raised or other nodes unstake.

If a node operator has users delegating to them, they cannot withdraw their own tokens
such that their own staked tokens would fall below the minimum requirement for that node type.
If they have delegators and try to submit [an unstaking transaction](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L510-L514)
that would put their stake below the minimum, it will fail.

If they want to unstake below the minimum, they must unstake all of their tokens using the special
[`unstakeAll` method,](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L538)
which also unstakes all of the tokens that have been delegated to them.

Consequently, a node operator cannot accept delegation unless [their own stake is above the minimum.](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L1066)

## Staking as a Delegator[​](#staking-as-a-delegator "Direct link to Staking as a Delegator")

Every staked non-access node in the Flow network is eligible for delegation by any other user.
The user only needs to know the node ID of the node they want to delegate to.

To register as a delegator, the delegator submits a **Register Delegator**
transaction that calls the [`registerNewDelegator function`](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L1590),
providing the ID of the node operator they want to delegate to.
This transaction should store the `NodeDelegator` object
in the user's account, which is what they use to perform staking operations.

Users are able to get a list of possible node IDs to delegate to via on-chain scripts.
This information will also be provided off-chain, directly from the node operators or via
third-party services. [Available node IDs are listed in a public repo.](https://github.com/onflow/flow/blob/master/nodeoperators/NodeOperatorList.md)

The fee that node operators take from the rewards their delegators receive is 8%.
A node operator cannot be delegated to unless the total tokens they have committed to stake
are above the minimum requirement for their node types.

The delegation logic keeps track of the amount of tokens each delegator has delegated for the node operator.
When rewards are paid, the protocol [automatically takes the 8% cut](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L888-L898)
of the delegator's rewards for the node operator
and the delegator's rewards are deposited in the delegator's reward pool.

## Staking Operations Available to All Stakers[​](#staking-operations-available-to-all-stakers "Direct link to Staking Operations Available to All Stakers")

Regardless of whether they are a node operator or delegator, a staker has access
to all the same staking operations, outlined below.
Specific implementations of these transactions are detailed in the [Staking Collection Docs](/networks/staking/staking-collection)

### Stake More Tokens[​](#stake-more-tokens "Direct link to Stake More Tokens")

A staker can commit more tokens to stake for the next epoch at any time during the staking auction,
and there are three different ways to do it.

1. They can commit new tokens to stake by submitting a **stake\_new\_tokens** transaction,
   which withdraws tokens from their account's flow token vault and commits them.
2. They can commit tokens that are in their unstaked token pool, which holds the tokens
   that they have unstaked. Submit a **stake\_unstaked\_tokens**
   transaction to move the tokens from the unstaked pool to the committed pool.
3. They can commit tokens that are in their rewarded token pool, which holds the tokens
   they have been awarded. They submit a **stake\_rewarded\_tokens**
   transaction to move the tokens from the rewards pool to the committed pool.

### Cancel Committed Stake / Unstake Tokens[​](#cancel-committed-stake--unstake-tokens "Direct link to Cancel Committed Stake / Unstake Tokens")

At any time during the staking auction, a staker can submit a request to unstake tokens with a **request\_unstaking** transaction.
If there are tokens that have been committed but are not staked yet,
they are moved to the unstaked pool and are available to withdraw.

If the requested tokens are in the staked pool,
it marks the specified amount of tokens to be unstaked at the end of the epoch.
At the end of the epoch, the tokens are moved to the unstaking pool.
They will sit in this pool for one (1) additional epoch,
at which point they will be moved to the unstaked tokens pool.

### Cancel an Unstake Request[​](#cancel-an-unstake-request "Direct link to Cancel an Unstake Request")

Unstaking requests are not fulfilled until the end of the epoch where they are submitted,
so a staker can cancel the unstaking request before it is carried out.
A staker can do this by submitting a **stake\_unstaked\_tokens** transaction, specifying
the number of tokens of their unstake request they would like to cancel.
If the specified number of tokens have been requested to unstake, the request will be canceled.

### Withdraw Unstaked Tokens[​](#withdraw-unstaked-tokens "Direct link to Withdraw Unstaked Tokens")

At any time, stakers are able to freely withdraw from their unstaked tokens pool
with the **withdraw\_unstaked** transaction.

### Withdraw Rewarded Tokens[​](#withdraw-rewarded-tokens "Direct link to Withdraw Rewarded Tokens")

Staking rewards are paid out at the end of every epoch based on how many tokens
are in a users `tokensStaked` pool. Every staker's rewards
are deposited into their rewarded tokens pool. Rewards can be withdrawn
at any time by submitting a **withdraw\_reward\_tokens** transaction.

These tokens are unlocked and can be transferred on-chain if desired, or re-staked.

The source code for the staking contract and more transactions
can be found in the [Flow Core Contracts GitHub Repository](https://github.com/onflow/flow-core-contracts).

# Monitor Events from the Identity Table and Staking Contract

See the [staking events document](/networks/staking/staking-scripts-events)
for information about the events that can be emitted by the staking contract.

# Appendix

## Token Pools[​](#token-pools "Direct link to Token Pools")

Each node operator has five token pools allocated to them:

* **Committed Tokens:** Tokens that are committed for the next epoch.
  They are automatically moved to the staked pool when the next epoch starts.
* **Staked Tokens:** Tokens that are staked by the node operator for the current epoch.
  They are only moved at the end of an epoch and if the staker
  has submitted an unstaking request.
* **Unstaking Tokens:** Tokens that have been unstaked,
  but are not free to withdraw until the following epoch.
* **Unstaked Tokens:** Tokens that are freely available to withdraw or re-stake.
  Unstaked tokens go to this pool.
* **Rewarded Tokens:** Tokens that are freely available to withdraw or re-stake.
  Rewards are paid and deposited to the rewarded Pool after each epoch.

At the end of every epoch, tokens are moved between pools in this order:

1. All committed tokens will get moved either to the staked tokens pool,
   or to the unstaked tokens pool (depending on if the registered node has met the minimum stake requirements).
2. All committed tokens get moved to staked tokens pool.
3. All unstaking tokens get moved to the unstaked tokens pool.
4. All requested unstaking tokens get moved from the staked pool to the unstaking pool.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/06-technical-overview.md)

Last updated on **Apr 17, 2025** by **leopardracer**

[Previous

Epoch Scripts and Events](/networks/staking/epoch-scripts-events)[Next

Staking Scripts and Events](/networks/staking/staking-scripts-events)

###### Rate this page

😞😐😊

* [Smart Contract Summary](#smart-contract-summary)
* [Staking as a Node Operator](#staking-as-a-node-operator)
* [Staking as a Delegator](#staking-as-a-delegator)
* [Staking Operations Available to All Stakers](#staking-operations-available-to-all-stakers)
  + [Stake More Tokens](#stake-more-tokens)
  + [Cancel Committed Stake / Unstake Tokens](#cancel-committed-stake--unstake-tokens)
  + [Cancel an Unstake Request](#cancel-an-unstake-request)
  + [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens)
  + [Withdraw Rewarded Tokens](#withdraw-rewarded-tokens)
* [Token Pools](#token-pools)

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
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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