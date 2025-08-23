# Source: https://developers.flow.com/blockchain-development-tutorials/token-launch/register-cadence-assets

Register Your Assets on Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)[Tutorials](/blockchain-development-tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)
* [Flow Actions](/blockchain-development-tutorials/defi)
* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)
* [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)
* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)
* [Token Launch](/blockchain-development-tutorials/token-launch)

  + [Register ERC20 Token](/blockchain-development-tutorials/token-launch/register-erc20-token)
  + [Register Cadence Assets](/blockchain-development-tutorials/token-launch/register-cadence-assets)
* [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)
* [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)
* [FlowtoBooth](/blockchain-development-tutorials/flowtobooth)
* [Integrations](/blockchain-development-tutorials/integrations/crossmint)

* [Token Launch](/blockchain-development-tutorials/token-launch)
* Register Cadence Assets

On this page

# Register Your Assets on Flow

To make your fungible token or non-fungible token visible in Flow ecosystem projects like **Flow Wallet** and **IncrementFi**, you need to register it on the Flow Token List. This process will generate JSON files based on the Uniswap TokenList Standard and ensures that wallets, explorers, and onchain apps can recognize and display your token correctly.

There are two ways to register your token: **manually** via a web interface or **programmatically** during token deployment.

---

## Manual Registration (~1 min)[​](#manual-registration-1-min "Direct link to Manual Registration (~1 min)")

The following works for both fungible and non-fungible tokens on Flow Cadence or Flow EVM.

1. **Go to** [Token List Registration](https://token-list.fixes.world/).
2. **Enter your contract address** in the **"Quick Register"** field and press **Enter**.
   * Both Fungible and Non-Fungible tokens are supported.
   * Both EVM and Cadence contracts are supported.
3. **Click "Register"** and sign the transaction.
   * If your token is **already registered to VM Bridge**, you're done.
   * Otherwise, the **first transaction** registers the token to **VM Bridge** (costs **1 $FLOW**).
   * After that, click **"Register"** again and sign the **second transaction** to finalize the process.

warning

ERC-20 tokens registered with this method will use the default logo of Flow Official Assets.

If you want to register your ERC-20 token on Flow EVM with your customized logo, you should follow the [Register ERC-20 Token on Flow EVM](/blockchain-development-tutorials/token-launch/register-erc20-token) guide.

---

## Programmatic Registration[​](#programmatic-registration "Direct link to Programmatic Registration")

For seamless automation, you can integrate token registration into your token deployment workflow.

You can use the following Cadence transaction to register your Fungible or Non-Fungible token on Flow Cadence or Flow EVM.

### Register Fungible Token or Non-Fungible Token automatically on Flow Cadence[​](#register-fungible-token-or-non-fungible-token-automatically-on-flow-cadence "Direct link to Register Fungible Token or Non-Fungible Token automatically on Flow Cadence")

Use a standalone Cadence transaction to register your Fungible Token or Non-Fungible Token on Flow Cadence.

* Use this **Cadence transaction**: [register-standard-asset.cdc](https://github.com/fixes-world/token-list/blob/main/cadence/transactions/register-standard-asset.cdc).
* This transaction should be executed **right after deploying your Fungible Token or Non-Fungible Token contract**.

Or you can also pick up some code from the [register-standard-asset.cdc](https://github.com/fixes-world/token-list/blob/main/cadence/transactions/register-standard-asset.cdc) file to make your own Cadence transaction with the same logic for more seamless integration. Here is an example:

`_15

import "TokenList"

_15

import "NFTList"

_15

_15

transaction(

_15

address: Address,

_15

contractName: String,

_15

) {

_15

execute {

_15

if TokenList.isValidToRegister(address, contractName) {

_15

TokenList.ensureFungibleTokenRegistered(address, contractName)

_15

} else if NFTList.isValidToRegister(address, contractName) {

_15

NFTList.ensureNFTCollectionRegistered(address, contractName)

_15

}

_15

}

_15

}`

### Register ERC-20 or ERC-721 Tokens automatically on Flow EVM[​](#register-erc-20-or-erc-721-tokens-automatically-on-flow-evm "Direct link to Register ERC-20 or ERC-721 Tokens automatically on Flow EVM")

* Use this **Cadence transaction**: [register-evm-asset.cdc](https://github.com/fixes-world/token-list/blob/main/cadence/transactions/register-evm-asset.cdc)
* This transaction should be executed **right after deploying your ERC-20 or ERC-721 contract**.

warning

Similar to manual registration:

* If the token **is not bridged** to **VM Bridge**, you will need to **send the transaction twice**.
* The **first transaction** deploys a **VM Bridged Cadence contract** for the ERC-20.
* The **second transaction** registers it on the Token List.

---

### Next Steps[​](#next-steps "Direct link to Next Steps")

* Verify your token listing in Flow Wallet.

For any issues, refer to the [Token List GitHub Repository](https://github.com/fixes-world/token-list) or reach out to the [Flow developer community](https://discord.gg/flow).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/token-launch/register-cadence-assets.md)

Last updated on **Aug 17, 2025** by **0xLisanAlGaib**

[Previous

Register ERC20 Token](/blockchain-development-tutorials/token-launch/register-erc20-token)[Next

Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

###### Rate this page

😞😐😊

Copy as Markdown

* [Manual Registration (~1 min)](#manual-registration-1-min)
* [Programmatic Registration](#programmatic-registration)
  + [Register Fungible Token or Non-Fungible Token automatically on Flow Cadence](#register-fungible-token-or-non-fungible-token-automatically-on-flow-cadence)
  + [Register ERC-20 or ERC-721 Tokens automatically on Flow EVM](#register-erc-20-or-erc-721-tokens-automatically-on-flow-evm)
  + [Next Steps](#next-steps)

Documentation

* [Getting Started](/build/cadence/getting-started/contract-interaction)
* [Tools & SDKs](/build/tools)
* [Cadence](https://cadence-lang.org/docs/)
* [Mobile](/build/cadence/guides/mobile/overview)
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