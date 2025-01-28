# Source: https://developers.flow.com/networks/staking/staking-rewards




Staking and Delegation rewards | Flow Developer Portal





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
* How to Query Staking rewards
On this page
# Staking and Delegation rewards

## Current method to check staking rewards[​](#current-method-to-check-staking-rewards "Direct link to Current method to check staking rewards")

Rewards payout happens automatically after the end of the epoch and without the need of an explicit transaction being submitted by the service account.
Instead of a separate reward payout transaction, the reward payout events will be recorded in the system chunk in the block that is produced at the time of the epoch transition without creating a regular transaction ID.

The rewards payout can be queried by querying the block which contains the system chunk that contains the reward payout events.

 `_10flow events get A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid --start <block Height> --end <block height> -n mainnet_10_10where block height is the height of the block containing the rewards payout events`

Example

 `_57$ flow events get A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid --start 51753836 --end 51753836 -n mainnet_57_57Events Block #51753836:_57 Index 6_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "a3075cf9280cab4fa0b7b1e639b675bdae3e8874557d98ee78963f0799338a5f"_57 - amount (UFix64): 1660.21200000_57_57 Index 9_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "cf0ff514b6aa659914b99ab1d17743edb2b69fbb338ab01945a08530a98c97d4"_57 - amount (UFix64): 3762.20370347_57_57 Index 12_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "de988efc8cb79d02876b7beffd404fc24b61c287ebeede567f90056f0eece90f"_57 - amount (UFix64): 939.85630919_57_57 Index 27_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "fa5f24a66c2f177ebc09b8b51429e9f157037880290e7858f4336479e57dc26b"_57 - amount (UFix64): 1660.21200000_57_57 Index 30_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "581525fa93d8fe4b334c179698c6e72baccb802593e55e40da61d24e589d85be"_57 - amount (UFix64): 1937.24727662_57 ..._57 ..._57 <clipped for brevity>_57 ..._57 ..._57 Index 50115_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "95ffacf0c05757cff71a4ee49e025d5a6d1103a3aa7d91253079e1bfb7c22458"_57 - delegatorID (UInt32): 23_57 - amount (UFix64): 0.10424555_57_57 Index 50118_57 Type A.8624b52f9ddcd04a.FlowIDTableStaking.DelegatorRewardsPaid_57 Tx ID f31815934bff124e332b3c8be5e1c7a949532707251a9f2f81def8cc9f3d1458_57 Values_57 - nodeID (String): "95ffacf0c05757cff71a4ee49e025d5a6d1103a3aa7d91253079e1bfb7c22458"_57 - delegatorID (UInt32): 18_57 - amount (UFix64): 17.31047712`

Example using [Flow Go SDK](/tools/clients/flow-go-sdk)

 `_39package main_39_39import (_39 "context"_39 "fmt"_39 client "github.com/onflow/flow-go-sdk/access/grpc"_39)_39_39func main() {_39_39 // the Flow testnet community Access node API endpoint_39 accessNodeAddress := "access.mainnet.nodes.onflow.org:9000"_39_39 // create a gRPC client for the Access node_39 accessNodeClient, err := client.NewClient(accessNodeAddress)_39 if err != nil {_39 fmt.Println("err:", err.Error())_39 panic(err)_39 }_39_39 ctx := context.Background()_39_39 blockEvents, err := accessNodeClient.GetEventsForHeightRange(ctx,_39 "A.8624b52f9ddcd04a.FlowIDTableStaking.RewardsPaid",_39 51753836,_39 51753836)_39 if err != nil {_39 panic(err)_39 }_39_39 for _, blockEvent := range blockEvents {_39 fmt.Println("Block: " + blockEvent.BlockID.String())_39 for _, event := range blockEvent.Events {_39 fmt.Println("\tEvent type: " + event.Type)_39 fmt.Println("\tEvent: " + event.Value.String())_39 fmt.Println("\tEvent payload: " + string(event.Payload))_39 }_39 }_39}`
