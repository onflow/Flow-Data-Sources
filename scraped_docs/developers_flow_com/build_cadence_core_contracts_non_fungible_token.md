# Source: https://developers.flow.com/build/cadence/core-contracts/non-fungible-token

Non-Fungible Token Contract | Flow Developer Portal



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
  + [Guides](/build/cadence/guides/account-linking)
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
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
  + [Guides](/build/evm/guides)
* [Tools & SDKs](/build/tools)

* Cadence
* [Core Smart Contracts](/build/cadence/core-contracts)
* Non-Fungible Token

On this page

The `NonFungibleToken` contract interface implements the Fungible Token Standard.
All NFT contracts are encouraged to import and implement this standard.

* [Basic Non-Fungible Token Tutorial](https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1)
* [Non Fungible Token Guide](/build/cadence/guides/nft)
* [Non Fungible Token Standard Repo](https://github.com/onflow/flow-nft)

Source: [NonFungibleToken.cdc](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x631e88ae7f1d7c20` |
| Mainnet | `0x1d7e57aa55817448` |

# Transactions

All `NonFungibleToken` projects are encouraged to use
the generic token transactions and scripts in the `flow-nft` [repo](https://github.com/onflow/flow-nft/tree/master/transactions).
They can be used for any token that implements the non-fungible token standard properly
without changing any code besides import addresses on different networks.

# Events

Events emitted from all contracts follow a standard format:

`_10

A.{contract address}.{contract name}.{event name}`

The components of the format are:

* `contract address` - the address of the account the contract has been deployed to
* `contract name` - the name of the contract in the source code
* `event name` - the name of the event as declared in the source code

## NonFungibleToken Events[​](#nonfungibletoken-events "Direct link to NonFungibleToken Events")

Contracts that implement the Non-Fungible Token standard get access
to standard events that are emitted every time a relevant action occurs,
like depositing and withdrawing tokens.

This means that projects do not have to implement their own custom events
unless the standard events do not satisfy requirements they have for events.

The `NonFungibleToken` events will have the following format:

`_10

A.{contract address}.NonFungibleToken.Deposited

_10

A.{contract address}.NonFungibleToken.Withdrawn`

Where the `contract address` is the `NonFungibleToken` address on the network being queried.
The addresses on the various networks are shown above.

### NonFungibleToken.Deposited[​](#nonfungibletokendeposited "Direct link to NonFungibleToken.Deposited")

`_10

access(all) event Deposited (

_10

type: String,

_10

id: UInt64,

_10

uuid: UInt64,

_10

to: Address?,

_10

collectionUUID: UInt64

_10

)`

Whenever `deposit()` is called on a resource type that implements
`NonFungibleToken.Collection`, the `NonFungibleToken.Deposited` event is emitted
with the following arguments:

* `type: String`: The type identifier of the token being deposited.
  + Example: `A.4445e7ad11568276.TopShot.NFT`
* `id: UInt64`: The ID of the token that was deposited. Note: This may or may not be the UUID.
  + Example: `173838`
* `uuid: UInt64`: The UUID of the token that was deposited.
  + Example: `177021372071991`
* `to: Address?`: The address of the account that owns the Collection that received
  the token. If the collection is not stored in an account, `to` will be `nil`.
  + Example: `0x4445e7ad11568276`
* `collectionUUID: UInt64`: The UUID of the Collection that received the token.
  + Example: `177021372071991`

### NonFungibleToken.Withdrawn[​](#nonfungibletokenwithdrawn "Direct link to NonFungibleToken.Withdrawn")

`_10

access(all) event Withdrawn (

_10

type: String,

_10

id: UInt64,

_10

uuid: UInt64,

_10

from: Address?,

_10

providerUUID: UInt64

_10

)`

Whenever `withdraw()` is called on a resource type that implements
`NonFungibleToken.Collection`, the `NonFungibleToken.Withdrawn` event is emitted
with the following arguments:

* `type: String`: The type identifier of the token being withdrawn.
  + Example: `A.4445e7ad11568276.TopShot.NFT`
* `id: UInt64`: The id of the token that was withdrawn. Note: May or may not be the UUID.
  + Example: `113838`
* `uuid: UInt64`: The UUID of the token that was withdrawn.
  + Example: `177021372071991`
* `from: Address?`: The address of the account that owns the Collection that
  the token was withdrawn from. If the collection is not stored in an account, `to` will be `nil`.
  + Example: `0x4445e7ad11568276`
* `providerUUID: UInt64`: The UUID of the Collection that the token was withdrawn from.
  + Example: `177021372071991`

### NonFungibleToken.Updated[​](#nonfungibletokenupdated "Direct link to NonFungibleToken.Updated")

`_10

access(all) event Updated(

_10

type: String,

_10

id: UInt64,

_10

uuid: UInt64,

_10

owner: Address?

_10

)`

Whenever a non-fungible token is updated for whatever reason,
projects should call the `NonFungibleToken.emitNFTUpdated()` function
to emit this event. It indicates to event listeners that they should query
the NFT to update any stored information they have about the NFT in their database.

* `type: String`: The type identifier of the token that was updated.
  + Example: `A.4445e7ad11568276.TopShot.NFT`
* `id: UInt64`: The ID of the token that was updated. Note: This may or may not be the UUID.
  + Example: `173838`
* `uuid: UInt64`: The UUID of the token that was updated.
  + Example: `177021372071991`
* `owner: Address?`: The address of the account that owns the Collection that owns
  the token. If the collection is not stored in an account, `to` will be `nil`.
  + Example: `0x4445e7ad11568276`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/08-non-fungible-token.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)[Next

NFT Metadata](/build/cadence/core-contracts/nft-metadata)

###### Rate this page

😞😐😊

Copy as Markdown

* [NonFungibleToken Events](#nonfungibletoken-events)
  + [NonFungibleToken.Deposited](#nonfungibletokendeposited)
  + [NonFungibleToken.Withdrawn](#nonfungibletokenwithdrawn)
  + [NonFungibleToken.Updated](#nonfungibletokenupdated)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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
* [EVM](/build/evm/about)

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