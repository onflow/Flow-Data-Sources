# Source: https://developers.flow.com/networks/node-ops/node-operation/monitoring-nodes




Monitoring Node Health | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

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
* Node Monitoring
On this page
# Monitoring Node Health

A Flow node generates logs and publishes metrics as it runs. These logs and metrics can be used to gain insights into the health of the node.

## Logs[​](#logs "Direct link to Logs")

Logs are emitted to `stdout` as JSON formed strings. Where these logs are available on your system depends on how you launch your containers. On `systemd` systems for example, the logs will be sent to the system journal daemon `journald`. Other systems may log to `/var/log`.

## Metrics[​](#metrics "Direct link to Metrics")

Flow nodes produce health metrics in the form of [Prometheus](https://prometheus.io) metrics, exposed from the node software on `/metrics`.

If you wish to make use of these metrics, you'll need to set up a Prometheus server to scrape your Nodes. Alternatively, you can deploy the Prometheus Server on top of your current Flow node to see the metrics without creating an additional server.

> The flow-go application doesn't expose any metrics from the underlying host such as CPU, network, or disk usages. It is recommended you collect these metrics in addition to the ones provided by flow using a tool like node exporter (<https://github.com/prometheus/node_exporter>)

1. Copy the following Prometheus configuration into your current flow node
   
    `_12 global:_12 scrape_interval: 15s # By default, scrape targets every 15 seconds._12_12 scrape_configs:_12 # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config._12 - job_name: 'prometheus'_12_12 # Override the global default and scrape targets from this job every 5 seconds._12 scrape_interval: 5s_12_12 static_configs:_12 - targets: ['localhost:8080']`
2. Start Prometheus server
   
    `_10 docker run \_10 --network=host \_10 -p 9090:9090 \_10 -v /path/to/prometheus.yml:/etc/prometheus/prometheus.yml \_10 prom/prometheus"`
3. (optional) Port forward to the node if you are not able to access port 9090 directly via the browser
   `ssh -L 9090:127.0.0.1:9090 YOUR_NODE`
4. Open your browser and go to the URL `http://localhost:9090/graph` to load the Prometheus Dashboard

### Key Metric Overview[​](#key-metric-overview "Direct link to Key Metric Overview")

The following are some important metrics produced by the node.

| Metric Name | Description |
| --- | --- |
| go\_\* | Go runtime metrics |
| consensus\_compliance\_finalized\_height | Latest height finalized by this node; should increase at a constant rate. |
| consensus\_compliance\_sealed\_height | Latest height sealed by this node; should increase at a constant rate. |
| consensus\_hotstuff\_cur\_view | Current view of the HotStuff consensus algorith; Consensus/Collection only; should increase at a constant rate. |
| consensus\_hotstuff\_timeout\_seconds | How long it takes to timeout failed rounds; Consensus/Collection only; values consistently larger than 5s are abnormal. |

### Machine Account[​](#machine-account "Direct link to Machine Account")

Collection and consensus nodes use a machine account that must be kept funded. See [here](/networks/staking/machine-account) for details.

Nodes check their machine account's configuration and funding and produce metrics.

| Metric Name | Description |
| --- | --- |
| machine\_account\_balance | The current balance (FLOW) |
| machine\_account\_recommended\_min\_balance | The recommended minimum balance (FLOW) |
| machine\_account\_is\_misconfigured | 0 if the node is configured correctly; 1 if the node is misconfigured |

To be notified when your node's machine account needs to be refilled or has a configuration error, you can set up alerts.

When the machine account balance needs to be refilled:

 `_10machine_account_balance < machine_account_recommended_min_balance`

When the machine account has a configuration error:

 `_10machine_account_is_misconfigured > 0`

The metrics include the account address of the machine account (`acct_address` label) for convenience:

 `_10# HELP machine_account_balance the last observed balance of this node's machine account, in units of FLOW_10# TYPE machine_account_balance gauge_10machine_account_balance{acct_address="7b16b57ae0a3c6aa"} 9.99464935`[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/node-operation/monitoring-nodes.md)Last updated on **Jan 7, 2025** by **Chase Fleming**[PreviousMachine Accounts for Existing Node Operators](/networks/node-ops/node-operation/machine-existing-operator)[NextNode Bootstrapping](/networks/node-ops/node-operation/node-bootstrap)
###### Rate this page

😞😐😊

* [Logs](#logs)
* [Metrics](#metrics)
  + [Key Metric Overview](#key-metric-overview)
  + [Machine Account](#machine-account)
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

