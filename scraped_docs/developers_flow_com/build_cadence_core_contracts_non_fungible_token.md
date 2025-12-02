# Source: https://developers.flow.com/build/cadence/core-contracts/non-fungible-token

Non-Fungible Token Contract | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)

                - [Fungible Token](/build/cadence/core-contracts/fungible-token)- [Flow Token](/build/cadence/core-contracts/flow-token)- [Service Account](/build/cadence/core-contracts/service-account)- [Flow Fees](/build/cadence/core-contracts/flow-fees)- [Staking Table](/build/cadence/core-contracts/staking-contract-reference)- [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)- [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)- [NFT Metadata](/build/cadence/core-contracts/nft-metadata)- [NFT Storefront](/build/cadence/core-contracts/nft-storefront)- [Staking Collection](/build/cadence/core-contracts/staking-collection)- [Account Linking](/build/cadence/core-contracts/hybrid-custody)- [EVM](/build/cadence/core-contracts/evm)- [Burner](/build/cadence/core-contracts/burner)- [VM Bridge](/build/cadence/core-contracts/bridge)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* [Core Smart Contracts](/build/cadence/core-contracts)* Non-Fungible Token

On this page

The `NonFungibleToken` contract interface implements the Fungible Token Standard.
All NFT contracts are encouraged to import and implement this standard.

* [Basic Non-Fungible Token Tutorial](https://cadence-lang.org/docs/tutorial/non-fungible-tokens-1)
* [Non Fungible Token Guide](/blockchain-development-tutorials/tokens/nft-cadence)
* [Non Fungible Token Standard Repo](https://github.com/onflow/flow-nft)

Source: [NonFungibleToken.cdc](https://github.com/onflow/flow-nft/blob/master/contracts/NonFungibleToken.cdc)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Contract Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Emulator `0xf8d6e0586b0a20c7`| Cadence Testing Framework `0x0000000000000001`| Testnet `0x631e88ae7f1d7c20`| Mainnet `0x1d7e57aa55817448` | | | | | | | | | |

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

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)[Next

NFT Metadata](/build/cadence/core-contracts/nft-metadata)

###### Rate this page

😞😐😊

Copy as Markdown

* [NonFungibleToken Events](#nonfungibletoken-events)
  + [NonFungibleToken.Deposited](#nonfungibletokendeposited)+ [NonFungibleToken.Withdrawn](#nonfungibletokenwithdrawn)+ [NonFungibleToken.Updated](#nonfungibletokenupdated)

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

Copyright © 2025 Flow Foundation. All Rights Reserved.