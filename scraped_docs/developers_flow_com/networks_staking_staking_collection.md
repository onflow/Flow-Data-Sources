# Source: https://developers.flow.com/networks/staking/staking-collection

Manage a Staking Collection | Flow Developer Portal



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
* Staking Collection Guide

On this page

This document outlines the steps a token holder can take to stake
using [the `FlowIDTableStaking` contract](/build/core-contracts/staking-contract-reference)
and [the `FlowStakingCollection` contract.](/build/core-contracts/staking-collection)
This is the recommended and most supported way to stake FLOW.
It supports any number of nodes and delegators per account, supports locked and unlocked FLOW,
and supports easily interaction with a node's machine account for collector and consensus nodes.

# Staking Collection Overview

A Staking Collection is a resource that allows its owner to manage multiple staking
objects in a single account via a single storage path, and perform staking actions
using both locked and unlocked Flow.

Before the staking collection, accounts could use the instructions in
[the unlocked staking guide](/networks/staking/staking-guide)
to stake with tokens. This was a bit restrictive, because that guide (and the corresponding transactions)
only supports one node and one delegator object
per account. If a user wanted to have more than one per account,
they would either have to use custom transactions with custom storage paths for each object,
or they would have had to use multiple accounts, which comes with many hassles of its own.

The staking collection is a solution to both of these deficiencies.
When an account is set up to use a staking collection, the staking collection recognizes
the existing locked account capabilities (if they exist) and unlocked account staking objects,
and incorporates their functionality so any user can stake for a node or stake as a delegator
through a single common interface, regardless of if they have a brand new account,
or have been staking through the locked account or unlocked account before.

The staking collection also easily allows a user to transfer their node or delegator objects
to other accounts without interrupting the staking process!

## Staker Object Fields[​](#staker-object-fields "Direct link to Staker Object Fields")

The staking collection resource has two main fields,

`_10

access(self) var nodeStakers: @{String: FlowIDTableStaking.NodeStaker}

_10

access(self) var nodeDelegators: @{String: FlowIDTableStaking.NodeDelegator}`

These dictionaries store the staking objects that are managed by the staking collection.
Access to these dictionaries are mediated by the staking methods.
When a user wants to perform a staking operation,
they specify the nodeID and/or delegatorID they want to stake for, and the function routes the function
call to the correct staking object and performs the specified operation.

## Vault Capability Fields[​](#vault-capability-fields "Direct link to Vault Capability Fields")

The staking collection also has a field that stores a capability for
the unlocked FLOW Vault and locked FLOW vault (if applicable)

`_10

/// unlocked vault

_10

access(self) var unlockedVault: Capability<&FlowToken.Vault>

_10

_10

/// locked vault

_10

/// will be nil if the account has no corresponding locked account

_10

access(self) var lockedVault: Capability<&FlowToken.Vault>?`

When a user performs staking operations like staking new tokens,
the staking collection tracks the number of unlocked tokens
and locked tokens (if applicable) that are used by the staking objects in the collection.
The collection will always try to stake any available locked tokens first.
Once all locked tokens are staked, if the user requested to stake more than the locked token balance,
the collection will then dip into the unlocked balance for the remaining tokens.
If the user has no locked tokens, the staking collection
will simply ignore the locked tokens part of the functionality and only use unlocked tokens.

When a user withdraws tokens from a staking object, the collection
will always try to withdraw unlocked tokens first.
Any unlocked tokens are then deposited directly into the vault on the unlocked account,
and remaining locked tokens are deposited to the vault in the locked account.

## Machine Account Support[​](#machine-account-support "Direct link to Machine Account Support")

The staking collection also supports an important feature for epochs, machine accounts.
Machine accounts are where node operators store important resource objects
that are critical to the functionality of the epoch preparation protocol.
Every collector and consensus node should have an associated machine account that stores these objects,
and the staking collection helps the user create and manage these accounts.

When a user registers a new collector or consensus node,
the staking collection also creates a machine account for them and registers
the required object that needs to go in the machine account.
The node operator is then responsible for adding keys to the account.
(the **Register Node** transaction includes this step).

Once the machine account is created and set up, the node operator just has to
connect it to their node software and make sure the account has enough FLOW
to pay for transaction fees, which can be handled simply by submitting
a regular FLOW transfer to the machine account's address

## Staking Collection Public Getter Methods[​](#staking-collection-public-getter-methods "Direct link to Staking Collection Public Getter Methods")

The staking collection also defines many getter methods to query information
about an account's staking collection. You can simply call one of these methods on the contract,
providing the account address, and the contract will retrieve
the relevant info for you, like so:

