# Source: https://developers.flow.com/protocol/access-onchain-data/websockets-stream-api/common-errors

Common errors | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

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

* * [Accessing Data](/protocol/access-onchain-data)* [WebSockets Stream API](/protocol/access-onchain-data/websockets-stream-api)* Common errors

On this page

# Common errors

This document outlines the possible errors returned from the WebSocket API. Understanding these errors will help properly handle error cases in client implementation.

## Error Structure[​](#error-structure "Direct link to Error Structure")

All errors returned by the WebSocket API follow this structure:

`_10

{

_10

"subscriptionID": "string",

_10

"error": {

_10

"code": number,

_10

"message": "string"

_10

},

_10

"action": "string"

_10

}`

Where:

* `subscriptionID`: The ID of the subscription related to the error (if applicable)
* `error.code`: HTTP status code indicating the error type
* `error.message`: Human-readable description of the error
* `action`: The action that was being performed when the error occurred (`subscribe`, `unsubscribe`, or `list_subscription`)

### Message Format Errors[​](#message-format-errors "Direct link to Message Format Errors")

**Status Code:** 400 Bad Request

These errors occur when the server cannot parse or validate your incoming message.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Error Message Description When to Expect|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error reading message: ..."* The raw message could not be read from the WebSocket connection When sending malformed JSON or when the connection is disrupted|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error parsing message: ..."* The message was read but could not be processed When the message structure doesn't match the expected format|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error unmarshalling base message: ..."* The message JSON could not be processed into the expected format When required fields are missing or of incorrect type|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error unmarshalling subscribe message: ..."* The message JSON could not be processed into a subscribe request When sending a malformed subscribe request|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error unmarshalling unsubscribe message: ..."* The message JSON could not be processed into an unsubscribe request When sending a malformed unsubscribe request|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | *"error unmarshalling list subscriptions message: ..."* The message JSON could not be processed into a list subscriptions request When sending a malformed list subscriptions request|  |  |  | | --- | --- | --- | | *"unknown action type: ..."* The action specified in the message is not recognized When specifying an action other than `subscribe`, `unsubscribe`, or `list_subscription` | | | | | | | | | | | | | | | | | | | | | | | |

## Subscription-Related Errors[​](#subscription-related-errors "Direct link to Subscription-Related Errors")

### Subscribe Action Errors[​](#subscribe-action-errors "Direct link to Subscribe Action Errors")

**Action:** `subscribe`

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Error Message Status Code Description When to Expect|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error creating new subscription: maximum number of subscriptions reached"* 429 Too Many Requests The maximum number of active subscriptions per connection has been reached When trying to create more subscriptions than allowed by the server|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | *"error parsing subscription id: ..."* 400 Bad Request The provided subscription ID is invalid When providing a malformed subscription ID|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | *"subscription ID is already in use: ..."* 400 Bad Request The provided subscription ID is already being used When trying to reuse an existing subscription ID|  |  |  |  | | --- | --- | --- | --- | | *"error creating data provider: ..."* 400 Bad Request The subscription could not be created When providing an invalid topic or arguments for your subscription | | | | | | | | | | | | | | | | | | | |

### Unsubscribe Action Errors[​](#unsubscribe-action-errors "Direct link to Unsubscribe Action Errors")

**Action:** "unsubscribe"

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Error Message Status Code Description When to Expect|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | *"error parsing subscription id: ..."* 400 Bad Request The provided subscription ID is invalid When providing a malformed subscription ID|  |  |  |  | | --- | --- | --- | --- | | *"subscription not found"* 404 Not Found The specified subscription does not exist When trying to unsubscribe from a non-existent subscription | | | | | | | | | | | |

### Subscription Runtime Errors[​](#subscription-runtime-errors "Direct link to Subscription Runtime Errors")

**Action:** "subscribe"

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Error Message Status Code Description When to Expect|  |  |  |  | | --- | --- | --- | --- | | *"internal error: ..."* 500 Internal Server Error An error occurred while processing your subscription When there's an issue with the subscription after it was successfully created | | | | | | | |

## Error Handling Best Practices[​](#error-handling-best-practices "Direct link to Error Handling Best Practices")

1. **Always check for errors in responses**: Every response from the WebSocket API should be checked for the presence of an error object.
2. **Handle subscription limits**: Be prepared to handle the case where the maximum number of subscriptions has been reached.
3. **Log detailed error information**: Log the complete error object for debugging purposes.
4. **Validate messages before sending**: Ensure your messages conform to the expected format to avoid parsing errors.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/protocol/access-onchain-data/websockets-stream-api/common-errors.md)

Last updated on **Aug 22, 2025** by **Brian Doyle**

[Previous

Connecting to WebSockets via Postman UI](/protocol/access-onchain-data/websockets-stream-api/postman-example)[Next

Governance](/protocol/governance)

###### Rate this page

😞😐😊

Copy as Markdown

* [Error Structure](#error-structure)
  + [Message Format Errors](#message-format-errors)* [Subscription-Related Errors](#subscription-related-errors)
    + [Subscribe Action Errors](#subscribe-action-errors)+ [Unsubscribe Action Errors](#unsubscribe-action-errors)+ [Subscription Runtime Errors](#subscription-runtime-errors)* [Error Handling Best Practices](#error-handling-best-practices)

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