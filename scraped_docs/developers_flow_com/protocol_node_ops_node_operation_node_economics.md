# Source: https://developers.flow.com/protocol/node-ops/node-operation/node-economics

Node Economics | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          + [Access Nodes](/protocol/node-ops/access-nodes/access-node-setup)

            + [EVM Gateway Setup](/protocol/node-ops/evm-gateway/evm-gateway-setup)

              + [Light Nodes](/protocol/node-ops/light-nodes/observer-node)

                + [Participating in the Network](/protocol/node-ops/node-operation/faq)

                  - [Operator FAQ](/protocol/node-ops/node-operation/faq)- [Byzantine Attack Response](/protocol/node-ops/node-operation/byzantine-node-attack-response)- [Database Encryption for Existing Node Operators](/protocol/node-ops/node-operation/db-encryption-existing-operator)- [Node Operations Guide](/protocol/node-ops/node-operation/guides/genesis-bootstrap)

                          - [Machine Accounts for Existing Node Operators](/protocol/node-ops/node-operation/machine-existing-operator)- [Node Monitoring](/protocol/node-ops/node-operation/monitoring-nodes)- [Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)- [Node Economics](/protocol/node-ops/node-operation/node-economics)- [Node Migration](/protocol/node-ops/node-operation/node-migration)- [Node Provisioning](/protocol/node-ops/node-operation/node-provisioning)- [Node Roles](/protocol/node-ops/node-operation/node-roles)- [Node Setup](/protocol/node-ops/node-operation/node-setup)- [Past Network Upgrades](/protocol/node-ops/node-operation/past-upgrades)- [Network Upgrade (Spork) Process](/protocol/node-ops/node-operation/network-upgrade)- [Slashing Conditions](/protocol/node-ops/node-operation/slashing)- [Node Providers](/protocol/node-ops/node-operation/node-providers)- [Height coordinated upgrade](/protocol/node-ops/node-operation/hcu)- [Protocol State Bootstrapping](/protocol/node-ops/node-operation/protocol-state-bootstrap)- [Managing disk space](/protocol/node-ops/node-operation/reclaim-disk)* [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Node Ops](/protocol/node-ops)* Participating in the Network* Node Economics

On this page

# Node Economics

Node operators play a crucial role in securing the Flow network. Here’s a simple example to illustrate what node operators can expect in terms of node economics.

## Node Operator Economics: An illustration[​](#node-operator-economics-an-illustration "Direct link to Node Operator Economics: An illustration")

warning

This illustration is strictly to serve as an example. Actual numbers will vary based on several factors.

For real-time numbers, please refer to the [block explorer](https://www.flowscan.io/tokenomics).

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| # Parameter Value Explanation|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | A Node Operator’s Stake 500,000 FLOW Assuming minimum staking requirements for a consensus node. Remember there’s no upper cap on how much FLOW can be staked to a Flow node.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | B Delegation to node 1,000,000 FLOW Funds that individual/ institutional delegators delegate to your node. Assuming 1M FLOW for this example.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | C APY 10% Subject to change based on total ecosystem stake in each epoch. Remember APY = R / S, where S = Total FLOW Staked / Total FLOW Supply and R = 5% (”reward rate”)|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | D Delegation Rate 8% Fee taken by the node operator from delegator rewards to cover their operating expenses, currently set at 8% of the rewards received by delegators. Note that the 8% fee is only applied to the staking reward, not to the tokens delegated.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | E Annual Staking Rewards 50,000 FLOW Product of A x C; the number shown is annualized but is paid each epoch (week).|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | F Annual Delegator Fee 8,000 FLOW Product of B x C x D; ; the number shown is annualized but is paid each epoch (week).|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | G Annual (Gross) Rewards 58,000 FLOW Sum of E and F|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | H COGS 4,190 FLOW Assumed costs of running a consensus node in FLOW assuming 1US$/FLOW. The actual cost will vary depending on several factors such as self-hosted vs cloud, bare metal vs VM, the type of node, the FLOW exchange rate.|  |  |  |  | | --- | --- | --- | --- | | J Net Annual Rewards 53,810 FLOW G less H | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Note[​](#note "Direct link to Note")

1. Each year, 5% of the total Flow supply is distributed as rewards to incentivize validators and delegators. While the total rewards for each epoch are fixed, the rewards for individual stakers vary depending on the amount they stake and the total funds delegated to their node.
2. All Flow node types follow the same economic principles, with the only difference being their minimum staking requirements. For details on the minimum stakes needed for each node type, see [here](https://flow.com/flow-tokenomics/technical-overview).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/node-economics.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Node Bootstrapping](/protocol/node-ops/node-operation/node-bootstrap)[Next

Node Migration](/protocol/node-ops/node-operation/node-migration)

###### Rate this page

😞😐😊

Copy as Markdown

* [Node Operator Economics: An illustration](#node-operator-economics-an-illustration)* [Note](#note)

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