# Source: https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions/connectors

Connectors | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

* * [Forte Network Upgrade](/blockchain-development-tutorials/forte)* [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)* Connectors

On this page

# Connectors

**Connectors** are the bridge between external DeFi protocols and the standardized Flow Actions primitive interfaces. They act as **protocol adapters** that translate protocol-specific APIs into the universal language of Flow Actions. Think of them as "drivers" that provide a connection between software and a piece of hardware without the software developer needing to know how the hardware expects to receive commands, or an MCP allowing an agent to use an API in a standardized manner.

Flow Actions act as "money LEGOs" with which you can compose various complex operations with simple transactions. These are the benefits of connectors:

* Abstraction Layer: Connectors act like a universal translator between your application and various decentralized finance (DeFi) protocols.
* Standardized Interface: All connectors implement the same core methods, which makes them interchangeable.
* Protocol Integration: They handle the complex interactions with different DeFi services (swaps, staking, lending, and so on).

## How Connectors Work[​](#how-connectors-work "Direct link to How Connectors Work")

### Abstraction Layer[​](#abstraction-layer "Direct link to Abstraction Layer")

Connectors sit between your application logic and protocol-specific contracts:

`_10

Your DeFi Strategy → Flow Actions Connector → Protocol Contract → Blockchain State`

### Interface Implementation[​](#interface-implementation "Direct link to Interface Implementation")

Each connector implements one or more of the five primitive interfaces:

`_10

// Example: A connector implementing the Sink primitive

_10

access(all) struct MyProtocolSink: DeFiActions.Sink {

_10

// Protocol-specific configuration

_10

access(self) let protocolConfig: MyProtocol.Config

_10

_10

// DeFiActions required methods

_10

access(all) fun getSinkType(): Type { ... }

_10

access(all) fun minimumCapacity(): UFix64 { ... }

_10

access(all) fun depositCapacity(from: auth(FungibleToken.Withdraw) &{FungibleToken.Vault}) { ... }

_10

}`

All connectors implement these standard methods:

`_18

// Identity & Component Info

_18

fun getComponentInfo(): ComponentInfo

_18

fun copyID(): UniqueIdentifier?

_18

fun setID(_ id: UniqueIdentifier?)

_18

_18

// Type-specific methods

_18

fun getSinkType(): Type // Sink only

_18

fun getSourceType(): Type // Source only

_18

fun inType() / outType(): Type // Swapper only

_18

_18

// Core operations

_18

fun minimumCapacity(): UFix64 // Sink

_18

fun depositCapacity(from: &Vault) // Sink

_18

fun minimumAvailable(): UFix64 // Source

_18

fun withdrawAvailable(maxAmount: UFix64): @Vault // Source

_18

fun swap(quote: Quote?, inVault: @Vault): @Vault // Swapper

_18

fun getPrice(baseAsset: Type, quoteAsset: Type): UFix64 // PriceOracle

_18

fun flashLoan(amount: UFix64, callback: Function) // Flasher`

### Composition Pattern[​](#composition-pattern "Direct link to Composition Pattern")

You can combine Connetors to create sophisticated workflows:

`_10

// Claim rewards → Swap to different token → Stake in new pool

_10

ProtocolA.RewardsSource → SwapConnectors.SwapSource → ProtocolB.StakingSink`

## Connector Library[​](#connector-library "Direct link to Connector Library")

🔄 SOURCE Primitive Implementations

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connector Location Protocol Purpose|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | VaultSource [FungibleTokenConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc) Generic FungibleToken Withdraw from vaults with minimum balance protection.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | VaultSinkAndSource [FungibleTokenConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc) Generic FungibleToken Combined vault operations (dual interface).|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | SwapSource [SwapConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/SwapConnectors.cdc) Generic (composes with Swappers) Source tokens then swap before returning.|  |  |  |  | | --- | --- | --- | --- | | PoolRewardsSource [IncrementFiStakingConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiStakingConnectors.cdc) IncrementFi Staking Claim staking rewards from pools. | | | | | | | | | | | | | | | | | | | |

