# Source: https://developers.flow.com/build/advanced-concepts/randomness

Flow On-chain Randomness in Cadence | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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

Flow onchain randomness delivers immediate random values within transactions, bypassing the latency and complexity of oracle integration. Developers can obtain verifiably random results with a single line of Cadence code, streamlining the development process and enhancing the performance of decentralized applications.

## Use Cases of Onchain Randomness[​](#use-cases-of-onchain-randomness "Direct link to Use Cases of Onchain Randomness")

* **Gaming:** Integrates fairness and unpredictability into gameplay, enhancing user engagement without delays.
* **NFTs:** Facilitates the creation of uniquely randomized traits in NFTs quickly, adding to their rarity and value.
* **Lotteries & Draws:** Offers instant and verifiably fair random selection for lotteries, solidifying trust in real-time.
* **DeFi Protocols:** Enables rapid and innovative random reward systems within decentralized finance.
* **DAOs:** Assists in unbiased voting and task assignments through immediate randomness.
* **Broad Applications:** Extends to any domain requiring impartial randomization, from asset distribution to security mechanisms, all with the added benefit of on-demand availability.
* **Flow protocol:** Contributes to the proof of stake consensus security by selecting which validator gets to propose the next block, and assigns verification nodes to check block computations.

## Flow Distributed Randomness Beacon[​](#flow-distributed-randomness-beacon "Direct link to Flow Distributed Randomness Beacon")

Within the Flow protocol, the heart of randomness generation lies in the "Distributed Randomness Beacon".
This module generates randomness that is distributed across the network while adhering to established cryptographic and security standards.
The output from the randomness beacon is a random source for each block that is unpredictable and impartial.
Any node or external client can validate the block random source and verify it was generated fairly, making the randomness beacon a Verifiable Random function (VRF).

Since Flow mainnet launch, the beacon has ensured protocol security by selecting which consensus node gets to propose the next block and assigning verification nodes to oversee block computations. For those interested in a more detailed exploration of the randomness beacon and its inner workings, you can read [the technical deep dive on the Flow forum](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110).

The randomness beacon is also used to provide the Flow Virtual Machine (FVM) with random numbers allowing both Cadence and EVM to access fresh, secure and instant randomness at every block and transaction.

## Revertible Randomness[​](#revertible-randomness "Direct link to Revertible Randomness")

For usage of randomness where result abortion is not an issue, it is recommended to use the built-in function `revertibleRandom.` `revertibleRandom` returns a pseudo-random number and is backed by the Distributed Randomness Beacon.
The function is available for both Cadence and EVM.

`_10

// Language reference:

_10

// https://cadence-lang.org/docs/language/built-in-functions#revertiblerandom

_10

access(all) fun main(): UInt64 {

_10

// Simple assignment using revertibleRandom - keep reading docs for safe usage!

_10

let rand: UInt64 = revertibleRandom<UInt64>()

_10

return rand

_10

}`

It is notable that the random number generation process is unpredictable (for miners unpredictable at block construction time and for cadence logic unpredictable at time of call), verifiable, uniform, as well as safe from bias by miners and previously-running Cadence code.

