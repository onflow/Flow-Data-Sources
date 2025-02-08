# Source: https://developers.flow.com/networks/staking/qc-dkg-scripts-events




Query QC/DKG Info with Scripts or Events | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
  + [Epoch and Staking Terminology](/networks/staking/epoch-terminology)
  + [Epoch and Reward Schedule](/networks/staking/schedule)
  + [Epoch Preparation Protocol](/networks/staking/epoch-preparation)
  + [Stake Slashing](/networks/staking/stake-slashing)
  + [Epoch Scripts and Events](/networks/staking/epoch-scripts-events)
  + [Staking Technical Overview](/networks/staking/technical-overview)
  + [Staking Scripts and Events](/networks/staking/staking-scripts-events)
  + [How to Query Staking rewards](/networks/staking/staking-rewards)
  + [QC and DKG](/networks/staking/qc-dkg)
  + [QC/DKG Scripts and Events](/networks/staking/qc-dkg-scripts-events)
  + [Machine Account](/networks/staking/machine-account)
  + [FAQs](/networks/staking/faq)
  + [Technical Staking Options](/networks/staking/staking-options)
  + [Staking Collection Guide](/networks/staking/staking-collection)
  + [Basic Staking Guide (Deprecated)](/networks/staking/staking-guide)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)


* [Staking and Epochs](/networks/staking)
* QC/DKG Scripts and Events
On this page
# Introduction

The Cluster Quorum Certificate (QC) and Distributed Key Generation (DKG) protocol smart contracts
store a lot of different state, and the state is constantly changing.
As an external party, there are two ways to keep track of these state changes.
You can either use Cadence scripts to query the state of the contract at any given time,
or you can monitor events that are emitted by the contracts to be notified of any important occurrences.

# Query Information with Scripts

These events can be queried using the Go or JavaScript SDKs to extract useful notifications and information about the
state of these processes.

## QC Scripts[​](#qc-scripts "Direct link to QC Scripts")

These scripts allow anyone to query information about the state of the QC contract.

### Get Clusters[​](#get-clusters "Direct link to Get Clusters")

To return a struct representing the information associated with a collector cluster,
can use the **Get Cluster** ([QC.03](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with the following argument:

| Argument | Type | Description |
| --- | --- | --- |
| **clusterIndex** | `UInt16` | The index of the cluster to query |

### Get QC Enabled[​](#get-qc-enabled "Direct link to Get QC Enabled")

To return a boolean representing if the QC is enabled,
can use the **Get QC Enabled** ([QC.04](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with no arguments.

### Get Node Has Voted[​](#get-node-has-voted "Direct link to Get Node Has Voted")

To return a boolean representing if a node has voted for the current QC, you
can use the **Get Node Has Voted** ([QC.05](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with the following argument:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID to check for |

### Get Voting Complete[​](#get-voting-complete "Direct link to Get Voting Complete")

To return a boolean representing if the voting for the QC phase is complete,
can use the **Get Voting Complete** ([QC.06](/build/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with no arguments.

## QC Events[​](#qc-events "Direct link to QC Events")

Documentation coming soon

## DKG Scripts[​](#dkg-scripts "Direct link to DKG Scripts")

### Get DKG Enabled[​](#get-dkg-enabled "Direct link to Get DKG Enabled")

To return a boolean representing if the DKG is enabled, you
can use the **Get DKG Enabled** ([DKG.04](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get DKG Completed[​](#get-dkg-completed "Direct link to Get DKG Completed")

To return a boolean representing if the dkg is complete, you
can use the **Get DKG Complete** ([DKG.05](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Whiteboard Messages[​](#get-whiteboard-messages "Direct link to Get Whiteboard Messages")

To return an array of structs representing all the whiteboard messages, you
can use the **Get DKG Whiteboard Messages** ([DKG.06](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Final Submissions[​](#get-final-submissions "Direct link to Get Final Submissions")

To return an array of key vectors for the nodes' final submissions, you
can use the **Get Final Submissions** ([DKG.07](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Node Has Submitted[​](#get-node-has-submitted "Direct link to Get Node Has Submitted")

To return a boolean representing if a node has sent their final submission for the DKG, you
can use the **Get Node Has Submitted** ([DKG.08](/build/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with the following argument:

| Argument | Type | Description |
| --- | --- | --- |
| **nodeID** | `String` | The node ID to check for |

## DKG Events[​](#dkg-events "Direct link to DKG Events")

 `_10/// Emitted when the admin enables the DKG_10access(all) event StartDKG()_10_10/// Emitted when the admin ends the DKG after enough submissions have been recorded_10access(all) event EndDKG(finalSubmission: [String?]?)_10_10/// Emitted when a consensus node has posted a message to the DKG whiteboard_10access(all) event BroadcastMessage(nodeID: String, content: String)`[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/10-qc-dkg-scripts-events.md)Last updated on **Jan 27, 2025** by **j pimmel**[PreviousQC and DKG](/networks/staking/qc-dkg)[NextMachine Account](/networks/staking/machine-account)
###### Rate this page

😞😐😊

* [QC Scripts](#qc-scripts)
  + [Get Clusters](#get-clusters)
  + [Get QC Enabled](#get-qc-enabled)
  + [Get Node Has Voted](#get-node-has-voted)
  + [Get Voting Complete](#get-voting-complete)
* [QC Events](#qc-events)
* [DKG Scripts](#dkg-scripts)
  + [Get DKG Enabled](#get-dkg-enabled)
  + [Get DKG Completed](#get-dkg-completed)
  + [Get Whiteboard Messages](#get-whiteboard-messages)
  + [Get Final Submissions](#get-final-submissions)
  + [Get Node Has Submitted](#get-node-has-submitted)
* [DKG Events](#dkg-events)
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

