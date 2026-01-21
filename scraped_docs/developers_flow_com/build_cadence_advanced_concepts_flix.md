# Source: https://developers.flow.com/build/cadence/advanced-concepts/flix

FLIX (Flow Interaction Templates) | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/computation-profiling)

              - [Cadence Computation Profiling](/build/cadence/advanced-concepts/computation-profiling)- [Build Faster with Flow’s Native Account Abstraction](/build/cadence/advanced-concepts/account-abstraction)- [Scheduled Transactions](/build/cadence/advanced-concepts/scheduled-transactions)- [Cron-Based Recurring Transactions](/build/cadence/advanced-concepts/flow-cron)- [Passkeys](/build/cadence/advanced-concepts/passkeys)- [FLIX (Flow Interaction Templates)](/build/cadence/advanced-concepts/flix)- [NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)- [VRF (Randomness) in Cadence](/build/cadence/advanced-concepts/randomness)- [Scaling Transactions from a Single Account](/build/cadence/advanced-concepts/scaling)+ [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* Advanced Concepts* FLIX (Flow Interaction Templates)

On this page

# Flow Interaction Templates

Flow Interaction Templates (FLIX) is a standard for how contract developers, wallets, users, auditors, and applications can create, audit, and verify the intent, security, and metadata of Flow scripts and transactions, with the goal to improve the understandability and security of transaction authorizations and promote patterns for change resilient composability of applications on Flow.

Interaction Templates provide a way to use and reuse current scripts and transactions, as well as to provide more metadata such as a human-readable title and description of what the transaction or script will do, which the developer can use, as well as the application user.

With FLIX transactions and scripts, developers don't have to write their own for common operations!

Read more about the design and purpose of FLIX in the [FLIP](https://github.com/onflow/flips/blob/main/application/20220503-interaction-templates.md).

## Use FLIX[​](#use-flix "Direct link to Use FLIX")

Flow makes FLIX available through an API available at flix.flow.com.

You can query a FLIX API to get an Interaction Template. An example query looks like [this](https://flix.flow.com/v1/templates?name=transfer-flow).

You can read more about how to query a FLIX API in the documentation available [here](https://github.com/onflow/flow-interaction-template-service).

info

The FLIX working group is currently working on a protocol to publish FLIX templates onchain.

### Example[​](#example "Direct link to Example")

How to integrate FLIX across different developer teams? For this example there are two GitHub repositories.

* (smart contracts) [<https://github.com/onflow/hello-world-flix>]
* (web development) [<https://github.com/onflow/hello-world-web>]

The Smart contract developer creates FLIX templates and makes them available in GitHub, these can be versioned. Example is `v0.1.0` release, the templates are available for a specific version. In this example the templates are located at:

* <https://github.com/onflow/hello-world-flix/blob/v0.1.0/cadence/templates/ReadHelloWorld.template.json>
* <https://github.com/onflow/hello-world-flix/blob/v0.1.0/cadence/templates/UpdateHelloWorld.template.json>

Developers can use FLIX templates from the smart contract github to interact with their smart contracts. They simply need the FLIX template URLs to create binding files (TypeScript or JavaScript). One major benefit is the web developers don't need to learn Cadence or copy Cadence to their repository in order to integrate with current smart contracts.

TypeScript code generated from templates:

* <https://github.com/onflow/hello-world-web/blob/main/app/cadence/readHelloWorld.ts>
* <https://github.com/onflow/hello-world-web/blob/main/app/cadence/updateHelloWorld.ts>

warning

manually added "@ts-ignore" in generated file because of linting error. 'template' property is typed as "object" when it should also allow strings (url to flix template file). There is current a dev effort that will fix this linting issue.

See the `hello-world-web` [README]for more information on how to generate and execute FLIX templates here.

[flow-cli flix]

### Clients[​](#clients "Direct link to Clients")

There are currently two clients that have integrated with FLIX that you can use:

**Go client** [<https://github.com/onflow/flixkit-go>]

**FCL client you** read how to get started [tools/clients/fcl-js/interaction-templates]

## (Advanced) Run a FLIX API[​](#advanced-run-a-flix-api "Direct link to (Advanced) Run a FLIX API")

Flow provides an implementation of the Flow interaction template service as an open-source project. If you wish to run your own API, you can find the repository at [<https://github.com/onflow/flow-interaction-template-service>].

[<https://github.com/onflow/hello-world-flix>]: <https://github.com/onflow/hello-world-flix>)
[<https://github.com/onflow/hello-world-web>]: <https://github.com/onflow/hello-world-web>)
[README]: <https://github.com/onflow/hello-world-web/tree/main>
[flow-cli flix]: ../../../build/tools/flow-cli/flix.md
[<https://github.com/onflow/flixkit-go>]: <https://github.com/onflow/flixkit-go>
[tools/clients/fcl-js/interaction-templates]: ../../../build/tools/clients/fcl-js/interaction-templates.mdx
[<https://github.com/onflow/flow-interaction-template-service>]: <https://github.com/onflow/flow-interaction-template-service>

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/advanced-concepts/flix.md)

Last updated on **Dec 1, 2025** by **cshannon1218**

[Previous

Passkeys](/build/cadence/advanced-concepts/passkeys)[Next

NFT Metadata Views](/build/cadence/advanced-concepts/metadata-views)

###### Rate this page

😞😐😊

Copy as Markdown

* [Use FLIX](#use-flix)
  + [Example](#example)+ [Clients](#clients)* [(Advanced) Run a FLIX API](#advanced-run-a-flix-api)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.