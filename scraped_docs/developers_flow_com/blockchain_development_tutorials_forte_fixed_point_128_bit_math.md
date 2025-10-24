# Source: https://developers.flow.com/blockchain-development-tutorials/forte/fixed-point-128-bit-math

High-Precision Fixed-Point Math | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      + [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

        + [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)

          + [DeFi Math Utils](/blockchain-development-tutorials/forte/fixed-point-128-bit-math)* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Forte Network Upgrade](/blockchain-development-tutorials/forte)* DeFi Math Utils

On this page

# High-Precision Fixed-Point 128 Bit Math

Dealing with decimals is a notorious issue for most developers on other chains, especially when working with DeFi. Blockchains are deterministic systems and floating-point arithmetic is non-deterministic across different compilers and architectures, this is why blockchains use fixed-point arithmetic via integers (scaling numbers by a fixed factor). The issue with this is that these fixed-point integers tend to be very imprecise when using various mathematical operations on them. The more operations you apply to these numbers, the more imprecise these numbers become. However [`DeFiActionsMathUtils`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/utils/DeFiActionsMathUtils.cdc) provides a standardized library for high-precision mathematical operations in DeFi applications on Flow. The contract extends Cadence's native 8-decimal precision (`UFix64`) to 24 decimals using `UInt128` for intermediate calculations, ensuring accuracy in complex financial computations while maintaining deterministic results across the network.

Through integration of this math utility library, developers can ensure that their DeFi protocols perform precise calculations for liquidity pools, yield farming, token swaps, and other financial operations without accumulating rounding errors.

info

While this documentation focuses on DeFi use cases, these mathematical utilities can be used for any application requiring high-precision decimal arithmetic beyond the native 8-decimal limitation of `UFix64`.

## The Precision Problem[​](#the-precision-problem "Direct link to The Precision Problem")

DeFi applications often require multiple sequential calculations, and each operation can introduce rounding errors. When these errors compound over multiple operations, they can lead to:

* Price manipulation vulnerabilities
* Incorrect liquidity calculations
* Unfair token distributions
* Arbitrage opportunities from precision loss

Consider a simple example:

`_10

// Native UFix64 with 8 decimals

_10

let price: UFix64 = 1.23456789 // Actually stored as 1.23456789

_10

let amount: UFix64 = 1000000.0

_10

let fee: UFix64 = 0.003 // 0.3%

_10

_10

// Multiple operations compound rounding errors

_10

let afterFee = amount * (1.0 - fee) // Some precision lost

_10

let output = afterFee * price // More precision lost

_10

let finalAmount = output / someRatio // Even more precision lost`

After 3-4 sequential operations, the cumulative rounding error can be significant, especially when dealing with large amounts. Assuming a rounding error with 8 decimals (1.234567885 rounds up to 1.23456789, causing a rounding error of 0.000000005), then after 100 operations with this error and dealing with 1 million dollars USDF, the protocol is losing $0.5 in revenue from this lack of precision. This might not seem like a lot, but if we consider the TVL of Aave, which is around 40 billion USD, then that loss results in $20,000 USD!

## The Solution: 24-Decimal Precision[​](#the-solution-24-decimal-precision "Direct link to The Solution: 24-Decimal Precision")

[`DeFiActionsMathUtils`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/utils/DeFiActionsMathUtils.cdc) solves this by using `UInt128` to represent fixed-point numbers with 24 decimal places (scaling factor of 10^24). This provides 16 additional decimal places for intermediate calculations, dramatically reducing precision loss.

Note: There is still some precision loss occurring, but it is orders of magnitud smaller than with 8 decimals.

### The Three-Tier Precision System[​](#the-three-tier-precision-system "Direct link to The Three-Tier Precision System")

The contract implements a precision sandwich pattern:

1. **Input Layer**: `UFix64` (8 decimals) - User-facing values
2. **Processing Layer**: `UInt128` (24 decimals) - Internal calculations
3. **Output Layer**: `UFix64` (8 decimals) - Final results with smart rounding