⬇️ SINK Primitive Implementations

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connector Location Protocol Purpose|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | VaultSink [FungibleTokenConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc) Generic FungibleToken Deposit to vaults with capacity limits.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | VaultSinkAndSource [FungibleTokenConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc) Generic FungibleToken Combined vault operations (dual interface).|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | SwapSink [SwapConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/SwapConnectors.cdc) Generic (composes with Swappers) Swap tokens before depositing to inner sink.|  |  |  |  | | --- | --- | --- | --- | | PoolSink [IncrementFiStakingConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiStakingConnectors.cdc) IncrementFi Staking Stake tokens in staking pools. | | | | | | | | | | | | | | | | | | | |

🔀 SWAPPER Primitive Implementations

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connector Location Protocol Purpose|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | MultiSwapper [SwapConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/SwapConnectors.cdc) Generic (DEX aggregation) Aggregate multiple swappers for optimal routing.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Swapper [IncrementFiSwapConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiSwapConnectors.cdc) IncrementFi DEX Token swapping through SwapRouter.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Zapper [IncrementFiPoolLiquidityConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiPoolLiquidityConnectors.cdc) IncrementFi Pools Single-token liquidity provision.|  |  |  |  | | --- | --- | --- | --- | | UniswapV2EVMSwapper [UniswapV2SwapConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/evm/UniswapV2SwapConnectors.cdc) Flow EVM Bridge Cross-VM UniswapV2-style swapping. | | | | | | | | | | | | | | | | | | | |

💰 PRICEORACLE Primitive Implementations

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Connector Location Protocol Purpose|  |  |  |  | | --- | --- | --- | --- | | PriceOracle [BandOracleConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/band-oracle/BandOracleConnectors.cdc) Band Protocol External price feeds with staleness validation. | | | | | | | |

⚡ FLASHER Primitive Implementations

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Connector Location Protocol Purpose|  |  |  |  | | --- | --- | --- | --- | | Flasher [IncrementFiFlashloanConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/increment-fi/IncrementFiFlashloanConnectors.cdc) IncrementFi DEX Flash loans through SwapPair contracts. | | | | | | | |

## Guide to Building Connectors[​](#guide-to-building-connectors "Direct link to Guide to Building Connectors")

### Choose Your Primitive[​](#choose-your-primitive "Direct link to Choose Your Primitive")

First, determine which Flow Actions primitive(s) your connector will implement:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Primitive When to Use Example Use Cases|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Source** Your protocol provides tokens Vault withdrawals, reward claiming, unstaking.|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Sink** Your protocol accepts tokens Vault deposits, staking, loan repayments.|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Swapper** Your protocol exchanges tokens DEX trades, cross-chain bridges, LP provision.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | **PriceOracle** Your protocol provides price data Oracle feeds, TWAP calculations.|  |  |  | | --- | --- | --- | | **Flasher** Your protocol offers flash loans Arbitrage opportunities, liquidations. | | | | | | | | | | | | | | | | | |

### Analyze Your Protocol[​](#analyze-your-protocol "Direct link to Analyze Your Protocol")

Study your target protocol to understand:

* **Contract interfaces** and method signatures
* **Required parameters** and data structures
* **Error conditions** and failure modes
* **Fee structures** and payment mechanisms
* **Access controls** and permissions

### Design Your Connector[​](#design-your-connector "Direct link to Design Your Connector")

Plan your connector implementation:

* **Configuration parameters** needed for initialization
* **Capability requirements** for protocol access
* **Error handling strategy** for graceful failures
* **Resource management** for token handling
* **Event emission** for traceability

### Implement the Interface[​](#implement-the-interface "Direct link to Implement the Interface")

Create your connector struct implementing the chosen primitive interface(s).

### Add Safety Features[​](#add-safety-features "Direct link to Add Safety Features")

