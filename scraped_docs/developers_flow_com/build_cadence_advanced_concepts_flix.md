# Source: https://developers.flow.com/build/cadence/advanced-concepts/flix

FLIX (Flow Interaction Templates) | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Cadence](/build/cadence/getting-started)

  + [Getting Started](/build/cadence/getting-started)
  + [Differences vs. EVM](/build/cadence/differences-vs-evm)
  + [Flow Protocol](/build/cadence/basics/network-architecture)
  + [App Architecture](/build/cadence/app-architecture)
  + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)
  + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

    - [Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)
    - [FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)
    - [NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)
    - [VRF (Randomness) in Cadence](/build/cadence/advanced-concepts/randomness)
    - [Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)
  + [Guides](/build/cadence/guides/account-linking)
  + [Core Smart Contracts](/build/cadence/core-contracts)
  + [Explore More](/build/cadence/explore-more)
* [Solidity (EVM)](/build/evm/about)

  + [Why EVM on Flow](/build/evm/about)
  + [How it Works](/build/evm/how-it-works)
  + [Using Flow EVM](/build/evm/using)
  + [Network Information](/build/evm/networks)
  + [EVM Quickstart](/build/evm/quickstart)
  + [Fees](/build/evm/fees)
  + [Accounts](/build/evm/accounts)
  + [Cross-chain Bridges ↙](/evm/cross-chain-bridges)
  + [Faucets ↙](/evm/faucets)
  + [Block Explorers ↙](/evm/block-explorers)
  + [Guides](/build/evm/guides)
* [Tools & SDKs](/build/tools)

* Cadence
* Advanced Concepts
* FLIX (Flow Interaction Templates)

On this page

# FLIX (Flow Interaction Templates)

Flow Interaction Templates is a standard for how contract developers, wallets, users, auditors, and applications can create, audit, and verify the intent, security, and metadata of Flow scripts and transactions, with the goal to improve the understandability and security of authorizing transactions and promote patterns for change resilient composability of applications on Flow.

Interaction Templates provide a way to use and reuse existing scripts and transactions, as well as to provide more metadata such as a human-readable title and description of what the transaction or script will do, which can be used by the developer as well as the user of the application.

By using FLIX transactions and scripts, developers don't have to write their own for common operations!

Read more about the design and purpose of FLIX in the [FLIP](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md)

## Using FLIX[​](#using-flix "Direct link to Using FLIX")

Flow makes FLIX available through an API available at flix.flow.com.

You can query a FLIX API to get an Interaction Template. An example query looks like: <https://flix.flow.com/v1/templates?name=transfer-flow>

You can read more about how to query a FLIX API in the documentation available here: <https://github.com/onflow/flow-interaction-template-service>

info

The FLIX working group is currently working on a protocol to publish FLIX templates onchain.

### Example[​](#example "Direct link to Example")

How to integrate FLIX across different developer teams? For this example there are two github repositories.

* (smart contracts) <https://github.com/onflow/hello-world-flix>
* (web development) <https://github.com/onflow/hello-world-web>

The Smart contract developer creates FLIX templates and makes them available in github, these can be versioned. Example is `v0.1.0` release, the templates are available for a specific version. In this example the templates are located at:

* <https://github.com/onflow/hello-world-flix/blob/v0.1.0/cadence/templates/ReadHelloWorld.template.json>
* <https://github.com/onflow/hello-world-flix/blob/v0.1.0/cadence/templates/UpdateHelloWorld.template.json>

Developers can use FLIX templates from the smart contract github to interact with their smart contracts. They simply need the FLIX template URLs to create binding files (TypeScript or JavaScript). One major benefit is the web developers don't need to learn Cadence or copy Cadence to their repository in order to integrate with existing smart contracts.

TypeScript code generated from templates:

* <https://github.com/onflow/hello-world-web/blob/main/app/cadence/readHelloWorld.ts>
* <https://github.com/onflow/hello-world-web/blob/main/app/cadence/updateHelloWorld.ts>

warning

manually added "@ts-ignore" in generated file because of linting error. 'template' property is typed as "object" when it should also allow strings (url to flix template file). There is current a dev effort that will fix this linting issue.

See the `hello-world-web` [README](https://github.com/onflow/hello-world-web/tree/main) for more information on how to generate and execute FLIX templates here [flow-cli flix](/build/tools/flow-cli/flix) commands

### Clients[​](#clients "Direct link to Clients")

There are currently two clients that have integrated with FLIX that you can use:

**Go client** <https://github.com/onflow/flixkit-go>

**FCL client you** read how to get started [tools/clients/fcl-js/interaction-templates](/build/tools/clients/fcl-js/interaction-templates)

## (Advanced) Running a FLIX API[​](#advanced-running-a-flix-api "Direct link to (Advanced) Running a FLIX API")

Flow provides an implementation of the Flow interaction template service as an open-source project. If you wish to run your own API, you can find the repository here: <https://github.com/onflow/flow-interaction-template-service>

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/advanced-concepts/flix.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)[Next

NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)

###### Rate this page

😞😐😊

Copy as Markdown

* [Using FLIX](#using-flix)
  + [Example](#example)
  + [Clients](#clients)
* [(Advanced) Running a FLIX API](#advanced-running-a-flix-api)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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
* [EVM](/build/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.