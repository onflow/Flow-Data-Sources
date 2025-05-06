# Source: https://developers.flow.com/networks/access-onchain-data/websockets-stream-api/unsubscribe-message

Unsubscribe request message format | Flow Developer Portal



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
* Unsubscribing from topic

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

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `subscription_id` | STRING | YES | Unique identifier of the subscription |
| `action` | STRING | YES | Action to perform. Must be `unsubscribe` to initiate a unsubscription |

[Edit this page](https://github.com/onflow/docs/tree/main/docs/networks/access-onchain-data/websockets-stream-api/unsubscribe-message.md)

Last updated on **May 5, 2025** by **Brian Doyle**

[Previous

Subscribing to topic](/networks/access-onchain-data/websockets-stream-api/subscribe-message)[Next

Supported topics](/networks/access-onchain-data/websockets-stream-api/supported-topics)

###### Rate this page

😞😐😊

Copy as Markdown

* [Example of unsubscribe request](#example-of-unsubscribe-request)
* [Example of successful response](#example-of-successful-response)
* [Example of error response](#example-of-error-response)
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