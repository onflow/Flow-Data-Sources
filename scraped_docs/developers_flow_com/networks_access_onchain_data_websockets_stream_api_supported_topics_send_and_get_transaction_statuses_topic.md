# Source: https://developers.flow.com/networks/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic

Send and get transaction statuses | Flow Developer Portal



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
* Send and get transaction statuses

On this page

# Send and get transaction statuses

Sends a transaction and provides updates on its status changes.

## Example Request[​](#example-request "Direct link to Example Request")

`_25

{

_25

"subscription_id": "some-id-7",

_25

"action": "subscribe",

_25

"topic": "send_and_get_transaction_statuses"

_25

"arguments": {

_25

"arguments": [],

_25

"authorizers": ["dba05362251g43g4"],

_25

"envelope_signatures": [

_25

{

_25

"address": "dba05362251g43g4",

_25

"key_index": "0",

_25

"signature": "PJPVEOCtPKubTEpPqd4zrrSXo1RhpABAMDuzIchgBje8gyh04XuWY4f/tu+c0llDhOU/5sQBokeOTdygaS6eTQ=="

_25

}

_25

],

_25

"gas_limit": "1000",

_25

"payer": "dba05362251g43g4",

_25

"proposal_key": {

_25

"address": "dba05362251g43g4",

_25

"key_index": "0",

_25

"sequence_number": "0"

_25

},

_25

"reference_block_id": "817d7c1d2c13a4bd37c182747a4116b45cd175c0ba4878071c33f0f278b37dd7",

_25

"script": "CgkJCXRyYW5zYWN0aW9uIHsKCQkJCXByZXBhcmUoYWNjOiAmQWNjb3VudCkge30KCQkJCWV4ZWN1dGUgewoJCQkJCWxvZygidGVzdCIpCgkJCQl9CgkJCX0KCQk="

_25

}

_25

}`

| Name | Type | REQUIRED | Description |
| --- | --- | --- | --- |
| `script` | STRING | YES | Base64-encoded content of the Cadence script. |
| `arguments` | LIST | YES | A list of arguments, each encoded as Base64. |
| `reference_block_id` | STRING | YES | BlockID for the transaction's reference block |
| `gas_limit` | STRING | YES | The limit on the amount of computation a transaction can perform. |
| `payer` | STRING | YES | The 8-byte address of an account. |
| `proposal_key` | OBJECT | YES | A required object representing the proposal key. |
| `authorizers` | LIST | YES | A list of authorizers, each represented as a hexadecimal-encoded address. |
| `payload_signatures` | LIST | NO | A list of Base64-encoded signatures. |
| `envelope_signatures` | LIST | YES | A list of Base64-encoded signatures. |

## Example Response[​](#example-response "Direct link to Example Response")

`_20

{

_20

"subscription_id": "some-id",

_20

"topic": "send_and_get_transaction_statuses",

_20

"payload": {

_20

"transaction_result": {

_20

"block_id": "7ad167602487665db095f7cb0b95139e5dcaf3ad2479ee4d14cade35b7d4bbdc",

_20

"collection_id": "d0855ed45c16be2831ab9892ec8a9ddfd10a0e01e683466971cfd87c759bf7d1",

_20

"execution": "Failure",

_20

"status": "Sealed",

_20

"status_code": 1,

_20

"error_message": "[Error Code: 1009] error caused by: 1 error occurred:\n\t* transaction verification failed: [Error Code: 1006] invalid proposal key: public key 0 on account dba05362251g43g4 does not have a valid signature: [Error Code: 1009] invalid envelope key: public key 0 on account dba05362251g43g4 does not have a valid signature: signature is not valid\n\n",

_20

"computation_used": "0",

_20

"events": [],

_20

"_links": {

_20

"_self": "/v1/transaction_results/92014de98466a6304ecd821c95ee2612e248c22419d243e6e3ff4d138dffde04"

_20

}

_20

},

_20

"message_index": 3

_20

}

_20

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic.md)

Last updated on **May 9, 2025** by **Brian Doyle**

[Previous

Transaction statuses](/networks/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic)[Next

Listing subscriptions](/networks/access-onchain-data/websockets-stream-api/list-subscriptions-message)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Request](#example-request)
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
* [Core Contracts & Standards](/build/core-contracts)
* [EVM](/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/networks/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/networks/node-ops)
* [Spork Information](/networks/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.