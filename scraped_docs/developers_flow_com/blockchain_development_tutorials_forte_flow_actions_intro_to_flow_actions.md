# Source: https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions

Introduction to Flow Actions | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      + [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

        - [Introduction to Flow Actions](/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions)- [Flow Actions Transaction](/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction)- [Connectors](/blockchain-development-tutorials/forte/flow-actions/connectors)- [Basic Combinations](/blockchain-development-tutorials/forte/flow-actions/basic-combinations)+ [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)

          + [DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Forte Network Upgrade](/blockchain-development-tutorials/forte)* [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)* Introduction to Flow Actions

On this page

# Introduction to Flow Actions

warning

We are reviewing and finalizing Flow Actions in [FLIP 339](https://github.com/onflow/flips/pull/339/files). The specific implementation may change as a part of this process.

We will update these tutorials, but you may need to refactor your code if the implementation changes.

*Actions* are a suite of standardized Cadence interfaces that allow developers to compose complex workflows, starting with decentralized finance (DeFi) workflows, by connecting small, reusable components. Actions provide a "LEGO" framework of blocks where each component performs a single operation (deposit, withdraw, swap, price lookup, flash loan) while maintaining composability with other components. This creates sophisticated workflows executable in a single atomic transaction.

By using Flow Actions, developers can remove large amounts of tailored complexity from building DeFi apps and can instead focus on business logic using nouns and verbs.

## Key features[​](#key-features "Direct link to Key features")

* **Atomic Composition** - All operations complete or fail together.
* **Weak Guarantees** - Flexible error handling, no-ops when conditions aren't met.
* **Event Traceability** - UniqueIdentifier system for tracking operations.
* **Protocol Agnostic** - Standardized interfaces across different protocols.
* **Struct-based** - Lightweight, copyable components for efficient composition.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After you complete this tutorial, you will be able to:

* Understand the key features of Flow Actions including atomic composition, weak guarantees, and event traceability
* Create and use Sources to provide tokens from various protocols and locations
* Create and use Sinks to accept tokens up to defined capacity limits
* Create and use Swappers to exchange tokens between different types with price estimation
* Create and use Price Oracles to get price data for assets with consistent denomination
* Create and use Flashers to provide flash loans with atomic repayment requirements
* Use UniqueIdentifiers to trace and correlate operations across multiple Flow Actions
* Compose complex DeFi workflows by connecting multiple Actions in a single atomic transaction

# Prerequisites

## Cadence programming language[​](#cadence-programming-language "Direct link to Cadence programming language")

This tutorial assumes you have a modest knowledge of [Cadence](https://cadence-lang.org/docs). If you don't, you can follow along, but you'll get more out of it if you complete our [Cadence](https://cadence-lang.org/docs) tutorials. Most developers find it easier than other blockchain languages and it's not hard to pick up.

## Flow Action types[​](#flow-action-types "Direct link to Flow Action types")

The first five Flow Actions implement five core primitives to integrate external DeFi protocols.

1. **Source**: Provides tokens on demand (for example, withdraw from vault, claim rewards, pull liquidity)

![source](/assets/images/source-bc4fb0b6e9216d36592df3e6ccf6c4f0.png)

2. **Sink**: Accepts tokens up to capacity (for example, deposit to vault, repay loan, add liquidity)

![sink](/assets/images/sink-ae5a2433af3f2bb198bbe50f9d31de15.png)

3. **Swapper**: Exchanges one token type for another (for example, targeted DEX trades, multi-protocol aggregated swaps)

![swapper](/assets/images/swapper-0640b19d3bb15ca688cb9e4b83a1bf81.png)

4. **PriceOracle**: Provides price data for assets (for example, external price feeds, DEX prices, price caching)

![price oracle](/assets/images/price-oracle-a63a48489d0e323d944097248db5f567.png)

5. **Flasher**: Provides flash loans with atomic repayment (for example, arbitrage, liquidations)

![flasher](/assets/images/flasher-7c35bdaa53846ef34edee481aa7fee08.png)

## Connectors[​](#connectors "Direct link to Connectors")

[Connectors](/blockchain-development-tutorials/forte/flow-actions/connectors) create the bridge between the standardized interfaces of Flow Actions and the often customized and complicated mechanisms of different DeFi protocols. You can use existing connectors that other developers wrote, or create your own.

To instantiate Flow Actions, create an instance of the appropriate [struct] from a connector that provides the desired type of action connected to the desired DeFi protocol.

For more information, read the [connectors article](/blockchain-development-tutorials/forte/flow-actions/connectors).

## Token types[​](#token-types "Direct link to Token types")

In Cadence, tokens that adhere to the [Fungible Token Standard](https://developers.flow.com/build/cadence/guides/fungible-token) have types that work with type safety principles.

For example, you can find the type of $FLOW by running this script:

`_10

import "FlowToken"

_10

_10

access(all) fun main(): String {

_10

return Type<@FlowToken.Vault>().identifier

_10

}`

You'll get:

`_10

A.1654653399040a61.FlowToken.Vault`

Many Flow Actions use these types to provide a safer method of working with tokens than an arbitrary address that may or may not be a token.

## Flow Actions[​](#flow-actions "Direct link to Flow Actions")

The following Flow Actions standardize **usage** patterns for common defi-related tasks. By working with them, you - or Artificial Intelligence (AI) agents - can more easily write transactions and functionality regardless of the myriad of different ways each protocol works to accomplish these tasks.

info

Defi protocols and tools operate very differently, which means the calls to instantiate the same kind of action connected to different protocols will vary by protocol and connector.

### Source[​](#source "Direct link to Source")

A source is a primitive component that can supply a [vault](https://developers.flow.com/build/cadence/guides/fungible-token#vaults-on-flow) which contains the requested type and amount of tokens from something the user controls, or has authorized access to. This includes, but isn't limited to, personal vaults, accounts in protocols, and rewards.

![source](/assets/images/source-bc4fb0b6e9216d36592df3e6ccf6c4f0.png)

You'll likely use one or more sources in any transactions using actions if the user needs to pay for something or otherwise provide tokens.

Sources conform to the `Source` [interface](https://cadence-lang.org/docs/language/interfaces):

`_10

access(all) struct interface Source : IdentifiableStruct {

_10

/// Returns the Vault type provided by this Source

_10

access(all) view fun getSourceType(): Type

_10

/// Returns an estimate of how much can be withdrawn

_10

access(all) fun minimumAvailable(): UFix64

_10

/// Withdraws up to maxAmount, returning what's actually available

_10

access(FungibleToken.Withdraw) fun withdrawAvailable(maxAmount: UFix64): @{FungibleToken.Vault}

_10

}`

Every source is guaranteed to have the above functions and return types that allow you to get the type of vault that the source returns, get an estimate of how many tokens users may currently withdraw, and actually withdraw those tokens, up to the amount available.

Sources *degrade gracefully* - If the requested amount of tokens is not available, they return the available amount. They always return a vault, even if that vault is empty.

To create a source, instantiate a struct that conforms to the `Source` interface corresponding to a given protocol [connector](/blockchain-development-tutorials/forte/flow-actions/connectors). For example, to create a source from a generic vault, create a `VaultSource` from [`FungibleTokenConnectors`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc):

`_20

import "FungibleToken"

_20

import "FungibleTokenConnectors"

_20

_20

transaction {

_20

_20

prepare(acct: auth(BorrowValue) {

_20

let withdrawCap = acct.storage.borrow<auth(FungibleToken.Withdraw) {FungibleToken.Vault}>(

_20

/storage/flowTokenVault

_20

)

_20

_20

let source = FungibleTokenConnectors.VaultSource(

_20

min: 0.0,

_20

withdrawVault: withdrawCap,

_20

uniqueID: nil

_20

)

_20

_20

// Note: Logs are only visible in the emulator console

_20

log("Source created for vault type: ".concat(source.withdrawVaultType.identifier))

_20

}

_20

}`

### Sink[​](#sink "Direct link to Sink")

A sink is the opposite of a source - it's a place to send tokens, up to the limit of the capacity defined in the sink. As with any [resource](https://cadence-lang.org/docs/language/resources), this process is non-destructive. Any remaining tokens remain in the vault that the source provides. They also have flexible limits, meaning the capacity can be dynamic.

![sink](/assets/images/sink-ae5a2433af3f2bb198bbe50f9d31de15.png)

Sinks adhere to the `Sink` [interface](https://cadence-lang.org/docs/language/interfaces).

`_10

access(all) struct interface Sink : IdentifiableStruct {

_10

/// Returns the Vault type accepted by this Sink

_10

access(all) view fun getSinkType(): Type

_10

/// Returns an estimate of remaining capacity

_10

access(all) fun minimumCapacity(): UFix64

_10

/// Deposits up to capacity, leaving remainder in the referenced vault

_10

access(all) fun depositCapacity(from: auth(FungibleToken.Withdraw) &{FungibleToken.Vault})

_10

}`

You create a sink similar how you create a source, which is to instantiate an instance of the appropriate `struct` from the [connector](/blockchain-development-tutorials/forte/flow-actions/connectors). For example, to create a sink in a generic vault from, instantiate a `VaultSink` from [`FungibleTokenConnectors`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc):

`_27

import "FungibleToken"

_27

import "FungibleTokenConnectors"

_27

_27

transaction {

_27

_27

prepare(acct: &Account) {

_27

// Public, non-auth capability to deposit into the vault

_27

let depositCap = acct.capabilities.get<&{FungibleToken.Vault}>(

_27

/public/flowTokenReceiver

_27

)

_27

_27

// Optional: specify a max balance the user's Flow Token vault should hold

_27

let maxBalance: UFix64? = nil // or UFix64(1000.0)

_27

_27

// Optional: for aligning with Source in a stack

_27

let uniqueID = nil

_27

_27

let sink = FungibleTokenConnectors.VaultSink(

_27

max: maxBalance,

_27

depositVault: depositCap,

_27

uniqueID: uniqueID

_27

)

_27

_27

// Note: Logs are only visible in the emulator console

_27

log("VaultSink created for deposit type: ".concat(sink.depositVaultType.identifier))

_27

}

_27

}`

### Swapper[​](#swapper "Direct link to Swapper")

A swapper exchanges tokens between different types with support for bidirectional swaps and price estimation. Bi-directional means that they support swaps in both directions, which is necessary if an inner connector can't accept the full swap output balance.

![swapper](/assets/images/swapper-0640b19d3bb15ca688cb9e4b83a1bf81.png)

They also contain price discovery to provide estimates for the amounts in and out via the [`{Quote}`] object, and the [quote system] allows price caching and execution parameter optimization.

Swappers conform to the `Swapper` [interface](https://cadence-lang.org/docs/language/interfaces):

`` _13

access(all) struct interface Swapper : IdentifiableStruct {

_13

/// Input and output token types - in and out token types via default `swap()` route

_13

access(all) view fun inType(): Type

_13

access(all) view fun outType(): Type

_13

_13

/// Price estimation methods - quote required amount given some desired output & output for some provided input

_13

access(all) fun quoteIn(forDesired: UFix64, reverse: Bool): {Quote}

_13

access(all) fun quoteOut(forProvided: UFix64, reverse: Bool): {Quote}

_13

_13

/// Swap execution methods

_13

access(all) fun swap(quote: {Quote}?, inVault: @{FungibleToken.Vault}): @{FungibleToken.Vault}

_13

access(all) fun swapBack(quote: {Quote}?, residual: @{FungibleToken.Vault}): @{FungibleToken.Vault}

_13

} ``

To create a swapper, instantiate the appropriate `struct` from the appropriate connector. To create a swapper for [IncrementFi](https://app.increment.fi/swap?in=A.1654653399040a61.FlowToken&out=) with the [`IncrementFiSwapConnectors`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiSwapConnectors.cdc), instantiate `Swapper`:

`_33

import "FlowToken"

_33

import "USDCFlow"

_33

import "IncrementFiSwapConnectors"

_33

import "SwapConfig"

_33

_33

transaction {

_33

prepare(acct: &Account) {

_33

// Derive the path keys from the token types

_33

let flowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@FlowToken.Vault>().identifier)

_33

let usdcFlowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@USDCFlow.Vault>().identifier)

_33

_33

// Minimal path Flow -> USDCFlow

_33

let swapper = IncrementFiSwapConnectors.Swapper(

_33

path: [

_33

flowKey,

_33

usdcFlowKey

_33

],

_33

inVault: Type<@FlowToken.Vault>(),

_33

outVault: Type<@USDCFlow.Vault>(),

_33

uniqueID: nil

_33

)

_33

_33

// Example: quote how much USDCFlow you'd get for 10.0 FLOW

_33

let qOut = swapper.quoteOut(forProvided: 10.0, reverse: false)

_33

// Note: Logs are only visible in the emulator console

_33

log(qOut)

_33

_33

// Example: quote how much FLOW you'd need to get 25.0 USDCFlow

_33

let qIn = swapper.quoteIn(forDesired: 25.0, reverse: false)

_33

// Note: Logs are only visible in the emulator console

_33

log(qIn)

_33

}

_33

}`

### Price oracle[​](#price-oracle "Direct link to Price oracle")

A price [oracle](https://developers.flow.com/defi/defi-contracts-mainnet#oracles) provides price data for assets with a consistent denomination. All prices are returned in the same unit and will return `nil` rather than reverting in the event that a price is unavailable. Prices are indexed by [Cadence type](https://cadence-lang.org/docs/language/types-and-type-system/type-safety), requiring a specific Cadence-based token type for which to serve prices, as opposed to looking up an asset by a generic address.

![price oracle](/assets/images/price-oracle-a63a48489d0e323d944097248db5f567.png)

You can pass an argument this `Type`, or any conforming fungible token type conforming to the interface to the `price` function to get a price.

The full [interface](https://cadence-lang.org/docs/language/interfaces) for `PriceOracle` is:

`_10

access(all) struct interface PriceOracle : IdentifiableStruct {

_10

/// Returns the denomination asset (e.g., USDCf, FLOW)

_10

access(all) view fun unitOfAccount(): Type

_10

/// Returns current price or nil if unavailable, conditions for which are implementation-specific

_10

access(all) fun price(ofToken: Type): UFix64?

_10

}`

To create a `PriceOracle` from [Band](https://blog.bandprotocol.com/) with [`BandOracleConnectors`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/band-oracle/BandOracleConnectors.cdc):

info

You need to pay the oracle to get information from it. Here, we're using another Flow Action - a source - to fund getting a price from the oracle.

`_32

import "FlowToken"

_32

import "FungibleToken"

_32

import "FungibleTokenConnectors"

_32

import "BandOracleConnectors"

_32

_32

transaction {

_32

_32

prepare(acct: auth(IssueStorageCapabilityController) &Account) {

_32

// Ensure we have an authorized capability for FlowToken (auth Withdraw)

_32

let storagePath = /storage/flowTokenVault

_32

let withdrawCap = acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(storagePath)

_32

_32

// Fee source must PROVIDE FlowToken vaults (per PriceOracle preconditions)

_32

let feeSource = FungibleTokenConnectors.VaultSource(

_32

min: 0.0, // keep at least 0.0 FLOW in the vault

_32

withdrawVault: withdrawCap, // auth withdraw capability

_32

uniqueID: nil

_32

)

_32

_32

// unitOfAccount must be a mapped symbol in BandOracleConnectors.assetSymbols.

_32

// The contract's init already maps FlowToken -> "FLOW", so this is valid.

_32

let oracle = BandOracleConnectors.PriceOracle(

_32

unitOfAccount: Type<@FlowToken.Vault>(), // quote token (e.g. FLOW in BASE/FLOW)

_32

staleThreshold: 600, // seconds; nil to skip staleness checks

_32

feeSource: feeSource,

_32

uniqueID: nil

_32

)

_32

_32

// Note: Logs are only visible in the emulator console

_32

log("Created PriceOracle; unit: ".concat(oracle.unitOfAccount().identifier))

_32

}

_32

}`

### Flasher[​](#flasher "Direct link to Flasher")

A flasher provides flash loans with atomic repayment requirements.

![flasher](/assets/images/flasher-7c35bdaa53846ef34edee481aa7fee08.png)

If you're not familiar with flash loans, imagine a scenario where you discovered an NFT listed for sale one one marketplace for 1 million dollars, then noticed an open bid to buy that same NFT for 1.1 million dollars on another marketplace.

In theory, you could make an easy 100k by buying the NFT on the first marketplace and then fulfilling the open buy offer on the second marketplace. There's just one big problem - You might not have 1 million dollars liquid just laying around for you to purchase the NFT!

Flash loans allow you to create one transaction during which you:

1. Borrow 1 million dollars.
2. Purchase the NFT.
3. Sell the NFT.
4. Repay 1 million dollars plus a small fee.

warning

This scenario may be a scam. A scammer could set up this situation as bait and cancel the buy order the instant someone purchases the NFT that is for sale. You'd have paid a vast amount of money for something worthless.

The great thing about Cadence transactions, with or without Actions, is that you can set up an atomic transaction where everything either works, or is reverted. Either you make 100k, or nothing happens except a tiny expenditure of compute units.

Flashers adhere to the `Flasher` interface:

`_13

access(all) struct interface Flasher : IdentifiableStruct {

_13

/// Returns the asset type this Flasher can issue as a flash loan

_13

access(all) view fun borrowType(): Type

_13

/// Returns the estimated fee for a flash loan of the specified amount

_13

access(all) fun calculateFee(loanAmount: UFix64): UFix64

_13

/// Performs a flash loan of the specified amount. The callback function is passed the fee amount, a loan Vault,

_13

/// and data. The callback function should return a Vault containing the loan + fee.

_13

access(all) fun flashLoan(

_13

amount: UFix64,

_13

data: AnyStruct?,

_13

callback: fun(UFix64, @{FungibleToken.Vault}, AnyStruct?): @{FungibleToken.Vault} // fee, loan, data

_13

)

_13

}`

You create a flasher the same way as the other actions, but you'll need the address for a `SwapPair`. You can get that onchain at runtime. For example, to borrow $FLOW from [IncrementFi](https://app.increment.fi/swap?in=A.1654653399040a61.FlowToken&out=):

`_62

import "FungibleToken"

_62

import "FlowToken"

_62

import "USDCFlow"

_62

import "SwapInterfaces"

_62

import "SwapConfig"

_62

import "SwapFactory"

_62

import "IncrementFiFlashloanConnectors"

_62

_62

transaction {

_62

_62

prepare(_ acct: &Account) {

_62

// Increment uses token *keys* like "A.1654653399040a61.FlowToken" (mainnet FlowToken)

_62

// and "A.f1ab99c82dee3526.USDCFlow" (mainnet USDCFlow).

_62

let flowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@FlowToken.Vault>().identifier)

_62

let usdcFlowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@USDCFlow.Vault>().identifier)

_62

_62

// Ask the factory for the pair's public capability (or address), then verify it.

_62

// Depending on the exact factory interface you have, one of these will exist:

_62

// - getPairAddress(token0Key: String, token1Key: String): Address

_62

// - getPairPublicCap(token0Key: String, token1Key: String): Capability<&{SwapInterfaces.PairPublic}>

_62

// - getPair(token0Key: String, token1Key: String): Address

_62

//

_62

// Try address first; if your factory exposes a different helper, swap it in.

_62

let pairAddr: Address = SwapFactory.getPairAddress(flowKey, usdcFlowKey)

_62

_62

// Sanity-check: borrow PairPublic and verify it actually contains FLOW/USDCFlow

_62

let pair = getAccount(pairAddr)

_62

.capabilities

_62

.borrow<&{SwapInterfaces.PairPublic}>(SwapConfig.PairPublicPath)

_62

?? panic("Could not borrow PairPublic at resolved address")

_62

_62

let info = pair.getPairInfoStruct()

_62

assert(

_62

(info.token0Key == flowKey && info.token1Key == usdcFlowKey) ||

_62

(info.token0Key == usdcFlowKey && info.token1Key == flowKey),

_62

message: "Resolved pair does not match FLOW/USDCFlow"

_62

)

_62

_62

// Instantiate the Flasher to borrow FLOW (switch to USDCFlow if you want that leg)

_62

let flasher = IncrementFiFlashloanConnectors.Flasher(

_62

pairAddress: pairAddr,

_62

type: Type<@FlowToken.Vault>(),

_62

uniqueID: nil

_62

)

_62

_62

// Note: Logs are only visible in the emulator console

_62

log("Flasher ready on mainnet FLOW/USDCFlow at ".concat(pairAddr.toString()))

_62

_62

flasher.flashloan(

_62

amount: 100.0

_62

data: nil

_62

callback: flashloanCallback

_62

)

_62

}

_62

}

_62

_62

// Callback function passed to flasher.flashloan

_62

access(all)

_62

fun flashloanCallback(fee: UFix64, loan: @{FungibleToken.Vault}, data: AnyStruct?): @{FungibleToken.Vault} {

_62

log("Flashloan with balance of \(loan.balance) \(loan.getType().identifier) executed")

_62

return <-loan

_62

}`

## Identification and traceability[​](#identification-and-traceability "Direct link to Identification and traceability")

The `UniqueIdentifier` allows protocols to trace stack operations via Flow Actions interface-level events, which identifies them by IDs. `IdentifiableResource` implementations should verify that access to the identifier is encapsulated by the structures they identify.

While you can create Cadence struct types in any context (such as passed in as transaction parameters), the authorized `AuthenticationToken` [capability](https://cadence-lang.org/docs/language/capabilities) verifies that only those issued by the Flow Actions contract can be used in connectors, preventing forgery.

For example, to use a `UniqueIdentifier` in a source->swap->sink:

`_82

import "FungibleToken"

_82

import "FlowToken"

_82

import "USDCFlow"

_82

import "FungibleTokenConnectors"

_82

import "IncrementFiSwapConnectors"

_82

import "SwapConfig"

_82

import "DeFiActions"

_82

_82

transaction {

_82

_82

prepare(acct: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue, UnpublishCapability) &Account) {

_82

// Standard token paths

_82

let storagePath = /storage/flowTokenVault

_82

let receiverStoragePath = USDCFlow.VaultStoragePath

_82

let receiverPublicPath = USDCFlow.VaultPublicPath

_82

_82

// Ensure private auth-withdraw (for Source)

_82

let withdrawCap = acct.capabilities.storage.issue<auth(FungibleToken.Withdraw) &{FungibleToken.Vault}>(storagePath)

_82

_82

// Ensure public receiver Capability (for Sink) - configure receiving Vault is none exists

_82

if acct.storage.type(at: receiverStoragePath) == nil {

_82

// Save the USDCFlow Vault

_82

acct.storage.save(<-USDCFlow.createEmptyVault(vaultType: Type<@USDCFlow.Vault>()), to: USDCFlow.VaultStoragePath)

_82

// Issue and publish public Capabilities to the token's default paths

_82

let publicCap = acct.capabilities.storage.issue<&USDCFlow.Vault>(storagePath)

_82

?? panic("failed to link public receiver")

_82

acct.capabilities.unpublish(receiverPublicPath)

_82

acct.capabilities.unpublish(USDCFlow.ReceiverPublicPath)

_82

acct.capabilities.publish(cap, at: receiverPublicPath)

_82

acct.capabilities.publish(cap, at: USDCFlow.ReceiverPublicPath)

_82

}

_82

let depositCap = acct.capabilities.get<&{FungibleToken.Vault}>(receiverPublicPath)

_82

_82

// Initialize shared UniqueIdentifier - passed to each connector on init

_82

let uniqueIdentifier = DeFiActions.createUniqueIdentifier()

_82

_82

// Instantiate: Source, Swapper, Sink

_82

let source = FungibleTokenConnectors.VaultSource(

_82

min: 5.0,

_82

withdrawVault: withdrawCap,

_82

uniqueID: uniqueIdentifier

_82

)

_82

_82

// Derive the IncrementFi token keys from the token types

_82

let flowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@FlowToken.Vault>().identifier)

_82

let usdcFlowKey = SwapConfig.SliceTokenTypeIdentifierFromVaultType(vaultTypeIdentifier: Type<@USDCFlow.Vault>().identifier)

_82

_82

// Replace with a real Increment path when swapping tokens (e.g., FLOW → USDCFlow)

_82

// e.g. ["A.1654653399040a61.FlowToken", "A.f1ab99c82dee3526.USDCFlow"]

_82

let swapper = IncrementFiSwapConnectors.Swapper(

_82

path: [flowKey, usdcFlowKey],

_82

inVault: Type<@FlowToken.Vault>(),

_82

outVault: Type<@USDCFlow.Vault>(),

_82

uniqueID: uniqueIdentifier

_82

)

_82

_82

let sink = FungibleTokenConnectors.VaultSink(

_82

max: nil,

_82

depositVault: depositCap,

_82

uniqueID: uniqueIdentifier

_82

)

_82

_82

// ----- Real composition (no destroy) -----

_82

// 1) Withdraw from Source

_82

let tokens <- source.withdrawAvailable(maxAmount: 100.0)

_82

_82

// 2) Swap with Swapper from FLOW → USDCFlow

_82

let swapped <- swapper.swap(quote: nil, inVault: <-tokens)

_82

_82

// 3) Deposit into Sink (consumes by reference via withdraw())

_82

sink.depositCapacity(from: &swapped as auth(FungibleToken.Withdraw) &{FungibleToken.Vault})

_82

_82

// 4) Return any residual by depositing the *entire* vault back to user's USDCFlow vault

_82

// (works even if balance is 0; deposit will still consume the resource)

_82

depositCap.borrow().deposit(from: <-swapped)

_82

_82

// Optional: inspect that all three share the same ID

_82

log(source.id())

_82

log(swapper.id())

_82

log(sink.id())

_82

}

_82

}`

## Why `UniqueIdentifier` matters in FlowActions[​](#why-uniqueidentifier-matters-in-flowactions "Direct link to why-uniqueidentifier-matters-in-flowactions")

The `UniqueIdentifier` is used to tag multiple FlowActions connectors as part of the **same logical operation**.  
By aligning the same ID across connectors (for example, Source → Swapper → Sink), you can:

### 1. Event correlation[​](#1-event-correlation "Direct link to 1. Event correlation")

* Every connector emits events tagged with its `UniqueIdentifier`.
* Shared IDs let you filter and group related events in the chain's event stream.
* Makes it easy to see that a withdrawal, swap, and deposit were part of **one workflow**.

### 2. Stack tracing[​](#2-stack-tracing "Direct link to 2. Stack tracing")

* When you use composite connectors (for example, `SwapSource`, `SwapSink`, `MultiSwapper`), IDs allow you to trace the complete path through the stack.
* Helpful to heklp you debug and understand the flow of operations inside complex strategies.

### 3. Analytics and attribution[​](#3-analytics-and-attribution "Direct link to 3. Analytics and attribution")

* Allows measuring usage of specific strategies or routes.
* Lets you join data from multiple connectors into a single logical "transaction" for reporting.
* Supports fee attribution and performance monitorsacross multi-step workflows.

### Without a shared `UniqueIdentifier`[​](#without-a-shared-uniqueidentifier "Direct link to without-a-shared-uniqueidentifier")

* Events from different connectors appear unrelated, even if they occurred in the same transaction.
* Harder to debug, track, or analyze multi-step processes.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned about Flow Actions, a suite of standardized Cadence interfaces that enable developers to compose complex DeFi workflows using small, reusable components. You explored the five core Flow Action types - Source, Sink, Swapper, PriceOracle, and Flasher - and learned how to create and use them with various connectors.

Now that you have completed this tutorial, you can:

* Understand the key features of Flow Actions including atomic composition, weak guarantees, and event traceability
* Create and use Sources to provide tokens from various protocols and locations
* Create and use Sinks to accept tokens up to defined capacity limits
* Create and use Swappers to exchange tokens between different types with price estimation
* Create and use Price Oracles to get price data for assets with consistent denomination
* Create and use Flashers to provide flash loans with atomic repayment requirements
* Use UniqueIdentifiers to trace and correlate operations across multiple Flow Actions
* Compose complex DeFi workflows by connecting multiple Actions in a single atomic transaction

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions.md)

Last updated on **Dec 1, 2025** by **Brian Doyle**

[Previous

Flow Actions](/blockchain-development-tutorials/forte/flow-actions)[Next

Flow Actions Transaction](/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Key features](#key-features)* [Learning Objectives](#learning-objectives)* [Cadence programming language](#cadence-programming-language)* [Flow Action types](#flow-action-types)* [Connectors](#connectors)* [Token types](#token-types)* [Flow Actions](#flow-actions)
              + [Source](#source)+ [Sink](#sink)+ [Swapper](#swapper)+ [Price oracle](#price-oracle)+ [Flasher](#flasher)* [Identification and traceability](#identification-and-traceability)* [Why `UniqueIdentifier` matters in FlowActions](#why-uniqueidentifier-matters-in-flowactions)
                  + [1. Event correlation](#1-event-correlation)+ [2. Stack tracing](#2-stack-tracing)+ [3. Analytics and attribution](#3-analytics-and-attribution)+ [Without a shared `UniqueIdentifier`](#without-a-shared-uniqueidentifier)* [Conclusion](#conclusion)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.