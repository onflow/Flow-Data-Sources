# Source: https://developers.flow.com/blockchain-development-tutorials/gasless-transactions

Gasless Transactions | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Build](/build/flow)[Tutorials](/blockchain-development-tutorials)[Protocol](/protocol/flow-networks)[Ecosystem](/ecosystem)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Blockchain Development Tutorials](/blockchain-development-tutorials)* [Flow Blockchain 101](/blockchain-development-tutorials/flow-101)* [Forte Network Upgrade](/blockchain-development-tutorials/forte)

      * [Use AI To Build On Flow](/blockchain-development-tutorials/use-AI-to-build-on-flow)

        * [Cadence Tutorials](/blockchain-development-tutorials/cadence)

          * [Flow EVM Guides](/blockchain-development-tutorials/evm)

            * [Cross-VM Apps](/blockchain-development-tutorials/cross-vm-apps)

              * [Native VRF (Built-in Randomness) Tutorials](/blockchain-development-tutorials/native-vrf)

                * [Token Development and Registration](/blockchain-development-tutorials/tokens)

                  * [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    + [Sponsored Transactions EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)* [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * Gasless Transactions

On this page

# Gasless Transactions on Flow

Flow is a **blockchain with no gas fees for end users**, making it one of the easiest platforms for developers to onboard new users. **Gasless transactions** are a native feature of the Flow Protocol: the Flow Wallet automatically sponsors transactions on both testnet and mainnet. This allows developers to build seamless Web3 applications without requiring users to manage gas tokens or pay transaction fees.

In addition to native sponsorship, Flow also supports multiple methods for gas sponsorship that can be tailored to your application’s needs. You can learn about these approaches in more detail [here](https://developers.flow.com/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions).

The [Flow Wallet](https://wallet.flow.com/) currently sponsors all transactions - on testnet and mainnet! This is possible because [sponsored transactions](/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions) are a native feature of the Flow Protocol. Additional methods for gas sponsorship are available and are described here.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

In this tutorial series, you’ll discover how to:

* Configure and deploy a **gas free EVM endpoint** for your backend
* Enable **gasless transactions** so that users can interact with your app without ever paying gas fees.
* Use Flow’s EVM Gateway service account to automatically cover gas fees for transactions, ensuring a smooth experience for your users.

## Tutorial for building on an EVM blockchain without Gas fees[​](#tutorial-for-building-on-an-evm-blockchain-without-gas-fees "Direct link to Tutorial for building on an EVM blockchain without Gas fees")

Learn how to set up a gas free EVM endpoint for your backend. All transactions sent through this endpoint will not be charged gas fees from the sender’s account. Instead, the EVM Gateway’s service account will sponsor the gas, making transactions completely **gasless for end users**.

Tutorial: [Gas Free EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/gasless-transactions/index.md)

Last updated on **Sep 12, 2025** by **Vishal**

[Previous

Register ERC20 Token](/blockchain-development-tutorials/tokens/register-erc20-token)[Next

Sponsored Transactions EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [Tutorial for building on an EVM blockchain without Gas fees](#tutorial-for-building-on-an-evm-blockchain-without-gas-fees)

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