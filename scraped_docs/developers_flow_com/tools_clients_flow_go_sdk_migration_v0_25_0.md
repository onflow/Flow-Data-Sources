# Source: https://developers.flow.com/tools/clients/flow-go-sdk/migration-v0.25.0

Migration Guide v0.25.0 | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)

    - [Migration Guide v0.25.0](/tools/clients/flow-go-sdk/migration-v0.25.0)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

* [Client Tools](/tools/clients)
* [Flow Go SDK](/tools/clients/flow-go-sdk)
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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/flow-go-sdk/migration-v0.25.0.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Flow Go SDK](/tools/clients/flow-go-sdk)[Next

Tools](/tools)

###### Rate this page

😞😐😊

* [Migration](#migration)

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