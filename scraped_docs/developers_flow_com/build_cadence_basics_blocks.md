# Source: https://developers.flow.com/build/cadence/basics/blocks

Blocks | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          - [Network Architecture ↗️](/build/cadence/basics/network-architecture)- [Blocks](/build/cadence/basics/blocks)- [Collections](/build/cadence/basics/collections)- [Accounts](/build/cadence/basics/accounts)- [Transactions](/build/cadence/basics/transactions)- [Scripts](/build/cadence/basics/scripts)- [Fees](/build/cadence/basics/fees)- [MEV Resistance](/build/cadence/basics/mev-resistance)- [Events](/build/cadence/basics/events)- [FLOW Coin](/build/cadence/basics/flow-token)- [Smart Contracts ↙](/build/cadence/basics/smart-contracts)+ [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Basics* Blocks

On this page

# Blocks

Blocks are entities that make up the Flow blockchain. Each block contains a list of [transactions](/build/cadence/basics/transactions) that were executed and as a result, changed the global blockchain state. Each block is identified by a unique ID which is a cryptographic hash of the block contents. Block also includes a link to the parent block ID, which creates a linked list of blocks called the Flow blockchain.

The unique block ID serves as proof of the block contents which any oberver can independently validate. Interesting cryptographic properties of the hash that make up the block ID guarantee that if any change is made to the block data, it would produce a different hash. Because blocks are linked, a different hash would break the link as it would no longer be referenced in the next block.

A very basic representation of blocks is:

![Screenshot 2023-08-16 at 15.16.38.png](/assets/images/Screenshot_2023-08-16_at_15.16.38-148cd864a5ee56f5f4c9b83ce3794e8a.png)

Blocks are ordered from the genesis block 0 up to the latest block. Each block contains an ordered list of transactions. This is how the Flow blockchain preserves the complete history of all the changes made to the state from the start to the current state.

Each block contains more data which is divided into **block header** and **block payload**. There are many representations of block data within the Flow protocol. APIs, node types, and specific components within the node may view a block from different perspectives. For the purpose of this document, we will talk about block data we expose through APIs to the clients.

![Screenshot 2023-08-16 at 10.50.53.png](/assets/images/Screenshot_2023-08-16_at_10.50.53-1f1b7b4eefcb77fcb150651d77194346.png)

### Block header[​](#block-header "Direct link to Block header")

The Block header contains the following fields:

* **ID** represents the block's unique identifier, which is derived from the hashing block header, which includes the payload hash. The algorithm used on Flow to hash the content and get an identifier is SHA3 256. This ID is a commitment to all the values in the block staying the same.
* **Parent ID** is a link to the previous block ID in the list that makes up the blockchain.
* **Height** is the block sequence number, where block 0 was the first block produced, and each next block increments the value by one.
* **Timestamp** is the timestamp at which this block was proposed by the consensus node. Depending on your use case, this time might not be accurate enough, [read more about how to measure time on the Flow blockchain](https://cadence-lang.org/docs/measuring-time#time-on-the-flow-blockchain).
* **Payload Hash** represents the payload hash that is included when producing the ID of the block. To calculate the payload hash take Merkle root hashes of collection guarantees, seals, execution receipts, and execution results and hash them together. For more information, see the block payload section below.

### Block payload[​](#block-payload "Direct link to Block payload")

The block payload contains the following fields:

* **Collection Guarantees** is a list of collection IDs with the signatures from the collection nodes that produced the collections. This acts as a guarantee by collection nodes that [transactions](/build/cadence/basics/transactions)data in the collection will be available on the collection node if requested by other nodes at a later time. Flow purposely skips including transaction data in a block, makes blocks as small as possible, and produces new blocks by consensus nodes fast, because consensus nodes have to sync the proposed block between nodes, and that data should be the smallest possible. The consensus nodes don't really care what will a transaction do as long as it's valid, they only need to define an order of those transactions in a block.
* **Block Seals** is the attestation by verification nodes that the transactions in a previously executed block have been verified. This seals a previous block referenced by the block ID. It also references the result ID and execution root hash. It contains signatures of the verification nodes that produced the seal.

## Lifecycle and status[​](#lifecycle-and-status "Direct link to Lifecycle and status")

Block status is not a value stored inside the block itself, but it represents the lifecycle of a block. We derive this value based on the block inclusion in the Flow blockchain and present it to the user as it acts as an important indicator of the finality of the changes the block contains.

Here, we'll give an overview of the different phases a block goes through. [More details can be found in the whitepaper](https://flow.com/technical-paper). Also, a lot of the block states are not necessarily important to the developer but only important to the Flow blockchain's function.

New blocks are constantly being proposed even if no new transactions are submitted to the network. Consensus nodes are in charge of blocks production. They use a consensus algorithm (an implementation of HotStuff) to agree on what the new block will be. A block contains the ordered list of collections and each collection contains an ordered list of transactions. This is an important fact to reiterate. A block serves as a list of transitions to the Flow state machine. It documents, as an ordered list, all the changes transactions will make to the state.

A block that is [agreed upon by the consensus nodes via an implementation of HotStuff consensus algorithm](https://arxiv.org/pdf/2002.07403.pdf) to be the next block is **finalized**. This means the block won't change anymore and it will next be executed by the execution node. Be careful because until a block is **sealed** the changes are not to be trusted. After verification nodes validate and agree on the correctness of execution results, a block is sealed and consensus nodes will include these seals in the new block.

In summary, a block can be either **finalized** which guarantees transactions included in the block will stay the same and will be executed, and **sealed** which means the block execution was verified.

![Screenshot 2023-08-16 at 10.48.26.png](/assets/images/Screenshot_2023-08-16_at_10.48.26-8013388182846fde95bf7a07c036d669.png)

## Block Retrieval[​](#block-retrieval "Direct link to Block Retrieval")

You can use the Flow CLI to get the block data by running:

`_10

flow blocks get latest -network mainnet`

Find [more about the command in the CLI docs](/build/tools/flow-cli/get-flow-data/get-blocks)

Blocks can be obtained from the access node APIs, currently, there are two gRPC and REST APIs. You can find more information about them here:

[**gRPC Block API**](/protocol/access-onchain-data#blocks)

[**REST Block API**](/http-api#tag/Blocks)

There are multiple SDKs that implement the above APIs for different languages:

[**Javascript SDK**](/build/tools/clients/fcl-js)

[**Go SDK**](/build/tools/clients/flow-go-sdk)

Find a list of all SDKs [here](/build/tools/clients).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/basics/blocks.md)

Last updated on **Dec 9, 2025** by **Brian Doyle**

[Previous

Network Architecture ↗️](/build/cadence/basics/network-architecture)[Next

Collections](/build/cadence/basics/collections)

###### Rate this page

😞😐😊

Copy as Markdown

* [Block header](#block-header)* [Block payload](#block-payload)* [Lifecycle and status](#lifecycle-and-status)* [Block Retrieval](#block-retrieval)

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