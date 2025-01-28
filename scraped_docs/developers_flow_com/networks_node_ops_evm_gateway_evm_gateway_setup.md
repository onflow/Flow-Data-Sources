# Source: https://developers.flow.com/networks/node-ops/evm-gateway/evm-gateway-setup




Setting up an EVM Gateway node | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
  + [Access Nodes](/networks/node-ops/access-nodes/access-node-setup)
  + [EVM Gateway Setup](/networks/node-ops/evm-gateway/evm-gateway-setup)
    - [EVM Gateway Setup](/networks/node-ops/evm-gateway/evm-gateway-setup)
  + [Light Nodes](/networks/node-ops/light-nodes/observer-node)
  + [Participating in the Network](/networks/node-ops/node-operation/faq)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)


* [Node Ops](/networks/node-ops)
* EVM Gateway Setup
* EVM Gateway Setup
On this page
# Setting up an EVM Gateway node


This guide is for running the [EVM Gateway](https://github.com/onflow/flow-evm-gateway) node on Flow. The EVM Gateway implements the
[Ethereum JSON-RPC specification](https://ethereum.org/en/developers/docs/apis/json-rpc/) and is the only node type which accepts EVM
client connections.

The EVM Gateway consumes Flow protocol state from the configured Flow Access Node and persists the indexed EVM state locally to
service EVM client requests. It submits EVM transactions it receives into the Flow network, wrapped in a Cadence transaction, and
mutating EVM state when executed. Non-mutating RPC methods only query the local state index of the gateway and are never forwarded
to Access Nodes. It does not participate in the block production process and requires no stake.

## Anyone can run EVM Gateway[​](#anyone-can-run-evm-gateway "Direct link to Anyone can run EVM Gateway")

The EVM Gateway can serve as a dedicated private RPC, a performance scaling solution, and a free gas provider offering similar capabilities
to centralized middleware providers like Infura, Alchemy, etc. at a fraction of the cost. EVM Gateway nodes connect directly to the Flow network
with no middleware giving you full control.

If you are just getting started building your application, you can use the [public EVM Gateway](https://developers.flow.com/evm/networks).
Applications generating high call volumes to the JSON-RPC may have hit rate limits on Flow public EVM Gateway and may benefit from running their
own gateway to remove rate limits. Self-hosted gateways connect directly to public Flow Access Nodes, which may also optionally be [run](/networks/node-ops/access-nodes/access-node-setup).

info

Apps can use EVM gateway to subsidize user transaction fees for smoother onboarding

Alternatively, you can also choose from any of the following providers who provide the EVM Gateway as a managed service along with other value added services on top.

1. [Alchemy](https://www.alchemy.com/flow)
2. [ThirdWeb](https://thirdweb.com/flow)
3. [Moralis](https://docs.moralis.com/web3-data-api/evm/chains/flow)
4. [QuickNode](https://www.quicknode.com/chains/flow)

## Hardware specifications[​](#hardware-specifications "Direct link to Hardware specifications")

The EVM Gateway is a lightweight node which runs on commodity hardware and cloud VMs. It can be run on GCP **standard** and AWS **large**
VM types for low to moderate volume app co-location use-cases. However, higher volume use cases may require larger instance types and more
testing. An inactive node requires less than 200MB memory when run in Docker and data storage growth corresponds with Flow EVM transaction
growth. Listed below are theoretical RPS maximums based on Flow mainnet CPU and memory resource utilization metrics and linear scaling assumptions.

### Google Cloud Platform (GCP) VM Types[​](#google-cloud-platform-gcp-vm-types "Direct link to Google Cloud Platform (GCP) VM Types")

| VM Type | vCPUs | Memory (GB) | Estimated Max Requests/s |
| --- | --- | --- | --- |
| n2-standard-2 | 2 | 8 | ~2,950 |
| c4a-standard-1 | 1 | 4 | ~1,475 |
| c4a-standard-2 | 2 | 8 | ~2,950 |
| n2-highmem-4 | 4 | 32 | ~11,800 |
| c3-standard-8 | 8 | 32 | ~29,500 |

### Amazon Web Services (AWS) EC2 Instance Types[​](#amazon-web-services-aws-ec2-instance-types "Direct link to Amazon Web Services (AWS) EC2 Instance Types")

| Instance Type | vCPUs | Memory (GB) | Estimated Max Requests/s |
| --- | --- | --- | --- |
| m6i.large | 2 | 8 | ~2,950 |
| c6i.large | 2 | 4 | ~3,687 |
| m6i.xlarge | 4 | 16 | ~11,800 |
| c6i.2xlarge | 8 | 16 | ~29,500 |
| t3.2xlarge | 8 | 32 | ~17,700 |

# How To Run EVM Gateway

## Step 1 - Account Creation[​](#step-1---account-creation "Direct link to Step 1 - Account Creation")

The EVM Gateway's role in mediating EVM transactions over to Cadence is how it accrues fees from handling client transactions. Since
the gateway submits Cadence transactions wrapping EVM transaction payloads to the Flow Access Node the transaction fee for that must
be paid by the EVM Gateway.

The account used for funding gateway Cadence transactions must be a COA, not an EOA. `--coa-address` is configured with the Cadence address
of the COA account and the `--coa-key` must belong to the same account. The `--coinbase` account accrues EVM Gateway fees from EVM client
transactions and can be either an EVM EOA or COA address.

It is acceptable to create a single Cadence account for the COA and use the EVM address associated with that for the COINBASE address.

### Create Flow account to use for COA[​](#create-flow-account-to-use-for-coa "Direct link to Create Flow account to use for COA")

If you don't already have a Flow account you will need to create one.

* Mainnet
* Testnet

1. Install [Flow Wallet](https://wallet.flow.com/)
2. Once installed you will be able to copy the wallet address, similar to *0x1844efeb3fef2242*
3. Obtain account private key from
   ```
   Settings -> Account List -> Choose Main account -> Private Key -> [Password prompt]
   ```
4. Ensure the wallet is funded from a CEX or other wallet

Install [Flow CLI](https://developers.flow.com/tools/flow-cli/install) if not already installed.

 `_10flow keys generate`

This will output something similar to:
`

 `_10🔴️ Store private key safely and don't share with anyone!_10Private Key 3cf8334d.....95c3c54a28e4ad1_10Public Key 33a13ade6....85f1b49a197747_10Mnemonic often scare peanut ... boil corn change_10Derivation Path m/44'/539'/0'/0/0_10Signature Algorithm ECDSA_P256`

Visit <https://faucet.flow.com/>, and use the generated `Public Key`, to create and fund your Flow testnet account.

## Step 2 - Build the gateway[​](#step-2---build-the-gateway "Direct link to Step 2 - Build the gateway")

To run EVM Gateway on bare metal or in a VM without the use of docker, select the '*Build from source*' tab otherwise refer to the
'*Build using Docker*' tab.

* Build from source
* Build using Docker
* Use Docker registry image

This will build the EVM gateway binary from source.

 `_10git clone https://github.com/onflow/flow-evm-gateway.git_10_10cd flow-evm-gateway_10git checkout $(curl -s https://api.github.com/repos/onflow/flow-evm-gateway/releases/latest | jq -r .tag_name)_10CGO_ENABLED=1 go build -o evm-gateway cmd/main/main.go_10chmod a+x evm-gateway_10mv evm-gateway /usr/bin` `_10git clone https://github.com/onflow/flow-evm-gateway.git_10_10cd flow-evm-gateway_10git checkout $(curl -s https://api.github.com/repos/onflow/flow-evm-gateway/releases/latest | jq -r .tag_name)_10make docker-build`

Registry versions available for download can be found [here](https://console.cloud.google.com/artifacts/docker/dl-flow-devex-production/us-west1/development/flow-evm-gateway).

 `_10docker pull us-west1-docker.pkg.dev/dl-flow-devex-production/development/flow-evm-gateway:${VERSION}`
## Step 3 - Start Your Node[​](#step-3---start-your-node "Direct link to Step 3 - Start Your Node")

Operators will need to refer to the gateway [configuration flags](https://github.com/onflow/flow-evm-gateway?tab=readme-ov-file#configuration-flags) and make adjustments that align with the desired
deployment topology.

### EVM Coinbase address[​](#evm-coinbase-address "Direct link to EVM Coinbase address")

If this is your first time setting up the gateway we need to ensure that an EVM COA or EOA address is available to configure the `COINBASE`. This account
can be an account created using Metamask or other web3.js wallet, or otherwise can be the EVM address corresponding to the Flow Wallet COA account created above.

If you haven't already got an EVM address and you have the COA account created by Flow Wallet above then follow the steps below:

* Click top left burger icon to show current profile
* Click 'Enable the path to EVM on Flow' button
* Your EVM account will now be available to use in the left nav account view
* When you switch to that account you can obtain its EVM address

### COA Address and Key[​](#coa-address-and-key "Direct link to COA Address and Key")

COA address and private key is configured for `--coa-address` & `--coa-key` configuration flags. If running multiple EVM Gateway hosts it is standard to
share the same COA address and key across *n* hosts.

### Run the gateway[​](#run-the-gateway "Direct link to Run the gateway")

Ensure that the following ENV variables have been set. Add/update as required if your configuration differs from those listed.

 `_12# Set required environment variables_12export ACCESS_NODE_GRPC_HOST="access.mainnet.nodes.onflow.org:9000" # or access.devnet.nodes.onflow.org:9000 for testnet_12export FLOW_NETWORK_ID="flow-mainnet" # or flow-testnet_12export INIT_CADENCE_HEIGHT="85981135" # 211176670 for testnet_12export COINBASE="${EVM_ADDRESS_WITHOUT_0x}"_12export COA_ADDRESS="${CADENCE_ACCOUNT_ADDRESS_WITHOUT_0x}"_12export COA_KEY="${CADENCE_ACCOUNT_PRIVATE_KEY_WITHOUT_0x}"_12export GAS_PRICE="100" # operators can set this to 0 for zero cost transactions. The linked COA account will pay for transactions on users behalf_12_12# $\{ACCESS_NODE_SPORK_HOSTS\} are comma separated_12# testnet: access-001.devnet51.nodes.onflow.org:9000_12# mainnet: access-001.mainnet25.nodes.onflow.org:9000`

ACCESS\_NODE\_SPORK\_HOSTS is used by the gateway to track state across Flow sporks. These are generally infrequent with only one planned
spork per year. A canonical list of required hosts can be found in the EVM Gateway [Makefile](https://github.com/onflow/flow-evm-gateway/blob/main/Makefile#L9).

* Run from binary
* Run with Docker

**Create EVM Gateway service**

 `_30sudo tee <<EOF >/dev/null /etc/systemd/system/gateway.service_30[Unit]_30Description=Gateway daemon_30After=network-online.target_30_30[Service]_30User=$USER_30ExecStart=/usr/bin/evm-gateway \_30--access-node-grpc-host=$ACCESS_NODE_GRPC_HOST \_30--access-node-spork-hosts=$ACCESS_NODE_SPORK_HOSTS \_30--flow-network-id=$FLOW_NETWORK_ID \_30--init-cadence-height=$INIT_CADENCE_HEIGHT \_30--ws-enabled=true \_30--coinbase=$COINBASE \_30--coa-address=$COA_ADDRESS \_30--coa-key=$COA_KEY \_30--rate-limit=9999999 \_30--rpc-host=0.0.0.0 \_30--gas-price=$GAS_PRICE \_30--tx-state-validation=local-index_30Restart=always_30RestartSec=3_30LimitNOFILE=4096_30_30[Install]_30WantedBy=multi-user.target_30EOF_30_30cat /etc/systemd/system/gateway.service_30sudo systemctl enable gateway`

**Start all services**

 `_10sudo systemctl daemon-reload_10sudo systemctl restart access-node_10sudo systemctl restart gateway`

**Check logs**

 `_10# change log settings to persistent if not already_10sed -i 's/#Storage=auto/Storage=persistent/g' /etc/systemd/journald.conf_10sudo systemctl restart systemd-journald_10_10journalctl -u gateway.service -f -n 100`

It may be necessary to make local changes to the `docker-run` target to add params which are needed for your requirements. If you pulled a
specific image from the gateway container registry ensure that the `$VERSION` environment variable is set to the same as the image version
you pulled.

 `_10cd flow-evm-gateway_10make docker-run`

Additional options are available as follows

 `_10DOCKER_RUN_DETACHED=true _10DOCKER_HOST_MOUNT=[host mount directory] _10DOCKER_HOST_PORT=[desired port to expose on host]_10DOCKER_HOST_METRICS_PORT=[desired port to expose on host for metrics]_10_10# Example usage_10_10make DOCKER_RUN_DETACHED=true DOCKER_HOST_PORT=1234 DOCKER_HOST_MOUNT=/my/host/dir docker-run`
### Startup bootstrap indexing[​](#startup-bootstrap-indexing "Direct link to Startup bootstrap indexing")

Once your EVM Gateway is up and running you will see it indexing the Flow network which was configured. At the present time this
is a lengthy process (possibly 1-3 days, depending on CPU core count) during which time the gateway will not respond to queries.
Once the data is fully indexed the gateway can serve requests to clients.

To speed up gateway setup we recommend backing up the `/${GATEWAY_HOME_DIR}/data` directory to use when creating additional nodes
using the same release version. We are currently working on an export/import feature that will enable gateway operators to
store state snapshots to bootstrap newly created nodes without the delay.

note

If you are upgrading the gateway from pre-v1.0.0 release versions the indexed data directory will need to be reindexed from genesis.
You will not be able to re-use the DB data dir from the previous versions.

### Account and Key Management[​](#account-and-key-management "Direct link to Account and Key Management")

EVM Gateway allows for Google and AWS Key Management Service (KMS) setup, which is the recommended way of setting up the gateway
for live networks. We recommend creating multiple KMS keys for the same Flow account (ideally 10 or more), how many depends on
the desired transaction throughput, since the keys are used in rotation when submitting the transactions. If too few keys
are configured it may result in sequence number collisions if the same key is used concurrently by multiple EVM client requests.

### KMS Configuration[​](#kms-configuration "Direct link to KMS Configuration")

 `_10--coa-cloud-kms-project-id=your-project-kms-id \_10--coa-cloud-kms-location-id=global \_10--coa-cloud-kms-key-ring-id=your-project-kms-key-ring-id \_10--coa-cloud-kms-key=example-gcp-kms1@1,example-gcp-kms2@1 \`
### Monitoring and Metrics[​](#monitoring-and-metrics "Direct link to Monitoring and Metrics")

The EVM Gateway reports Prometheus metrics which are a way to monitor the gateway's availability and progress. The database folder
size may also need to be monitored to prevent disk full issues.

**Metric labels**

 `_12evm_gateway_api_errors_total # Total count of API errors for period_12evm_gateway_api_request_duration_seconds_bucket # Histogram metric buckets for API request durations_12evm_gateway_api_request_duration_seconds_count # Histogram metric API request count for period_12evm_gateway_api_request_duration_seconds_sum # Histogram metric API request sum of values for period_12evm_gateway_api_server_panics_total # Total count of server panics for period_12evm_gateway_blocks_indexed_total # Total count of EVM blocks indexed _12evm_gateway_cadence_block_height # Cadence block height _12evm_gateway_evm_account_interactions_total # Count of unique accounts observed for period_12evm_gateway_evm_block_height # EVM block height _12evm_gateway_operator_balance # Gateway node COA operator account balance_12evm_gateway_trace_download_errors_total # Total count of trace download errors_12evm_gateway_txs_indexed_total # Total count of indexed transactions`

Alerts are recommended to be configured on server panics, low operator balance, and disk usage metrics.

**Metrics port**

 `_10--metrics-port 8080 \`
### Node Status[​](#node-status "Direct link to Node Status")

For basic node status or keepalive monitoring we recommend automated checks on the following monotonically increasing counter:

 `_10curl -s -XPOST 'your-evm-gw-host:8545' --header 'Content-Type: application/json' --data-raw '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' | jq -r '.result' | xargs printf "%d\n"_1010020239`
## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

Join our [Discord](https://discord.com/invite/J6fFnh2xx6) and use the `#flow-evm` channel to ask any questions you may have about
EVM Gateway.

### Database version inconsistency/corruption[​](#database-version-inconsistencycorruption "Direct link to Database version inconsistency/corruption")

If you see a similar message to this from an aborted startup the gateway database directory is not compatible with the schema versions of the runtime, or there may be corruption. In this instance we recommend that you delete the contents of the EVM GW data directory.

 `_10Jan 16 17:00:57 nodename docker[6552]: {"level":"error","error":"failed to open db for dir: /flow-evm-gateway/db, with: pebble: manifest file \"MANIFEST-018340\" for DB \"/flow-evm-gateway/db\": comparer name from file \"leveldb.BytewiseComparator\" != comparer name from Options \"flow.MVCCComparer\"","time":"2025-01-16T17:00:57Z","message":"Gateway runtime error"}`
### State stream configuration[​](#state-stream-configuration "Direct link to State stream configuration")

If you are running an Access Node on the same logical host as the EVM Gateway you may see ehe following log entries.

 `_10failure in event subscription at height ${INIT-CADENCE-HEIGHT}, with: recoverable: disconnected: error receiving event: rpc error: code = Unimplemented desc = unknown service flow.executiondata.ExecutionDataAPI”`
 `_10component execution data indexer initialization failed: could not verify checkpoint file: could not find expected root hash e6d4f4c755666c21d7456441b4d33d3521e5e030b3eae391295577e9130fd715 in checkpoint file which contains: [e10d3c53608a1f195b7969fbc06763285281f64595be491630a1e1bdfbe69161]`

To resolve this configure `--state-stream-addr` to use the same address/port combination which is set for Access Node `--rpc-addr`.
This is required by the gateway to allow both the streaming and non-streaming APIs to query using the same connection.

### Access Node not fully synced[​](#access-node-not-fully-synced "Direct link to Access Node not fully synced")

The following log entry will occur when the EVM Gateway attempts to sync with the Access Node but it has not yet synced up to latest block

 `_10failure in event subscription at height ${INIT-CADENCE-HEIGHT}, with: recoverable: disconnected: error receiving event: rpc error: code = FailedPrecondition desc = could not get start height: failed to get lowest indexed height: index not initialized`[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/node-ops/evm-gateway/evm-gateway-setup.md)Last updated on **Jan 27, 2025** by **j pimmel**[PreviousExecution Data](/networks/node-ops/access-nodes/access-node-configuration-options)[NextLight Node Setup](/networks/node-ops/light-nodes/observer-node)
###### Rate this page

😞😐😊

* [Anyone can run EVM Gateway](#anyone-can-run-evm-gateway)
* [Hardware specifications](#hardware-specifications)
  + [Google Cloud Platform (GCP) VM Types](#google-cloud-platform-gcp-vm-types)
  + [Amazon Web Services (AWS) EC2 Instance Types](#amazon-web-services-aws-ec2-instance-types)
* [Step 1 - Account Creation](#step-1---account-creation)
  + [Create Flow account to use for COA](#create-flow-account-to-use-for-coa)
* [Step 2 - Build the gateway](#step-2---build-the-gateway)
* [Step 3 - Start Your Node](#step-3---start-your-node)
  + [EVM Coinbase address](#evm-coinbase-address)
  + [COA Address and Key](#coa-address-and-key)
  + [Run the gateway](#run-the-gateway)
  + [Startup bootstrap indexing](#startup-bootstrap-indexing)
  + [Account and Key Management](#account-and-key-management)
  + [KMS Configuration](#kms-configuration)
  + [Monitoring and Metrics](#monitoring-and-metrics)
  + [Node Status](#node-status)
* [Troubleshooting](#troubleshooting)
  + [Database version inconsistency/corruption](#database-version-inconsistencycorruption)
  + [State stream configuration](#state-stream-configuration)
  + [Access Node not fully synced](#access-node-not-fully-synced)
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

