# Source: https://developers.flow.com/networks/node-ops/node-operation/node-provisioning

Provisioning a Flow node | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

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
* Node Provisioning

On this page

# Provisioning a Flow node

## Hardware Requirements[​](#hardware-requirements "Direct link to Hardware Requirements")

The hardware your Node will need varies depending on the role your Node will play in the Flow network. For an overview of the differences see the [Node Roles Overview](/networks/node-ops/node-operation/node-roles).

| Node Type | CPU | Memory | Disk | Example GCP Instance | Example AWS Instance |
| --- | --- | --- | --- | --- | --- |
| **Collection** | 4 cores | 32 GB | 200 GB | n2-highmem-4 | r6i.xlarge |
| **Consensus** | 2 cores | 16 GB | 200 GB | n2-standard-4 | m6a.xlarge |
| **Execution** | 128 cores | 864 GB | 9 TB (with maintenance see: [pruning chunk data pack](https://forum.flow.com/t/execution-node-upgrade-to-v0-31-15-and-managing-disk-space-usage/5167) or 30 TB without maintenance) | n2-highmem-128 |  |
| **Verification** | 2 cores | 16 GB | 200 GB | n2-highmem-2 | r6a.large |
| **Access** | 16 cores | 64 GB | 750 GB | n2-standard-16 | m6i.4xlarge |
| **Observer** | 2 cores | 4 GB | 300 GB | n2-standard-4 | m6i.xlarge |
| **EVM Gateway** | 2 cores | 32 GB | 30 GB | n2-highmem-4 | r6i.xlarge |

*Note: The above numbers represent our current best estimate for the state of the network. These will be actively updated as we continue benchmarking the network's performance.*

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
for this database - see [this guide](/networks/node-ops/node-operation/db-encryption-existing-operator) for instructions.

Confidential information used by Flow is stored in the `private-root-information` subtree of the `bootstrap` folder.
In particular:

* the staking private key (`node-info.priv.json`)
* the networking private key (`node-info.priv.json`)
* the encryption key for the secrets database (`secretsdb-key`)
* (if applicable) the initial random beacon private key (`random-beacon.priv.json`)

These files contain confidential data, and must be stored and accessed securely.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/node-provisioning.md)

Last updated on **Feb 25, 2025** by **Chase Fleming**

[Previous

Node Migration](/networks/node-ops/node-operation/node-migration)[Next

Node Roles](/networks/node-ops/node-operation/node-roles)

###### Rate this page

😞😐😊

* [Hardware Requirements](#hardware-requirements)
* [Networking Requirements](#networking-requirements)
* [Operating System Requirements](#operating-system-requirements)
* [Time synchronization](#time-synchronization)
* [Setup Data Directories & Disks](#setup-data-directories--disks)
  + [Confidential Data & Files](#confidential-data--files)

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