## Check staking rewards before May 2023[​](#check-staking-rewards-before-may-2023 "Direct link to Check staking rewards before May 2023")

Before May 2023, rewards payouts were done manually by the Flow governance committee.

When the transactions executed, they generated events for the rewards paid to each node and delegator.
To check the staking and delegation rewards, those transactions should be queried directly.

Example using [Flow cli](/tools/flow-cli)

 `_64$ flow transactions get 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84 -n mainnet_64_64Status ✅ SEALED_64ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64Payer e467b9dd11fa00df_64Authorizers [e467b9dd11fa00df]_64_64Proposal Key:_64 Address e467b9dd11fa00df_64 Index 11_64 Sequence 118_64_64No Payload Signatures_64_64Envelope Signature 0: e467b9dd11fa00df_64Envelope Signature 1: e467b9dd11fa00df_64Envelope Signature 2: e467b9dd11fa00df_64Envelope Signature 3: e467b9dd11fa00df_64Envelope Signature 4: e467b9dd11fa00df_64Signatures (minimized, use --include signatures)_64_64Events:_64 Index 0_64 Type A.1654653399040a61.FlowToken.TokensWithdrawn_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 64.59694884_64 - from (Address?): 0xf919ee77447b7497_64_64 Index 1_64 Type A.f919ee77447b7497.FlowFees.TokensWithdrawn_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 64.59694884_64_64 Index 2_64 Type A.1654653399040a61.FlowToken.TokensMinted_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 1326397.40305116_64_64 Index 3_64 Type A.1654653399040a61.FlowToken.TokensDeposited_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 1326397.40305116_64 - to (Never?): nil_64_64 Index 4_64 Type A.1654653399040a61.FlowToken.TokensWithdrawn_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 1004.16460872_64 - from (Never?): nil_64_64 Index 5_64 Type A.1654653399040a61.FlowToken.TokensDeposited_64 Tx ID 84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84_64 Values_64 - amount (UFix64): 1004.16460872_64 - to (Address?): 0x8624b52f9ddcd04a_64 ..._64 ..._64 <clipped for brevity>`

Example using [Flow Go SDK](/tools/clients/flow-go-sdk)

 `_42package main_42_42import (_42 "context"_42 "fmt"_42 "github.com/onflow/flow-go-sdk"_42 client "github.com/onflow/flow-go-sdk/access/grpc"_42 "google.golang.org/grpc"_42 "google.golang.org/grpc/credentials/insecure"_42)_42_42func main() {_42_42 // the Flow mainnet community Access node API endpoint_42 accessNodeAddress := "access.mainnet.nodes.onflow.org:9000"_42_42 maxGRPCMessageSize := 1024 * 1024 * 20 // to accommodate for the large transaction payload_42_42 // create a gRPC client for the Access node_42 accessNodeClient, err := client.NewClient(accessNodeAddress,_42 grpc.WithTransportCredentials(insecure.NewCredentials()),_42 grpc.WithDefaultCallOptions(grpc.MaxCallRecvMsgSize(maxGRPCMessageSize)))_42 if err != nil {_42 fmt.Println("err:", err.Error())_42 panic(err)_42 }_42_42 ctx := context.Background()_42_42 txID := flow.HexToID("84eca4ff612ef70047d60510710cca872c8a17c1bd9f63686e74852b6382cc84")_42_42 rewardsTxResult, err := accessNodeClient.GetTransactionResult(ctx, txID)_42 if err != nil {_42 panic(err)_42 }_42_42 for _, event := range rewardsTxResult.Events {_42 fmt.Println("Event type: " + event.Type)_42 fmt.Println("Event: " + event.Value.String())_42 fmt.Println("Event payload: " + string(event.Payload))_42 }_42}`[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/staking/08-staking-rewards.md)Last updated on **Jan 10, 2025** by **Brian Doyle**[PreviousStaking Scripts and Events](/networks/staking/staking-scripts-events)[NextQC and DKG](/networks/staking/qc-dkg)
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