`_13

// Import the contract

_13

import DeFiActionsMathUtils from 'ContractAddress'

_13

_13

// Convert UFix64 to high-precision UInt128

_13

let inputAmount: UFix64 = 1000.12345678

_13

let highPrecision = DeFiActionsMathUtils.toUInt128(inputAmount)

_13

// highPrecision now represents 1000.123456780000000000000000 (24 decimals)

_13

_13

// Perform calculations at 24-decimal precision

_13

let result = DeFiActionsMathUtils.mul(highPrecision, anotherValue)

_13

_13

// Convert back to UFix64 with rounding

_13

let output = DeFiActionsMathUtils.toUFix64Round(result)`

## Core Constants[​](#core-constants "Direct link to Core Constants")

The contract defines several key constants:

`_10

access(all) let e24: UInt128 // 10^24 = 1,000,000,000,000,000,000,000,000

_10

access(all) let e8: UInt128 // 10^8 = 100,000,000

_10

access(all) let decimals: UInt8 // 24`

These constants ensure consistent scaling across all operations.

## Rounding Modes[​](#rounding-modes "Direct link to Rounding Modes")

Smart rounding is the strategic selection of rounding strategies based on the financial context of your calculation. After performing high-precision calculations at 24 decimals, the final results must be converted back to `UFix64` (8 decimals), and how you handle this conversion can protect your protocol from losses, ensure fairness to users, and reduce systematic bias.

[`DeFiActionsMathUtils`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/utils/DeFiActionsMathUtils.cdc) provides four rounding modes, each optimized for specific financial scenarios:

`_13

access(all) enum RoundingMode: UInt8 {

_13

/// Rounds down (floor) - use for payouts

_13

access(all) case RoundDown

_13

_13

/// Rounds up (ceiling) - use for fees/liabilities

_13

access(all) case RoundUp

_13

_13

/// Standard rounding: < 0.5 down, >= 0.5 up

_13

access(all) case RoundHalfUp

_13

_13

/// Banker's rounding: ties round to even number

_13

access(all) case RoundEven

_13

}`

### When to Use Each Mode[​](#when-to-use-each-mode "Direct link to When to Use Each Mode")

**RoundDown** - Choose this when calculating user payouts, withdrawals, or rewards. By rounding down, your protocol retains any fractional amounts, protecting against losses from accumulated rounding errors. This is the conservative choice when funds leave your protocol.

`_10

// When calculating how much to pay out to users

_10

let userReward = DeFiActionsMathUtils.toUFix64RoundDown(calculatedReward)`

**RoundUp** - Use this for protocol fees, transaction costs, or amounts owed to your protocol. Rounding up ensures your protocol collects slightly more, compensating for precision loss and preventing systematic under-collection of fees over many transactions.

`_10

// When calculating fees the protocol collects

_10

let protocolFee = DeFiActionsMathUtils.toUFix64RoundUp(calculatedFee)`

**RoundHalfUp** - Apply this for general-purpose calculations, display values, or when presenting prices to users. This is the familiar rounding method (values 0.5 and above round up, below 0.5 round down) that users expect in traditional finance.

`_10

// For display values or general calculations

_10

let displayValue = DeFiActionsMathUtils.toUFix64Round(calculatedValue)`

**RoundEven** - Select this for scenarios involving many repeated calculations where you want to minimize systematic bias. Also known as "[banker's rounding](https://learn.microsoft.com/en-us/openspecs/microsoft_general_purpose_programming_languages/ms-vbal/98152b5a-4d86-4acb-b875-66cb1f49433e)", this mode rounds ties (exactly 0.5) to the nearest even number, which statistically balances out over many operations, making it ideal for large-scale distributions or statistical calculations.

`_10

// For repeated operations where bias matters

_10

let unbiasedValue = DeFiActionsMathUtils.toUFix64(calculatedValue, DeFiActionsMathUtils.RoundingMode.RoundEven)`

## Core Functions[​](#core-functions "Direct link to Core Functions")

### Conversion Functions[​](#conversion-functions "Direct link to Conversion Functions")

**Converting UFix64 to UInt128**

`_10

access(all) view fun toUInt128(_ value: UFix64): UInt128`

Converts a `UFix64` value to `UInt128` with 24-decimal precision.

**Example:**