Implement safety mechanisms:

* **Capacity checking** before operations
* **Balance validation** after operations
* **Graceful error handling** with no-ops
* **Resource cleanup** for empty vaults

### Support Flow Actions Standards[​](#support-flow-actions-standards "Direct link to Support Flow Actions Standards")

Add required Flow Actions support:

* **IdentifiableStruct** implementation
* **UniqueIdentifier** management
* **ComponentInfo** for introspection
* **Event emission** integration

## Best Practices[​](#best-practices "Direct link to Best Practices")

### **Error Handling**[​](#error-handling "Direct link to error-handling")

* **Graceful Failures**: Return empty results instead of panicking.
* **Validation**: Check all inputs and preconditions.
* **Resource Safety**: Properly handle vault resources in all paths.

`_13

// Good: Graceful failure

_13

access(all) fun minimumCapacity(): UFix64 {

_13

if let pool = self.poolCapability.borrow() {

_13

return pool.getAvailableCapacity()

_13

}

_13

return 0.0 // Graceful failure

_13

}

_13

_13

// Bad: Panics on failure

_13

access(all) fun minimumCapacity(): UFix64 {

_13

let pool = self.poolCapability.borrow()! // Will panic if invalid

_13

return pool.getAvailableCapacity()

_13

}`

### **Capacity and Balance Checking**[​](#capacity-and-balance-checking "Direct link to capacity-and-balance-checking")

* **Always Check First**: Validate capacity/availability before operations.
* **Respect Limits**: Work within available constraints.
* **Handle Edge Cases**: Zero amounts, maximum values, empty vaults.

`_14

access(all) fun depositCapacity(from: auth(FungibleToken.Withdraw) &{FungibleToken.Vault}) {

_14

// Check capacity first

_14

let capacity = self.minimumCapacity()

_14

if capacity == 0.0 { return }

_14

_14

// Calculate actual deposit amount

_14

let availableAmount = from.balance

_14

let depositAmount = capacity < availableAmount ? capacity : availableAmount

_14

_14

// Handle edge case

_14

if depositAmount == 0.0 { return }

_14

_14

// Proceed with deposit...

_14

}`

### **Type Safety**[​](#type-safety "Direct link to type-safety")

* **Validate Types**: Ensure vault types match expected types.
* **Early Returns**: Fail fast on type mismatches.
* **Clear Error Messages**: Help developers understand issues.

`_10

access(all) fun depositCapacity(from: auth(FungibleToken.Withdraw) &{FungibleToken.Vault}) {

_10

// Type validation

_10

if from.getType() != self.getSinkType() {

_10

return // No-op for wrong token type

_10

}

_10

_10

// Continue with deposit...

_10

}`

### **Event Integration**[​](#event-integration "Direct link to event-integration")

* **Leverage Post-conditions**: Flow Actions interfaces emit events automatically.
* **Provide Context**: Include relevant information in events.
* **Support Traceability**: Use UniqueIdentifiers consistently.

### **Resource Management**[​](#resource-management "Direct link to resource-management")

* **Handle Empty Vaults**: Use `DeFiActionsUtils.getEmptyVault()` for consistent empty vault creation.
* **Destroy Properly**: Clean up resources in all code paths.
* **Avoid Resource Leaks**: Ensure all vaults are handled appropriately.

### **Capability Management**[​](#capability-management "Direct link to capability-management")

* **Validate Capabilities**: Check capabilities before using them.
* **Handle Revocation**: Gracefully handle revoked capabilities.
* **Proper Entitlements**: Use correct entitlement levels (auth vs unauth).

### **Documentation**[​](#documentation "Direct link to documentation")

* **Clear Comments**: Explain protocol-specific logic.
* **Usage Examples**: Show how to use your connectors.
* **Integration Patterns**: Demonstrate composition with other connectors.

## Integration into Flow Actions[​](#integration-into-flow-actions "Direct link to Integration into Flow Actions")