`_10

import FlowStakingCollection from 0xSTAKINGCOLLECTIONADDRESS

_10

import FlowIDTableStaking from 0xIDENTITYTABLEADDRESS

_10

_10

/// Gets an array of all the delegator metadata for delegators stored in the staking collection

_10

access(all) fun main(address: Address): [FlowIDTableStaking.DelegatorInfo] {

_10

return FlowStakingCollection.getAllDelegatorInfo(address: address)

_10

}`

Remember: A Staking Collection does not require an account
to have a secondary locked account or locked FLOW.
However, if an account does have an associated locked account, when the Staking Collection is initialized,
it will connect to that locked account's node and delegator objects
as well as it's locked token vault allowing it to perform staking actions with locked and unlocked FLOW.

info

Staking Collection is backwards compatible with other methods of staking on Flow.
Existing accounts with associated locked accounts
will still be able to stake in the same way as before,
but they will also be able to use the staking collection, if desired.

# How to use the Staking Collection

There is a standard set of transactions provided with the staking collection.

## Setup[​](#setup "Direct link to Setup")

### Setup a Staking Collection[​](#setup-a-staking-collection "Direct link to Setup a Staking Collection")

To set up a Staking Collection, you must run the **Setup Staking Collection** ([SCO.01](/build/core-contracts/staking-collection)) transaction.

This transaction requires no arguments and will perform the following actions:

1. Create private capabilities for the unlocked vault and locked vault (if applicable).
2. Create a new staking collection resource object, initializing it with the unlocked and locked vault capabilities.
3. Store the staking collection at a pre-defined storage path.
4. Create a public link to the staking collection so others can query metadata about it.
5. If there are any node or delegator objects in the unlocked account, the transaction stores those in the staking collection
   so they can be used through the same interface as usual.

**No arguments** are required for the **Setup Staking Collection** transaction.

Once this transaction is complete, your existing staking objects (if any) from your unlocked account and locked account
will be available via the staking collection and you can use all the transactions described below to access them.

### Create a Machine Account for an existing Node[​](#create-a-machine-account-for-an-existing-node "Direct link to Create a Machine Account for an existing Node")

Many nodes will have been created before the staking collection was set up and before epochs were enabled,
meaning that they don't already have an associated machine account.
These nodes need a new transaction to create the machine account for the node and save it to the staking collection.

