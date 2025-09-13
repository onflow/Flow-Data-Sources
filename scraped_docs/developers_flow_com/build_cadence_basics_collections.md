# Source: https://developers.flow.com/build/cadence/basics/collections

Collections | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)

    - [Network Architecture ↗️](/build/cadence/basics/network-architecture)
    - [Blocks](/build/cadence/basics/blocks)
    - [Collections](/build/cadence/basics/collections)
    - [Accounts](/build/cadence/basics/accounts)
    - [Transactions](/build/cadence/basics/transactions)
    - [Scripts](/build/cadence/basics/scripts)
    - [Fees](/build/cadence/basics/fees)
    - [MEV Resistance](/build/cadence/basics/mev-resistance)
    - [Events](/build/cadence/basics/events)
    - [FLOW Coin](/build/cadence/basics/flow-token)
    - [Smart Contracts ↙](/build/cadence/basics/smart-contracts)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/quickstart)

  + [EVM Quickstart](/build/evm/quickstart)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
* [Tools & SDKs](/build/tools)

* Cadence
* Flow Protocol
* Collections

On this page

# Collections

Collections link blocks and transactions together. Collection node clusters make these collections (using the HotStuff consensus algorithm), made up of an ordered list of one or more hashes of [signed transactions](/build/cadence/basics/transactions). In order to optimize data, blocks don't contain transactions (as they do on Ethereum). The benefits are transaction data does not get transferred to consensus nodes on the network which optimizes transfer speed and this architecture allows scaling of ingestion speed by adding collection clusters. Consensus nodes need to only agree on the order of transactions to be executed, they don't need to know the transaction payload, thus making blocks and collections lightweight. Collection nodes hold transaction payloads for anyone who requests them (e.g. execution nodes).

![Screenshot 2023-08-17 at 19.50.39.png](/assets/images/Screenshot_2023-08-17_at_19.50.39-2b14e257fed830fc8a1c9d315ac113ab.png)

## Collection Retrieval[​](#collection-retrieval "Direct link to Collection Retrieval")

You can use the Flow CLI to get the collection data by running:

`_10

flow collections get caff1a7f4a85534e69badcda59b73428a6824ef8103f09cb9eaeaa216c7d7d3f -n mainnet`

Find [more about the command in the CLI docs](/build/tools/flow-cli/get-flow-data/get-collections).

Collections can be obtained from the access node APIs, currently, there are two gRPC and REST APIs. You can find more information about them here:

[**gRPC Collection API**](/protocol/access-onchain-data#collections)

[**REST Collection API**](/http-api#tag/Collections)

There are multiple SDKs implementing the above APIs for different languages:

[**Javascript SDK**](/build/tools/clients/fcl-js)

[**Go SDK**](/build/tools/clients/flow-go-sdk)

Find a list of all SDKs [here](/build/tools/clients)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/basics/collections.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Blocks](/build/cadence/basics/blocks)[Next

Accounts](/build/cadence/basics/accounts)

###### Rate this page

😞😐😊

Copy as Markdown

* [Collection Retrieval](#collection-retrieval)

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
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.