We will now go over how to build a connector and integrate it with Flow Actions. Specifically, we will showcase the process of using the **VaultSink** connector in the [FungibleTokenConnectors](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/connectors/FungibleTokenConnectors.cdc). It only performs basic token deposits to a vault with capacity limits, implements the Sink interface, has minimal external dependencies (only FungibleToken standard), and requires simple configuration (max balance, deposit vault capability,and unique ID).

The `VaultSink` connector is already deployed and working in Flow Actions. Let's examine how it's integrated:

**Location**: `cadence/contracts/connectors/FungibleTokenConnectors.cdc`
**Contract**: `FungibleTokenConnectors`
**Connector**: `VaultSink` struct that defines the interaction with the connector.

### Deploy Your Connector Contract[​](#deploy-your-connector-contract "Direct link to Deploy Your Connector Contract")

Deploy your connector contract with the following command:

`_10

flow project deploy`

In your 'flow.json' you will find:

`_12

{

_12

"contracts": {

_12

"FungibleTokenConnectors": {

_12

"source": "./cadence/contracts/connectors/FungibleTokenConnectors.cdc",

_12

"aliases": {

_12

"emulator": "f8d6e0586b0a20c7",

_12

"testnet": "...",

_12

"mainnet": "..."

_12

}

_12

}

_12

}

_12

}`

### Create Usage Transactions[​](#create-usage-transactions "Direct link to Create Usage Transactions")

Create transaction templates for using your connectors:

`_23

// Transaction: save_vault_sink.cdc

_23

import "FungibleTokenConnectors"

_23

import "DeFiActions"

_23

import "FungibleToken"

_23

_23

transaction(maxBalance: UFix64) {

_23

prepare(signer: auth(Storage, Capabilities) &Account) {

_23

// Get vault capability for deposits

_23

let vaultCap = signer.capabilities.get<&{FungibleToken.Receiver}>(

_23

/public/flowTokenReceiver

_23

)

_23

_23

// Create the VaultSink connector

_23

let vaultSink = FungibleTokenConnectors.VaultSink(

_23

max: maxBalance,

_23

depositVault: vaultCap,

_23

uniqueID: nil

_23

)

_23

_23

// Save to storage for later use

_23

signer.storage.save(vaultSink, to: /storage/FlowTokenVaultSink)

_23

}

_23

}`

### Real Usage Transaction: VaultSink[​](#real-usage-transaction-vaultsink "Direct link to Real Usage Transaction: VaultSink")

Here's the actual working transaction that creates a VaultSink:

`_43

// File: cadence/transactions/fungible-token-stack/save_vault_sink.cdc

_43

import "FungibleToken"

_43

import "FungibleTokenMetadataViews"

_43

import "FlowToken"

_43

import "FungibleTokenConnectors"

_43

_43

transaction(receiver: Address, vaultPublicPath: PublicPath, sinkStoragePath: StoragePath, max: UFix64?) {

_43

let depositVault: Capability<&{FungibleToken.Vault}>

_43

let signer: auth(SaveValue) &Account

_43

_43

prepare(signer: auth(SaveValue) &Account) {

_43

// Get the receiver's vault capability

_43

self.depositVault = getAccount(receiver).capabilities.get<&{FungibleToken.Vault}>(vaultPublicPath)

_43

self.signer = signer

_43

}

_43

_43

pre {

_43

self.signer.storage.type(at: sinkStoragePath) == nil:

_43

"Collision at sinkStoragePath \(sinkStoragePath.toString())"

_43

self.depositVault.check(): "Invalid deposit vault capability"

_43

}

_43

_43

execute {

_43

// Create the VaultSink connector

_43

let sink = FungibleTokenConnectors.VaultSink(

_43

max: max, // Maximum capacity (nil = unlimited)

_43

depositVault: self.depositVault, // Where tokens will be deposited

_43

uniqueID: nil // No unique ID for this example

_43

)

_43

_43

// Save the connector for later use

_43

self.signer.storage.save(sink, to: sinkStoragePath)

_43

_43

log("VaultSink created and saved!")

_43

log("Max capacity: ".concat(max?.toString() ?? "unlimited"))

_43

log("Receiver: ".concat(receiver.toString()))

_43

}

_43

_43

post {

_43

self.signer.storage.type(at: sinkStoragePath) == Type<FungibleTokenConnectors.VaultSink>():

_43

"VaultSink was not stored correctly"

_43

}

_43

}`

