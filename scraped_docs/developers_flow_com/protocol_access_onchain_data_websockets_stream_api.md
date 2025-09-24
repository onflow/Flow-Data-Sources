# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api

Overview | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

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
* WebSockets Stream API

On this page

# Websockets Stream API

## Overview[​](#overview "Direct link to Overview")

The Stream API allows clients to receive real-time updates from the Flow blockchain via WebSocket connections. It
supports subscribing to various topics, such as blocks, events, and transactions, enabling low-latency access to live
data.

### Important Information[​](#important-information "Direct link to Important Information")

* **Endpoint**: The WebSocket server is available at:

  + Mainnet: `wss://rest-mainnet.onflow.org/v1/ws`
  + Testnet: `wss://rest-testnet.onflow.org/v1/ws`
* **Limits**:

  + Each connection supports up to 20 concurrent subscriptions. Exceeding this limit will result in an error.
  + Each subscription may provide up to 20 responses per second.
  + After 1 minute of inactivity (no data sent or received) the connection is closed.
* **Supported Topics**: See more details on [Supported Topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics) page.

  + [`block_digests`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_digests_topic)
  + [`block_headers`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic)
  + [`blocks`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic)
  + [`events`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/events_topic)
  + [`account_statuses`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic)
  + [`transaction_statuses`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic)
  + [`send_and_get_transaction_statuses`](/protocol/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic)
* **Notes**: Always handle errors gracefully and close unused subscriptions to maintain efficient connections.

---

## Setting Up a WebSocket Connection[​](#setting-up-a-websocket-connection "Direct link to Setting Up a WebSocket Connection")

Use any WebSocket client library to connect to the endpoint. Below is an example using JavaScript:

`_13

const ws = new WebSocket('wss://rest-mainnet.onflow.org/ws');

_13

_13

ws.onopen = () => {

_13

console.log('Connected to WebSocket server');

_13

};

_13

_13

ws.onclose = () => {

_13

console.log('Disconnected from WebSocket server');

_13

};

_13

_13

ws.onerror = (error) => {

_13

console.error('WebSocket error:', error);

_13

};`

---

## Subscribing to Topics[​](#subscribing-to-topics "Direct link to Subscribing to Topics")

To receive data from a specific topic, send a subscription request in JSON format over the WebSocket connection.

### Request Format[​](#request-format "Direct link to Request Format")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"action": "subscribe",

_10

"topic": "blocks",

_10

"arguments": {

_10

"block_status": "sealed",

_10

"start_block_height": "123456789"

_10

}

_10

}`

* **`subscription_id`**(optional): A unique identifier for the subscription (a string with maximum length constraint of 20 characters). If omitted, the server generates one.
* **`action`**: The action to perform. Supported actions include: `subscribe`, `unsubscribe`, `list_subscriptions`.
* **`topic`**: The topic to subscribe to. See the supported topics in the Overview.
* **`arguments`**: Additional topic specific arguments for subscriptions, such as `start_block_height`, `start_block_id`, and others. See more details about arguments for each topic on [Supported Topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics) page.

### Successful Response Format[​](#successful-response-format "Direct link to Successful Response Format")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"action": "subscribe"

_10

}`

---

## Unsubscribing from Topics[​](#unsubscribing-from-topics "Direct link to Unsubscribing from Topics")

To stop receiving data from a specific topic, send an unsubscribe request.

### Request Format[​](#request-format-1 "Direct link to Request Format")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"action": "unsubscribe"

_10

}`

### Successful Response Format[​](#successful-response-format-1 "Direct link to Successful Response Format")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"action": "unsubscribe"

_10

}`

---

## Listing Active Subscriptions[​](#listing-active-subscriptions "Direct link to Listing Active Subscriptions")

You can retrieve a list of all active subscriptions for the current WebSocket connection.

### Request Format[​](#request-format-2 "Direct link to Request Format")

`_10

{

_10

"action": "list_subscriptions"

_10

}`

### Successful Response Format[​](#successful-response-format-2 "Direct link to Successful Response Format")

`_17

{

_17

"subscriptions": [

_17

{

_17

"subscription_id": "some-id-1",

_17

"topic": "blocks",

_17

"arguments": {

_17

"block_status": "sealed",

_17

"start_block_height": "123456789"

_17

}

_17

},

_17

{

_17

"subscription_id": "some-id-2",

_17

"topic": "events",

_17

"arguments": {}

_17

}

_17

]

_17

}`

---

## Errors Example[​](#errors-example "Direct link to Errors Example")

If a request is invalid or cannot be processed, the server responds with an error message.

### OK Response[​](#ok-response "Direct link to OK Response")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"topic": "block_digests",

_10

"payload": {

_10

"id": "0x1234...",

_10

"height:": "123456789",

_10

"timestamp": "2025-01-02T10:00:00Z"

_10

}

_10

}`

### Error Response[​](#error-response "Direct link to Error Response")

`_10

{

_10

"subscription_id": "some-id-42",

_10

"error": {

_10

"code": 500,

_10

"message": "Access Node failed"

_10

}

_10

}`

### Common Error Codes[​](#common-error-codes "Direct link to Common Error Codes")

* **400**: Invalid message format or arguments
* **404**: Subscription not found
* **500**: Internal server error

### Asynchronous environments[​](#asynchronous-environments "Direct link to Asynchronous environments")

If you're working in an asynchronous environment, the Streaming API ensures **first-in first-out** message processing,
so responses will be returned in the same order the requests were received over the connection.
You can leverage this feature to simplify your code and maintain consistency.

Additionally, you can specify a custom `subscription_id` in the subscribe request to easily identify the correct response. It must not be an empty string and must follow a maximum length constraint of 20 characters.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/index.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Access HTTP API ↗️](/protocol/access-onchain-data/access-http-api)[Next

Subscribing to topic](/protocol/access-onchain-data/websockets-stream-api/subscribe-message)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)
  + [Important Information](#important-information)
* [Setting Up a WebSocket Connection](#setting-up-a-websocket-connection)
* [Subscribing to Topics](#subscribing-to-topics)
  + [Request Format](#request-format)
  + [Successful Response Format](#successful-response-format)
* [Unsubscribing from Topics](#unsubscribing-from-topics)
  + [Request Format](#request-format-1)
  + [Successful Response Format](#successful-response-format-1)
* [Listing Active Subscriptions](#listing-active-subscriptions)
  + [Request Format](#request-format-2)
  + [Successful Response Format](#successful-response-format-2)
* [Errors Example](#errors-example)
  + [OK Response](#ok-response)
  + [Error Response](#error-response)
  + [Common Error Codes](#common-error-codes)
  + [Asynchronous environments](#asynchronous-environments)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
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