# Source: https://developers.flow.com/build/cadence/core-contracts/epoch-contract-reference

Flow Epoch Contracts Reference | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)

                - [Fungible Token](/build/cadence/core-contracts/fungible-token)- [Flow Token](/build/cadence/core-contracts/flow-token)- [Service Account](/build/cadence/core-contracts/service-account)- [Flow Fees](/build/cadence/core-contracts/flow-fees)- [Staking Table](/build/cadence/core-contracts/staking-contract-reference)- [Epoch Contracts](/build/cadence/core-contracts/epoch-contract-reference)- [Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)- [NFT Metadata](/build/cadence/core-contracts/nft-metadata)- [NFT Storefront](/build/cadence/core-contracts/nft-storefront)- [Staking Collection](/build/cadence/core-contracts/staking-collection)- [Account Linking](/build/cadence/core-contracts/hybrid-custody)- [EVM](/build/cadence/core-contracts/evm)- [Burner](/build/cadence/core-contracts/burner)- [VM Bridge](/build/cadence/core-contracts/bridge)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

* * Cadence* [Core Smart Contracts](/build/cadence/core-contracts)* Epoch Contracts

On this page

# Contract

The `FlowEpoch` contract is the state machine that manages Epoch phases and emits service events.
The `FlowClusterQC` and `FlowDKG` contracts manage the processes that happen during the Epoch Setup phase.

These contracts are all deployed to the same account as the `FlowIDTableStaking` contract.

Sources:

* [FlowEpoch.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowEpoch.cdc)
* [FlowClusterQC.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowClusterQC.cdc)
* [FlowDKG.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/epochs/FlowDKG.cdc)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Contract Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Emulator `0xf8d6e0586b0a20c7`| Cadence Testing Framework `0x0000000000000001`| Testnet `0x9eca2b38b18b5dfe`| Mainnet `0x8624b52f9ddcd04a` | | | | | | | | | |

# Transactions

## Getting Epoch Info[​](#getting-epoch-info "Direct link to Getting Epoch Info")

These scripts are read-only and get info about the current state of the epoch contract.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID Name Source|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **`EP.01`** Get Epoch Metadata [epoch/get\_epoch\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_metadata.cdc)| **`EP.02`** Get Configurable Metadata [epoch/get\_config\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_config_metadata.cdc)| **`EP.03`** Get Epoch Counter [epoch/get\_epoch\_counter.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_counter.cdc)| **`EP.04`** Get Epoch Phase [epoch/get\_epoch\_phase.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/epoch/scripts/get_epoch_phase.cdc) | | | | | | | | | | | | | | |

## Quorum Certificate Transactions and Scripts[​](#quorum-certificate-transactions-and-scripts "Direct link to Quorum Certificate Transactions and Scripts")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID Name Source|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **`QC.01`** Create QC Voter [quorumCertificate/get\_epoch\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/create_voter.cdc)| **`QC.02`** Submit QC Vote [quorumCertificate/get\_config\_metadata.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/submit_vote.cdc)| **`QC.03`** Get Collector Cluster [quorumCertificate/scripts/get\_cluster.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_cluster.cdc)| **`QC.04`** Get QC Enabled [quorumCertificate/scripts/get\_qc\_enabled.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_qc_enabled.cdc)| **`QC.05`** Get Node Has Voted [quorumCertificate/scripts/get\_node\_has\_voted.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_node_has_voted.cdc)| **`QC.06`** Get QC Voting Complete [quorumCertificate/scripts/get\_voting\_completed.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/quorumCertificate/scripts/get_voting_completed.cdc) | | | | | | | | | | | | | | | | | | | | |

## DKG Transactions and Scripts[​](#dkg-transactions-and-scripts "Direct link to DKG Transactions and Scripts")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ID Name Source|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **`DKG.01`** Create DKG Participant [dkg/create\_participant.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/create_participant.cdc)| **`DKG.02`** Get Configurable Metadata [dkg/send\_whiteboard\_message.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_whiteboard_message.cdc)| **`DKG.03`** Send Final Submission [dkg/send\_final\_submission.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/send_final_submission.cdc)| **`DKG.04`** Get DKG Enabled [dkg/scripts/get\_dkg\_enabled.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_enabled.cdc)| **`DKG.05`** Get DKG Completed [dkg/scripts/get\_dkg\_completed.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_dkg_completed.cdc)| **`DKG.06`** Get Whiteboard Messages [dkg/scripts/get\_whiteboard\_messages.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_whiteboard_messages.cdc)| **`DKG.07`** Get Final Submissions [dkg/scripts/get\_final\_submissions.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_final_submissions.cdc)| **`DKG.08`** Get Node Has Submitted [dkg/scripts/get\_node\_has\_submitted.cdc](https://github.com/onflow/flow-core-contracts/blob/master/transactions/dkg/scripts/get_node_has_submitted.cdc) | | | | | | | | | | | | | | | | | | | | | | | | | | |

# Events

See the [epoch documentation](/protocol/staking/epoch-scripts-events)
for a list and documentation for important `FlowEpoch` events.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/07-epoch-contract-reference.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Staking Table](/build/cadence/core-contracts/staking-contract-reference)[Next

Non-Fungible Token](/build/cadence/core-contracts/non-fungible-token)

###### Rate this page

😞😐😊

Copy as Markdown

* [Getting Epoch Info](#getting-epoch-info)* [Quorum Certificate Transactions and Scripts](#quorum-certificate-transactions-and-scripts)* [DKG Transactions and Scripts](#dkg-transactions-and-scripts)

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