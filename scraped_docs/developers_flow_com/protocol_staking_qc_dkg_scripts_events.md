# Source: https://developers.flow.com/protocol/staking/qc-dkg-scripts-events

Query QC/DKG Info with Scripts or Events | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        + [Epoch and Staking Terminology](/protocol/staking/epoch-terminology)+ [Epoch and Reward Schedule](/protocol/staking/schedule)+ [Epoch Preparation Protocol](/protocol/staking/epoch-preparation)+ [Stake Slashing](/protocol/staking/stake-slashing)+ [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events)+ [Staking Technical Overview](/protocol/staking/technical-overview)+ [Staking Scripts and Events](/protocol/staking/staking-scripts-events)+ [How to Query Staking rewards](/protocol/staking/staking-rewards)+ [QC and DKG](/protocol/staking/qc-dkg)+ [QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)+ [Machine Account](/protocol/staking/machine-account)+ [FAQs](/protocol/staking/faq)+ [Technical Staking Options](/protocol/staking/staking-options)+ [Staking Collection Guide](/protocol/staking/staking-collection)* [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Staking and Epochs](/protocol/staking)* QC/DKG Scripts and Events

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
can use the **Get Cluster** ([QC.03](/build/cadence/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with the following argument:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Argument Type Description|  |  |  | | --- | --- | --- | | **clusterIndex** `UInt16` The index of the cluster to query | | | | | |

### Get QC Enabled[​](#get-qc-enabled "Direct link to Get QC Enabled")

To return a boolean representing if the QC is enabled,
can use the **Get QC Enabled** ([QC.04](/build/cadence/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with no arguments.

### Get Node Has Voted[​](#get-node-has-voted "Direct link to Get Node Has Voted")

To return a boolean representing if a node has voted for the current QC, you
can use the **Get Node Has Voted** ([QC.05](/build/cadence/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with the following argument:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Argument Type Description|  |  |  | | --- | --- | --- | | **nodeID** `String` The node ID to check for | | | | | |

### Get Voting Complete[​](#get-voting-complete "Direct link to Get Voting Complete")

To return a boolean representing if the voting for the QC phase is complete,
can use the **Get Voting Complete** ([QC.06](/build/cadence/core-contracts/epoch-contract-reference#quorum-certificate-transactions-and-scripts)) script with no arguments.

## DKG Scripts[​](#dkg-scripts "Direct link to DKG Scripts")

### Get DKG Enabled[​](#get-dkg-enabled "Direct link to Get DKG Enabled")

To return a boolean representing if the DKG is enabled, you
can use the **Get DKG Enabled** ([DKG.04](/build/cadence/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get DKG Completed[​](#get-dkg-completed "Direct link to Get DKG Completed")

To return a boolean representing if the dkg is complete, you
can use the **Get DKG Complete** ([DKG.05](/build/cadence/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Whiteboard Messages[​](#get-whiteboard-messages "Direct link to Get Whiteboard Messages")

To return an array of structs representing all the whiteboard messages, you
can use the **Get DKG Whiteboard Messages** ([DKG.06](/build/cadence/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Final Submissions[​](#get-final-submissions "Direct link to Get Final Submissions")

To return an array of key vectors for the nodes' final submissions, you
can use the **Get Final Submissions** ([DKG.07](/build/cadence/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with no arguments.

### Get Node Has Submitted[​](#get-node-has-submitted "Direct link to Get Node Has Submitted")

To return a boolean representing if a node has sent their final submission for the DKG, you
can use the **Get Node Has Submitted** ([DKG.08](/build/cadence/core-contracts/epoch-contract-reference#dkg-transactions-and-scripts)) script with the following argument:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Argument Type Description|  |  |  | | --- | --- | --- | | **nodeID** `String` The node ID to check for | | | | | |

## DKG Events[​](#dkg-events "Direct link to DKG Events")

`_10

/// Emitted when the admin enables the DKG

_10

access(all) event StartDKG()

_10

_10

/// Emitted when the admin ends the DKG after enough submissions have been recorded

_10

access(all) event EndDKG(finalSubmission: [String?]?)

_10

_10

/// Emitted when a consensus node has posted a message to the DKG whiteboard

_10

access(all) event BroadcastMessage(nodeID: String, content: String)`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/10-qc-dkg-scripts-events.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

QC and DKG](/protocol/staking/qc-dkg)[Next

Machine Account](/protocol/staking/machine-account)

###### Rate this page

😞😐😊

Copy as Markdown

* [QC Scripts](#qc-scripts)
  + [Get Clusters](#get-clusters)+ [Get QC Enabled](#get-qc-enabled)+ [Get Node Has Voted](#get-node-has-voted)+ [Get Voting Complete](#get-voting-complete)* [DKG Scripts](#dkg-scripts)
    + [Get DKG Enabled](#get-dkg-enabled)+ [Get DKG Completed](#get-dkg-completed)+ [Get Whiteboard Messages](#get-whiteboard-messages)+ [Get Final Submissions](#get-final-submissions)+ [Get Node Has Submitted](#get-node-has-submitted)* [DKG Events](#dkg-events)

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