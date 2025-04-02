# Source: https://developers.flow.com/build/guides/mobile/react-native-quickstart

React Native Development | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/clients)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Why Flow](/build/flow)
* [Differences vs. EVM](/build/differences-vs-evm)
* [Getting Started](/build/getting-started/contract-interaction)
* [Flow Protocol](/build/basics/blocks)
* [App Architecture](/build/app-architecture)
* [Writing and Deploying Smart Contracts](/build/learn-cadence)
* [Advanced Concepts](/build/advanced-concepts/account-abstraction)
* [Guides](/build/guides/account-linking)

  + [Account Linking (FLIP 72)](/build/guides/account-linking)
  + [Account Linking With NBA Top Shot](/build/guides/account-linking-with-dapper)
  + [More Guides](/build/guides/more-guides)
  + [Creating an NFT Contract](/build/guides/nft)
  + [Creating a Fungible Token](/build/guides/fungible-token)
  + [Building on Mobile](/build/guides/mobile/overview)

    - [Overview](/build/guides/mobile/overview)
    - [Build a Walletless Mobile App (PWA)](/build/guides/mobile/walletless-pwa)
    - [IOS Development](/build/guides/mobile/ios-quickstart)
    - [React Native Development](/build/guides/mobile/react-native-quickstart)
* [Core Smart Contracts](/build/core-contracts)
* [Explore More](/build/explore-more)

* Guides
* Building on Mobile
* React Native Development

On this page

# React Native Development

**Last Updated:** January 11th 2022

