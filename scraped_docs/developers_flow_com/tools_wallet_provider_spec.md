# Source: https://developers.flow.com/tools/wallet-provider-spec

Wallet Provider Spec | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Client Tools](/tools/clients)
* [Tools](/tools)
* [Error Codes](/tools/error-codes)
* [Flow CLI](/tools/flow-cli)
* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Wallet Provider Spec](/tools/wallet-provider-spec)

  + [Authorization Function](/tools/wallet-provider-spec/authorization-function)
  + [Introduction](/tools/wallet-provider-spec/custodial)
  + [Provable Authn](/tools/wallet-provider-spec/provable-authn)
  + [User Signature](/tools/wallet-provider-spec/user-signature)

* Wallet Provider Spec

On this page

# Wallet Provider Spec

## Status[​](#status "Direct link to Status")

* **Last Updated:** June 20th 2022
* **Stable:** Yes
* **Risk of Breaking Change:** Medium
* **Compatibility:** `>= @onflow/fcl@1.0.0-alpha.0`

## Definitions[​](#definitions "Direct link to Definitions")

This document is written with the perspective that *you* who are reading this right now are an FCL Wallet Developer. All references to *you* in this doc are done with this perspective in mind.

# Overview

Flow Client Library (FCL) approaches the idea of blockchain wallets on Flow in a different way than how wallets may be supported on other blockchains. For example, with FCL, a wallet is not necessarily limited to being a browser extension or even a native application on a users device. FCL offers wallet developers the flexibility and freedom to build many different types of applications. Since wallet applications can take on many forms, we needed to create a way for these varying applications to be able to communicate and work together.

FCL acts in many ways as a protocol to facilitate communication and configuration between the different parties involved in a blockchain application. An *Application* can use FCL to *authenticate* users, and request *authorizations* for transactions, as well as mutate and query the *Blockchain*. An application using FCL offers its *Users* a way to connect and select any number of Wallet Providers and their Wallet Services. A selected *Wallet* provides an Application's instance of FCL with configuration information about itself and its Wallet Services, allowing the *User* and *Application* to interact with them.

In the following paragraphs we'll explore ways in which you can integrate with FCL by providing implementations of various FCL services.

The following services will be covered:

* Authentication (Authn) Service
* Authorization (Authz) Service
* User Signature Service
* Pre-Authz Service

# Service Methods

FCL Services are your way as a Wallet Provider of configuring FCL with information about what your wallet can do. FCL uses what it calls `Service Methods` to perform your supported FCL services. Service Methods are the ways FCL can talk to your wallet. Your wallet gets to decide which of these service methods each of your supported services use to communicate with you.

Sometimes services just configure FCL and that's it. An example of this can be seen with the Authentication Service and the OpenID Service.
With those two services you are simply telling FCL "here is a bunch of info about the current user". (You will see that those two services both have a `method: "DATA"` field in them.
Currently these are the only two cases that can be a data service.)

Other services can be a little more complex. For example, they might require a back and forth communication between FCL and the Service in question.
Ultimately we want to do this back and forth via a secure back-channel (https requests to servers), **but in some situations that isn't a viable option, so there is also a front-channel option**.
Where possible, you should aim to provide a back-channel support for services, and only fall back to a front-channel if absolutely necessary.

Back-channel communications use `method: "HTTP/POST"`, while front-channel communications use `method: "IFRAME/RPC"`, `method: "POP/RPC"`, `method: "TAB/RPC` and `method: "EXT/RPC"`.

| Service Method | Front | Back |
| --- | --- | --- |
| HTTP/POST | ⛔ | ✅ |
| IFRAME/RPC | ✅ | ⛔ |
| POP/RPC | ✅ | ⛔ |
| TAB/RPC | ✅ | ⛔ |
| EXT/RPC | ✅ | ⛔ |

It's important to note that regardless of the method of communication, the data that is sent back and forth between the parties involved is the same.

# Protocol schema definitions

In this section we define the schema of objects used in the protocol. While they are JavaScript objects, only features supported by JSON should be used. (Meaning that conversion of an object to and from JSON should not result in any loss.)

For the schema definition language we choose TypeScript, so that the schema closely resembles the actual type definitions one would use when making an FCL implementation.

**Note that currently there are no official type definitions available for FCL. If you are using TypeScript, you will have to create your own type definitions (possibly based on the schema definitions presented in this document).**

## Common definitions[​](#common-definitions "Direct link to Common definitions")

In this section we introduce some common definitions that the individual object definitions will be deriving from.

First, let us define the kinds of FCL objects available:

`_10

type ObjectType =

_10

| 'PollingResponse'

_10

| 'Service'

_10

| 'Identity'

_10

| 'ServiceProvider'

_10

| 'AuthnResponse'

_10

| 'Signable'

_10

| 'CompositeSignature'

_10

| 'OpenID'`

The fields common to all FCL objects then can be defined as follows:

`_10

interface ObjectBase<Version = '1.0.0'> {

_10

f_vsn: Version

_10

f_type: ObjectType

_10

}`

The `f_vsn` field is usually `1.0.0` for this specification, but some exceptions will be defined by passing a different `Version` type parameter to `ObjectBase`.

All FCL objects carry an `f_type` field so that their types can be identified at runtime.

## FCL objects[​](#fcl-objects "Direct link to FCL objects")

In this section we will define the FCL objects with each `ObjectType`.

We also define the union of them to mean any FCL object:

`_10

type FclObject =

_10

| PollingResponse

_10

| Service

_10

| Identity

_10

| ServiceProvider

_10

| AuthnResponse

_10

| Signable

_10

| CompositeSignature

_10

| OpenID`

