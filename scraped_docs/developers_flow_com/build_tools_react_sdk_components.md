# Source: https://developers.flow.com/build/tools/react-sdk/components

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

        + [Flow React SDK](/build/tools/react-sdk)

          - [Hooks](/build/tools/react-sdk/hooks)- [Components](/build/tools/react-sdk/components)+ [Flow Emulator](/build/tools/emulator)+ [Flow CLI](/build/tools/flow-cli)

              + [Cadence VS Code Extension](/build/tools/vscode-extension)+ [Flow Dev Wallet](/build/tools/flow-dev-wallet)+ [Client Tools](/build/tools/clients)

                    + [Error Codes](/build/tools/error-codes)+ [Wallet Provider Spec](/build/tools/wallet-provider-spec)

* * [Tools & SDKs](/build/tools)* [Flow React SDK](/build/tools/react-sdk)* Components

On this page

# React SDK Components

## Components[​](#components "Direct link to Components")

### `Connect`[​](#connect "Direct link to connect")

A drop-in wallet connection component with UI for copy address, logout, and balance display. Displays user scheduled transactions within its profile modal with support for multiple tokens.

[Open in Playground →](https://react.flow.com/#connect)

**Props:**

* `variant?: ButtonProps["variant"]` – Optional button style variant (default: `"primary"`)
* `onConnect?: () => void` – Callback triggered after successful authentication
* `onDisconnect?: () => void` – Callback triggered after logout
* `balanceType?: "cadence" | "evm" | "combined"` – Specifies which balance to display (default: `"cadence"`). Options:
  + `"cadence"`: Shows the token balance from the Cadence side
  + `"evm"`: Shows the token balance from the Flow EVM side
  + `"combined"`: Shows the total combined token balance from both sides
* `balanceTokens?: TokenConfig[]` – Optional array of token configurations to display in the balance selector. Each `TokenConfig` requires:
  + `symbol: string` – Token symbol (e.g. "FLOW", "USDC")
  + `name: string` – Full token name
  + Either `vaultIdentifier: string` (for Cadence tokens) or `erc20Address: string` (for EVM tokens)
* `modalConfig?: ConnectModalConfig` – Optional configuration for the profile modal:
  + `scheduledTransactions.show?: boolean` – Whether to show the scheduled transactions tab (default: `false`)
  + `scheduledTransactions.filterHandlerTypes?: string[]` – Optional array of handler type identifiers to filter displayed transactions
* `modalEnabled?: boolean` – Whether to show the profile modal on click when connected (default: `true`). When `false`, clicking the button when connected will disconnect instead

WalletConnect Support

To enable WalletConnect as a wallet option, add your registered project ID to the `walletconnectProjectId` field in your `FlowProvider` config.

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

#### Live Demo[​](#live-demo "Direct link to Live Demo")



---

### `Profile`[​](#profile "Direct link to profile")

A standalone component for displaying wallet information including account address, balance and optional scheduled transactions.

[Open in Playground →](https://react.flow.com/#profile)

**Props:**

* `onDisconnect?: () => void` – Callback triggered when the user clicks the disconnect button
* `balanceType?: "cadence" | "evm" | "combined"` – Specifies which balance to display (default: `"cadence"`). Options:
  + `"cadence"`: Shows the token balance from the Cadence side
  + `"evm"`: Shows the token balance from the Flow EVM side
  + `"combined"`: Shows the total combined token balance from both sides
* `balanceTokens?: TokenConfig[]` – Optional array of token configurations to display in the balance selector. Each `TokenConfig` requires:
  + `symbol: string` – Token symbol (e.g. "FLOW", "USDC")
  + `name: string` – Full token name
  + Either `vaultIdentifier: string` (for Cadence tokens) or `erc20Address: string` (for EVM tokens)
* `profileConfig?: ProfileConfig` – Optional configuration for the profile display:
  + `scheduledTransactions.show?: boolean` – Whether to show the scheduled transactions tab (default: `false`)
  + `scheduledTransactions.filterHandlerTypes?: string[]` – Optional array of handler type identifiers to filter displayed transactions
* `className?: string` – Optional custom CSS class
* `style?: React.CSSProperties` – Optional inline styles

WalletConnect Support

To enable WalletConnect as a wallet option, add your registered project ID to the `walletconnectProjectId` field in your `FlowProvider` config.

`_10

import { Profile } from "@onflow/react-sdk"

_10

_10

<Profile

_10

balanceType="combined"

_10

onDisconnect={() => console.log("User disconnected")}

_10

/>`

---

### `TransactionButton`[​](#transactionbutton "Direct link to transactionbutton")

Button component for executing Flow transactions with built-in loading states and global transaction management.

[Open in Playground →](https://react.flow.com/#transactionbutton)

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

#### Live Demo[​](#live-demo-1 "Direct link to Live Demo")



---

### `TransactionDialog`[​](#transactiondialog "Direct link to transactiondialog")

Dialog component for real-time transaction status updates.

[Open in Playground →](https://react.flow.com/#transactiondialog)

**Props:**

* `open: boolean` – Whether the dialog is open
* `onOpenChange: (open: boolean) => void` – Callback to open/close dialog
* `txId?: string` – Optional Flow transaction ID or scheduled transaction ID to track
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

#### Live Demo[​](#live-demo-2 "Direct link to Live Demo")



---

### `TransactionLink`[​](#transactionlink "Direct link to transactionlink")

Link to the block explorer with the appropriate network scoped to transaction ID or scheduled transaction ID.

[Open in Playground →](https://react.flow.com/#transactionlink)

**Props:**

* `txId: string` – The transaction ID or scheduled transaction ID to link to
* `variant?: ButtonProps["variant"]` – Optional button variant (defaults to `"link"`)

`_10

import { TransactionLink } from "@onflow/react-sdk"

_10

_10

<TransactionLink txId="your-tx-id" />`

#### Live Demo[​](#live-demo-3 "Direct link to Live Demo")



---

### `NftCard`[​](#nftcard "Direct link to nftcard")

A component for rendering a NFT with image, name, description, collection details, traits and external links. Features include loading states, error handling, dark mode support and optional custom actions.

[Open in Playground →](https://react.flow.com/#nftcard)

**Props:**

* `accountAddress: string` – The Flow account address that owns the NFT
* `tokenId: string | number` – The ID of the NFT
* `publicPathIdentifier: string` – The public path identifier for the NFT collection (e.g., "A.0b2a3299cc857e29.TopShot.Collection")
* `showTraits?: boolean` – Whether to display NFT traits/attributes (default: `false`). Shows up to 4 traits with a button to view all
* `showExtra?: boolean` – Whether to display additional information like serial number, rarity, and external links (default: `false`)
* `actions?: NftCardAction[]` – Optional array of custom action buttons displayed in a dropdown menu. Each action requires:
  + `title: string` – Display text for the action
  + `onClick: () => Promise<void> | void` – Handler function called when action is clicked
* `className?: string` – Optional custom CSS class
* `style?: React.CSSProperties` – Optional inline styles

`_23

import { NftCard } from "@onflow/react-sdk"

_23

_23

<NftCard

_23

accountAddress="0x1234567890abcdef"

_23

tokenId="12345"

_23

publicPathIdentifier="A.0b2a3299cc857e29.TopShot.Collection"

_23

showTraits={true}

_23

showExtra={true}

_23

actions={[

_23

{

_23

title: "Transfer NFT",

_23

onClick: async () => {

_23

// Handle transfer logic

_23

}

_23

},

_23

{

_23

title: "List for Sale",

_23

onClick: async () => {

_23

// Handle listing logic

_23

}

_23

}

_23

]}

_23

/>`

---

### `ScheduledTransactionList`[​](#scheduledtransactionlist "Direct link to scheduledtransactionlist")

A component for displaying scheduled transactions for a Flow account. Shows transaction metadata including thumbnails, descriptions, priority, scheduled time, execution effort, fees and provides an optional transaction cancellation functionality.

[Open in Playground →](https://react.flow.com/#scheduledtransactionlist)

**Props:**

* `address: string` – The Flow account address to fetch scheduled transactions for
* `filterHandlerTypes?: string[]` – Optional array of handler type identifiers to filter which transactions are displayed. Only transactions with matching `handlerTypeIdentifier` will be shown
* `cancelEnabled?: boolean` – Whether to show the cancel button for transactions (default: `true`)
* `className?: string` – Optional custom CSS class
* `style?: React.CSSProperties` – Optional inline styles
* `flowClient?: UseFlowScheduledTransactionListArgs["flowClient"]` – Optional custom Flow client instance

`_10

import { ScheduledTransactionList } from "@onflow/react-sdk"

_10

_10

<ScheduledTransactionList

_10

address="0x1234567890abcdef"

_10

filterHandlerTypes={[

_10

"A.1234.MyContract.Handler",

_10

"A.5678.OtherContract.Handler"

_10

]}

_10

cancelEnabled={true}

_10

/>`

---

## Theming[​](#theming "Direct link to Theming")

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

## Dark Mode[​](#dark-mode "Direct link to Dark Mode")

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

#### Notes[​](#notes "Direct link to Notes")

* The kit does **not** automatically follow system preferences or save user choices. You are responsible for managing and passing the correct `darkMode` value.
* All kit components will automatically apply the correct Tailwind `dark:` classes based on the `darkMode` prop.
* For best results, ensure your app's global theme and the kit's `darkMode` prop are always in sync.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/tools/react-sdk/components.md)

Last updated on **Nov 26, 2025** by **Jordan Ribbink**

[Previous

Hooks](/build/tools/react-sdk/hooks)[Next

Flow Emulator](/build/tools/emulator)

###### Rate this page

😞😐😊

Copy as Markdown

* [Components](#components)
  + [`Connect`](#connect)+ [`Profile`](#profile)+ [`TransactionButton`](#transactionbutton)+ [`TransactionDialog`](#transactiondialog)+ [`TransactionLink`](#transactionlink)+ [`NftCard`](#nftcard)+ [`ScheduledTransactionList`](#scheduledtransactionlist)* [Theming](#theming)
    + [How Theming Works](#how-theming-works)* [Dark Mode](#dark-mode)
      + [How Dark Mode Works](#how-dark-mode-works)

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