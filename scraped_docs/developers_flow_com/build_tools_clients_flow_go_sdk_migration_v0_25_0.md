# Source: https://developers.flow.com/build/tools/clients/flow-go-sdk/migration-v0.25.0

Migration Guide v0.25.0 | Flow Developer Portal



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

  + [@onflow/react-sdk](/build/tools/react-sdk)
  + [Flow Emulator](/build/tools/emulator)
  + [Flow CLI](/build/tools/flow-cli)
  + [Cadence VS Code Extension](/build/tools/vscode-extension)
  + [Flow Dev Wallet](/build/tools/flow-dev-wallet)
  + [Client Tools](/build/tools/clients)

    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)
    - [Flow Go SDK](/build/tools/clients/flow-go-sdk)

      * [Migration Guide v0.25.0](/build/tools/clients/flow-go-sdk/migration-v0.25.0)
  + [Error Codes](/build/tools/error-codes)
  + [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* [Tools & SDKs](/build/tools)
* [Client Tools](/build/tools/clients)
* [Flow Go SDK](/build/tools/clients/flow-go-sdk)
* Migration Guide v0.25.0

On this page

# Migration Guide v0.25.0

The Go SDK version 0.25.0 introduced breaking changes in the API and package naming.
Changes were required to make the implementation of the new HTTP access node API available.

We will list all the changes and provide examples on how to migrate.

* **Renamed package: client -> access:** the `client` package was renamed to `access`
  which now includes both `grpc` package containing previously only gRPC implementation and
  also `http` package containing the new HTTP API implementation.
* **Removed package: convert:** the `convert` package was removed and all its functions were moved
  to each of the corresponding `grpc` or `http` packages. The methods were also changed to not be exported,
  so you can no longer use them outside the `convert` package.
* **New clients:** new clients were added each implementing the functions from the client interface
  and exposing a factory for creating them.
* **New Client Interface**: new client interface was created which is now network agnostic, meaning it
  doesn't any more expose additional options in the API that were used to pass gRPC specific options. You can
  still pass those options but you must use the network specific client as shown in the example bellow.
  The interface also changed some functions:
  + `GetCollectionByID` renamed to `GetCollection`
  + `Close() error` was added

### Migration[​](#migration "Direct link to Migration")

#### Creating a Client[​](#creating-a-client "Direct link to Creating a Client")

Creating a client for communicating with the access node has changed since it's now possible
to pick and choose between HTTP and gRPC communication protocols.

*Previous versions:*

`_10

// initialize a gRPC emulator client

_10

flowClient, err := client.New("127.0.0.1:3569", grpc.WithInsecure())`

*Version 0.25.0*:

`_10

// common client interface

_10

var flowClient access.Client

_10

_10

// initialize an http emulator client

_10

flowClient, err := http.NewClient(http.EmulatorHost)

_10

_10

// initialize a gPRC emulator client

_10

flowClient, err = grpc.NewClient(grpc.EmulatorHost)`

#### Using the gRPC Client with Options[​](#using-the-grpc-client-with-options "Direct link to Using the gRPC Client with Options")

Using the client is in most cases the same except for the advance case of passing additional
options to the gRPC client which is no longer possible in the base client, you must use a
network specific client as shown in the advanced example:

*Previous versions:*

`_10

// initialize a gRPC emulator client

_10

flowClient, err := client.New("127.0.0.1:3569", grpc.WithInsecure())

_10

latestBlock, err := flowClient.GetLatestBlock(ctx, true, MaxCallSendMsgSize(100))`

*Version 0.25.0:*

`_10

// initialize a grpc network specific client

_10

flowClient, err := NewBaseClient(

_10

grpc.EmulatorHost,

_10

grpc.WithTransportCredentials(insecure.NewCredentials()),

_10

)

_10

latestBlock, err := flowClient.GetLatestBlock(ctx, true, MaxCallSendMsgSize(100))`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/flow-go-sdk/migration-v0.25.0.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Flow Go SDK](/build/tools/clients/flow-go-sdk)[Next

Error Codes](/build/tools/error-codes)

###### Rate this page

😞😐😊

Copy as Markdown

* [Migration](#migration)

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