### `PollingResponse`[​](#pollingresponse "Direct link to pollingresponse")

`_10

interface PollingResponse extends ObjectBase {

_10

f_type: 'PollingResponse'

_10

status: 'APPROVED' | 'DECLINED' | 'PENDING' | 'REDIRECT'

_10

reason: string | null

_10

data?: FclObject

_10

updates?: FclObject

_10

local?: FclObject

_10

}`

Each response back to FCL must be "wrapped" in a `PollingResponse`. The `status` field determines the meaning of the response:

* An `APPROVED` status means that the request has been approved. The `data` field should be present.
* A `DECLINED` status means that the request has been declined. The `reason` field should contain a human readable reason for the refusal.
* A `PENDING` status means that the request is being processed. More `PENDING` responses may follow, but eventually a non-pending status should be returned. The `updates` and `local` fields may be present.
* The `REDIRECT` status is reserved, and should not be used by wallet services.

In summary, zero or more `PENDING` responses should be followed by a non-pending response. It is entirely acceptable for your service to immediately return an `APPROVED` Polling Response, skipping a `PENDING` state.

See also [PollingResponse](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/polling-response.js).

Here are some examples of valid `PollingResponse` objects:

`_55

// APPROVED

_55

{

_55

f_type: "PollingResponse",

_55

f_vsn: "1.0.0",

_55

status: "APPROVED",

_55

data: ___, // what the service needs to send to FCL

_55

}

_55

_55

// Declined

_55

{

_55

f_type: "PollingResponse",

_55

f_vsn: "1.0.0",

_55

status: "DECLINED",

_55

reason: "Declined by user."

_55

}

_55

_55

// Pending - Simple

_55

{

_55

f_type: "PollingResponse",

_55

f_vsn: "1.0.0",

_55

status: "PENDING",

_55

updates: {

_55

f_type: "Service",

_55

f_vsn: "1.0.0",

_55

type: "back-channel-rpc",

_55

endpoint: "https://____", // where post request will be sent

_55

method: "HTTP/POST",

_55

data: {}, // will be included in the request's body

_55

params: {}, // will be included in the request's url

_55

}

_55

}

_55

_55

// Pending - First Time with Local

_55

{

_55

f_type: "PollingResponse",

_55

f_vsn: "1.0.0",

_55

status: "PENDING",

_55

updates: {

_55

f_type: "Service",

_55

f_vsn: "1.0.0",

_55

type: "back-channel-rpc",

_55

endpoint: "https://____", // where post request will be sent

_55

method: "HTTP/POST",

_55

data: {}, // included in body of request

_55

params: {}, // included as query params on endpoint

_55

},

_55

local: {

_55

f_type: "Service",

_55

f_vsn: "1.0.0",

_55

endpoint: "https://____", // the iframe that will be rendered,

_55

method: "VIEW/IFRAME",

_55

data: {}, // sent to frame when ready

_55

params: {}, // included as query params on endpoint

_55

}

_55

}`

A `PollingResponse` can alternatively be constructed using `WalletUtils` when sending `"APPROVED"` or `"DECLINED"` responses.

`_14

import {WalletUtils} from "@onflow/fcl"

_14

_14

// Approving a PollingResponse

_14

// Example using an AuthnResponse as the PollingResponse data

_14

WalletUtils.approve({

_14

f_type: "AuthnResponse",

_14

f_vsn: "1.0.0"

_14

...

_14

})

_14

_14

// Rejecting a PollingResponse

_14

// Supplies a reason for declining

_14

const reason = "User declined to authenticate."

_14

WalletUtils.decline(reason)`

### `Service`[​](#service "Direct link to service")

`_28

type ServiceType =

_28

| 'authn'

_28

| 'authz'

_28

| 'user-signature'

_28

| 'pre-authz'

_28

| 'open-id'

_28

| 'back-channel-rpc'

_28

| 'authn-refresh'

_28

_28

type ServiceMethod =

_28

| 'HTTP/POST'

_28

| 'IFRAME/RPC'

_28

| 'POP/RPC'

_28

| 'TAB/RPC'

_28

| 'EXT/RPC'

_28

| 'DATA'

_28

_28

interface Service extends ObjectBase {

_28

f_type: 'Service'

_28

type: ServiceType

_28

method: ServiceMethod

_28

uid: string

_28

endpoint: string

_28

id: string

_28

identity: Identity

_28

provider?: ServiceProvider

_28

data?: FclObject

_28

}`

The meaning of the fields is as follows.

* `type`: The type of this service.
* `method`: The service method this service uses. `DATA` means that the purpose of this service is just to provide the information in this `Service` object, and no active communication services are provided.
* `uid`: A unique identifier for the service. A common scheme for deriving this is to use `'wallet-name#${type}'`, where `${type}` refers to the type of this service.
* `endpoint`: Defines where to communicate with the service.
  + When `method` is `EXT/RPC`, this can be an arbitrary unique string, and the extension will need to use it to identify its own services. A common scheme for deriving the `endpoint` is to use `'ext:${address}'`, where `${address}` refers to the wallet's address. (See `ServiceProvider` for more information.)
* `id`: The wallet's internal identifier for the user. If no other identifier is used, simply the user's flow account address can be used here.
* `identity`: Information about the identity of the user.
* `provider`: Information about the wallet.
* `data`: Additional information used with a service of type `open-id`.

See also:

* [authn](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/authn.js)
* [authz](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/authz.js)
* [user-signature](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/user-signature.js)
* [pre-authz](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/pre-authz.js)
* [open-id](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/open-id.js)
* [back-channel-rpc](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/back-channel-rpc.js)

