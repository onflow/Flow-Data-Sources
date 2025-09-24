# Source: https://developers.flow.com/protocol/flow-networks/accessing-testnet

Flow Testnet | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  + [Mainnet](/protocol/flow-networks/accessing-mainnet)
  + [Testnet](/protocol/flow-networks/accessing-testnet)
* [Networks](/protocol)
* [Flow Network Architecture](/protocol/network-architecture)
* [Staking and Epochs](/protocol/staking)
* [Node Ops](/protocol/node-ops)
* [Accessing Data](/protocol/access-onchain-data)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

* [Flow Networks](/protocol/flow-networks)
* Testnet

On this page

# Flow Testnet

## About Flow Testnet[​](#about-flow-testnet "Direct link to About Flow Testnet")

Flow Testnet is Flow's official testing and development network. It is intended to provide a staging and testing environment for dApp developers.
It aims to balance similarity with Mainnet with being a productive development environment, resulting in the following key differences:

* Testnet has significantly fewer validator nodes, resulting in a faster block rate compared to Mainnet
* Testnet is configured with shorter epochs (about 12 hours, compared to 7 days on Mainnet)
* Testnet receives software upgrades up to 2 weeks before Mainnet

## Accessing Flow Testnet[​](#accessing-flow-testnet "Direct link to Accessing Flow Testnet")

Flow Testnet is available for access at this URL:

`_10

access.devnet.nodes.onflow.org:9000`

For example, to access the network using the [Flow Go SDK](https://github.com/onflow/flow-go-sdk):

`_10

import "github.com/onflow/flow-go-sdk/client"

_10

_10

func main() {

_10

flowAccessAddress := "access.devnet.nodes.onflow.org:9000"

_10

flowClient, _ := client.New(flowAccessAddress, grpc.WithInsecure())

_10

// ...

_10

}`

### Generating Testnet Key Pair[​](#generating-testnet-key-pair "Direct link to Generating Testnet Key Pair")

You can generate a new key pair with the [Flow CLI](https://github.com/onflow/flow-cli) as follows:

`_10

> flow keys generate

_10

_10

🙏 If you want to create an account on Testnet with the generated keys use this link:

_10

https://testnet-faucet.onflow.org/?key= cc1c3d72...

_10

_10

_10

🔴️ Store private key safely and don't share with anyone!

_10

Private Key 246256f3...

_10

Public Key cc1c3d72...`

**Note: By default, this command generates an ECDSA key pair on the P-256 curve. Keep in mind, the CLI is intended for development purposes only and is not recommended for production use. Handling keys using a Key Management Service is the best practice.**

## Account Creation and Token Funding Requests[​](#account-creation-and-token-funding-requests "Direct link to Account Creation and Token Funding Requests")

Accounts and tokens for testing can be obtained through the [testnet faucet](https://testnet-faucet.onflow.org/). If you generated the keypair through the CLI, you can click on the URL provided to create an account and request testnet FLOW tokens.

## Important Smart Contract Addresses[​](#important-smart-contract-addresses "Direct link to Important Smart Contract Addresses")

You can review [all available core contracts](/build/cadence/core-contracts) deployed to the Testnet to identify which ones you want to import.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/flow-networks/accessing-testnet.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Mainnet](/protocol/flow-networks/accessing-mainnet)[Next

Networks](/protocol)

###### Rate this page

😞😐😊

Copy as Markdown

* [About Flow Testnet](#about-flow-testnet)
* [Accessing Flow Testnet](#accessing-flow-testnet)
  + [Generating Testnet Key Pair](#generating-testnet-key-pair)
* [Account Creation and Token Funding Requests](#account-creation-and-token-funding-requests)
* [Important Smart Contract Addresses](#important-smart-contract-addresses)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
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
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.