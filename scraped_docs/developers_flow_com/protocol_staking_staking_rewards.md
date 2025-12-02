# Source: https://developers.flow.com/protocol/staking/staking-rewards

Staking and Delegation rewards | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        + [Epoch and Staking Terminology](/protocol/staking/epoch-terminology)+ [Epoch and Reward Schedule](/protocol/staking/schedule)+ [Epoch Preparation Protocol](/protocol/staking/epoch-preparation)+ [Stake Slashing](/protocol/staking/stake-slashing)+ [Epoch Scripts and Events](/protocol/staking/epoch-scripts-events)+ [Staking Technical Overview](/protocol/staking/technical-overview)+ [Staking Scripts and Events](/protocol/staking/staking-scripts-events)+ [How to Query Staking rewards](/protocol/staking/staking-rewards)+ [QC and DKG](/protocol/staking/qc-dkg)+ [QC/DKG Scripts and Events](/protocol/staking/qc-dkg-scripts-events)+ [Machine Account](/protocol/staking/machine-account)+ [FAQs](/protocol/staking/faq)+ [Technical Staking Options](/protocol/staking/staking-options)+ [Staking Collection Guide](/protocol/staking/staking-collection)* [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            * [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Staking and Epochs](/protocol/staking)* How to Query Staking rewards

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

Example using [Flow Go SDK](/build/tools/clients/flow-go-sdk)

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

Example using [Flow cli](/build/tools/flow-cli)

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

Example using [Flow Go SDK](/build/tools/clients/flow-go-sdk)

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

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/staking/08-staking-rewards.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Staking Scripts and Events](/protocol/staking/staking-scripts-events)[Next

QC and DKG](/protocol/staking/qc-dkg)

###### Rate this page

😞😐😊

Copy as Markdown

* [Current method to check staking rewards](#current-method-to-check-staking-rewards)* [Check staking rewards before May 2023](#check-staking-rewards-before-may-2023)

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