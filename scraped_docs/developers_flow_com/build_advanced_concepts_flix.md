# Source: https://developers.flow.com/build/advanced-concepts/flix




FLIX (Flow Interaction Templates) | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
  + [Account Abstraction](/build/advanced-concepts/account-abstraction)
  + [FLIX (Flow Interaction Templates)](/build/advanced-concepts/flix)
  + [NFT Metadata Views](/build/advanced-concepts/metadata-views)
  + [VRF (Randomness) in Cadence](/build/advanced-concepts/randomness)
  + [Scaling Transactions from a Single Account](/build/advanced-concepts/scaling)
* [Guides](/build/guides/fungible-token)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)


* Advanced Concepts
* FLIX (Flow Interaction Templates)
On this page
# FLIX (Flow Interaction Templates)

Flow Interaction Templates is a standard for how contract developers, wallets, users, auditors, and applications can create, audit, and verify the intent, security, and metadata of Flow scripts and transactions, with the goal to improve the understandability and security of authorizing transactions and promote patterns for change resilient composability of applications on Flow.

Interaction Templates provide a way to use and reuse existing scripts and transactions, as well as to provide more metadata such as a human-readable title and description of what the transaction or script will do, which can be used by the developer as well as the user of the application.

By using FLIX transactions and scripts, developers don’t have to write their own for common operations!

Read more about the design and purpose of FLIX in the [FLIP](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md)

## Using FLIX[​](#using-flix "Direct link to Using FLIX")

Flow makes FLIX available through an API available at flix.flow.com.

You can query a FLIX API to get an Interaction Template. An example query looks like: <https://flix.flow.com/v1/templates?name=transfer-flow>

You can read more about how to query a FLIX API in the documentation available here: <https://github.com/onflow/flow-interaction-template-service>

info

The FLIX working group is currently working on a protocol to publish FLIX templates on-chain.

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

See the `hello-world-web` [README](https://github.com/onflow/hello-world-web/tree/main) for more information on how to generate and execute FLIX templates here [flow-cli flix](/tools/flow-cli/flix) commands

### Clients[​](#clients "Direct link to Clients")

There are currently two clients that have integrated with FLIX that you can use:

**Go client** <https://github.com/onflow/flixkit-go>

**FCL client you** read how to get started [tools/clients/fcl-js/interaction-templates](/tools/clients/fcl-js/interaction-templates)

## (Advanced) Running a FLIX API[​](#advanced-running-a-flix-api "Direct link to (Advanced) Running a FLIX API")

Flow provides an implementation of the Flow interaction template service as an open-source project. If you wish to run your own API, you can find the repository here: <https://github.com/onflow/flow-interaction-template-service>

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/advanced-concepts/flix.md)Last updated on **Jan 14, 2025** by **Giovanni Sanchez**[PreviousAccount Abstraction](/build/advanced-concepts/account-abstraction)[NextNFT Metadata Views](/build/advanced-concepts/metadata-views)
###### Rate this page

😞😐😊

* [Using FLIX](#using-flix)
  + [Example](#example)
  + [Clients](#clients)
* [(Advanced) Running a FLIX API](#advanced-running-a-flix-api)
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