`_10

import DeFiActionsMathUtils from 'ContractAddress'

_10

_10

let price: UFix64 = 123.45678900

_10

let highPrecisionPrice = DeFiActionsMathUtils.toUInt128(price)

_10

// highPrecisionPrice = 123456789000000000000000000 (represents 123.45678900... with 24 decimals)`

**Converting UInt128 to UFix64**

`_10

access(all) view fun toUFix64(_ value: UInt128, _ roundingMode: RoundingMode): UFix64

_10

access(all) view fun toUFix64Round(_ value: UInt128): UFix64

_10

access(all) view fun toUFix64RoundDown(_ value: UInt128): UFix64

_10

access(all) view fun toUFix64RoundUp(_ value: UInt128): UFix64`

Converts a `UInt128` value back to `UFix64`, applying the specified rounding strategy.

**Example:**

`_10

let highPrecisionValue: UInt128 = 1234567890123456789012345678

_10

let roundedValue = DeFiActionsMathUtils.toUFix64Round(highPrecisionValue)

_10

// roundedValue = 1234567.89012346 (rounded to 8 decimals using RoundHalfUp)

_10

_10

let flooredValue = DeFiActionsMathUtils.toUFix64RoundDown(highPrecisionValue)

_10

// flooredValue = 1234567.89012345 (truncated to 8 decimals)

_10

_10

let ceilingValue = DeFiActionsMathUtils.toUFix64RoundUp(highPrecisionValue)

_10

// ceilingValue = 1234567.89012346 (rounded up to 8 decimals)`

## High-Precision Arithmetic[​](#high-precision-arithmetic "Direct link to High-Precision Arithmetic")

### Multiplication[​](#multiplication "Direct link to Multiplication")

`_10

access(all) view fun mul(_ x: UInt128, _ y: UInt128): UInt128`

Multiplies two 24-decimal fixed-point numbers, maintaining precision.

**Example:**

`_10

let amount = DeFiActionsMathUtils.toUInt128(1000.0)

_10

let price = DeFiActionsMathUtils.toUInt128(1.5)

_10

_10

let totalValue = DeFiActionsMathUtils.mul(amount, price)

_10

let result = DeFiActionsMathUtils.toUFix64Round(totalValue)

_10

// result = 1500.0`

info

**Important:** The multiplication uses `UInt256` internally to prevent overflow:

`_10

// Internal implementation prevents overflow

_10

return UInt128(UInt256(x) * UInt256(y) / UInt256(e24))`

### Division[​](#division "Direct link to Division")

`_10

access(all) view fun div(_ x: UInt128, _ y: UInt128): UInt128`

Divides two 24-decimal fixed-point numbers, maintaining precision.

**Example:**

`_10

let totalValue = DeFiActionsMathUtils.toUInt128(1500.0)

_10

let shares = DeFiActionsMathUtils.toUInt128(3.0)

_10

_10

let pricePerShare = DeFiActionsMathUtils.div(totalValue, shares)

_10

let result = DeFiActionsMathUtils.toUFix64Round(pricePerShare)

_10

// result = 500.0`

### UFix64 Division with Rounding[​](#ufix64-division-with-rounding "Direct link to UFix64 Division with Rounding")

For convenience, the contract provides direct division functions that handle
conversion and rounding in one call:

`_10

access(all) view fun divUFix64WithRounding(_ x: UFix64, _ y: UFix64): UFix64

_10

access(all) view fun divUFix64WithRoundingUp(_ x: UFix64, _ y: UFix64): UFix64

_10

access(all) view fun divUFix64WithRoundingDown(_ x: UFix64, _ y: UFix64): UFix64`

**Example:**

`_14

let totalAmount: UFix64 = 1000.0

_14

let numberOfUsers: UFix64 = 3.0

_14

_14

// Standard rounding

_14

let perUserStandard = DeFiActionsMathUtils.divUFix64WithRounding(totalAmount, numberOfUsers)

_14

// perUserStandard = 333.33333333

_14

_14

// Round down (conservative for payouts)

_14

let perUserSafe = DeFiActionsMathUtils.divUFix64WithRoundingDown(totalAmount, numberOfUsers)

_14

// perUserSafe = 333.33333333

_14

_14

// Round up (conservative for fees)

_14

let perUserFee = DeFiActionsMathUtils.divUFix64WithRoundingUp(totalAmount, numberOfUsers)

_14

// perUserFee = 333.33333334`