> **Note**: This page will walk you through a very bare bones project to get started building a web3 dapp using the Flow Client Library (FCL). If you are looking for a clonable repo, Flow community members have created quickstart templates for different JavaScript frameworks (e.g. [Next.js](https://github.com/muttoni/fcl-nextjs-quickstart), [SvelteKit](https://github.com/muttoni/fcl-sveltekit-quickstart), [Nuxt](https://github.com/bluesign/nuxt3-fcl)). You can consult the complete list [here](https://github.com/ph0ph0/Get-The-Flow-Down#fcl).

## Introduction[​](#introduction "Direct link to Introduction")

FCL-JS is the easiest way to start building decentralized applications. FCL (aka Flow Client Library) wraps much of the logic you'd have to write yourself on other blockchains. Follow this quick start and you'll have a solid overview of how to build a shippable dapp on Flow.

We're going to make an assumption that you know or understand React; however, the concepts should be easy to understand and transfer to another framework. While this tutorial will make use of Cadence (Flow's smart contract language), you do not need to know it. Instead, we recommend later diving into [learning the Cadence language](https://cadence-lang.org/docs/language/) once you've gotten the core FCL concepts down.

In this tutorial, we are going to interact with an existing smart contract on Flow's testnet known as the [Profile Contract](https://testnet.flowdiver.io/contract/A.ba1132bc08f82fe2.Profile). Using this contract, we will create a new profile and edit the profile information, both via a wallet. In order to do this, the FCL concepts we'll cover are:

* [Installation](#installation)
* [Configuration](#configuration)
* [Authentication](#authentication)
* [Querying the Blockchain](#querying-the-blockchain)
* [Initializing an Account](#initializing-an-account)
* [Mutating the Blockchain](#mutating-the-blockchain)

And if you ever have any questions we're always happy to help on [Discord](https://discord.gg/flowblockchain). There are also links at the end of this article for diving deeper into building on Flow.

## Installation[​](#installation "Direct link to Installation")

The first step is to generate a React app using Next.js and [create-expo-app](https://docs.expo.dev/get-started/create-a-project/). From your terminal, run the following:

`_10

npx create-expo-app flow-react-native

_10

cd flow-react-native`

Next, install FCL so we can use it in our app.

`_10

npm install @onflow/fcl@alpha @react-native-async-storage/async-storage expo-web-browser --save`

Now run the app using the following command in your terminal.

`_10

npm run start`

You should now see your app running.

## Configuration[​](#configuration "Direct link to Configuration")

Now that your app is running, you can configure FCL. Within the main project directory, create a folder called `flow` and create a file called `config.js`. This file will contain configuration information for FCL, such as what Access Node and wallet discovery endpoint to use (e.g. testnet or a local emulator). Add the following contents to the file:

**Note**: These values are required to use FCL with your app.

> **Create file:** `./flow/config.js`

./flow/config.js

`_10

import { config } from "@onflow/fcl";

_10

_10

config({

_10

"accessNode.api": "https://rest-testnet.onflow.org", // Mainnet: "https://rest-mainnet.onflow.org"

_10

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn", // Mainnet: "https://fcl-discovery.onflow.org/authn"

_10

"discovery.authn.endpoint": "https://fcl-discovery.onflow.org/api/testnet/authn", // Mainnet: "https://fcl-discovery.onflow.org/api/authn"

_10

})`

📣 **Tip**: It's recommend to replace these values with environment variables for easy deployments across different environments like development/production or Testnet/Mainnet.

* The `accessNode.api` key specifies the address of a Flow access node. Flow provides these, but in the future access to Flow may be provided by other 3rd parties, through their own access nodes.
* `discovery.wallet` and `discovery.authn.endpoint` are addresses that point to a service that lists FCL compatible wallets. Flow's FCL Discovery service is a service that FCL wallet providers can be added to, and be made 'discoverable' to any application that uses the `discovery.wallet` and `discovery.authn.endpoint`.

> Learn more about [configuring Discovery](/tools/clients/fcl-js/discovery) or [setting configuration values](/tools/clients/fcl-js/api#setting-configuration-values).

> If you are running a Wallet Discovery locally and want to use it in the React Native app, change `https://fcl-discovery.onflow.org/` to `http://<LOCAL_IP_ADDRESS>:<PORT>/`
> For Example:
> using local [Wallet Discovery](/tools/clients/fcl-js/discovery) and local [Dev Wallet](/tools/flow-dev-wallet):
>
> ./flow/config.js
>
> `_10
>
> import { config } from "@onflow/fcl";
>
> _10
>
> _10
>
> config({
>
> _10
>
> ...
>
> _10
>
> "discovery.wallet": "http://10.0.0.1:3002/local/authn",
>
> _10
>
> "discovery.authn.endpoint": "http://10.0.0.1:3002/api/local/authn",
>
> _10
>
> ...
>
> _10
>
> })`

The main screen for React Native apps is located in `./App.js` or in `./App.tsx`. So let's finish configuring our dapp by going in the root directory and importing the config file into the top of our `App.js` file. We'll then swap out the default component in `App.js` to look like this:

> **Replace file:** `./App.js`

./App.js

`_21

import { StatusBar } from 'expo-status-bar';

_21

import { StyleSheet, Text, View } from 'react-native';

_21

import "./flow/config";

_21

_21

export default function App() {

_21

return (

_21

<View style={styles.container}>

_21

<Text>Open up App.js to start working on your app!</Text>

_21

<StatusBar style="auto" />

_21

</View>

_21

);

_21

}

_21

_21

const styles = StyleSheet.create({

_21

container: {

_21

flex: 1,

_21

backgroundColor: '#fff',

_21

alignItems: 'center',

_21

justifyContent: 'center',

_21

},

_21

});`

Now we're ready to start talking to Flow!

## Authentication[​](#authentication "Direct link to Authentication")

To authenticate a user, you'll need to render a `ServiceDiscovery` component provided by `fcl-react-native`. Alternatively you can build your own component using `useServiceDiscovery`.

Unauthenticate is as simple as calling `fcl.unauthenticate()`. Once authenticated, FCL sets an object called `fcl.currentUser` which exposes methods for watching changes in user data, signing transactions, and more. For more information on the `currentUser`, read more [here](/tools/clients/fcl-js/api#current-user).

Let's add in a few components and buttons buttons for sign up/login and also subscribe to changes on the `currentUser`. When the user is updated (which it will be after authentication), we'll set the user state in our component to reflect this. To demonstrate user authenticated sessions, we'll conditionally render a component based on if the user is or is not logged in.

This is what your file should look like now:

> **Replace file:** `./App.js`

./App.js

`_42

import { Text, View, Button } from 'react-native';

_42

import "./flow/config";

_42

_42

import { useState, useEffect } from "react";

_42

import * as fcl from "@onflow/fcl/dist/fcl-react-native";

_42

_42

export default function App() {

_42

_42

const [user, setUser] = useState({loggedIn: null})

_42

_42

useEffect(() => fcl.currentUser.subscribe(setUser), [])

_42

_42

const AuthedState = () => {

_42

return (

_42

<View>

_42

<Text>Address: {user?.addr ?? "No Address"}</Text>

_42

<Button onPress={fcl.unauthenticate} title='Log Out'/>

_42

</View>

_42

)

_42

}

_42

_42

if (user.loggedIn) {

_42

return <View style={styles.container}>

_42

<Text>Flow App</Text>

_42

<AuthedState />

_42

<StatusBar style="auto" />

_42

</View>

_42

}

_42

_42

return (

_42

<fcl.ServiceDiscovery fcl={fcl}/>

_42

)

_42

}

_42

_42

const styles = StyleSheet.create({

_42

container: {

_42

flex: 1,

_42

backgroundColor: '#fff',

_42

alignItems: 'center',

_42

justifyContent: 'center',

_42

},

_42

});`

You should now be able to log in or sign up a user and unauthenticate them. Upon logging in or signing up your users will see a popup where they can choose between wallet providers. Let's select the [Blocto wallet](https://blocto.portto.io/) for this example to create an account. Upon completing authentication, you'll see the component change and the user's wallet address appear on the screen if you've completed this properly.

## Querying the Blockchain[​](#querying-the-blockchain "Direct link to Querying the Blockchain")

One of the main things you'll often need to do when building a dapp is query the Flow blockchain and the smart contracts deployed on it for data. Since smart contracts will live on both Testnet and Mainnet, let's put the account address where the smart contract lives into the configuration (remember, it's recommended that you change this later to use environment variables). Let's also give it a key of `Profile` and prefix it with `0x` so that the final key is `0xProfile`. The prefix is important because it tells FCL to pull the corresponding addresses needed from the configuration value.

> **Replace file:** `./flow/config.js`

./flow/config.js

`_10

import { config } from "@onflow/fcl";

_10

_10

config({

_10

"accessNode.api": "https://rest-testnet.onflow.org", // Mainnet: "https://rest-mainnet.onflow.org"

_10

"discovery.wallet": "https://fcl-discovery.onflow.org/testnet/authn", // Mainnet: "https://fcl-discovery.onflow.org/authn"

_10

"discovery.authn.endpoint": "https://fcl-discovery.onflow.org/api/testnet/authn",

_10

"0xProfile": "0xba1132bc08f82fe2" // The account address where the Profile smart contract lives on Testnet

_10

})`

If you want to see the on chain smart contract we'll be speaking with next, you can view the [Profile Contract](https://testnet.flowdiver.io/contract/A.ba1132bc08f82fe2.Profile) source code but again for this tutorial it's not necessary you understand it.

**First, lets query the contract to see what the user's profile name is.**

A few things need to happen in order to do that:

1. We need to import the contract and pass it the user's account address as an argument.
2. Execute the script using `fcl.query`.
3. Set the result of the script to the app state in React so we can display the profile name in our browser.
4. Display "No Profile" if one was not found.

Take a look at the new code. We'll explain each new piece as we go. Remember, the cadence code is a separate language from JavaScript used to write smart contracts, so you don't need to spend too much time trying to understand it. (Of course, you're more than welcome to, if you want to!)

> **Replace file:** `./App.js`

./App.js

`_62

import { StatusBar } from 'expo-status-bar';

_62

import { StyleSheet, Text, View, Button } from 'react-native';

_62

import { useEffect, useState } from 'react';

_62

import './flow/config'

_62

_62

import * as fcl from "@onflow/fcl/dist/fcl-react-native";

_62

_62

export default function App() {

_62

_62

const [user, setUser] = useState({loggedIn: null})

_62

const [name, setName] = useState('') // NEW

_62

_62

useEffect(() => fcl.currentUser.subscribe(setUser), [])

_62

_62

// NEW

_62

const sendQuery = async () => {

_62

const profile = await fcl.query({

_62

cadence: `

_62

import Profile from 0xProfile

_62

_62

access(all) fun main(address: Address): Profile.ReadOnly? {

_62

return Profile.read(address)

_62

}

_62

`,

_62

args: (arg, t) => [arg(user.addr, t.Address)]

_62

})

_62

_62

setName(profile?.name ?? 'No Profile')

_62

}

_62

_62

const AuthedState = () => {

_62

return (

_62

<View >

_62

<Text>Address: {user?.addr ?? "No Address"}</Text>{/* NEW */}

_62

<Text>Profile Name: {name ?? "--"}</Text>{/* NEW */}

_62

<Button onPress={sendQuery} title='Send Query'/>{/* NEW */}

_62

<Button onPress={fcl.unauthenticate} title='Log Out'/>

_62

</View>

_62

)

_62

}

_62

_62

if (user.loggedIn) {

_62

return <View style={styles.container}>

_62

<Text>Flow App</Text>

_62

<AuthedState />

_62

<StatusBar style="auto" />

_62

</View>

_62

}

_62

_62

return (

_62

<fcl.ServiceDiscovery fcl={fcl}/>

_62

)

_62

}

_62

_62

const styles = StyleSheet.create({

_62

container: {

_62

flex: 1,

_62

backgroundColor: '#fff',

_62

alignItems: 'center',

_62

justifyContent: 'center',

_62

},

_62

});`

A few things happened. In our `AuthedState` component, we added a button to send a query for the user's profile name and a `Text` to display the result above it. The corresponding `useState` initialization can be seen at the top of the component.

The other thing we did is build out the actual query inside of `sendQuery` method. Let's take a look at it more closely:

`_10

await fcl.query({

_10

cadence: `

_10

import Profile from 0xProfile

_10

_10

access(all) fun main(address: Address): Profile.ReadOnly? {

_10

return Profile.read(address)

_10

}

_10

`,

_10

args: (arg, t) => [arg(user.addr, t.Address)]

_10

});`

Inside the query you'll see we set two things: `cadence` and `args`. Cadence is Flow's smart contract language we mentioned. For this tutorial, when you look at it you just need to notice that it's importing the `Profile` contract from the account we named `0xProfile` earlier in our config file, then also taking an account address, and reading it. That's it until you're ready to [learn more Cadence](https://cadence-lang.org/docs).

In the `args` section, we are simply passing it our user's account address from the user we set in state after authentication and giving it a type of `Address`. For more possible types, [see this reference](/tools/clients/fcl-js/api#ftype).

Go ahead and click the "Send Query" button. You should see "No Profile." That's because we haven't initialized the account yet.

## Initializing an Account[​](#initializing-an-account "Direct link to Initializing an Account")

For the Profile contract to store a Profile in a user's account, it does so by initializing what is called a "resource." A resource is an ownable piece of data and functionality that can live in the user's account storage. This paradigm is known is as "resource-oriented-programming", a principle that is core to Cadence and differentiates its ownership model from other smart contract languages, [read more here](https://cadence-lang.org/docs/#intuiting-ownership-with-resources). Cadence makes it so that resources can only exist in one place at any time, they must be deliberately created, cannot be copied, and if desired, must be deliberately destroyed.

> There's a lot more to resources in Cadence than we'll cover in this guide, so if you'd like to know more, check out [this Cadence intro](https://cadence-lang.org/docs).

To do this resource initialization on an account, we're going to add another function called `initAccount`. Inside of that function, we're going to add some Cadence code which says, *"Hey, does this account have a profile? If it doesn't, let's add one."* We do that using something called a "transaction." Transactions occur when you want to change the state of the blockchain, in this case, some data in a resource, in a specific account. And there is a cost (transaction fee) in order to do that; unlike a query.

That's where we jump back into FCL code. Instead of `query`, we use `mutate` for transactions. And because there is a cost, we need to add a few fields that tell Flow who is proposing the transaction, who is authorizing it, who is paying for it, and how much they're willing to pay for it. Those fields — not surprisingly — are called: `proposer`, `authorizer`, `payer`, and `limit`. For more information on these signatory roles, check out [this doc](/build/basics/transactions#signer-roles).

Let's take a look at what our account initialization function looks like:

`_29

const initAccount = async () => {

_29

const transactionId = await fcl.mutate({

_29

cadence: `

_29

import Profile from 0xProfile

_29

_29

transaction {

_29

prepare(account: auth(Storage, Capabilities) &Account) {

_29

// Only initialize the account if it hasn't already been initialized

_29

if (!Profile.check(account.address)) {

_29

// This creates and stores the profile in the user's account

_29

account.storage.save(<- Profile.new(), to: Profile.privatePath)

_29

_29

// This creates the public capability that lets applications read the profile's info

_29

let newCap = account.capabilities.storage.issue<&Profile.Base>(Profile.privatePath)

_29

_29

account.capabilities.publish(newCap, at: Profile.publicPath)

_29

}

_29

}

_29

}

_29

`,

_29

payer: fcl.authz,

_29

proposer: fcl.authz,

_29

authorizations: [fcl.authz],

_29

limit: 50

_29

})

_29

_29

const transaction = await fcl.tx(transactionId).onceExecuted()

_29

console.log(transaction)

_29

}`

You can see the new fields we talked about. You'll also notice `fcl.authz`. That's shorthand for "use the current user to authorize this transaction", (you could also write it as `fcl.currentUser.authorization`). If you want to learn more about transactions and signing transactions, you can [view the docs here](/build/basics/transactions). For this example, we'll keep it simple with the user being each of these roles.

You'll also notice we are awaiting a response with our transaction data by using the syntax `fcl.tx(transactionId).onceExecuted()`. This will return when the transaction has been executed by an execution node ("soft-finality"). If you want to wait until the transaction is sealed ("hard-finality"), you can use `onceSealed()` instead.

To learn more about the transaction lifecycle, check out [this doc](/build/basics/transactions#transaction-lifecycle).

Now your `index.js` file should look like this (we also added a button for calling the `initAccount` function in the `AuthedState`):

> **Replace file:** `./App.js`

./App.js

`_93

import { StatusBar } from 'expo-status-bar';

_93

import { StyleSheet, Text, View, Button } from 'react-native';

_93

import { useEffect, useState } from 'react';

_93

import './flow/config'

_93

_93

import * as fcl from "@onflow/fcl/dist/fcl-react-native";

_93

_93

export default function App() {

_93

_93

const [user, setUser] = useState({loggedIn: null})

_93

const [name, setName] = useState('')

_93

_93

useEffect(() => fcl.currentUser.subscribe(setUser), [])

_93

_93

const sendQuery = async () => {

_93

const profile = await fcl.query({

_93

cadence: `

_93

import Profile from 0xProfile

_93

_93

access(all) fun main(address: Address): Profile.ReadOnly? {

_93

return Profile.read(address)

_93

}

_93

`,

_93

args: (arg, t) => [arg(user.addr, t.Address)]

_93

})

_93

_93

setName(profile?.name ?? 'No Profile')

_93

}

_93

_93

// NEW

_93

const initAccount = async () => {

_93

const transactionId = await fcl.mutate({

_93

cadence: `

_93

import Profile from 0xProfile

_93

_93

transaction {

_93

prepare(account: auth(Storage, Capabilities) &Account) {

_93

// Only initialize the account if it hasn't already been initialized

_93

if (!Profile.check(account.address)) {

_93

// This creates and stores the profile in the user's account

_93

account.storage.save(<- Profile.new(), to: Profile.privatePath)

_93

_93

// This creates the public capability that lets applications read the profile's info

_93

let newCap = account.capabilities.storage.issue<&Profile.Base>(Profile.privatePath)

_93

_93

account.capabilities.publish(newCap, at: Profile.publicPath)

_93

}

_93

}

_93

}

_93

`,

_93

payer: fcl.authz,

_93

proposer: fcl.authz,

_93

authorizations: [fcl.authz],

_93

limit: 50

_93

})

_93

_93

const transaction = await fcl.tx(transactionId).onceExecuted()

_93

console.log(transaction)

_93

}

_93

_93

const AuthedState = () => {

_93

return (

_93

<View >

_93

<Text>Address: {user?.addr ?? "No Address"}</Text>

_93

<Text>Profile Name: {name ?? "--"}</Text>

_93

<Button onPress={sendQuery} title='Send Query'/>

_93

<Button onPress={initAccount} title='Init Account'/>{/* NEW */}

_93

<Button onPress={fcl.unauthenticate} title='Log Out'/>

_93

</View>

_93

)

_93

}

_93

_93

if (user.loggedIn) {

_93

return <View style={styles.container}>

_93

<Text>Flow App</Text>

_93

<AuthedState />

_93

<StatusBar style="auto" />

_93

</View>

_93

}

_93

_93

return (

_93

<fcl.ServiceDiscovery fcl={fcl}/>

_93

)

_93

}

_93

_93

const styles = StyleSheet.create({

_93

container: {

_93

flex: 1,

_93

backgroundColor: '#fff',

_93

alignItems: 'center',

_93

justifyContent: 'center',

_93

},

_93

});`

Press the "Init Account" button you should see the wallet ask you to approve a transaction. After approving, you will see a transaction response appear in your console (make sure to have that open). It may take a few moments. With the transaction result printed, you can use the `transactionId` to look up the details of the transaction using a [block explorer](https://testnet.flowscan.io/).

## Mutating the Blockchain[​](#mutating-the-blockchain "Direct link to Mutating the Blockchain")

Now that we have the profile initialized, we are going to want to mutate it some more. In this example, we'll use the same smart contract provided to change the profile name.

To do that, we are going to write another transaction that adds some Cadence code which lets us set the name. Everything else looks the same in the following code except for one thing: we'll subscribe to the status changes instead of waiting for it to be sealed after the mutate function returns.

It looks like this:

`_25

const executeTransaction = async () => {

_25

const transactionId = await fcl.mutate({

_25

cadence: `

_25

import Profile from 0xProfile

_25

_25

transaction(name: String) {

_25

prepare(account: auth(BorrowValue) &Account) {

_25

let profileRef = account.borrow<&Profile.Base>(from: Profile.privatePath)

_25

?? panic("The signer does not store a Profile.Base object at the path "

_25

.concat(Profile.privatePath.toString())

_25

.concat(". The signer must initialize their account with this object first!"))

_25

_25

profileRef.setName(name)

_25

}

_25

}

_25

`,

_25

args: (arg, t) => [arg("Flow Developer", t.String)],

_25

payer: fcl.authz,

_25

proposer: fcl.authz,

_25

authorizations: [fcl.authz],

_25

limit: 50

_25

})

_25

_25

fcl.tx(transactionId).subscribe(res => setTransactionStatus(res.status))

_25

}`

Here you can see our argument is "Flow Developer" and at the bottom we've called the `subscribe` method instead of `onceExecuted`.

Let's see how that works inside our whole `index.js` file. But, let's also set the statuses to our React component's state so we can see on screen what state we're in.

> **Replace file:** `./App.js`

./App.js

`_122

import { StatusBar } from 'expo-status-bar';

_122

import { StyleSheet, Text, View, Button } from 'react-native';

_122

import { useEffect, useState } from 'react';

_122

import './flow/config'

_122

_122

import * as fcl from "@onflow/fcl/dist/fcl-react-native";

_122

_122

export default function App() {

_122

_122

const [user, setUser] = useState({loggedIn: null})

_122

const [name, setName] = useState('')

_122

const [transactionStatus, setTransactionStatus] = useState(null) // NEW

_122

_122

useEffect(() => fcl.currentUser.subscribe(setUser), [])

_122

_122

const sendQuery = async () => {

_122

const profile = await fcl.query({

_122

cadence: `

_122

import Profile from 0xProfile

_122

_122

access(all) fun main(address: Address): Profile.ReadOnly? {

_122

return Profile.read(address)

_122

}

_122

`,

_122

args: (arg, t) => [arg(user.addr, t.Address)]

_122

})

_122

_122

setName(profile?.name ?? 'No Profile')

_122

}

_122

_122

const initAccount = async () => {

_122

const transactionId = await fcl.mutate({

_122

cadence: `

_122

import Profile from 0xProfile

_122

_122

transaction {

_122

prepare(account: auth(Storage, Capabilities) &Account) {

_122

// Only initialize the account if it hasn't already been initialized

_122

if (!Profile.check(account.address)) {

_122

// This creates and stores the profile in the user's account

_122

account.storage.save(<- Profile.new(), to: Profile.storagePath)

_122

_122

// This creates the public capability that lets applications read the profile's info

_122

let newCap = account.capabilities.storage.issue<&Profile.Base>(Profile.privatePath)

_122

_122

account.capabilities.publish(newCap, at: Profile.publicPath)

_122

}

_122

}

_122

}

_122

`,

_122

payer: fcl.authz,

_122

proposer: fcl.authz,

_122

authorizations: [fcl.authz],

_122

limit: 50

_122

})

_122

_122

const transaction = await fcl.tx(transactionId).onceExecuted()

_122

console.log(transaction)

_122

}

_122

_122

// NEW

_122

const executeTransaction = async () => {

_122

const transactionId = await fcl.mutate({

_122

cadence: `

_122

import Profile from 0xProfile

_122

_122

transaction(name: String) {

_122

prepare(account: auth(BorrowValue) &Account) {

_122

let profileRef = account.storage.borrow<&Profile.Base>(from: Profile.privatePath)

_122

?? panic("The signer does not store a Profile.Base object at the path "

_122

.concat(Profile.privatePath.toString())

_122

.concat(". The signer must initialize their account with this object first!"))

_122

_122

profileRef.setName(name)

_122

}

_122

}

_122

`,

_122

args: (arg, t) => [arg("Flow Developer", t.String)],

_122

payer: fcl.authz,

_122

proposer: fcl.authz,

_122

authorizations: [fcl.authz],

_122

limit: 50

_122

})

_122

_122

fcl.tx(transactionId).subscribe(res => setTransactionStatus(res.status))

_122

}

_122

_122

const AuthedState = () => {

_122

return (

_122

<View >

_122

<Text>Address: {user?.addr ?? "No Address"}</Text>

_122

<Text>Profile Name: {name ?? "--"}</Text>

_122

<Text>Transaction Status: {transactionStatus ?? "--"}</Text>{/* NEW */}

_122

<Button onPress={sendQuery} title='Send Query'/>

_122

<Button onPress={initAccount} title='Init Account'/>{/* NEW */}

_122

<Button onPress={executeTransaction} title='Execute Transaction'/>{/* NEW */}

_122

<Button onPress={fcl.unauthenticate} title='Log Out'/>

_122

</View>

_122

)

_122

}

_122

_122

if (user.loggedIn) {

_122

return <View style={styles.container}>

_122

<Text>Flow App</Text>

_122

<AuthedState />

_122

<StatusBar style="auto" />

_122

</View>

_122

}

_122

_122

return (

_122

<fcl.ServiceDiscovery fcl={fcl}/>

_122

)

_122

}

_122

_122

const styles = StyleSheet.create({

_122

container: {

_122

flex: 1,

_122

backgroundColor: '#fff',

_122

alignItems: 'center',

_122

justifyContent: 'center',

_122

},

_122

});`

Now if you click the "Execute Transaction" button you'll see the statuses update next to "Transaction Status." When you see "4" that means it's sealed! Status code meanings [can be found here](/tools/clients/fcl-js/api#transaction-statuses).
If you query the account profile again, "Profile Name:" should now display "Flow Developer".

That's it! You now have a shippable Flow dapp that can auth, query, init accounts, and mutate the chain. This is just the beginning. There is so much more to know. We have a lot more resources to help you build. To dive deeper, here are a few good places for taking the next steps:

**Cadence**

* [Cadence Playground Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Hello World Video](https://www.youtube.com/watch?v=pRz7EzrWchs)
* [Why Cadence?](https://www.onflow.org/post/flow-blockchain-cadence-programming-language-resources-assets)

**Full Stack NFT Marketplace Example**

* [Beginner Example: CryptoDappy](https://github.com/bebner/crypto-dappy)

**More FCL**

* [FCL API Quick Reference](/tools/clients/fcl-js/api)
* [More on Scripts](/tools/clients/fcl-js/scripts)
* [More on Transactions](/tools/clients/fcl-js/transactions)
* [User Signatures](/tools/clients/fcl-js/user-signatures)
* [Proving Account Ownership](/tools/clients/fcl-js/proving-authentication)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/build/guides/mobile/react-native-quickstart.md)

Last updated on **Mar 28, 2025** by **Jordan Ribbink**

[Previous

IOS Development](/build/guides/mobile/ios-quickstart)[Next

Core Smart Contracts](/build/core-contracts)

###### Rate this page

😞😐😊

* [Introduction](#introduction)
* [Installation](#installation)
* [Configuration](#configuration)
* [Authentication](#authentication)
* [Querying the Blockchain](#querying-the-blockchain)
* [Initializing an Account](#initializing-an-account)
* [Mutating the Blockchain](#mutating-the-blockchain)

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
* [Flowscan Mainnet](https://flowdscan.io/)
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