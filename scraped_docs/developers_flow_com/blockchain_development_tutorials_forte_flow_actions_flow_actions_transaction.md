# Source: https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction

Flow Actions Transaction | Flow Developer Portal



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

* * [Forte Network Upgrade](/blockchain-development-tutorials/forte)* [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)* Flow Actions Transaction

On this page

# Flow Actions Transaction

warning

We are reviewing and finalizing Flow Actions in [FLIP 339](https://github.com/onflow/flips/pull/339/files). The specific implementation may change as a part of this process.

We will update these tutorials, but you may need to refactor your code if the implementation changes.

[Staking](/protocol/staking) is a simple way to participate in the blockchain process. You supply tokens to help with governance and, in return, you earn a share of the network's rewards. It's a way to grow unused assets and provides a much higher rate of return than a savings account.

warning

Make certain you understand how [slashing](/protocol/staking/stake-slashing) works and assess your risk tolerance before you stake.

To stake directly, lock up your tokens with [Flow Port](https://port.flow.com/). You can also use other platforms and protocols that have a different strategy for participating in this process. [IncrementFi](https://app.increment.fi/) offers a Liquid Staking Protocol (LSP) they describe as:

> LSP allows users to earn staking rewards without locking $flow tokens or running node softwares. Users can deposit $flow tokens and receive transferrable $stFlow tokens in return. Liquid staking combines the benefits of staking (earning rewards) and brings liquidity, as well as additional possibilities to increase your assets or hedge your positions by participating in Flow's DeFi ecosystem.

Participation in staking comes with a tedious chore - you'll need to regularly complete one or more transactions to claim your rewards and restake them to compound your earnings.

Flow Actions simplifies this task. It gives you a suite of blocks that, after instantiation, perform actions in the same way from one protocol to another.

In this tutorial, you'll learn how to build a transaction that simplifies restaking on [IncrementFi](https://app.increment.fi/), and that you can adapt with different connectors to work on other protocols as well.

tip

If you combine this transaction with [scheduled transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction), you can automate it completely!

## Learning objectives[​](#learning-objectives "Direct link to Learning objectives")

After you complete this tutorial, you will be able to:

* Chain multiple decentralized finance (DeFi) operations atomically
* Handle token type mismatches automatically
* Build safe, validated transactions with proper error handling
* Create reusable, protocol-agnostic DeFi building blocks

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Flow CLI: install from the [Flow CLI docs](/build/tools/flow-cli/install)
* Cursor + [Cadence Extension](https://marketplace.visualstudio.com/items?itemName=onflow.cadence) (recommended)

## Cadence programming language[​](#cadence-programming-language "Direct link to Cadence programming language")

This tutorial assumes you have a modest knowledge of [Cadence](https://cadence-lang.org/docs/). If you don't, you can still follow along, but we recommend that you complete our series of [Cadence](https://cadence-lang.org/docs/) tutorials. Most developers find it more pleasant than other blockchain languages and it's easy to pick up.

## Get started on mainnet[​](#get-started-on-mainnet "Direct link to Get started on mainnet")

This demo uses **mainnet** and a real DeFi protocol. Before you write any code, set up your staking position.

danger

This tutorial uses a real protocol with real funds. Only work with funds your comfortable losing in the event of an error or mistake. Cadence is much safer than Solidity, you can make a mistake and all investment involves risk.

### Stake with IncrementFi[​](#stake-with-incrementfi "Direct link to Stake with IncrementFi")

To complete this tutorial, set up a staking position in Increment Fi. If you already have LP tokens, skip to the **Staking LP Token** step.

**Create an LP position**

First, go to the [Increment Fi Liquidity Pool](https://app.increment.fi/liquidity/add?in=A.1654653399040a61.FlowToken&out=A.d6f80565193ad727.stFlowToken&stable=true) and select 'Single Asset' to provide liquidity with your FLOW tokens.

![single asset](/assets/images/single-asset-17c2120337c11287e63bb16131605571.png)

Then, enter the amount of FLOW you want to add as liquidity. Confirm the transaction and continue to the next step.

**Staking LP token**

Now that you have LP tokens from the FLOW-stFLOW pool, you can stake these tokens to receive rewards from them. To do this, go to the [IncrementFi Farms](https://app.increment.fi/farm) page and look for the `Flow-stFlow Pool #199` pool. Note that the #199 is the Pool ID (pid). You might need to select the list view first (the middle button in the upper-right section of the LP pools page) in order to properly see the pid.

![list view](/assets/images/list-view-farms-9a3fcbfd054f1207912cd294ca8fea18.png)

This pid is necessary to execute the restaking transaction later, so make certain you know which pid to use.

![pid](/assets/images/pid-5b34a8110123ae36cb41de1734f70eb2.png)

Then, select `Stake LP` and enter the amount of LP tokens to stake into the pool. After the transaction is approved and confirmed, you will see the total stake position and claimable rewards in the pool card.

![pool card](/assets/images/pool-card-b42b52725be8428d449124fdeb3faa6f.png)

Now our staking position generates rewards as time passes by. We use Flow Actions to execute a single transaction that can claim the rewards (stFLOW), convert the optimal amount into FLOW, increase the LP position (thus getting more LP tokens), and restake them into the farm.

### Initialize Your Staking.UserCertificate[​](#initialize-your-stakingusercertificate "Direct link to Initialize Your Staking.UserCertificate")

IncrementFi uses a `Staking.UserCertificate` internally for some actions, and you'll need this certificate to complete this tutorial. While the platform automatically creates it when you perform other actions on the platform, you can explicitly set it up with the [script on Flow Runner](https://run.dnz.dev/snippet/d1bf715483551879).

When the transaction succeeds, you'll see output similar to:

`_10

Transaction ID: 7d3efabb98d3fed69aabf8fa9007fa11571b70300cbd641120271bbfa8e932f5

_10

Transaction Result:

_10

{6 items

_10

"blockId":string"1206e0a1e6f16098e8d3555f7568f7f14e8e6df1983946408627a964dd87d69d"

_10

"status":int4

_10

"statusString":string"SEALED"

_10

"statusCode":int0

_10

"errorMessage":string""

_10

# Remaining details omitted for brevity`

The UserCertificate is a resource stored in your account's private storage that:

1. Proves your identity for IncrementFi staking operations.
2. Allows you to claim rewards from staking pools.

## Set up the project[​](#set-up-the-project "Direct link to Set up the project")

To start, use the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) repo as a template to create a new repository. Clone your new repository and open it in your editor.

Follow the instructions in the README for **mainnet**.

### Start With the scaffold[​](#start-with-the-scaffold "Direct link to Start With the scaffold")

Create a new repo with the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) as a template. Clone your new repo locally and open it in your editor.

Run `flow deps install` to install dependencies.

note

This Scaffold repo is a minimal Flow project with dependencies for Flow Actions and Increment Fi connectors. It only has support for the specific transaction that we execute in this demo (Claim → Zap → Restake for IncrementFi LP rewards)

### Export Your wallet key[​](#export-your-wallet-key "Direct link to Export Your wallet key")

danger

Never use a wallet with with a large amount of funds for development! If you download a malicious VS Code extension, your funds could be stolen.

Never put a wallet key directly in `flow.json`.

warning

Transactions on mainnet incur fees and affect onchain balances. We recommend that you create a new Flow Wallet account with limited funds.

[Export](https://docs.wallet.flow.com/tutorial/extension-private-key-and-seed-phrase-guide) the key for the wallet you want to use for this exercise. It needs to have some funds in it, but you shouldn't do development with the same wallet you keep any valuable assets in.

Create a `.pkey` file for your wallet key, **add it to `.gitignore`**, then add the account to `flow.json`:

`_10

"accounts": {

_10

"my-testing-account": {

_10

"address": "<YOUR CADENCE ADDRESS>",

_10

"key": {

_10

"type": "file",

_10

"location": "./my-testing-account.pkey"

_10

}

_10

}

_10

}`

## Build the transaction[​](#build-the-transaction "Direct link to Build the transaction")

Now that the dependencies have been properly setup and we have made sure that our account is properly setup, the staking position is established as well as the `Staking.UserCertificate`; we are now ready to finally build the restaking transaction

We will be duplicating the transaction provided in the scaffold `cadence/transactions/increment_fi_restake.cdc`

The key pattern we need to create is:

**Source** → **Swap** → **Sink**

* **Source**: Provides tokens (rewards, vaults, etc.)
* **Swap**: Converts tokens (swapping to zap input then zapping to LP tokens)
* **Sink**: Receives and deposits tokens (staking pools, vaults)

### Import required contracts[​](#import-required-contracts "Direct link to Import required contracts")

First, import all the contracts you need to build the transaction:

`_10

import "FungibleToken"

_10

import "DeFiActions"

_10

import "SwapConnectors"

_10

import "IncrementFiStakingConnectors"

_10

import "IncrementFiPoolLiquidityConnectors"

_10

import "Staking"`

* `FungibleToken`: Standard token interface for Flow
* `DeFiActions`: Core Flow Actions framework for composability
* `SwapConnectors`: Wraps swap operations as Flow Actions
* `IncrementFiStakingConnectors`: Flow Actions connectors for IncrementFi staking
* `IncrementFiPoolLiquidityConnectors`: LP token creation (zapping)
* `Staking`: Core staking contract for user certificates

### Define transaction parameters[​](#define-transaction-parameters "Direct link to Define transaction parameters")

We will specify the `pid` (Pool ID) as the transaction parameter because it identifies which IncrementFi staking pool to interact with

`_10

transaction(

_10

pid: UInt64

_10

) {`

### Declare transaction properties[​](#declare-transaction-properties "Direct link to Declare transaction properties")

Then, declare all the properties needed for the transaction. Here is where you'll use the `Staking.UserCertificate` for authentication staking operations. The `pool` is used to reference the staking pool for validation. The starting balance for post-condition verification is the `startingStake`. The composable source that provides LP tokens is the `swapSource`. The `expectedStakeIncrease` is the minimum expected increase for safety. Finally, the `operationID` serves as the unique identifier for tracing the operation across Flow Actions.

`_10

let userCertificateCap: Capability<&Staking.UserCertificate>

_10

let pool: &{Staking.PoolPublic}

_10

let startingStake: UFix64

_10

let swapSource: SwapConnectors.SwapSource

_10

let expectedStakeIncrease: UFix64

_10

let operationID: DeFiActions.UniqueIdentifier`

### Prepare phase[​](#prepare-phase "Direct link to Prepare phase")

The `prepare` phase runs first in the transaction. You use it to set up and validate a Cadence transaction. It's also the only place where a transaction can interact with a user's account and the [resources] within.

**Pool Validation** verifies that the specified pool exists and is accessible.

`_10

// Get pool reference and validate it exists

_10

self.pool = IncrementFiStakingConnectors.borrowPool(pid: pid)

_10

?? panic("Pool with ID \(pid) not found or not accessible")`

**User State Validation** records current staking balance to verify the transaction worked correctly.

`_10

// Get starting stake amount for post-condition validation

_10

self.startingStake = self.pool.getUserInfo(address: acct.address)?.stakingAmount

_10

?? panic("No user info for address \(acct.address)")`

**User Authentication** creates a capability to access your UserCertificate (required for staking operations)

`_10

// Issue capability for user certificate

_10

self.userCertificateCap = acct.capabilities.storage

_10

.issue<&Staking.UserCertificate>(Staking.UserCertificateStoragePath)`

**Operation Tracking** creates a unique ID to trace this operation through all Flow Actions components

`_10

// Create unique identifier for tracing this composed operation

_10

self.operationID = DeFiActions.createUniqueIdentifier()`

### Token type detection and configuration[​](#token-type-detection-and-configuration "Direct link to Token type detection and configuration")

Use the `pid` from the pool we staked the LP tokens to get the liquidity pair information (what tokens make up this pool). We also convert token identifiers to actual Cadence types and determines if this is a stableswap pool or a regular AMM.

`_10

// Get pair info to determine token types and stable mode

_10

let pair = IncrementFiStakingConnectors.borrowPairPublicByPid(pid: pid)

_10

?? panic("Pair with ID \(pid) not found or not accessible")

_10

_10

// Derive token types from the pair

_10

let token0Type = IncrementFiStakingConnectors.tokenTypeIdentifierToVaultType(pair.getPairInfoStruct().token0Key)

_10

let token1Type = IncrementFiStakingConnectors.tokenTypeIdentifierToVaultType(pair.getPairInfoStruct().token1Key)`

### Build the Flow Actions chain[​](#build-the-flow-actions-chain "Direct link to Build the Flow Actions chain")

We need to create the `RewardsSource` so that we can claim the available rewards from the staking pool.

`_10

// Create rewards source to claim staking rewards

_10

let rewardsSource = IncrementFiStakingConnectors.PoolRewardsSource(

_10

userCertificate: self.userCertificateCap,

_10

pid: pid,

_10

uniqueID: self.operationID

_10

)`

In case the reward token might not match the pool's `token0`, we check if we need to reverse the order to account for this mismatch. This helps us verify that the zapper can function properly.

`_10

// Check if we need to reverse token order: if reward token doesn't match token0, we reverse

_10

// so that the reward token becomes token0 (the input token to the zapper)

_10

let reverse = rewardsSource.getSourceType() != token0Type`

Now the zapper can function properly and it takes the reward token as an input (regardless of token ordering). The zapper swaps half to the other token pair to combine them into LP tokens.

`_10

// Create zapper to convert rewards to LP tokens

_10

let zapper = IncrementFiPoolLiquidityConnectors.Zapper(

_10

token0Type: reverse ? token1Type : token0Type, // input token (reward token)

_10

token1Type: reverse ? token0Type : token1Type, // other pair token

_10

stableMode: pair.getPairInfoStruct().isStableswap,

_10

uniqueID: self.operationID

_10

)`

Here is where the true **composition** of Flow Actions come into place. The `lpSource` creates a single source that claims rewards from the staking pool. automatically converts them into LP tokens, and provides LP tokens as output.

`_10

// Wrap rewards source with zapper to convert rewards to LP tokens

_10

let lpSource = SwapConnectors.SwapSource(

_10

swapper: zapper,

_10

source: rewardsSource,

_10

uniqueID: self.operationID

_10

)`

Then the minimum LP tokens we expect to receive are calculated for safety validation.

`_10

// Calculate expected stake increase for post-condition

_10

self.expectedStakeIncrease = zapper.quoteOut(

_10

forProvided: lpSource.minimumAvailable(),

_10

reverse: false

_10

).outAmount`

### Post-condition safety check[​](#post-condition-safety-check "Direct link to Post-condition safety check")

This phase runs at the end for condition verification. We verify that the transaction actually increased your staking balance as expected.

`_10

post {

_10

// Verify that staking amount increased by at least the expected amount

_10

self.pool.getUserInfo(address: self.userCertificateCap.address)!.stakingAmount

_10

>= self.startingStake + self.expectedStakeIncrease:

_10

"Restake below expected amount"

_10

}`

### Execute the transaction[​](#execute-the-transaction "Direct link to Execute the transaction")

`poolSink` creates the staking pool sink in which the LP tokens are deposited.

`_10

// Create pool sink to receive LP tokens for staking

_10

let poolSink = IncrementFiStakingConnectors.PoolSink(

_10

pid: pid,

_10

staker: self.userCertificateCap.address,

_10

uniqueID: self.operationID

_10

)`

Now we have all the components ready for the full flow of transactions. `swapSource.withdrawAvailable()` triggers the entire Source → Transformer chain. This claims rewards, swaps to LP tokens and withdraws LP tokens. The `poolSink.depositCapacity()` deposits LP tokens into the staking pool. And finally, we verify that all tokens were properly deposited (no dust left behind) and destroy the empty vault.

`_10

// Withdraw LP tokens from swap source (sized by sink capacity)

_10

let vault <- self.swapSource.withdrawAvailable(maxAmount: poolSink.minimumCapacity())

_10

_10

// Deposit LP tokens into pool for staking

_10

poolSink.depositCapacity(from: &vault as auth(FungibleToken.Withdraw) &{FungibleToken.Vault})

_10

_10

// Ensure no residual tokens remain

_10

assert(vault.balance == 0.0, message: "Residual after deposit")

_10

destroy vault`

See what happened? We executed this whole (and quite complex) flow in an atomic manner with a single transaction!

## Run the transaction[​](#run-the-transaction "Direct link to Run the transaction")

We are now ready to restake the position with a single transaction!

`_10

flow transactions send cadence/transactions/increment_fi_restake.cdc \

_10

--network mainnet \

_10

--signer my-testing-account \

_10

--args-json '[{"type":"UInt64","value":"<YOUR_POOL_PID>"}]'`

Replace `<YOUR_POOL_PID>` with your actual pool ID (PID) from the IncrementFi Farms page, in this case it is 1999. The PID changes over time.

### Interpret the results[​](#interpret-the-results "Direct link to Interpret the results")

After you complete the transaction, you see that the following events occurred:

* The rewards (stFLOW) were claimed from pool #199 (or the current pool number if you run this exercise yourself) and the reward balance was updated properly.
* The stFLOW was converted to FLOW.
* FLOW and stFLOW was used to add liquidity to the liquidity pool.
* LP tokens were received.
* LP tokens were staked back into the #199 pool causing the staking balance to increase.

## Run the transaction on emulator[​](#run-the-transaction-on-emulator "Direct link to Run the transaction on emulator")

You can run this whole transaction on Emulator as well. Although this example used a real pool to demonstrate a real-world use case, we recommend you start any real projects by testing on the Emulator. After cloning the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) and installing the dependencies you can run:

`_10

make start`

The `make start` command handles all setup automatically using the built-in emulator service account, so no manual configuration is needed. This starts the Flow Emulator and deploys Increment FI dependencies, creates test tokens (1M each), sets up the liquidity pool, sets up the staking pool #0 and displays the complete environment summary. The `pid` is `0` because the automated setup creates the first staking pool with ID `0` containing your staked LP tokens and active rewards

Now you can test the restake workflow:

`_15

# Check available rewards

_15

flow scripts execute cadence/scripts/get_available_rewards.cdc \

_15

--network emulator \

_15

--args-json '[{"type":"Address","value":"0xf8d6e0586b0a20c7"},{"type":"UInt64","value":"0"}]'

_15

_15

# Run the restake transaction

_15

flow transactions send cadence/transactions/increment_fi_restake.cdc \

_15

--signer emulator-account \

_15

--network emulator \

_15

--args-json '[{"type":"UInt64","value":"0"}]'

_15

_15

# Verify rewards were claimed and restaked

_15

flow scripts execute cadence/scripts/get_available_rewards.cdc \

_15

--network emulator \

_15

--args-json '[{"type":"Address","value":"0xf8d6e0586b0a20c7"},{"type":"UInt64","value":"0"}]'`

If you want to run Cadence tests, then use the following commands:

`_10

make test

_10

# or directly:

_10

flow test`

## Conclusion[​](#conclusion "Direct link to Conclusion")

This transaction demonstrates how to chain multiple DeFi operations atomically, handle token type mismatches automatically, build safe validated transactions with proper error handling, and create reusable protocol-agnostic DeFi building blocks. You can apply these patterns to build yield farming, arbitrage, and portfolio management strategies across Flow's DeFi ecosystem. Flow Actions allow sophisticated DeFi strategies, that are complex in nature and dependant on various protocols, to execute in a single atomic transaction.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction.md)

Last updated on **Nov 18, 2025** by **Brian Doyle**

[Previous

Introduction to Flow Actions](/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions)[Next

Connectors](/blockchain-development-tutorials/forte/flow-actions/connectors)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Cadence programming language](#cadence-programming-language)* [Get started on mainnet](#get-started-on-mainnet)
        + [Stake with IncrementFi](#stake-with-incrementfi)+ [Initialize Your Staking.UserCertificate](#initialize-your-stakingusercertificate)* [Set up the project](#set-up-the-project)
          + [Start With the scaffold](#start-with-the-scaffold)+ [Export Your wallet key](#export-your-wallet-key)* [Build the transaction](#build-the-transaction)
            + [Import required contracts](#import-required-contracts)+ [Define transaction parameters](#define-transaction-parameters)+ [Declare transaction properties](#declare-transaction-properties)+ [Prepare phase](#prepare-phase)+ [Token type detection and configuration](#token-type-detection-and-configuration)+ [Build the Flow Actions chain](#build-the-flow-actions-chain)+ [Post-condition safety check](#post-condition-safety-check)+ [Execute the transaction](#execute-the-transaction)* [Run the transaction](#run-the-transaction)
              + [Interpret the results](#interpret-the-results)* [Run the transaction on emulator](#run-the-transaction-on-emulator)* [Conclusion](#conclusion)

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