To create a machine account for a node that doesn't already have one,
you must submit the **Create Machine Account** ([SCO.03](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The ID of the node. |
| **publicKeys** | `[String]` | The public keys to add to the machine account. |

If the node is a collector or consensus node, this transaction creates the associated machine account,
registers the QC or DKG object, stores it in the machine account,
and adds the provided public key(s) to the machine account.
If no public keys are provided, the transaction will fail.

## Register Stakers[​](#register-stakers "Direct link to Register Stakers")

### Register a New Staked Node[​](#register-a-new-staked-node "Direct link to Register a New Staked Node")

To register a new staked node, you must submit the **Register Node** ([SCO.03](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **id** | `String` | The ID of the new node. It must be a 32 byte `String`. The operator is free to choose this value, but it must be unique across all nodes. A recommended process to generate this is to hash the staking public key. |
| **role** | `UInt8` | The role of the new node. (1: collection, 2: consensus, 3: execution, 4: verification, 5: access) |
| **networkingAddress** | `String` | The IP address of the new node. |
| **networkingKey** | `String` | The networking public key as a hex-encoded string. |
| **stakingKey** | `String` | The staking public key as a hex-encoded string. |
| **stakingKeyPoP** | `String` | The staking key Proof-of-Possesion as a hex-encoded string. |
| **amount** | `UFix64` | The number of FLOW tokens to stake. |
| **publicKeys** | `[String]?` | The public keys to add to the machine account. `nil` if no machine account |

This transaction registers the account as a staker with the specified node information
and attaches a `NodeStaker` resource to the `Staking Collection`.
This `NodeStaker` resourece can then later be used to perform staking actions via the staking collection staking methods.

If the node is a collector or consensus node, it also creates the associated machine account,
registers the QC or DKG object, stores it in the machine account,
and adds the provided public key(s) to the machine account.
If the node requires a machine account and no public keys are provided, the transaction will fail.

Once the account has registered their node using their Staking Collection,
their tokens and node information are committed to the central staking contract for the next epoch.

At this point, the Staking Collection now has access to various staking operations that they can perform,
assuming they have the correct number of tokens to perform the action.

### Register a New Staked Delegator[​](#register-a-new-staked-delegator "Direct link to Register a New Staked Delegator")

To register a new delegator, you must submit the **Register Delegator** ([SCO.02](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **id** | `String` | The ID of the node to delegate to. |
| **amount** | `UFix64` | The number of FLOW tokens to delegate. |

This transaction registers the account as a delegator to the node identified by the supplied node id.
It also attaches a `NodeDelegator` resource to the `Staking Collection`.
This `NodeDelegator` resourece can then later be used to perform delegation actions.

Once the account has registered their new delegator using their Staking Collection,
their tokens are committed to the central staking contract for the next epoch.

At this point, the Staking Collection now has access to various delegator operations that they can perform,
assuming they have the correct number of tokens to perform the action.

## Staking Operations[​](#staking-operations "Direct link to Staking Operations")

These transactions perform actions that directly interact with the staking contract.
Most of them will only succeed during the Staking Auction phase of the epoch.

### Stake New Tokens[​](#stake-new-tokens "Direct link to Stake New Tokens")

The Staking Collection can stake additional tokens for any Node or Delegator managed by it at any time.

The owner of a Staking Collection can use the **Stake New Tokens** ([SCO.06](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to stake new tokens to. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to stake. |

info

To stake new tokens for an active node, leave the **delegatorID** argument as **nil**.

If staking for a delegator, **delegatorID** should be the delegator ID you are staking for.

The amount may be any number of tokens up to the sum of an accounts locked and unlocked FLOW.

### Re-stake Unstaked Tokens[​](#re-stake-unstaked-tokens "Direct link to Re-stake Unstaked Tokens")

After tokens become unstaked, the owner of a Staking Collection can choose
to re-stake the unstaked tokens to the same Node or Delegator.

The owner of a Staking Collection can use the **Stake Unstaked Tokens** ([SCO.08](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to stake the unstaked tokens to. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to restake. |

info

To stake unstaked tokens for an active node, leave the **delegatorID** argument as **nil**.

If staking for a delegator, **delegatorID** should be the delegator ID you are staking for.

### Re-stake Rewarded Tokens[​](#re-stake-rewarded-tokens "Direct link to Re-stake Rewarded Tokens")

After earning rewards from staking, the owner of a Staking Collection
can choose to re-stake the rewarded tokens to the same node or delegator.

The owner of a Staking Collection can use the **Stake Unstaked Tokens** ([SCO.07](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to stake the rewarded tokens to. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to restake. |

info

To stake rewarded tokens for an active node, leave the **delegatorID** argument as **nil**.

### Request to Unstake Tokens at the end of the Epoch[​](#request-to-unstake-tokens-at-the-end-of-the-epoch "Direct link to Request to Unstake Tokens at the end of the Epoch")

The owner of a Staking Collection can submit a request to unstake their tokens at any time for any Node or Delegator in their collection.

If the tokens aren't staked yet, they will be uncommitted and available to withdraw.

*Note: unstaked tokens will be held by the central staking contract until the end of the following epoch.*
*Once the tokens are released (unstaked), they can be claimed via the [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens) action below.*

The owner of a Staking Collection can use the **Unstake Tokens** ([SCO.05](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the chosen node. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to restake. |

info

To unstake tokens from an active node, leave the **delegatorID** argument as **nil**.

### Unstake All Tokens[​](#unstake-all-tokens "Direct link to Unstake All Tokens")

The owner of a Staking Collection can use the **Unstake All** ([SCO.09](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to unstake all tokens from. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |

### Withdraw Unstaked Tokens[​](#withdraw-unstaked-tokens "Direct link to Withdraw Unstaked Tokens")

After tokens for an active Node or Delegator become unstaked,
the ownder of Staking Collection can withdraw them from the central staking contract.

The owner of a Staking Collection can use the **Withdraw Unstaked Tokens** ([SCO.11](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to withdraw the unstaked tokens from. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to withdraw. |

info

To withdraw unstaked tokens from an active node, leave the **delegatorID** argument as **nil**.

### Withdraw Rewarded Tokens[​](#withdraw-rewarded-tokens "Direct link to Withdraw Rewarded Tokens")

After earning rewards from staking, the token holder can withdraw them from the central staking contract.

The owner of a Staking Collection can use the **Withdraw Rewarded Tokens** ([SCO.10](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to withdraw the rewarded tokens from. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |
| **amount** | `UFix64` | The number of FLOW tokens to withdraw. |

info

To withdraw rewarded tokens from an active node, leave the **delegatorID** argument as **nil**.

## Staking Collection Modification[​](#staking-collection-modification "Direct link to Staking Collection Modification")

### Close a Node or Delegator[​](#close-a-node-or-delegator "Direct link to Close a Node or Delegator")

Once a Node or Delegator has no tokens staked, comitted or in an unstaking state, it is eligible to be closed.

Closing a Node or Delegator first returns any unstaked or rewarded tokens
to the account for which the Staking Collection is stored in.
It then destroys the NodeStaker or NodeDelegator object from within the Staking Collection.

*Note: Once a Node or Delegator has been closed, it cannot be accessed again,*
*and no staking or delegation actions can be further preformed on it.*

The owner of a Staking Collection can use the **Close Stake** ([SCO.12](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to close. |
| **delegatorID** | `Optional(UInt32)` | `nil` if staking for a node. If staking for a delegator, the delegator ID. |

info

To close an active node, leave the **delegatorID** argument as **nil**.

### Transfer a Node[​](#transfer-a-node "Direct link to Transfer a Node")

A user may transfer an existing Node to another another account's Staking Collection.

The account to transfer the Node to must have a valid Staking Collection set up.

Transferring a Node will remove it from the authorizer's Staking Collection
and deposit it to the receiver's Staking Collection.

*Note: Once a Node or Delegator has been transferred, it cannot be accessed again by the sender.*
*As well, all staked tokens will be considered staked by the receiver's Staking Collection.*

warning

Transferring a Node will result in loss of custody of any Staked tokens for the sender.

The owner of a Staking Collection can use the **Transfer Node** ([SCO.13](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to transfer. |
| **to** | `Address` | The address of the account which contains the Staking Collection to transfer the Node to. |

### Transfer a Delegator[​](#transfer-a-delegator "Direct link to Transfer a Delegator")

A user may transfer an existing Delegator to another another account's Staking Collection.

The account to transfer the Delegator to must have a valid Staking Collection set up.

Transferring a Delegator will remove it from the authorizer's Staking Collection
and deposit it to the receiver's Staking Collection.

*Note: Once a Node or Delegator has been transferred, it cannot be accessed again by the sender.*
*As well, all staked tokens will be considered staked by the receiver's Staking Collection.*

warning

Transferring a Delegator will result in loss of custody of any Staked tokens for the sender.

The owner of a Staking Collection can use the **Transfer Delegator** ([SCO.14](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the delegator to transfer. |
| **delegatorID** | `UInt32` | The delegatorID of the delegator to transfer. |
| **to** | `Address` | The address of the account which contains the Staking Collection to transfer the Delegator to. |

### Update A Node's Networking Address[​](#update-a-nodes-networking-address "Direct link to Update A Node's Networking Address")

A user may update their node's networking address if it has become inconsistent with the protocol state.

This operation can only be performed in the staking auction phase of an epoch.

*Note: Currently, if a node updates its networking address and the new address does not match*
*what is stored in the protocol state for the node, the node will not be able to participate in the upcoming epoch*
*Only update your networking address if you have already confirmed with the Flow team that you can.*
*This restriction will be removed once fully automated epochs are completely implemented*

The owner of a Staking Collection can use the **Update Networking Address** ([SCO.22](/build/core-contracts/staking-collection))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The nodeID of the node to update. |
| **newAddress** | `String` | The new networking address |

# Staking Collection Scripts

These scripts allow anyone to query information about an account's staking collection

### Get All Node Info[​](#get-all-node-info "Direct link to Get All Node Info")

To return an array of structs representing the information associated with each node managed by an account's Staking Collection, anyone
can use the **Get All Node Info** ([SCO.15](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns an array of `FlowIDTableStaking.NodeInfo` [structs](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L264)
representing the nodes managed by an accounts Staking Collection.

### Get All Delegator Info[​](#get-all-delegator-info "Direct link to Get All Delegator Info")

To return an array of structs representing the information associated with each delegator managed by an account's Staking Collection, anyone
can use the **Get All Delegator Info** ([SCO.16](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns an array of `FlowIDTableStaking.DelegatorInfo` [structs](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowIDTableStaking.cdc#L264)
representing the delegators managed by an accounts Staking Collection.

### Get All Node Ids[​](#get-all-node-ids "Direct link to Get All Node Ids")

To return an array of Strings representing the ids associated with each node managed by an account's Staking Collection, anyone
can use the **Get All Node Ids** ([SCO.17](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns an array of `String`
representing each id of each node managed by an accounts Staking Collection.

### Get All Delegator Ids[​](#get-all-delegator-ids "Direct link to Get All Delegator Ids")

To return an array of structs representing the delegator ids associated with each delegation managed by an account's Staking Collection, anyone
can use the **Get All Delegator Ids** ([SCO.22](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns an array of `FlowStakingCollection.DelegatorIDs` [structs](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowStakingCollection.cdc#L40)
representing the delegator Ids of each delegator managed by an accounts Staking Collection.

### Get Locked Tokens Used[​](#get-locked-tokens-used "Direct link to Get Locked Tokens Used")

To query how many Locked FLOW tokens an account has staked using their Staking Collection, anyone
can use the **Get Locked Tokens Used** ([SCO.19](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns a `UFix64` representing the number of Locked FLOW tokens staked using an accounts Staking Collection.

info

Note: This number does not include Locked FLOW tokens staked not through an accounts Staking Collection.

### Get Unlocked Tokens Used[​](#get-unlocked-tokens-used "Direct link to Get Unlocked Tokens Used")

To query how many Unlocked FLOW tokens an account has staked using their Staking Collection, anyone
can use the **Get Unlocked Tokens Used** ([SCO.20](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns a `UFix64` representing the number of Unlocked FLOW tokens staked using an accounts Staking Collection.

info

Note: This number does not include Unlocked FLOW tokens staked not through an accounts Staking Collection.

### Get Does Node Exist[​](#get-does-node-exist "Direct link to Get Does Node Exist")

To query if a Node or Delegator is managed by an accounts Staking Collection, anyone
can use the **Get Does Node Exist** ([SCO.21](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |
| **nodeID** | `String` | The nodeID of the node to check, or the nodeID of the node delegating to to check. |
| **delegatorID** | `Optional(UInt32)` | The delegatorID of the delegator to check, if checking for a delegator. |

This script returns a `Bool`.

info

To query if a Node is managed by an accounts Staking Collection, leave the **delegatorID** argument as **nil**.
Otherwise, fill it in with the **delegatorID** of the Delegator.

### Get Machine Account Info[​](#get-machine-account-info "Direct link to Get Machine Account Info")

To query the machine account information for an account's staking collection, anyone
can use the **Get Machine Account Info** ([SCO.21](/build/core-contracts/staking-collection)) script with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **address** | `Addresss` | The Address of the account holding the Staking Collection to query from |

This script returns a `{String: FlowStakingCollection.MachineAccountInfo}`,
which is a mapping of nodeIDs to the `FlowStakingCollection.MachineAccountInfo` struct.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/14-staking-collection.md)

Last updated on **Apr 17, 2025** by **leopardracer**

[Previous

Technical Staking Options](/networks/staking/staking-options)[Next

Basic Staking Guide (Deprecated)](/networks/staking/staking-guide)

###### Rate this page

😞😐😊

* [Staker Object Fields](#staker-object-fields)
* [Vault Capability Fields](#vault-capability-fields)
* [Machine Account Support](#machine-account-support)
* [Staking Collection Public Getter Methods](#staking-collection-public-getter-methods)
* [Setup](#setup)
  + [Setup a Staking Collection](#setup-a-staking-collection)
  + [Create a Machine Account for an existing Node](#create-a-machine-account-for-an-existing-node)
* [Register Stakers](#register-stakers)
  + [Register a New Staked Node](#register-a-new-staked-node)
  + [Register a New Staked Delegator](#register-a-new-staked-delegator)
* [Staking Operations](#staking-operations)
  + [Stake New Tokens](#stake-new-tokens)
  + [Re-stake Unstaked Tokens](#re-stake-unstaked-tokens)
  + [Re-stake Rewarded Tokens](#re-stake-rewarded-tokens)
  + [Request to Unstake Tokens at the end of the Epoch](#request-to-unstake-tokens-at-the-end-of-the-epoch)
  + [Unstake All Tokens](#unstake-all-tokens)
  + [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens)
  + [Withdraw Rewarded Tokens](#withdraw-rewarded-tokens)
* [Staking Collection Modification](#staking-collection-modification)
  + [Close a Node or Delegator](#close-a-node-or-delegator)
  + [Transfer a Node](#transfer-a-node)
  + [Transfer a Delegator](#transfer-a-delegator)
  + [Update A Node's Networking Address](#update-a-nodes-networking-address)
  + [Get All Node Info](#get-all-node-info)
  + [Get All Delegator Info](#get-all-delegator-info)
  + [Get All Node Ids](#get-all-node-ids)
  + [Get All Delegator Ids](#get-all-delegator-ids)
  + [Get Locked Tokens Used](#get-locked-tokens-used)
  + [Get Unlocked Tokens Used](#get-unlocked-tokens-used)
  + [Get Does Node Exist](#get-does-node-exist)
  + [Get Machine Account Info](#get-machine-account-info)

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