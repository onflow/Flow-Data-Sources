# Source: https://developers.flow.com/tutorials/token-launch/register-erc20-token

Register Your ERC20 Token on Flow EVM | Flow Developer Portal



[Skip to main content](#__docusaurus_skipToContent_fallback)

[![Flow Developer Portal Logo](/img/flow-docs-logo-dark.png)![Flow Developer Portal Logo](/img/flow-docs-logo-light.png)](/)[Cadence](/build/flow)[EVM](/evm/about)[Tools](/tools/kit)[Networks](/networks/flow-networks)[Ecosystem](/ecosystem)[Growth](/growth)[Tutorials](/tutorials)

Sign In[![GitHub]()Github](https://github.com/onflow)[![Discord]()Discord](https://discord.gg/flow)

Search

* [Tutorials](/tutorials)
* [AI Plus Flow](/tutorials/ai-plus-flow)
* [Token Launch](/tutorials/token-launch)

  + [Register ERC20 Token](/tutorials/token-launch/register-erc20-token)
  + [Register Cadence Assets](/tutorials/token-launch/register-cadence-assets)
* [Cross-VM Apps](/tutorials/cross-vm-apps)
* [FlowtoBooth](/tutorials/flowtobooth)
* [Native VRF](/tutorials/native-vrf)

* [Token Launch](/tutorials/token-launch)
* Register ERC20 Token

On this page

# Register Your ERC20 Token on Flow EVM

## Overview[​](#overview "Direct link to Overview")

This section covers the process of registering your ERC20 token on Flow EVM via a Github Pull Request process so it appears in Flow standard Token List which is used by Flow Wallet, MetaMask, and other ecosystem apps.

We will use the [Flow Official Assets](https://github.com/onflow/assets) repository as the standard token list repository for updating the token list for the whole Flow ecosystem.  
The repository is open to the public and you can submit your PRs to add your token to the list.

Note: The logic of the registration is based on the [Register Assets in Cadence](/tutorials/token-launch/register-cadence-assets) backend process.

## Guides for submitting your PRs[​](#guides-for-submitting-your-prs "Direct link to Guides for submitting your PRs")

Steps to submit your PRs:

1. **Fork the [Flow Official Assets](https://github.com/onflow/assets) repository**
   * Click the `Fork` button in the top right corner of the repository.
   * Create a new fork of the repository in your own Github account.
2. **Create a new branch**
   * Clone your forked repository to your local development environment by `git clone https://github.com/your-github-username/assets`
   * Create a new branch for your token by `git checkout -b new-token-branch`
3. **Add/Update your token to the list**
   * For new Tokens:
     + Create the token folders in the `tokens/registry` directory.
     + The name of the token folders must be the same as the token's contract address.
       - e.g. `tokens/registry/0x1234567890123456789012345678901234567890`
       - for Testnet tokens, the folder should be `tokens/registry/testnet:0x1234567890123456789012345678901234567890`
     + Put the required metadata file in the token folder, at least one of the following files should be included:
       - `logo.png`: PNG format token logo (256x256px recommended)
       - `logo.svg`: SVG format token logo, optimized and viewboxed
     + You can also add extra optional metadata file:
       - `mods.json`: Mods JSON file for token metadata, you can adjust the `symbol`, `name`, `description` for the final output in the `token.json` file.
   * For existing Tokens:
     + Identify the token folder in the `tokens/registry` directory by the token's contract address.
     + Update the token metadata in the `tokens/registry/${token_address}` directory.
4. **Submit a Pull Request**
   * Commit your changes and push to your forked repository.
   * Create a new Pull Request for your changes in the [Flow Official Assets](https://github.com/onflow/assets) repository.
   * A Github Action will be triggered to verify the on-chain status of the token and update the report in the PR's comment.
     + If there is any issue, you will see some warnings and suggestions in the PR's comment. Please check the report and update the token metadata if needed.
     + You may see a comment from the Github Action that you need to send 1 $FLOW to the registry address for the token registration because there is a VM Bridge onboarding fee.

Learn more about the registration process in the [Assets Registry](https://github.com/onflow/assets/tree/main/tokens) README.md file of the repository.

## What's next?[​](#whats-next "Direct link to What's next?")

After submitting your PR, you just need to wait for the Flow team to review your token and merge your PR.  
Once the PR is merged, your token will be registered by the Github Actions in the [Flow Official Assets](https://github.com/onflow/assets) repository automatically and a new PR will be created automatically by Github Actions to update the token list. The Flow team will regularly merge the token list updates PR to the main branch.

## How to verify the token is registered?[​](#how-to-verify-the-token-is-registered "Direct link to How to verify the token is registered?")

As the registration and token list generation is executed by Github Actions, you can check the status of the PRs and the token list JSON files in the [Flow Official Assets](https://github.com/onflow/assets) repository.  
Here are the URLs for the token list JSON files:

* Mainnet: `https://raw.githubusercontent.com/onflow/assets/refs/heads/main/tokens/outputs/mainnet/token-list.json`
* Testnet: `https://raw.githubusercontent.com/onflow/assets/refs/heads/main/tokens/outputs/testnet/token-list.json`

You can check the token list JSON files to verify the token is registered in the `token-list.json` file.

[Edit this page](https://github.com/onflow/docs/tree/main/docs/tutorials/token-launch/register-erc20-token.md)

Last updated on **Apr 25, 2025** by **Brian Doyle**

[Previous

Token Launch](/tutorials/token-launch)[Next

Register Cadence Assets](/tutorials/token-launch/register-cadence-assets)

###### Rate this page

😞😐😊

Copy as Markdown

* [Overview](#overview)
* [Guides for submitting your PRs](#guides-for-submitting-your-prs)
* [What's next?](#whats-next)
* [How to verify the token is registered?](#how-to-verify-the-token-is-registered)

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
* [Flowscan Mainnet](https://flowscan.io/)
* [Flowscan Testnet](https://testnet.flowscan.io/)
* [Past Sporks](/networks/node-ops/node-operation/past-upgrades)
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