## Common DeFi Use Cases[​](#common-defi-use-cases "Direct link to Common DeFi Use Cases")

### Liquidity Pool Pricing (Constant Product AMM)[​](#liquidity-pool-pricing-constant-product-amm "Direct link to Liquidity Pool Pricing (Constant Product AMM)")

Automated Market Makers like Uniswap use the formula `x * y = k`. Here's how to calculate swap outputs with high precision:

`_35

import DeFiActionsMathUtils from 'ContractAddress'

_35

import FungibleToken from 'FungibleTokenAddress'

_35

_35

access(all) fun calculateSwapOutput(

_35

inputAmount: UFix64,

_35

inputReserve: UFix64,

_35

outputReserve: UFix64,

_35

feeBasisPoints: UFix64 // e.g., 30 for 0.3%

_35

): UFix64 {

_35

// Convert to high precision

_35

let input = DeFiActionsMathUtils.toUInt128(inputAmount)

_35

let reserveIn = DeFiActionsMathUtils.toUInt128(inputReserve)

_35

let reserveOut = DeFiActionsMathUtils.toUInt128(outputReserve)

_35

let fee = DeFiActionsMathUtils.toUInt128(feeBasisPoints)

_35

let basisPoints = DeFiActionsMathUtils.toUInt128(10000.0)

_35

_35

// Calculate: inputWithFee = inputAmount * (10000 - fee)

_35

let feeMultiplier = DeFiActionsMathUtils.div(

_35

basisPoints - fee,

_35

basisPoints

_35

)

_35

let inputWithFee = DeFiActionsMathUtils.mul(input, feeMultiplier)

_35

_35

// Calculate: numerator = inputWithFee * outputReserve

_35

let numerator = DeFiActionsMathUtils.mul(inputWithFee, reserveOut)

_35

_35

// Calculate: denominator = inputReserve + inputWithFee

_35

let denominator = reserveIn + inputWithFee

_35

_35

// Calculate output: numerator / denominator

_35

let output = DeFiActionsMathUtils.div(numerator, denominator)

_35

_35

// Return with conservative rounding (round down for user protection)

_35

return DeFiActionsMathUtils.toUFix64RoundDown(output)

_35

}`

### Compound Interest Calculations[​](#compound-interest-calculations "Direct link to Compound Interest Calculations")

Calculate compound interest for yield farming rewards:

`_30

import DeFiActionsMathUtils from 0xYourAddress

_30

_30

access(all) fun calculateCompoundInterest(

_30

principal: UFix64,

_30

annualRate: UFix64, // e.g., 0.05 for 5%

_30

periodsPerYear: UInt64,

_30

numberOfYears: UFix64

_30

): UFix64 {

_30

// Convert to high precision

_30

let p = DeFiActionsMathUtils.toUInt128(principal)

_30

let r = DeFiActionsMathUtils.toUInt128(annualRate)

_30

let n = DeFiActionsMathUtils.toUInt128(UFix64(periodsPerYear))

_30

let t = DeFiActionsMathUtils.toUInt128(numberOfYears)

_30

let one = DeFiActionsMathUtils.toUInt128(1.0)

_30

_30

// Calculate: rate per period = r / n

_30

let ratePerPeriod = DeFiActionsMathUtils.div(r, n)

_30

_30

// Calculate: (1 + rate per period)

_30

let onePlusRate = one + ratePerPeriod

_30

_30

// Calculate: number of periods = n * t

_30

let totalPeriods = DeFiActionsMathUtils.mul(n, t)

_30

_30

// Note: For production, you'd need to implement a power function

_30

// This is simplified for demonstration

_30

_30

// Calculate final amount with rounding

_30

return DeFiActionsMathUtils.toUFix64Round(finalAmount)

_30

}`

### Proportional Distribution[​](#proportional-distribution "Direct link to Proportional Distribution")

Distribute rewards proportionally among stakeholders:

