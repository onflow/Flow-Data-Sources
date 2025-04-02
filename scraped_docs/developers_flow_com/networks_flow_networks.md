# Source: https://developers.flow.com/networks/flow-networks

Flow Networks | Flow Developer Portal



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

* Flow Networks

On this page

# Flow Networks

## About Flow Networks[​](#about-flow-networks "Direct link to About Flow Networks")

note

This page provides information on Flow network RPCs. Flow EVM network RPCs can be found [here](/evm/networks)

In addition to Mainnet, developers have access to the Testnet environment, which serves as an essential testing ground for applications and smart contracts prior to their deployment on Mainnet. This ensures that any potential issues can be identified and resolved in a controlled setting, mitigating risks associated with live deployment.

Furthermore, during network upgrades, Testnet receives updates ahead of Mainnet. This preemptive update process allows developers to comprehensively test their apps against the latest versions of the nodes, enhancements to the Cadence programming language, and core contract upgrades. This strategy guarantees that when these updates are eventually applied to Mainnet, applications and smart contracts will operate seamlessly, enhancing overall network stability and user experience.

### How To Access These Networks?[​](#how-to-access-these-networks "Direct link to How To Access These Networks?")

| Network | GRPC | Web GRPC | REST |
| --- | --- | --- | --- |
| Mainnet | `access.mainnet.nodes.onflow.org:9000` | `mainnet.onflow.org` | `rest-mainnet.onflow.org` |
| Testnet | `access.devnet.nodes.onflow.org:9000` | `testnet.onflow.org` | `rest-testnet.onflow.org` |

For more information on how to access these networks, refer to the following guides:

* [Flow Testnet](/networks/flow-networks/accessing-testnet)
* [Flow Mainnet](/networks/flow-networks/accessing-mainnet)

### Network[​](#network "Direct link to Network")

There are two primary ways to access on-chain data within the Flow network; Access Nodes and Light nodes. Access Nodes are the node type that are most useful for developers, as they provide access to the Flow network via the following API endpoints:

* [Flow Access API](/networks/access-onchain-data)
  + [Mainnet](/networks/flow-networks/accessing-mainnet): `access.mainnet.nodes.onflow.org:9000`
  + [Testnet](/networks/flow-networks/accessing-testnet): `access.devnet.nodes.onflow.org:9000`
* [Status Page](https://status.onflow.org/) - Network status page

### Rate limits[​](#rate-limits "Direct link to Rate limits")

Rate limits for Flow Public Access nodes hosted by QuickNode are detailed [here](https://www.quicknode.com/docs/flow#endpoint-rate-limits).

### Running Your Own Node[​](#running-your-own-node "Direct link to Running Your Own Node")

If you’re getting started you don’t need to run your own node and you can use the above public nodes. The public access nodes are rate-limited, so as your product matures you might want to run your own node. There are multiple options available:

* Start with a [Light (Observer) Node](/networks/node-ops/light-nodes/observer-node).
* You can also use a third-party provider like [Quicknode](https://www.quicknode.com/docs/flow).

Check out [Running a Node](/networks/node-ops/light-nodes/observer-node) for more information.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/flow-networks/index.md)

Last updated on **Mar 27, 2025** by **Brian Doyle**

[Next

Mainnet](/networks/flow-networks/accessing-mainnet)

###### Rate this page

😞😐😊

* [About Flow Networks](#about-flow-networks)
  + [How To Access These Networks?](#how-to-access-these-networks)
  + [Network](#network)
  + [Rate limits](#rate-limits)
  + [Running Your Own Node](#running-your-own-node)

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