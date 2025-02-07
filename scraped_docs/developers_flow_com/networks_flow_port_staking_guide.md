# Source: https://developers.flow.com/networks/flow-port/staking-guide




Flow Port Staking Guide | Flow Developer Portal





[Skip to main content](#__docusaurus_skipToContent_fallback)[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build With Cadence](/build/flow)[Build With EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)Connect[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)
  + [Flow Port Staking Guide](/networks/flow-port/staking-guide)


* [Flow Port](/networks/flow-port)
* Flow Port Staking Guide
On this page
# Flow Port Staking Guide

This guide provides step-by-step instructions for using the Flow Port to stake your FLOW tokens and start earning rewards.
Currently, Flow Port only supports staking or delegating using tokens held in Blocto or Ledger wallets.
If you're new to the concepts of staking and delegating you can [read this guide](/networks/staking) to learn more.

## First Step[​](#first-step "Direct link to First Step")

When you arrive in Port, select **Stake & Delegate** from the left-hand menu. You should be taken to this page.

![Flow Port Staking pt. 0](/assets/images/port-stake-0-00-15c75f58a27d277620ad56e79959274d.png)

From here you can decide whether to stake or delegate.

* Select **Stake** if you plan to stake a node you're running.
* Select **Delegate** to delegate your stake to another Node Operator. You don't need to know which Node Operator, you'll be provided with a list to choose from. If you are not running your own node you scan skip directly to the [delegation section](#delegating)

## Stake a Node[​](#stake-a-node "Direct link to Stake a Node")

Users who will be running their own nodes can stake them using the Flow Port.

#### Prerequisites[​](#prerequisites "Direct link to Prerequisites")

In order to stake your node, you'll need to have the required amount of FLOW for your node type.
You'll also need the following information about your node:

* Node ID
* Network Address
* Networking Key
* Staking Key
* Machine Account Public Key (for collection/consensus nodes only)

If you don't have this information, go [here](/networks/node-ops/node-operation/node-bootstrap#step-1---run-genesis-bootstrap) for instructions on how to acquire it.

### Begin Staking[​](#begin-staking "Direct link to Begin Staking")

First, select the type of node you'll be running by choosing from the list. You must have the required amount of locked FLOW in your account.

![Flow Port Staking](/assets/images/port-stake-0-02-ec632972b71f3d1cc02500b1d696101b.png)

Once you selected your node type, click next and specify how much you'd like to stake. The minimum amount for your node type is required,
but you may stake as much as you like beyond that. Here's the screen you should see:

![Flow Port Staking](/assets/images/port-stake-0-03-7365204b6912f08d81ff9f3127121c5b.png)

Clicking next will take you to the final screen, where you'll need to enter information about your node you previously obtained.
If you don't have this information, go [here](/networks/node-ops/node-operation/node-bootstrap#step-1---run-genesis-bootstrap) for instructions on how to acquire it.
Here's the screen you should see:

![Flow Port Staking](/assets/images/port-stake-0-04-72ee335247ea972bff2a6d207cb27562.png)

Clicking next will take you to a confirmation screen. This is your chance to double-check that you've entered your information correctly. If you're ready, check the
box confirming your information and click submit to send the transaction that will stake your node! You should see a transaction status screen like this:

![Flow Port Staking](/assets/images/port-stake-0-05-c5c93efbe7b4a58126c2afb3b7b6bcd7.png)

**Note:** If your transaction fails, double-check the information you provided.   
   


If you return to the home screen, you'll be able to see your staking request in progress!

![Flow Port Staking](/assets/images/port-stake-4-91a68814d26e24a5ad2e1d3df28a9eab.png)

## Delegating[​](#delegating "Direct link to Delegating")

Delegating is the process of staking your locked FLOW to nodes which are being run by another party.

#### Prerequisites[​](#prerequisites-1 "Direct link to Prerequisites")

In order to delegate your stake to another node, you'll need to know the **node operator ID** of the operator who is running the nodes you wish to stake.
Here is a list of node operator IDs you can delegate to: [List of Available Node Operators](https://github.com/onflow/flow/blob/master/nodeoperators/NodeOperatorList.md)

### Enter a Node Operator ID[​](#enter-a-node-operator-id "Direct link to Enter a Node Operator ID")

Simply enter the ID of the node operator of your choice and click next.

![Flow Port Staking](/assets/images/port-delegate-1-1ca9effbfed4491f8eb74bc789b23fd6.png)

### Enter an amount[​](#enter-an-amount "Direct link to Enter an amount")

Next you'll enter an amount of FLOW you would like to delegate. When delegating you may send any amount to the node operator.

![Flow Port Staking](/assets/images/port-delegate-2-ce86317bccedc87ba69a60dd86190424.png)

Click next to reach the confirmation screen. Confirm the details of your delegation request and click submit!

![Flow Port Staking](/assets/images/port-delegate-3-1e23cd6033ad6769a16bae70a48f3347.png)

Once your transaction is submitted, you can monitor its status from this screen, or return to the Flow Port home screen.

![Flow Port Staking](/assets/images/port-delegate-4-f2cfdf332ed864627842f929e6457e53.png)

**Note:** If you transaction fails, double-check the information you provided.   
   


That's it! You've successfully delegated stake to your chosen node operator!

## Returning to Port[​](#returning-to-port "Direct link to Returning to Port")

Within Flow Port, navigate to the ‘Stake & Delegate’ page to see details about your existing staked and/or delegated tokens.
This will also show you the rewards you have earned for your staked/delegated tokens.

![Flow Port Staking pt. 1](/assets/images/port-stake-1-97173e61152cf4e4511a10e12e8a0ab6.png)

From here, you can do a few different things with your rewards:

* You can choose to **re-stake** them to the associated node.
* You can choose to **withdraw** them to your wallet.

## Re-staking[​](#re-staking "Direct link to Re-staking")

Flow Port will not automatically re-stake your rewards.
To re-stake your rewards, simply hover your cursor over the 3 dots next to the rewards field:

![Flow Port Re-Staking](/assets/images/port-stake-2-af524896a940797144a6fadda3804408.png)

Click on the Restake option. This will take you to a screen that looks like the below. Input the amount of rewards you want to re-stake, acknowledge the transaction inputs and click submit:

![Flow Port Re-Staking](/assets/images/port-stake-3-1710037da8e37cfeebc6593dfdb30e5a.png)

Once the transition is processed, you can reference the Stake & Delegate page again to see the pending stake now:

![Flow Port Re-Staking](/assets/images/port-stake-4-91a68814d26e24a5ad2e1d3df28a9eab.png)

## Withdraw your Rewards[​](#withdraw-your-rewards "Direct link to Withdraw your Rewards")

To withdraw your rewards, simply hover your cursor over the 3 dots next to the rewards field, and click on ‘Withdraw’.

![Flow Port Re-Staking](/assets/images/port-stake-5-af524896a940797144a6fadda3804408.png)

Input the amount that you want to withdraw to your wallet, acknowledge the transaction inputs and click submit:

![Flow Port Re-Staking](/assets/images/port-stake-6-11d724c6fc65a64fa87b99df83bfeaa5.png)

Once the transition is processed, you can now see the withdrawn rewards in your balance and you are now free to do other actions with them (send them to other accounts, delegate to a node, etc).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/flow-port/staking-guide.md)Last updated on **Jan 23, 2025** by **Brian Doyle**[PreviousFlow Port](/networks/flow-port)
###### Rate this page

😞😐😊

* [First Step](#first-step)
* [Stake a Node](#stake-a-node)
  + [Begin Staking](#begin-staking)
* [Delegating](#delegating)
  + [Enter a Node Operator ID](#enter-a-node-operator-id)
  + [Enter an amount](#enter-an-amount)
* [Returning to Port](#returning-to-port)
* [Re-staking](#re-staking)
* [Withdraw your Rewards](#withdraw-your-rewards)
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

