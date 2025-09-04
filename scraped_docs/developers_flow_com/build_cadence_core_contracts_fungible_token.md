# Source: https://developers.flow.com/build/cadence/core-contracts/fungible-token

Fungible Token Contract | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)

    - [Fungible Token](/build/cadence/core-contracts/fungible-token)
    - [Flow Token](/build/cadence/core-contracts/flow-token)
    - [Service Account](/build/cadence/core-contracts/service-account)
    - [Flow Fees](/build/cadence/core-contracts/flow-fees)
    - [Staking Table](/build/cadence/core-contracts/staking-contract-reference)
    - [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)
    - [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)
    - [NFT Metadata](/build/cadence/core-contracts/nft-metadata)
    - [NFT Storefront](/build/cadence/core-contracts/nft-storefront)
    - [Staking Collection](/build/cadence/core-contracts/staking-collection)
    - [Account Linking](/build/cadence/core-contracts/hybrid-custody)
    - [EVM](/build/cadence/core-contracts/evm)
    - [Burner](/build/cadence/core-contracts/burner)
    - [VM Bridge](/build/cadence/core-contracts/bridge)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

* Cadence
* [Core Smart Contracts](/build/cadence/core-contracts)
* Fungible Token

On this page

The `FungibleToken` contract implements the Fungible Token Standard. It is the second contract ever deployed on Flow.

* [Basic Fungible Token Tutorial](https://cadence-lang.org/docs/tutorial/fungible-tokens)
* [Fungible Token Guide](/blockchain-development-tutorials/tokens/fungible-token-cadence)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/02-fungible-token.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Core Smart Contracts](/build/cadence/core-contracts)[Next

Flow Token](/build/cadence/core-contracts/flow-token)

###### Rate this page

😞😐😊

Copy as Markdown

* [FungibleToken Events](#fungibletoken-events)
  + [FungibleToken.Deposited](#fungibletokendeposited)
  + [FungibleToken.Withdrawn](#fungibletokenwithdrawn)
  + [FungibleToken.Burned](#fungibletokenburned)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.