# Source: https://developers.flow.com/networks/access-onchain-data/websockets-stream-api/list-subscriptions-message

List subscriptions request message format | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)

  + [Access HTTP API ↗️](/networks/access-onchain-data/access-http-api)
  + [WebSockets Stream API](/networks/access-onchain-data/websockets-stream-api)

    - [Subscribing to topic](/networks/access-onchain-data/websockets-stream-api/subscribe-message)
    - [Unsubscribing from topic](/networks/access-onchain-data/websockets-stream-api/unsubscribe-message)
    - [Supported topics](/networks/access-onchain-data/websockets-stream-api/supported-topics)
    - [Listing subscriptions](/networks/access-onchain-data/websockets-stream-api/list-subscriptions-message)
    - [Connecting to WebSockets via Postman UI](/networks/access-onchain-data/websockets-stream-api/postman-example)
    - [Common errors](/networks/access-onchain-data/websockets-stream-api/common-errors)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Accessing Data](/networks/access-onchain-data)
* [WebSockets Stream API](/networks/access-onchain-data/websockets-stream-api)
* Listing subscriptions

On this page

# List subscriptions message format

List subscriptions requests must be sent as JSON in text frames, one request per frame.
This message is different from others as it doesn't require you to provide subscription ID.
Thus, the response for this message is different too.

### Example of request[​](#example-of-request "Direct link to Example of request")

`_10

{

_10

"action": "list_subscriptions"

_10

}`

### Example of response[​](#example-of-response "Direct link to Example of response")

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

"block_status": "finalized",

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

If there are no active subscriptions, `subscriptions` array will be empty.

### Request fields[​](#request-fields "Direct link to Request fields")

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `action` | STRING | YES | Action to perform. Must be `list_subscriptions` to initiate a list subscription request |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/access-onchain-data/websockets-stream-api/list-subscriptions-message.md)

Last updated on **May 6, 2025** by **Brian Doyle**

[Previous

Send and get transaction statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic)[Next

Connecting to WebSockets via Postman UI](/networks/access-onchain-data/websockets-stream-api/postman-example)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example of request](#example-of-request)
* [Example of response](#example-of-response)
* [Request fields](#request-fields)

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
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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