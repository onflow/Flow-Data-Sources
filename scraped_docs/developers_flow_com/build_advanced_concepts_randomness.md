# Source: https://developers.flow.com/build/advanced-concepts/randomness

Flow On-chain Randomness in Cadence | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)

  + [Account Abstraction](/build/advanced-concepts/account-abstraction)
  + [FLIX (Flow Interaction Templates)](/build/advanced-concepts/flix)
  + [NFT Metadata Views](/build/advanced-concepts/metadata-views)
  + [VRF (Randomness) in Cadence](/build/advanced-concepts/randomness)
  + [Scaling Transactions from a Single Account](/build/advanced-concepts/scaling)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Advanced Concepts
* VRF (Randomness) in Cadence

On this page

# Randomness on FLOW

Flow enhances blockchain functionality and eliminates reliance on external oracles by providing native onchain randomness at the protocol level. This secure, decentralized feature empowers developers to build a variety of applications with truly unpredictable, transparent, and fair outcomes, achieved with greater efficiency.

Flow's onchain randomness delivers immediate random values within smart contracts, bypassing the latency and complexity of oracle integration. Developers can obtain verifiably random results with a single line of Cadence code, streamlining the development process and enhancing the performance of decentralized applications.

## Use Cases of Onchain Randomness[​](#use-cases-of-onchain-randomness "Direct link to Use Cases of Onchain Randomness")

* **Gaming:** Integrates fairness and unpredictability into gameplay, enhancing user engagement without delays.
* **NFTs:** Facilitates the creation of uniquely randomized traits in NFTs quickly, adding to their rarity and value.
* **Lotteries & Draws:** Offers instant and verifiably fair random selection for lotteries, solidifying trust in real-time.
* **DeFi Protocols:** Enables rapid and innovative random reward systems within decentralized finance.
* **DAOs:** Assists in unbiased voting and task assignments through immediate randomness.
* **Broad Applications:** Extends to any domain requiring impartial randomization, from asset distribution to security mechanisms, all with the added benefit of on-demand availability.

## History of the Distributed Randomness Beacon[​](#history-of-the-distributed-randomness-beacon "Direct link to History of the Distributed Randomness Beacon")

Within the Flow protocol, the heart of randomness generation lies in the "Distributed Randomness Beacon".
This module generates randomness that is distributed across the network while adhering to established cryptographic and security standards.
The output from the randomness beacon is a random source for each block that is unpredictable and impartial.

For over three years, the beacon has ensured protocol security by selecting which consensus node gets to propose the next block and assigning verification nodes to oversee block computations. For those interested in a more detailed exploration of the randomness beacon and its inner workings, you can read [the technical deep dive on the Flow forum](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110).

### The History and Limitations of `unsafeRandom` (Now Deprecated)[​](#the-history-and-limitations-of-unsaferandom-now-deprecated "Direct link to the-history-and-limitations-of-unsaferandom-now-deprecated")

Cadence has historically provided the `unsafeRandom` function to return a pseudo-random number. The stream of random numbers produced was potentially unsafe in the following two regards:

1. The sequence of random numbers is potentially predictable by transactions within the same block and by other smart contracts calling into your smart contract.
2. A transaction calling into your smart contract can potentially bias the sequence of random numbers which your smart contract internally generates. Currently, the block hash seeds `unsafeRandom`. Consensus nodes can *easily* bias the block hash and **influence the seed for `unsafeRandom`**.

warning

⚠️ Note `unsafeRandom` is deprecated since the Cadence 1.0 release.

## Guidelines for Safe Usage[​](#guidelines-for-safe-usage "Direct link to Guidelines for Safe Usage")

For usage of randomness where result abortion is not an issue, it is recommended to use the Cadence built-in function `revertibleRandom.` `revertibleRandom` returns a pseudo-random number and is based on the Distributed Randomness Beacon.

`_10

// Language reference:

_10

// https://cadence-lang.org/docs/language/built-in-functions#revertiblerandom

_10

// Run the snippet here: https://academy.ecdao.org/en/snippets/cadence-random

_10

access(all) fun main(): UInt64 {

_10

// Simple assignment using revertibleRandom - keep reading docs for safe usage!

_10

let rand: UInt64 = revertibleRandom()

_10

return rand

_10

}`

