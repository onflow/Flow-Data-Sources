# Source: https://developers.flow.com/build/cadence/core-contracts/flow-fees

Flow Fees Contract | Flow Developer Portal



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

* * Cadence* [Core Smart Contracts](/build/cadence/core-contracts)* Flow Fees

On this page

# Flow Fees Contract

## FlowFees[​](#flowfees "Direct link to FlowFees")

The `FlowFees` contract is where all the collected flow fees are gathered.

Source: [FlowFees.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowFees.cdc)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Contract Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Emulator `0xe5a8b7f23e8b548f`| Cadence Testing Framework `0x0000000000000004`| Testnet `0x912d5440f7e3769e`| Mainnet `0xf919ee77447b7497` | | | | | | | | | |

### Events[​](#events "Direct link to Events")

Important events for `FlowFees` are:

`_11

// Event that is emitted when tokens are deposited to the fee vault

_11

access(all) event TokensDeposited(amount: UFix64)

_11

_11

// Event that is emitted when tokens are withdrawn from the fee vault

_11

access(all) event TokensWithdrawn(amount: UFix64)

_11

_11

// Event that is emitted when fees are deducted

_11

access(all) event FeesDeducted(amount: UFix64, inclusionEffort: UFix64, executionEffort: UFix64)

_11

_11

// Event that is emitted when fee parameters change

_11

access(all) event FeeParametersChanged(surgeFactor: UFix64, inclusionEffortCost: UFix64, executionEffortCost: UFix64)`

## FlowStorageFees[​](#flowstoragefees "Direct link to FlowStorageFees")

The `FlowStorageFees` contract defines the parameters and utility methods for storage fees.

Source: [FlowStorageFees.cdc](https://github.com/onflow/flow-core-contracts/blob/master/contracts/FlowStorageFees.cdc)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Network Contract Address|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | Emulator `0xf8d6e0586b0a20c7`| Cadence Testing Framework `0x0000000000000001`| Testnet `0x8c5303eaa26202d6`| Mainnet `0xe467b9dd11fa00df` | | | | | | | | | |

### Events[​](#events-1 "Direct link to Events")

Important events for `FlowStorageFees` are:

`_10

// Emitted when the amount of storage capacity an account has per reserved Flow token changes

_10

access(all) event StorageMegaBytesPerReservedFLOWChanged(_ storageMegaBytesPerReservedFLOW: UFix64)

_10

_10

// Emitted when the minimum amount of Flow tokens that an account needs to have reserved for storage capacity changes.

_10

access(all) event MinimumStorageReservationChanged(_ minimumStorageReservation: UFix64)`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/cadence/core-contracts/05-flow-fees.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Service Account](/build/cadence/core-contracts/service-account)[Next

Staking Table](/build/cadence/core-contracts/staking-contract-reference)

###### Rate this page

😞😐😊

Copy as Markdown

* [FlowFees](#flowfees)
  + [Events](#events)* [FlowStorageFees](#flowstoragefees)
    + [Events](#events-1)

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