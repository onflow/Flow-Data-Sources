# Source: https://developers.flow.com/ecosystem/defi-liquidity/band-oracle

Band Oracle on Flow | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Ecosystem Index](/ecosystem)* [Developer Support Hub](/ecosystem/developer-support-hub)

    * [Flow Block Explorers](/ecosystem/block-explorers)* [Hackathons and Events](/ecosystem/hackathons-and-events)* [Data Indexers](/ecosystem/data-indexers)* [Developer Profile](/ecosystem/developer-profile)* [Wallets](/ecosystem/wallets)* [DeFi & Liquidity](/ecosystem/defi-liquidity)

                + [Build with Forte ↙](/ecosystem/defi-liquidity/forte)+ [DeFi Contracts Mainnet](/ecosystem/defi-liquidity/defi-contracts-mainnet)+ [DeFi Contracts Testnet](/ecosystem/defi-liquidity/defi-contracts-testnet)+ [Cross-chain swaps on Flow EVM](/ecosystem/defi-liquidity/cross-chain-swaps)+ [Add Token To MetaMask](/ecosystem/defi-liquidity/add-token-to-metamask)+ [Stablecoins & Bridges FAQ](/ecosystem/defi-liquidity/faq)+ [Band Oracle](/ecosystem/defi-liquidity/band-oracle)* [Faucets](/ecosystem/faucets)* [Bridges](/ecosystem/bridges)* [Collectibles & NFTs](/ecosystem/collectibles)* [Community Projects](/ecosystem/projects)* [Auditors](/ecosystem/auditors)

* * [DeFi & Liquidity](/ecosystem/defi-liquidity)* Band Oracle

On this page

# Band Oracle with Cadence

