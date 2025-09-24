# Source: https://developers.flow.com/protocol/flow-networks

Flow Networks | Flow Developer Portal



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

* Flow Networks

On this page

# Flow Networks

## About Flow Networks[​](#about-flow-networks "Direct link to About Flow Networks")

note

This page provides information on Flow network RPCs. Flow EVM network RPCs can be found [here](/build/evm/networks)

In addition to Mainnet, developers have access to the Testnet environment, which serves as an essential testing ground for applications and smart contracts prior to their deployment on Mainnet. This ensures that any potential issues can be identified and resolved in a controlled setting, mitigating risks associated with live deployment.

Furthermore, during network upgrades, Testnet receives updates ahead of Mainnet. This preemptive update process allows developers to comprehensively test their apps against the latest versions of the nodes, enhancements to the Cadence programming language, and core contract upgrades. This strategy guarantees that when these updates are eventually applied to Mainnet, applications and smart contracts will operate seamlessly, enhancing overall network stability and user experience.

### How To Access These Networks?[​](#how-to-access-these-networks "Direct link to How To Access These Networks?")

| Network | GRPC | Web GRPC | REST |
| --- | --- | --- | --- |
| Mainnet | `access.mainnet.nodes.onflow.org:9000` | `mainnet.onflow.org` | `rest-mainnet.onflow.org` |
| Testnet | `access.devnet.nodes.onflow.org:9000` | `testnet.onflow.org` | `rest-testnet.onflow.org` |

For more information on how to access these networks, refer to the following guides:

* [Flow Testnet](/protocol/flow-networks/accessing-testnet)
* [Flow Mainnet](/protocol/flow-networks/accessing-mainnet)

### Network[​](#network "Direct link to Network")

There are two primary ways to access onchain data within the Flow network; Access Nodes and Light nodes. Access Nodes are the node type that are most useful for developers, as they provide access to the Flow network via the following API endpoints:

* [Flow Access API](/protocol/access-onchain-data)
  + [Mainnet](/protocol/flow-networks/accessing-mainnet): `access.mainnet.nodes.onflow.org:9000`
  + [Testnet](/protocol/flow-networks/accessing-testnet): `access.devnet.nodes.onflow.org:9000`
* [Status Page](https://status.onflow.org/) - Network status page

### Rate limits[​](#rate-limits "Direct link to Rate limits")

Rate limits for Flow Public Access nodes hosted by QuickNode are detailed [here](https://www.quicknode.com/docs/flow#endpoint-rate-limits).

### Running Your Own Node[​](#running-your-own-node "Direct link to Running Your Own Node")

If you’re getting started you don’t need to run your own node and you can use the above public nodes. The public access nodes are rate-limited, so as your product matures you might want to run your own node. There are multiple options available:

* Start with a [Light (Observer) Node](/protocol/node-ops/light-nodes/observer-node).
* You can also use a third-party provider like [Quicknode](https://www.quicknode.com/docs/flow).

Check out [Running a Node](/protocol/node-ops/light-nodes/observer-node) for more information.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/flow-networks/index.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Next

Mainnet](/protocol/flow-networks/accessing-mainnet)

###### Rate this page

😞😐😊

Copy as Markdown

* [About Flow Networks](#about-flow-networks)
  + [How To Access These Networks?](#how-to-access-these-networks)
  + [Network](#network)
  + [Rate limits](#rate-limits)
  + [Running Your Own Node](#running-your-own-node)

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