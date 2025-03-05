# Source: https://developers.flow.com/tutorials/token-launch/register-token

Register Your Token on Flow | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/flow-cli)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [Token Launch](/tutorials/token-launch)

  + [Register Token](/tutorials/token-launch/register-token)
* [Cross-VM App](/tutorials/cross-vm-apps)

* [Token Launch](/tutorials/token-launch)
* Register Token

On this page

# Register Your Token on Flow

To make your token visible in Flow ecosystem projects like **Flow Wallet** and **IncrementFi**, you need to register it on the Flow Token List. This process will generate JSON files based on Uniswap TokenList Standard and ensures that wallets, explorers, and onchain apps can recognize and display your token correctly.

There are two ways to register your token: **manually** via a web interface or **programmatically** during token deployment.

---

## Manual Registration (~1 min)[​](#manual-registration-1-min "Direct link to Manual Registration (~1 min)")

The following works for both fungible tokens on Flow Cadence and ERC20 tokens on Flow EVM.

1. **Go to** [Token List Registration](https://token-list.fixes.world/).
2. **Enter your contract address** in the **"Quick Register"** field and press **Enter**.
3. **Click "Register"** and sign the transaction.
   * If your token is **already registered to VM Bridge**, you're done.
   * Otherwise, the **first transaction** registers the token to **VM Bridge** (costs **1 $FLOW**).
   * After that, click **"Register"** again and sign the **second transaction** to finalize the process.

---

## Programmatic Registration (~1-2 hrs)[​](#programmatic-registration-1-2-hrs "Direct link to Programmatic Registration (~1-2 hrs)")

For seamless automation, you can integrate token registration into your token deployment workflow.

### Register ERC-20 Tokens automatically on Flow EVM[​](#register-erc-20-tokens-automatically-on-flow-evm "Direct link to Register ERC-20 Tokens automatically on Flow EVM")

* Use this **Cadence transaction**: [register-evm-asset.cdc](https://github.com/fixes-world/token-list/blob/main/cadence/transactions/register-evm-asset.cdc)
* This transaction should be executed **right after deploying your ERC-20 contract**.
* **Note:** Similar to manual registration:
  + If the token **is not bridged** to **VM Bridge**, you will need to **send the transaction twice**.
  + The **first transaction** deploys a **VM Bridged Cadence contract** for the ERC-20.
  + The **second transaction** registers it on the Token List.

---

### Next Steps[​](#next-steps "Direct link to Next Steps")

* Verify your token listing in Flow Wallet.

For any issues, refer to the [Token List GitHub Repository](https://github.com/fixes-world/token-list) or reach out to the [Flow developer community](https://discord.gg/flow).

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/token-launch/register-token.md)

Last updated on **Feb 24, 2025** by **j pimmel**

[Previous

Token Launch](/tutorials/token-launch)[Next

Cross-VM App](/tutorials/cross-vm-apps)

###### Rate this page

😞😐😊

* [Manual Registration (~1 min)](#manual-registration-1-min)
* [Programmatic Registration (~1-2 hrs)](#programmatic-registration-1-2-hrs)
  + [Register ERC-20 Tokens automatically on Flow EVM](#register-erc-20-tokens-automatically-on-flow-evm)
  + [Next Steps](#next-steps)

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