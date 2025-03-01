# Source: https://developers.flow.com/build/core-contracts/flow-token

Flow Token Contract | Flow Developer Portal



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
* Flow Token

On this page

The `FlowToken` contract defines the FLOW network token.

Source: [FlowToken.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowToken.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0x0ae53cb6e3f42a79` |
| Cadence Testing Framework | `0x0000000000000003` |
| Testnet | `0x7e60df042a9c0868` |
| Mainnet | `0x1654653399040a61` |

# Transactions

Transactions and scripts for `FlowToken` are in the `flow-core-contracts` [repo](https://github.com/onflow/flow-core-contracts/tree/master/transactions/flowToken).

As mentioned in the `FungibleToken` page, developers are encouraged to use
the generic token transactions in the `flow-ft` [repo](https://github.com/onflow/flow-ft/tree/master/transactions) instead.

# Events

Flow relies on a set of core contracts that define key portions of the Flow protocol. Those contracts are core contracts
and are made to emit the events documented below. You can read about the [core contracts here](/build/core-contracts)
and view their source code and event definitions.

Events emitted from core contracts follow a standard format:

`_10

A.{contract address}.{contract name}.{event name}`

The components of the format are:

* `contract address` - the address of the account the contract has been deployed to
* `contract name` - the name of the contract in the source code
* `event name` - the name of the event as declared in the source code

### Flow Token Contract[​](#flow-token-contract "Direct link to Flow Token Contract")

Description of events emitted from the [FLOW Token contract](/build/core-contracts/flow-token).
The contract defines the fungible FLOW token. Please note that events for the fungible token contracts are the same
if deployed to a different account but the `contract address` is
changed to the address of the account the contract has been deployed to.

### Tokens Initialized[​](#tokens-initialized "Direct link to Tokens Initialized")

Event that is emitted when the contract gets created.

* Event name: `TokensInitialized`
* Mainnet event: `A.1654653399040a61.FlowToken.TokensInitialized`
* Testnet event: `A.7e60df042a9c0868.FlowToken.TokensInitialized`

`_10

access(all) event TokensInitialized(initialSupply: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| initialSupply | UFix64 | The initial supply of the tokens |

### Tokens Withdrawn[​](#tokens-withdrawn "Direct link to Tokens Withdrawn")

Event that is emitted when tokens get withdrawn from a Vault.

* Event name: `TokensWithdrawn`
* Mainnet event: `A.1654653399040a61.FlowToken.TokensWithdrawn`
* Testnet event: `A.7e60df042a9c0868.FlowToken.TokensWithdrawn`

`_10

access(all) event TokensWithdrawn(amount: UFix64, from: Address?)`

| Field | Type | Description |
| --- | --- | --- |
| amount | UFix64 | The amount of tokens withdrawn |
| from | Address? | Optional address of the account that owns the vault where tokens were withdrawn from. `nil` if the vault is not in an account's storage |

### Tokens Deposited[​](#tokens-deposited "Direct link to Tokens Deposited")

Event that is emitted when tokens get deposited to a Vault.

* Event name: `TokensDeposited`
* Mainnet event: `A.1654653399040a61.FlowToken.TokensDeposited`
* Testnet event: `A.7e60df042a9c0868.FlowToken.TokensDeposited`

`_10

access(all) event TokensDeposited(amount: UFix64, to: Address?)`

| Field | Type | Description |
| --- | --- | --- |
| amount | UFix64 | The amount of tokens withdrawn |
| to | Address? | Optional address of the account that owns the vault where tokens were deposited to. `nil` if the vault is not in an account's storage |

### Tokens Minted[​](#tokens-minted "Direct link to Tokens Minted")

Event that is emitted when new tokens gets minted.

* Event name: `TokensMinted`
* Mainnet event: `A.1654653399040a61.FlowToken.TokensMinted`
* Testnet event: `A.7e60df042a9c0868.FlowToken.TokensMinted`

`_10

access(all) event TokensMinted(amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| amount | UFix64 | The amount of tokens to mint |

### Tokens Burned[​](#tokens-burned "Direct link to Tokens Burned")

Event that is emitted when tokens get destroyed.

* Event name: `TokensBurned`
* Mainnet event: `A.1654653399040a61.FlowToken.TokensBurned`
* Testnet event: `A.7e60df042a9c0868.FlowToken.TokensBurned`

`_10

access(all) event TokensBurned(amount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| amount | UFix64 | The amount of tokens to burn |

### Minter Created[​](#minter-created "Direct link to Minter Created")

Event that is emitted when a new minter resource gets created.

* Event name: `MinterCreated`
* Mainnet event: `A.1654653399040a61.FlowToken.MinterCreated`
* Testnet event: `A.7e60df042a9c0868.FlowToken.MinterCreated`

`_10

access(all) event MinterCreated(allowedAmount: UFix64)`

| Field | Type | Description |
| --- | --- | --- |
| allowedAmount | UFix64 | The amount of tokens that the minter is allowed to mint |

### Burner Created[​](#burner-created "Direct link to Burner Created")

Event that is emitted when a new burner Resource gets created.

* Event name: `BurnerCreated`
* Mainnet event: `A.1654653399040a61.FlowToken.BurnerCreated`
* Testnet event: `A.7e60df042a9c0868.FlowToken.BurnerCreated`

`_10

access(all) event BurnerCreated()`

### Staking Events[​](#staking-events "Direct link to Staking Events")

To learn more about staking events, read [staking/events/](/networks/staking/staking-scripts-events)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/03-flow-token.md)

Last updated on **Feb 22, 2025** by **bz**

[Previous

Fungible Token](/build/core-contracts/fungible-token)[Next

Service Account](/build/core-contracts/service-account)

###### Rate this page

😞😐😊

* [Flow Token Contract](#flow-token-contract)
* [Tokens Initialized](#tokens-initialized)
* [Tokens Withdrawn](#tokens-withdrawn)
* [Tokens Deposited](#tokens-deposited)
* [Tokens Minted](#tokens-minted)
* [Tokens Burned](#tokens-burned)
* [Minter Created](#minter-created)
* [Burner Created](#burner-created)
* [Staking Events](#staking-events)

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