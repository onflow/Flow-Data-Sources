# Source: https://developers.flow.com/build/tools/clients/flow-go-sdk/migration-v0.25.0

Migration Guide v0.25.0 | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          + [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                        - [Flow Go SDK](/build/tools/clients/flow-go-sdk)

                          * [Flow Project Configuration](/build/tools/clients/flow-go-sdk/flowkit)* [Migration Guide v0.25.0](/build/tools/clients/flow-go-sdk/migration-v0.25.0)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Go SDK](/build/tools/clients/flow-go-sdk)* Migration Guide v0.25.0

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

Flow Project Configuration](/build/tools/clients/flow-go-sdk/flowkit)[Next

Error Codes](/build/tools/error-codes)

###### Rate this page

😞😐😊

Copy as Markdown

* [Migration](#migration)

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