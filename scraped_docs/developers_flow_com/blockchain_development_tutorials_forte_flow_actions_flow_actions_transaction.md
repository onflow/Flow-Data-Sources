# Source: https://developers.flow.com/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction

Flow Actions Transaction | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      + [Flow Actions](/blockchain-development-tutorials/forte/flow-actions)

        - [Introduction to Flow Actions](/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions)- [Flow Actions Transaction](/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction)- [Connectors](/blockchain-development-tutorials/forte/flow-actions/connectors)- [Basic Combinations](/blockchain-development-tutorials/forte/flow-actions/basic-combinations)+ [Scheduled Transactions](/blockchain-development-tutorials/forte/scheduled-transactions)* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

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

Flow Actions are being reviewed and finalized in [FLIP 339](https://github.com/onflow/flips/pull/339/files). The specific implementation may change as a part of this process.

These tutorials will be updated, but you may need to refactor your code if the implementation changes.

[Staking](/protocol/staking) is an entry-level way to participate in the blockchain process by supplying some of the tokens needed to participate in governance in return for a share of the reward this process generates. It's a great way to increase the value of a holding that would otherwise sit unutilized and provides a much higher rate of return than a savings account, though you should make sure you understand how [slashing](/protocol/staking/stake-slashing) works and make your own determinations on risk.

You can stake directly by locking up your tokens with [Flow Port](https://port.flow.com/), or you can participate in other platforms and protocols that have a different strategy for participating in this process. [IncrementFi](https://app.increment.fi/) has a Liquid Staking Protocol they describe as:

> LSP allows users to earn staking rewards without locking $flow tokens or running node softwares. Users can deposit $flow tokens and receive transferrable $stFlow tokens in return. Liquid staking combines the benefits of staking (earning rewards) and brings liquidity, as well as additional possibilities to increase your assets or hedge your positions by participating in Flow's DeFi ecosystem.

Participation in staking comes with a tedious chore - you'll need to regularly complete one or more transactions to claim your rewards and restake them to compound your earnings.

Flow Actions help developers simplify this type of task by giving developers a suite of blocks that once instantiated, perform actions in the same way from one protocol to another.

In this tutorial, you'll learn how to build a transaction that simplifies restaking on [IncrementFi](https://app.increment.fi/), and can be adapted using different connectors to work on other protocols as well.

tip

If you combine this transaction with [scheduled transactions](/blockchain-development-tutorials/forte/scheduled-transactions/scheduled-transactions-introduction), you can automate it completely!

## Learning Objectives[​](#learning-objectives "Direct link to Learning Objectives")

After completing this tutorial, you will be able to:

* Chain multiple DeFi operations atomically
* Handle token type mismatches automatically
* Build safe, validated transactions with proper error handling
* Create reusable, protocol-agnostic DeFi building blocks

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Flow CLI: install from the [Flow CLI docs](https://developers.flow.com/tools/flow-cli/install)
* Cursor + [Cadence Extension](https://marketplace.visualstudio.com/items?itemName=onflow.cadence) (recommended)

## Cadence Programming Language[​](#cadence-programming-language "Direct link to Cadence Programming Language")

This tutorial assumes you have a modest knowledge of [Cadence](https://cadence-lang.org/docs). If you don't, you'll be able to follow along, but you'll get more out of it if you complete our series of [Cadence](https://cadence-lang.org/docs) tutorials. Most developers find it more pleasant than other blockchain languages and it's not hard to pick up.

## Getting Started on Mainnet[​](#getting-started-on-mainnet "Direct link to Getting Started on Mainnet")

This demo uses **mainnet** and a real DeFi protocol. Before writing any code, you'll need to do some setup.

danger

This tutorial uses a real protocol with real funds. Only work with funds your comfortable losing in the event of an error or mistake.

Cadence is much safer than Solidity, but there are a limited number of ways you could accidentally do something undesirable.

### Staking with IncrementFi[​](#staking-with-incrementfi "Direct link to Staking with IncrementFi")

In order to complete this tutorial, we must set up a staking position in Increment Fi. If you already have LP tokens then you can skip to the **Staking LP Token** step.

**Creating an LP Position**

First go to the [Increment Fi Liquidity Pool](https://app.increment.fi/liquidity/add?in=A.1654653399040a61.FlowToken&out=A.d6f80565193ad727.stFlowToken&stable=true) and select the 'Single Asset' button to be able to provide liquidity with your FLOW tokens.

![single asset](/assets/images/single-asset-17c2120337c11287e63bb16131605571.png)

Then input the amount of FLOW you want to add as liquidity. Once the transaction is confirmed, you are ready to proceed with the next step.

**Staking LP Token**

Now that you have LP tokens from the FLOW-stFLOW pool, you can stake these token to receive rewards from them. To do this you must go to the [IncrementFi Farms](https://app.increment.fi/farm) page and look for the `Flow-stFlow Pool #199` pool. Note that the #199 is the Pool ID (pid). You might need to select the list view first (the middle button in the upper-right section of the LP pools page) in order to properly see the pid.

![list view](/assets/images/list-view-farms-9a3fcbfd054f1207912cd294ca8fea18.png)

This pid is necessary to execute the restaking transaction later, so be sure to know with pid you are using.

![pid](/assets/images/pid-5b34a8110123ae36cb41de1734f70eb2.png)

Then select the `Stake LP` button and input the amount of LP tokens that you wish to stake into the pool. Once the transaction has been approved and confirmed, you will see you total stake position and rewards that are claimable in the pool card.

![pool card](/assets/images/pool-card-b42b52725be8428d449124fdeb3faa6f.png)

Now our staking position will generate rewards as time passes by. We will use Flow Actions to be able to execute a single transaction that can claim the rewards (stFLOW), convert the optimal amount into FLOW, increase the LP position (thus getting more LP tokens), and restaking them into the farm.

### Initialize Your Staking User Certificate[​](#initialize-your-staking-user-certificate "Direct link to Initialize Your Staking User Certificate")

IncrementFi uses a `Staking.UserCertificate` internally for some actions. You don't need one of these to stake tokens, and it's automatically created when you do other actions on the platform that use it. You will need this certificate to complete this tutorial. You can accomplish that with this [script on Flow Runner](https://run.dnz.dev/snippet/d1bf715483551879).

When it succeeds, you'll see output similar to:

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

1. Proves your identity for IncrementFi staking operations
2. Allows you to claim rewards from staking pools

## Setting Up the Project[​](#setting-up-the-project "Direct link to Setting Up the Project")

Begin by using the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) repo as a template to create a new repository. Clone your new repository and open it in your editor.

Follow the instructions in the README for **mainnet**.

### Starting With the Scaffold[​](#starting-with-the-scaffold "Direct link to Starting With the Scaffold")

Create a new repo using the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) as a template. Clone your new repo locally and open it in your editor.

Run `flow deps install` to install dependencies.

**Note** that this Scaffold repo is a minimal Flow project with dependencies for Flow Actions and Increment Fi connectors. It only has support for the specific transaction that we will execute in this demo (Claim → Zap → Restake for IncrementFi LP rewards)

### Export Your Wallet Key[​](#export-your-wallet-key "Direct link to Export Your Wallet Key")

danger

Never use a wallet with with a large amount of funds for development! If you are tricked into downloading a malicious VS Code extension, these funds may be stolen.

Never put a wallet key directly in `flow.json`.

warning

Transactions on mainnet incur fees and affect onchain balances. Consider creating a new Flow Wallet account with limited funds.

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

## Building the Transaction[​](#building-the-transaction "Direct link to Building the Transaction")

Now that the dependencies have been properly setup and we have made sure that our account is properly setup, the staking position is established as well as the `Staking.UserCertificate`; we are now ready to finally build the restaking transaction

We will be duplicating the transaction provided in the scaffold `cadence/transactions/increment_fi_restake.cdc`

The key pattern we need to create is:

**Source** → **Swap** → **Sink**

* **Source**: Provides tokens (rewards, vaults, etc.)
* **Swap**: Converts tokens (swapping to zap input then zapping to LP tokens)
* **Sink**: Receives and deposits tokens (staking pools, vaults)

### Import Required Contracts[​](#import-required-contracts "Direct link to Import Required Contracts")

First we need to import all the contracts needed to build the transaction:

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

### Define Transaction Parameters[​](#define-transaction-parameters "Direct link to Define Transaction Parameters")

We will specify the `pid` (Pool ID) as the transaction parameter because it identifies which IncrementFi staking pool to interact with

`_10

transaction(

_10

pid: UInt64

_10

) {`

### Declare Transaction Properties[​](#declare-transaction-properties "Direct link to Declare Transaction Properties")

Then we need to declare all the properties that are needed for the transaction to occur. Here is where the `Staking.UserCertificate` we created will be useful for authentication staking operations. The `pool` is used to reference the staking pool for validation. The starting balance for post-condition verification is the `startingStake`. The composable source that provides LP tokens is the `swapSource`. The `expectedStakeIncrease` is the minimum expected increase for safety. Finally we have the `operationID` which serves as the unique identifier for tracing the operation across Flow Actions.

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

### Prepare Phase[​](#prepare-phase "Direct link to Prepare Phase")

The `prepare` phase is used for setup and validation for a transaction in Cadence, it runs before anything else. The `prepare` phase is essentially "plan and validate" while `execute` is "do it atomically".

**Pool Validation** ensures the specified pool exists and is accessible.

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

### Token Type Detection and Configuration[​](#token-type-detection-and-configuration "Direct link to Token Type Detection and Configuration")

Then we need to get the liquidity pair information (what tokens make up this pool), this will be done with the `pid` from the pool we staked the LP tokens. We also convert token identifiers to actual Cadence types and determines if this is a stableswap pool or a regular AMM

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

### Build the Flow Actions Chain[​](#build-the-flow-actions-chain "Direct link to Build the Flow Actions Chain")

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

In case the reward token might not match the pool's token0, we check if we need to reverse the order to account for this mismatch. This helps us ensure that the zapper can function properly.

`_10

// Check if we need to reverse token order: if reward token doesn't match token0, we reverse

_10

// so that the reward token becomes token0 (the input token to the zapper)

_10

let reverse = rewardsSource.getSourceType() != token0Type`

Now the zapper can function properly and it will take the reward token as an input (regardless of token ordering). The zapper will swap half to the other token pair in order to combine them into LP tokens.

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

### Post-Condition Safety Check[​](#post-condition-safety-check "Direct link to Post-Condition Safety Check")

This phase runs at the end and it is used for condition verification. We ensure that the transaction actually increased your staking balance as expected.

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

### Execute the Transaction[​](#execute-the-transaction "Direct link to Execute the Transaction")

**poolSink** creates the staking pool sink in which the LP tokens will be deposited.

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

Now we have all the components ready for the full flow of transactions. `swapSource.withdrawAvailable()` triggers the entire Source → Transformer chain. This claims rewards, swaps to LP tokens and withdraws LP tokens. The `poolSink.depositCapacity()` deposits LP tokens into the staking pool. And finally we ensure that all tokens were properly deposited (no dust left behind).

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

See what happened? We are able to execute this whole (and quite complex) flow in an atomic manner with a single transaction!

## Running the Transaction[​](#running-the-transaction "Direct link to Running the Transaction")

We are now ready to restake the position with a single transaction!

`_10

flow transactions send cadence/transactions/increment_fi_restake.cdc \

_10

--network mainnet \

_10

--signer my-testing-account \

_10

--args-json '[{"type":"UInt64","value":"<YOUR_POOL_PID>"}]'`

Replace `<YOUR_POOL_PID>` with your actual pool ID from the IncrementFi Farms page, in this case it is 199.

### Interpreting the Results[​](#interpreting-the-results "Direct link to Interpreting the Results")

Once you have completed the transaction successfully you see that the following events occurred:

* The rewards (stFLOW) were claimed from pool #199 and the reward balance has been updated properly
* The stFLOW was converted to FLOW
* FLOW and stFLOW was used to add liquidity to the liquidity pool
* LP tokens were received
* LP tokens were staked back into the #199 pool causing the staking balance to increase

## Running the Transaction on Emulator[​](#running-the-transaction-on-emulator "Direct link to Running the Transaction on Emulator")

You can run this whole flow on Emulator as well. It is recommended to do all the testing on Emulator. After cloning the [Flow Actions Scaffold](https://github.com/onflow/flow-actions-scaffold) and installing the dependencies you can run:

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

If you want to run Cadence tests then you can use the following commands:

`_10

make test

_10

# or directly:

_10

flow test`

## Conclusion[​](#conclusion "Direct link to Conclusion")

This transaction demonstrates how to chain multiple DeFi operations atomically, handle token type mismatches automatically, build safe validated transactions with proper error handling, and create reusable protocol-agnostic DeFi building blocks. These patterns can be applied to build yield farming, arbitrage, and portfolio management strategies across Flow's DeFi ecosystem. Flow Actions enable sophisticated DeFi strategies, that are complex in nature and dependant on various protocols, to be executed in a single atomic transaction.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/forte/flow-actions/flow-actions-transaction.md)

Last updated on **Sep 25, 2025** by **Brian Doyle**

[Previous

Introduction to Flow Actions](/blockchain-development-tutorials/forte/flow-actions/intro-to-flow-actions)[Next

Connectors](/blockchain-development-tutorials/forte/flow-actions/connectors)

###### Rate this page

😞😐😊

Copy as Markdown

* [Learning Objectives](#learning-objectives)* [Prerequisites](#prerequisites)* [Cadence Programming Language](#cadence-programming-language)* [Getting Started on Mainnet](#getting-started-on-mainnet)
        + [Staking with IncrementFi](#staking-with-incrementfi)+ [Initialize Your Staking User Certificate](#initialize-your-staking-user-certificate)* [Setting Up the Project](#setting-up-the-project)
          + [Starting With the Scaffold](#starting-with-the-scaffold)+ [Export Your Wallet Key](#export-your-wallet-key)* [Building the Transaction](#building-the-transaction)
            + [Import Required Contracts](#import-required-contracts)+ [Define Transaction Parameters](#define-transaction-parameters)+ [Declare Transaction Properties](#declare-transaction-properties)+ [Prepare Phase](#prepare-phase)+ [Token Type Detection and Configuration](#token-type-detection-and-configuration)+ [Build the Flow Actions Chain](#build-the-flow-actions-chain)+ [Post-Condition Safety Check](#post-condition-safety-check)+ [Execute the Transaction](#execute-the-transaction)* [Running the Transaction](#running-the-transaction)
              + [Interpreting the Results](#interpreting-the-results)* [Running the Transaction on Emulator](#running-the-transaction-on-emulator)* [Conclusion](#conclusion)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.