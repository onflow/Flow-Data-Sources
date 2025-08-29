# Source: https://developers.flow.com/blockchain-development-tutorials/flow-actions/basic-combinations

Basic Combinations | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Flow Actions](/blockchain-development-tutorials/flow-actions)

  + [Introduction to Flow Actions](/blockchain-development-tutorials/flow-actions/intro-to-flow-actions)
  + [Flow Actions Transaction](/blockchain-development-tutorials/flow-actions/flow-actions-transaction)
  + [Connectors](/blockchain-development-tutorials/flow-actions/connectors)
  + [Basic Combinations](/blockchain-development-tutorials/flow-actions/basic-combinations)
  + [Introduction to Scheduled Callbacks](/blockchain-development-tutorials/flow-actions/scheduled-callbacks-introduction)
* [Token Development and Registration](/blockchain-development-tutorials/tokens)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Flow EVM Guides](/blockchain-development-tutorials/evm)
* [Cadence Tutorials](/blockchain-development-tutorials/cadence)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* [Flow Actions](/blockchain-development-tutorials/flow-actions)
* Basic Combinations

On this page

# Composing Workflows with Flow Actions

warning

Flow Actions are being reviewed and finalized in [FLIP 339](https://github.com/onflow/flips/pull/339/files). The specific implementation may change as a part of this process.

These tutorials will be updated, but you may need to refactor your code if the implementation changes.

Flow Actions are designed to be **composable** meaning you can chain them together like LEGO blocks to build complex strategies. Each primitive has a standardized interface that works consistently across all protocols, eliminating the need to learn multiple APIs. This composability enables atomic execution of multi-step workflows within single transactions, ensuring either complete success or safe failure. By combining these primitives, developers can create sophisticated DeFi strategies like automated yield farming, cross-protocol arbitrage, and portfolio rebalancing. The [5 Flow Actions Primitives](/blockchain-development-tutorials/flow-actions/intro-to-flow-actions) are:

* **Source** → Provides tokens on demand by withdrawing from vaults or claiming rewards. Sources respect minimum balance constraints and return empty vaults gracefully when nothing is available.
* **Sink** → Accepts token deposits up to a specified capacity limit. Sinks perform no-ops when capacity is exceeded rather than reverting, enabling smooth workflow execution.
* **Swapper** → Exchanges one token type for another through DEX trades or cross-chain bridges. Swappers support bidirectional operations and provide quote estimation for slippage protection.
* **PriceOracle** → Provides real-time price data for assets from external feeds or DEX prices. Oracles handle staleness validation and return nil for unavailable prices rather than failing.
* **Flasher** → Issues flash loans that must be repaid within the same transaction via callback execution. Flashers enable capital-efficient strategies like arbitrage and liquidations without requiring upfront capital.

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After completing this tutorial, you will be able to:

* Understand the key features of Flow Actions including atomic composition, weak guarantees, and event traceability
* Create and use Sources to provide tokens from various protocols and locations
* Create and use Sinks to accept tokens up to defined capacity limits
* Create and use Swappers to exchange tokens between different types with price estimation
* Create and use Price Oracles to get price data for assets with consistent denomination
* Create and use Flashers to provide flash loans with atomic repayment requirements
* Use UniqueIdentifiers to trace and correlate operations across multiple Flow Actions
* Compose complex DeFi workflows by connecting multiple Actions in a single atomic transaction

## Core Flow Patterns[​](#core-flow-patterns "Direct link to Core Flow Patterns")

### Linear Flow (Source → Swapper → Sink)[​](#linear-flow-source--swapper--sink "Direct link to Linear Flow (Source → Swapper → Sink)")

The most common pattern: get tokens, convert them, then deposit them.

![vault source](/assets/images/vault-source-fdd4d13a71b7cb7efe5a644b7b838086.png)
![swap vault sink](/assets/images/swap-vaultsink-9f9e5ec19aa980f504dded666deec04b.png)

**Example**: Claim rewards → Swap to different token → Stake in new pool

### Bidirectional Flow (Source ↔ Sink)[​](#bidirectional-flow-source--sink "Direct link to Bidirectional Flow (Source ↔ Sink)")

Two-way operations where you can both deposit and withdraw.

![vault source](/assets/images/vault-source-fdd4d13a71b7cb7efe5a644b7b838086.png)
![vault sink](/assets/images/vault-sink-52a21926e34bb10ee162d42cd91bdc3f.png)

**Example**: Vault operations with both deposit and withdrawal capabilities

### Aggregated Flow (Multiple Sources → Aggregator → Sink)[​](#aggregated-flow-multiple-sources--aggregator--sink "Direct link to Aggregated Flow (Multiple Sources → Aggregator → Sink)")

Combine multiple sources for optimal results.

`_10

Source A → Aggregator → Sink

_10

Source B ↗

_10

Source C ↗`

**Example**: Multiple DEX aggregators finding the best swap route

## Common DeFi Workflow Combinations[​](#common-defi-workflow-combinations "Direct link to Common DeFi Workflow Combinations")

### Single Token to LP (Zapper)[​](#single-token-to-lp-zapper "Direct link to Single Token to LP (Zapper)")

**Goal**: Convert a single token into liquidity provider (LP) tokens in one transaction

The **Zapper** is a specialized connector that combines swapper and sink functionality. It takes a single token input and outputs LP tokens by automatically handling the token splitting, swapping, and liquidity provision process.

![zapper](/assets/images/zapper-20af683d5f036b793f416f55a46d2afc.png)

**How it works:**

1. Takes single token A as input
2. Splits it into two portions
3. Swaps one portion to token B
4. Provides liquidity with A + B to get LP tokens
5. Returns LP tokens as output

`_13

// Zapper: Convert single FLOW token to FLOW/USDC LP tokens

_13

let zapper = IncrementFiPoolLiquidityConnectors.Zapper(

_13

token0Type: Type<@FlowToken.Vault>(), // Input token type

_13

token1Type: Type<@USDC.Vault>(), // Paired token type

_13

stableMode: false, // Use volatile pricing

_13

uniqueID: nil

_13

)

_13

_13

// Execute: Input 100 FLOW → Output FLOW/USDC LP tokens

_13

let flowTokens <- flowVault.withdraw(amount: 100.0)

_13

let lpTokens <- zapper.swap(nil, inVault: <-flowTokens)

_13

_13

// Now you have LP tokens ready for staking or further use`

**Benefits:**

* **Simplicity**: Single transaction converts any token to LP position
* **Efficiency**: Automatically calculates optimal split ratios
* **Composability**: Output LP tokens work with any sink connector

### Reward Harvesting & Conversion[​](#reward-harvesting--conversion "Direct link to Reward Harvesting & Conversion")

**Goal**: Claim staking rewards and convert them to a stable token

This workflow automatically claims accumulated staking rewards and converts them to a stable asset like USDC. It combines a rewards source, token swapper, and vault sink to create a seamless reward collection and conversion process.

**How it works:**

1. Claims pending rewards from a staking pool using user certificate
2. Swaps the reward tokens (e.g., FLOW) to stable tokens (e.g., USDC)
3. Deposits the stable tokens to a vault with capacity limits
4. Returns any unconverted tokens back to the user

`_28

// 1. Source: Claim rewards from staking pool

_28

let rewardsSource = IncrementFiStakingConnectors.PoolRewardsSource(

_28

userCertificate: userCert,

_28

poolID: 1,

_28

vaultType: Type<@FlowToken.Vault>(),

_28

overflowSinks: {},

_28

uniqueID: nil

_28

)

_28

_28

// 2. Swapper: Convert rewards to stable token

_28

let swapper = IncrementFiSwapConnectors.Swapper(

_28

path: ["A.FlowToken", "A.USDC"],

_28

inVault: Type<@FlowToken.Vault>(),

_28

outVault: Type<@USDC.Vault>(),

_28

uniqueID: nil

_28

)

_28

_28

// 3. Sink: Deposit stable tokens to vault

_28

let vaultSink = FungibleTokenConnectors.VaultSink(

_28

max: 1000.0,

_28

depositVault: vaultCap,

_28

uniqueID: nil

_28

)

_28

_28

// Execute the workflow

_28

let rewards = rewardsSource.withdrawAvailable(1000.0)

_28

let stableTokens = swapper.swap(nil, inVault: <-rewards)

_28

vaultSink.depositCapacity(from: &stableTokens)`

**Benefits:**

* **Risk Reduction**: Converts volatile reward tokens to stable assets
* **Automation**: Single transaction handles claim, swap, and storage
* **Capital Efficiency**: No manual intervention needed for reward management

### Liquidity Provision & Yield Farming[​](#liquidity-provision--yield-farming "Direct link to Liquidity Provision & Yield Farming")

**Goal**: Convert single token to LP tokens for yield farming

This workflow takes a single token from your vault, converts it into liquidity provider (LP) tokens, and immediately stakes them for yield farming rewards. It combines vault operations, zapping functionality, and staking in one seamless transaction.

**How it works:**

1. Withdraws single token (e.g., FLOW) from vault with minimum balance protection
2. Uses Zapper to split token and create LP position (FLOW/USDC pair)
3. Stakes the resulting LP tokens in a yield farming pool
4. Begins earning rewards on the staked LP position

`_26

// 1. Source: Provide single token (e.g., FLOW)

_26

let flowSource = FungibleTokenConnectors.VaultSource(

_26

min: 100.0,

_26

withdrawVault: flowVaultCap,

_26

uniqueID: nil

_26

)

_26

_26

// 2. Zapper: Convert to LP tokens

_26

let zapper = IncrementFiPoolLiquidityConnectors.Zapper(

_26

token0Type: Type<@FlowToken.Vault>(),

_26

token1Type: Type<@USDC.Vault>(),

_26

stableMode: false,

_26

uniqueID: nil

_26

)

_26

_26

// 3. Sink: Stake LP tokens for rewards

_26

let stakingSink = IncrementFiStakingConnectors.PoolSink(

_26

staker: user.address,

_26

poolID: 2,

_26

uniqueID: nil

_26

)

_26

_26

// Execute the workflow

_26

let flowTokens = flowSource.withdrawAvailable(100.0)

_26

let lpTokens = zapper.swap(nil, inVault: <-flowTokens)

_26

stakingSink.depositCapacity(from: &lpTokens)`

**Benefits:**

* **Yield Optimization**: Converts idle tokens to yield-generating LP positions
* **Single Transaction**: No need for multiple manual steps or approvals
* **Automatic Staking**: LP tokens immediately start earning rewards

### Cross-VM Bridge & Swap[​](#cross-vm-bridge--swap "Direct link to Cross-VM Bridge & Swap")

**Goal**: Bridge tokens from Cadence to EVM, swap them, then bridge back

This workflow demonstrates Flow's unique cross-VM capabilities by bridging tokens from Cadence to Flow EVM, executing a swap using UniswapV2-style routing, and bridging the results back to Cadence. This enables access to EVM-based DEX liquidity while maintaining Cadence token ownership.

**How it works:**

1. Withdraws tokens from Cadence vault with minimum balance protection
2. Bridges tokens from Cadence to Flow EVM environment
3. Executes swap using UniswapV2 router on EVM side
4. Bridges the swapped tokens back to Cadence environment
5. Deposits final tokens to target Cadence vault

`_28

// 1. Source: Cadence vault

_28

let cadenceSource = FungibleTokenConnectors.VaultSource(

_28

min: 50.0,

_28

withdrawVault: cadenceVaultCap,

_28

uniqueID: nil

_28

)

_28

_28

// 2. EVM Swapper: Cross-VM swap

_28

let evmSwapper = UniswapV2SwapConnectors.Swapper(

_28

routerAddress: EVM.EVMAddress(0x...),

_28

path: [tokenA, tokenB],

_28

inVault: Type<@FlowToken.Vault>(),

_28

outVault: Type<@USDC.Vault>(),

_28

coaCapability: coaCap,

_28

uniqueID: nil

_28

)

_28

_28

// 3. Sink: Cadence vault for swapped tokens

_28

let cadenceSink = FungibleTokenConnectors.VaultSink(

_28

max: nil,

_28

depositVault: usdcVaultCap,

_28

uniqueID: nil

_28

)

_28

_28

// Execute the workflow

_28

let cadenceTokens = cadenceSource.withdrawAvailable(50.0)

_28

let evmTokens = evmSwapper.swap(nil, inVault: <-cadenceTokens)

_28

cadenceSink.depositCapacity(from: &evmTokens)`

**Benefits:**

* **Extended Liquidity**: Access to both Cadence and EVM DEX liquidity
* **Cross-VM Arbitrage**: Exploit price differences between VM environments
* **Atomic Execution**: All bridging and swapping happens in single transaction

### Flash Loan Arbitrage[​](#flash-loan-arbitrage "Direct link to Flash Loan Arbitrage")

**Goal**: Borrow tokens, execute arbitrage, repay loan with profit

This advanced strategy uses flash loans to execute risk-free arbitrage by borrowing tokens, exploiting price differences across multiple DEXs, and repaying the loan with interest while keeping the profit. The entire operation happens atomically within a single transaction.

**How it works:**

1. Borrows tokens via flash loan without collateral requirements
2. Uses multi-swapper to find optimal arbitrage routes across DEXs
3. Executes trades to exploit price differences
4. Repays flash loan with fees from arbitrage profits
5. Keeps remaining profit after loan repayment

`_17

// 1. Flasher: Borrow tokens for arbitrage

_17

let flasher = IncrementFiFlashloanConnectors.Flasher(

_17

pairAddress: pairAddress,

_17

type: Type<@FlowToken.Vault>(),

_17

uniqueID: nil

_17

)

_17

_17

// 2. Multi-swapper: Find best arbitrage route

_17

let multiSwapper = SwapConnectors.MultiSwapper(

_17

inVault: Type<@FlowToken.Vault>(),

_17

outVault: Type<@FlowToken.Vault>(),

_17

swappers: [swapper1, swapper2, swapper3],

_17

uniqueID: nil

_17

)

_17

_17

// 3. Execute arbitrage with callback

_17

flasher.flashLoan(1000.0, callback: arbitrageCallback)`

**Benefits:**

* **Zero Capital Required**: No upfront investment needed for arbitrage
* **Risk-Free Profit**: Transaction reverts if arbitrage isn't profitable
* **Market Efficiency**: Helps eliminate price discrepancies across DEXs

## Advanced Workflow Combinations[​](#advanced-workflow-combinations "Direct link to Advanced Workflow Combinations")

### Vault Source + Zapper Integration[​](#vault-source--zapper-integration "Direct link to Vault Source + Zapper Integration")

**Goal**: Withdraw tokens from a vault and convert them to LP tokens in a single transaction

This advanced workflow demonstrates the power of combining VaultSource with Zapper functionality to seamlessly convert idle vault tokens into yield-generating LP positions. The Zapper handles the complex process of splitting the single token and creating balanced liquidity.

![vault source zapper](/assets/images/vaultsource-zapper-e0815ae52689e1c0e031d6319139b1b8.png)

**How it works:**

1. VaultSource withdraws tokens from vault while respecting minimum balance
2. Zapper receives the single token and splits it optimally
3. Zapper swaps a portion of token A to token B using internal DEX routing
4. Zapper provides balanced liquidity (A + B) to the pool
5. Returns LP tokens that represent the liquidity position

`_21

// 1. Create VaultSource with minimum balance protection

_21

let vaultSource = FungibleTokenConnectors.VaultSource(

_21

min: 500.0, // Keep 500 tokens minimum in vault

_21

withdrawVault: flowVaultCapability,

_21

uniqueID: nil

_21

)

_21

_21

// 2. Create Zapper for FLOW/USDC pair

_21

let zapper = IncrementFiPoolLiquidityConnectors.Zapper(

_21

token0Type: Type<@FlowToken.Vault>(), // Input token (A)

_21

token1Type: Type<@USDC.Vault>(), // Paired token (B)

_21

stableMode: false, // Use volatile pair pricing

_21

uniqueID: nil

_21

)

_21

_21

// 3. Execute Vault Source → Zapper workflow

_21

let availableTokens <- vaultSource.withdrawAvailable(maxAmount: 1000.0)

_21

let lpTokens <- zapper.swap(quote: nil, inVault: <-availableTokens)

_21

_21

// Result: LP tokens ready for staking or further DeFi strategies

_21

log("LP tokens created: ".concat(lpTokens.balance.toString()))`

**Benefits:**

* **Capital Efficiency**: Converts idle vault tokens to yield-generating LP positions
* **Automated Balancing**: Zapper handles optimal token split calculations automatically
* **Single Transaction**: Complex multi-step process executed atomically
* **Minimum Protection**: VaultSource ensures vault never goes below safety threshold

### Price-Informed Rebalancing[​](#price-informed-rebalancing "Direct link to Price-Informed Rebalancing")

**Goal**: Create autonomous rebalancing system based on price feeds

This sophisticated workflow creates an autonomous portfolio management system that maintains target value ratios by monitoring real-time price data. The AutoBalancer combines price oracles, sources, and sinks to automatically rebalance positions when they deviate from target thresholds.

**How it works:**

1. Price oracle provides real-time asset valuations with staleness protection
2. AutoBalancer tracks historical deposit values vs current market values
3. When portfolio value exceeds upper threshold (120%), excess is moved to rebalance sink
4. When portfolio value falls below lower threshold (80%), additional funds are sourced
5. System maintains target allocation automatically without manual intervention

`_19

// Create autonomous rebalancing system

_19

let priceOracle = BandOracleConnectors.PriceOracle(

_19

unitOfAccount: Type<@FlowToken.Vault>(),

_19

staleThreshold: 3600, // 1 hour

_19

feeSource: flowTokenSource,

_19

uniqueID: nil

_19

)

_19

_19

let autoBalancer <- FlowActions.createAutoBalancer(

_19

vault: <-initialVault,

_19

lowerThreshold: 0.8,

_19

upperThreshold: 1.2,

_19

source: rebalanceSource,

_19

sink: rebalanceSink,

_19

oracle: priceOracle,

_19

uniqueID: nil

_19

)

_19

_19

autoBalancer.rebalance(force: false) // Autonomous rebalancing`

**Benefits:**

* **Autonomous Operation**: Maintains portfolio balance without manual intervention
* **Risk Management**: Prevents excessive exposure through automated position sizing
* **Market Responsive**: Adapts to price movements using real-time oracle data
* **Threshold Flexibility**: Configurable upper/lower bounds for different risk profiles

### Restake & Compound Strategy[​](#restake--compound-strategy "Direct link to Restake & Compound Strategy")

**Goal**: Automatically compound staking rewards back into the pool

This advanced compounding strategy maximizes yield by automatically claiming staking rewards and converting them back into LP tokens for re-staking. The workflow combines rewards claiming, zapping, and staking into a seamless compound operation that accelerates yield accumulation through reinvestment.

**How it works:**

1. PoolRewardsSource claims accumulated staking rewards from the pool
2. Zapper receives the reward tokens and converts them to LP tokens
3. SwapSource orchestrates the rewards → LP token conversion process
4. PoolSink re-stakes the new LP tokens back into the same pool
5. Compound interest effect increases overall position size and future rewards

`_31

// Restake rewards workflow

_31

let rewardsSource = IncrementFiStakingConnectors.PoolRewardsSource(

_31

poolID: 1,

_31

staker: userAddress,

_31

vaultType: Type<@FlowToken.Vault>(),

_31

overflowSinks: {},

_31

uniqueID: nil

_31

)

_31

_31

let zapper = IncrementFiPoolLiquidityConnectors.Zapper(

_31

token0Type: Type<@FlowToken.Vault>(),

_31

token1Type: Type<@USDC.Vault>(),

_31

stableMode: false,

_31

uniqueID: nil

_31

)

_31

_31

let swapSource = SwapConnectors.SwapSource(

_31

swapper: zapper,

_31

source: rewardsSource,

_31

uniqueID: nil

_31

)

_31

_31

let poolSink = IncrementFiStakingConnectors.PoolSink(

_31

staker: userAddress,

_31

poolID: 1,

_31

uniqueID: nil

_31

)

_31

_31

// Execute compound strategy

_31

let lpTokens <- swapSource.withdrawAvailable(maxAmount: UFix64.max)

_31

poolSink.depositCapacity(from: lpTokens)`

**Benefits:**

* **Compound Growth**: Exponential yield increase through automatic reinvestment
* **Gas Efficiency**: Single transaction handles claim, convert, and re-stake operations
* **Set-and-Forget**: Automated compounding without manual intervention required
* **Optimal Conversion**: Zapper ensures efficient reward token to LP token conversion

## Safety Best Practices[​](#safety-best-practices "Direct link to Safety Best Practices")

### Always Check Capacity[​](#always-check-capacity "Direct link to Always Check Capacity")

Prevents transaction failures and enables graceful handling when sinks reach their maximum capacity limits. This is crucial for automated workflows that might encounter varying capacity conditions.

`_10

// Check before depositing

_10

if sink.depositCapacity(from: &vault) {

_10

sink.depositCapacity(from: &vault)

_10

} else {

_10

// Handle insufficient capacity

_10

}`

### Validate Balances[​](#validate-balances "Direct link to Validate Balances")

Ensures operations behave as expected and helps detect unexpected token loss or gain during complex workflows. Balance validation is essential for financial applications where token accuracy is critical.

`_10

// Verify operations completed successfully

_10

let beforeBalance = vault.balance

_10

sink.depositCapacity(from: &vault)

_10

let afterBalance = vault.balance

_10

_10

assert(afterBalance >= beforeBalance, message: "Balance should not decrease")`

### Use Graceful Degradation[​](#use-graceful-degradation "Direct link to Use Graceful Degradation")

Prevents entire workflows from failing when individual components encounter issues. This approach enables robust strategies that can adapt to changing market conditions or temporary protocol unavailability.

`_10

// Handle failures gracefully

_10

if let result = try? operation.execute() {

_10

// Success path

_10

} else {

_10

// Fallback or no-op

_10

log("Operation failed, continuing with strategy")

_10

}`

### Resource Management[​](#resource-management "Direct link to Resource Management")

Proper resource cleanup prevents token loss and ensures all vaults are properly handled, even when transactions partially fail. This is critical in Cadence where resources must be explicitly managed.

`_10

// Always clean up resources

_10

let vault = source.withdrawAvailable(amount)

_10

defer {

_10

// Ensure vault is properly handled

_10

if vault.balance > 0 {

_10

// Return unused tokens

_10

sourceVault.deposit(from: <-vault)

_10

}

_10

}`

## Testing Your Combinations[​](#testing-your-combinations "Direct link to Testing Your Combinations")

### Unit Testing[​](#unit-testing "Direct link to Unit Testing")

Tests individual connectors in isolation to verify they respect their constraints and behave correctly under various conditions. This catches bugs early and ensures each component works as designed.

`_10

// Test individual components

_10

test("VaultSource should maintain minimum balance") {

_10

let source = VaultSource(min: 100.0, withdrawVault: vaultCap, uniqueID: nil)

_10

_10

// Test minimum balance enforcement

_10

let available = source.minimumAvailable()

_10

assert(available >= 100.0, message: "Should maintain minimum balance")

_10

}`

### Integration Testing[​](#integration-testing "Direct link to Integration Testing")

Validates that multiple connectors work together correctly in complete workflows. This ensures the composition logic is sound and identifies issues that only appear when components interact.

`_11

// Test complete workflows

_11

test("Reward harvesting workflow should complete successfully") {

_11

let workflow = RewardHarvestingWorkflow(

_11

rewardsSource: rewardsSource,

_11

swapper: swapper,

_11

sink: sink

_11

)

_11

_11

let result = workflow.execute()

_11

assert(result.success, message: "Workflow should complete successfully")

_11

}`

### Simulation Testing[​](#simulation-testing "Direct link to Simulation Testing")

Tests strategies under various market conditions using mock data to verify they respond appropriately to price changes, liquidity variations, and other market dynamics. This is essential for strategies that rely on external market data.

`_16

// Test with simulated market conditions

_16

test("Strategy should handle price volatility") {

_16

let strategy = ArbitrageStrategy(

_16

priceOracle: mockPriceOracle,

_16

swapper: mockSwapper

_16

)

_16

_16

// Simulate price changes

_16

mockPriceOracle.setPrice(1.0)

_16

let result1 = strategy.execute()

_16

_16

mockPriceOracle.setPrice(2.0)

_16

let result2 = strategy.execute()

_16

_16

assert(result1 != result2, message: "Strategy should adapt to price changes")

_16

}`

## 📚 Next Steps[​](#-next-steps "Direct link to 📚 Next Steps")

Now that you understand basic combinations, explore:

1. **Advanced Strategies**: Complex multi-step workflows
2. **Risk Management**: Advanced safety and monitoring techniques
3. **Custom Connectors**: Building your own protocol adapters

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to combine Flow Actions primitives to create sophisticated workflows that leverage atomic composition, weak guarantees, and event traceability. You can now create and use Sources, Sinks, Swappers, Price Oracles, and Flashers, while utilizing UniqueIdentifiers to trace operations and compose complex atomic transactions.

Composability is the core strength of Flow Actions. These examples demonstrate how Flow Actions primitives can be combined to create powerful, automated workflows that integrate multiple protocols seamlessly. The framework's standardized interfaces enable developers to chain operations together like LEGO blocks, focusing on strategy implementation rather than protocol-specific integration details.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/flow-actions/basic-combinations.md)

Last updated on **Aug 26, 2025** by **Felipe Cevallos**

[Previous

Connectors](/blockchain-development-tutorials/flow-actions/connectors)[Next

Introduction to Scheduled Callbacks](/blockchain-development-tutorials/flow-actions/scheduled-callbacks-introduction)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)
* [Core Flow Patterns](#core-flow-patterns)
  + [Linear Flow (Source → Swapper → Sink)](#linear-flow-source--swapper--sink)
  + [Bidirectional Flow (Source ↔ Sink)](#bidirectional-flow-source--sink)
  + [Aggregated Flow (Multiple Sources → Aggregator → Sink)](#aggregated-flow-multiple-sources--aggregator--sink)
* [Common DeFi Workflow Combinations](#common-defi-workflow-combinations)
  + [Single Token to LP (Zapper)](#single-token-to-lp-zapper)
  + [Reward Harvesting & Conversion](#reward-harvesting--conversion)
  + [Liquidity Provision & Yield Farming](#liquidity-provision--yield-farming)
  + [Cross-VM Bridge & Swap](#cross-vm-bridge--swap)
  + [Flash Loan Arbitrage](#flash-loan-arbitrage)
* [Advanced Workflow Combinations](#advanced-workflow-combinations)
  + [Vault Source + Zapper Integration](#vault-source--zapper-integration)
  + [Price-Informed Rebalancing](#price-informed-rebalancing)
  + [Restake & Compound Strategy](#restake--compound-strategy)
* [Safety Best Practices](#safety-best-practices)
  + [Always Check Capacity](#always-check-capacity)
  + [Validate Balances](#validate-balances)
  + [Use Graceful Degradation](#use-graceful-degradation)
  + [Resource Management](#resource-management)
* [Testing Your Combinations](#testing-your-combinations)
  + [Unit Testing](#unit-testing)
  + [Integration Testing](#integration-testing)
  + [Simulation Testing](#simulation-testing)
* [📚 Next Steps](#-next-steps)
* [Conclusion](#conclusion)

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