It is notable that the random number generation process is unpredictable (for miners unpredictable at block construction time and for cadence logic unpredictable at time of call), verifiable, uniform, as well as safe from bias by miners and previously-running Cadence code.

Protocol improvements (documented in [FLIP 120](https://github.com/onflow/flips/blob/main/cadence/20230713-random-function.md))
expose the randomness beacon to the FVM and Cadence where it can be used to draw safe randoms without latency.

Although Cadence exposes safe randomness generated by the Flow protocol via `revertibleRandom`, there is an additional safety-relevant aspect that developers need to be mindful about.

The `revertibleRandom` function can be used safely in some applications where the transaction results are *not* deliberately reverted after the random number is revealed (i.e. a trusted contract distributing random NFTs to registered users or onchain lucky draw).
However, if applications require a non-trusted party (for instance app users) to submit a transaction calling a randomized (non-deterministic) contract, the developer must explicitly protect the stream of random numbers to not break the security guarantees:

warning

🚨 A transaction can atomically revert all its action during its runtime and abort. Therefore, it is possible for a transaction calling into your smart contract to post-select favorable results and revert the transaction for unfavorable results.

In other words, transactions submitted by a non-trusted party are able to reject their results after the random is revealed.

info

**Post-selection** - the ability for transactions to reject results they don't like - is inherent to any smart contract platform that allows transactions to roll back atomically. See this very similar [Ethereum example](https://consensys.github.io/smart-contract-best-practices/development-recommendations/general/public-data/).

The central aspect that a contract developer needs to think about is the following scenario:

* Imagine an adversarial user that is sending a transaction that calls your smart contract.
* The transaction includes code that runs after your smart contract returns and inspects the outcome.
* If the outcome is unfavorable (based on some criteria codified in the transaction), the transaction aborts itself.

As an example, consider a simple coin toss randomized contract where users can bet any amount of tokens against a random binary output. If the coin toss contract outputs `1`, the user doubles their bet. If the coin toss contract outputs `0`, the user loses their bet in favor of the coin toss.

Although the user (or the honest coin toss contract) cannot predict or bias the outcome, the user transaction can check the randomized result and cancel the transaction if they are losing their bet. This can be done by calling an exception causing the transaction to error. All temporary state changes are cancelled and the user can repeat the process till they double their bet.

## Commit-Reveal Scheme[​](#commit-reveal-scheme "Direct link to Commit-Reveal Scheme")

The recommended way to mitigate the problems above is via a commit-reveal scheme. The scheme involves two steps: commit and reveal. During the commit phase, the user transaction commits to accepting the future output of a smart contract where the last remaining input is an unknown random source. The smart contract stores this commitment on the blockchain. At the current level of optimization, the reveal phase can start as early as the next block, when the "future" beacon's source of randomness becomes available. The reveal phase can be executed at any block after that, now that the commitment to a past block is stored on-chain. With a second transaction, the smart contract can be executed to explicitly generate the random outputs.

There are ideas how to further optimize the developer experience in the future. For example, a transaction could delegate part of its gas to an independent transaction it spawns. Conceptually, also this future solution would be a commit-and-reveal scheme, just immediately happening within the same block. Until we eventually get to this next level, developers may need to implement their own commit-reveal. In Cadence, it is clean and short.

### FLIP 123[​](#flip-123 "Direct link to FLIP 123")

On Flow, we have absorbed all security complexity into the platform.

[FLIP 123: On-chain Random beacon history for commit-reveal schemes](https://github.com/onflow/flips/blob/main/protocol/20230728-commit-reveal.md#flip-123-on-chain-random-beacon-history-for-commit-reveal-schemes) was introduced to provide a safe pattern to use randomness in transactions so that it's not possible to revert unfavorable randomized transaction results.
We recommend this approach as a best-practice example for implementing a commit-reveal scheme in Cadence. The `RandomBeaconHistory` contract provides a convenient archive, where for each past block height (starting Nov 2023) the respective "source of randomness" can be retrieved. The `RandomBeaconHistory` contract is automatically executed by the system at each block to store the next source of randomness value.

info

While the commit-and-reveal scheme mitigates post-selection of results by adversarial clients, Flow's secure randomness additionally protects against any pre-selection vulnerabilities (like biasing attacks by byzantine miners).

A commit-reveal scheme can be implemented as follows. The coin toss example described earlier will be used for illustration:

* When a user submits a bidding transaction, the bid amount is transferred to the coin toss contract, and the block height where the bid was made is stored. This is a commitment by the user to use the SoR at the current block. Note that the current block's `SoR_A` isn't known to the transaction execution environment, and therefore the transaction has no way to inspect the random outcome and predict the coin toss result. The current block's `SoR_A` is only available once added to the history core-contract, which only happens at the end of the block's execution. The user may also commit to using an SoR of some future block, which is equally unknown at the time the bid is made.
* The coin toss contract may grant the user a limited window of time (i.e a block height range) to send a second transaction for resolving the results and claim any winnings. Failing to do so, the bid amount remains in the coin toss contract.
* Within that reveal transaction, the user calls the coin toss contract, looks us up the block height at which the block was committed and checks that it has already passed. The contract queries that block's `SoR_A` from the core-contract `RandomBeaconHistory` via block height.
* The coin toss contract uses a PRG seeded with the queried `SoR_A` and diversified using a specific information to the use-case (a user ID or resource ID for instance). Diversification does not add new entropy, but it avoids generating the same outcome for different use-cases. If a diversifier (or salt) isn't used, all users that committed a bid on the same block would either win or lose.
* The PRG is used to generate the random result and resolve the bid. Note that the user can make the transaction abort after inspecting a losing result. However, the bid amount would be lost anyway when the allocated window expires.

The following lines of code illustrate a random coin toss that cannot be gamed or biased. The reveal-and-commit scheme prevent clients from post-selecting favorable outcomes.

`_54

// The code below is taken from the example CoinToss contract found in this project repo

_54

// Source: https://github.com/onflow/random-coin-toss

_54

_54

/// --- Commit ---

_54

/// In this method, the caller commits a bet. The contract takes note of the

_54

/// block height and bet amount, returning a Receipt resource which is used

_54

/// by the better to reveal the coin toss result and determine their winnings.

_54

access(all) fun commitCoinToss(bet: @FungibleToken.Vault): @Receipt {

_54

let receipt <- create Receipt(

_54

betAmount: bet.balance

_54

)

_54

// commit the bet

_54

// `self.reserve` is a `@FungibleToken.Vault` field defined on the app contract

_54

// and represents a pool of funds

_54

self.reserve.deposit(from: <-bet)

_54

_54

emit CoinTossBet(betAmount: receipt.betAmount, commitBlock: receipt.commitBlock, receiptID: receipt.uuid)

_54

_54

return <- receipt

_54

}

_54

_54

/// --- Reveal ---

_54

/// Here the caller provides the Receipt given to them at commitment. The contract

_54

/// then "flips a coin" with randomCoin(), providing the committed block height

_54

/// and salting with the Receipts unique identifier.

_54

/// If result is 1, user loses, if it's 0 the user doubles their bet.

_54

/// Note that the caller could condition the revealing transaction, but they've

_54

/// already provided their bet amount so there's no loss for the contract if

_54

/// they do

_54

access(all) fun revealCoinToss(receipt: @Receipt): @FungibleToken.Vault {

_54

pre {

_54

receipt.commitBlock <= getCurrentBlock().height: "Cannot reveal before commit block"

_54

}

_54

_54

let betAmount = receipt.betAmount

_54

let commitBlock = receipt.commitBlock

_54

let receiptID = receipt.uuid

_54

// self.randomCoin() errors if commitBlock <= current block height in call to

_54

// RandomBeaconHistory.sourceOfRandomness()

_54

let coin = self.randomCoin(atBlockHeight: receipt.commitBlock, salt: receipt.uuid)

_54

_54

destroy receipt

_54

_54

if coin == 1 {

_54

emit CoinTossReveal(betAmount: betAmount, winningAmount: 0.0, commitBlock: commitBlock, receiptID: receiptID)

_54

return <- FlowToken.createEmptyVault()

_54

}

_54

_54

let reward <- self.reserve.withdraw(amount: betAmount * 2.0)

_54

_54

emit CoinTossReveal(betAmount: betAmount, winningAmount: reward.balance, commitBlock: commitBlock, receiptID: receiptID)

_54

_54

return <- reward

_54

}`

### Which random function should be used:[​](#which-random-function-should-be-used "Direct link to Which random function should be used:")

While both are backed by Flow's Randomness Beacon it is important for developers to mindfully choose between `revertibleRandom` or
seeding their own PRNG utilizing the `RandomBeaconHistory` smart contract:

* With `revertibleRandom` a developer is calling the transaction environment,
  which has the power to abort and revert if it doesn't like `revertibleRandom`'s outputs.
  `revertibleRandom` is only suitable for smart contract functions that exclusively run within the trusted transactions.
* In contrast, the `RandomBeaconHistory` contract is key for effectively implementing a commit-reveal scheme, where the transaction is non-trusted and may revert the random outputs.
  During the commit phase, the user commits to proceed with a future source of randomness,
  which is only revealed after the commit transaction concluded.
  For each block, the `RandomBeaconHistory` automatically stores the generated source of randomness.
  At the time of revealing the source, the committed source becomes a past-block source that can be queried through the history contract.

Adding a safe pattern to reveal randomness without the possibility of conditional transaction reversion unlocks applications relying on randomness. By providing examples of commit-reveal implementations we hope to foster a more secure ecosystem of decentralized applications and encourage developers to build with best practices.

In simpler terms, the native secure randomness provided by the protocol can now be safely utilized within Cadence smart contracts
and is available to all developers on Flow and the FVM.

## An Invitation to Build[​](#an-invitation-to-build "Direct link to An Invitation to Build")

Flow's onchain randomness opens new doors for innovation in web3, offering developers the tools to create fair and transparent decentralized applications. With this feature, new possibilities emerge—from enhancing gameplay in decentralized gaming to ensuring the integrity of smart contract-driven lotteries or introducing novel mechanisms in DeFi.

This is an invitation for builders and creators: leverage Flow's onchain randomness to distinguish your projects and push the boundaries of what's possible. Your imagination and code have the potential to forge new paths in the web3 landscape. So go ahead and build; the community awaits the next big thing that springs from true randomness.

## Learn More[​](#learn-more "Direct link to Learn More")

If you'd like to dive deeper into Flow's onchain randomness, here's a list of resources:

* To learn more about how randomness works under the hood, see [the forum post](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110).
* These documents provide a more in-depth technical understanding of the updates and enhancements to the Flow blockchain.
  + **[FLIP 120: Update unsafeRandom function](https://github.com/onflow/flips/blob/main/cadence/20230713-random-function.md#flip-120-update-unsaferandom-function)**
  + **[FLIP 123: On-chain Random beacon history for commit-reveal schemes](https://github.com/onflow/flips/blob/main/protocol/20230728-commit-reveal.md#flip-123-on-chain-random-beacon-history-for-commit-reveal-schemes)**
* To see working Cadence code, explore the [coin toss example on GitHub](https://github.com/onflow/random-coin-toss).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/advanced-concepts/randomness.md)

Last updated on **Apr 1, 2025** by **Brian Doyle**

[Previous

NFT Metadata Views](/build/advanced-concepts/metadata-views)[Next

Scaling Transactions from a Single Account](/build/advanced-concepts/scaling)

###### Rate this page

😞😐😊

* [Use Cases of Onchain Randomness](#use-cases-of-onchain-randomness)
* [History of the Distributed Randomness Beacon](#history-of-the-distributed-randomness-beacon)
  + [The History and Limitations of `unsafeRandom` (Now Deprecated)](#the-history-and-limitations-of-unsaferandom-now-deprecated)
* [Guidelines for Safe Usage](#guidelines-for-safe-usage)
* [Commit-Reveal Scheme](#commit-reveal-scheme)
  + [FLIP 123](#flip-123)
  + [Which random function should be used:](#which-random-function-should-be-used)
* [An Invitation to Build](#an-invitation-to-build)
* [Learn More](#learn-more)

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
* [Flowscan Mainnet](https://flowscan.io/)
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