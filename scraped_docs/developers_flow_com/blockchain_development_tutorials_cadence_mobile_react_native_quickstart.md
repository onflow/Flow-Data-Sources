# Source: https://developers.flow.com/blockchain-development-tutorials/cadence/mobile/react-native-quickstart

React Native Development | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          + [Getting Started with Cadence](/blockchain-development-tutorials/cadence/getting-started)

            + [Cadence Advantages](/blockchain-development-tutorials/cadence/cadence-advantages)

              + [Account Linking](/blockchain-development-tutorials/cadence/account-management)

                + [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)

                  - [IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)- [React Native Development](/blockchain-development-tutorials/cadence/mobile/react-native-quickstart)- [Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)+ [Fork Testing](/blockchain-development-tutorials/cadence/fork-testing)* [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Cadence Tutorials](/blockchain-development-tutorials/cadence)* [Mobile Development on Flow](/blockchain-development-tutorials/cadence/mobile)* React Native Development

On this page

# React Negative Development

**Last Updated:** January 11th 2022

info

This page will walk you through a very bare bones project to get started building a web3 dapp using the Flow Client Library (FCL). If you want a clonable repo, Flow community members created quickstart templates for different JavaScript frameworks (for example, [Next.js](https://github.com/muttoni/fcl-nextjs-quickstart), [SvelteKit](https://github.com/muttoni/fcl-sveltekit-quickstart), [Nuxt](https://github.com/bluesign/nuxt3-fcl)). You can consult the complete list [here](https://github.com/ph0ph0/Get-The-Flow-Down#fcl).

FCL-JS is the easiest way to start building decentralized applications. Flow Client Library (FCL) wraps much of the logic you'd have to write yourself on other blockchains. Follow this quick start and you'll have a solid overview of how to build a shippable dapp on Flow.

We're going to make an assumption that you know or understand React; however, the concepts should be easy to understand and transfer to another framework. While this tutorial uses Cadence (Flow's smart contract language), you do not need to know it. Instead, we recommend that you later [learn the Cadence language](https://cadence-lang.org/docs/language/) after you've gotten the core FCL concepts down.

In this tutorial, we are going to interact with an current smart contract on Flow's testnet known as the [Profile Contract](https://testnet.flowdiver.io/contract/A.ba1132bc08f82fe2.Profile). With this contract, we will create a new profile and edit the profile information, both via a wallet. To do this, the FCL concepts we'll cover are:

* [Installation](#installation)
* [Configuration](#configuration)
* [Authentication](#authentication)
* [Querying the Blockchain](#querying-the-blockchain)
* [Initializing an Account](#initializing-an-account)
* [Mutating the Blockchain](#mutating-the-blockchain)

If you ever have any questions, we're always happy to help on [Discord](https://discord.gg/flowblockchain). There are also links at the end of this article for diving deeper into how to build on Flow.

## Installation[​](#installation "Direct link to Installation")

The first step is to generate a React app using Next.js and [create-expo-app](https://docs.expo.dev/get-started/create-a-project/). From your terminal, run the following:

`_10

npx create-expo-app flow-react-native

_10

cd flow-react-native`

Next, install FCL so we can use it in our app.

`_10

npm install @onflow/fcl@alpha @react-native-async-storage/async-storage expo-web-browser --save`

Now run the app with the following command in your terminal.

`_10

npm run start`

Your app is now running.

## Configuration[​](#configuration "Direct link to Configuration")

Now that your app is running, you can configure FCL. Within the main project directory, create a folder called `flow` and create a file called `config.js`. This file contains configuration information for FCL, such as what Access Node and wallet discovery endpoint to use (such as testnet or a local emulator). Add the following contents to the file:

info

These values are required to use FCL with your app.

> **Create file:** `./flow/config.js`

./flow/config.js

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'accessNode.api': 'https://rest-testnet.onflow.org', // Mainnet: "https://rest-mainnet.onflow.org"

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn', // Mainnet: "https://fcl-discovery.onflow.org/authn"

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn', // Mainnet: "https://fcl-discovery.onflow.org/api/authn"

_10

});`

📣 **Tip**: We recommend that you replace these values with environment variables for easy deployments across different environments like development/production or Testnet/Mainnet.

* The `accessNode.api` key specifies the address of a Flow access node. Flow provides these, but in the future, third parties ay provide access to Flow through their own access nodes.
* `discovery.wallet` and `discovery.authn.endpoint` are addresses that point to a service that lists FCL compatible wallets. Flow's FCL Discovery service is a service that FCL wallet providers can be added to, and be made 'discoverable' to any application that uses the `discovery.wallet` and `discovery.authn.endpoint`.

> Learn more about [configuring Discovery](/build/tools/clients/fcl-js/discovery) or [setting configuration values](/build/tools/clients/fcl-js/packages-docs/fcl#setting-configuration-values).

> If you are running a Wallet Discovery locally and want to use it in the React Native app, change `https://fcl-discovery.onflow.org/` to `http://<LOCAL_IP_ADDRESS>:<PORT>/`
> For Example:
> using local [Wallet Discovery](/build/tools/clients/fcl-js/discovery) and local [Dev Wallet](/build/tools/flow-dev-wallet):
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

The main screen for React Native apps is located in `./App.js` or in `./App.tsx`. So, to finish configuring our dApp, let's go into the root directory and import the config file into the top of our `App.js` file. We'll then swap out the default component in `App.js` to look like this:

> **Replace file:** `./App.js`

./App.js

`_21

import { StatusBar } from 'expo-status-bar';

_21

import { StyleSheet, Text, View } from 'react-native';

_21

import './flow/config';

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

To authenticate a user, you'll need to render a `ServiceDiscovery` component provided by `fcl-react-native`. Alternatively, you can build your own component using `useServiceDiscovery`.

Unauthenticate is as simple as calling `fcl.unauthenticate()`. After you're authenticated, FCL sets an object called `fcl.currentUser` which exposes methods to watch for changes in user data, signing transactions, and more.

Let's add in a few components and buttons for sign up, login, and to subscribe to changes on the `currentUser`. When the user updates (which happens after authentication), we'll set the user state in our component to reflect this. To demonstrate user authenticated sessions, we'll conditionally render a component based on if the user is or is not logged in.

This is what your file should look like now:

> **Replace file:** `./App.js`

./App.js

`_41

import { Text, View, Button } from 'react-native';

_41

import './flow/config';

_41

_41

import { useState, useEffect } from 'react';

_41

import * as fcl from '@onflow/fcl/dist/fcl-react-native';

_41

_41

export default function App() {

_41

const [user, setUser] = useState({ loggedIn: null });

_41

_41

useEffect(() => fcl.currentUser.subscribe(setUser), []);

_41

_41

const AuthedState = () => {

_41

return (

_41

<View>

_41

<Text>Address: {user?.addr ?? 'No Address'}</Text>

_41

<Button onPress={fcl.unauthenticate} title="Log Out" />

_41

</View>

_41

);

_41

};

_41

_41

if (user.loggedIn) {

_41

return (

_41

<View style={styles.container}>

_41

<Text>Flow App</Text>

_41

<AuthedState />

_41

<StatusBar style="auto" />

_41

</View>

_41

);

_41

}

_41

_41

return <fcl.ServiceDiscovery fcl={fcl} />;

_41

}

_41

_41

const styles = StyleSheet.create({

_41

container: {

_41

flex: 1,

_41

backgroundColor: '#fff',

_41

alignItems: 'center',

_41

justifyContent: 'center',

_41

},

_41

});`

You can now log in or sign up a user and unauthenticate them. After your users log in or sign up, they'll see a popup where they can choose between wallet providers. Let's select the [Blocto wallet](https://blocto.portto.io/) for this example to create an account. After you authenticate, you'll see the component change and the user's wallet address appear if you've completed this properly.

## Querying the blockchain[​](#querying-the-blockchain "Direct link to Querying the blockchain")

One of the main things you'll often need to do when building a dApp is query the Flow blockchain and the smart contracts deployed on it for data. Since smart contracts will live on both Testnet and Mainnet, let's put the account address where the smart contract lives into the configuration (remember, we recommend that you change this later to use environment variables). Let's also give it a key of `Profile` and prefix it with `0x` so that the final key is `0xProfile`. The prefix is important because it tells FCL to pull the corresponding addresses needed from the configuration value.

> **Replace file:** `./flow/config.js`

./flow/config.js

`_10

import { config } from '@onflow/fcl';

_10

_10

config({

_10

'accessNode.api': 'https://rest-testnet.onflow.org', // Mainnet: "https://rest-mainnet.onflow.org"

_10

'discovery.wallet': 'https://fcl-discovery.onflow.org/testnet/authn', // Mainnet: "https://fcl-discovery.onflow.org/authn"

_10

'discovery.authn.endpoint':

_10

'https://fcl-discovery.onflow.org/api/testnet/authn',

_10

'0xProfile': '0xba1132bc08f82fe2', // The account address where the Profile smart contract lives on Testnet

_10

});`

If you want to see the on chain smart contract that we'll speak with next, you can view the [Profile Contract](https://testnet.flowdiver.io/contract/A.ba1132bc08f82fe2.Profile) source code but again, for this tutorial, it's not necessary you understand it.

**First, lets query the contract to see what the user's profile name is.**

A few things need to happen to do that:

1. We need to import the contract and pass it the user's account address as an argument.
2. Execute the script with `fcl.query`.
3. Set the result of the script to the app state in React so we can display the profile name in our browser.
4. Display "No Profile" if one wasn't found.

Take a look at the new code. We'll explain each new piece as we go. Remember, the cadence code is a separate language from JavaScript used to write smart contracts, so you don't need to spend too much time trying to understand it. (Of course, you're more than welcome to, if you want to!)

> **Replace file:** `./App.js`

./App.js

`` _64

import { StatusBar } from 'expo-status-bar';

_64

import { StyleSheet, Text, View, Button } from 'react-native';

_64

import { useEffect, useState } from 'react';

_64

import './flow/config';

_64

_64

import * as fcl from '@onflow/fcl/dist/fcl-react-native';

_64

_64

export default function App() {

_64

const [user, setUser] = useState({ loggedIn: null });

_64

const [name, setName] = useState(''); // NEW

_64

_64

useEffect(() => fcl.currentUser.subscribe(setUser), []);

_64

_64

// NEW

_64

const sendQuery = async () => {

_64

const profile = await fcl.query({

_64

cadence: `

_64

import Profile from 0xProfile

_64

_64

access(all) fun main(address: Address): Profile.ReadOnly? {

_64

return Profile.read(address)

_64

}

_64

`,

_64

args: (arg, t) => [arg(user.addr, t.Address)],

_64

});

_64

_64

setName(profile?.name ?? 'No Profile');

_64

};

_64

_64

const AuthedState = () => {

_64

return (

_64

<View>

_64

<Text>Address: {user?.addr ?? 'No Address'}</Text>

_64

{/* NEW */}

_64

<Text>Profile Name: {name ?? '--'}</Text>

_64

{/* NEW */}

_64

<Button onPress={sendQuery} title="Send Query" />

_64

{/* NEW */}

_64

<Button onPress={fcl.unauthenticate} title="Log Out" />

_64

</View>

_64

);

_64

};

_64

_64

if (user.loggedIn) {

_64

return (

_64

<View style={styles.container}>

_64

<Text>Flow App</Text>

_64

<AuthedState />

_64

<StatusBar style="auto" />

_64

</View>

_64

);

_64

}

_64

_64

return <fcl.ServiceDiscovery fcl={fcl} />;

_64

}

_64

_64

const styles = StyleSheet.create({

_64

container: {

_64

flex: 1,

_64

backgroundColor: '#fff',

_64

alignItems: 'center',

_64

justifyContent: 'center',

_64

},

_64

}); ``

A few things happened. In our `AuthedState` component, we added a button to send a query for the user's profile name and a `Text` to display the result above it. The corresponding `useState` initialization appears at the top of the component.

The other thing we did is build out the actual query inside of `sendQuery` method. Let's take a look at it more closely:

`` _10

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

args: (arg, t) => [arg(user.addr, t.Address)],

_10

}); ``

Inside the query, you'll see we set two things: `cadence` and `args`. Cadence is Flow's smart contract language we mentioned. For this tutorial, when you look at it, you just need to notice that it's importing the `Profile` contract from the account we named `0xProfile` earlier in our config file, then also taking an account address, and reading it. That's it until you're ready to [learn more Cadence](https://cadence-lang.org/docs).

In the `args` section, we are simply passing it our user's account address from the user we set in state after authentication and giving it a type of `Address`. For more possible types, [see this reference](/build/tools/clients/fcl-js/packages-docs/types).

Go ahead and click "Send Query". You will see "No Profile." That's because we haven't initialized the account yet.

## Initialize an account[​](#initialize-an-account "Direct link to Initialize an account")

For the Profile contract to store a Profile in a user's account, it initializes what is called a "resource." A resource is an ownable piece of data and functionality that can live in the user's account storage. This paradigm is known is as "resource-oriented-programming", a principle that is core to Cadence and differentiates its ownership model from other smart contract languages, [read more here](https://cadence-lang.org/docs/#intuiting-ownership-with-resources). Cadence makes it so that resources can only exist in one place at any time, they must be deliberately created, cannot be copied, and if desired, must be deliberately destroyed.

> There's a lot more to resources in Cadence than we'll cover in this guide, so if you'd like to know more, check out [this Cadence intro](https://cadence-lang.org/docs).

To do this resource initialization on an account, we're going to add another function called `initAccount`. Inside of that function, we're going to add some Cadence code which says, *"Hey, does this account have a profile? If it doesn't, let's add one."* We do that with something called a "transaction." Transactions occur when you want to change the state of the blockchain, in this case, some data in a resource, in a specific account. And there is a cost (transaction fee) in order to do that; unlike a query.

That's where we jump back into FCL code. Instead of `query`, we use `mutate` for transactions. And because there is a cost, we need to add a few fields that tell Flow who is proposing the transaction, who is authorizing it, who is paying for it, and how much they're willing to pay for it. Those fields — not surprisingly — are called: `proposer`, `authorizer`, `payer`, and `limit`. For more information on these signatory roles, check out [this doc](/build/cadence/basics/transactions#signer-roles).

Let's take a look at what our account initialization function looks like:

`` _29

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

limit: 50,

_29

});

_29

_29

const transaction = await fcl.tx(transactionId).onceExecuted();

_29

console.log(transaction);

_29

}; ``

You can see the new fields we talked about. You'll also notice `fcl.authz`. That's shorthand for "use the current user to authorize this transaction", (you could also write it as `fcl.currentUser.authorization`). If you want to learn more about transactions and signing transactions, you can [view the docs here](/build/cadence/basics/transactions). For this example, we'll keep it simple with the user being each of these roles.

You'll also notice we are awaiting a response with our transaction data by using the syntax `fcl.tx(transactionId).onceExecuted()`. This returns when an execution node completes the transaction ("soft-finality"). If you want to wait until the transaction is sealed ("hard-finality"), you can use `onceSealed()` instead.

To learn more about the transaction lifecycle, check out [this doc](/build/cadence/basics/transactions#transaction-lifecycle).

Now your `index.js` file looks like this (we also added a button to call the `initAccount` function in the `AuthedState`):

> **Replace file:** `./App.js`

./App.js

`` _93

import { StatusBar } from 'expo-status-bar';

_93

import { StyleSheet, Text, View, Button } from 'react-native';

_93

import { useEffect, useState } from 'react';

_93

import './flow/config';

_93

_93

import * as fcl from '@onflow/fcl/dist/fcl-react-native';

_93

_93

export default function App() {

_93

const [user, setUser] = useState({ loggedIn: null });

_93

const [name, setName] = useState('');

_93

_93

useEffect(() => fcl.currentUser.subscribe(setUser), []);

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

args: (arg, t) => [arg(user.addr, t.Address)],

_93

});

_93

_93

setName(profile?.name ?? 'No Profile');

_93

};

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

limit: 50,

_93

});

_93

_93

const transaction = await fcl.tx(transactionId).onceExecuted();

_93

console.log(transaction);

_93

};

_93

_93

const AuthedState = () => {

_93

return (

_93

<View>

_93

<Text>Address: {user?.addr ?? 'No Address'}</Text>

_93

<Text>Profile Name: {name ?? '--'}</Text>

_93

<Button onPress={sendQuery} title="Send Query" />

_93

<Button onPress={initAccount} title="Init Account" />

_93

{/* NEW */}

_93

<Button onPress={fcl.unauthenticate} title="Log Out" />

_93

</View>

_93

);

_93

};

_93

_93

if (user.loggedIn) {

_93

return (

_93

<View style={styles.container}>

_93

<Text>Flow App</Text>

_93

<AuthedState />

_93

<StatusBar style="auto" />

_93

</View>

_93

);

_93

}

_93

_93

return <fcl.ServiceDiscovery fcl={fcl} />;

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

}); ``

Press "Init Account," and the wallet asks you to approve a transaction. After you approve it, you will see a transaction response appear in your console (make sure to have that open). It may take a few moments. With the transaction result printed, you can use the `transactionId` to look up the details of the transaction using a [block explorer](https://testnet.flowscan.io/).

## Mutating the blockchain[​](#mutating-the-blockchain "Direct link to Mutating the blockchain")

Now that we have the profile initialized, we are going to want to mutate it some more. In this example, we'll use the same smart contract provided to change the profile name.

To do that, we are going to write another transaction that adds some Cadence code which lets us set the name. Everything else looks the same in the following code except for one thing: we'll subscribe to the status changes instead of waiting for it to be sealed after the mutate function returns.

It looks like this:

`` _25

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

args: (arg, t) => [arg('Flow Developer', t.String)],

_25

payer: fcl.authz,

_25

proposer: fcl.authz,

_25

authorizations: [fcl.authz],

_25

limit: 50,

_25

});

_25

_25

fcl.tx(transactionId).subscribe((res) => setTransactionStatus(res.status));

_25

}; ``

Here you can see our argument is "Flow Developer" and at the bottom we've called the `subscribe` method instead of `onceExecuted`.

Let's see how that works inside our whole `index.js` file. But, let's also set the statuses to our React component's state so we can see on screen what state we're in.

> **Replace file:** `./App.js`

./App.js

`` _124

import { StatusBar } from 'expo-status-bar';

_124

import { StyleSheet, Text, View, Button } from 'react-native';

_124

import { useEffect, useState } from 'react';

_124

import './flow/config';

_124

_124

import * as fcl from '@onflow/fcl/dist/fcl-react-native';

_124

_124

export default function App() {

_124

const [user, setUser] = useState({ loggedIn: null });

_124

const [name, setName] = useState('');

_124

const [transactionStatus, setTransactionStatus] = useState(null); // NEW

_124

_124

useEffect(() => fcl.currentUser.subscribe(setUser), []);

_124

_124

const sendQuery = async () => {

_124

const profile = await fcl.query({

_124

cadence: `

_124

import Profile from 0xProfile

_124

_124

access(all) fun main(address: Address): Profile.ReadOnly? {

_124

return Profile.read(address)

_124

}

_124

`,

_124

args: (arg, t) => [arg(user.addr, t.Address)],

_124

});

_124

_124

setName(profile?.name ?? 'No Profile');

_124

};

_124

_124

const initAccount = async () => {

_124

const transactionId = await fcl.mutate({

_124

cadence: `

_124

import Profile from 0xProfile

_124

_124

transaction {

_124

prepare(account: auth(Storage, Capabilities) &Account) {

_124

// Only initialize the account if it hasn't already been initialized

_124

if (!Profile.check(account.address)) {

_124

// This creates and stores the profile in the user's account

_124

account.storage.save(<- Profile.new(), to: Profile.storagePath)

_124

_124

// This creates the public capability that lets applications read the profile's info

_124

let newCap = account.capabilities.storage.issue<&Profile.Base>(Profile.privatePath)

_124

_124

account.capabilities.publish(newCap, at: Profile.publicPath)

_124

}

_124

}

_124

}

_124

`,

_124

payer: fcl.authz,

_124

proposer: fcl.authz,

_124

authorizations: [fcl.authz],

_124

limit: 50,

_124

});

_124

_124

const transaction = await fcl.tx(transactionId).onceExecuted();

_124

console.log(transaction);

_124

};

_124

_124

// NEW

_124

const executeTransaction = async () => {

_124

const transactionId = await fcl.mutate({

_124

cadence: `

_124

import Profile from 0xProfile

_124

_124

transaction(name: String) {

_124

prepare(account: auth(BorrowValue) &Account) {

_124

let profileRef = account.storage.borrow<&Profile.Base>(from: Profile.privatePath)

_124

?? panic("The signer does not store a Profile.Base object at the path "

_124

.concat(Profile.privatePath.toString())

_124

.concat(". The signer must initialize their account with this object first!"))

_124

_124

profileRef.setName(name)

_124

}

_124

}

_124

`,

_124

args: (arg, t) => [arg('Flow Developer', t.String)],

_124

payer: fcl.authz,

_124

proposer: fcl.authz,

_124

authorizations: [fcl.authz],

_124

limit: 50,

_124

});

_124

_124

fcl.tx(transactionId).subscribe((res) => setTransactionStatus(res.status));

_124

};

_124

_124

const AuthedState = () => {

_124

return (

_124

<View>

_124

<Text>Address: {user?.addr ?? 'No Address'}</Text>

_124

<Text>Profile Name: {name ?? '--'}</Text>

_124

<Text>Transaction Status: {transactionStatus ?? '--'}</Text>

_124

{/* NEW */}

_124

<Button onPress={sendQuery} title="Send Query" />

_124

<Button onPress={initAccount} title="Init Account" />

_124

{/* NEW */}

_124

<Button onPress={executeTransaction} title="Execute Transaction" />

_124

{/* NEW */}

_124

<Button onPress={fcl.unauthenticate} title="Log Out" />

_124

</View>

_124

);

_124

};

_124

_124

if (user.loggedIn) {

_124

return (

_124

<View style={styles.container}>

_124

<Text>Flow App</Text>

_124

<AuthedState />

_124

<StatusBar style="auto" />

_124

</View>

_124

);

_124

}

_124

_124

return <fcl.ServiceDiscovery fcl={fcl} />;

_124

}

_124

_124

const styles = StyleSheet.create({

_124

container: {

_124

flex: 1,

_124

backgroundColor: '#fff',

_124

alignItems: 'center',

_124

justifyContent: 'center',

_124

},

_124

}); ``

Now if you click "Execute Transaction," you'll see the statuses update next to "Transaction Status." When you see "4" that means it's sealed! Status code meanings [can be found here](/build/tools/clients/fcl-js/packages-docs/types).
If you query the account profile again, "Profile Name:" should now display "Flow Developer".

That's it! You now have a shippable Flow dapp that can auth, query, init accounts, and mutate the chain. This is just the beginning. There is so much more to know. We have a lot more resources to help you build. To dive deeper, here are a few good places for taking the next steps:

**Cadence**

* [Cadence Playground Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Hello World Video](https://www.youtube.com/watch?v=pRz7EzrWchs)
* [Why Cadence?](https://www.flow.com/post/flow-blockchain-cadence-programming-language-resources-assets)

**Full Stack NFT Marketplace Example**

* [Beginner Example: CryptoDappy](https://github.com/bebner/crypto-dappy)

**More FCL**

* [More on Scripts](/build/tools/clients/fcl-js/scripts)
* [More on Transactions](/build/tools/clients/fcl-js/transactions)
* [User Signatures](/build/tools/clients/fcl-js/user-signatures)
* [Proving Account Ownership](/build/tools/clients/fcl-js/proving-authentication)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/cadence/mobile/react-native-quickstart.md)

Last updated on **Nov 4, 2025** by **cshannon1218**

[Previous

IOS Development](/blockchain-development-tutorials/cadence/mobile/ios-quickstart)[Next

Build a Walletless Mobile App (PWA)](/blockchain-development-tutorials/cadence/mobile/walletless-pwa)

###### Rate this page

😞😐😊

Copy as Markdown

* [Installation](#installation)* [Configuration](#configuration)* [Authentication](#authentication)* [Querying the blockchain](#querying-the-blockchain)* [Initialize an account](#initialize-an-account)* [Mutating the blockchain](#mutating-the-blockchain)

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