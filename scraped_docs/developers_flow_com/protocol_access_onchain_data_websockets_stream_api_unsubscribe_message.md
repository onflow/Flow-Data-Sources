# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/unsubscribe-message

Unsubscribe request message format | Flow Developer Portal



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

                      - [Listing subscriptions](/protocol/access-onchain-data/websockets-stream-api/list-subscriptions-message)- [Connecting to WebSockets via Postman UI](/protocol/access-onchain-data/websockets-stream-api/postman-example)- [Common errors](/protocol/access-onchain-data/websockets-stream-api/common-errors)* [Governance](/protocol/governance)* [Flow Port](/protocol/flow-port)

* * [Accessing Data](/protocol/access-onchain-data)* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)* Unsubscribing from topic

On this page

# Unsubscribe message format

Unsubscribe requests must be sent as JSON in text frames, one request per frame.

### Example of unsubscribe request[​](#example-of-unsubscribe-request "Direct link to Example of unsubscribe request")

`_10

{

_10

"subscription_id": "some-id-1",

_10

"action": "unsubscribe"

_10

}`

### Example of successful response[​](#example-of-successful-response "Direct link to Example of successful response")

`_10

{

_10

"subscription_id": "some-id-1",

_10

"action": "unsubscribe"

_10

}`

### Example of error response[​](#example-of-error-response "Direct link to Example of error response")

`_10

{

_10

"error": {

_10

"code": 404,

_10

"message": "subscription not found"

_10

}

_10

}`

### Request fields[​](#request-fields "Direct link to Request fields")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Name Type Required Description|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `subscription_id` STRING YES Unique identifier of the subscription|  |  |  |  | | --- | --- | --- | --- | | `action` STRING YES Action to perform. Must be `unsubscribe` to initiate a unsubscription | | | | | | | | | | | |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/unsubscribe-message.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Subscribing to topic](/protocol/access-onchain-data/websockets-stream-api/subscribe-message)[Next

Supported topics](/protocol/access-onchain-data/websockets-stream-api/supported-topics)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example of unsubscribe request](#example-of-unsubscribe-request)* [Example of successful response](#example-of-successful-response)* [Example of error response](#example-of-error-response)* [Request fields](#request-fields)

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