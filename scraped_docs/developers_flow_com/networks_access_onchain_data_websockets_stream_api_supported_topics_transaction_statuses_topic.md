# Source: https://developers.flow.com/networks/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic

Transaction statuses | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/networks/flow-networks)
* [Networks](/networks)
* [Flow's Network Architecture](/networks/network-architecture)
* [Staking and Epochs](/networks/staking)
* [Node Ops](/networks/node-ops)
* [Accessing Data](/networks/access-onchain-data)

  + [Access HTTP API ↗️](/networks/access-onchain-data/access-http-api)
  + [WebSockets Stream API](/networks/access-onchain-data/websockets-stream-api)

    - [Subscribing to topic](/networks/access-onchain-data/websockets-stream-api/subscribe-message)
    - [Unsubscribing from topic](/networks/access-onchain-data/websockets-stream-api/unsubscribe-message)
    - [Supported topics](/networks/access-onchain-data/websockets-stream-api/supported-topics)

      * [Block digests](/networks/access-onchain-data/websockets-stream-api/supported-topics/block_digests_topic)
      * [Block headers](/networks/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic)
      * [Blocks](/networks/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic)
      * [Events](/networks/access-onchain-data/websockets-stream-api/supported-topics/events_topic)
      * [Account statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic)
      * [Transaction statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic)
      * [Send and get transaction statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic)
    - [Listing subscriptions](/networks/access-onchain-data/websockets-stream-api/list-subscriptions-message)
    - [Connecting to WebSockets via Postman UI](/networks/access-onchain-data/websockets-stream-api/postman-example)
    - [Common errors](/networks/access-onchain-data/websockets-stream-api/common-errors)
* [Governance](/networks/governance)
* [Flow Port](/networks/flow-port)

* [Accessing Data](/networks/access-onchain-data)
* [WebSockets Stream API](/networks/access-onchain-data/websockets-stream-api)
* [Supported topics](/networks/access-onchain-data/websockets-stream-api/supported-topics)
* Transaction statuses

On this page

# Transaction statuses

Provides updates on transaction status changes for already sent transactions.

## Example Request[​](#example-request "Direct link to Example Request")

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "transaction_statuses",

_10

"arguments": {

_10

"tx_id": "fe3784095bc194dca02e4b14e7e6a1e0519d10b7bc907453e5b5dc276259a106"

_10

}

_10

}`

### Request Arguments[​](#request-arguments "Direct link to Request Arguments")

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `tx_id` | STRING | YES | The ID of the transaction to monitor for status changes. |

## Example Response[​](#example-response "Direct link to Example Response")

`_36

{

_36

"subscription_id": "some-id",

_36

"topic": "transaction_statuses",

_36

"payload": {

_36

"transaction_result": {

_36

"block_id": "b668e472c404e471cba8bab5246ca98f90d8492e80c81aae4cccbfae6e734aad",

_36

"collection_id": "efdcbf3b2b02b20cdfa7f2669034da05e44232ea68e41d3ed14756472081f9b9",

_36

"execution": "Success",

_36

"status": "Sealed",

_36

"status_code": 0,

_36

"error_message": "",

_36

"computation_used": "0",

_36

"events": [

_36

{

_36

"type": "A.0b2a3299cc857e29.TopShot.Withdraw",

_36

"transaction_id": "fe3784095bc194dca02e4b14e7e6a1e0519d10b7bc907453e5b5dc276259a106",

_36

"transaction_index": "4",

_36

"event_index": "0",

_36

"payload": "eyJ2YWx1ZSI6eyJpZCI6IkEuMGIyYTMyOTljYzg1N2UyOS5Ub3BTaG90LldpdGhkcmF3IiwiZmllbGRzIjpbeyJ2YWx1ZSI6eyJ2YWx1ZSI6IjQwOTQ3MzE4IiwidHlwZSI6IlVJbnQ2NCJ9LCJuYW1lIjoiaWQifSx7InZhbHVlIjp7InZhbHVlIjp7InZhbHVlIjoiMHg2N2Q5OTk5MWMxMzRlODQ4IiwidHlwZSI6IkFkZHJlc3MifSwidHlwZSI6Ik9wdGlvbmFsIn0sIm5hbWUiOiJmcm9tIn1dfSwidHlwZSI6IkV2ZW50In0K"

_36

},

_36

// Full response is cut down due to its large size; see `_links` for the full response. ...

_36

{

_36

"type": "A.f919ee77447b7497.FlowFees.FeesDeducted",

_36

"transaction_id": "fe3784095bc194dca02e4b14e7e6a1e0519d10b7bc907453e5b5dc276259a106",

_36

"transaction_index": "4",

_36

"event_index": "22",

_36

"payload": "eyJ2YWx1ZSI6eyJpZCI6IkEuZjkxOWVlNzc0NDdiNzQ5Ny5GbG93RmVlcy5GZWVzRGVkdWN0ZWQiLCJmaWVsZHMiOlt7InZhbHVlIjp7InZhbHVlIjoiMC4wMDAwNDc5OCIsInR5cGUiOiJVRml4NjQifSwibmFtZSI6ImFtb3VudCJ9LHsidmFsdWUiOnsidmFsdWUiOiIxLjAwMDAwMDAwIiwidHlwZSI6IlVGaXg2NCJ9LCJuYW1lIjoiaW5jbHVzaW9uRWZmb3J0In0seyJ2YWx1ZSI6eyJ2YWx1ZSI6IjAuMDAwMDAxODgiLCJ0eXBlIjoiVUZpeDY0In0sIm5hbWUiOiJleGVjdXRpb25FZmZvcnQifV19LCJ0eXBlIjoiRXZlbnQifQo="

_36

}

_36

],

_36

"_links": {

_36

"_self": "/v1/transaction_results/fe3784095bc194dca02e4b14e7e6a1e0519d10b7bc907453e5b5dc276259a106"

_36

}

_36

},

_36

"message_index": 3

_36

}

_36

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic.md)

Last updated on **Apr 21, 2025** by **Illia**

[Previous

Account statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic)[Next

Send and get transaction statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic)

###### Rate this page

😞😐😊

* [Example Request](#example-request)
  + [Request Arguments](#request-arguments)
* [Example Response](#example-response)

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