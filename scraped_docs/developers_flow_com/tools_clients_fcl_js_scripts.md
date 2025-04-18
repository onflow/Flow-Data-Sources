# Source: https://developers.flow.com/tools/clients/fcl-js/scripts

Scripts | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [@onflow/kit](/tools/kit)
* [Flow Emulator](/tools/emulator)
* [Flow CLI](/tools/flow-cli)
* [Cadence VS Code Extension](/tools/vscode-extension)
* [Flow Dev Wallet](/tools/flow-dev-wallet)
* [Client Tools](/tools/clients)

  + [Flow Client Library (FCL)](/tools/clients/fcl-js)

    - [FCL Reference](/tools/clients/fcl-js/api)
    - [SDK Reference](/tools/clients/fcl-js/sdk-guidelines)
    - [Authentication](/tools/clients/fcl-js/authentication)
    - [How to Configure FCL](/tools/clients/fcl-js/configure-fcl)
    - [Cross VM Packages](/tools/clients/fcl-js/cross-vm)
    - [Wallet Discovery](/tools/clients/fcl-js/discovery)
    - [Installation](/tools/clients/fcl-js/installation)
    - [Interaction Templates](/tools/clients/fcl-js/interaction-templates)
    - [Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)
    - [Scripts](/tools/clients/fcl-js/scripts)
    - [Transactions](/tools/clients/fcl-js/transactions)
    - [Signing and Verifying Arbitrary Data](/tools/clients/fcl-js/user-signatures)
    - [WalletConnect 2.0 Manual Configuration](/tools/clients/fcl-js/wallet-connect)
  + [Flow Go SDK](/tools/clients/flow-go-sdk)
* [Error Codes](/tools/error-codes)
* [Wallet Provider Spec](/tools/wallet-provider-spec)
* [Tools](/tools)

* [Client Tools](/tools/clients)
* [Flow Client Library (FCL)](/tools/clients/fcl-js)
* Scripts

On this page

# Scripts

Scripts let you run non-permanent Cadence scripts on the Flow blockchain. They can return data.

They always need to contain a `access(all) fun main()` function as an entry point to the script.

`fcl.query` is a function that sends Cadence scripts to the chain and receives back decoded responses.

The `cadence` key inside the object sent to the `query` function is a [JavaScript Tagged Template Literal](https://styled-components.com/docs/advanced#tagged-template-literals) that we can pass Cadence code into.

### Sending Your First Script[​](#sending-your-first-script "Direct link to Sending Your First Script")

The following example demonstrates how to send a script to the Flow blockchain. This script adds two numbers and returns the result.

`_11

import * as fcl from "@onflow/fcl"

_11

_11

const response = await fcl.query({

_11

cadence: `

_11

access(all) fun main(): Int {

_11

return 1 + 2

_11

}

_11

`

_11

})

_11

_11

console.log(response) // 3`

### A More Complex Script[​](#a-more-complex-script "Direct link to A More Complex Script")

[Resources](https://cadence-lang.org/docs/language/resources) and [Structs](https://cadence-lang.org/docs/language/composite-types#structures) are complex data types that are fairly common place in Cadence.

In the following code snippet, our script defines a struct called `Point`, it then returns a list of them.

The closest thing to a Structure in JavaScript is an object. In this case when we decode this response, we would be expecting to get back an array of objects, where the objects have an `x` and `y` value.

`_21

import * as fcl from "@onflow/fcl"

_21

_21

const response = await fcl.query({

_21

cadence: `

_21

access(all) struct Point {

_21

access(all) var x: Int

_21

access(all) var y: Int

_21

_21

init(x: Int, y: Int) {

_21

self.x = x

_21

self.y = y

_21

}

_21

}

_21

_21

access(all) fun main(): [Point] {

_21

return [Point(x: 1, y: 1), Point(x: 2, y: 2)]

_21

}

_21

`

_21

})

_21

_21

console.log(response) // [{x:1, y:1}, {x:2, y:2}]`

### Transforming Data with Custom Decoders[​](#transforming-data-with-custom-decoders "Direct link to Transforming Data with Custom Decoders")

In our app, we probably have a way of representing these Cadence values internally. In the above example it might be a `Point` class.

FCL enables us to provide custom decoders that we can use to transform the data we receive from the Flow blockchain at the edge, before anything else in our dapp gets a chance to look at it.

We add these custom decoders by [Configuring FCL](/tools/clients/fcl-js/configure-fcl).
This lets us set it once when our dapp starts up and use our normalized data through out the rest of our dapp.

In the below example we will use the concept of a `Point` again, but this time, we will add a custom decoder, that enables `fcl.decode` to transform it into a custom JavaScript `Point` class.

`_31

import * as fcl from "@onflow/fcl"

_31

_31

class Point {

_31

constructor({ x, y }) {

_31

this.x = x

_31

this.y = y

_31

}

_31

}

_31

_31

fcl.config()

_31

.put("decoder.Point", point => new Point(point))

_31

_31

const response = await fcl.query({

_31

cadence: `

_31

access(all) struct Point {

_31

access(all) var x: Int

_31

access(all) var y: Int

_31

_31

init(x: Int, y: Int) {

_31

self.x = x

_31

self.y = y

_31

}

_31

}

_31

_31

access(all) fun main(): [Point] {

_31

return [Point(x: 1, y: 1), Point(x: 2, y: 2)]

_31

}

_31

`

_31

})

_31

_31

console.log(response) // [Point{x:1, y:1}, Point{x:2, y:2}]`

To learn more about `query`, check out the [API documentation](/tools/clients/fcl-js/api#query).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tools/clients/fcl-js/scripts.md)

Last updated on **Apr 15, 2025** by **Brian Doyle**

[Previous

Proving Ownership of a Flow Account](/tools/clients/fcl-js/proving-authentication)[Next

Transactions](/tools/clients/fcl-js/transactions)

###### Rate this page

😞😐😊

* [Sending Your First Script](#sending-your-first-script)
* [A More Complex Script](#a-more-complex-script)
* [Transforming Data with Custom Decoders](#transforming-data-with-custom-decoders)

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