The Band Protocol Oracle contract enables Flow blockchain applications to access real-time price data from the [Band Protocol Oracle network](https://faq.bandprotocol.com/). The oracle provides a comprehensive set of cryptocurrency and fiat currency price quotes from the Band Standard Dataset, making them available to any Cadence application, contract, or transaction.

## Contract Addresses[​](#contract-addresses "Direct link to Contract Addresses")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Address [CLI](https://developers.flow.com/build/tools/flow-cli/dependency-manager) Explorer|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Testnet `0x9fb6606c300b5051` [View Contract](https://testnet.flowscan.io/contract/A.9fb6606c300b5051.BandOracle)| Mainnet `0x6801a6222ebf784a` [View Contract](https://flowscan.io/contract/A.6801a6222ebf784a.BandOracle) | | | | | | | | | | | |

## Supported Symbols[​](#supported-symbols "Direct link to Supported Symbols")

### Cryptocurrency Pairs (against USD)[​](#cryptocurrency-pairs-against-usd "Direct link to Cryptocurrency Pairs (against USD)")

* **Major**: ETH, FLOW, USDC, USDT, WBTC, BNB, XRP, ADA, DOGE, POL (MATIC)
* **Layer 1**: SOL, DOT, AVAX, ATOM, XLM, TRX, SUI
* **DeFi**: AAVE, LINK, CRV, OP, UNI, SUSHI, CAKE, DYDX, 1INCH, BAT
* **Others**: LTC, SHIB, DAI, FTM

### Fiat Currency Pairs (against USD)[​](#fiat-currency-pairs-against-usd "Direct link to Fiat Currency Pairs (against USD)")

* **Asian**: KRW, INR, HKD, TWD, THB, JPY, MYR, PHP, CNY, SGD
* **European**: PLN, CZK, EUR, GBP, CHF, RUB, SEK, TRY
* **Americas**: BRL, CAD
* **Oceanic**: AUD, NZD

## How It Works[​](#how-it-works "Direct link to How It Works")

### Architecture[​](#architecture "Direct link to Architecture")

The Band Oracle contract maintains a decentralized price feed system with three key components:

1. **Data Storage**: Price data is stored in a contract-level dictionary `symbolsRefData: {String: RefData}` where each symbol maps to its latest price information.
2. **Data Updates**: Authorized BandChain relayers continuously update price data from the Band Protocol network to keep prices current.
3. **Data Access**: Any user or contract can query the latest price data through public functions, enabling real-time price integrations.

### Data Structure[​](#data-structure "Direct link to Data Structure")

Price data is stored using the `RefData` struct:

`_10

access(all) struct RefData {

_10

// USD-rate, multiplied by 1e9

_10

access(all) var rate: UInt64

_10

// UNIX epoch when data was last resolved

_10

access(all) var timestamp: UInt64

_10

// BandChain request identifier for this data

_10

access(all) var requestID: UInt64

_10

}`

When querying prices, you receive a `ReferenceData` struct:

`_10

access(all) struct ReferenceData {

_10

// Rate as integer multiplied by 1e18

_10

access(all) var integerE18Rate: UInt256

_10

// Rate as a fixed-point decimal

_10

access(all) var fixedPointRate: UFix64

_10

// Timestamp of base symbol data

_10

access(all) var baseTimestamp: UInt64

_10

// Timestamp of quote symbol data

_10

access(all) var quoteTimestamp: UInt64

_10

}`

### Data Normalization[​](#data-normalization "Direct link to Data Normalization")

All price data is stored with a USD conversion rate. When you query for price conversions between two non-USD symbols, the contract derives the rate from their respective USD rates. For example, to get ETH/EUR, the contract calculates: `(ETH/USD) / (EUR/USD)`.

## Features[​](#features "Direct link to Features")

### Price Queries[​](#price-queries "Direct link to Price Queries")

* Query any supported symbol pair in real-time
* Get both integer (e18 precision) and fixed-point decimal rates
* Access timestamp information to verify data freshness
* Track BandChain request IDs for transparency

### Fee Structure[​](#fee-structure "Direct link to Fee Structure")

* Configurable fee system for oracle usage (currently set to zero)
* Fee collected in FLOW tokens
* Query current fee using `BandOracle.getFee()`

### Event Monitoring[​](#event-monitoring "Direct link to Event Monitoring")

The contract emits events to notify applications of updates:

`_10

// Emitted when symbol prices are updated

_10

access(all) event BandOracleSymbolsUpdated(

_10

symbols: [String],

_10

relayerID: UInt64,

_10

requestID: UInt64

_10

)

_10

_10

// Emitted when a symbol is removed

_10

access(all) event BandOracleSymbolRemoved(symbol: String)`

## Usage Guide[​](#usage-guide "Direct link to Usage Guide")

### Basic Price Query (Transaction)[​](#basic-price-query-transaction "Direct link to Basic Price Query (Transaction)")

To query price data from a transaction:

`_32

import "BandOracle"

_32

import "FlowToken"

_32

import "FungibleToken"

_32

_32

transaction(baseSymbol: String, quoteSymbol: String) {

_32

_32

let payment: @{FungibleToken.Vault}

_32

_32

prepare(acct: auth(BorrowValue) &Account) {

_32

// Borrow reference to user's FLOW vault

_32

let vaultRef = acct.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(

_32

from: /storage/flowTokenVault

_32

) ?? panic("Cannot borrow reference to signer's FLOW vault")

_32

_32

// Withdraw payment for oracle fee

_32

self.payment <- vaultRef.withdraw(amount: BandOracle.getFee())

_32

}

_32

_32

execute {

_32

// Get reference data

_32

let priceData = BandOracle.getReferenceData(

_32

baseSymbol: baseSymbol,

_32

quoteSymbol: quoteSymbol,

_32

payment: <- self.payment

_32

)

_32

_32

log("Rate (fixed-point): ".concat(priceData.fixedPointRate.toString()))

_32

log("Rate (integer e18): ".concat(priceData.integerE18Rate.toString()))

_32

log("Base timestamp: ".concat(priceData.baseTimestamp.toString()))

_32

log("Quote timestamp: ".concat(priceData.quoteTimestamp.toString()))

_32

}

_32

}`

### Example: ETH/USD Price[​](#example-ethusd-price "Direct link to Example: ETH/USD Price")

`_10

// Get ETH price in USD

_10

let priceData = BandOracle.getReferenceData(

_10

baseSymbol: "ETH",

_10

quoteSymbol: "USD",

_10

payment: <- flowPayment

_10

)

_10

// priceData.fixedPointRate contains ETH price in USD`

### Example: Cross-Currency Conversion[​](#example-cross-currency-conversion "Direct link to Example: Cross-Currency Conversion")

`_10

// Get EUR price in JPY

_10

let priceData = BandOracle.getReferenceData(

_10

baseSymbol: "EUR",

_10

quoteSymbol: "JPY",

_10

payment: <- flowPayment

_10

)

_10

// priceData.fixedPointRate contains EUR/JPY exchange rate`

### Contract Integration[​](#contract-integration "Direct link to Contract Integration")

Here's how to integrate the oracle into your smart contract:

`_44

import "BandOracle"

_44

import "FlowToken"

_44

import "FungibleToken"

_44

_44

access(all) contract MyDeFiContract {

_44

_44

// Store a vault to pay for oracle fees

_44

access(self) let oracleFeeVault: @{FungibleToken.Vault}

_44

_44

access(all) fun getTokenPriceInUSD(tokenSymbol: String): UFix64 {

_44

// Withdraw payment for oracle

_44

let payment <- self.oracleFeeVault.withdraw(

_44

amount: BandOracle.getFee()

_44

)

_44

_44

// Query the oracle

_44

let priceData = BandOracle.getReferenceData(

_44

baseSymbol: tokenSymbol,

_44

quoteSymbol: "USD",

_44

payment: <- payment

_44

)

_44

_44

return priceData.fixedPointRate

_44

}

_44

_44

access(all) fun swapTokens(amount: UFix64, maxPrice: UFix64) {

_44

// Get current price

_44

let currentPrice = self.getTokenPriceInUSD(tokenSymbol: "ETH")

_44

_44

// Verify price is acceptable

_44

if currentPrice > maxPrice {

_44

panic("Price too high")

_44

}

_44

_44

// Proceed with swap logic...

_44

}

_44

_44

init() {

_44

// Initialize vault for oracle fees

_44

self.oracleFeeVault <- FlowToken.createEmptyVault(

_44

vaultType: Type<@FlowToken.Vault>()

_44

)

_44

}

_44

}`

## Best Practices[​](#best-practices "Direct link to Best Practices")

### 1. Listen for Price Updates[​](#1-listen-for-price-updates "Direct link to 1. Listen for Price Updates")

Monitor the `BandOracleSymbolsUpdated` event to keep your contract's stored prices up-to-date:

`_10

// Listen for this event in your application

_10

access(all) event BandOracleSymbolsUpdated(

_10

symbols: [String],

_10

relayerID: UInt64,

_10

requestID: UInt64

_10

)`

When you detect an update for symbols your app uses, trigger a transaction to refresh your stored prices.

## Advanced Features[​](#advanced-features "Direct link to Advanced Features")

### Converting Between Number Formats[​](#converting-between-number-formats "Direct link to Converting Between Number Formats")

The contract provides a utility function to convert between integer and fixed-point representations:

`_10

// Convert e18 integer to fixed-point decimal

_10

let fixedPoint = BandOracle.e18ToFixedPoint(rate: integerE18Rate)`

### Fee Management[​](#fee-management "Direct link to Fee Management")

For contract administrators, the oracle supports dynamic fee configuration:

`_10

// Query current fee

_10

let currentFee = BandOracle.getFee()

_10

_10

// Fee can be updated by the fee collector (admin only)

_10

// feeCollector.setFee(fee: 0.001) // 0.001 FLOW per query`

## Resources[​](#resources "Direct link to Resources")

* [Band Protocol FAQ](https://faq.bandprotocol.com/)
* [Band Standard Dataset](https://data.bandprotocol.com/)
* [Cadence Language Reference](https://cadence-lang.org/)

---

**Note**: The oracle currently charges no fees for usage, but this may change in the future. Always check `BandOracle.getFee()` before querying to ensure your contract has sufficient FLOW tokens allocated.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/ecosystem/defi-liquidity/band-oracle.md)

Last updated on **Oct 10, 2025** by **Chase Fleming**

[Previous

Stablecoins & Bridges FAQ](/ecosystem/defi-liquidity/faq)[Next

Faucets](/ecosystem/faucets)

###### Rate this page

😞😐😊

Copy as Markdown

* [Contract Addresses](#contract-addresses)* [Supported Symbols](#supported-symbols)
    + [Cryptocurrency Pairs (against USD)](#cryptocurrency-pairs-against-usd)+ [Fiat Currency Pairs (against USD)](#fiat-currency-pairs-against-usd)* [How It Works](#how-it-works)
      + [Architecture](#architecture)+ [Data Structure](#data-structure)+ [Data Normalization](#data-normalization)* [Features](#features)
        + [Price Queries](#price-queries)+ [Fee Structure](#fee-structure)+ [Event Monitoring](#event-monitoring)* [Usage Guide](#usage-guide)
          + [Basic Price Query (Transaction)](#basic-price-query-transaction)+ [Example: ETH/USD Price](#example-ethusd-price)+ [Example: Cross-Currency Conversion](#example-cross-currency-conversion)+ [Contract Integration](#contract-integration)* [Best Practices](#best-practices)
            + [1. Listen for Price Updates](#1-listen-for-price-updates)* [Advanced Features](#advanced-features)
              + [Converting Between Number Formats](#converting-between-number-formats)+ [Fee Management](#fee-management)* [Resources](#resources)

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