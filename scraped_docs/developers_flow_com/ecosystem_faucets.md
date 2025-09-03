# Source: https://developers.flow.com/ecosystem/faucets

Faucets | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Ecosystem](/ecosystem)
* [Developer Support Hub](/ecosystem/developer-support-hub)
* [Wallets](/ecosystem/wallets)
* [Flow Block Explorers](/ecosystem/block-explorers)
* [Data Indexers](/ecosystem/data-indexers)
* [Developer Profile](/ecosystem/developer-profile)
* [DeFi & Liquidity](/ecosystem/defi-liquidity)
* [Bridges](/ecosystem/bridges)
* [Collectibles & NFTs](/ecosystem/collectibles)
* [Community Projects](/ecosystem/projects)
* [Faucets](/ecosystem/faucets)
* [Hackathons and Events](/ecosystem/Hackathons and Events)
* [Auditors](/ecosystem/auditors)
* [Ecosystem Overview](/ecosystem/overview)

* Faucets

On this page

# Faucets

Network Faucets provide free Flow tokens for testing purposes, functioning like taps that dispense tokens. They are valuable tools for experimenting with Flow without the need to purchase tokens.

## Flow Faucet[​](#flow-faucet "Direct link to Flow Faucet")

[Flow Faucet](https://faucet.flow.com/fund-account) is a dedicated tool that provides a seamless way to acquire small amounts of Flow tokens for testing and development purposes on the Flow blockchain's testnet environment.

### Supported Networks[​](#supported-networks "Direct link to Supported Networks")

* [Testnet](https://faucet.flow.com/fund-account)

## LearnWeb3 Flow Faucet[​](#learnweb3-flow-faucet "Direct link to LearnWeb3 Flow Faucet")

[LearnWeb3 Flow Faucet](https://learnweb3.io/faucets/flow) is a community faucet tool that provides a seamless way to acquire small amounts of Flow tokens for testing and development purposes on the Flow blockchain's testnet environment.

### Supported Networks[​](#supported-networks-1 "Direct link to Supported Networks")

* [Testnet](https://learnweb3.io/faucets/flow)

## Using Flow Faucet[​](#using-flow-faucet "Direct link to Using Flow Faucet")

### Funding Your Account[​](#funding-your-account "Direct link to Funding Your Account")

If you already have a Flow account, you can fund it directly from the Faucet's landing page. Simply paste the address of the account you want to fund, complete the CAPTCHA, and click "Fund Your Account."

![fund-your-account](/assets/images/faucet-fund-account-ed3185d3c12c70dc79f8a125d8faca7a.png)

After a few seconds, you'll see your account's FLOW balance as a confirmation. Note, the Faucet will automatically determine if the address you paste is a Flow or EVM address and will fund the account accordingly.

### Creating a Flow Account[​](#creating-a-flow-account "Direct link to Creating a Flow Account")

#### Generate a Key Pair[​](#generate-a-key-pair "Direct link to Generate a Key Pair")

To create a Flow-native account, you'll need to generate a key pair. You can do this most easily [Flow CLI](/build/cadence/getting-started/flow-cli) with the [`keys generate` command](/build/tools/flow-cli/keys/generate-keys)

`_10

flow keys generate`

You'll receive a private key and a public key pair with default `ECDSA_P256` signature and `SHA3_256` hash algorithms.

`_10

❯ flow keys generate

_10

_10

🔴️ Store private key safely and don't share with anyone!

_10

Private Key <PRIVATE_KEY>

_10

Public Key <PUBLIC_KEY>

_10

Mnemonic <MNEMONIC_PHRASE>

_10

Derivation Path m/44'/539'/0'/0/0

_10

Signature Algorithm ECDSA_P256`

You can then use the public key to create a new Flow account on the Faucet. Copy the resulting public key for the next step.

#### Create a Flow-Native Account[​](#create-a-flow-native-account "Direct link to Create a Flow-Native Account")

From the Faucet's landing page, click on the "Create Account" button. You'll be prompted to enter your public key. Paste the public key you generated using the Flow CLI and click "Create Account."

tip

Know that there is a distinction between Flow native accounts and EVM accounts. Native accounts allow you to interact with the Cadence runtime, while EVM accounts are used for interacting with Flow's EVM. To create an EVM account, you can use EVM tooling to generate an Ethereum Owned Account (EOA) and simply fund the associated address. Alternatively, you can create an EVM account controlled by your Flow native account - known as a Cadence Owned Account (COA) - in which case you'll need a Flow native account and should continue with the steps below.

For more information interacting with EVM via COAs, see the [Interacting With COAs documentation](/blockchain-development-tutorials/cross-vm-apps/interacting-with-coa).

![create-flow-account](/assets/images/faucet-create-account-996dcd971c6e6972d94e91962c14b278.png)

You can then paste your public key into the input field, complete the CAPTCHA, and click "Create Account."

![input-public-key](/assets/images/faucet-input-public-key-12430cae39c9b02e8b55c9530ce30d1f.png)

You'll be met with a confirmation screen, showing your Flow account address and the funded balance.

![account-created](/assets/images/faucet-account-created-f542db5bb38ac9b0fbc3f378a31a8bc7.png)

#### Using your Flow Account[​](#using-your-flow-account "Direct link to Using your Flow Account")

Once your account has been created, you can add the account to your `flow.json` configuration file under the `accounts` attribute, like so:

`_10

{

_10

"accounts": {

_10

"testnet-dev-account": {

_10

"address": "<YOUR_ADDRESS>",

_10

"key": "<PRIVATE_KEY>"

_10

}

_10

}

_10

}`

warning

If you plan on using your flow.json in a production environment, you'll want to look at alternative methods to manage your keys more securely, at minimum using environment variables instead of storing your account private keys in plain text. See [How to Securely Use CLI](/build/tools/flow-cli/flow.json/security) for more information on alternate key management strategies and how to configure them in your `flow.json` file.

After adding your account to your `flow.json` file, you're ready to use your account in your project. You can now deploy contracts, run transactions, and interact with the Flow blockchain using your new account.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/ecosystem/faucets.md)

Last updated on **Aug 21, 2025** by **Brian Doyle**

[Previous

Community Projects](/ecosystem/projects)[Next

Hackathons and Events](/ecosystem/Hackathons and Events)

###### Rate this page

😞😐😊

Copy as Markdown

* [Flow Faucet](#flow-faucet)
  + [Supported Networks](#supported-networks)
* [LearnWeb3 Flow Faucet](#learnweb3-flow-faucet)
  + [Supported Networks](#supported-networks-1)
* [Using Flow Faucet](#using-flow-faucet)
  + [Funding Your Account](#funding-your-account)
  + [Creating a Flow Account](#creating-a-flow-account)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/blockchain-development-tutorials/cadence/mobile)
* [FCL](/build/tools/clients/fcl-js)
* [Testing](/build/cadence/smart-contracts/testing)
* [CLI](/build/tools/flow-cli)
* [Emulator](/build/tools/emulator)
* [Dev Wallet](https://github.com/onflow/fcl-dev-wallet)
* [VS Code Extension](/build/tools/vscode-extension)

Community

* [Ecosystem](/ecosystem)
* [Flow Port](https://port.flow.com/)
* [Developer Grants](https://github.com/onflow/developer-grants)
* [Responsible Disclosure](https://flow.com/flow-responsible-disclosure)
* [Flowverse](https://www.flowverse.co/)
* [Emerald Academy](https://academy.ecdao.org/)
* [FLOATs (Attendance NFTs)](https://floats.city/)

Start Building

* [Flow Playground](https://play.flow.com/)
* [Cadence Tutorials](https://cadence-lang.org/docs/tutorial/first-steps)
* [Cadence Cookbook](https://cookbook.flow.com)
* [Core Contracts & Standards](/build/cadence/core-contracts)
* [EVM](/build/evm/about)

Network

* [Network Status](https://status.flow.com/)
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/protocol/node-ops/node-operation/past-upgrades)
* [Upcoming Sporks](/protocol/node-ops/node-operation/upcoming-sporks)
* [Node Operation](/protocol/node-ops)
* [Spork Information](/protocol/node-ops/node-operation/spork)

More

* [GitHub](https://github.com/onflow)
* [Discord](https://discord.gg/flow)
* [Forum](https://forum.flow.com/)
* [Flow](https://flow.com/)
* [Blog](https://flow.com/blog)

Copyright © 2025 Flow, Inc. Built with Docusaurus.