### `Identity`[​](#identity "Direct link to identity")

This object is used to define the identity of the user.

`_10

interface Identity extends ObjectBase {

_10

f_type: 'Identity'

_10

address: string

_10

keyId?: number

_10

}`

The meaning of the fields is as follows.

* `address`: The flow account address of the user.
* `keyId`: The id of the key associated with this account that will be used for signing.

### `ServiceProvider`[​](#serviceprovider "Direct link to serviceprovider")

This object is used to communicate information about a wallet.

`_10

interface ServiceProvider extends ObjectBase {

_10

f_type: 'ServiceProvider'

_10

address: string

_10

name?: string

_10

description?: string

_10

icon?: string

_10

website?: string

_10

supportUrl?: string

_10

supportEmail?: string

_10

}`

The meaning of the fields is as follows.

* `address`: A flow account address owned by the wallet. It is unspecified what this will be used for.
* `name`: The name of the wallet.
* `description`: A short description for the wallet.
* `icon`: An image URL for the wallet's icon.
* `website`: The wallet's website.
* `supportUrl`: A URL the user can use to get support with the wallet.
* `supportEmail`: An e-mail address the user can use to get support with the wallet.

### `AuthnResponse`[​](#authnresponse "Direct link to authnresponse")

This object is used to inform FCL about the services a wallet provides.

`_10

interface AuthnResponse extends ObjectBase {

_10

f_type: 'AuthnResponse'

_10

addr: string

_10

services: Service[]

_10

}`

The meaning of the fields is as follows.

* `addr`: The flow account address of the user.
* `services`: The list of services provided by the wallet.

### `Signable`[​](#signable "Direct link to signable")

`_21

interface Signable extends ObjectBase<'1.0.1'> {

_21

f_type: 'Signable'

_21

addr: string

_21

keyId: number

_21

voucher: {

_21

cadence: string

_21

refBlock: string

_21

computeLimit: number

_21

arguments: {

_21

type: string

_21

value: unknown

_21

}[]

_21

proposalKey: {

_21

address: string

_21

keyId: number

_21

sequenceNum: number

_21

}

_21

payer: string

_21

authorizers: string[]

_21

}

_21

}`

The `WalletUtils.encodeMessageFromSignable` function can be used to calculate the message that needs to be signed.

### `CompositeSignature`[​](#compositesignature "Direct link to compositesignature")

`_10

interface CompositeSignature extends ObjectBase {

_10

f_type: 'CompositeSignature'

_10

addr: string

_10

keyId: number

_10

signature: string

_10

}`

See also [CompositeSignature](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/composite-signature.js).

### `OpenID`[​](#openid "Direct link to openid")

TODO

## Miscellaneous objects[​](#miscellaneous-objects "Direct link to Miscellaneous objects")

### `Message`[​](#message "Direct link to message")

`_10

type MessageType =

_10

| 'FCL:VIEW:READY'

_10

| 'FCL:VIEW:READY:RESPONSE'

_10

| 'FCL:VIEW:RESPONSE'

_10

| 'FCL:VIEW:CLOSE'

_10

_10

type Message = {

_10

type: MessageType

_10

}`

A message that indicates the status of the protocol invocation.

This type is sometimes used as part of an *intersection type*. For example, the type `Message & PollingResponse` means a `PollingResponse` extended with the `type` field from `Message`.

### `ExtensionServiceInitiationMessage`[​](#extensionserviceinitiationmessage "Direct link to extensionserviceinitiationmessage")

`_10

type ExtensionServiceInitiationMessage = {

_10

service: Service

_10

}`

This object is used to invoke a service when the `EXT/RPC` service method is used.

## See also[​](#see-also "Direct link to See also")

