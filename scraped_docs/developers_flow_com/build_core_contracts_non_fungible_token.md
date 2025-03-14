# Source: https://developers.flow.com/build/core-contracts/non-fungible-token

Non-Fungible Token Contract | Flow Developer Portal



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
* Non-Fungible Token

On this page

The `NonFungibleToken` contract interface implements the Fungible Token Standard.
All NFT contracts are encouraged to import and implement this standard.

* [Basic Non-Fungible Token Tutorial](https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1)
* [Non Fungible Token Guide](/build/guides/nft)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/08-non-fungible-token.md)

Last updated on **Feb 27, 2025** by **Vishal**

[Previous

Epoch Contracts](/build/core-contracts/epoch-contract-reference)[Next

NFT Metadata](/build/core-contracts/nft-metadata)

###### Rate this page

😞😐😊

* [NonFungibleToken Events](#nonfungibletoken-events)
  + [NonFungibleToken.Deposited](#nonfungibletokendeposited)
  + [NonFungibleToken.Withdrawn](#nonfungibletokenwithdrawn)
  + [NonFungibleToken.Updated](#nonfungibletokenupdated)

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