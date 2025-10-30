# Source: https://developers.flow.com/build/cadence/basics/collections

Collections | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          - [Network Architecture ↗️](/build/cadence/basics/network-architecture)- [Blocks](/build/cadence/basics/blocks)- [Collections](/build/cadence/basics/collections)- [Accounts](/build/cadence/basics/accounts)- [Transactions](/build/cadence/basics/transactions)- [Scripts](/build/cadence/basics/scripts)- [Fees](/build/cadence/basics/fees)- [MEV Resistance](/build/cadence/basics/mev-resistance)- [Events](/build/cadence/basics/events)- [FLOW Coin](/build/cadence/basics/flow-token)- [Smart Contracts ↙](/build/cadence/basics/smart-contracts)+ [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Basics* Collections

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