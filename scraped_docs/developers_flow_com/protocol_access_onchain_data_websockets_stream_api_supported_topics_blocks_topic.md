# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic

Blocks | Flow Developer Portal



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

* * [Accessing Data](/protocol/access-onchain-data)* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)* [Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)* Blocks

On this page

# Blocks

Provides full block information each time a new block appears on the blockchain.

## Example Request[​](#example-request "Direct link to Example Request")

Started from latest block:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "blocks",

_10

"arguments": {

_10

"block_status": "sealed"

_10

}

_10

}`

Started from block height `106192109`:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "blocks",

_10

"arguments": {

_10

"block_status": "sealed",

_10

"start_block_height": "106192109"

_10

}

_10

}`

Started from block id `83a8229cbe552f9b10160163394986dc7d99790ad3fedf7db4153d7d7863a3fa`:

`_10

{

_10

"subscription_id": "some-id",

_10

"action": "subscribe",

_10

"topic": "blocks",

_10

"arguments": {

_10

"block_status": "sealed",

_10

"start_block_id": "83a8229cbe552f9b10160163394986dc7d99790ad3fedf7db4153d7d7863a3fa"

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

`_104

{

_104

"subscription_id": "some-id",

_104

"topic": "blocks",

_104

"payload": {

_104

"header": {

_104

"id": "7a7bc4dc574f67f0dc01a6c96cfbabe73ead23f76ac8130e620996779a500925",

_104

"parent_id": "70b7f0a8c14e9f374eaf2f37da4dee7815c8639b3f9e67c301e84cf7fb51070c",

_104

"height": "106195712",

_104

"timestamp": "2025-03-11T12:25:00.450424315Z",

_104

"parent_voter_signature": "+GyIAAAAAAAAAACwobZq2GxrWxPUuNJwo5T1pFWvwcAF4/ue8e7j7eFTcRhtReHV+dWnneyGtJdpuaIagLCEfjHvfItzt3J/kXsbdEFeycVBeznP4LIHs0XWWkeRn+yds4NAM8jltmGGBnvgJ68="

_104

},

_104

"payload": {

_104

"collection_guarantees": [

_104

{

_104

"collection_id": "74d146368179f95a49531072cda799d1c0905523fd5a35c224eefbd92fab6a90",

_104

"signer_indices": "71d9de679d7ff457a0",

_104

"signature": ""

_104

},

_104

{

_104

"collection_id": "b4b40fa4bd5a98cc5f61924aa63a98c588f56447cec5bcdad538e0a855f1a0f3",

_104

"signer_indices": "710746ee7fd5f7a540",

_104

"signature": ""

_104

}

_104

],

_104

"block_seals": [

_104

{

_104

"block_id": "71418383aefda2df4da5fabb03d5ff0e8778f83783c5566c1110ba4a4d6e8de3",

_104

"result_id": "35f480934324280f6eebd6016b143bc28cecb8f71fcd8262153320ad93b16c61",

_104

"final_state": "\"0cc68829215fb9d69641537a317787b4ff805fe07d2f9ce12534b87d7d0f1335\"",

_104

"aggregated_approval_signatures": [

_104

{

_104

"verifier_signatures": [

_104

"rF6XjkIxY8lYD1vZvUycBtT+9DNY4d0U+p1q6WxiA8siYuFawrThkEIkLA3lYPjz"

_104

],

_104

"signer_ids": [

_104

"80a0eaa9eb5fd541b2abbd1b5ffa79f0ae9a36973322556ebd4bdd3e1d9fe4cd"

_104

]

_104

},

_104

{

_104

"verifier_signatures": [

_104

"j2Y94dVrZZT1qNuK1ZbTOxj5HfNZxmV5zVBA3uwTKrQ4FFQ6gN0na1nXhZDJN1po"

_104

],

_104

"signer_ids": [

_104

"e7e46cd698170b1f86bc9116dded0ac7df6ea0d86c41788c599fa77072059ea1"

_104

]

_104

},

_104

{

_104

"verifier_signatures": [

_104

"jp1/x2dr+LVS6Wl3ScaabsxD8745sb1kec3FUrj0SVXGEFnS7AUvG5RTKfsdF6m3"

_104

],

_104

"signer_ids": [

_104

"49c9f946170d5fb40c2af953b1534fae771905865b142ab6ac9685b8ba5b51c1"

_104

]

_104

},

_104

{

_104

"verifier_signatures": [

_104

"rogMdMXwEKJvMUxdHcFqseW9VGVmNzya51kI8yoc8M0kPfuRfENqfgY1NuQBVn3N"

_104

],

_104

"signer_ids": [

_104

"a1e6a5d9385d549f546803566747463e616e1d02ade2fcadba1b49c492ec8f29"

_104

]

_104

},

_104

{

_104

"verifier_signatures": [

_104

"seNSZjDBI7P4730jLcMWp1cq5XjSoSao9KLmrevSz2voQ+92Fcf7HqcSIpiF5CLi"

_104

],

_104

"signer_ids": [

_104

"8f8d77ba98d1606b19fce8f6d35908bfc29ea171c02879162f6755c05e0ca1ee"

_104

]

_104

}

_104

]

_104

},

_104

{

_104

"block_id": "9735518c51b170372fc3d04a6e360fef8b7f987fdb5f1e0f84d9a065d21a550c",

_104

"result_id": "328efa584043b0042b32b5e53c4d3c56988387440d94e9507d0a8d24a0f31e82",

_104

"final_state": "\"e1fb1b23de61b1cd83f22ffbcdd14a1844332d2e730e01df519c43ea3565bc3a\"",

_104

"aggregated_approval_signatures": [

_104

{

_104

"verifier_signatures": [

_104

"tchbJMwDd92Ui2UXnGPL20rEsTrkHQIYsYPZDAgR7O/9lRZh/u/5Y/7JN9+AiMwP"

_104

],

_104

"signer_ids": [

_104

"0a29d8eb288d9bb0a0a4f2f9ff180ec83617659998ce363814048ec1683083e0"

_104

]

_104

},

_104

{

_104

"verifier_signatures": [

_104

"q07CVWjMP1ocBmShFFZ9K5SYIwBitF8g5gajVkOJ0t+O8twzbtW7SjWPY8NIWKyp"

_104

],

_104

"signer_ids": [

_104

"446ae6d5ebdf6bc45aee29ed3b8da8dcf155afff87296401a3c0a28206121bcc"

_104

]

_104

}

_104

]

_104

}

_104

]

_104

},

_104

"_expandable": {},

_104

"_links": {

_104

"_self": "/v1/blocks/7a7bc4dc574f67f0dc01a6c96cfbabe73ead23f76ac8130e620996779a500925"

_104

},

_104

"block_status": "BLOCK_SEALED"

_104

}

_104

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/supported-topics/blocks_topic.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Block headers](/protocol/access-onchain-data/websockets-stream-api/supported-topics/block_headers_topic)[Next

Events](/protocol/access-onchain-data/websockets-stream-api/supported-topics/events_topic)

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