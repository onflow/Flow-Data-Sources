# Source: https://developers.flow.com/build/tools/clients/fcl-js/scripts

Scripts | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[DeFi](/defi)[Tutorials](/blockchain-development-tutorials)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [Flow React SDK](/build/tools/react-sdk)

          + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    - [Flow Client Library (FCL)](/build/tools/clients/fcl-js)

                      * [Packages Docs](/build/tools/clients/fcl-js/packages-docs)

                        * [Authentication](/build/tools/clients/fcl-js/authentication)* [How to Configure FCL](/build/tools/clients/fcl-js/configure-fcl)* [Cross VM Packages](/build/tools/clients/fcl-js/cross-vm)

                              * [Wallet Discovery](/build/tools/clients/fcl-js/discovery)* [Installation](/build/tools/clients/fcl-js/installation)* [Interaction Templates](/build/tools/clients/fcl-js/interaction-templates)* [Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)* [Scripts](/build/tools/clients/fcl-js/scripts)* [Transactions](/build/tools/clients/fcl-js/transactions)* [Signing and Verifying Arbitrary Data](/build/tools/clients/fcl-js/user-signatures)- [Flow Go SDK](/build/tools/clients/flow-go-sdk)+ [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Client Tools](/build/tools/clients)* [Flow Client Library (FCL)](/build/tools/clients/fcl-js)* Scripts

On this page

# Scripts

Scripts let you run non-permanent Cadence scripts on the Flow blockchain. They can return data.

They always need to contain a `access(all) fun main()` function as an entry point to the script.

`fcl.query` is a function that sends Cadence scripts to the chain and receives back decoded responses.

The `cadence` key inside the object sent to the `query` function is a [JavaScript Tagged Template Literal](https://styled-components.com/docs/advanced#tagged-template-literals) that we can pass Cadence code into.

### Send your first script[​](#send-your-first-script "Direct link to Send your first script")

The following example demonstrates how to send a script to the Flow blockchain. This script adds two numbers and returns the result.

`` _11

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

console.log(response) // 3 ``

### A more complex script[​](#a-more-complex-script "Direct link to A more complex script")

[Resources](https://cadence-lang.org/docs/language/resources) and [Structs](https://cadence-lang.org/docs/language/composite-types#structures) are complex data types that are fairly common place in Cadence.

In the following code snippet, our script defines a struct called `Point`, it then returns a list of them.

The closest thing to a Structure in JavaScript is an object. In this case when we decode this response, we would expect to get back an array of objects, where the objects have an `x` and `y` value.

`` _21

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

console.log(response) // [{x:1, y:1}, {x:2, y:2}] ``

### Transform data with custom decoders[​](#transform-data-with-custom-decoders "Direct link to Transform data with custom decoders")

In our app, we probably have a way to represent these Cadence values internally. In the above example it might be a `Point` class.

FCL allows us to provide custom decoders that we can use to transform the data we receive from the Flow blockchain at the edge, before anything else in our dApp gets a chance to look at it.

To add these custom decoders, we [configure FCL](/build/tools/clients/fcl-js/configure-fcl). This lets us set it once when our dApp starts up and use our normalized data through out the rest of our dapp.

In the below example, we will use the concept of a `Point` again, but this time, we will add a custom decoder, that allows `fcl.decode` to transform it into a custom JavaScript `Point` class.

`` _31

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

console.log(response) // [Point{x:1, y:1}, Point{x:2, y:2}] ``

To learn more about `query`, check out the [API documentation](/build/tools/clients/fcl-js/packages-docs/fcl/query).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/clients/fcl-js/scripts.md)

Last updated on **Dec 9, 2025** by **cshannon1218**

[Previous

Proving Ownership of a Flow Account](/build/tools/clients/fcl-js/proving-authentication)[Next

Transactions](/build/tools/clients/fcl-js/transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Send your first script](#send-your-first-script)* [A more complex script](#a-more-complex-script)* [Transform data with custom decoders](#transform-data-with-custom-decoders)

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