Check the [Cadence documentation](https://cadence-lang.org/docs/language/built-in-functions#revertiblerandom) for more details about the function usage.

Although Cadence and EVM exposes safe randomness generated by the Flow protocol via `revertibleRandom`, there is an additional safety-relevant aspect that developers need to be mindful about.

The `revertibleRandom` function can be used safely in some applications where the transaction results are *not* deliberately reverted after the random number is revealed (i.e. a trusted contract distributing random NFTs to registered users or onchain lucky draw).
However, if applications require a non-trusted party (for instance app users) to submit a transaction calling a randomized (non-deterministic) contract, the developer must explicitly protect the stream of random numbers to not break the security guarantees:

warning

🚨 A transaction can atomically revert all its action during its runtime and abort. Therefore, it is possible for a transaction calling into your smart contract to post-select favorable results and revert the transaction for unfavorable results.

In other words, if you write a lottery function that immediately draws a random number that may or may not be a winner, a clever attacker can get infinite guesses for free. Use commit-reveal and sell them a ticket instead!

In other words, transactions submitted by a non-trusted party are able to reject their results after the random is revealed.

info

**Post-selection** - the ability for transactions to reject results they don't like - is inherent to any smart contract platform that allows transactions to roll back atomically. See this very similar [Ethereum example](https://consensys.github.io/smart-contract-best-practices/development-recommendations/general/public-data/).

The risky scenario that a contract developer needs to think about is the following:

* Imagine an adversarial user that is sending a transaction that calls your smart contract.
* The transaction includes code that runs after your smart contract returns and inspects the outcome.
* If the outcome is unfavorable (based on some criteria codified in the transaction), the transaction aborts itself.

As an example, consider a simple coin toss randomized contract where users can bet any amount of tokens against a random binary output. If the coin toss contract outputs `1`, the user doubles their bet. If the coin toss contract outputs `0`, the user loses their bet in favor of the coin toss.

Although the user (or the honest coin toss contract) cannot predict or bias the outcome, the user transaction can check the randomized result and cancel the transaction if they are losing their bet. This can be done by calling an exception causing the transaction to error (division by zero for instance). All temporary state changes are cancelled and the user can repeat the process till they double their bet.

## Commit-Reveal Scheme[​](#commit-reveal-scheme "Direct link to Commit-Reveal Scheme")

The recommended way to mitigate the problems above is via a commit-reveal scheme. The scheme involves two steps: commit and reveal. During the commit phase, the user transaction commits to accepting the future output of a smart contract where the last remaining input is an unknown random source. The user transaction does not know the random source at the time of committing. The smart contract stores this commitment on the blockchain. The reveal phase can start as early as the next block, when the committed beacon's source of randomness becomes available. The reveal phase can be executed at any block after that, now that the commitment to a past block is stored on-chain. With a second transaction, the smart contract can be executed to explicitly generate the random outputs.

There are ideas how to further optimize the developer experience in the future. For example, a transaction could delegate part of its gas to an independent transaction it spawns. Conceptually, also this future solution would be a commit-and-reveal scheme, just immediately happening within the same block. Until we eventually get to this next level, developers can implement their own commit-reveal using the tools available to them on Cadence and EVM.

### Commit-Reveal pattern on Flow[​](#commit-reveal-pattern-on-flow "Direct link to Commit-Reveal pattern on Flow")

[FLIP 123: On-chain Random beacon history for commit-reveal schemes](https://github.com/onflow/flips/blob/main/protocol/20230728-commit-reveal.md#flip-123-on-chain-random-beacon-history-for-commit-reveal-schemes) was introduced to provide a safe pattern to use randomness in transactions so that it's not possible to revert unfavorable randomized transaction results.
We recommend this approach as a best-practice example for implementing a commit-reveal scheme in Cadence or EVM. The `RandomBeaconHistory` contract provides a convenient archive, where for each past block height (starting Nov 2023) the respective "source of randomness" can be retrieved. The `RandomBeaconHistory` contract is automatically executed by the system at each block to store the next source of randomness. The history table can be used to query the user's committed random source from the past.

info

While the commit-and-reveal scheme mitigates post-selection of results by adversarial clients, secure randomness on Flow additionally protects against any pre-selection vulnerabilities (like biasing attacks by byzantine miners).

A commit-reveal scheme can be implemented as follows. To illustrate, we'll revisit the coin toss example discussed earlier:

* When a user submits a bidding transaction, the bid amount is transferred to the coin toss contract, and the block height where the bid was made is stored. This is a commitment by the user to use the Source of Randomness (`SoR`) at the current block. Note that the current block's `SoR` isn't known to the transaction execution environment, and therefore the transaction has no way to inspect the random outcome and predict the coin toss result. The current block's `SoR` is only available once added to the history core-contract, which only happens at the end of the block's execution. The user may also commit to using an SoR of some future block, which is equally unknown at the time the bid is made.
* The coin toss contract may grant the user a limited window of time (i.e a block height range) to send a second transaction for resolving the results and claim any winnings. Failing to do so, the bid amount remains in the coin toss contract.
* Within that reveal transaction, the user calls the coin toss contract, looks us up the block height at which the block was committed and checks that it has already passed. The contract queries that block's `SoR` from the core-contract `RandomBeaconHistory` via block height.
* The coin toss contract uses a PRG seeded with the queried `SoR` and diversified using a specific information to the use-case (a user ID or resource ID for instance). Diversification does not add new entropy, but it avoids generating the same outcome for different use-cases. If a diversifier (or salt) isn't used, all users that committed a bid on the same block would either win or lose.
* The PRG is used to generate the random result and resolve the bid. Note that the user can make the transaction abort after inspecting a losing result. However, the bid amount would be lost anyway when the allocated window expires.

The following lines of code illustrate a random coin toss that cannot be gamed or biased. The commit-reveal scheme prevent clients from post-selecting favorable outcomes.

`_54

// The code below is taken from the example CoinToss contract found in the project repo

_54

// https://github.com/onflow/random-coin-toss

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

access(all) fun flipCoin(bet: @{FungibleToken.Vault}): @Receipt {

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

emit CoinFlipped(betAmount: receipt.betAmount, commitBlock: receipt.commitBlock, receiptID: receipt.uuid)

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

access(all) fun revealCoin(receipt: @Receipt): @FungibleToken.Vault {

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

emit CoinRevealed(betAmount: betAmount, winningAmount: 0.0, commitBlock: commitBlock, receiptID: receiptID)

_54

return <- FlowToken.createEmptyVault()

_54

}

_54

_54

let reward <- self.reserve.withdraw(amount: betAmount * 2.0)

_54

_54

emit CoinRevealed(betAmount: betAmount, winningAmount: reward.balance, commitBlock: commitBlock, receiptID: receiptID)

_54

_54

return <- reward

_54

}`

## Revertible Random or Commit-Reveal?[​](#revertible-random-or-commit-reveal "Direct link to Revertible Random or Commit-Reveal?")

While both methods are backed by the Flow Randomness Beacon,
it is important for developers to mindfully choose between `revertibleRandom` or seeding a PRNG using the `RandomBeaconHistory` smart contract:

* With `revertibleRandom` a user has the power to abort and revert if it doesn't like `revertibleRandom`'s outputs.
  `revertibleRandom` is only suitable for smart contract functions that exclusively run within trusted transactions emitted by trusted parties. You can think of a lottery contract picking a winning user, where the picking transaction is emitted by the lottery developer who is trusted to not add the abortion logic into the transaction. Users are able to check the transaction code after it is submitted and make sure the lottery developer acted fairly.
* In contrast, the commit-reveal method using the `RandomBeaconHistory` is necessary in cases where the transaction is submitted by non-trusted users and may revert the random outputs.
  You can think of a user minting a randomized NFT and is able to add a logic to their transaction to check the random traits and abandon the NFT if they are not happy with the result.
  Another user playing a betting game, adds a logic to check the bet result and abort whenever they lose the bet.
  General users are not guaranteed to act honestly when they submit transactions to play. Commit-reveal patterns are the way to limit their actions.
  During the commit phase, the user commits to proceed with a future source of randomness,
  which is only revealed after the commit transaction concluded.

Adding a safe pattern to reveal randomness without the possibility of conditional transaction reversion unlocks applications relying on randomness. By providing examples of commit-reveal implementations we hope to foster a more secure ecosystem of decentralized applications and encourage developers to build with best practices.

## An Invitation to Build[​](#an-invitation-to-build "Direct link to An Invitation to Build")

Flow onchain randomness opens new doors for innovation, offering developers the tools to create fair and transparent decentralized applications. With this feature, new possibilities emerge—from enhancing gameplay in decentralized gaming to ensuring the integrity of smart contract-driven lotteries or introducing novel mechanisms in DeFi.

This is an invitation for builders and creators: leverage onchain randomness on Flow to distinguish your projects and push the boundaries of what's possible. Your imagination and code have the potential to forge new paths in the web3 landscape. So go ahead and build; the community awaits the next big thing that springs from true randomness.

## Learn More[​](#learn-more "Direct link to Learn More")

If you'd like to dive deeper into onchain randomness on Flow, here's a list of resources:

* To learn more about how the randomness beacon works under the hood, see [the forum post](https://forum.flow.com/t/secure-random-number-generator-for-flow-s-smart-contracts/5110).
* These FLIPs provide a more in-depth technical understanding of recent updates related to randomness:
  + **[FLIP 120: Update unsafeRandom function:](https://github.com/onflow/flips/blob/main/cadence/20230713-random-function.md#flip-120-update-unsaferandom-function)** describes how the beacon provides randoms to `revertibleRandomness`.
  + **[FLIP 123: On-chain Random beacon history for commit-reveal schemes:](https://github.com/onflow/flips/blob/main/protocol/20230728-commit-reveal.md#flip-123-on-chain-random-beacon-history-for-commit-reveal-schemes)** describes the commit-reveal design and why it is secure.
* To see working Cadence and EVM code, explore the [coin toss example on GitHub](https://github.com/onflow/random-coin-toss).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/advanced-concepts/randomness.md)

Last updated on **May 8, 2025** by **Brian Doyle**

[Previous

NFT Metadata Views](/build/advanced-concepts/metadata-views)[Next

Scaling Transactions from a Single Account](/build/advanced-concepts/scaling)

###### Rate this page

😞😐😊

Copy as Markdown

* [Use Cases of Onchain Randomness](#use-cases-of-onchain-randomness)
* [Flow Distributed Randomness Beacon](#flow-distributed-randomness-beacon)
* [Revertible Randomness](#revertible-randomness)
* [Commit-Reveal Scheme](#commit-reveal-scheme)
  + [Commit-Reveal pattern on Flow](#commit-reveal-pattern-on-flow)
* [Revertible Random or Commit-Reveal?](#revertible-random-or-commit-reveal)
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
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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