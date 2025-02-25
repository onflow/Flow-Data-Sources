# Source: https://developers.flow.com/build/basics/collections

Collections | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)

  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [Events](/build/basics/events)
  + [FLOW Coin](/build/basics/flow-token)
  + [Smart Contracts ↙](/build/basics/smart-contracts)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Flow Protocol
* Collections

On this page

# Collections

Collections link blocks and transactions together. Collection node clusters make these collections (using the HotStuff consensus algorithm), made up of an ordered list of one or more hashes of [signed transactions](/build/basics/transactions). In order to optimize data, blocks don't contain transactions (as they do on Ethereum). The benefits are transaction data does not get transferred to consensus nodes on the network which optimizes transfer speed and this architecture allows scaling of ingestion speed by adding collection clusters. Consensus nodes need to only agree on the order of transactions to be executed, they don't need to know the transaction payload, thus making blocks and collections lightweight. Collection nodes hold transaction payloads for anyone who requests them (e.g. execution nodes).

![Screenshot 2023-08-17 at 19.50.39.png](/assets/images/Screenshot_2023-08-17_at_19.50.39-2b14e257fed830fc8a1c9d315ac113ab.png)

## Collection Retrieval[​](#collection-retrieval "Direct link to Collection Retrieval")

You can use the Flow CLI to get the collection data by running:

`_10

flow collections get caff1a7f4a85534e69badcda59b73428a6824ef8103f09cb9eaeaa216c7d7d3f -n mainnet`

Find [more about the command in the CLI docs](/tools/flow-cli/get-flow-data/get-collections).

Collections can be obtained from the access node APIs, currently, there are two gRPC and REST APIs. You can find more information about them here:

[**gRPC Collection API**](/networks/access-onchain-data#collections)

[**REST Collection API**](/http-api#tag/Collections)

There are multiple SDKs implementing the above APIs for different languages:

[**Javascript SDK**](/tools/clients/fcl-js)

[**Go SDK**](/tools/clients/flow-go-sdk)

Find a list of all SDKs [here](/tools/clients)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/collections.md)

Last updated on **Feb 18, 2025** by **BT.Wood(Tang Bo Hao)**

[Previous

Blocks](/build/basics/blocks)[Next

Accounts](/build/basics/accounts)

###### Rate this page

😞😐😊

* [Collection Retrieval](#collection-retrieval)

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