# Source: https://developers.flow.com/networks/staking/staking-rewards

Staking and Delegation rewards | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

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
* How to Query Staking rewards

On this page

# Staking and Delegation rewards

## Current method to check staking rewards[​](#current-method-to-check-staking-rewards "Direct link to Current method to check staking rewards")

Rewards payout happens automatically after the end of the epoch and without the need of an explicit transaction being submitted by the service account.
Instead of a separate reward payout transaction, the reward payout events will be recorded in the system chunk in the block that is produced at the time of the epoch transition without creating a regular transaction ID.

The rewards payout can be queried by querying the block which contains the system chunk that contains the reward payout events.

`_10

flow events get A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid --start <block Height> --end <block height> -n mainnet

_10

_10

where block height is the height of the block containing the rewards payout events`

Example

`_57

$ flow events get A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid --start 51753836 --end 51753836 -n mainnet

_57

_57

Events Block #51753836:

_57

Index 6

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "a3075cf9280cab4fa0b7b1e639b675bdae3e8874557d98ee78963f0799338a5f"

_57

- amount (UFix64): 1660.21200000

_57

_57

Index 9

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "cf0ff514b6aa659914b99ab1d17743edb2b69fbb338ab01945a08530a98c97d4"

_57

- amount (UFix64): 3762.20370347

_57

_57

Index 12

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "de988efc8cb79d02876b7beffd404fc24b61c287ebeede567f90056f0eece90f"

_57

- amount (UFix64): 939.85630919

_57

_57

Index 27

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "fa5f24a66c2f177ebc09b8b51429e9f157037880290e7858f4336479e57dc26b"

_57

- amount (UFix64): 1660.21200000

_57

_57

Index 30

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "581525fa93d8fe4b334c179698c6e72baccb802593e55e40da61d24e589d85be"

_57

- amount (UFix64): 1937.24727662

_57

...

_57

...

_57

<clipped for brevity>

_57

...

_57

...

_57

Index 50115

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "95ffacf0c05757cff71a4ee49e025d5a6d1103a3aa7d91253079e1bfb7c22458"

_57

- delegatorID (UInt32): 23

_57

- amount (UFix64): 0.10424555

_57

_57

Index 50118

_57

Type A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid

_57

Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458

_57

Values

_57

- nodeID (String): "95ffacf0c05757cff71a4ee49e025d5a6d1103a3aa7d91253079e1bfb7c22458"

_57

- delegatorID (UInt32): 18

_57

- amount (UFix64): 17.31047712`

Example using [Flow Go SDK](/tools/clients/flow-go-sdk)

`_39

package main

_39

_39

import (

_39

"context"

_39

"fmt"

_39

client "github.com/onflow/flow-go-sdk/access/grpc"

_39

)

_39

_39

func main() {

_39

_39

// the Flow testnet community Access node API endpoint

_39

accessNodeAddress := "access.mainnet.nodes.onflow.org:9000"

_39

_39

// create a gRPC client for the Access node

_39

accessNodeClient, err := client.NewClient(accessNodeAddress)

_39

if err != nil {

_39

fmt.Println("err:", err.Error())

_39

panic(err)

_39

}

_39

_39

ctx := context.Background()

_39

_39

blockEvents, err := accessNodeClient.GetEventsForHeightRange(ctx,

_39

"A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid",

_39

51753836,

_39

51753836)

_39

if err != nil {

_39

panic(err)

_39

}

_39

_39

for _, blockEvent := range blockEvents {

_39

fmt.Println("Block: " + blockEvent.BlockID.String())

_39

for _, event := range blockEvent.Events {

_39

fmt.Println("\tEvent type: " + event.Type)

_39

fmt.Println("\tEvent: " + event.Value.String())

_39

fmt.Println("\tEvent payload: " + string(event.Payload))

_39

}

_39

}

_39

}`

## Check staking rewards before May 2023[​](#check-staking-rewards-before-may-2023 "Direct link to Check staking rewards before May 2023")

Before May 2023, rewards payouts were done manually by the Flow governance committee.

