# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic

Block headers | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Flow Networks](/protocol/flow-networks)

  * [Networks](/protocol)* [Flow Network Architecture](/protocol/network-architecture)

      * [Staking and Epochs](/protocol/staking)

        * [Node Ops](/protocol/node-ops)

          * [Accessing Data](/protocol/access-onchain-data)

            + [Access HTTP API ↗️](/protocol/access-onchain-data/access-http-api)+ [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)

                - [Subscribing to topic](/protocol/access-onchain-data/websockets-stream-api/subscribe-message)- [Unsubscribing from topic](/protocol/access-onchain-data/websockets-stream-api/unsubscribe-message)- [Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)

                      * [Block digests](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_digests_topic)* [Block headers](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic)* [Blocks](/protocol/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic)* [Events](/protocol/access-onchain-data/websockets-stream-api/supported-topics/events_topic)* [Account statuses](/protocol/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic)* [Transaction statuses](/protocol/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic)* [Send and get transaction statuses](/protocol/access-onchain-data/websockets-stream-api/supported-topics/send_and_get_transaction_statuses_topic)- [Listing subscriptions](/protocol/access-onchain-data/websockets-stream-api/list-subscriptions-message)- [Connecting to WebSockets via Postman UI](/protocol/access-onchain-data/websockets-stream-api/postman-example)- [Common errors](/protocol/access-onchain-data/websockets-stream-api/common-errors)* [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Accessing Data](/protocol/access-onchain-data)* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)* [Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)* Block headers

On this page

# Block headers

Provides block headers without the payload, each time a new block appears on the blockchain.

## Example Request[​](#example-request "Direct link to Example Request")

Started from latest block:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "block_headers",

_10

"arguments": {

_10

"block_status": "finalized"

_10

}

_10

}`

Started from block height `106195326`:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "block_headers",

_10

"arguments": {

_10

"block_status": "finalized",

_10

"start_block_height": "106195326"

_10

}

_10

}`

Started from block id `cb27b014fa105a1e0e64d56cfbe2d7e140f4adf32938e38c3459592d01a72e91`:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "block_headers",

_10

"arguments": {

_10

"block_status": "finalized",

_10

"start_block_id": "cb27b014fa105a1e0e64d56cfbe2d7e140f4adf32938e38c3459592d01a72e91"

_10

}

_10

}`

### Request Arguments[​](#request-arguments "Direct link to Request Arguments")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `block_status` STRING YES The status of blocks to subscribe to. Supported values are: `sealed`, `finalized`.| `start_block_id` STRING NO The ID of the block from which the subscription starts. If this argument is set, it is **not** possible to set `start_block_height`.| `start_block_height` STRING NO The height of the block from which the subscription starts. If this argument is set, it is **not** possible to set `start_block_id` | | | | | | | | | | | | | | | |

If neither `start_block_id` nor `start_block_height` is set, the subscription will start from the latest block based on its status.

## Example Response[​](#example-response "Direct link to Example Response")

`_11

{

_11

"subscription_id": "some-id",

_11

"topic": "block_headers",

_11

"payload": {

_11

"id": "5cd0b1d0a0f0017c25647a6e2454a59aafa90682f2329449a610e19673ba07de",

_11

"parent_id": "72ecd7cf6b18488b3597e677c5fa620d2dfad981fdd81b5cdb1851490b0cff56",

_11

"height": "106195236",

_11

"timestamp": "2025-03-11T12:18:39.702990376Z",

_11

"parent_voter_signature": "+GyIAAAAAAAAAACwsabEiORFcP/ru95TABxwxXsxnUtJNoUbGB1xKKNtpR/LNUqDL5TyIQjL3xBl5KtKgLCFde8F5DHtUSGYSQUzaGhv+IoQgh1wgbXlY/soY5T30/HwmrucwD925EKOJAQUj7s="

_11

}

_11

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Block digests](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_digests_topic)[Next

Blocks](/protocol/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example Request](#example-request)
  + [Request Arguments](#request-arguments)* [Example Response](#example-response)

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