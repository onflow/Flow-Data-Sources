# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions

Compose with Cadence Transactions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              - [Compose with Cadence Transactions](/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions)- [Native Data Availability With Cadence Scripts](/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts)+ [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)* Compose with Cadence Transactions

On this page

# Compose with Cadence Transactions

In this tutorial, you will **compose with someone else's contracts** on Flow testnet. You'll write a Cadence transaction that reads public state from a contract named `Counter` and only increments the counter when it is odd. Then you will extend the transaction to mint NFTs when the counter is odd, demonstrating how to compose multiple contracts in a single transaction. Everything runs against testnet using the Flow CLI and the dependency manager.

You can use transactions developed and tested this way from the frontend of your app.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you will be able to:

* Configure the Flow CLI *dependency manager* to import named contracts from **testnet**
* Write a Cadence **transaction** that reads and writes to a public contract you did not deploy
* Run the transaction on **testnet** with a funded account using the Flow CLI
* Extend the transaction to compose multiple public contracts (`Counter` + `ExampleNFT` + `NonFungibleToken`) without redeploying anything
* Set up NFT collections and mint NFTs conditionally based on on-chain state
* View transaction results and NFT transfers using Flowscan

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* [Flow CLI installed](/build/tools/flow-cli/install)
* A **funded testnet account** to sign transactions  
  See **Create accounts** and **Fund accounts** in the Flow CLI commands:
  + Create: <https://developers.flow.com/build/tools/flow-cli/commands#create-accounts>
  + Fund: <https://developers.flow.com/build/tools/flow-cli/commands#fund-accounts>

## Getting Started[​](#getting-started "Direct link to Getting Started")

Create a [new project](/build/tools/flow-cli/flow.json/initialize-configuration) with the [Flow CLI](/build/tools/flow-cli):

`_10

flow init`

Follow the prompts and create your project. You do **not** need to install any dependencies.

### Install dependencies[​](#install-dependencies "Direct link to Install dependencies")

We will resolve imports **using string format** (`import "Counter"`) using the [dependency manager](/build/tools/flow-cli/dependency-manager).

This is the recommended way of working with imports of already-deployed contracts. You should also use the CLI to create new files and add existing ones to `flow.json`.

warning

For this exercise, you need to **delete** the existing contract entry for `Counter` from your `flow.json`. You could also use an alias here, but this is simpler since you won't be deploying the `Counter` contract.

You can install dependencies for already deployed contracts, whether yours or those deployed by others:

`_10

# Add a deployed instance of the Counter contract

_10

flow dependencies install testnet://0x8a4dce54554b225d.Counter`

Pick `none` for the deployment account as you won't need to redeploy these contracts.

Once installed with the dependency manager, Cadence imports like `import "Counter"` will resolve to the testnet address when sending transactions on testnet.

info

In Cadence, contracts are deployed to the account storage of the deploying address. Due to security reasons, the same private key produces different address on Cadence testnet and mainnet. One of the features of the dependency manager is to automatically select the right address for imports based on the network you're working on.

---

## Compose with the public `Counter` contract[​](#compose-with-the-public-counter-contract "Direct link to compose-with-the-public-counter-contract")

Review the `Counter` contract that's created as an example by `flow init`:

`_31

access(all) contract Counter {

_31

_31

access(all) var count: Int

_31

_31

// Event to be emitted when the counter is incremented

_31

access(all) event CounterIncremented(newCount: Int)

_31

_31

// Event to be emitted when the counter is decremented

_31

access(all) event CounterDecremented(newCount: Int)

_31

_31

init() {

_31

self.count = 0

_31

}

_31

_31

// Public function to increment the counter

_31

access(all) fun increment() {

_31

self.count = self.count + 1

_31

emit CounterIncremented(newCount: self.count)

_31

}

_31

_31

// Public function to decrement the counter

_31

access(all) fun decrement() {

_31

self.count = self.count - 1

_31

emit CounterDecremented(newCount: self.count)

_31

}

_31

_31

// Public function to get the current count

_31

view access(all) fun getCount(): Int {

_31

return self.count

_31

}

_31

}`

It's an example of a simple contract.