`_19

import DeFiActionsMathUtils from 0xYourAddress

_19

_19

access(all) fun calculateProportionalShare(

_19

totalRewards: UFix64,

_19

userStake: UFix64,

_19

totalStaked: UFix64

_19

): UFix64 {

_19

// Convert to high precision

_19

let rewards = DeFiActionsMathUtils.toUInt128(totalRewards)

_19

let stake = DeFiActionsMathUtils.toUInt128(userStake)

_19

let total = DeFiActionsMathUtils.toUInt128(totalStaked)

_19

_19

// Calculate: (userStake / totalStaked) * totalRewards

_19

let proportion = DeFiActionsMathUtils.div(stake, total)

_19

let userReward = DeFiActionsMathUtils.mul(proportion, rewards)

_19

_19

// Round down for conservative payout

_19

return DeFiActionsMathUtils.toUFix64RoundDown(userReward)

_19

}`

### Price Impact Calculation[​](#price-impact-calculation "Direct link to Price Impact Calculation")

Calculate the price impact of a large trade:

`_29

import DeFiActionsMathUtils from 0xYourAddress

_29

_29

access(all) fun calculatePriceImpact(

_29

inputAmount: UFix64,

_29

inputReserve: UFix64,

_29

outputReserve: UFix64

_29

): UFix64 {

_29

// Convert to high precision

_29

let input = DeFiActionsMathUtils.toUInt128(inputAmount)

_29

let reserveIn = DeFiActionsMathUtils.toUInt128(inputReserve)

_29

let reserveOut = DeFiActionsMathUtils.toUInt128(outputReserve)

_29

_29

// Calculate initial price: outputReserve / inputReserve

_29

let initialPrice = DeFiActionsMathUtils.div(reserveOut, reserveIn)

_29

_29

// Calculate new reserves after trade

_29

let newReserveIn = reserveIn + input

_29

let k = DeFiActionsMathUtils.mul(reserveIn, reserveOut)

_29

let newReserveOut = DeFiActionsMathUtils.div(k, newReserveIn)

_29

_29

// Calculate final price: newOutputReserve / newInputReserve

_29

let finalPrice = DeFiActionsMathUtils.div(newReserveOut, newReserveIn)

_29

_29

// Calculate impact: (initialPrice - finalPrice) / initialPrice

_29

let priceDiff = initialPrice - finalPrice

_29

let impact = DeFiActionsMathUtils.div(priceDiff, initialPrice)

_29

_29

return DeFiActionsMathUtils.toUFix64Round(impact)

_29

}`

## Benefits of High-Precision Math[​](#benefits-of-high-precision-math "Direct link to Benefits of High-Precision Math")

### Precision Preservation[​](#precision-preservation "Direct link to Precision Preservation")

The 24-decimal precision provides headroom for complex calculations:

`_10

// Chain multiple operations without significant precision loss

_10

let step1 = DeFiActionsMathUtils.mul(valueA, valueB)

_10

let step2 = DeFiActionsMathUtils.div(step1, valueC)

_10

let step3 = DeFiActionsMathUtils.mul(step2, valueD)

_10

let step4 = DeFiActionsMathUtils.div(step3, valueE)

_10

// Still maintains 24 decimals of precision until final conversion`

### Overflow Protection[​](#overflow-protection "Direct link to Overflow Protection")

The contract uses `UInt256` for intermediate multiplication to prevent overflow:

`_10

// Internal implementation protects against overflow

_10

access(all) view fun mul(_ x: UInt128, _ y: UInt128): UInt128 {

_10

return UInt128(UInt256(x) * UInt256(y) / UInt256(self.e24))

_10

}`

And includes explicit bounds checking when converting to `UFix64`:

`_10

access(all) view fun assertWithinUFix64Bounds(_ value: UInt128) {

_10

let MAX_1E24: UInt128 = 184_467_440_737_095_516_150_000_000_000_000_000

_10

assert(

_10

value <= MAX_1E24,

_10

message: "Value exceeds UFix64.max"

_10

)

_10

}`

## Best Practices[​](#best-practices "Direct link to Best Practices")

Always Use High Precision for Intermediate Calculations

**❌ Low precision (loses ~$0.50 per 1M USDC):**

`_10

let fee: UFix64 = amount * 0.003

_10

let afterFee: UFix64 = amount - fee

_10

let output: UFix64 = afterFee * price`

**✅ High precision (safe and accurate):**

