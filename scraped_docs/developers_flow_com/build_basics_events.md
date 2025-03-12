# Source: https://developers.flow.com/build/basics/events

Events | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)

  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [MEV Resistance](/build/basics/mev-resistance)
  + [Events](/build/basics/events)
  + [FLOW Coin](/build/basics/flow-token)
  + [Smart Contracts ↙](/build/basics/smart-contracts)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Flow Protocol
* Events

On this page

# Events

Flow events are special values that are emitted on the network during the execution of a Cadence program and can be observed by off-chain observers.

Events are defined as Cadence code and you should [read Cadence documentation](https://cadence-lang.org/docs/language/events) to understand how to define them.

Since transactions don't have return values you can leverage events to broadcast certain changes the transaction caused. Clients listening on Flow networks (apps) can listen to these events being emitted and react.

![Screenshot 2023-08-18 at 14.09.33.png](/assets/images/Screenshot_2023-08-18_at_14.09.33-5a94d1214f7016737c79587c24373313.png)

There are two types of events emitted on the Flow network:

* Core events
* User-defined events

Events consist of the **event name** and an optional **payload**.

![Screenshot 2023-08-18 at 13.59.01.png](/assets/images/Screenshot_2023-08-18_at_13.59.01-8d9f5c4cb0bfebd04b3e864a34bdc79b.png)

## Core Events[​](#core-events "Direct link to Core Events")

Core events are events emitted directly from the FVM (Flow Virtual Machine). The events have the same name on all networks and do not follow the same naming as user-defined events (they have no address).

A list of events that are emitted by the Flow network is:

| Event Name | Description |
| --- | --- |
| flow.AccountCreated | Event that is emitted when a new account gets created. |
| flow.AccountKeyAdded | Event that is emitted when a key gets added to an account. |
| flow.AccountKeyRemoved | Event that is emitted when a key gets removed from an account. |
| flow.AccountContractAdded | Event that is emitted when a contract gets deployed to an account. |
| flow.AccountContractUpdated | Event that is emitted when a contract gets updated on an account. |
| flow.AccountContractRemoved | Event that is emitted when a contract gets removed from an account. |
| flow.InboxValuePublished | Event that is emitted when a Capability is published from an account. |
| flow.InboxValueUnpublished | Event that is emitted when a Capability is unpublished from an account. |
| flow.InboxValueClaimed1 | Event that is emitted when a Capability is claimed by an account. |

For more details [on the core events, you can read Cadence reference documentation](https://cadence-lang.org/docs/language/core-events).

## User-defined events[​](#user-defined-events "Direct link to User-defined events")

Events that are defined inside contracts and when emitted follow a common naming schema. The schema consists of 4 parts:

`_10

A.{contract address}.{contract name}.{event type}`

An example event would look like:

![Screenshot 2023-08-18 at 14.30.36.png](/assets/images/Screenshot_2023-08-18_at_14.30.36-b0570852e01e8ef1d9b340c5cc162c3e.png)

The first `A` means the event is originating from a contract, which will always be the case for user-defined events. The contract address as the name implies is the location of a contract deployed on the Flow network. Next, is the name of the contracted event originates from, and last is the event type defined in the contract.

There is an unlimited amount of events that can be defined on Flow, but you should know about the most common ones.

### Fungible Token Events[​](#fungible-token-events "Direct link to Fungible Token Events")

All fungible token contracts, including [The FLOW Token contract](/build/core-contracts/flow-token),
use the [fungible token standard on Flow](/build/core-contracts/fungible-token).
As with any contract, the standard emits events when interacted with.
When any fungible token is transferred, standard events are emitted.
You can find a lot of details on the events emitted in the [Fungible Token documentation](/build/core-contracts/fungible-token).

The most common events are when tokens are transferred which is accomplished with two actions: withdrawing tokens from the payer and depositing tokens in the receiver. Each of those actions has a corresponding event:

**Withdraw Tokens**

Event name: `FungibleToken.Withdrawn`

`_10

event Withdrawn(type: String,

_10

amount: UFix64,

_10

from: Address?,

_10

fromUUID: UInt64,

_10

withdrawnUUID: UInt64,

_10

balanceAfter: UFix64)`

Mainnet event: `A.f233dcee88fe0abe.FungibleToken.Withdrawn`

Testnet event: `A.9a0766d93b6608b7.FungibleToken.Withdrawn`

**Deposit Tokens**

`_10

event Deposited(type: String,

_10

amount: UFix64,

_10

to: Address?,

_10

toUUID: UInt64,

_10

depositedUUID: UInt64,

_10

balanceAfter: UFix64)`

Event name: `FungibleToken.Deposited`

Mainnet event: `A.f233dcee88fe0abe.FungibleToken.Deposited`

Testnet event: `A.9a0766d93b6608b7.FungibleToken.Deposited`

### **Fee Events**[​](#fee-events "Direct link to fee-events")

Since fees are governed by a contract deployed on the Flow network, that contract also emits events when fees are deducted.

Charging fees consists of a couple of steps:

* Calculate and deduct fees
* Withdraw Flow tokens from the payer account
* Deposit Flow tokens to the fees contract

These events are very common since they accommodate all transactions on Flow. Each fee deduction will result in three events: the withdrawal of Flow tokens, the deposit of Flow tokens, and the fee deduction.

An example of fee events:

`_24

Events:

_24

- Index: 0

_24

Type: A.f233dcee88fe0abe.FungibleToken.Withdrawn

_24

Tx ID: 1ec90051e3bc74fc36cbd16fc83df08e463dda8f92e8e2193e061f9d41b2ad92

_24

Values:

_24

- type (String): "1654653399040a61.FlowToken.Vault"

_24

- amount (UFix64): 0.00000100

_24

- from (Address?): b30eb2755dca4572

_24

_24

- Index: 1

_24

Type: A.f233dcee88fe0abe.FungibleToken.Deposited

_24

Tx ID: 1ec90051e3bc74fc36cbd16fc83df08e463dda8f92e8e2193e061f9d41b2ad92

_24

Values:

_24

- type (String): "1654653399040a61.FlowToken.Vault"

_24

- amount (UFix64): 0.00000100

_24

- to (Address?): f919ee77447b7497

_24

_24

- Index: 2

_24

Type: A.f919ee77447b7497.FlowFees.FeesDeducted

_24

Tx ID: 1ec90051e3bc74fc36cbd16fc83df08e463dda8f92e8e2193e061f9d41b2ad92

_24

Values:

_24

- amount (UFix64): 0.00000100

_24

- inclusionEffort (UFix64): 1.00000000

_24

- executionEffort (UFix64): 0.00000000`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/events.md)

Last updated on **Feb 27, 2025** by **Chase Fleming**

[Previous

MEV Resistance](/build/basics/mev-resistance)[Next

FLOW Coin](/build/basics/flow-token)

###### Rate this page

😞😐😊

* [Core Events](#core-events)
* [User-defined events](#user-defined-events)
  + [Fungible Token Events](#fungible-token-events)
  + [**Fee Events**](#fee-events)

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