Unlike in Solidity, apps aren't limited to the functionality deployed in a smart contract. One of the ways you can expand your app is to write new transactions that call multiple functions in multiple contracts, with branching based on conditions and state, using a single call and a single signature. You don't need to deploy a new contract, use a proxy, or switch to V2.

In this simple example, imagine that you've already deployed a product that has thousands of users and is dependent on the `Counter` smart contract. After a time, you realize that a significant portion of your users only wish to use the `increment` feature if the current `count` is odd, to try and make the number be even.

In Cadence, this sort of upgrade is easy, even if you didn't anticipate the need at contract deployment.

All you need to do is to write a new [transaction](https://cadence-lang.org/docs/language/transactions) that **reads** the current count from `Counter` and **only increments** it if the value is odd.

Create a new [transaction](https://cadence-lang.org/docs/language/transactions) called `IncrementIfOdd` using the Flow CLI:

`_10

flow generate transaction IncrementIfOdd`

Start by adding the code from the existing `IncrementCounter` [transaction](https://cadence-lang.org/docs/language/transactions):

`_17

import "Counter"

_17

_17

transaction {

_17

_17

prepare(acct: &Account) {

_17

// Authorizes the transaction

_17

}

_17

_17

execute {

_17

// Increment the counter

_17

Counter.increment()

_17

_17

// Retrieve the new count and log it

_17

let newCount = Counter.getCount()

_17

log("New count after incrementing: ".concat(newCount.toString()))

_17

}

_17

}`

Then, modify it to handle the new feature:

`_21

import "Counter"

_21

_21

transaction() {

_21

prepare(account: &Account) {}

_21

_21

execute {

_21

// Get the current count from the Counter contract (public read)

_21

let currentCount = Counter.getCount()

_21

_21

// Print the current count

_21

log("Current count: ".concat(currentCount.toString()))

_21

_21

// If odd (remainder when divided by 2 is not 0), increment

_21

if currentCount % 2 != 0 {

_21

Counter.increment()

_21

log("Counter was odd, incremented to: ".concat(Counter.getCount().toString()))

_21

} else {

_21

log("Counter was even, no increment performed")

_21

}

_21

}

_21

}`

info

As with most blockchains, `log`s are not exposed or returned when transactions are run on testnet or mainnet, but they are visible in the console when you use the [emulator](/build/tools/flow-cli/deployment/start-emulator).

### Run on testnet[​](#run-on-testnet "Direct link to Run on testnet")

You need a **funded** testnet account to sign the transaction. For development tasks, the CLI has [account commands](/build/tools/flow-cli/commands#account-management) that you can use to create and manage your accounts.

Create and fund an account called `testnet-account`:

`_10

# If needed, create a testnet account (one-time)

_10

flow accounts create --network testnet

_10

_10

# If needed, fund it (one-time)

_10

flow accounts fund testnet-account`

danger

As with other blockchain accounts, once the private key for an account is compromised, anyone with that key has complete control over an account and it's assets. **Never** put private keys directly in `flow.json`.

Creating an account using the CLI automatically puts the private key in a `.pkey` file, which is already in `.gitignore`.

[Send the transaction](/build/tools/flow-cli/commands#send-transaction) to testnet, signed with `testnet-account`:

`_10

flow transactions send cadence/transactions/IncrementIfOdd.cdc --signer testnet-account --network testnet`

You should see logs that show the prior value and whether the increment occurred.

tip

This same transaction could be triggered **from an app** and **signed by a wallet** with a single user click. Your dApp would assemble and submit this exact Cadence transaction using your preferred client library, and the user's wallet would authorize it.

---

## Extend with NFT Minting[​](#extend-with-nft-minting "Direct link to Extend with NFT Minting")

Now let's take our composition to the next level by adding NFT minting functionality when the counter is odd. We'll use an example NFT contract that's already deployed on testnet.

This is a silly use case, but it demonstrates the complex use cases you can add to your apps, after contract deployment, and even if you aren't the author of any of the contracts!

### Install the NFT Contract[​](#install-the-nft-contract "Direct link to Install the NFT Contract")

First, let's install the ExampleNFT contract dependency:

`_10

flow dependencies install testnet://012e4d204a60ac6f.ExampleNFT`

warning

This repository uses different deployments for core contracts than those installed by the Flow CLI. If you previously installed core contract dependencies (like `NonFungibleToken`, `MetadataViews`, etc.) using the CLI, you should manually delete all `dependencies` except `Counter` from your `flow.json` file to avoid conflicts.

### Understanding NFT Minting[​](#understanding-nft-minting "Direct link to Understanding NFT Minting")

Let's look at how NFT minting works with this contract. The [MintExampleNFT transaction](https://github.com/mfbz/flow-nft-tester/blob/main/cadence/transactions/MintExampleNFT.cdc) shows the pattern:

`_31

import "ExampleNFT"

_31

import "NonFungibleToken"

_31

_31

transaction(

_31

recipient: Address,

_31

name: String,

_31

description: String,

_31

thumbnail: String,

_31

creator: String,

_31

rarity: String

_31

) {

_31

let recipientCollectionRef: &{NonFungibleToken.Receiver}

_31

_31

prepare(signer: &Account) {

_31

self.recipientCollectionRef = getAccount(recipient)

_31

.capabilities.get<&{NonFungibleToken.Receiver}>(ExampleNFT.CollectionPublicPath)

_31

.borrow()

_31

?? panic("Could not get receiver reference to the NFT Collection")

_31

}

_31

_31

execute {

_31

ExampleNFT.mintNFT(

_31

recipient: self.recipientCollectionRef,

_31

name: name,

_31

description: description,

_31

thumbnail: thumbnail,

_31

creator: creator,

_31

rarity: rarity

_31

)

_31

}

_31

}`

You can copy this functionality and adapt it for our use case.

### Update the IncrementIfOdd Transaction[​](#update-the-incrementifodd-transaction "Direct link to Update the IncrementIfOdd Transaction")

Now let's update our `IncrementIfOdd` transaction to mint an NFT when the counter is odd. You can either modify the existing transaction or create a new one:

`_43

import "Counter"

_43

import "ExampleNFT"

_43

import "NonFungibleToken"

_43

_43

transaction() {

_43

let recipientCollectionRef: &{NonFungibleToken.Receiver}

_43

_43

prepare(acct: &Account) {

_43

// Get the recipient's NFT collection reference

_43

self.recipientCollectionRef = getAccount(acct.address)

_43

.capabilities.get<&{NonFungibleToken.Receiver}>(ExampleNFT.CollectionPublicPath)

_43

.borrow()

_43

?? panic("Could not get receiver reference to the NFT Collection")

_43

}

_43

_43

execute {

_43

// Get the current count from the Counter contract (public read)

_43

let currentCount = Counter.getCount()

_43

_43

// Print the current count

_43

log("Current count: ".concat(currentCount.toString()))

_43

_43

// If odd (remainder when divided by 2 is not 0), increment and mint NFT

_43

if currentCount % 2 != 0 {

_43

Counter.increment()

_43

let newCount = Counter.getCount()

_43

log("Counter was odd, incremented to: ".concat(newCount.toString()))

_43

_43

// Mint an NFT to celebrate the odd number

_43

ExampleNFT.mintNFT(

_43

recipient: self.recipientCollectionRef,

_43

name: "Odd Counter NFT #".concat(newCount.toString()),

_43

description: "This NFT was minted when the counter was odd!",

_43

thumbnail: "https://example.com/odd-counter.png",

_43

creator: "Counter Composer",

_43

rarity: "Rare"

_43

)

_43

log("Minted NFT for odd counter!")

_43

} else {

_43

log("Counter was even, no increment performed")

_43

}

_43

}

_43

}`

### Setup NFT Collection[​](#setup-nft-collection "Direct link to Setup NFT Collection")

Before you can mint NFTs, you need to set up an NFT collection in your account. Create a transaction to do this:

`_10

flow generate transaction SetupCollection`

Add this content to the new transaction:

`_18

import "ExampleNFT"

_18

import "NonFungibleToken"

_18

import "MetadataViews"

_18

_18

transaction {

_18

prepare(signer: auth(BorrowValue, IssueStorageCapabilityController, PublishCapability, SaveValue) &Account) {

_18

if signer.storage.borrow<&ExampleNFT.Collection>(from: ExampleNFT.CollectionStoragePath) != nil {

_18

return

_18

}

_18

_18

let collection <- ExampleNFT.createEmptyCollection(nftType: Type<@ExampleNFT.NFT>())

_18

_18

signer.storage.save(<-collection, to: ExampleNFT.CollectionStoragePath)

_18

_18

let cap = signer.capabilities.storage.issue<&ExampleNFT.Collection>(ExampleNFT.CollectionStoragePath)

_18

signer.capabilities.publish(cap, at: ExampleNFT.CollectionPublicPath)

_18

}

_18

}`

Run the setup transaction:

`_10

flow transactions send cadence/transactions/SetupCollection.cdc --signer testnet-account --network testnet`

### Test the Enhanced Transaction[​](#test-the-enhanced-transaction "Direct link to Test the Enhanced Transaction")

Now run the enhanced transaction:

`_10

flow transactions send cadence/transactions/IncrementIfOdd.cdc --signer testnet-account --network testnet`

You may need to run the regular `IncrementCounter` transaction first to get an odd number:

`_10

flow transactions send cadence/transactions/IncrementCounter.cdc --signer testnet-account --network testnet`

### View Your NFT[​](#view-your-nft "Direct link to View Your NFT")

Click the transaction link in the console to view the transaction in [testnet Flowscan](https://testnet.flowscan.io/). After running the transaction **while the counter is odd**, you'll see an NFT in the `Asset Transfers` tab.

info

The broken image is expected. We didn't use a real URL in the example nft metadata.

![NFT](/assets/images/nft-74e1dd81f4774772b26a2ef6534a2454.png)

---

## Why this matters[​](#why-this-matters "Direct link to Why this matters")

* **No redeploys, no forks:** You composed your app logic with on-chain public contracts you do not control.
* **Cadence-first composition:** Transactions can include *arbitrary logic* that calls into multiple contracts in one atomic operation with a single signature.
* **Production-ready path:** The same code path works from a CLI or a dApp frontend, authorized by a wallet.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, you learned how to compose with multiple on-chain contracts using Cadence transactions. You built a transaction that conditionally interacts with a Counter contract based on its current state, and then extended it to mint NFTs when the counter is odd, demonstrating the power and flexibility of Cadence's composition model.

Now that you have completed the tutorial, you should be able to:

* Configure the Flow CLI *dependency manager* to import named contracts from **testnet**
* Write a Cadence **transaction** that reads and writes to a public contract you did not deploy
* Run the transaction on **testnet** with a funded account using the Flow CLI
* Extend the transaction to compose multiple public contracts (`Counter` + `ExampleNFT` + `NonFungibleToken`) without redeploying anything
* Set up NFT collections and mint NFTs conditionally based on on-chain state
* View transaction results and NFT transfers using Flowscan

This approach gives you the freedom to build complex application logic that composes with any public contracts on Flow, making Cadence's composition model a powerful tool for developers building on Flow.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/cadence-advantages/compose-with-cadence-transactions.md)

Last updated on **Sep 24, 2025** by **Brian Doyle**

[Previous

Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)[Next

Native Data Availability With Cadence Scripts](/blockchain-development-tutorials/cadence/cadence-advantages/native-data-availibility-with-cadence-scripts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Objectives](#objectives)* [Prerequisites](#prerequisites)* [Getting Started](#getting-started)
      + [Install dependencies](#install-dependencies)* [Compose with the public `Counter` contract](#compose-with-the-public-counter-contract)
        + [Run on testnet](#run-on-testnet)* [Extend with NFT Minting](#extend-with-nft-minting)
          + [Install the NFT Contract](#install-the-nft-contract)+ [Understanding NFT Minting](#understanding-nft-minting)+ [Update the IncrementIfOdd Transaction](#update-the-incrementifodd-transaction)+ [Setup NFT Collection](#setup-nft-collection)+ [Test the Enhanced Transaction](#test-the-enhanced-transaction)+ [View Your NFT](#view-your-nft)* [Why this matters](#why-this-matters)* [Conclusion](#conclusion)

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