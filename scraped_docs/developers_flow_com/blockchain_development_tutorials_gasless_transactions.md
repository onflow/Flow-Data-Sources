# Source: https://developers.flow.com/blockchain-development-tutorials/gasless-transactions

Gasless Transactions | Flow Developer Portal



LLM Notice: This documentation site supports content negotiation for AI agents. Request any page with Accept: text/markdown or Accept: text/plain header to receive Markdown instead of HTML. Alternatively, append ?format=md to any URL. All markdown files are available at /md/ prefix paths. For all content in one file, visit /llms-full.txt

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

Flow is one of the easiest platforms for developers to onboard new users. Currently, the Flow Wallet automatically sponsors transactions on **both testnet and mainnet**. This allows developers to build seamless Web3 applications without requiring users to manage gas tokens or pay transaction fees.

In addition to native sponsorship, Flow also supports multiple methods for gas sponsorship that you can tailor to your application’s needs. You can learn about these approaches in more detail [here](https://developers.flow.com/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions).

The [Flow Wallet](https://wallet.flow.com/) currently sponsors all transactions - on testnet and mainnet! This is possible because [sponsored transactions](/build/cadence/advanced-concepts/account-abstraction#sponsored-transactions) are a native feature of the Flow Protocol. Additional methods for gas sponsorship are available and are described here.

## What You'll Learn[​](#what-youll-learn "Direct link to What You'll Learn")

In this tutorial series, you’ll discover how to:

* Configure and deploy a **gas free EVM endpoint** for your backend.
* Allow **gasless transactions** so that users can interact with your app without ever paying gas fees.
* Use Flow’s EVM Gateway service account to automatically cover gas fees for transactions, which ensures a smooth experience for your users.

## Tutorial for how to build on an EVM blockchain without Gas fees[​](#tutorial-for-how-to-build-on-an-evm-blockchain-without-gas-fees "Direct link to Tutorial for how to build on an EVM blockchain without Gas fees")

Learn how to set up a gas free EVM endpoint for your backend. All transactions sent through this endpoint aren't charged gas fees from the sender’s account. Instead, the EVM Gateway’s service account will sponsor the gas, which makes transactions completely **gasless for end users**.

Tutorial: [Gas Free EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/gasless-transactions/index.md)

Last updated on **Nov 12, 2025** by **Brian Doyle**

[Previous

Register ERC20 Token](/blockchain-development-tutorials/tokens/register-erc20-token)[Next

Sponsored Transactions EVM Endpoint](/blockchain-development-tutorials/gasless-transactions/sponsored-transactions-evm-endpoint)

###### Rate this page

😞😐😊

Copy as Markdown

* [What You'll Learn](#what-youll-learn)* [Tutorial for how to build on an EVM blockchain without Gas fees](#tutorial-for-how-to-build-on-an-evm-blockchain-without-gas-fees)

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