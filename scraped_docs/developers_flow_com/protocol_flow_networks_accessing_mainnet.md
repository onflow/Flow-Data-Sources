# Source: https://developers.flow.com/protocol/flow-networks/accessing-mainnet

Flow Mainnet | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  + [Mainnet](/protocol/flow-networks/accessing-mainnet)+ [Testnet](/protocol/flow-networks/accessing-testnet)* [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Flow Networks](/protocol/flow-networks)* Mainnet

On this page

# Flow Mainnet

## Accessing Flow Mainnet[​](#accessing-flow-mainnet "Direct link to Accessing Flow Mainnet")

The Flow Mainnet is available for access at this URL:

`_10

access.mainnet.nodes.onflow.org:9000`

For example, to access the network using the [Flow Go SDK](https://github.com/onflow/flow-go-sdk):

`_10

import "github.com/onflow/flow-go-sdk/client"

_10

_10

func main() {

_10

flowAccessAddress := "access.mainnet.nodes.onflow.org:9000"

_10

flowClient, _ := client.New(flowAccessAddress, grpc.WithInsecure())

_10

// ...

_10

}`

## Account Creation[​](#account-creation "Direct link to Account Creation")

You can follow the [Flow Port account creation steps](/protocol/flow-port) to create a new mainnet account.

If you prefer watching a video, check out this tutorial:

## Generating a Non-Custodial Account[​](#generating-a-non-custodial-account "Direct link to Generating a Non-Custodial Account")

A non-custodial account will make sure you are the only one holding the keys to your account.

You can follow the following steps to add a non-custodial account:

First, generate a new key pair with the [Flow CLI](https://github.com/onflow/flow-cli):

`_10

> flow keys generate --network=mainnet

_10

_10

🔴️ Store private key safely and don't share with anyone!

_10

Private Key 5b438...

_10

Public Key 1bdc5...`

> **Note**: By default, this command generates an ECDSA key pair on the P-256 curve. Keep in mind the CLI is intended for development purposes only and is not recommended for production use. Handling keys using a Key Management Service is the best practice.

Take a note of the public key and go back to Flow Port. Open the ["Create a new account" page](https://port.flow.com/transaction?hash=a0a78aa7821144efd5ebb974bb52ba04609ce76c3863af9d45348db93937cf98&showcode=false&weight=1000&halg=3).

On the page, enter your public key from the CLI, ensure the hash algorithm is set to `SHA3_256` and the weight is set to `1000`. Finally, check the box confirming correctness and hit 'Submit'.

> **Important**: Your account needs to have at least 0.002 FLOW for the account creation. More details can be found [in this guide](/build/cadence/basics/fees#storage).

Once the transaction is sealed, you should scroll down to the events section and locate the `flow.AccountCreated` event with the newly generated address.

![flow-port-sealed](/assets/images/port-sealed-tx-d6bd12b3044b726057506ae440ae6967.png)

Make sure to take a note of the address. If you want to verify the public key for this address, you can visit [flow-view-source](https://flow-view-source.com/).

## Important Mainnet Smart Contract Addresses[​](#important-mainnet-smart-contract-addresses "Direct link to Important Mainnet Smart Contract Addresses")

You can review [all available core contracts](/build/cadence/core-contracts) deployed to the mainnet to identify which ones you want to import.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/flow-networks/accessing-mainnet.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Flow Networks](/protocol/flow-networks)[Next

Testnet](/protocol/flow-networks/accessing-testnet)

###### Rate this page

😞😐😊

Copy as Markdown

* [Accessing Flow Mainnet](#accessing-flow-mainnet)* [Account Creation](#account-creation)* [Generating a Non-Custodial Account](#generating-a-non-custodial-account)* [Important Mainnet Smart Contract Addresses](#important-mainnet-smart-contract-addresses)

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