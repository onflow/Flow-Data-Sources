# Source: https://developers.flow.com/build/tools/react-sdk/components

Flow React SDK Components | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)* [Cadence](/build/cadence/quickstart)

    + [Quickstart ↙](/build/cadence/quickstart)+ [Differences vs. EVM](/build/cadence/differences-vs-evm)+ [Basics](/build/cadence/basics/network-architecture)

          + [Writing and Deploying Smart Contracts](/build/cadence/learn-cadence)

            + [Advanced Concepts](/build/cadence/advanced-concepts/account-abstraction)

              + [Core Smart Contracts](/build/cadence/core-contracts)* [Solidity (EVM)](/build/evm/quickstart)

      + [EVM Quickstart](/build/evm/quickstart)+ [How it Works](/build/evm/how-it-works)+ [EVM Wallet Setup](/build/evm/using)+ [Network Information](/build/evm/networks)+ [Fees](/build/evm/fees)+ [Accounts](/build/evm/accounts)* [Tools & SDKs](/build/tools)

        + [@onflow/react-sdk](/build/tools/react-sdk)

          - [Flow React SDK Hooks](/build/tools/react-sdk/hooks)- [Flow React SDK Components](/build/tools/react-sdk/components)+ [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [@onflow/react-sdk](/build/tools/react-sdk)* Flow React SDK Components

On this page

# React SDK Components

## 🎨 Theming[​](#-theming "Direct link to 🎨 Theming")

### How Theming Works[​](#how-theming-works "Direct link to How Theming Works")

All UI components in `@onflow/react-sdk` are styled using [Tailwind CSS](https://tailwindcss.com/) utility classes. The kit supports both light and dark themes out of the box, using Tailwind's `dark:` variant for dark mode styling.

You can customize the look and feel of the kit by providing a custom theme to the `FlowProvider` via the `theme` prop. This allows you to override default colors and styles to better match your app's branding.

`_17

import { FlowProvider } from "@onflow/react-sdk"

_17

_17

<FlowProvider

_17

config={...}

_17

theme={{

_17

colors: {

_17

primary: {

_17

background: "bg-blue-600 dark:bg-blue-400",

_17

text: "text-white dark:text-blue-900",

_17

hover: "hover:bg-blue-700 dark:hover:bg-blue-300",

_17

},

_17

// ...other color overrides

_17

}

_17

}}

_17

>

_17

<App />

_17

</FlowProvider>`

---

## 🌙 Dark Mode[​](#-dark-mode "Direct link to 🌙 Dark Mode")

### How Dark Mode Works[​](#how-dark-mode-works "Direct link to How Dark Mode Works")

Dark mode is **fully controlled by the parent app** using the `darkMode` prop on `FlowProvider`. The kit does not manage dark mode state internally—this gives you full control and ensures the kit always matches your app's theme.

* `darkMode={false}` (default): Forces all kit components to use light mode styles.
* `darkMode={true}`: Forces all kit components to use dark mode styles.
* You can dynamically change the `darkMode` prop to switch themes at runtime.

**Example:**

`_10

function App() {

_10

// Parent app manages dark mode state

_10

const [isDark, setIsDark] = useState(false)

_10

_10

return (

_10

<FlowProvider config={...} darkMode={isDark}>

_10

<MyFlowComponents />

_10

</FlowProvider>

_10

)

_10

}`

**Accessing Dark Mode State in Components:**

You can use the `useDarkMode` hook to check the current mode inside your components:

`_10

import { useDarkMode } from "@onflow/react-sdk"

_10

_10

function MyComponent() {

_10

// useDarkMode only returns the current state, no setter

_10

const { isDark } = useDarkMode()

_10

return <div>{isDark ? "Dark mode" : "Light mode"}</div>

_10

}`

### Notes[​](#notes "Direct link to Notes")

* The kit does **not** automatically follow system preferences or save user choices. You are responsible for managing and passing the correct `darkMode` value.
* All kit components will automatically apply the correct Tailwind `dark:` classes based on the `darkMode` prop.
* For best results, ensure your app's global theme and the kit's `darkMode` prop are always in sync.

---

## Components[​](#components "Direct link to Components")

### `Connect`[​](#connect "Direct link to connect")

A drop-in wallet connection component with UI for copy address, logout, and balance display.

**Props:**

* `variant?: ButtonProps["variant"]` – Optional button style variant (default: `"primary"`)
* `onConnect?: () => void` – Callback triggered after successful authentication
* `onDisconnect?: () => void` – Callback triggered after logout
* `balanceType?: "cadence" | "evm" | "combined"` – Specifies which balance to display (default: `"cadence"`). Options:
  + `"cadence"`: Shows the FLOW token balance from the Cadence side
  + `"evm"`: Shows the FLOW token balance from the Flow EVM side
  + `"combined"`: Shows the total combined FLOW token balance from both sides

`_10

import { Connect } from "@onflow/react-sdk"

_10

_10

<Connect

_10

onConnect={() => console.log("Connected!")}

_10

onDisconnect={() => console.log("Logged out")}

_10

/>`

### Live Demo[​](#live-demo "Direct link to Live Demo")



---

### `TransactionButton`[​](#transactionbutton "Direct link to transactionbutton")

Button component for executing Flow transactions with built-in loading states and global transaction management.

**Props:**

* `transaction: Parameters<typeof mutate>[0]` – Flow transaction object to execute when clicked
* `label?: string` – Optional custom button label (default: `"Execute Transaction"`)
* `mutation?: UseMutationOptions<string, Error, Parameters<typeof mutate>[0]>` – Optional TanStack React Query mutation options
* `...buttonProps` – All other `ButtonProps` except `onClick` and `children` (includes `variant`, `disabled`, `className`, etc.)

`` _23

import { TransactionButton } from "@onflow/react-sdk"

_23

_23

const myTransaction = {

_23

cadence: `

_23

transaction() {

_23

prepare(acct: &Account) {

_23

log("Hello from ", acct.address)

_23

}

_23

}

_23

`,

_23

args: (arg, t) => [],

_23

limit: 100,

_23

}

_23

_23

<TransactionButton

_23

transaction={myTransaction}

_23

label="Say Hello"

_23

variant="primary"

_23

mutation={{

_23

onSuccess: (txId) => console.log("Transaction sent:", txId),

_23

onError: (error) => console.error("Transaction failed:", error),

_23

}}

_23

/> ``

### Live Demo[​](#live-demo-1 "Direct link to Live Demo")



---

### `TransactionDialog`[​](#transactiondialog "Direct link to transactiondialog")

Dialog component for real-time transaction status updates.

**Props:**

* `open: boolean` – Whether the dialog is open
* `onOpenChange: (open: boolean) => void` – Callback to open/close dialog
* `txId?: string` – Optional Flow transaction ID to track
* `onSuccess?: () => void` – Optional callback when transaction is successful
* `pendingTitle?: string` – Optional custom pending state title
* `pendingDescription?: string` – Optional custom pending state description
* `successTitle?: string` – Optional custom success state title
* `successDescription?: string` – Optional custom success state description
* `closeOnSuccess?: boolean` – If `true`, closes the dialog automatically after success

`_11

import { TransactionDialog } from "@onflow/react-sdk"

_11

_11

_11

<TransactionDialog

_11

open={isOpen}

_11

onOpenChange={setIsOpen}

_11

txId="6afa38b7bd1a23c6cc01a4ea2e51ed376f16761f9d06eca0577f674a9edc0716"

_11

pendingTitle="Sending..."

_11

successTitle="All done!"

_11

closeOnSuccess

_11

/>`

### Live Demo[​](#live-demo-2 "Direct link to Live Demo")



---

### `TransactionLink`[​](#transactionlink "Direct link to transactionlink")

Link to the block explorer with the appropriate network scoped to transaction ID.

**Props:**

* `txId: string` – The transaction ID to link to
* `variant?: ButtonProps["variant"]` – Optional button variant (defaults to `"link"`)

`_10

import { TransactionLink } from "@onflow/react-sdk"

_10

_10

<TransactionLink txId="your-tx-id" />`

### Live Demo[​](#live-demo-3 "Direct link to Live Demo")

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/components.md)

Last updated on **Sep 25, 2025** by **Felipe Cevallos**

[Previous

Flow React SDK Hooks](/build/tools/react-sdk/hooks)[Next

Flow Emulator](/build/tools/emulator)

###### Rate this page

😞😐😊

Copy as Markdown

* [🎨 Theming](#-theming)
  + [How Theming Works](#how-theming-works)* [🌙 Dark Mode](#-dark-mode)
    + [How Dark Mode Works](#how-dark-mode-works)+ [Notes](#notes)* [Components](#components)
      + [`Connect`](#connect)+ [Live Demo](#live-demo)+ [`TransactionButton`](#transactionbutton)+ [Live Demo](#live-demo-1)+ [`TransactionDialog`](#transactiondialog)+ [Live Demo](#live-demo-2)+ [`TransactionLink`](#transactionlink)+ [Live Demo](#live-demo-3)

Documentation

* [Getting Started](/blockchain-development-tutorials/cadence/getting-started/smart-contract-interaction)* [Tools & SDKs](/build/tools)* [Cadence](https://cadence-lang.org/docs/)* [Mobile](/blockchain-development-tutorials/cadence/mobile)* [FCL](/build/tools/clients/fcl-js)* [Testing](/build/cadence/smart-contracts/testing)* [CLI](/build/tools/flow-cli)* [Emulator](/build/tools/emulator)* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)* [Flow Port](https://port.flow.com/)* [Developer Grants](https://github.com/onflow/developer-grants)* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)* [Flowverse](https://www.flowverse.co/)* [Emerald Academy](https://academy.ecdao.org/)* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)* [Cadence Cookbook](https://cookbook.flow.com)* [Core Contracts & Standards](/build/cadence/core-contracts)* [EVM](/build/evm/quickstart)

Network

* [Network Status](https://status.flow.com/)* [Flowscan Mainnet](https://flowscan.io/)* [Flowscan Testnet](https://testnet.flowscan.io/)* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)* [Node Operation](/protocol/node-ops)* [Spork Information](/protocol/node-ops/node-operation/network-upgrade)

More

* [GitHub](https://github.com/onflow)* [Discord](https://discord.gg/flow)* [Forum](https://forum.flow.com/)* [Flow](https://flow.com/)* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.