* [local-view](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/local-view.js)
* [frame](https://github.com/onflow/fcl-js/blob/master/packages/fcl-core/src/normalizers/service/frame.js)

# Service Methods

## IFRAME/RPC (Front Channel)[​](#iframerpc-front-channel "Direct link to IFRAME/RPC (Front Channel)")

`IFRAME/RPC` is the easiest to explain, so we will start with it:

* An iframe is rendered (comes from the `endpoint` in the service).
* The rendered iframe adds a listener and sends the `"FCL:VIEW:READY"` message. This can be simplified `WalletUtils.ready(callback)`
* FCL will send the data to be dealt with:
  + Where `body` is the stuff you care about, `params` and `data` are additional information you can provide in the service object.
* The wallet sends back an `"APPROVED"` or `"DECLINED"` post message. (It will be a `f_type: "PollingResponse"`, which we will get to in a bit). This can be simplified using `WalletUtils.approve` and `WalletUtils.decline`
  + If it's approved, the polling response's data field will need to be what FCL is expecting.
  + If it's declined, the polling response's reason field should say why it was declined.

`_19

export const WalletUtils.approve = data => {

_19

sendMsgToFCL("FCL:VIEW:RESPONSE", {

_19

f_type: "PollingResponse",

_19

f_vsn: "1.0.0",

_19

status: "APPROVED",

_19

reason: null,

_19

data: data,

_19

})

_19

}

_19

_19

export const WalletUtils.decline = reason => {

_19

sendMsgToFCL("FCL:VIEW:RESPONSE", {

_19

f_type: "PollingResponse",

_19

f_vsn: "1.0.0",

_19

status: "DECLINED",

_19

reason: reason,

_19

data: null,

_19

})

_19

}`

`_10

graph LR

_10

Start1(Start)

_10

--Bot 启动--> check1[检查群内的非 Authing 用户]

_10

--> addUser[添加 Authing 用户并消息提醒绑定手机号]

_10

--> End1(End)`

![IFRAME/RPC Diagram](https://raw.githubusercontent.com/onflow/fcl-js/master/packages/fcl-core/assets/service-method-diagrams/iframe-rpc.png)

## POP/RPC | TAB/RPC (Front Channel)[​](#poprpc--tabrpc-front-channel "Direct link to POP/RPC | TAB/RPC (Front Channel)")

`POP/RPC` and `TAB/RPC` work in an almost entirely similar way to `IFRAME/RPC`, except instead of rendering the `method` in an iframe, we render it in a popup or new tab. The same communication protocol between the rendered view and FCL applies.

![POP/RPC Diagram](https://raw.githubusercontent.com/onflow/fcl-js/master/packages/fcl-core/assets/service-method-diagrams/pop-rpc.png)

![TAB/RPC Diagram](https://raw.githubusercontent.com/onflow/fcl-js/master/packages/fcl-core/assets/service-method-diagrams/tab-rpc.png)

## HTTP/POST (Back Channel)[​](#httppost-back-channel "Direct link to HTTP/POST (Back Channel)")

`HTTP/POST` initially sends a post request to the `endpoint` specified in the service, which should immediately return a `f_type: "PollingResponse"`.

Like `IFRAME/RPC`, `POP/RPC` or `TAB/RPC`, our goal is to eventually get an `APPROVED` or `DECLINED` polling response, and technically this endpoint could return one of those immediately.

But more than likely that isn't the case and it will be in a `PENDING` state (`PENDING` is not available to `IFRAME/RPC`, `POP/RPC` or `TAB/RPC`).
When the polling response is `PENDING` it requires an `updates` field that includes a service, `BackChannelRpc`, that FCL can use to request an updated `PollingResponse` from.
FCL will use that `BackChannelRpc` to request a new `PollingResponse` which itself can be `APPROVED`, `DECLINED` or `PENDING`.
If it is `APPROVED` FCL will return, otherwise if it is `DECLINED` FCL will error. However, if it is `PENDING`, it will use the `BackChannelRpc` supplied in the new `PollingResponse` updates field. It will repeat this cycle until it is either `APPROVED` or `DECLINED`.

There is an additional optional feature that `HTTP/POST` enables in the first `PollingResponse` that is returned.
This optional feature is the ability for FCL to render an iframe, popup or new tab, and it can be triggered by supplying a service `type: "VIEW/IFRAME"`, `type: "VIEW/POP"` or `type: "VIEW/TAB"` and the `endpoint` that the wallet wishes to render in the `local` field of the `PollingResponse`. This is a great way for a wallet provider to switch to a webpage if displaying a UI is necessary for the service it is performing.

![HTTP/POST Diagram](https://raw.githubusercontent.com/onflow/fcl-js/master/packages/fcl-core/assets/service-method-diagrams/http-post.png)

## EXT/RPC (Front Channel)[​](#extrpc-front-channel "Direct link to EXT/RPC (Front Channel)")

`EXT/RPC` is used to enable and communicate between FCL and an installed web browser extension. (Though this specification is geared towards Chromium based browsers, it should be implementable in any browser with similar extension APIs available. From now on we will be using the word *Chrome* to refer to Chromium based browsers.)

An implementation of `EXT/RPC` needs to somehow enable communication between the application and the extension context. Implementing this is a bit more complex and usually relies on 3 key scripts to allow message passing between an installed extension and FCL. The separation of contexts enforced by Chrome and the availability of different Chrome APIs within those contexts require these scripts to be set up in a particular sequence so that the communication channels needed by FCL's `EXT/RPC` service method will work.

The following is an overview of these scripts and the functionality they need to support FCL:

* `background.js`: Used to launch the extension popup with `chrome.windows.create` if selected by the user from Discovery or set directly via `fcl.config.discovery.wallet`
* `content.js`: Used to proxy messages between the application to the extension via `chrome.runtime.sendMessage`.
* `script.js`: Injected by `content.js` into the application's HTML page. It appends the extension authn service to the `window.fcl_extensions` array on page load. This allows FCL to confirm installation and send extension details to Discovery or launch your wallet as the default wallet.

An example and guide showing how to build an FCL compatible wallet extension on Flow can be found [here](https://github.com/onflow/wallet-extension-example).

Once the extension is enabled (for example when the user selects it through the discovery service), the following communication protocol applies. (The term *send* should specifically refer to using `window.postMessage` in the application context, as this is the only interface between the application and the extension. Note that since `window.postMessage` broadcasts messages to all message event handlers, care should be taken by each party to filter only the messages targeted at them.)

* An `ExtensionServiceInitiationMessage` object is sent by FCL. It is the extension's responsibility to inspect the `endpoint` field of the service, and only activate itself (e.g. by opening a popup) if it is the provider of this service.
* The extension should respond by sending a `Message` with type `FCL:VIEW:READY`. (Usually this message will originate from the extension popup, and be relayed to the application context.)
* FCL will send a `Message` with type `FCL:VIEW:READY:RESPONSE`. Additional fields specific to the service (such as `body`, `params` or `data`) are usually present. See the section on the specific service for a description of these fields.
* The wallet sends back a `Message & PollingResponse` with type `FCL:VIEW:RESPONSE` with either an `APPROVED` or `DECLINED` status.
  + If it's approved, the polling response's data field will need to be what FCL is expecting.
  + If it's declined, the polling response's reason field should say why it was declined.

The extension can send a `Message` with type `FCL:VIEW:CLOSE` at any point during this protocol to indicate an interruption. This will halt FCL's current routine. On the other hand, once a `PollingResponse` with either an `APPROVED` or `DECLINED` status was sent, the protocol is considered finished, and the extension should not send any further messages as part of this exchange.

Conversely, when FCL sends a new `ExtensionServiceInitiationMessage`, the previous routine is interrupted. (This is the case even when the new service invocation is targeted at a different extension.)

Note that as a consequence of the above restrictions, only single service invocation can be in progress at a time.

Here is a code example for how an extension popup might send its response:

`_12

chrome.tabs.sendMessage(tabs[0].id, {

_12

f_type: "PollingResponse",

_12

f_vsn: "1.0.0",

_12

status: "APPROVED",

_12

reason: null,

_12

data: {

_12

f_type: "AuthnResponse",

_12

f_vsn: "1.0.0",

_12

addr: address,

_12

services: services,

_12

},

_12

});`

![EXT/RPC Diagram](https://raw.githubusercontent.com/onflow/fcl-js/master/packages/fcl-core/assets/service-method-diagrams/ext-rpc.png)

## `data` and `params`[​](#data-and-params "Direct link to data-and-params")

`data` and `params` are information that the wallet can provide in the service config that FCL will pass back to the service.

* `params` will be added onto the `endpoint` as query params.
* `data` will be included in the body of the `HTTP/POST` request or in the `FCL:VIEW:READY:RESPONSE` for a `IFRAME/RPC`, `POP/RPC`, `TAB/RPC` or `EXT/RPC`.

# Authentication Service

In the following examples, we'll walk you through the process of building an authentication service.

In FCL, wallets are configured by passing in a wallet provider's authentication URL or extension endpoint as the `discovery.wallet` config variable.

You will need to make and expose a webpage or API hosted at an authentication endpoint that FCL will use.

`_10

// IN APPLICATION

_10

// configuring fcl to point at a wallet looks like this

_10

import {config} from "@onflow/fcl"

_10

_10

config({

_10

"discovery.wallet": "url-or-endpoint-fcl-will-use-for-authentication", // FCL Discovery endpoint, wallet provider's authentication URL or extension endpoint

_10

"discovery.wallet.method": "IFRAME/RPC" // Optional. Available methods are "IFRAME/RPC", "POP/RPC", "TAB/RPC", "EXT/RPC" or "HTTP/POST", defaults to "IFRAME/RPC".

_10

})`

If the method specified is `IFRAME/RPC`, `POP/RPC` or `TAB/RPC`, then the URL specified as `discovery.wallet` will be rendered as a webpage. If the configured method is `EXT/RPC`, `discovery.wallet` should be set to the extension's `authn` `endpoint`. Otherwise, if the method specified is `HTTP/POST`, then the authentication process will happen over HTTP requests. (While authentication can be accomplished using any of those service methods, this example will use the `IFRAME/RPC` service method.)

Once the Authentication webpage is rendered, the extension popup is enabled, or the API is ready, you then need to tell FCL that it is ready. You will do this by sending a message to FCL, and FCL will send back a message with some additional information that you can use about the application requesting authentication on behalf of the user.

The following example is using the `IFRAME/RPC` method. Your authentication webpage will likely resemble the following code:

`_37

// IN WALLET AUTHENTICATION FRAME

_37

import {WalletUtils} from "@onflow/fcl"

_37

_37

function callback(data) {

_37

if (typeof data != "object") return

_37

if (data.type !== "FCL:VIEW:READY:RESPONSE") return

_37

_37

... // Do authentication things ...

_37

_37

// Send back AuthnResponse

_37

WalletUtils.sendMsgToFCL("FCL:VIEW:RESPONSE", {

_37

f_type: "PollingResponse",

_37

f_vsn: "1.0.0",

_37

status: "APPROVED",

_37

data: {

_37

f_type: "AuthnResponse",

_37

f_vsn: "1.0.0"

_37

...

_37

}

_37

})

_37

_37

// Alternatively be sent using WalletUtils.approve (or WalletUtils.decline)

_37

// which will wrap AuthnResponse in a PollingResponse

_37

WalletUtils.approve({

_37

f_type: "AuthnResponse",

_37

f_vsn: "1.0.0"

_37

...

_37

})

_37

}

_37

// add event listener first

_37

WalletUtils.onMsgFromFCL("FCL:VIEW:READY:RESPONSE", callback)

_37

_37

// tell fcl the wallet is ready

_37

WalletUtils.sendMsgToFCL("FCL:VIEW:READY")

_37

_37

// alternatively adds "FCL:VIEW:READY:RESPONSE" listener and sends "FCL:VIEW:READY"

_37

WalletUtils.ready(callback)`

During authentication, the application has a chance to request to you what they would like you to send back to them. These requests are included in the `FCL:VIEW:READY:RESPONSE` message sent to the wallet from FCL.

An example of such a request is the OpenID service. The application can request for example that you to send them the email address of the current user. The application requesting this information does not mean you need to send it. It's entirely optional for you to do so. However, some applications may depend on you sending the requested information back, and should you decline to do so it may cause the application to not work.

In the config they can also tell you a variety of things about them, such as the name of their application or a url for an icon of their application. You can use these pieces of information to customize your wallet's user experience should you desire to do so.

Your wallet having a visual distinction from the application, but still a seamless and connected experience is our goal here.

Whether your authentication process happens using a webpage with the `IFRAME/RPC`, `POP/RPC` or `TAB/RPC` methods, via an enabled extension using the `EXT/RPC` method, or using a backchannel to an API with the `HTTP/POST` method, the handshake is the same. The same messages are sent in all methods, however the transport mechanism changes. For `IFRAME/RPC`, `POP/RPC`, `TAB/RPC` or `EXT/RPC` methods, the transport is `window.postMessage()`, with the `HTTP/POST` method, the transport is HTTP post messages.

As always, you must never trust anything you receive from an application. Always do your due-diligence and be alert as you are the user's first line of defense against potentially malicious applications.

### Authenticate your User[​](#authenticate-your-user "Direct link to Authenticate your User")

It's important that you are confident that the user is who the user claims to be.

Have them provide enough proof to you that you are okay with passing their details back to FCL.
Using Blocto as an example, an authentication code is sent to the email a user enters at login.
This code can be used as validation and is everything Blocto needs to be confident in the user's identity.

### Once you know who your User is[​](#once-you-know-who-your-user-is "Direct link to Once you know who your User is")

Once you're confident in the user's identity, we can complete the authentication process.

The authentication process is complete once FCL receives back a response that configures FCL with FCL Services for the current user. This response is extremely important to FCL. At its core it tells FCL who the user is, and then via the included services it tells FCL how the user authenticated, how to request transaction signatures, how to get a personal message signed and the user's email and other details if requested. In the future it may also include many more things!

You can kind of think of FCL as a plugin system. But since those plugins exist elsewhere outside of FCL, FCL needs to be configured with information on how to communicate with them.

What you are sending back to FCL is everything that it needs to communicate with the plugins that you are supplying.
Your wallet is like a plugin to FCL, and these details tell FCL how to use you as a plugin.

Here is an example of an authentication response:

`_94

// IN WALLET AUTHENTICATION FRAME

_94

import {WalletUtils} from "@onflow/fcl"

_94

_94

WalletUtils.approve({

_94

f_type: "AuthnResponse",

_94

f_vsn: "1.0.0",

_94

addr: "0xUSER", // The user's flow address

_94

_94

services: [ // All the stuff that configures FCL

_94

_94

// Authentication Service - REQUIRED

_94

{

_94

f_type: "Service", // It's a service!

_94

f_vsn: "1.0.0", // Follows the v1.0.0 spec for the service

_94

type: "authn", // the type of service it is

_94

method: "DATA", // It's data!

_94

uid: "amazing-wallet#authn", // A unique identifier for the service

_94

endpoint: "your-url-that-fcl-will-use-for-authentication", // should be the same as was passed into the config

_94

id: "0xUSER", // the wallet's internal id for the user, use flow address if you don't have one

_94

// The User's Info

_94

identity: {

_94

f_type: "Identity", // It's an Identity!

_94

f_vsn: "1.0.0", // Follows the v1.0.0 spec for an identity

_94

address: "0xUSER", // The user's address

_94

keyId: 0, // OPTIONAL - The User's KeyId they will use

_94

},

_94

// The Wallet's Info

_94

provider: {

_94

f_type: "ServiceProvider", // It's a Service Provider

_94

f_vsn: "1.0.0", // Follows the v1.0.0 spec for service providers

_94

address: "0xWallet", // A flow address owned by the wallet

_94

name: "Amazing Wallet", // OPTIONAL - The name of your wallet. ie: "Dapper Wallet" or "Blocto Wallet"

_94

description: "The best wallet", // OPTIONAL - A short description for your wallet

_94

icon: "https://___", // OPTIONAL - Image url for your wallet's icon

_94

website: "https://___", // OPTIONAL - Your wallet's website

_94

supportUrl: "https://___", // OPTIONAL - An url the user can use to get support from you

_94

supportEmail: "help@aw.com", // OPTIONAL - An email the user can use to get support from you

_94

},

_94

},

_94

_94

// Authorization Service

_94

{

_94

f_type: "Service",

_94

f_vsn: "1.0.0",

_94

type: "authz",

_94

uid: "amazing-wallet#authz",

_94

...

_94

// We will cover this at length in the authorization section of this guide

_94

},

_94

_94

// User Signature Service

_94

{

_94

f_type: "Service",

_94

f_vsn: "1.0.0",

_94

type: "user-signature",

_94

uid: "amazing-wallet#user-signature",

_94

...

_94

// We will cover this at length in the user signature section of this guide

_94

},

_94

_94

// OpenID Service

_94

{

_94

f_type: "Service",

_94

f_vsn: "1.0.0",

_94

type: "open-id",

_94

uid: "amazing-wallet#open-id",

_94

method: "DATA",

_94

data: { // only include data that was request, ideally only if the user approves the sharing of data, everything is optional

_94

f_type: "OpenID",

_94

f_vsn: "1.0.0",

_94

profile: {

_94

name: "Jeff",

_94

family_name: "D", // icky underscored names because of OpenID Connect spec

_94

given_name: "Jeffrey",

_94

middle_name: "FakeMiddleName",

_94

nickname: "JeffJeff",

_94

preferred_username: "Jeff",

_94

profile: "https://www.jeff.jeff/",

_94

picture: "https://avatars.onflow.org/avatar/jeff",

_94

website: "https://www.jeff.jeff/",

_94

gender: "male",

_94

birthday: "1900-01-01", // can use 0000 for year if year is not known

_94

zoneinfo: "America/Vancouver",

_94

locale: "en",

_94

updated_at: "1625588304427"

_94

},

_94

email: {

_94

email: "jeff@jeff.jeff",

_94

email_verified: false,

_94

}

_94

},

_94

}

_94

]

_94

})`

### Stopping an Authentication Process[​](#stopping-an-authentication-process "Direct link to Stopping an Authentication Process")

From any frame, you can send a `FCL:VIEW:CLOSE` post message to FCL, which will halt FCL's current routine and close the frame.

`_10

import {WalletUtils} from "@onflow/fcl"

_10

_10

WalletUtils.sendMsgToFCL("FCL:VIEW:CLOSE")`

# Authorization Service

Authorization services are depicted with with a `type: "authz"`, and a `method` of either `HTTP/POST`, `IFRAME/RPC`, `POP/RPC`, `TAB/RPC` or `EXT/RPC`.
They are expected to eventually return a `f_type: "CompositeSignature"`.

An authorization service is expected to know the Account and the Key that will be used to sign the transaction at the time the service is sent to FCL (during authentication).

`_16

{

_16

f_type: "Service",

_16

f_vsn: "1.0.0",

_16

type: "authz", // say it's an authorization service

_16

uid: "amazing-wallet#authz", // standard service uid

_16

method: "HTTP/POST", // can also be `IFRAME/RPC` or `POP/RPC`

_16

endpoint: "https://____", // where to talk to the service

_16

identity: {

_16

f_type: "Identity",

_16

f_vsn: "1.0.0",

_16

address: "0xUser", // the address that the signature will be for

_16

keyId: 0, // the key for the address that the signature will be for

_16

},

_16

data: {},

_16

params: {},

_16

}`

FCL will use the `method` provided to request an array of composite signature from authorization service (Wrapped in a `PollingResponse`).
The authorization service will be sent a `Signable`.
The service is expected to construct an encoded message to sign from `Signable.voucher`.
It then needs to hash the encoded message, and prepend a required [transaction domain tag](https://github.com/onflow/fcl-js/blob/master/packages/sdk/src/encode/encode.ts#L18-L21).
Finally it signs the payload with the user/s keys, producing a signature.
This signature, as a HEX string, is sent back to FCL as part of the `CompositeSignature` which includes the user address and keyID in the data property of a `PollingResponse`.

`_10

signature =

_10

signable.voucher

_10

|> encode

_10

|> hash

_10

|> tag

_10

|> sign

_10

|> convert_to_hex`

The eventual response back from the authorization service should resolve to something like this:

`_12

{

_12

f_type: "PollingResponse",

_12

f_vsn: "1.0.0",

_12

status: "APPROVED",

_12

data: {

_12

f_type: "CompositeSignature",

_12

f_vsn: "1.0.0",

_12

addr: "0xUSER",

_12

keyId: 0,

_12

signature: "signature as hex value"

_12

}

_12

}`

A `CompositeSignature` can alternatively be constructed using `WalletUtils`

`_10

import {WalletUtils} from "@onflow/fcl"

_10

_10

WalletUtils.CompositeSignature(addr: String, keyId: Number, signature: Hex)`

# User Signature Service

User Signature services are depicted with a `type: "user-signature"` and a `method` of either `HTTP/POST`, `IFRAME/RPC`, `POP/RPC`, `TAB/RPC` or `EXT/RPC`.
They are expected to eventually return an array of `f_type: "CompositeSignature"`.

The User Signature service is a stock/standard service.

`_10

{

_10

f_type: "Service",

_10

f_vsn: "1.0.0",

_10

type: "user-signature", // say it's an user-signature service

_10

uid: "amazing-wallet#user-signature", // standard service uid

_10

method: "HTTP/POST", // can also be `IFRAME/RPC`

_10

endpoint: "https://___", // where to talk to the service

_10

data: {},

_10

params: {},

_10

}`

FCL will use the `method` provided to request an array of composite signatures from the user signature service (Wrapped in a `PollingResponse`).
The user signature service will be sent a `Signable`.
The service is expected to tag the `Signable.message` and then sign it with enough keys to produce a full weight.
The signatures need to be sent back to FCL as HEX strings in an array of `CompositeSignatures`.

`_10

// Pseudocode:

_10

// For every required signature

_10

import {WalletUtils} from "@onflow/fcl"

_10

_10

const encoded = WalletUtils.encodeMessageFromSignable(signable, signerAddress)

_10

const taggedMessage = tagMessage(encoded) // Tag the message to sign

_10

const signature = signMessage(taggedMessage) // Sign the message

_10

const hexSignature = signatureToHex(signature) // Convert the signature to hex, if required.

_10

_10

return hexSignature`

The eventual response back from the user signature service should resolve to something like this:

`_21

{

_21

f_type: "PollingResponse",

_21

f_vsn: "1.0.0",

_21

status: "APPROVED",

_21

data: [

_21

{

_21

f_type: "CompositeSignature",

_21

f_vsn: "1.0.0",

_21

addr: "0xUSER",

_21

keyId: 0,

_21

signature: "signature as hex value"

_21

},

_21

{

_21

f_type: "CompositeSignature",

_21

f_vsn: "1.0.0",

_21

addr: "0xUSER",

_21

keyId: 1,

_21

signature: "signature as hex value"

_21

}

_21

]

_21

}`

# Pre Authz Service

This is a strange one, but extremely powerful. This service should be used when a wallet is responsible for an account that's signing as multiple roles of a transaction, and wants the ability to change the accounts on a per role basis.

Pre Authz Services are depicted with a `type: "pre-authz"` and a `method` of either `HTTP/POST`, `IFRAME/RPC`, `POP/RPC`, `TAB/RPC` or `EXT/RPC`.
They are expected to eventually return a `f_type: "PreAuthzResponse"`.

The Pre Authz Service is a stock/standard service.

`_10

{

_10

f_type: "Service",

_10

f_vsn: "1.0.0",

_10

type: "pre-authz", // say it's a pre-authz service

_10

uid: "amazing-wallet#pre-authz", // standard service uid

_10

method: "HTTP/POST", // can also be IFRAME/RPC, POP/RPC, TAB/RPC

_10

endpoint: "https://___", // where to talk to the service

_10

data: {},

_10

params: {},

_10

}`

FCL will use the `method` provided to request a `PreAuthzReponse` (Wrapped in a `PollingResponse`).
The Authorizations service will be sent a `PreSignable`.
The pre-authz service is expected to look at the `PreSignable` and determine the breakdown of accounts to be used.
The pre-authz service is expected to return `Authz` services for each role it is responsible for.
A pre-authz service can only supply roles it is responsible for.
If a pre-authz service is responsible for multiple roles, but it wants the same account to be responsible for all the roles, it will need to supply an Authz service per role.

The eventual response back from the pre-authz service should resolve to something like this:

`_31

{

_31

f_type: "PollingResponse",

_31

f_vsn: "1.0.0",

_31

status: "APPROVED",

_31

data: {

_31

f_type: "PreAuthzResponse",

_31

f_vsn: "1.0.0",

_31

proposer: { // A single Authz Service

_31

f_type: "Service",

_31

f_vsn: "1.0.0",

_31

type: "authz",

_31

...

_31

},

_31

payer: [ // An array of Authz Services

_31

{

_31

f_type: "Service",

_31

f_vsn: "1.0.0",

_31

type: "authz",

_31

...

_31

}

_31

],

_31

authorization: [ // An array of Authz Services (it's singular because it only represents a singular authorization)

_31

{

_31

f_type: "Service",

_31

f_vsn: "1.0.0",

_31

type: "authz",

_31

...

_31

}

_31

],

_31

}

_31

}`

# Authentication Refresh Service

Since synchronization of a user's session is important to provide a seamless user experience when using an app and transacting with the Flow Blockchain, a way to confirm, extend, and refresh a user session can be provided by the wallet.

Authentication Refresh Services should include a `type: "authn-refresh"`, `endpoint`, and supported `method` (`HTTP/POST`, `IFRAME/RPC`, `POP/RPC`, or `EXT/RPC`).

FCL will use the `endpoint` and service `method` provided to request updated authentication data.
The `authn-refresh` service should refresh the user's session if necessary and return updated authentication configuration and user session data.

The service is expected to return a `PollingResponse` with a new `AuthnResponse` as data. If user input is required, a `PENDING` `PollingResponse` can be returned with a `local` view for approval/re-submission of user details.

The Authentication Refresh Service is a stock/standard service.

`_11

{

_11

"f_type": "Service",

_11

"f_vsn": "1.0.0",

_11

"type": "authn-refresh",

_11

"uid": "uniqueDedupeKey",

_11

"endpoint": "https://rawr",

_11

"method": "HTTP/POST", // "HTTP/POST", // HTTP/POST | IFRAME/RPC | HTTP/RPC

_11

"id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", // wallet's internal id for the user

_11

"data": {}, // included in body of request

_11

"params": {}, // included as query params on endpoint url

_11

}`

The provided `data` and `params` should include all the wallet needs to identify and re-authenticate the user if necessary.

The eventual response back from the `authn-refresh` service should resolve to an `AuthnResponse` and look something like this:

`_34

{

_34

f_type: "PollingResponse",

_34

f_vsn: "1.0.0",

_34

status: "APPROVED",

_34

data: {

_34

f_type: "AuthnResponse",

_34

f_vsn: "1.0.0",

_34

addr: "0xUSER",

_34

services: [

_34

// Authentication Service - REQUIRED

_34

{

_34

f_type: "Service",

_34

f_vsn: "1.0.0",

_34

type: "authn",

_34

...

_34

},

_34

// Authorization Service

_34

{

_34

f_type: "Service",

_34

f_vsn: "1.0.0",

_34

type: "authz",

_34

...

_34

},

_34

// Authentication Refresh Service

_34

{

_34

f_type: "Service",

_34

f_vsn: "1.0.0",

_34

type: "authn-refresh",

_34

...

_34

}

_34

// Additional Services

_34

],

_34

}

_34

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/wallet-provider-spec/index.md)

Last updated on **Apr 14, 2025** by **Brian Doyle**

[Previous

Cadence VS Code Extension](/tools/vscode-extension)[Next

Authorization Function](/tools/wallet-provider-spec/authorization-function)

###### Rate this page

😞😐😊

* [Status](#status)
* [Definitions](#definitions)
* [Common definitions](#common-definitions)
* [FCL objects](#fcl-objects)
  + [`PollingResponse`](#pollingresponse)
  + [`Service`](#service)
  + [`Identity`](#identity)
  + [`ServiceProvider`](#serviceprovider)
  + [`AuthnResponse`](#authnresponse)
  + [`Signable`](#signable)
  + [`CompositeSignature`](#compositesignature)
  + [`OpenID`](#openid)
* [Miscellaneous objects](#miscellaneous-objects)
  + [`Message`](#message)
  + [`ExtensionServiceInitiationMessage`](#extensionserviceinitiationmessage)
* [See also](#see-also)
* [IFRAME/RPC (Front Channel)](#iframerpc-front-channel)
* [POP/RPC | TAB/RPC (Front Channel)](#poprpc--tabrpc-front-channel)
* [HTTP/POST (Back Channel)](#httppost-back-channel)
* [EXT/RPC (Front Channel)](#extrpc-front-channel)
* [`data` and `params`](#data-and-params)
  + [Authenticate your User](#authenticate-your-user)
  + [Once you know who your User is](#once-you-know-who-your-user-is)
  + [Stopping an Authentication Process](#stopping-an-authentication-process)

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
* [Past Sporks](/networks/node-ops/node-operation/past-sporks)
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