Execute this transaction:

`_10

flow transactions send cadence/transactions/fungible-token-stack/save_vault_sink.cdc \

_10

--arg Address:0x01cf0e2f2f715450 \

_10

--arg PublicPath:"/public/FlowTokenReceiver" \

_10

--arg StoragePath:"/storage/FlowTokenSink" \

_10

--arg "UFix64?":1000.0 \

_10

--signer emulator`

### Create Combinations Examples[​](#create-combinations-examples "Direct link to Create Combinations Examples")

Show how your connectors work with existing Flow Actions components:

`_30

// Example: Using VaultSink in a real deposit workflow

_30

import "FungibleTokenConnectors"

_30

import "FlowToken"

_30

_30

transaction(depositAmount: UFix64) {

_30

prepare(signer: auth(BorrowValue) &Account) {

_30

// 1. Load the saved VaultSink

_30

let sink = signer.storage.borrow<&FungibleTokenConnectors.VaultSink>(

_30

from: /storage/FlowTokenSink

_30

) ?? panic("VaultSink not found - create one first!")

_30

_30

// 2. Create a simple source (your own vault)

_30

let flowVault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_30

from: /storage/FlowTokenVault

_30

) ?? panic("FlowToken vault not found")

_30

_30

// 3. Check sink capacity before depositing

_30

let capacity = sink.minimumCapacity()

_30

log("Sink capacity: ".concat(capacity.toString()))

_30

_30

if capacity >= depositAmount {

_30

// 4. Execute Source → Sink workflow

_30

let tokens <- flowVault.withdraw(amount: depositAmount)

_30

sink.depositCapacity(from: tokens)

_30

log("Deposited ".concat(depositAmount.toString()).concat(" FLOW through VaultSink!"))

_30

} else {

_30

log("Insufficient sink capacity: ".concat(capacity.toString()))

_30

}

_30

}

_30

}`

### Add to Existing Workflows[​](#add-to-existing-workflows "Direct link to Add to Existing Workflows")

You can use VaultSink in advanced Flow Actions workflows:

`_51

// Example: VaultSink in AutoBalancer (real integration pattern)

_51

import "DeFiActions"

_51

import "FungibleTokenConnectors"

_51

import "BandOracleConnectors"

_51

_51

transaction() {

_51

prepare(signer: auth(SaveValue, BorrowValue, IssueStorageCapabilityController) &Account) {

_51

// 1. Create rebalancing sink using VaultSink pattern

_51

let rebalanceCap = getAccount(signer.address)

_51

.capabilities.get<&{FungibleToken.Receiver}>(/public/FlowTokenReceiver)

_51

_51

let rebalanceSink = FungibleTokenConnectors.VaultSink(

_51

max: nil, // No limit for rebalancing

_51

depositVault: rebalanceCap,

_51

uniqueID: nil

_51

)

_51

_51

// 2. Create rebalancing source

_51

let sourceCap = signer.capabilities.storage.issue<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_51

/storage/FlowTokenVault

_51

)

_51

let rebalanceSource = FungibleTokenConnectors.VaultSource(

_51

min: 100.0, // Keep 100 FLOW minimum

_51

withdrawVault: sourceCap,

_51

uniqueID: nil

_51

)

_51

_51

// 3. Create price oracle

_51

let priceOracle = BandOracleConnectors.PriceOracle(

_51

unitOfAccount: Type<@FlowToken.Vault>(),

_51

staleThreshold: 3600,

_51

feeSource: rebalanceSource,

_51

uniqueID: nil

_51

)

_51

_51

// 4. Create AutoBalancer using VaultSink pattern

_51

let autoBalancer <- DeFiActions.createAutoBalancer(

_51

oracle: priceOracle,

_51

vaultType: Type<@FlowToken.Vault>(),

_51

lowerThreshold: 0.9,

_51

upperThreshold: 1.1,

_51

rebalanceSink: rebalanceSink, // Uses VaultSink!

_51

rebalanceSource: rebalanceSource, // Uses VaultSource!

_51

uniqueID: nil

_51

)

_51

_51

signer.storage.save(<-autoBalancer, to: /storage/FlowAutoBalancer)

_51

_51

log("AutoBalancer created using VaultSink/VaultSource pattern!")

_51

}

_51

}`

