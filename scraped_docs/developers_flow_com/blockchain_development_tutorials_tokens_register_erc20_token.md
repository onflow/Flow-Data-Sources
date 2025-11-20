# Source: https://developers.flow.com/blockchain-development-tutorials/tokens/register-erc20-token

Register Your ERC20 Token on Flow EVM | Flow Developer Portal



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

                  + [Creating a Fungible Token](/blockchain-development-tutorials/tokens/fungible-token-cadence)+ [Creating an NFT Contract](/blockchain-development-tutorials/tokens/nft-cadence)+ [Register Cadence Assets](/blockchain-development-tutorials/tokens/register-cadence-assets)+ [Register ERC20 Token](/blockchain-development-tutorials/tokens/register-erc20-token)* [Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

                    * [Third-Party Integrations](/blockchain-development-tutorials/integrations)

* * [Token Development and Registration](/blockchain-development-tutorials/tokens)* Register ERC20 Token

On this page

# Register Your ERC20 Token on Flow EVM

## Overview[​](#overview "Direct link to Overview")

This section covers how to register your ERC20 token on Flow EVM via a Github Pull Request process so it appears in Flow standard Token List, which Flow Wallet, MetaMask, and other ecosystem apps use.

We will use the [Flow Official Assets](https://github.com/onflow/assets) repository as the standard token list repository to update the token list for the whole Flow ecosystem. The repository is open to the public and you can submit your PRs to add your token to the list.

info

The logic of the registration is based on the [Register Assets in Cadence](/blockchain-development-tutorials/tokens/register-cadence-assets) backend process.

## Guides for how to submit your PRs[​](#guides-for-how-to-submit-your-prs "Direct link to Guides for how to submit your PRs")

Steps to submit your PRs:

1. **Fork the [Flow Official Assets](https://github.com/onflow/assets) repository**
   * Click `Fork` in the top right corner of the repository.
   * Create a new fork of the repository in your own Github account.
2. **Create a new branch**
   * Clone your forked repository to your local development environment by `git clone https://github.com/your-github-username/assets`
   * Create a new branch for your token by `git checkout -b new-token-branch`
3. **Add or update your token to the list**
   * For new Tokens:
     + Create the token folders in the `tokens/registry` directory.
     + The name of the token folders must be the same as the token's contract address.
       - For example, `tokens/registry/0x1234567890123456789012345678901234567890`
       - for Testnet tokens, the folder should be `tokens/registry/testnet:0x1234567890123456789012345678901234567890`
     + Put the required metadata file in the token folder, include at least one of the following files:
       - `logo.png`: PNG format token logo (256x256px recommended)
       - `logo.svg`: SVG format token logo, optimized and viewboxed
     + You can also add extra optional metadata file:
       - `mods.json`: Mods JSON file for token metadata, you can adjust the `symbol`, `name`, `description` for the final output in the `token.json` file.
   * For current Tokens:
     + Identify the token folder in the `tokens/registry` directory by the token's contract address.
     + Update the token metadata in the `tokens/registry/${token_address}` directory.
4. **Submit a Pull Request**
   * Commit your changes and push to your forked repository.
   * Create a new Pull Request (PR) for your changes in the [Flow Official Assets](https://github.com/onflow/assets) repository.
   * A Github Action will be triggered to verify the onchain status of the token and update the report in the PR's comment.
     + If there is any issue, you will see some warnings and suggestions in the PR's comment. Check the report and update the token metadata if needed.
     + You may see a comment from the Github Action that you need to send 1 $FLOW to the registry address for the token registration because there is a VM Bridge onboarding fee.

Learn more about the registration process in the [Assets Registry](https://github.com/onflow/assets/tree/main/tokens) README.md file of the repository.

## What's next?[​](#whats-next "Direct link to What's next?")

After you submit your PR, you just need to wait for the Flow team to review your token and merge your PR.

After the PR is merged, your token will be registered by the Github Actions in the [Flow Official Assets](https://github.com/onflow/assets) repository automatically and Github Actions automatically creates a new PR to update the token list. The Flow team will regularly merge the token list updates PR to the main branch.

## How to verify the token is registered[​](#how-to-verify-the-token-is-registered "Direct link to How to verify the token is registered")

As Github Actions executes the registration and token list generation, you can check the status of the PRs and the token list JSON files in the [Flow Official Assets](https://github.com/onflow/assets) repository.  
Here are the URLs for the token list JSON files:

* Mainnet: `https://raw.githubusercontent.com/onflow/assets/refs/heads/main/tokens/outputs/mainnet/token-list.json`
* Testnet: `https://raw.githubusercontent.com/onflow/assets/refs/heads/main/tokens/outputs/testnet/token-list.json`

You can check the token list JSON files to verify the token is registered in the `token-list.json` file.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/blockchain-development-tutorials/tokens/register-erc20-token.md)

Last updated on **Nov 18, 2025** by **cshannon1218**

[Previous

Register Cadence Assets](/blockchain-development-tutorials/tokens/register-cadence-assets)[Next

Gasless Transactions](/blockchain-development-tutorials/gasless-transactions)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)* [Guides for how to submit your PRs](#guides-for-how-to-submit-your-prs)* [What's next?](#whats-next)* [How to verify the token is registered](#how-to-verify-the-token-is-registered)

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