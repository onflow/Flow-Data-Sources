# Source: https://developers.flow.com/networks/flow-networks/accessing-mainnet




Flow Mainnet | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Mainnet
On this page
# Flow Mainnet

## Accessing Flow Mainnet[​](#accessing-flow-mainnet "Direct link to Accessing Flow Mainnet")

The Flow Mainnet is available for access at this URL:

 `_10access.mainnet.nodes.onflow.org:9000`

For example, to access the network using the [Flow Go SDK](https://github.com/onflow/flow-go-sdk):

 `_10import "github.com/onflow/flow-go-sdk/client"_10_10func main() {_10 flowAccessAddress := "access.mainnet.nodes.onflow.org:9000"_10 flowClient, _ := client.New(flowAccessAddress, grpc.WithInsecure())_10 // ..._10}`
## Account Creation[​](#account-creation "Direct link to Account Creation")

You can follow the [Flow Port account creation steps](/networks/flow-port) to create a new mainnet account.

If you prefer watching a video, check out this tutorial:

## Generating a Non-Custodial Account[​](#generating-a-non-custodial-account "Direct link to Generating a Non-Custodial Account")

A non-custodial account will make sure you are the only one holding the keys to your account.

You can follow the following steps to add a non-custodial account:

First, generate a new key pair with the [Flow CLI](https://github.com/onflow/flow-cli):

 `_10> flow keys generate --network=mainnet_10_10🔴️ Store private key safely and don't share with anyone!_10Private Key 5b438..._10Public Key 1bdc5...`
> **Note**: By default, this command generates an ECDSA key pair on the P-256 curve. Keep in mind the CLI is intended for development purposes only and is not recommended for production use. Handling keys using a Key Management Service is the best practice.

Take a note of the public key and go back to Flow Port. Open the ["Create a new account" page](https://port.onflow.org/transaction?hash=a0a78aa7821144efd5ebb974bb52ba04609ce76c3863af9d45348db93937cf98&showcode=false&weight=1000&halg=3).

On the page, enter your public key from the CLI, ensure the hash algorithm is set to `SHA3_256` and the weight is set to `1000`. Finally, check the box confirming correctness and hit 'Submit'.

> **Important**: Your account needs to have at least 0.002 FLOW for the account creation. More details can be found [in this guide](/build/basics/fees#storage).

Once the transaction is sealed, you should scroll down to the events section and locate the `flow.AccountCreated` event with the newly generated address.

![flow-port-sealed](/assets/images/port-sealed-tx-d6bd12b3044b726057506ae440ae6967.png)

Make sure to take a note of the address. If you want to verify the public key for this address, you can visit [flow-view-source](https://flow-view-source.com/).

## Important Mainnet Smart Contract Addresses[​](#important-mainnet-smart-contract-addresses "Direct link to Important Mainnet Smart Contract Addresses")

You can review [all available core contracts](/build/core-contracts) deployed to the mainnet to identify which ones you want to import.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/flow-networks/accessing-mainnet.md)Last updated on **Jan 3, 2025** by **Brian Doyle**[PreviousFlow Networks](/networks/flow-networks)[NextTestnet](/networks/flow-networks/accessing-testnet)
###### Rate this page

😞😐😊

* [Accessing Flow Mainnet](#accessing-flow-mainnet)
* [Account Creation](#account-creation)
* [Generating a Non-Custodial Account](#generating-a-non-custodial-account)
* [Important Mainnet Smart Contract Addresses](#important-mainnet-smart-contract-addresses)
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

