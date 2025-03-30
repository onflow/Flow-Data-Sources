# Source: https://developers.flow.com/networks/node-ops/node-operation/node-economics

Node Economics | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)

  + [Access Nodes](/networks/node-ops/access-nodes/access-node-setup)
  + [EVM Gateway Setup](/networks/node-ops/evm-gateway/evm-gateway-setup)
  + [Light Nodes](/networks/node-ops/light-nodes/observer-node)
  + [Participating in the Network](/networks/node-ops/node-operation/faq)

    - [Operator FAQ](/networks/node-ops/node-operation/faq)
    - [Byzantine Attack Response](/networks/node-ops/node-operation/byzantine-node-attack-response)
    - [Database Encryption for Existing Node Operators](/networks/node-ops/node-operation/db-encryption-existing-operator)
    - [Node Operations Guide](/networks/node-ops/node-operation/guides/genesis-bootstrap)
    - [Machine Accounts for Existing Node Operators](/networks/node-ops/node-operation/machine-existing-operator)
    - [Node Monitoring](/networks/node-ops/node-operation/monitoring-nodes)
    - [Node Bootstrapping](/networks/node-ops/node-operation/node-bootstrap)
    - [Node Economics](/networks/node-ops/node-operation/node-economics)
    - [Node Migration](/networks/node-ops/node-operation/node-migration)
    - [Node Provisioning](/networks/node-ops/node-operation/node-provisioning)
    - [Node Roles](/networks/node-ops/node-operation/node-roles)
    - [Node Setup](/networks/node-ops/node-operation/node-setup)
    - [Past Spork Info](/networks/node-ops/node-operation/past-sporks)
    - [Network Upgrade (Spork) Process](/networks/node-ops/node-operation/spork)
    - [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
    - [Slashing Conditions](/networks/node-ops/node-operation/slashing)
    - [Node Providers](/networks/node-ops/node-operation/node-providers)
    - [Height coordinated upgrade](/networks/node-ops/node-operation/hcu)
    - [Protocol State Bootstrapping](/networks/node-ops/node-operation/protocol-state-bootstrap)
    - [Managing disk space](/networks/node-ops/node-operation/reclaim-disk)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Node Ops](/networks/node-ops)
* Participating in the Network
* Node Economics

On this page

# Node Economics

Node operators play a crucial role in securing the Flow network. Here’s a simple example to illustrate what node operators can expect in terms of node economics.

## Node Operator Economics: An illustration[​](#node-operator-economics-an-illustration "Direct link to Node Operator Economics: An illustration")

warning

This illustration is strictly to serve as an example. Actual numbers will vary based on several factors.

For real-time numbers, please refer to the [block explorer](https://www.flowscan.io/tokenomics).

| # | Parameter | Value | Explanation |
| --- | --- | --- | --- |
| A | Node Operator’s Stake | 500,000 FLOW | Assuming minimum staking requirements for a consensus node. Remember there’s no upper cap on how much FLOW can be staked to a Flow node. |
| B | Delegation to node | 1,000,000 FLOW | Funds that individual/ institutional delegators delegate to your node. Assuming 1M FLOW for this example. |
| C | APY | 10% | Subject to change based on total ecosystem stake in each epoch. Remember APY = R / S, where S = Total FLOW Staked / Total FLOW Supply and R = 5% (”reward rate”) |
| D | Delegation Rate | 8% | Fee taken by the node operator from delegator rewards to cover their operating expenses, currently set at 8% of the rewards received by delegators. Note that the 8% fee is only applied to the staking reward, not to the tokens delegated. |
| E | Annual Staking Rewards | 50,000 FLOW | Product of A x C; the number shown is annualized but is paid each epoch (week). |
| F | Annual Delegator Fee | 8,000 FLOW | Product of B x C x D; ; the number shown is annualized but is paid each epoch (week). |
| G | Annual (Gross) Rewards | 58,000 FLOW | Sum of E and F |
| H | COGS | 4,190 FLOW | Assumed costs of running a consensus node in FLOW assuming 1US$/FLOW. The actual cost will vary depending on several factors such as self-hosted vs cloud, bare metal vs VM, the type of node, the FLOW exchange rate. |
| J | Net Annual Rewards | 53,810 FLOW | G less H |

## Note[​](#note "Direct link to Note")

1. Each year, 5% of the total Flow supply is distributed as rewards to incentivize validators and delegators. While the total rewards for each epoch are fixed, the rewards for individual stakers vary depending on the amount they stake and the total funds delegated to their node.
2. All Flow node types follow the same economic principles, with the only difference being their minimum staking requirements. For details on the minimum stakes needed for each node type, see [here](https://flow.com/flow-tokenomics/technical-overview).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-economics.md)

Last updated on **Mar 14, 2025** by **j pimmel**

[Previous

Node Bootstrapping](/networks/node-ops/node-operation/node-bootstrap)[Next

Node Migration](/networks/node-ops/node-operation/node-migration)

###### Rate this page

😞😐😊

* [Node Operator Economics: An illustration](#node-operator-economics-an-illustration)
* [Note](#note)

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