When the transactions executed, they generated events for the rewards paid to each node and delegator.
To check the staking and delegation rewards, those transactions should be queried directly.

Example using [Flow cli](/tools/flow-cli)

`_64

$ flow transactions get 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84 -n mainnet

_64

_64

Status ✅ SEALED

_64

ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Payer e467b9dd11fa00df

_64

Authorizers [e467b9dd11fa00df]

_64

_64

Proposal Key:

_64

Address e467b9dd11fa00df

_64

Index 11

_64

Sequence 118

_64

_64

No Payload Signatures

_64

_64

Envelope Signature 0: e467b9dd11fa00df

_64

Envelope Signature 1: e467b9dd11fa00df

_64

Envelope Signature 2: e467b9dd11fa00df

_64

Envelope Signature 3: e467b9dd11fa00df

_64

Envelope Signature 4: e467b9dd11fa00df

_64

Signatures (minimized, use --include signatures)

_64

_64

Events:

_64

Index 0

_64

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 64.59694884

_64

- from (Address?): 0xf919ee77447b7497

_64

_64

Index 1

_64

Type A.f919ee77447b7497.FlowFees.TokensWithdrawn

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 64.59694884

_64

_64

Index 2

_64

Type A.1654653399040a61.FlowToken.TokensMinted

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 1326397.40305116

_64

_64

Index 3

_64

Type A.1654653399040a61.FlowToken.TokensDeposited

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 1326397.40305116

_64

- to (Never?): nil

_64

_64

Index 4

_64

Type A.1654653399040a61.FlowToken.TokensWithdrawn

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 1004.16460872

_64

- from (Never?): nil

_64

_64

Index 5

_64

Type A.1654653399040a61.FlowToken.TokensDeposited

_64

Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84

_64

Values

_64

- amount (UFix64): 1004.16460872

_64

- to (Address?): 0x8624b52f9ddcd04a

_64

...

_64

...

_64

<clipped for brevity>`

Example using [Flow Go SDK](/tools/clients/flow-go-sdk)

`_42

package main

_42

_42

import (

_42

"context"

_42

"fmt"

_42

"github.com/onflow/flow-go-sdk"

_42

client "github.com/onflow/flow-go-sdk/access/grpc"

_42

"google.golang.org/grpc"

_42

"google.golang.org/grpc/credentials/insecure"

_42

)

_42

_42

func main() {

_42

_42

// the Flow mainnet community Access node API endpoint

_42

accessNodeAddress := "access.mainnet.nodes.onflow.org:9000"

_42

_42

maxGRPCMessageSize := 1024 * 1024 * 20 // to accommodate for the large transaction payload

_42

_42

// create a gRPC client for the Access node

_42

accessNodeClient, err := client.NewClient(accessNodeAddress,

_42

grpc.WithTransportCredentials(insecure.NewCredentials()),

_42

grpc.WithDefaultCallOptions(grpc.MaxCallRecvMsgSize(maxGRPCMessageSize)))

_42

if err != nil {

_42

fmt.Println("err:", err.Error())

_42

panic(err)

_42

}

_42

_42

ctx := context.Background()

_42

_42

txID := flow.HexToID("84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84")

_42

_42

rewardsTxResult, err := accessNodeClient.GetTransactionResult(ctx, txID)

_42

if err != nil {

_42

panic(err)

_42

}

_42

_42

for _, event := range rewardsTxResult.Events {

_42

fmt.Println("Event type: " + event.Type)

_42

fmt.Println("Event: " + event.Value.String())

_42

fmt.Println("Event payload: " + string(event.Payload))

_42

}

_42

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/08-staking-rewards.md)

Last updated on **Feb 27, 2025** by **BT.Wood(Tang Bo Hao)**

[Previous

Staking Scripts and Events](/networks/staking/staking-scripts-events)[Next

QC and DKG](/networks/staking/qc-dkg)

###### Rate this page

😞😐😊

* [Current method to check staking rewards](#current-method-to-check-staking-rewards)
* [Check staking rewards before May 2023](#check-staking-rewards-before-may-2023)

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