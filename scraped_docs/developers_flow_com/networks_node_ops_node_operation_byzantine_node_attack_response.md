# Source: https://developers.flow.com/networks/node-ops/node-operation/byzantine-node-attack-response

Byzantine Node Attack Response | Flow Developer Portal



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
* Byzantine Attack Response

On this page

# Byzantine Node Attack Response

Flow, like most blockchains, forms an open decentralized peer-to-peer network between all of the nodes
on the network. Due to its decentralized nature, there is a potential for nodes to behave maliciously
(byzantine) and intentionally try to harm the network. There are a variety of protections within the
node software to deal with invalid messages - message signatures, sender authorization, payload
validation, etc. These protections guard the network against many types of attacks. However, there
could still be a byzantine node that spams other nodes in the network with invalid messages at volumes
that are intended to impact node performance. While this will not compromise the security of the
network it could impact network liveness.

This guide explains how to detect such a node and what actions you should take as a node operator
to deal with such byzantine nodes.

Responding to an attack from a byzantine node requires the following:

1. Immediate action to block network traffic originating from the byzantine node to your node.
2. Raising a governance FLIP to remove the node from the network as described in this [FLIP](https://github.com/onflow/flips/blob/main/governance/20230105-identify-errant-node.md).
3. A service account transaction to set the node weight to 0.

This guide focuses on the first action.

## Admin Server[​](#admin-server "Direct link to Admin Server")

Flow nodes have an admin server which exposes a simple REST API for interacting with the node.
See the [README](https://github.com/onflow/flow-go/blob/master/admin/README.md) for some useful examples.
It is disabled by default.

### Enable the Admin Server[​](#enable-the-admin-server "Direct link to Enable the Admin Server")

To enable to admin server,

1. Add the following option to the node's CLI flags.

`_10

--admin-addr=localhost:9002`

> Note: The port does not have to be 9002. You can choose any free port.

> ⚠️ Do NOT expose the port outside the machine and always use **localhost**:port

2. Reboot the node to apply the new setting. You can then verify it’s working by logging into
   the machine via ssh and running,

`_10

curl localhost:9002`

This should return a json response message as below.

`_10

{"code":5,"message":"Not Found","details":[]}`

If you instead get a connection rejected message then it’s not configured correctly.

## Detecting a Byzantine Node[​](#detecting-a-byzantine-node "Direct link to Detecting a Byzantine Node")

There are 2 general categories of byzantine attacks:

1. Safety attacks - are attacks where a node attempts to corrupt or modify the state of the
   blockchain outside of normal protocol rules.
2. Liveness attacks - sometimes called spamming attacks, are when a node attempts to disrupt the
   network by abusing their access to waste network and node resources. This generally results in
   degraded performance.

Flow nodes are protected against safety attacks, but liveness attacks are extremely difficult to
completely prevent. To close the gap, we rely on coordination between node operators to detect
and block abusive nodes.

### Metrics[​](#metrics "Direct link to Metrics")

Flow nodes generate a variety of metrics that can be used to measure the node's performance and
identify abnormal behavior. Most metrics are only useful in the context of "normal" operation,
so it is a good idea to regularly review them to build an understanding of what is "normal".

Metrics to watch:

* CPU, memory, network connections, network I/O, file descriptors
* `network_authorization_*` - counts the number of unauthorized/invalid messages received
* `network_queue_message_queue_size` - measures the number of incoming messages waiting to be processed
* `network_engine_messages_received_total` - measures the number of messages received from the network

There are many other metrics, but these are a good starting point. If you notice any anomalous trends,
review the logs for additional context.

### Logs[​](#logs "Direct link to Logs")

Log events related to suspicious activity are logged with the label `"suspicious":true`. This is
helpful to identify the most relevant logs, but there are legitimate cases when these logs are
emitted, so they cannot be used as a definitive indicator of malicious activity. Two examples of
expected log messages are:

* `rejected inbound connection` - You may see this error if an operator unstaked their node between
  sporks, but never shut it down. The node will continue to operate as usual, but peers will not have
  it in their identity table and will (correctly) reject incoming connections.
* `middleware does not have subscription for the channel ID indicated in the unicast message received` -
  This is commonly logged during node startup when receiving messages before all of the components
  have finished registering their channels with the network layer. It is NOT expected after startup.

The following is an example of a log message indicating an Access node attempted to send a message it
is not authorized to send:

`_16

{

_16

"level": "error",

_16

"node_role": "collection",

_16

"node_id": "4a6f7264616e20536368616c6d00a875801849f2b5bea9e9d2c9603f00e5d533",

_16

"module": "network_slashing_consumer",

_16

"peer_id": "QmY2kby3xt3ugu2QqJP5w24rP4HSakYgDFpAJy1ifSRkF7",

_16

"networking_offense": "unauthorized_sender",

_16

"message_type": "messages.BlockProposal",

_16

"channel": "sync-committee",

_16

"protocol": "publish",

_16

"suspicious": true,

_16

"role": "access",

_16

"sender_id": "f9237c896507b8d654165c36b61c9a3080e6dd042dea562a4a494fbd73133634",

_16

"time": "2023-01-24T21:10:32.74684667Z",

_16

"message": "potential slashable offense: sender role not authorized to send message on channel"

_16

}`

### Identifying the Source of Malicious Traffic[​](#identifying-the-source-of-malicious-traffic "Direct link to Identifying the Source of Malicious Traffic")

Most log messages include either the node ID or peer ID. Peer ID is the ID used to identify nodes on
by the libp2p library. Peer IDs are derived from the node's networking public key, so there is a 1:1
mapping between node ID and peer ID.

The two simplest ways to match a node ID to a peer ID:

1. `inbound connection established` and `outbound connection established` log messages contain both
   the node and peer IDs
2. The following admin command will return the node info for a given peer ID:

`_10

curl localhost:9002/admin/run_command \

_10

-H 'Content-Type: application/json' \

_10

-d '{"commandName": "get-latest-identity", "data": { "peer_id": "QmY2kby3xt3ugu2QqJP5w24rP4HSakYgDFpAJy1ifSRkF7" }}'`

If you cannot find any log messages at the current log level, you may need to enable debug logging.
See the admin server's [README](https://github.com/onflow/flow-go/blob/master/admin/README.md) for
an example.

## Reporting the Byzantine Node[​](#reporting-the-byzantine-node "Direct link to Reporting the Byzantine Node")

Report the suspicious node on Discord in the `#flow-validators-alerts` channel along with all the
evidence you have collected (log messages, other networking related metrics, etc).
This will alert other node operators who can review their nodes to corroborate the report. Using
evidence from multiple operators, a consensus can be reached about the suspicious node, and
appropriate action can be taken.

## Blocking a Byzantine Node[​](#blocking-a-byzantine-node "Direct link to Blocking a Byzantine Node")

Once a consensus is reached about the suspicious node on Discord among the node operators, the
suspicious node can be blocked using the admin command.

`_10

curl localhost: 9002/admin/run_command \

_10

-H 'Content-Type: application/json' \

_10

-d '{"commandName": "set-config","data": {"network-id-provider-blocklist": ["<suspcious node id>"]}}`

After blocking the node, all traffic coming from the node will be rejected and you should only see
logs about reject messages and connections for that node ID.

## Unblocking a Node[​](#unblocking-a-node "Direct link to Unblocking a Node")

If you need to unblock a node, you can use the same command to remove the node ID from the blocklist.
Simply run it again with an empty list to remove all blocked nodes, or an existing list with the
specific node ID you want to unblock removed.

The following command returns a list of the currently blocked nodes.

`_10

curl localhost: 9002/admin/run_command \

_10

-H 'Content-Type: application/json' \

_10

-d '{"commandName": "get-config", "data": "network-id-provider-blocklist"}`

After unblocking the node, connections and traffic coming from the node should resume.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/byzantine-node-attack-response.md)

Last updated on **Mar 28, 2025** by **Jordan Ribbink**

[Previous

Operator FAQ](/networks/node-ops/node-operation/faq)[Next

Database Encryption for Existing Node Operators](/networks/node-ops/node-operation/db-encryption-existing-operator)

###### Rate this page

😞😐😊

* [Admin Server](#admin-server)
  + [Enable the Admin Server](#enable-the-admin-server)
* [Detecting a Byzantine Node](#detecting-a-byzantine-node)
  + [Metrics](#metrics)
  + [Logs](#logs)
  + [Identifying the Source of Malicious Traffic](#identifying-the-source-of-malicious-traffic)
* [Reporting the Byzantine Node](#reporting-the-byzantine-node)
* [Blocking a Byzantine Node](#blocking-a-byzantine-node)
* [Unblocking a Node](#unblocking-a-node)

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