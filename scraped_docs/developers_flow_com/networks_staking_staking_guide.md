# Source: https://developers.flow.com/networks/staking/staking-guide




Basic Staking with FLOW | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Basic Staking Guide (Deprecated)
On this page

This document outlines the steps a token holder can take to stake and manage
a Flow node with FLOW using only the types defined in the `FlowIDTableStaking` contract.
It only supports having one node or delegator object per account and is not supported by ledger
and will likely not be supported by other wallets, so it is recommended to use the staking collection
instead.

warning

This guide covers staking with **FLOW tokens**.


# Staking

## Setup[​](#setup "Direct link to Setup")

### Register a New Staked Node[​](#register-a-new-staked-node "Direct link to Register a New Staked Node")

To register as a node operator with FLOW, the token holder can use the **Register Node** ([SC.11](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **id** | `String` | The ID of the new node. It must be a 32 byte `String`. The operator is free to choose this value, but it must be unique across all nodes. A recommended process to generate this is to hash the staking public key. |
| **role** | `UInt8` | The role of the new node. (1: collection, 2: consensus, 3: execution, 4: verification, 5: access) |
| **networkingAddress** | `String` | The IP address of the new node. (Length must be less than 255 bytes (510 Hex characters)) |
| **networkingKey** | `String` | The networking public key as a 64 byte hex-encoded `String` (128 hex characters) |
| **stakingKey** | `String` | The staking public key as a 96 byte hex-encoded `String` (192 hex characters) |
| **amount** | `UFix64` | The number of FLOW tokens to stake. |

This transaction registers the account as a node operator with the specified node information
and creates a public link to query the nodes ID from the account address.

---

Once the token holder has registered their node,
their tokens and node information are committed to the central staking contract for the next epoch.

At this point, the token holder now has access to various staking operations that they can perform,
assuming they have the correct number of tokens to perform the action.

## Stake Tokens[​](#stake-tokens "Direct link to Stake Tokens")

The token holder can stake additional tokens at any time.

*Note: this transaction stakes additional tokens to the same node that was registered in the setup phase.*

To stake tokens, the token holder can use the **Stake FLOW** ([SC.12](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of FLOW tokens to stake. |

This transaction commits tokens to stake from the token holder's account.

## Re-stake Unstaked Tokens[​](#re-stake-unstaked-tokens "Direct link to Re-stake Unstaked Tokens")

After tokens become unstaked, the token holder can choose to re-stake the unstaked tokens to the same node.

To staked unstaked tokens, the token holder can use the **Re-stake Unstaked FLOW** ([SC.13](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of unstaked FLOW tokens to stake. |

## Re-stake Rewarded Tokens[​](#re-stake-rewarded-tokens "Direct link to Re-stake Rewarded Tokens")

After earning rewards from staking, the token holder can choose to re-stake the rewarded tokens to the same node.

To stake rewarded tokens, the token holder can use the **Re-stake Rewarded FLOW** ([SC.14](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of rewarded FLOW tokens to stake. |

## Request Unstake Tokens[​](#request-unstake-tokens "Direct link to Request Unstake Tokens")

The token holder can submit a request to unstake some of their tokens at any time.
If the tokens aren't staked yet, they will be uncommitted and available to withdraw.

To request to unstake staked tokens, the token holder can use
the **Request Unstaking** ([SC.15](/build/core-contracts/staking-contract-reference#staking)) transaction.

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of rewarded FLOW tokens to request to un-stake. |

*Note: this transaction will not succeed if the node operator has delegators and the request
would put the node operator below the minimum required tokens staked for their node type.
Use the `Unstake All` transaction instead, which will also unstake all delegators.*

*Note: unstaked tokens will be held by the central staking contract until the end of the following epoch.
Once the tokens are released (unstaked), they can be claimed via the
[Withdraw Unstaked Tokens](#withdraw-unstaked-tokens) action below.*

## Unstake All Tokens[​](#unstake-all-tokens "Direct link to Unstake All Tokens")

The token holder can submit a request to unstake all their tokens at any time.
If the tokens aren't staked yet, they will be uncommitted and available to withdraw.

To unstake all staked tokens, the token holder can use
the **Unstake All FLOW** ([SC.16](/build/core-contracts/staking-contract-reference#staking)) transaction.

This transaction requires no arguments.

**Warning: this will unstake all of the user's staked tokens and unstake all of the tokens
from users that are delegating FLOW to the node.**

## Withdraw Unstaked Tokens[​](#withdraw-unstaked-tokens "Direct link to Withdraw Unstaked Tokens")

After tokens become unstaked, the token holder can withdraw them from the central staking contract.

To withdraw unstaked tokens,
the token holder can use the **Withdraw Unstaked FLOW** ([SC.17](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of unstaked FLOW tokens to withdraw. |

This transaction moves the unstaked tokens back into the `FlowToken.Vault` owned by the token holder.

## Withdraw Rewarded Tokens[​](#withdraw-rewarded-tokens "Direct link to Withdraw Rewarded Tokens")

After earning rewards from staking, the token holder can withdraw them from the central staking contract.

To withdraw rewarded tokens,
the token holder can use the **Withdraw Rewarded FLOW** ([SC.18](/build/core-contracts/staking-contract-reference#staking))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of rewarded FLOW tokens to withdraw. |

This transaction moves the rewarded tokens back into the `FlowToken.Vault` owned by the token holder.

## Stake Multiple Nodes from the Same Account[​](#stake-multiple-nodes-from-the-same-account "Direct link to Stake Multiple Nodes from the Same Account")

Currently, the default staking transactions can only be used as they are to stake one node per account.

If a token holder wants to create a second staking relationship using the transactions as is, they must create a new account
and transfer their tokens to the new account.

It is possible to have multiple nodes per account by storing the node objects at different storage paths,
but this would require small changes to these transactions to use the new storage paths.

# Delegating

## Setup[​](#setup-1 "Direct link to Setup")

## Register as a Delegator[​](#register-as-a-delegator "Direct link to Register as a Delegator")

To register as a delegator, the token holder can use the **Register Delegator** ([SC.19](/build/core-contracts/staking-contract-reference#delegating))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **id** | `String` | The ID of the node to delegate to. |
| **amount** | `UFix64` | The number of FLOW tokens to delegate. |

This transaction registers the account as a delegator to the node ID they specified.

---

## Delegate New Tokens[​](#delegate-new-tokens "Direct link to Delegate New Tokens")

The token holder can delegate additional tokens after registering as a delegator.

*Note: this transaction delegates additional tokens to the same node that was registered in the setup phase.*

To delegate new tokens,
the token holder can use the **Delegate New FLOW** ([SC.20](/build/core-contracts/staking-contract-reference#delegating))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of FLOW tokens to delegate. |

## Re-delegate Unstaked Tokens[​](#re-delegate-unstaked-tokens "Direct link to Re-delegate Unstaked Tokens")

After delegated tokens become unstaked, the token holder can choose to re-delegate the unstaked tokens to the same node.

To delegate unstaked tokens,
the token holder can use the **Re-delegate Unstaked FLOW** ([SC.21](/build/core-contracts/staking-contract-reference#delegating))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of unstaked FLOW tokens to delegate. |

## Re-delegate Rewarded Tokens[​](#re-delegate-rewarded-tokens "Direct link to Re-delegate Rewarded Tokens")

After earning rewards from delegation, the token holder can choose to re-delegate the rewarded tokens to the same node.

To delegate rewarded tokens,
the token holder can use the **Re-delegate Rewarded FLOW** ([SC.22](/build/core-contracts/staking-contract-reference#delegating))
| Argument | Type | Description |
| **amount** | `UFix64` | The number of rewarded FLOW tokens to delegate. |

## Unstake Delegated Tokens[​](#unstake-delegated-tokens "Direct link to Unstake Delegated Tokens")

The token holder can submit a request to unstake their delegated tokens at any time.
If the tokens aren't staked yet, they will be uncommitted and available to withdraw.

To unstake delegated tokens,
the token holder can use the **Unstake Delegated FOW** ([SC.23](/build/core-contracts/staking-contract-reference#delegating))

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of FLOW tokens to unstake. |

*Note: unstaked delegated tokens will be held by the central staking contract for a period of time
(the rest of the current epoch plus all of the next epoch) before they are
released to the token holder. Once the tokens are released (unstaked),
they can be claimed via the [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens) action below.*

## Withdraw Unstaked Tokens[​](#withdraw-unstaked-tokens-1 "Direct link to Withdraw Unstaked Tokens")

After delegated tokens become unstaked, the token holder can withdraw them from the central staking contract.

To withdraw unstaked tokens,
the token holder can use the **Withdraw Unstaked FLOW** ([SC.24](/build/core-contracts/staking-contract-reference#delegating))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of unstaked FLOW tokens to withdraw. |

This transaction moves the unstaked tokens back into the `FlowToken.Vault` owned by the token holder.

## Withdraw Rewarded Tokens[​](#withdraw-rewarded-tokens-1 "Direct link to Withdraw Rewarded Tokens")

After earning rewards from delegation, the token holder can withdraw them from the central staking contract.

To withdraw rewarded tokens,
the token holder can use the **Withdraw Rewarded FLOW** ([SC.25](/build/core-contracts/staking-contract-reference#delegating))
transaction with the following arguments:

| Argument | Type | Description |
| --- | --- | --- |
| **amount** | `UFix64` | The number of rewarded FLOW tokens to withdraw. |

This transaction moves the rewarded tokens back into the `FlowToken.Vault` owned by the token holder.

## Delegate to Multiple Nodes from the Same Account[​](#delegate-to-multiple-nodes-from-the-same-account "Direct link to Delegate to Multiple Nodes from the Same Account")

Currently, the default delegating transactions can only be used as they are to stake one node per account.

If a token holder wants to create a second delegating relationship using the transactions as is, they must create a new account
and transfer their tokens to the new account.

It is possible to have multiple delegator objects per account
by storing the node objects at different storage paths,
but this would require small changes to these transactions to use the new storage paths.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/15-staking-guide.md)Last updated on **Jan 7, 2025** by **Chase Fleming**[PreviousStaking Collection Guide](/networks/staking/staking-collection)[NextNode Operations](/networks/node-ops)
###### Rate this page

😞😐😊

* [Setup](#setup)
  + [Register a New Staked Node](#register-a-new-staked-node)
* [Stake Tokens](#stake-tokens)
* [Re-stake Unstaked Tokens](#re-stake-unstaked-tokens)
* [Re-stake Rewarded Tokens](#re-stake-rewarded-tokens)
* [Request Unstake Tokens](#request-unstake-tokens)
* [Unstake All Tokens](#unstake-all-tokens)
* [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens)
* [Withdraw Rewarded Tokens](#withdraw-rewarded-tokens)
* [Stake Multiple Nodes from the Same Account](#stake-multiple-nodes-from-the-same-account)
* [Setup](#setup-1)
* [Register as a Delegator](#register-as-a-delegator)
* [Delegate New Tokens](#delegate-new-tokens)
* [Re-delegate Unstaked Tokens](#re-delegate-unstaked-tokens)
* [Re-delegate Rewarded Tokens](#re-delegate-rewarded-tokens)
* [Unstake Delegated Tokens](#unstake-delegated-tokens)
* [Withdraw Unstaked Tokens](#withdraw-unstaked-tokens-1)
* [Withdraw Rewarded Tokens](#withdraw-rewarded-tokens-1)
* [Delegate to Multiple Nodes from the Same Account](#delegate-to-multiple-nodes-from-the-same-account)
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

