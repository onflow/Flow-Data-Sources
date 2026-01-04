# Source: https://developers.flow.com/protocol/node-ops/node-operation/node-provisioning

Provisioning a Flow node | Flow Developer Portal



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

* * [Node Ops](/protocol/node-ops)* Participating in the Network* Node Provisioning

On this page

# Provisioning a Flow node

## Hardware Requirements[​](#hardware-requirements "Direct link to Hardware Requirements")

The hardware your Node will need varies depending on the role your Node will play in the Flow network. For an overview of the differences see the [Node Roles Overview](/protocol/node-ops/node-operation/node-roles).

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Node Type CPU Memory Disk Example GCP Instance Example AWS Instance|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Collection** 2 cores 🆕 (was 4 cores) 8 GB 🆕 (was 32 GB) 200 GB n2-standard-2 m5.large|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Consensus** 2 cores 8 GB 🆕 (was 16 GB) 200 GB n2-standard-2 m5.large|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Execution** 128 cores 864 GB 9 TB1 n2-highmem-128 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Verification** 2 cores 8 GB 🆕 (was 16 GB) 200 GB n2-standard-2 m5.large|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Access** 8 cores 🆕 (was 16 cores) 32 GB 🆕 (was 64 GB) 750 GB n2-standard-8 m5.2xlarge|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Observer** 2 cores 4 GB 300 GB n2-standard-4 m6i.xlarge|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | **EVM Gateway** 2 cores 32 GB 30 GB n2-highmem-4 r6i.xlarge | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

1: Recommended with maintenance see: [pruning chunk data pack](https://forum.flow.com/t/execution-node-upgrade-to-v0-31-15-and-managing-disk-space-usage/5167), 30 TB without maintenance.

*Note: The above numbers represent our current best estimate for the state of the network. These will be actively updated as we continue benchmarking the network's performance.*

*Note: If you are running your node on bare metal, we recommend provisioning a machine with higher CPU and memory than the minimum requirements. Unlike cloud instances, bare metal servers cannot be easily scaled up, and over-provisioning upfront helps avoid the need for disruptive hardware upgrades later.*

## Networking Requirements[​](#networking-requirements "Direct link to Networking Requirements")

Most of the load on your nodes will be messages sent back and forth between other nodes on the network. Make sure you have a sufficiently fast connection; we recommend at *least* 1Gbps, and 5Gbps is better.

Each node will require a fixed DNS name and we will refer to this more generally as your 'Node Address' from here on out.

Node Address Requirements

Your Node Address must be a publicly routable valid DNS name
that points to your node. This is how other nodes in the network will
communicate with you.

Your firewalls must expose **TCP/3569** for both, ingress and egress.

If you are running an Access Node, you must also expose the GRPC port **9000** to your internal network traffic. Port 9000 is not required for external ingress/egress.

![Flow Architecture](/assets/images/flow-architecture-19e1adb0cc7199ea3d19c468c3b5d8b6.png)

## Operating System Requirements[​](#operating-system-requirements "Direct link to Operating System Requirements")

The Flow node code is distributed as a Linux container image, so your node must be running an OS with a container runtime like [docker](https://docker.com) or [containerd](https://containerd.io).

The bootstrapping scripts we'll use later are compiled binaries targeting an `amd64` architecture, so your system must be 64-bit. Some of these scripts are bash based hence a shell interpreter that is bash compatible will also be needed.

Flow also provides `systemd` service and unit files as a template for installation, though `systemd` is not required to run Flow.

Choose Your Own Adventure

Flow is distributed in such a way that makes it very system agnostic. You are
free to build your own orchestration around how you run your nodes and manage
your keys.

For the remainder of this guide, we cover the most simple case, a single node being
hand deployed. This should give you a good sense of what's needed, and you can
modify to suit your needs from there.

The Flow team has tested running nodes on Ubuntu 18.04 and GCP's Container
Optimized OS, which is based on Chromium OS. If you are unsure where to start,
those are good choices.

## Time synchronization[​](#time-synchronization "Direct link to Time synchronization")

You should also ensure you run **time synchronization** on the machine hosting the container, to avoid clock drift. In practice, this means configuring a client for the NTP protocol, and making sure it runs as a daemon. `ntpd` is one recommended example. To configure it, you just have to point it to an NTP server to query periodically. A default from your Linux distribution or cloud operator may already be set, and in the interest of decentralization, our recommendation would be to use it unless you have a specific reason to do otherwise.

Time synchronization FAQ

* **Leap-smearing**: Leap-smearing time servers and non-leap-smearing time servers are both acceptable for the magnitude of our time precision requirements - though considering very few providers offer leap smearing time servers, a "regular" time server helps ensure our pool of time providers is more diverse.
* **Why not do it in the container itself? Why do we need to do this?**: Without special privileges and in all major container runtimes, a container will not run with the `CAP_SYS_TIME` capability. For Flow, this means that the node software itself cannot change the time of the host machine, making the in-container use of standard time synchronization protocols ineffective.
* **Why does time matter in Flow?**: Time information comes up in consensus and in smart contracts. The consensus algorithm of Flow allows nodes to exit the influence of a corrupt or ineffective "leader" node by collectively deciding to switch to the next "phase" of the protocol at the right time. The smart contract language also allows developer access to block time stamps, which provide an approximation of time. To resist manipulation in each case, honest nodes must compute timing values from an aggregate of the information provided by all nodes. That approach, though resilient, is still sensitive to inaccurate time information. In other words, a node subject to clock drift but otherwise honest will not stop the consensus, but might make it slower.

## Setup Data Directories & Disks[​](#setup-data-directories--disks "Direct link to Setup Data Directories & Disks")

Flow stores protocol state on disk, as well as execution state in the case of execution nodes.

Where the data is stored is up to you. By default, the `systemd` files that ship with Flow use `/var/flow/data`.
This is where the vast majority of Flow's disk usage comes from, so you may wish to mount this directory on a separate disk from the OS.
The performance of this disk IO is also a major bottleneck for certain node types.
While all nodes need to make use of this disk, if you are running an execution node, you should make sure this is a high performing SSD.

As a rough benchmark for planning storage capacity, each Flow block will grow the data directory by 3-5KiB.

### Confidential Data & Files[​](#confidential-data--files "Direct link to Confidential Data & Files")

Flow stores dynamically generated confidential data in a separate database. We strongly recommend enabling encryption
for this database - see [this guide](/protocol/node-ops/node-operation/db-encryption-existing-operator) for instructions.

Confidential information used by Flow is stored in the `private-root-information` subtree of the `bootstrap` folder.
In particular:

* the staking private key (`node-info.priv.json`)
* the networking private key (`node-info.priv.json`)
* the encryption key for the secrets database (`secretsdb-key`)
* (if applicable) the initial random beacon private key (`random-beacon.priv.json`)

These files contain confidential data, and must be stored and accessed securely.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/node-ops/node-operation/node-provisioning.md)

Last updated on **Oct 16, 2025** by **Vishal**

[Previous

Node Migration](/protocol/node-ops/node-operation/node-migration)[Next

Node Roles](/protocol/node-ops/node-operation/node-roles)

###### Rate this page

😞😐😊

Copy as Markdown

* [Hardware Requirements](#hardware-requirements)* [Networking Requirements](#networking-requirements)* [Operating System Requirements](#operating-system-requirements)* [Time synchronization](#time-synchronization)* [Setup Data Directories & Disks](#setup-data-directories--disks)
          + [Confidential Data & Files](#confidential-data--files)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.