# Source: https://developers.flow.com/build/cadence/basics/scripts

Scripts | Flow Developer Portal



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

* * Cadence* Basics* Scripts

On this page

# Scripts

A script provides a light-weight method to query chain data.

It is executable Cadence code that can query for Flow execution state data but cannot modify it in any way.

Unlike a Flow transaction, a script is not signed and requires no transaction fees. Also unlike a transaction, a script can return a value back to the caller.
You can think of executing a script as a read-only operation, very similar to the `eth_call` RPC method on Ethereum.

Scripts are currently executed on either the Access Nodes or the Execution Nodes based on the Access node configuration.

Scripts are defined by the following the Cadence code:

`_10

// The 'main' function is the entry point function and every script needs to have one.

_10

access(all) fun main() {

_10

// Cadence statements to be executed go here

_10

}`

Scripts can return a typed value:

`_10

access(all) fun main(): Int {

_10

return 1 + 2

_10

}`

Scripts can also accept arguments:

`_10

access(all) fun main(arg: String): String {

_10

return "Hello ".concat(arg)

_10

}`

Scripts can call contract functions and query the state of a contract. To call a function on another contract, import it from its address and invoke the function:

`_10

import World from 0x01

_10

_10

access(all) fun main(): String {

_10

return World.hello()

_10

}`

Scripts can also be run against previous blocks, allowing you to query historic data from the Flow network. This is particularly useful for retrieving historical states of contracts or tracking changes over time.

## When to use a script?[​](#when-to-use-a-script "Direct link to When to use a script?")

Scripts can be used for the following:

1. Validating a transaction before submitting it e.g. checking if the payer has sufficient balance, the receiver account is setup correctly to receive a token or NFT etc.
2. Collecting chain data over time.
3. Continuously verifying accounts through a background job e.g. a Discord bot that verifies users by their Flow account.
4. Querying core contracts e.g. see [staking scripts and events](/protocol/staking/staking-scripts-events) for querying staking and epoch related information, see the scripts directory under each of the [core contract transactions](https://github.com/onflow/flow-core-contracts/tree/master/transactions) for other core contracts related scripts.

## Executing Scripts[​](#executing-scripts "Direct link to Executing Scripts")

### Access API[​](#access-api "Direct link to Access API")

A script can be executed by submitting it to the Access API provided by access nodes. Currently, there are three API endpoints that allow a user to execute scripts at the latest sealed block, a previous block height, or a previous block ID.

[**gRPC Script API**](/protocol/access-onchain-data#scripts)

[**REST Script API**](/http-api#tag/Scripts)

There are multiple SDKs implementing the above APIs for different languages:

[**Javascript SDK**](/build/tools/clients/fcl-js)

[**Go SDK**](/build/tools/clients/flow-go-sdk)

Find a list of all SDKs [here](/build/tools/clients)

### Flow CLI[​](#flow-cli "Direct link to Flow CLI")

You can also execute a script by using the [Flow CLI](/build/tools/flow-cli/scripts/execute-scripts):

`_10

flow scripts execute ./helloWorld.cdc`

A user can define their own scripts or can use already defined scripts by the contract authors that can be found by using the [FLIX](/build/tools/flow-cli/flix) service.

## Best Practices[​](#best-practices "Direct link to Best Practices")

Following are some recommendations on how to write efficient scripts:

1. **Simpler and shorter scripts**: Scripts, like transactions, are subject to computation limits (see [limitations](#limitations)). It is recommended to run shorter and simpler scripts which have low time complexity for a faster response. If you have a script with several nested loops, long iteration, or that queries many onchain fields, consider simplifying the script logic.
2. **Fewer state reads**: A script reads execution state and to get a faster response, it is best to limit the amount of state that is read by the script.
3. **Smaller length of array or dictionary type arguments**: If your script requires an array or a dictionary as an argument where each element causes a state lookup, instead of making a single script call passing in a long list, make multiple calls with a smaller subset of the array or dictionary.
4. **NFTCatalog**: If your script uses the [NFTCatalog](https://github.com/onflow/nft-catalog) functions, ensure that you use the [latest functions](https://github.com/onflow/nft-catalog?tab=readme-ov-file#using-the-catalog-for-marketplaces-and-other-nft-applications) and do not use any of the deprecated functions such as `getCatalog()`.

## Limitations[​](#limitations "Direct link to Limitations")

1. **Rate limit** - Script execution is subjected to API rate-limits imposed by the Access nodes and the Execution nodes. The rate limits for the Public Access nodes hosted by QuickNode are outlined [here](https://www.quicknode.com/docs/flow#endpoint-rate-limits).
2. **Computation limit** - Similar to a transaction, each script is also subjected to a computation limit. The specific value can be configured by individual Access and Execution node operators. Currently, the default compute unit (gas) limit for a script is 100,000.
3. **Historic block data limit**

   1. Script execution on execution nodes is restricted to approximately the last 100 blocks. Any request for script execution on an execution node on a past block (specified by block ID or block height) will fail if that block is more than 100 blocks in the past.
   2. Script execution on an access node can go much beyond the last 100 blocks but is restricted to the height when the [last](https://developers.flow.com/protocol/node-ops/node-operation/past-upgrades) network upgrade ([HCU](https://developers.flow.com/protocol/node-ops/node-operation/hcu) or spork) occurred.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/basics/scripts.md)

Last updated on **Nov 12, 2025** by **Brian Doyle**

[Previous

Transactions](/build/cadence/basics/transactions)[Next

Fees](/build/cadence/basics/fees)

###### Rate this page

😞😐😊

Copy as Markdown

* [When to use a script?](#when-to-use-a-script)* [Executing Scripts](#executing-scripts)
    + [Access API](#access-api)+ [Flow CLI](#flow-cli)* [Best Practices](#best-practices)* [Limitations](#limitations)

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