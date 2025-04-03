# Source: https://developers.flow.com/tutorials/native-vrf/commit-reveal-cadence

Secure Randomness with Commit-Reveal in Cadence | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Token Launch](/tutorials/token-launch)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth Tutorials](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

  + [Secure Randomness with Commit-Reveal in Cadence](/tutorials/native-vrf/commit-reveal-cadence)
  + [Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract)

* [Native VRF](/tutorials/native-vrf)
* Secure Randomness with Commit-Reveal in Cadence

On this page

# Secure Randomness with Commit-Reveal in Cadence

Randomness is a critical component in blockchain applications, enabling fair and unpredictable outcomes for use cases like gaming, lotteries, and cryptographic protocols. The most basic approach to generating a random number on EVM chains is to utilize block hashes, which combines the block hash with a user-provided seed and hashes them together. The resulting hash can be used as a pseudo-random number. However, this approach has limitations:

1. Predictability: Miners can potentially manipulate the block hash to influence the generated random number.
2. Replay attacks: In case of block reorganizations, the revealed answers will not be re-used again.

[Chainlink VRF](https://docs.chain.link/vrf) is a popular tool that improves on this by providing another approach for generating provably random values on Ethereum and other blockchains by relying on a decentralized oracle network to deliver cryptographically secure randomness from off-chain sources. However, this dependence on external oracles introduces several weaknesses, such as cost, latency, and scalability concerns.

In contrast, Flow offers a simpler and more integrated approach with its Random Beacon contract, which provides native on-chain randomness at the protocol level, eliminating reliance on external oracles and sidestepping their associated risks. Via a commit-and-reveal scheme, Flow's protocol-native secure randomness can be used within both Cadence and Solidity smart contracts.

## Objectives[​](#objectives "Direct link to Objectives")

By the end of this guide, you will be able to:

* Deploy a Cadence smart contract on the Flow blockchain
* Implement commit-reveal randomness to ensure fairness
* Interact with Flow's on-chain randomness features
* Build and test the Coin Toss game using Flow's Testnet

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

You'll need the following:

* Flow Testnet Account: An account on the Flow Testnet with test FLOW tokens for deploying contracts and executing transactions (e.g., via [Flow Faucet](https://testnet-faucet.onflow.org/)).
* Flow CLI or Playground: The Flow CLI or Flow Playground for deploying and testing contracts (install via [Flow Docs](https://docs.onflow.org/flow-cli/install/)).

## Overview[​](#overview "Direct link to Overview")

In this guide, we will explore how to use a commit-reveal scheme in conjunction with Flow's Random Beacon to achieve secure, non-revertible randomness. This mechanism mitigates post-selection attacks, where participants attempt to manipulate or reject unfavorable random outcomes after they are revealed.

To illustrate this concept, we will build a Coin Toss game on Flow, demonstrating how smart contracts can leverage commit-reveal randomness for fair, tamper-resistant results.

### What is the Coin Toss Game?[​](#what-is-the-coin-toss-game "Direct link to What is the Coin Toss Game?")

The Coin Toss Game is a decentralized betting game that showcases Flow's commit-reveal randomness. Players place bets without knowing the random outcome, ensuring fairness and resistance to manipulation.

The game consists of two distinct phases:

1. Commit Phase – The player places a bet by sending Flow tokens to the contract. The contract records the commitment and requests a random value from Flow's Random Beacon. The player receives a Receipt, which they will use to reveal the result later.
2. Reveal Phase – Once the random value becomes available in `RandomBeaconHistory`, the player submits their Receipt to determine the outcome:
   * If the result is 0, the player wins and receives double their bet.
   * If the result is 1, the player loses, and their bet remains in the contract.

### Why Use Commit-Reveal Randomness?[​](#why-use-commit-reveal-randomness "Direct link to Why Use Commit-Reveal Randomness?")

* Prevents manipulation – Players cannot selectively reveal results after seeing the randomness.
* Ensures fairness – Flow's Random Beacon provides cryptographically secure, verifiable randomness.
* Reduces reliance on external oracles – The randomness is generated natively on-chain, avoiding additional complexity, third party risk and cost.

## Building the Coin Toss Contract[​](#building-the-coin-toss-contract "Direct link to Building the Coin Toss Contract")

In this section, we'll walk through constructing the `CoinToss.cdc` contract, which contains the core logic for the Coin Toss game. To function properly, the contract relies on supporting contracts and a proper deployment setup.

This tutorial will focus specifically on writing and understanding the `CoinToss.cdc` contract, while additional setup details can be found in the [original GitHub repo](https://github.com/onflow/random-coin-toss).

### Step 1: Defining the `CoinToss.cdc` Contract[​](#step-1-defining-the-cointosscdc-contract "Direct link to step-1-defining-the-cointosscdc-contract")

Let's define our `CoinToss.cdc` and bring the other supporting contracts.

`_18

import "Burner"

_18

import "FungibleToken"

_18

import "FlowToken"

_18

_18

import "RandomConsumer"

_18

_18

access(all) contract CoinToss {

_18

/// The multiplier used to calculate the winnings of a successful coin toss

_18

access(all) let multiplier: UFix64

_18

/// The Vault used by the contract to store funds.

_18

access(self) let reserve: @FlowToken.Vault

_18

/// The RandomConsumer.Consumer resource used to request & fulfill randomness

_18

access(self) let consumer: @RandomConsumer.Consumer

_18

_18

/* --- Events --- */

_18

access(all) event CoinFlipped(betAmount: UFix64, commitBlock: UInt64, receiptID: UInt64)

_18

access(all) event CoinRevealed(betAmount: UFix64, winningAmount: UFix64, commitBlock: UInt64, receiptID: UInt64)

_18

}`

### Step 2: Implementing the Commit Phase With `flipCoin`[​](#step-2-implementing-the-commit-phase-with-flipcoin "Direct link to step-2-implementing-the-commit-phase-with-flipcoin")

Let's define the first step in our scheme; the commit phase. We do this through a `flipCoin` public function. In this method, the caller commits a bet. The contract takes note of the block height and bet amount, returning a `Receipt` resource which is used by the former to reveal the coin toss result and determine their winnings.

`_12

access(all) fun flipCoin(bet: @{FungibleToken.Vault}): @Receipt {

_12

let request <- self.consumer.requestRandomness()

_12

let receipt <- create Receipt(

_12

betAmount: bet.balance,

_12

request: <-request

_12

)

_12

self.reserve.deposit(from: <-bet)

_12

_12

emit CoinFlipped(betAmount: receipt.betAmount, commitBlock: receipt.getRequestBlock()!, receiptID: receipt.uuid)

_12

_12

return <- receipt

_12

}`

### Step 3: Implementing the Reveal Phase With `revealCoin`[​](#step-3-implementing-the-reveal-phase-with-revealcoin "Direct link to step-3-implementing-the-reveal-phase-with-revealcoin")

Now we implement the reveal phase with the `revealCoin` function. Here the caller provides the Receipt given to them at commitment. The contract then "flips a coin" with `_randomCoin()` providing the Receipt's contained Request. If result is 1, user loses, but if it's 0 the user doubles their bet. Note that the caller could condition the revealing transaction, but they've already provided their bet amount so there's no loss for the contract if they do.

`_23

access(all) fun revealCoin(receipt: @Receipt): @{FungibleToken.Vault} {

_23

let betAmount = receipt.betAmount

_23

let commitBlock = receipt.getRequestBlock()!

_23

let receiptID = receipt.uuid

_23

_23

let coin = self._randomCoin(request: <-receipt.popRequest())

_23

_23

Burner.burn(<-receipt)

_23

_23

// Deposit the reward into a reward vault if the coin toss was won

_23

let reward <- FlowToken.createEmptyVault(vaultType: Type<@FlowToken.Vault>())

_23

if coin == 0 {

_23

let winningsAmount = betAmount * self.multiplier

_23

let winnings <- self.reserve.withdraw(amount: winningsAmount)

_23

reward.deposit(

_23

from: <-winnings

_23

)

_23

}

_23

_23

emit CoinRevealed(betAmount: betAmount, winningAmount: reward.balance, commitBlock: commitBlock, receiptID: receiptID)

_23

_23

return <- reward

_23

}`

The final version of `CoinToss.cdc` should look like [this contract code](https://github.com/onflow/random-coin-toss/blob/main/contracts/CoinToss.cdc).

## Testing CoinToss on Flow Testnet[​](#testing-cointoss-on-flow-testnet "Direct link to Testing CoinToss on Flow Testnet")

To make things easy, we've already deployed the `CoinToss.cdx` contract for you at this address: [0xb6c99d7ff216a684](https://contractbrowser.com/A.b6c99d7ff216a684.CoinToss). We'll walk through placing a bet and revealing the result using [run.dnz](https://run.dnz.dev/), a Flow-friendly tool similar to Ethereum's Remix.

### Placing a Bet with flipCoin[​](#placing-a-bet-with-flipcoin "Direct link to Placing a Bet with flipCoin")

First, you'll submit a bet to the CoinToss contract by withdrawing Flow tokens and storing a receipt. Here's how to get started:

1. Open Your Dev Environment: Head to [run.dnz](https://run.dnz.dev/).
2. Enter the Transaction Code: Paste the following Cadence code into the editor:

`_26

import FungibleToken from 0x9a0766d93b6608b7

_26

import FlowToken from 0x7e60df042a9c0868

_26

import CoinToss from 0xb6c99d7ff216a684

_26

_26

/// Commits the defined amount of Flow as a bet to the CoinToss contract, saving the returned Receipt to storage

_26

///

_26

transaction(betAmount: UFix64) {

_26

_26

prepare(signer: auth(BorrowValue, SaveValue) &Account) {

_26

// Withdraw my bet amount from my FlowToken vault

_26

let flowVault = signer.storage.borrow<auth(FungibleToken.Withdraw) &FlowToken.Vault>(from: /storage/flowTokenVault)!

_26

let bet <- flowVault.withdraw(amount: betAmount)

_26

_26

// Commit my bet and get a receipt

_26

let receipt <- CoinToss.flipCoin(bet: <-bet)

_26

_26

// Check that I don't already have a receipt stored

_26

if signer.storage.type(at: CoinToss.ReceiptStoragePath) != nil {

_26

panic("Storage collision at path=".concat(CoinToss.ReceiptStoragePath.toString()).concat(" a Receipt is already stored!"))

_26

}

_26

_26

// Save that receipt to my storage

_26

// Note: production systems would consider handling path collisions

_26

signer.storage.save(<-receipt, to: CoinToss.ReceiptStoragePath)

_26

}

_26

}`

3. Set Your Bet: A modal will pop up asking for the betAmount. Enter a value (e.g., 1.0 for 1 Flow token) and submit
4. Execute the Transaction: Click "Run," and a WalletConnect window will appear. Choose Blocto, sign in with your email, and hit "Approve" to send the transaction to Testnet.

![remix5-sc](/assets/images/remix5-cd6636b214a1b17fc4a012322777d3a5.png)

5. Track it: You can take the transaction id to [FlowDiver](https://testnet.flowdiver.io/)[.io](https://testnet.flowdiver.io/tx/9c4f5436535d36a82d4ae35467b37fea8971fa0ab2409dd0d5f861f61e463d98) to have a full view of everything that's going on with this `FlipCoin` transaction.

### Revealing the Coin Toss Result[​](#revealing-the-coin-toss-result "Direct link to Revealing the Coin Toss Result")

Let's reveal the outcome of your coin toss to see if you've won. This step uses the receipt from your bet, so ensure you're using the same account that placed the bet. Here's how to do it:

1. Return to your Dev Environment: Open [run.dnz](https://run.dnz.dev/) again.
2. Enter the Reveal Code: Paste the following Cadence transaction into the editor:

`_24

import FlowToken from 0x7e60df042a9c0868

_24

import CoinToss from 0xb6c99d7ff216a684

_24

_24

/// Retrieves the saved Receipt and redeems it to reveal the coin toss result, depositing winnings with any luck

_24

///

_24

transaction {

_24

_24

prepare(signer: auth(BorrowValue, LoadValue) &Account) {

_24

// Load my receipt from storage

_24

let receipt <- signer.storage.load<@CoinToss.Receipt>(from: CoinToss.ReceiptStoragePath)

_24

?? panic("No Receipt found in storage at path=".concat(CoinToss.ReceiptStoragePath.toString()))

_24

_24

// Reveal by redeeming my receipt - fingers crossed!

_24

let winnings <- CoinToss.revealCoin(receipt: <-receipt)

_24

_24

if winnings.balance > 0.0 {

_24

// Deposit winnings into my FlowToken Vault

_24

let flowVault = signer.storage.borrow<&FlowToken.Vault>(from: /storage/flowTokenVault)!

_24

flowVault.deposit(from: <-winnings)

_24

} else {

_24

destroy winnings

_24

}

_24

}

_24

}`

After running this transaction, we reveal the result of the coin flip and it's 1! Meaning we have won nothing this time, but keep trying!

You can find the full transaction used for this example, with its result and events, at [FlowDiver.io/tx/](https://testnet.flowdiver.io/tx/a79fb2f947e7803eefe54e48398f6983db4e0d4d5e217d2ba94f8ebdec132957).

## Conclusion[​](#conclusion "Direct link to Conclusion")

The commit-reveal scheme, implemented within the context of Flow's Random Beacon, provides a robust solution for generating secure and non-revertible randomness in decentralized applications. By leveraging this mechanism, developers can ensure that their applications are:

* Fair: Outcomes remain unbiased and unpredictable.
* Resistant to manipulation: Protects against post-selection attacks.
* Immune to replay attacks: A common pitfall in traditional random number generation on other blockchains.

The CoinToss game serves as a practical example of these principles in action. By walking through its implementation, you've seen firsthand how straightforward yet effective this approach can be—balancing simplicity for developers with robust security for users. As blockchain technology advances, embracing such best practices is essential to creating a decentralized ecosystem that upholds fairness and integrity, empowering developers to innovate with confidence.

This tutorial has equipped you with hands-on experience and key skills:

* You deployed a Cadence smart contract on the Flow blockchain.
* You implemented commit-reveal randomness to ensure fairness.
* You interacted with Flow's on-chain randomness features.
* You built and tested the Coin Toss game using Flow's Testnet.

By harnessing Flow's built-in capabilities, you can now focus on crafting engaging, user-centric experiences without grappling with the complexities or limitations of external systems. This knowledge empowers you to create secure, scalable, and fair decentralized applications.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/native-vrf/commit-reveal-cadence.md)

Last updated on **Mar 28, 2025** by **Brian Doyle**

[Previous

Native VRF](/tutorials/native-vrf)[Next

Deploy a Solidity Contract Using Cadence](/tutorials/native-vrf/deploy-solidity-contract)

###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Prerequisites](#prerequisites)
* [Overview](#overview)
  + [What is the Coin Toss Game?](#what-is-the-coin-toss-game)
  + [Why Use Commit-Reveal Randomness?](#why-use-commit-reveal-randomness)
* [Building the Coin Toss Contract](#building-the-coin-toss-contract)
  + [Step 1: Defining the `CoinToss.cdc` Contract](#step-1-defining-the-cointosscdc-contract)
  + [Step 2: Implementing the Commit Phase With `flipCoin`](#step-2-implementing-the-commit-phase-with-flipcoin)
  + [Step 3: Implementing the Reveal Phase With `revealCoin`](#step-3-implementing-the-reveal-phase-with-revealcoin)
* [Testing CoinToss on Flow Testnet](#testing-cointoss-on-flow-testnet)
  + [Placing a Bet with flipCoin](#placing-a-bet-with-flipcoin)
  + [Revealing the Coin Toss Result](#revealing-the-coin-toss-result)
* [Conclusion](#conclusion)

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