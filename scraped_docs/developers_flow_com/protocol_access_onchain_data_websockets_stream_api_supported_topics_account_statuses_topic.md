# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic

Account statuses | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

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

* * [Accessing Data](/protocol/access-onchain-data)* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)* [Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)* Account statuses

On this page

# Account statuses

Provides accounts statuses updates. The response can be configured using additional arguments to filter and retrieve only filtered account statuses instead of all core account events.

## Example Request[​](#example-request "Direct link to Example Request")

Started from latest block for event types `flow.AccountKeyAdded` and `flow.AccountKeyRemoved`:

`_11

{

_11

"subscription_id": "some-id",

_11

"action": "subscribe",

_11

"topic": "account_statuses",

_11

"arguments": {

_11

"event_types": [

_11

"flow.AccountKeyAdded",

_11

"flow.AccountKeyRemoved"

_11

]

_11

}

_11

}`

Started from block height `106219488` for all accounts events with heartbeat interval equal 10 blocks:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "account_statuses",

_10

"arguments": {

_10

"start_block_height": "106219488",

_10

"heartbeat_interval": "10"

_10

}

_10

}`

Started from block id `f1ba2fb02daf02c7a213b6b0f75774aaf54180ae67fb62bdf22ae37295fe1120` for account addresses `0xe544175ee0461c4b` and `2d4c3caffbeab845` with heartbeat interval equal 5 blocks:

`_13

{

_13

"subscription_id": "some-id",

_13

"action": "subscribe",

_13

"topic": "account_statuses",

_13

"arguments": {

_13

"start_block_id": "f1ba2fb02daf02c7a213b6b0f75774aaf54180ae67fb62bdf22ae37295fe1120",

_13

"heartbeat_interval": "5",

_13

"account_addresses": [

_13

"0xe544175ee0461c4b",

_13

"2d4c3caffbeab845"

_13

]

_13

}

_13

}`

### Request Arguments[​](#request-arguments "Direct link to Request Arguments")

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `start_block_id` STRING NO The ID of the block from which the subscription starts. If this argument is set, it is **not** possible to set `start_block_height`.| `start_block_height` STRING NO The height of the block from which the subscription starts. If this argument is set, it is **not** possible to set `start_block_id`| `heartbeat_interval` STRING NO Maximum number of blocks between messages after which a response with no events is returned. This helps the client track progress for sparse event filters.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `event_types` LIST NO A comma-separated list of event types to include. See the list of possible event types value [below](#the-list-of-possible-core-event-types).| `account_addresses` LIST NO A comma-separated list of addresses who's events should be included. The format could be `"0xe544175ee0461c4b"` or `"e544175ee0461c4b"`. | | | | | | | | | | | | | | | | | | | | | | | |

If neither `start_block_id` nor `start_block_height` is set, the subscription will start from the latest block based on its status.

#### The list of possible core event types[​](#the-list-of-possible-core-event-types "Direct link to The list of possible core event types")

* `flow.AccountCreated` emitted when a new account gets created.
* `flow.AccountKeyAdded` emitted when a key gets added to an account.
* `flow.AccountKeyRemoved` emitted when a key gets removed from an account.
* `flow.AccountContractAdded` emitted when a contract gets deployed to an account.
* `flow.AccountContractUpdated` emitted when a contract gets updated on an account.
* `flow.AccountContractRemoved` emitted when a contract gets removed from an account.
* `flow.InboxValuePublished` emitted when a Capability is published from an account.
* `flow.InboxValueUnpublished` emitted when a Capability is unpublished from an account.
* `flow.InboxValueClaimed` emitted when a Capability is claimed by an account.

## Example Response[​](#example-response "Direct link to Example Response")

`_20

{

_20

"subscription_id": "some-id",

_20

"topic": "account_statuses",

_20

"payload": {

_20

"block_id": "ab20d1a3574177e69636eea73e7db4e74cffb2754cb14ca0bf18c2b96e8b68b9",

_20

"height": "106219247",

_20

"account_events": {

_20

"0x37d2b958f6970c48": [

_20

{

_20

"type": "flow.AccountKeyAdded",

_20

"transaction_id": "19af79cf2fe081491f1e7b0bf490869c8baece742c6606b4a51383515131b5f0",

_20

"transaction_index": "1",

_20

"event_index": "14",

_20

"payload": "2IGChNigg0BpUHVibGljS2V5goJpcHVibGljS2V52IvYiQyCcnNpZ25hdHVyZUFsZ29yaXRobdiIQQLYpINBAW1IYXNoQWxnb3JpdGhtgYJocmF3VmFsdWXYiQzYpINBAnJTaWduYXR1cmVBbGdvcml0aG2BgmhyYXdWYWx1ZdiJDNiig0EDdGZsb3cuQWNjb3VudEtleUFkZGVkhYJnYWRkcmVzc9iJA4JpcHVibGljS2V52IhAgmZ3ZWlnaHTYiReCbWhhc2hBbGdvcml0aG3YiEEBgmhrZXlJbmRleNiJBILYiEEDhUg30rlY9pcMSIKYQBjBGFoYKhg8GLoAGEIHGHAYYREYoBirGKsYiRhrGDAY3xiTGLkUGJYYdRixGOwYjxjNGCkAExhRGCoY/xgfEBh/GJ0YtxjBGH8YLxiqGD4JGKIY6xgmDhiUGDEYqRhvGCYY8hitGMEWGKwY6RiEGF4YQRhBGKGBAhsAAAAXSHboAIEBwkA="

_20

}

_20

]

_20

},

_20

"message_index": 4

_20

}

_20

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/supported-topics/account_statuses_topic.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Events](/protocol/access-onchain-data/websockets-stream-api/supported-topics/events_topic)[Next

Transaction statuses](/protocol/access-onchain-data/websockets-stream-api/supported-topics/transaction_statuses_topic)

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

Copyright © 2026 Flow Foundation. All Rights Reserved.