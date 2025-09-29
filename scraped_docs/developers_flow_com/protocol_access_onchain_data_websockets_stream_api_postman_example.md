# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/postman-example

Connecting to WebSockets via Postman UI | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)
* [Networks](/protocol)
* [Flow Network Architecture](/protocol/network-architecture)
* [Staking and Epochs](/protocol/staking)
* [Node Ops](/protocol/node-ops)
* [Accessing Data](/protocol/access-onchain-data)

  + [Access HTTP API ↗️](/protocol/access-onchain-data/access-http-api)
  + [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)

    - [Subscribing to topic](/protocol/access-onchain-data/websockets-stream-api/subscribe-message)
    - [Unsubscribing from topic](/protocol/access-onchain-data/websockets-stream-api/unsubscribe-message)
    - [Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)
    - [Listing subscriptions](/protocol/access-onchain-data/websockets-stream-api/list-subscriptions-message)
    - [Connecting to WebSockets via Postman UI](/protocol/access-onchain-data/websockets-stream-api/postman-example)
    - [Common errors](/protocol/access-onchain-data/websockets-stream-api/common-errors)
* [Governance](/protocol/governance)
* [Flow Port](/protocol/flow-port)

* [Accessing Data](/protocol/access-onchain-data)
* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)
* Connecting to WebSockets via Postman UI

On this page

# Connecting to WebSockets via Postman UI

This tutorial will guide you through connecting to a WebSocket using Postman and sending a subscription message.

## Step 1: Open Postman[​](#step-1-open-postman "Direct link to Step 1: Open Postman")

Ensure you have Postman installed and opened on your system. If you don’t have it yet, download it from [Postman’s official website](https://www.postman.com/downloads/).

## Step 2: Create a New WebSocket Request[​](#step-2-create-a-new-websocket-request "Direct link to Step 2: Create a New WebSocket Request")

1. In Postman, click on **File** > **New...** > **WebSocket**.
   ![pe_1](/assets/images/pe_1-bb4b1259cbf965170fd298540cacdba4.png)
2. Enter the WebSocket URL in **Enter URL** field : `wss://rest-mainnet.onflow.org/v1/ws` or `wss://rest-testnet.onflow.org/v1/ws`
3. Click **Connect** button to establish the WebSocket connection.
   ![pe_2](/assets/images/pe_2-fad2825d44ebb56f85bf187829350269.png)

## Step 3: Send a Subscription Message[​](#step-3-send-a-subscription-message "Direct link to Step 3: Send a Subscription Message")

1. Once connected, go to the **Messages** tab.
2. Enter the JSON message into the text box. In this example the [digests block subscription](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_digests_topic) will be established. For other available topics check [Supported topics page](/protocol/access-onchain-data/websockets-stream-api/supported-topics).
3. Click **Send** to subscribe to the WebSocket topic.
   ![pe_3](/assets/images/pe_3-f5c00c8fa002b7acc55ff5b89e3ab28b.png)

## Step 4: View Responses[​](#step-4-view-responses "Direct link to Step 4: View Responses")

* After sending the message, you should start receiving responses in the **Response** bottom tab.
* Each message received from the server will be displayed in real-time.

![pe_4](/assets/images/pe_4-1a1ba77a604e82be976534b0bddf4061.png)

## Step 5: Disconnect[​](#step-5-disconnect "Direct link to Step 5: Disconnect")

* When you are done, click **Disconnect** to close the WebSocket connection.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

* Ensure WebSocket URL is correct and active.
* In case of an error validate your JSON message for any syntax errors before sending and check correctness of all arguments on [Supported topics page](/protocol/access-onchain-data/websockets-stream-api/supported-topics).

Congratulations! You have successfully connected to a WebSocket server using Postman and sent a subscription message.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/postman-example.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Listing subscriptions](/protocol/access-onchain-data/websockets-stream-api/list-subscriptions-message)[Next

Common errors](/protocol/access-onchain-data/websockets-stream-api/common-errors)

###### Rate this page

😞😐😊

Copy as Markdown

* [Step 1: Open Postman](#step-1-open-postman)
* [Step 2: Create a New WebSocket Request](#step-2-create-a-new-websocket-request)
* [Step 3: Send a Subscription Message](#step-3-send-a-subscription-message)
* [Step 4: View Responses](#step-4-view-responses)
* [Step 5: Disconnect](#step-5-disconnect)
* [Troubleshooting](#troubleshooting)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.