`_11

// Convert once at the start

_11

let amountHP = DeFiActionsMathUtils.toUInt128(amount)

_11

let feeRate = DeFiActionsMathUtils.toUInt128(0.003)

_11

let priceHP = DeFiActionsMathUtils.toUInt128(price)

_11

_11

// Perform all calculations at high precision

_11

let afterFeeHP = DeFiActionsMathUtils.mul(amountHP, DeFiActionsMathUtils.toUInt128(1.0) - feeRate)

_11

let outputHP = DeFiActionsMathUtils.mul(afterFeeHP, priceHP)

_11

_11

// Convert once at the end with smart rounding

_11

let output = DeFiActionsMathUtils.toUFix64RoundDown(outputHP)`

The pattern is simple: **convert → calculate → convert back**. The extra lines give you production-grade precision that protects your protocol from financial losses.

Always validate that inputs are within acceptable ranges:

`_10

access(all) fun swap(inputAmount: UFix64) {

_10

pre {

_10

inputAmount > 0.0: "Amount must be positive"

_10

inputAmount <= 1000000.0: "Amount exceeds maximum"

_10

}

_10

_10

let inputHP = DeFiActionsMathUtils.toUInt128(inputAmount)

_10

// ... perform calculations

_10

}`

## More Resources[​](#more-resources "Direct link to More Resources")

* [View the DeFiActionsMathUtils source code](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/utils/DeFiActionsMathUtils.cdc)
* [Flow DeFi Actions Documentation](https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions)
* [Cadence Fixed-Point Numbers](https://cadence-lang.org/docs/language/values-and-types/fixed-point-nums-ints)

## Key takeaways[​](#key-takeaways "Direct link to Key takeaways")

* Use high precision (24 decimals) for all intermediate calculations
* Convert to `UFix64` only for final results
* Choose appropriate rounding modes based on your use case
* Always validate inputs and test edge cases
* Document your rounding decisions for maintainability

## Conclusion[​](#conclusion "Direct link to Conclusion")

[`DeFiActionsMathUtils`](https://github.com/onflow/FlowActions/blob/main/cadence/contracts/utils/DeFiActionsMathUtils.cdc) gives Flow developers a significant advantage in building DeFi applications. With 24-decimal precision, it is orders of magnitude more accurate than typical blockchain implementations (which use 6-18 decimals). The standardized library eliminates the need to build custom math implementations.

The simple **convert → calculate → convert back** pattern, combined with strategic rounding modes and built-in overflow protection, means you can focus on your protocol's business logic instead of low-level precision handling. At scale, this protection prevents thousands of dollars in losses from accumulated rounding errors.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/fixed-point-128-bit-math.md)

Last updated on **Oct 21, 2025** by **0xLisanAlGaib**

[Previous

Introduction to Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction)[Next

Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

###### Rate this page

😞😐😊

Copy as Markdown

* [The Precision Problem](#the-precision-problem)* [The Solution: 24-Decimal Precision](#the-solution-24-decimal-precision)
    + [The Three-Tier Precision System](#the-three-tier-precision-system)* [Core Constants](#core-constants)* [Rounding Modes](#rounding-modes)
        + [When to Use Each Mode](#when-to-use-each-mode)* [Core Functions](#core-functions)
          + [Conversion Functions](#conversion-functions)* [High-Precision Arithmetic](#high-precision-arithmetic)
            + [Multiplication](#multiplication)+ [Division](#division)+ [UFix64 Division with Rounding](#ufix64-division-with-rounding)* [Common DeFi Use Cases](#common-defi-use-cases)
              + [Liquidity Pool Pricing (Constant Product AMM)](#liquidity-pool-pricing-constant-product-amm)+ [Compound Interest Calculations](#compound-interest-calculations)+ [Proportional Distribution](#proportional-distribution)+ [Price Impact Calculation](#price-impact-calculation)* [Benefits of High-Precision Math](#benefits-of-high-precision-math)
                + [Precision Preservation](#precision-preservation)+ [Overflow Protection](#overflow-protection)* [Best Practices](#best-practices)* [More Resources](#more-resources)* [Key takeaways](#key-takeaways)* [Conclusion](#conclusion)

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