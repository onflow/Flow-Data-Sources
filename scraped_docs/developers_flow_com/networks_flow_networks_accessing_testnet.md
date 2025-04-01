# Source: https://developers.flow.com/networks/flow-networks/accessing-testnet

Flow Testnet | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)

  + [Mainnet](/networks/flow-networks/accessing-mainnet)
  + [Testnet](/networks/flow-networks/accessing-testnet)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Flow Networks](/networks/flow-networks)
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

You can review [all available core contracts](/build/core-contracts) deployed to the Testnet to identify which ones you want to import.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/flow-networks/accessing-testnet.md)

Last updated on **Mar 14, 2025** by **j pimmel**

[Previous

Mainnet](/networks/flow-networks/accessing-mainnet)[Next

Networks](/networks)

###### Rate this page

😞😐😊

* [About Flow Testnet](#about-flow-testnet)
* [Accessing Flow Testnet](#accessing-flow-testnet)
  + [Generating Testnet Key Pair](#generating-testnet-key-pair)
* [Account Creation and Token Funding Requests](#account-creation-and-token-funding-requests)
* [Important Smart Contract Addresses](#important-smart-contract-addresses)

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