# Source: https://developers.flow.com/build/basics/scripts

Scripts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)

  + [Network Architecture ↗️](/build/basics/network-architecture)
  + [Blocks](/build/basics/blocks)
  + [Collections](/build/basics/collections)
  + [Accounts](/build/basics/accounts)
  + [Transactions](/build/basics/transactions)
  + [Scripts](/build/basics/scripts)
  + [Fees](/build/basics/fees)
  + [MEV Resistance](/build/basics/mev-resistance)
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
* Scripts

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
4. Querying core contracts e.g. see [staking scripts and events](/networks/staking/staking-scripts-events) for querying staking and epoch related information, see the scripts directory under each of the [core contract transactions](https://github.com/onflow/flow-core-contracts/tree/master/transactions) for other core contracts related scripts.

## Executing Scripts[​](#executing-scripts "Direct link to Executing Scripts")

### Access API[​](#access-api "Direct link to Access API")

A script can be executed by submitting it to the Access API provided by access nodes. Currently, there are three API endpoints that allow a user to execute scripts at the latest sealed block, a previous block height, or a previous block ID.

[**gRPC Script API**](/networks/access-onchain-data#scripts)

[**REST Script API**](/http-api#tag/Scripts)

There are multiple SDKs implementing the above APIs for different languages:

[**Javascript SDK**](/tools/clients/fcl-js)

[**Go SDK**](/tools/clients/flow-go-sdk)

Find a list of all SDKs [here](/tools/clients)

### Flow CLI[​](#flow-cli "Direct link to Flow CLI")

You can also execute a script by using the [Flow CLI](/tools/flow-cli/scripts/execute-scripts):

`_10

flow scripts execute ./helloWorld.cdc`

A user can define their own scripts or can use already defined scripts by the contract authors that can be found by using the [FLIX](/tools/flow-cli/flix) service.

## Best Practices[​](#best-practices "Direct link to Best Practices")

Following are some recommendations on how to write efficient scripts:

1. **Simpler and shorter scripts**: Scripts, like transactions, are subject to computation limits (see [limitations](#limitations)). It is recommended to run shorter and simpler scripts which have low time complexity for a faster response. If you have a script with several nested loops, long iteration, or that queries many onchain fields, consider simplifying the script logic.
2. **Fewer state reads**: A script reads execution state and to get a faster response, it is best to limit the amount of state that is read by the script.
3. **Smaller length of array or dictionary type arguments**: If your script requires an array or a dictionary as an argument where each element causes a state lookup, instead of making a single script call passing in a long list, make multiple calls with a smaller subset of the array or dictionary.
4. **NFTCatalog**: If your script uses the [NFTCatalog](https://github.com/onflow/nft-catalog) functions, ensure that you use the [latest functions](https://github.com/onflow/nft-catalog?tab=readme-ov-file#using-the-catalog-for-marketplaces-and-other-nft-applications) and do not use any of the deprecated functions such as `getCatalog()`.

## Limitations[​](#limitations "Direct link to Limitations")

1. **Rate limit** - Script execution is subjected to API rate-limits imposed by the Access nodes and the Execution nodes. The rate limits for the Public Access nodes hosted by QuickNode are outlined [here](https://www.quicknode.com/docs/flow#endpoint-rate-limits).
2. **Computation limit** - Similar to a transaction, each script is also subjected to a computation limit. The specific value can be configured by individual Access and Execution node operators. Currently, the default compute (gas) limit for a script is 100,000.
3. **Historic block data limit**

   1. Script execution on execution nodes is restricted to approximately the last 100 blocks. Any request for script execution on an execution node on a past block (specified by block ID or block height) will fail if that block is more than 100 blocks in the past.
   2. Script execution on an access node can go much beyond the last 100 blocks but is restricted to the height when the [last](https://developers.flow.com/networks/node-ops/node-operation/past-sporks) network upgrade ([HCU](https://developers.flow.com/networks/node-ops/node-operation/hcu) or spork) occurred.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/basics/scripts.md)

Last updated on **Apr 1, 2025** by **Brian Doyle**

[Previous

Transactions](/build/basics/transactions)[Next

Fees](/build/basics/fees)

###### Rate this page

😞😐😊

* [When to use a script?](#when-to-use-a-script)
* [Executing Scripts](#executing-scripts)
  + [Access API](#access-api)
  + [Flow CLI](#flow-cli)
* [Best Practices](#best-practices)
* [Limitations](#limitations)

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
* [Flowscan Mainnet](https://flowscan.io/)
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