# Source: https://developers.flow.com/build/tools/react-native-sdk/components

Components | Flow Developer Portal



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

        + [Flow React Native SDK](/build/tools/react-native-sdk)

          - [Hooks](/build/tools/react-native-sdk/hooks)- [Components](/build/tools/react-native-sdk/components)+ [Flow React SDK](/build/tools/react-sdk)

            + [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

                + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                      + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow React Native SDK](/build/tools/react-native-sdk)* Components

On this page

# Components

## Connect[​](#connect "Direct link to Connect")

A drop-in wallet connection component that handles the entire authentication flow. When disconnected, it displays a "Connect Wallet" button. When connected, it shows the user's address and opens a Profile modal on press.

**Props:**

* `onConnect?: () => void` – Callback triggered after successful authentication
* `onDisconnect?: () => void` – Callback triggered after logout
* `balanceType?: "cadence" | "evm" | "combined"` – Specifies which balance to display (default: `"cadence"`)
  + `"cadence"`: Shows the token balance from the Cadence side
  + `"evm"`: Shows the token balance from the Flow EVM side
  + `"combined"`: Shows the total combined token balance from both sides
* `balanceTokens?: TokenConfig[]` – Optional array of token configurations to display in the balance selector
* `modalEnabled?: boolean` – Whether to show the profile modal on press when connected (default: `true`)

**Basic Usage:**

The simplest way to add wallet connection to your app:

`_12

import { View, Text } from "react-native";

_12

import { Connect } from "@onflow/react-native-sdk";

_12

_12

function WalletSection() {

_12

return (

_12

<View>

_12

<Text>Connect Wallet</Text>

_12

<Text>Connect your Flow wallet to interact with the blockchain.</Text>

_12

<Connect />

_12

</View>

_12

);

_12

}`

**With Callbacks:**

`_10

import { Connect } from "@onflow/react-native-sdk";

_10

_10

<Connect

_10

onConnect={() => console.log("Wallet connected!")}

_10

onDisconnect={() => console.log("Wallet disconnected")}

_10

/>`

**With Balance Display:**

`_12

import { Connect } from "@onflow/react-native-sdk";

_12

_12

<Connect

_12

balanceType="combined"

_12

balanceTokens={[

_12

{

_12

symbol: "FLOW",

_12

name: "Flow",

_12

vaultIdentifier: "A.1654653399040a61.FlowToken.Vault",

_12

},

_12

]}

_12

/>`

---

## Profile[​](#profile "Direct link to Profile")

A standalone component for displaying wallet information including account address and balance. Use this when you want to show user details separately from the Connect button.

**Props:**

* `onDisconnect?: () => void` – Callback triggered when the user presses the disconnect button
* `balanceType?: "cadence" | "evm" | "combined"` – Specifies which balance to display (default: `"cadence"`)
  + `"cadence"`: Shows the token balance from the Cadence side
  + `"evm"`: Shows the token balance from the Flow EVM side
  + `"combined"`: Shows the total combined token balance from both sides
* `balanceTokens?: TokenConfig[]` – Optional array of token configurations to display in the balance selector

**Usage:**

`_19

import { View } from "react-native";

_19

import { Profile, useFlowCurrentUser } from "@onflow/react-native-sdk";

_19

_19

function UserProfile() {

_19

const { user } = useFlowCurrentUser();

_19

_19

if (!user?.loggedIn) {

_19

return null;

_19

}

_19

_19

return (

_19

<View>

_19

<Profile

_19

balanceType="combined"

_19

onDisconnect={() => console.log("User disconnected")}

_19

/>

_19

</View>

_19

);

_19

}`

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-native-sdk/components.md)

Last updated on **Dec 17, 2025** by **Michael Fabozzi**

[Previous

Hooks](/build/tools/react-native-sdk/hooks)[Next

Flow React SDK](/build/tools/react-sdk)

###### Rate this page

😞😐😊

Copy as Markdown

* [Connect](#connect)* [Profile](#profile)

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