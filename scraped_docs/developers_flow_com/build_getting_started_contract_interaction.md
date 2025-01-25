# Source: https://developers.flow.com/build/getting-started/contract-interaction




Contract Interaction | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
  + [Contract Interaction](/build/getting-started/contract-interaction)
  + [Local Development](/build/getting-started/flow-cli)
  + [Simple Frontend](/build/getting-started/fcl-quickstart)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/fungible-token)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Getting Started
* Contract Interaction
On this page

# Contract Interaction

In this quickstart guide, you'll interact with your first smart contract on the Flow Testnet. `Testnet` is a public instance of the Flow blockchain designed for experimentation, where you can deploy and invoke smart contracts without incurring any real-world costs.

Smart contracts on Flow are permanent pieces of code that live on the blockchain. They allow you to encode business logic, define digital assets, and much more. By leveraging smart contracts, you can create decentralized applications (dApps) that are transparent, secure, and open to anyone.

Flow supports modern smart contracts written in [Cadence](https://cadence-lang.org/), a resource-oriented programming language designed specifically for smart contracts. Cadence focuses on safety and security, making it easier to write robust contracts. Flow also supports traditional [EVM](https://flow.com/upgrade/crescendo/evm)-compatible smart contracts written in Solidity, allowing developers to port their existing Ethereum contracts to Flow. In this guide, we'll focus on interacting with Cadence smart contracts.

## Objectives[​](#objectives "Direct link to Objectives")

After completing this guide, you'll be able to:

* Read data from a [Cadence](https://cadence-lang.org/) smart contract deployed on Flow.
* Understand how to interact with contracts on Flow's `testnet`.
* Retrieve and display data from a deployed smart contract via scripts.

In later steps, you'll learn how to:

* Create a Flow project using the [Flow CLI](/tools/flow-cli).
* Add an already-deployed contract to your project with the [Dependency Manager](/tools/flow-cli/dependency-manager).
* Deploy a smart contract locally to the [Flow Emulator](/tools/emulator).
* Write and execute transactions to interact with a deployed smart contract.
* Display data from a Cadence smart contract on a React frontend using the [Flow Client Library](/tools/clients/fcl-js).

## Calling a Contract With a Script[​](#calling-a-contract-with-a-script "Direct link to Calling a Contract With a Script")

The `Counter` contract exposes a public function named `getCount()` that returns the current value of the counter. We can retrieve its value using a simple script written in the [Cadence](https://cadence-lang.org/) programming language. Scripts in Cadence are read-only operations that allow you to query data from the blockchain without changing any state.

Here's the script:

 `_10import Counter from 0x8a4dce54554b225d_10_10access(all)_10fun main(): Int {_10 return Counter.getCount()_10}`

Let's break down what this script does:

* **Import Statement**: `import Counter from 0x8a4dce54554b225d` tells the script to use the `Counter` contract deployed at the address `0x8a4dce54554b225d` on the `testnet`.
* **Main Function**: `access(all) fun main(): Int` defines the entry point of the script, which returns an `Int`.
* **Return Statement**: `return Counter.getCount()` calls the `getCount()` function from the `Counter` contract and returns its value.

### Steps to Execute the Script[​](#steps-to-execute-the-script "Direct link to Steps to Execute the Script")

* **Run the Script**: Click the Run button to execute the script.
* **View the Output**: Observe the output returned by the script. You should see the current value of the `count` variable, which is `0` unless it has been modified.

## Understanding the `Counter` Contract[​](#understanding-the-counter-contract "Direct link to understanding-the-counter-contract")

To fully grasp how the script works, it's important to understand the structure of the `Counter` contract. Below is the source code for the contract:

 `_31access(all) contract Counter {_31_31 access(all) var count: Int_31_31 // Event to be emitted when the counter is incremented_31 access(all) event CounterIncremented(newCount: Int)_31_31 // Event to be emitted when the counter is decremented_31 access(all) event CounterDecremented(newCount: Int)_31_31 init() {_31 self.count = 0_31 }_31_31 // Public function to increment the counter_31 access(all) fun increment() {_31 self.count = self.count + 1_31 emit CounterIncremented(newCount: self.count)_31 }_31_31 // Public function to decrement the counter_31 access(all) fun decrement() {_31 self.count = self.count - 1_31 emit CounterDecremented(newCount: self.count)_31 }_31_31 // Public function to get the current count_31 view access(all) fun getCount(): Int {_31 return self.count_31 }_31}`
### Breakdown of the Contract[​](#breakdown-of-the-contract "Direct link to Breakdown of the Contract")

* **Contract Declaration**: `access(all) contract Counter` declares a new contract named `Counter` that is accessible to everyone.
* **State Variable**: `access(all) var count: Int` declares a public variable `count` of type `Int`. The `access(all)` modifier means that this variable can be read by anyone.
* **Events**: Two events are declared:
  + `CounterIncremented(newCount: Int)`: Emitted when the counter is incremented.
  + `CounterDecremented(newCount: Int)`: Emitted when the counter is decremented.
* **Initializer**: The `init()` function initializes the `count` variable to `0` when the contract is deployed.
* **Public Functions**:
  + `increment()`: Increases the `count` by `1` and emits the `CounterIncremented` event.
  + `decrement()`: Decreases the `count` by `1` and emits the `CounterDecremented` event.
  + `getCount()`: Returns the current value of `count`. The `view` modifier indicates that this function does not modify the contract's state.

### Key Points[​](#key-points "Direct link to Key Points")

* **Public Access**: The `count` variable and the functions `increment()`, `decrement()`, and `getCount()` are all public, allowing anyone to interact with them.
* **State Modification**: The `increment()` and `decrement()` functions modify the state of the contract by changing the value of `count` and emitting events.
* **Read Costs**: Reading data from the blockchain is free on Flow. Executing scripts like the one you ran does not incur any costs. However, transactions that modify state, such as calling `increment()` or `decrement()`, will incur costs and require proper authorization.

### What's Next?[​](#whats-next "Direct link to What's Next?")

In the upcoming tutorials, you'll learn how to:

* **Modify the Counter**: Invoke the `increment()` and `decrement()` functions to update the `count` value.
* **Deploy Contracts**: Use the Flow CLI to deploy your own smart contracts.
* **Interact with Contracts Locally**: Use the Flow Emulator to test contracts in a local development environment.
* **Build Frontend Applications**: Display data from smart contracts in a React application using the Flow Client Library.

By understanding the `Counter` contract and how to interact with it, you're building a solid foundation for developing more complex applications on the Flow blockchain.

Proceed to the next tutorial to learn how to create your own contracts and deploy them live using the Flow CLI.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/getting-started/contract-interaction.md)Last updated on **Jan 7, 2025** by **Chase Fleming**[PreviousDifferences vs. EVM](/build/differences-vs-evm)[NextLocal Development](/build/getting-started/flow-cli)
###### Rate this page

😞😐😊

* [Objectives](#objectives)
* [Calling a Contract With a Script](#calling-a-contract-with-a-script)
  + [Steps to Execute the Script](#steps-to-execute-the-script)
* [Understanding the `Counter` Contract](#understanding-the-counter-contract)
  + [Breakdown of the Contract](#breakdown-of-the-contract)
  + [Key Points](#key-points)
  + [What's Next?](#whats-next)
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

