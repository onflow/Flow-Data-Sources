# Source: https://developers.flow.com/build/core-contracts/fungible-token

Fungible Token Contract | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
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
* [Explore More](/build/explore-more)

* [Core Smart Contracts](/build/core-contracts)
* Fungible Token

On this page

The `FungibleToken` contract implements the Fungible Token Standard. It is the second contract ever deployed on Flow.

* [Basic Fungible Token Tutorial](https://cadence-lang.org/docs/tutorial/fungible-tokens)
* [Fungible Token Guide](/build/guides/fungible-token)
* [Fungible Token Standard Repo](https://github.com/onflow/flow-ft)

The `FungibleTokenMetadataViews` and `FungibleTokenSwitchboard` contracts
are also deployed to the same account as `FungibleToken`.

Source: [FungibleToken.cdc](https://github.com/onflow/flow-ft/blob/master/contracts/FungibleToken.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xee82856bf20e2aa6` |
| Cadence Testing Framework | `0x0000000000000002` |
| Testnet | `0x9a0766d93b6608b7` |
| Mainnet | `0xf233dcee88fe0abe` |

# Transactions

All `FungibleToken` projects are encouraged to use
the generic token transactions and scripts in the `flow-ft` [repo](https://github.com/onflow/flow-ft/tree/master/transactions).
They can be used for any token that implements the fungible token standard properly
without changing any code besides import addresses on different networks.

# Events

Events emitted from all contracts follow a standard format:

`_10

A.{contract address}.{contract name}.{event name}`

The components of the format are:

* `contract address` - the address of the account the contract has been deployed to
* `contract name` - the name of the contract in the source code
* `event name` - the name of the event as declared in the source code

## FungibleToken Events[​](#fungibletoken-events "Direct link to FungibleToken Events")

Contracts that implement the Fungible Token standard get access
to standard events that are emitted every time a relevant action occurs,
like depositing and withdrawing tokens.

This means that projects do not have to implement their own custom events
unless the standard events do not satisfy requirements they have for events.

The `FungibleToken` events will have the following format:

`_10

A.{contract address}.FungibleToken.Deposited

_10

A.{contract address}.FungibleToken.Withdrawn`

Where the `contract address` is the `FungibleToken` address on the network being queried.
The addresses on the various networks are shown above.

### FungibleToken.Deposited[​](#fungibletokendeposited "Direct link to FungibleToken.Deposited")

`_10

access(all) event Deposited (

_10

type: String,

_10

amount: UFix64,

_10

to: Address?,

_10

toUUID: UInt64,

_10

depositedUUID: UInt64,

_10

balanceAfter: UFix64

_10

)`

Whenever `deposit()` is called on a resource type that implements
`FungibleToken.Vault`, the `FungibleToken.Deposited` event is emitted
with the following arguments:

* `type: String`: The type identifier of the token being deposited.
  + Example: `A.4445e7ad11568276.FlowToken.Vault`
* `amount: UFix64`: The amount of tokens that were deposited.
  + Example: `0.00017485`
* `to: Address?`: The address of the account that owns the Vault that received
  the tokens. If the vault is not stored in an account, `to` will be `nil`.
  + Example: `0x4445e7ad11568276`
* `toUUID: UInt64`: The UUID of the Vault that received the tokens.
  + Example: `177021372071991`
* `depositedUUID`: The UUID of the Vault that was deposited (and therefore destroyed).
  + Example: `177021372071991`
* `balanceAfter: UFix64`: The balance of the Vault that received the tokens after the deposit happened.
  + Example: `1.00047545`

### FungibleToken.Withdrawn[​](#fungibletokenwithdrawn "Direct link to FungibleToken.Withdrawn")

`_10

access(all) event Withdrawn (

_10

type: String,

_10

amount: UFix64,

_10

from: Address?,

_10

fromUUID: UInt64,

_10

withdrawnUUID: UInt64,

_10

balanceAfter: UFix64

_10

)`

Whenever `withdraw()` is called on a resource type that implements
`FungibleToken.Vault`, the `FungibleToken.Withdrawn` event is emitted
with the following arguments:

* `type: String`: The type identifier of the token being withdrawn.
  + Example: `A.4445e7ad11568276.FlowToken.Vault`
* `amount: UFix64`: The amount of tokens that were withdrawn.
  + Example: `0.00017485`
* `from: Address?`: The address of the account that owns the Vault that the tokens
  were withdrawn from. If the vault is not stored in an account, `to` will be `nil`.
  + Example: `0x4445e7ad11568276`
* `fromUUID: UInt64`: The UUID of the Vault that the tokens were withdrawn from.
  + Example: `177021372071991`
* `withdrawnUUID`: The UUID of the Vault that was withdrawn.
  + Example: `177021372071991`
* `balanceAfter: UFix64`: The balance of the Vault that the tokens
  were withdrawn from after the withdrawal.
  + Example: `1.00047545`

### FungibleToken.Burned[​](#fungibletokenburned "Direct link to FungibleToken.Burned")

`_10

access(all) event Burned (

_10

type: String,

_10

amount: UFix64,

_10

fromUUID: UInt64

_10

)`

Whenever a fungible token that implements `FungibleToken.Vault` is burned
via the `Burner.burn()` method, this event is emitted with the following arguments:

* `type: String`: The type identifier of the token that was burnt.
  + Example: `A.4445e7ad11568276.FlowToken.Vault`
* `amount: UFix64`: The amount of tokens that were burnt.
  + Example: `0.00017485`
* `fromUUID: UInt64`: The UUID of the Vault that was burnt.
  + Example: `177021372071991`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/02-fungible-token.md)

Last updated on **Feb 25, 2025** by **Chase Fleming**

[Previous

Core Smart Contracts](/build/core-contracts)[Next

Flow Token](/build/core-contracts/flow-token)

###### Rate this page

😞😐😊

* [FungibleToken Events](#fungibletoken-events)
  + [FungibleToken.Deposited](#fungibletokendeposited)
  + [FungibleToken.Withdrawn](#fungibletokenwithdrawn)
  + [FungibleToken.Burned](#fungibletokenburned)

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