### For Your Own Connectors[​](#for-your-own-connectors "Direct link to For Your Own Connectors")

When building your own connectors, follow the VaultSink pattern:

1. **Keep constructors simple** - minimal required parameters.
2. **Validate inputs** - check capabilities and preconditions.
3. **Handle errors gracefully** - no-ops instead of panics.
4. **Support Flow Actions standards** - UniqueIdentifier, ComponentInfo.
5. **Test thoroughly** - create usage transactions like the ones shown.
6. **Document clearly** - show real integration examples.

## Conclusion[​](#conclusion "Direct link to Conclusion")

The Flow Actions framework provides a comprehensive set of connectors that successfully implement the five fundamental DeFi primitives across multiple protocols:

* **20+ Connector Implementations** spanning basic vault operations to complex cross-VM swapping.
* **4 Protocol Integrations**: Generic FungibleToken, IncrementFi, Band Oracle, Flow EVM.
* **Composable Architecture**: Combine Connectors to create sophisticated financial workflows.
* **Safety-First Design**: Graceful error handling and resource safety throughout.
* **Event-Driven Traceability**: Full workflow tracking and debugging capabilities.

This framework allows developers to build sophisticated DeFi strategies while maintaining the simplicity and reliability of standardized primitive interfaces. The modular design allows for easy extension to additional protocols while preserving composability and atomic execution guarantees.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/flow-actions/connectors.md)

Last updated on **Oct 29, 2025** by **Brian Doyle**

[Previous

Flow Actions Transaction](/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction)[Next

Basic Combinations](/blockchain-development-tutorials/forte/flow-actions/basic-combinations)

###### Rate this page

😞😐😊

Copy as Markdown

* [How Connectors Work](#how-connectors-work)
  + [Abstraction Layer](#abstraction-layer)+ [Interface Implementation](#interface-implementation)+ [Composition Pattern](#composition-pattern)* [Connector Library](#connector-library)* [Guide to Building Connectors](#guide-to-building-connectors)
      + [Choose Your Primitive](#choose-your-primitive)+ [Analyze Your Protocol](#analyze-your-protocol)+ [Design Your Connector](#design-your-connector)+ [Implement the Interface](#implement-the-interface)+ [Add Safety Features](#add-safety-features)+ [Support Flow Actions Standards](#support-flow-actions-standards)* [Best Practices](#best-practices)
        + [**Error Handling**](#error-handling)+ [**Capacity and Balance Checking**](#capacity-and-balance-checking)+ [**Type Safety**](#type-safety)+ [**Event Integration**](#event-integration)+ [**Resource Management**](#resource-management)+ [**Capability Management**](#capability-management)+ [**Documentation**](#documentation)* [Integration into Flow Actions](#integration-into-flow-actions)
          + [Deploy Your Connector Contract](#deploy-your-connector-contract)+ [Create Usage Transactions](#create-usage-transactions)+ [Real Usage Transaction: VaultSink](#real-usage-transaction-vaultsink)+ [Create Combinations Examples](#create-combinations-examples)+ [Add to Existing Workflows](#add-to-existing-workflows)+ [For Your Own Connectors](#for-your-own-connectors)* [Conclusion](#conclusion)

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