# Source: https://developers.flow.com/build/core-contracts/epoch-contract-reference

Flow Epoch Contracts Reference | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/network-architecture)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)
* [Core Smart Contracts](/build/core-contracts)

  + [Fungible Token](/build/core-contracts/fungible-token)
  + [Flow Token](/build/core-contracts/flow-token)
  + [Service Account](/build/core-contracts/service-account)
  + [Flow Fees](/build/core-contracts/flow-fees)
  + [Staking Table](/build/core-contracts/staking-contract-reference)
  + [Epoch Contracts](/build/core-contracts/epoch-contract-reference)
  + [Non-Fungible Token](/build/core-contracts/non-fungible-token)
  + [NFT Metadata](/build/core-contracts/nft-metadata)
  + [NFT Storefront](/build/core-contracts/nft-storefront)
  + [Staking Collection](/build/core-contracts/staking-collection)
  + [Account Linking](/build/core-contracts/hybrid-custody)
  + [EVM](/build/core-contracts/evm)
  + [Burner](/build/core-contracts/burner)
  + [VM Bridge](/build/core-contracts/bridge)
* [Explore More](/build/explore-more)

* [Core Smart Contracts](/build/core-contracts)
* Epoch Contracts

On this page

# Contract

The `FlowEpoch` contract is the state machine that manages Epoch phases and emits service events.
The `FlowClusterQC` and `FlowDKG` contracts manage the processes that happen during the Epoch Setup phase.

These contracts are all deployed to the same account as the `FlowIDTableStaking` contract.

Sources:

* [FlowEpoch.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowEpoch.cdc)
* [FlowClusterQC.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowClusterQC.cdc)
* [FlowDKG.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowDKG.cdc)

| Network | Contract Address |
| --- | --- |
| Emulator | `0xf8d6e0586b0a20c7` |
| Cadence Testing Framework | `0x0000000000000001` |
| Testnet | `0x9eca2b38b18b5dfe` |
| Mainnet | `0x8624b52f9ddcd04a` |

# Transactions

## Getting Epoch Info[​](#getting-epoch-info "Direct link to Getting Epoch Info")

These scripts are read-only and get info about the current state of the epoch contract.

| ID | Name | Source |
| --- | --- | --- |
| **`EP.01`** | Get Epoch Metadata | [epoch/get\_epoch\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_metadata.cdc) |
| **`EP.02`** | Get Configurable Metadata | [epoch/get\_config\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_config_metadata.cdc) |
| **`EP.03`** | Get Epoch Counter | [epoch/get\_epoch\_counter.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_counter.cdc) |
| **`EP.04`** | Get Epoch Phase | [epoch/get\_epoch\_phase.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_phase.cdc) |

## Quorum Certificate Transactions and Scripts[​](#quorum-certificate-transactions-and-scripts "Direct link to Quorum Certificate Transactions and Scripts")

| ID | Name | Source |
| --- | --- | --- |
| **`QC.01`** | Create QC Voter | [quorumCertificate/get\_epoch\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/create_voter.cdc) |
| **`QC.02`** | Submit QC Vote | [quorumCertificate/get\_config\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/submit_vote.cdc) |
| **`QC.03`** | Get Collector Cluster | [quorumCertificate/scripts/get\_cluster.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster.cdc) |
| **`QC.04`** | Get QC Enabled | [quorumCertificate/scripts/get\_qc\_enabled.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_qc_enabled.cdc) |
| **`QC.05`** | Get Node Has Voted | [quorumCertificate/scripts/get\_node\_has\_voted.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_node_has_voted.cdc) |
| **`QC.06`** | Get QC Voting Complete | [quorumCertificate/scripts/get\_voting\_completed.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_voting_completed.cdc) |

## DKG Transactions and Scripts[​](#dkg-transactions-and-scripts "Direct link to DKG Transactions and Scripts")

| ID | Name | Source |
| --- | --- | --- |
| **`DKG.01`** | Create DKG Participant | [dkg/create\_participant.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/create_participant.cdc) |
| **`DKG.02`** | Get Configurable Metadata | [dkg/send\_whiteboard\_message.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_whiteboard_message.cdc) |
| **`DKG.03`** | Send Final Submission | [dkg/send\_final\_submission.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_final_submission.cdc) |
| **`DKG.04`** | Get DKG Enabled | [dkg/scripts/get\_dkg\_enabled.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_enabled.cdc) |
| **`DKG.05`** | Get DKG Completed | [dkg/scripts/get\_dkg\_completed.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_completed.cdc) |
| **`DKG.06`** | Get Whiteboard Messages | [dkg/scripts/get\_whiteboard\_messages.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_whiteboard_messages.cdc) |
| **`DKG.07`** | Get Final Submissions | [dkg/scripts/get\_final\_submissions.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_final_submissions.cdc) |
| **`DKG.08`** | Get Node Has Submitted | [dkg/scripts/get\_node\_has\_submitted.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_has_submitted.cdc) |

# Events

See the [epoch documentation](/networks/staking/epoch-scripts-events)
for a list and documentation for important `FlowEpoch` events.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/core-contracts/07-epoch-contract-reference.md)

Last updated on **Apr 4, 2025** by **Brian Doyle**

[Previous

Staking Table](/build/core-contracts/staking-contract-reference)[Next

Non-Fungible Token](/build/core-contracts/non-fungible-token)

###### Rate this page

😞😐😊

* [Getting Epoch Info](#getting-epoch-info)
* [Quorum Certificate Transactions and Scripts](#quorum-certificate-transactions-and-scripts)
* [DKG Transactions and Scripts](#dkg-transactions-and-scripts)

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
* [Flowscan Mainnet](https://flowscan.io/)
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